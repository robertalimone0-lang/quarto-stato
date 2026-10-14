"""Modello del quadro finanziario del programma Quarto Stato.

Legge la tabella unica delle coperture (coperture.csv), i costi di Fase 1 (misure.csv),
le leve di entrata (leve.csv) e la coda di attivazione (coda.csv). Valori in miliardi
di euro correnti. Anni 2027-2035: legislatura 2027-2031, poi valori a regime.

Regole applicate (CLAUDE.md):
- scenari per voce con tassi di realizzazione e rampe; costi +5% nel prudente, +10% nell'avverso;
- lo scenario prudente chiude ogni anno con margine >= 0: la Priorita 2 impegnata e il minimo
  tra fabbisogno e busta prudente presente e futura;
- Priorita 2 del 2027 dal 1 luglio, cofinanziamento degli investimenti dal 2028;
- coda: certificazione trimestrale (media di quattro trimestri, quindi anni Y-1 e Y-2),
  soglia 110% del costo a regime, scorrimento con prenotazione del 50%;
- la coda si copre prima con il 50% dell'eccedenza delle coperture sul prudente, poi con le leve;
  sul gettito delle leve rimasto libero vale la regola 50% IRPEF, 30% debito, 20% riserva.

Varianti: quadro(variante) ricalcola tutto il quadro con ipotesi diverse, senza toccare i CSV.
La variante e un dizionario:
  {"costanti": {"SOGLIA": 1.2, ...},
   "tabelle": {"coda": {"modifica": {"Q16": {"costo_regime": 0.34, "dopo": ""}},
                        "aggiungi": [{"riga": {...}, "prima_di": "Q15"}],
                        "togli": ["Q14"]}}}
Tabelle: coperture, misure, leve, coda, riserva, dpfp (chiave di riga: codice; dpfp: quadro+anno;
riserva: gradino). Senza variante il quadro coincide con il quadro del programma, e le funzioni
del modulo (M.copertura, M.P2, M.simula_coda, ...) restano quelle del quadro del programma.
"""
from pathlib import Path
import copy
import csv

DIR = Path(__file__).resolve().parent
Y = list(range(2027, 2036))
SC = ["centrale", "prudente", "avverso"]

COSTANTI = dict(
    MULT={"centrale": 1.00, "prudente": 1.05, "avverso": 1.10, "alta": 1.00},
    SOGLIA=1.10, PRENOTAZIONE=0.50, QUOTA_ECCEDENZA=0.50,
    RIPARTIZIONE_LEVE={"irpef": 0.50, "debito": 0.30, "riserva": 0.20},  # gettito delle leve rimasto libero
    AVVIO_P2_2027=0.5,  # Priorita 2 del 2027 dal 1 luglio
    CRESCITA_PIL_DOPO_2029=1.026,  # ipotesi: crescita nominale invariata al livello 2029
    RICONOSCIMENTO_R1=3.85,  # quota della Riforma 1 riconosciuta in via prudente come misure discrezionali (D20)
    RAMPA_EV="2028:0.25;2029:0.5;2030:0.75;2031:1",
)
TABELLE = {"coperture": "coperture.csv", "misure": "misure.csv", "leve": "leve.csv",
           "coda": "coda.csv", "dpfp": "dpfp_2026.csv", "riserva": "riserva.csv"}


def _csv(nome):
    with open(DIR / nome, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def rampa(testo):
    """'2027:0.5;2028:1' -> valore per anno; 0 prima del primo anno, costante dopo l'ultimo."""
    punti = sorted((int(a), float(b)) for a, b in (p.split(":") for p in testo.split(";")))
    out, v = {}, 0.0
    for y in Y:
        for a, b in punti:
            if a <= y:
                v = b
        out[y] = v
    return out


def _chiave(tabella, r):
    if tabella == "dpfp":
        return f'{r["quadro"]}:{r["anno"]}'
    if tabella == "riserva":
        return r["gradino"]
    return r["codice"]


def _applica(tabella, righe, mod):
    """Applica a una tabella le modifiche della variante: modifica, togli, aggiungi."""
    righe = [dict(r) for r in righe]
    for k, campi in mod.get("modifica", {}).items():
        trovate = [r for r in righe if _chiave(tabella, r) == k]
        if not trovate:
            raise KeyError(f"variante: {tabella} senza la riga {k}")
        for campo, valore in campi.items():
            if campo not in trovate[0]:
                raise KeyError(f"variante: {tabella} senza il campo {campo}")
            trovate[0][campo] = str(valore)
    togli = set(mod.get("togli", []))
    righe = [r for r in righe if _chiave(tabella, r) not in togli]
    for nuova in mod.get("aggiungi", []):
        riga = {c: "" for c in righe[0]} if righe else {}
        riga.update({c: str(v) for c, v in nuova["riga"].items()})
        prima = nuova.get("prima_di")
        i = next((j for j, r in enumerate(righe) if _chiave(tabella, r) == prima), len(righe))
        righe.insert(i, riga)
    return righe


class Quadro:
    """Quadro finanziario completo per una variante delle ipotesi (None = quadro del programma)."""

    def __init__(self, variante=None):
        self.variante = copy.deepcopy(variante or {})
        c = copy.deepcopy(COSTANTI)
        for k, v in self.variante.get("costanti", {}).items():
            if k not in c:
                raise KeyError(f"variante: costante {k} inesistente")
            c[k] = v
        self.Y, self.SC = Y, SC
        self.MULT, self.SOGLIA = c["MULT"], c["SOGLIA"]
        self.PRENOTAZIONE, self.QUOTA_ECCEDENZA = c["PRENOTAZIONE"], c["QUOTA_ECCEDENZA"]
        self.RIPARTIZIONE_LEVE, self.AVVIO_P2_2027 = c["RIPARTIZIONE_LEVE"], c["AVVIO_P2_2027"]
        self.RICONOSCIMENTO_R1 = c["RICONOSCIMENTO_R1"]
        self._RAMPA_EV = rampa(c["RAMPA_EV"])

        tab = {k: _applica(k, _csv(f), self.variante.get("tabelle", {}).get(k, {})) for k, f in TABELLE.items()}
        self.COPERTURE, self.MISURE, self.LEVE = tab["coperture"], tab["misure"], tab["leve"]
        self.CODA, self.DPFP, self.RISERVA = tab["coda"], tab["dpfp"], tab["riserva"]

        self.PIL = {int(r["anno"]): float(r["pil_nominale_mld"]) for r in self.DPFP if r["quadro"] == "tendenziale"}
        for y in range(2030, 2036):
            self.PIL[y] = self.PIL[y - 1] * c["CRESCITA_PIL_DOPO_2029"]

        self.BUSTA = {y: (self.copertura("prudente", y) - self.p1(y) * self.MULT["prudente"]) / self.MULT["prudente"]
                      for y in Y}
        self.P2_PIENA = {y: max(0.0, min(self.p2_fabbisogno(y), min(self.BUSTA[u] for u in Y if u >= y))) for y in Y}
        self._cof = next(r for r in self.MISURE if r["codice"] == "M08")
        _cof_rinviato = float(next(v for v in self.CODA if v["codice"] == "Q09")["costo_regime"])
        self._cof_fase1 = float(self._cof["costo_regime"]) - _cof_rinviato  # quota del cofinanziamento rimasta in Fase 1
        _cof_2027 = self._cof_fase1 * rampa(self._cof["rampa"])[2027] * self.P2_PIENA[2027] / self.p2_fabbisogno(2027)
        self.P2 = dict(self.P2_PIENA)
        self.P2[2027] = self.AVVIO_P2_2027 * (self.P2_PIENA[2027] - _cof_2027)  # dal 1 luglio 2027, cofinanziamento dal 2028
        self.P2_RINVIATA = self.p2_fabbisogno(2031) - self.P2[2031]
        self._TARDIVE = [r for r in self.MISURE if r["priorita"] == "2"
                         and min(int(p.split(":")[0]) for p in r["rampa"].split(";")) >= 2028]

    # ---------------- coperture di Fase 1 ----------------
    @staticmethod
    def _sc(s):
        return "centrale" if s == "alta" else s

    def copertura(self, s, y, solo_p1=False):
        t = 0.0
        for r in self.COPERTURE:
            if solo_p1 and r["ammessa_priorita_1"] != "si":
                continue
            t += float(r["nominale"]) * float(r[f"tasso_{self._sc(s)}"]) * rampa(r["rampa"])[y]
        return t

    def per_classe(self, s, y):
        out = {}
        for r in self.COPERTURE:
            v = float(r["nominale"]) * (float(r[f"tasso_{self._sc(s)}"]) if s != "nominale" else 1) * rampa(r["rampa"])[y]
            out[r["classe"]] = out.get(r["classe"], 0.0) + v
        return out

    def costo(self, priorita, y):
        return sum(float(r["costo_regime"]) * rampa(r["rampa"])[y] for r in self.MISURE if r["priorita"] == str(priorita))

    def p1(self, y):
        return self.costo(1, y)

    def p2_fabbisogno(self, y):
        return self.costo(2, y)

    def costo_fase1(self, s, y):
        return (self.p1(y) + self.P2[y]) * self.MULT[s]

    def margine_fase1(self, s, y):
        return self.copertura(s, y) - self.costo_fase1(s, y)

    def eccedenza(self, s, y):
        return max(0.0, self.copertura(s, y) - self.copertura("prudente", y))

    # ---------------- leve e coda ----------------
    def leva(self, s, y, tipo=("fiscale", "risparmio"), confronto=False):
        tipi = set(tipo) | ({"confronto"} if confronto else set())
        return sum(float(r[s]) * rampa(r["rampa"])[y] for r in self.LEVE if r["tipo"] in tipi)

    @staticmethod
    def _cert(d, y):
        return (d.get(y - 1, 0.0) + d.get(y - 2, 0.0)) / 2

    @staticmethod
    def _profilo(voce, k):
        if voce["profilo"] == "capitale_umano":
            f = min(1.0, (k + 1) / 7)
            return 0.685 * f + 0.55 * f + 0.10
        p = [float(x) for x in voce["profilo"].split(";")]
        return float(voce["costo_regime"]) * p[min(k, len(p) - 1)]

    def _fonte_ok(self, voce, s, y, costo):
        """Voci legate a una leva (colonna fonte): il gettito certificato di quella leva deve coprire il costo con la soglia."""
        f = voce.get("fonte", "")
        if not f:
            return True
        r = next(x for x in self.LEVE if x["codice"] == f)
        g = {a: float(r[s]) * rampa(r["rampa"])[a] for a in Y}
        return self._cert(g, y) >= self.SOGLIA * costo

    def simula_coda(self, s, confronto=False):
        g = {y: self.leva(s, y, confronto=confronto) for y in Y}
        x = {y: self.eccedenza(s, y) for y in Y}
        attiva, impegnato, prenotato, stato = {}, 0.0, 0.0, {}
        for y in Y:
            risorse = self._cert(g, y) + self.QUOTA_ECCEDENZA * self._cert(x, y)
            libero = risorse - impegnato - prenotato
            while True:
                resto = [v for v in self.CODA if v["codice"] not in attiva
                         and (not v.get("dopo") or v["dopo"] in attiva)]  # colonna dopo: voce attivabile solo dopo un'altra
                if not resto:
                    break
                c0 = float(resto[0]["costo_regime"]) * self.MULT[s]
                if not self._fonte_ok(resto[0], s, y, c0):
                    break
                if prenotato + libero >= self.SOGLIA * c0:
                    attiva[resto[0]["codice"]] = y
                    impegnato += c0
                    libero, prenotato = libero + prenotato - c0, 0.0
                    continue
                nuova = self.PRENOTAZIONE * max(0.0, libero)
                prenotato += nuova
                disp = libero - nuova
                for v in resto[1:]:
                    c = float(v["costo_regime"]) * self.MULT[s]
                    if disp >= self.SOGLIA * c and self._fonte_ok(v, s, y, c):
                        attiva[v["codice"]] = y
                        impegnato += c
                        disp -= c
                break
            stato[y] = dict(risorse=risorse, impegnato=impegnato, prenotato=prenotato)
        return attiva, g, x, stato

    def costo_coda(self, s, attiva, y):
        t = 0.0
        for v in self.CODA:
            a = attiva.get(v["codice"])
            if a is not None and y >= a:
                t += self._profilo(v, y - a) * self.MULT[s]
        return t

    def flussi(self, s, confronto=False):
        """Effetto annuo sul saldo primario rispetto al tendenziale, in miliardi."""
        attiva, g, x, st = self.simula_coda(s, confronto)
        out = {}
        for y in Y:
            usato_leve = max(0.0, st[y]["impegnato"] + st[y]["prenotato"] - self.QUOTA_ECCEDENZA * self._cert(x, y))
            irpef = self.RIPARTIZIONE_LEVE["irpef"] * max(0.0, self._cert(g, y) - usato_leve)
            contributi = self.leva(s, y, tipo=("contributiva", "una_tantum"))
            cc = self.costo_coda(s, attiva, y)
            m1 = self.margine_fase1(s, y)
            out[y] = dict(margine_fase1=m1, leve=g[y], coda=cc, irpef=irpef, contributi=contributi,
                          saldo=m1 + g[y] - cc - irpef + contributi)
        return attiva, out

    # ---------------- clausola di salvaguardia (scenario avverso) ----------------
    def salvaguardia(self, primo=2028):
        s, righe = "avverso", {}
        base_p2, base_p1 = 0.0, self.p1(primo - 1)  # nello scenario avverso la Priorita 2 del 2027 non e mai partita
        for y in Y:
            buco = self.margine_fase1(s, y)
            if buco >= 0:
                righe[y] = dict(buco=buco, g1=0.0, g2=0.0, g3=0.0, g4=0.0, residuo=0.0)
                continue
            if y < primo:  # primo anno: la Priorita 2 di luglio non parte (gradino 2), poi rinvio dei nuovi ingressi P1 (gradino 4)
                g2 = min(-buco, self.P2[y] * self.MULT[s])
                g4 = min(-buco - g2, self.p1(y) * self.MULT[s])
                righe[y] = dict(buco=buco, g1=0.0, g2=g2, g3=0.0, g4=g4, residuo=min(0.0, buco + g2 + g4))
                continue
            tardive = (sum(float(r["costo_regime"]) * rampa(r["rampa"])[y] for r in self._TARDIVE)
                       * self.P2[y] / self.p2_fabbisogno(y) * self.MULT[s])
            cap = [0.0, tardive, max(0.0, (self.P2[y] - base_p2) * self.MULT[s] - tardive),
                   max(0.0, (self.p1(y) - base_p1) * self.MULT[s])]
            bisogno, usati = -buco, []
            for c in cap:
                u = min(c, max(0.0, bisogno))
                usati.append(u)
                bisogno -= u
            righe[y] = dict(buco=buco, g1=usati[0], g2=usati[1], g3=usati[2], g4=usati[3], residuo=-max(0.0, bisogno))
        return righe

    def sanita_pil(self, s, attiva, y, base=6.4):
        extra = sum(self._profilo(v, y - attiva[v["codice"]]) * self.MULT[s] for v in self.CODA
                    if v["codice"] in ("Q07", "Q08") and v["codice"] in attiva and y >= attiva[v["codice"]])
        return base + 100 * (11.0 * self.MULT[s] + extra) / self.PIL[y]

    # ---------------- percorso di spesa netta e riserva condizionata (D19, D20, D22) ----------------
    def _cofinanziamento_fase1(self, y):
        """Cofinanziamento di programmi UE, escluso dalla spesa netta (quota di Fase 1, dal 2028)."""
        if y <= 2027:
            return 0.0
        return self._cof_fase1 * rampa(self._cof["rampa"])[y] * (self.P2[y] / self.p2_fabbisogno(y))

    def scarto_spesa_netta(self, s, y, riconoscimento=False):
        """Coperture valide ai fini UE meno spesa di Fase 1 rilevante per la spesa netta (miliardi)."""
        spesa = self.costo_fase1(s, y) - self._cofinanziamento_fase1(y) * self.MULT[s]
        if riconoscimento:
            valide = self.copertura(s, y)
        else:
            valide = sum(float(r["nominale"]) * float(r[f"tasso_{self._sc(s)}"]) * rampa(r["rampa"])[y]
                         * float(r["quota_ue_senza_riconoscimento"]) for r in self.COPERTURE)
            valide += self.RICONOSCIMENTO_R1 * self._RAMPA_EV[y]
        return valide - spesa

    def gradini(self, s, curva_bonus):
        """Copertura dei gradini della riserva nella variante senza riconoscimento. curva_bonus: {anno: miliardi}."""
        out = {}
        for y in Y:
            bisogno = max(0.0, -self.scarto_spesa_netta(s, y))
            riga = {"scarto": self.scarto_spesa_netta(s, y)}
            for g in self.RISERVA:
                k = g["gradino"]
                if k == "d":
                    cap = curva_bonus.get(y, 0.0)
                elif k == "e":
                    cap = self.P2[y] * self.MULT[s]
                else:
                    cap = float(g[self._sc(s)]) if y >= int(g["dal"]) else 0.0
                u = min(cap, bisogno)
                riga[k] = u
                bisogno -= u
            riga["residuo"] = -bisogno
            riga["p2_dopo"] = self.P2[y] - riga["e"] / self.MULT[s]
            out[y] = riga
        return out


_PROGRAMMA = Quadro()


def quadro(variante=None):
    """Quadro del programma (variante None) o ricalcolato con le ipotesi della variante."""
    return _PROGRAMMA if not variante else Quadro(variante)


# Interfaccia del modulo: il quadro del programma, come prima del refactoring.
MULT, SOGLIA, PRENOTAZIONE, QUOTA_ECCEDENZA = (_PROGRAMMA.MULT, _PROGRAMMA.SOGLIA,
                                                _PROGRAMMA.PRENOTAZIONE, _PROGRAMMA.QUOTA_ECCEDENZA)
RIPARTIZIONE_LEVE, AVVIO_P2_2027, RICONOSCIMENTO_R1 = (_PROGRAMMA.RIPARTIZIONE_LEVE, _PROGRAMMA.AVVIO_P2_2027,
                                                       _PROGRAMMA.RICONOSCIMENTO_R1)
COPERTURE, MISURE, LEVE, CODA, DPFP, RISERVA = (_PROGRAMMA.COPERTURE, _PROGRAMMA.MISURE, _PROGRAMMA.LEVE,
                                                _PROGRAMMA.CODA, _PROGRAMMA.DPFP, _PROGRAMMA.RISERVA)
PIL, BUSTA, P2_PIENA, P2, P2_RINVIATA = (_PROGRAMMA.PIL, _PROGRAMMA.BUSTA, _PROGRAMMA.P2_PIENA,
                                         _PROGRAMMA.P2, _PROGRAMMA.P2_RINVIATA)
copertura, per_classe, costo, p1, p2_fabbisogno = (_PROGRAMMA.copertura, _PROGRAMMA.per_classe, _PROGRAMMA.costo,
                                                   _PROGRAMMA.p1, _PROGRAMMA.p2_fabbisogno)
costo_fase1, margine_fase1, eccedenza, leva = (_PROGRAMMA.costo_fase1, _PROGRAMMA.margine_fase1,
                                               _PROGRAMMA.eccedenza, _PROGRAMMA.leva)
simula_coda, costo_coda, flussi, salvaguardia, sanita_pil = (_PROGRAMMA.simula_coda, _PROGRAMMA.costo_coda,
                                                             _PROGRAMMA.flussi, _PROGRAMMA.salvaguardia,
                                                             _PROGRAMMA.sanita_pil)
scarto_spesa_netta, gradini = _PROGRAMMA.scarto_spesa_netta, _PROGRAMMA.gradini
