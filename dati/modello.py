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
"""
from pathlib import Path
import csv

DIR = Path(__file__).resolve().parent
Y = list(range(2027, 2036))
SC = ["centrale", "prudente", "avverso"]
MULT = {"centrale": 1.00, "prudente": 1.05, "avverso": 1.10, "alta": 1.00}
SOGLIA, PRENOTAZIONE, QUOTA_ECCEDENZA = 1.10, 0.50, 0.50
RIPARTIZIONE_LEVE = {"irpef": 0.50, "debito": 0.30, "riserva": 0.20}  # gettito delle leve rimasto libero
AVVIO_P2_2027 = 0.5  # Priorita 2 del 2027 dal 1 luglio


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


COPERTURE = _csv("coperture.csv")
MISURE = _csv("misure.csv")
LEVE = _csv("leve.csv")
CODA = _csv("coda.csv")
DPFP = _csv("dpfp_2026.csv")

PIL = {int(r["anno"]): float(r["pil_nominale_mld"]) for r in DPFP if r["quadro"] == "tendenziale"}
for y in range(2030, 2036):
    PIL[y] = PIL[y - 1] * 1.026  # ipotesi: crescita nominale invariata al livello 2029


def _sc(s):
    return "centrale" if s == "alta" else s


# ---------------- coperture di Fase 1 ----------------
def copertura(s, y, solo_p1=False):
    t = 0.0
    for r in COPERTURE:
        if solo_p1 and r["ammessa_priorita_1"] != "si":
            continue
        t += float(r["nominale"]) * float(r[f"tasso_{_sc(s)}"]) * rampa(r["rampa"])[y]
    return t


def per_classe(s, y):
    out = {}
    for r in COPERTURE:
        v = float(r["nominale"]) * (float(r[f"tasso_{_sc(s)}"]) if s != "nominale" else 1) * rampa(r["rampa"])[y]
        out[r["classe"]] = out.get(r["classe"], 0.0) + v
    return out


def costo(priorita, y):
    return sum(float(r["costo_regime"]) * rampa(r["rampa"])[y] for r in MISURE if r["priorita"] == str(priorita))


def p1(y):
    return costo(1, y)


def p2_fabbisogno(y):
    return costo(2, y)


BUSTA = {y: (copertura("prudente", y) - p1(y) * MULT["prudente"]) / MULT["prudente"] for y in Y}
P2_PIENA = {y: max(0.0, min(p2_fabbisogno(y), min(BUSTA[u] for u in Y if u >= y))) for y in Y}
_cof = next(r for r in MISURE if r["codice"] == "M08")
_cof_rinviato = float(next(v for v in CODA if v["codice"] == "Q09")["costo_regime"])
_cof_fase1 = float(_cof["costo_regime"]) - _cof_rinviato  # quota del cofinanziamento rimasta in Fase 1
_COF_2027 = _cof_fase1 * rampa(_cof["rampa"])[2027] * P2_PIENA[2027] / p2_fabbisogno(2027)
P2 = dict(P2_PIENA)
P2[2027] = AVVIO_P2_2027 * (P2_PIENA[2027] - _COF_2027)  # dal 1 luglio 2027, cofinanziamento dal 2028
P2_RINVIATA = p2_fabbisogno(2031) - P2[2031]


def costo_fase1(s, y):
    return (p1(y) + P2[y]) * MULT[s]


def margine_fase1(s, y):
    return copertura(s, y) - costo_fase1(s, y)


def eccedenza(s, y):
    return max(0.0, copertura(s, y) - copertura("prudente", y))


# ---------------- leve e coda ----------------
def leva(s, y, tipo=("fiscale", "risparmio"), confronto=False):
    tipi = set(tipo) | ({"confronto"} if confronto else set())
    return sum(float(r[s]) * rampa(r["rampa"])[y] for r in LEVE if r["tipo"] in tipi)


def _cert(d, y):
    return (d.get(y - 1, 0.0) + d.get(y - 2, 0.0)) / 2


def _profilo(voce, k):
    if voce["profilo"] == "capitale_umano":
        f = min(1.0, (k + 1) / 7)
        return 0.685 * f + 0.55 * f + 0.10
    p = [float(x) for x in voce["profilo"].split(";")]
    return float(voce["costo_regime"]) * p[min(k, len(p) - 1)]


def simula_coda(s, confronto=False):
    g = {y: leva(s, y, confronto=confronto) for y in Y}
    x = {y: eccedenza(s, y) for y in Y}
    attiva, impegnato, prenotato, stato = {}, 0.0, 0.0, {}
    for y in Y:
        risorse = _cert(g, y) + QUOTA_ECCEDENZA * _cert(x, y)
        libero = risorse - impegnato - prenotato
        while True:
            resto = [v for v in CODA if v["codice"] not in attiva]
            if not resto:
                break
            c0 = float(resto[0]["costo_regime"]) * MULT[s]
            if prenotato + libero >= SOGLIA * c0:
                attiva[resto[0]["codice"]] = y
                impegnato += c0
                libero, prenotato = libero + prenotato - c0, 0.0
                continue
            nuova = PRENOTAZIONE * max(0.0, libero)
            prenotato += nuova
            disp = libero - nuova
            for v in resto[1:]:
                c = float(v["costo_regime"]) * MULT[s]
                if disp >= SOGLIA * c:
                    attiva[v["codice"]] = y
                    impegnato += c
                    disp -= c
            break
        stato[y] = dict(risorse=risorse, impegnato=impegnato, prenotato=prenotato)
    return attiva, g, x, stato


def costo_coda(s, attiva, y):
    t = 0.0
    for v in CODA:
        a = attiva.get(v["codice"])
        if a is not None and y >= a:
            t += _profilo(v, y - a) * MULT[s]
    return t


def flussi(s, confronto=False):
    """Effetto annuo sul saldo primario rispetto al tendenziale, in miliardi."""
    attiva, g, x, st = simula_coda(s, confronto)
    out = {}
    for y in Y:
        usato_leve = max(0.0, st[y]["impegnato"] + st[y]["prenotato"] - QUOTA_ECCEDENZA * _cert(x, y))
        irpef = RIPARTIZIONE_LEVE["irpef"] * max(0.0, _cert(g, y) - usato_leve)
        contributi = leva(s, y, tipo=("contributiva", "una_tantum"))
        cc = costo_coda(s, attiva, y)
        m1 = margine_fase1(s, y)
        out[y] = dict(margine_fase1=m1, leve=g[y], coda=cc, irpef=irpef, contributi=contributi,
                      saldo=m1 + g[y] - cc - irpef + contributi)
    return attiva, out


# ---------------- clausola di salvaguardia (scenario avverso) ----------------
_TARDIVE = [r for r in MISURE if r["priorita"] == "2" and min(int(p.split(":")[0]) for p in r["rampa"].split(";")) >= 2028]


def salvaguardia(primo=2028):
    s, righe = "avverso", {}
    base_p2, base_p1 = P2[primo - 1], p1(primo - 1)
    for y in Y:
        buco = margine_fase1(s, y)
        if buco >= 0:
            righe[y] = dict(buco=buco, g1=0.0, g2=0.0, g3=0.0, g4=0.0, residuo=0.0)
            continue
        if y < primo:  # primo anno: solo il rinvio dei nuovi ingressi della Priorita 1 (gradino 4)
            g4 = min(-buco, p1(y) * MULT[s])
            righe[y] = dict(buco=buco, g1=0.0, g2=0.0, g3=0.0, g4=g4, residuo=min(0.0, buco + g4))
            continue
        tardive = sum(float(r["costo_regime"]) * rampa(r["rampa"])[y] for r in _TARDIVE) * P2[y] / p2_fabbisogno(y) * MULT[s]
        cap = [0.0, tardive, max(0.0, (P2[y] - base_p2) * MULT[s] - tardive), max(0.0, (p1(y) - base_p1) * MULT[s])]
        bisogno, usati = -buco, []
        for c in cap:
            u = min(c, max(0.0, bisogno))
            usati.append(u)
            bisogno -= u
        righe[y] = dict(buco=buco, g1=usati[0], g2=usati[1], g3=usati[2], g4=usati[3], residuo=-max(0.0, bisogno))
    return righe


def sanita_pil(s, attiva, y, base=6.4):
    extra = sum(_profilo(v, y - attiva[v["codice"]]) * MULT[s] for v in CODA
                if v["codice"] in ("Q07", "Q08") and v["codice"] in attiva and y >= attiva[v["codice"]])
    return base + 100 * (11.0 * MULT[s] + extra) / PIL[y]


# ---------------- percorso di spesa netta e riserva condizionata (D19, D20, D22) ----------------
RICONOSCIMENTO_R1 = 3.85  # quota della Riforma 1 riconosciuta in via prudente come misure discrezionali (D20)
_RAMPA_EV = rampa("2028:0.25;2029:0.5;2030:0.75;2031:1")
RISERVA = _csv("riserva.csv")


def _cofinanziamento_fase1(y):
    """Cofinanziamento di programmi UE, escluso dalla spesa netta (quota di Fase 1, dal 2028)."""
    if y <= 2027:
        return 0.0
    return _cof_fase1 * rampa(_cof["rampa"])[y] * (P2[y] / p2_fabbisogno(y))


def scarto_spesa_netta(s, y, riconoscimento=False):
    """Coperture valide ai fini UE meno spesa di Fase 1 rilevante per la spesa netta (miliardi)."""
    spesa = costo_fase1(s, y) - _cofinanziamento_fase1(y) * MULT[s]
    if riconoscimento:
        valide = copertura(s, y)
    else:
        valide = sum(float(r["nominale"]) * float(r[f"tasso_{_sc(s)}"]) * rampa(r["rampa"])[y]
                     * float(r["quota_ue_senza_riconoscimento"]) for r in COPERTURE)
        valide += RICONOSCIMENTO_R1 * _RAMPA_EV[y]
    return valide - spesa


def gradini(s, curva_bonus):
    """Copertura dei gradini della riserva nella variante senza riconoscimento. curva_bonus: {anno: miliardi}."""
    out = {}
    for y in Y:
        bisogno = max(0.0, -scarto_spesa_netta(s, y))
        riga = {"scarto": scarto_spesa_netta(s, y)}
        for g in RISERVA:
            k = g["gradino"]
            if k == "d":
                cap = curva_bonus.get(y, 0.0)
            elif k == "e":
                cap = P2[y] * MULT[s]
            else:
                cap = float(g[_sc(s)]) if y >= int(g["dal"]) else 0.0
            u = min(cap, bisogno)
            riga[k] = u
            bisogno -= u
        riga["residuo"] = -bisogno
        riga["p2_dopo"] = P2[y] - riga["e"] / MULT[s]
        out[y] = riga
    return out
