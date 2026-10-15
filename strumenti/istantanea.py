"""Test di non regressione del modello.

Raccoglie tutti i risultati del quadro (coperture, Priorita 1 e 2, coda e anni di attivazione,
flussi, salvaguardia, sanita, spesa netta, gradini della riserva, debito) per tutti gli scenari
e le varianti, e li confronta con l'istantanea di riferimento salvata prima del refactoring.

Uso: python strumenti/istantanea.py            confronta con il riferimento (esce con errore se diverge)
     python strumenti/istantanea.py --salva    riscrive il riferimento (solo su decisione esplicita) e stampa
                                               il riepilogo delle differenze da riportare nel commit
"""
import json
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RADICE / "dati"))
sys.path.insert(0, str(RADICE / "dati" / "spese_fiscali"))

RIFERIMENTO = Path(__file__).resolve().parent / "istantanea_riferimento.json"
SCENARI = ["centrale", "prudente", "avverso", "alta"]


def _chiavi(d):
    return {str(k): v for k, v in d.items()}


def raccogli(M, D, curva_bonus):
    """M: modello (modulo o quadro); D: funzioni del debito legate allo stesso modello."""
    Y = M.Y
    out = {"P2_RINVIATA": M.P2_RINVIATA}
    out["costanti"] = dict(SOGLIA=M.SOGLIA, PRENOTAZIONE=M.PRENOTAZIONE, QUOTA_ECCEDENZA=M.QUOTA_ECCEDENZA,
                           RIPARTIZIONE_LEVE=M.RIPARTIZIONE_LEVE, AVVIO_P2_PRIMO_ANNO=M.AVVIO_P2_PRIMO_ANNO, MULT=M.MULT)
    out["PIL"] = _chiavi(M.PIL)
    for nome in ("BUSTA", "P2_PIENA", "P2"):
        out[nome] = _chiavi(getattr(M, nome))
    out["p1"] = {str(y): M.p1(y) for y in Y}
    out["p2_fabbisogno"] = {str(y): M.p2_fabbisogno(y) for y in Y}
    for s in SCENARI:
        r = out.setdefault("scenari", {}).setdefault(s, {})
        r["copertura"] = {str(y): M.copertura(s, y) for y in Y}
        r["copertura_p1"] = {str(y): M.copertura(s, y, solo_p1=True) for y in Y}
        r["per_classe"] = {str(y): M.per_classe(s, y) for y in Y}
        r["costo_fase1"] = {str(y): M.costo_fase1(s, y) for y in Y}
        r["margine_fase1"] = {str(y): M.margine_fase1(s, y) for y in Y}
        r["eccedenza"] = {str(y): M.eccedenza(s, y) for y in Y}
        r["leva"] = {str(y): M.leva(s, y) for y in Y}
        r["leva_contributiva"] = {str(y): M.leva(s, y, tipo=("contributiva", "una_tantum")) for y in Y}
        for conf in (False, True):
            att, g, x, st = M.simula_coda(s, confronto=conf)
            k = "confronto" if conf else "base"
            r[f"coda_{k}"] = dict(attiva=att, stato=_chiavi(st))
            att2, fl = M.flussi(s, confronto=conf)
            r[f"flussi_{k}"] = _chiavi(fl)
            r[f"costo_coda_{k}"] = {str(y): M.costo_coda(s, att, y) for y in Y}
            r[f"sanita_pil_{k}"] = {str(y): M.sanita_pil(s, att, y) for y in Y}
        if s != "alta":
            r["spesa_netta"] = {str(y): M.scarto_spesa_netta(s, y) for y in Y}
            r["spesa_netta_riconoscimento"] = {str(y): M.scarto_spesa_netta(s, y, riconoscimento=True) for y in Y}
            r["gradini"] = _chiavi(M.gradini(s, curva_bonus))
            r["gradini_riconoscimento"] = _chiavi(M.gradini(s, curva_bonus, riconoscimento=True))
    out["per_classe_nominale"] = {str(y): M.per_classe("nominale", y) for y in Y}
    out["salvaguardia"] = _chiavi(M.salvaguardia())
    out["salvaguardia_2030"] = _chiavi(M.salvaguardia(primo=2030))
    out["debito"] = {k: _chiavi(v) for k, v in D["scenari"]().items()}
    out["debito_confronto"] = _chiavi(D["percorso"](ds=D["avanzo_programma"]("centrale", True)))
    out["debito_prudente_stress"] = _chiavi(D["percorso"](ds=D["avanzo_programma"]("prudente"), dg=-0.005, shock=0.01))
    return json.loads(json.dumps(out))  # normalizza chiavi e tipi come nel file


def _differenze(a, b, via=""):
    if isinstance(a, dict) and isinstance(b, dict):
        out = [f"{via}/{k}: presente solo in uno dei due" for k in set(a) ^ set(b)]
        for k in set(a) & set(b):
            out += _differenze(a[k], b[k], f"{via}/{k}")
        return out
    return [] if a == b else [f"{via}: {a!r} != {b!r}"]


def attuale():
    import modello as M
    import debito
    import analisi
    D = dict(scenari=debito.scenari, percorso=debito.percorso, avanzo_programma=debito.avanzo_programma)
    return raccogli(M, D, analisi.profilo_curva(M.Y))


def da_quadro():
    """Stessi risultati calcolati su un Quadro creato da zero, con il debito legato a quel quadro."""
    import modello as M
    import debito
    import analisi
    q = M.Quadro()
    D = dict(scenari=lambda: debito.scenari(m=q), percorso=lambda **kw: debito.percorso(m=q, **kw),
             avanzo_programma=lambda s, c=False: debito.avanzo_programma(s, c, m=q))
    return raccogli(q, D, analisi.profilo_curva(q.Y))


def main():
    dati = attuale()
    if "--salva" in sys.argv:
        # Regola (CLAUDE.md): il commit che aggiorna il riferimento indica il codice D che lo giustifica,
        # il numero di valori cambiati e le differenze principali: questo riepilogo va nel messaggio di commit.
        if RIFERIMENTO.exists():
            diff = _differenze(json.loads(RIFERIMENTO.read_text(encoding="utf-8")), dati)
            print(f"Valori cambiati rispetto al riferimento precedente: {len(diff)}")
            for d in sorted(diff, key=lambda x: (x.count("/"), x))[:20]:
                print("  " + d)
        RIFERIMENTO.write_text(json.dumps(dati, indent=1, sort_keys=True), encoding="utf-8")
        print(f"Istantanea salvata: {RIFERIMENTO.name}")
        return
    rif = json.loads(RIFERIMENTO.read_text(encoding="utf-8"))
    diff = _differenze(rif, dati) + [f"Quadro(): {d}" for d in _differenze(rif, da_quadro())]
    if diff:
        print(f"Non regressione: {len(diff)} differenze rispetto al riferimento")
        for d in sorted(diff)[:40]:
            print("  " + d)
        sys.exit(1)
    print("Non regressione: risultati identici al riferimento (interfaccia del modulo e Quadro() da zero).")


if __name__ == "__main__":
    main()
