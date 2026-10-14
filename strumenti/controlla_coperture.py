"""Controlli automatici sulla tabella unica delle coperture e sul quadro finanziario.

Blocca la build (exit 1) se:
- un codice compare due volte in coperture, misure, leve o coda;
- una copertura ha classe diversa da A, B, C o tassi non ordinati (centrale >= prudente >= avverso);
- la stessa risorsa finanzia due misure (dati/allocazioni.csv, se presente): somma > valore prudente;
- lo scenario prudente chiude un anno con margine negativo;
- la Priorita 1 non e coperta senza le voci escluse (azzardo, patrimonio pubblico) nel prudente;
- la Priorita 2 rinviata non coincide con le voci di coda corrispondenti.
"""
import csv
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RADICE / "dati"))
import modello as M  # noqa: E402

errori = []


def unici(righe, nome):
    visti = set()
    for r in righe:
        if r["codice"] in visti:
            errori.append(f"{nome}: codice duplicato {r['codice']}")
        visti.add(r["codice"])


unici(M.COPERTURE, "coperture.csv")
unici(M.MISURE, "misure.csv")
unici(M.LEVE, "leve.csv")
unici(M.CODA, "coda.csv")

voci = {}
for r in M.COPERTURE:
    if r["classe"] not in ("A", "B", "C"):
        errori.append(f"{r['codice']}: classe non valida {r['classe']}")
    c, p, a = (float(r[f"tasso_{s}"]) for s in M.SC)
    if not c >= p >= a:
        errori.append(f"{r['codice']}: tassi non ordinati {c} {p} {a}")
    chiave = r["voce"].strip().lower()
    if chiave in voci:
        errori.append(f"{r['codice']}: stessa voce di {voci[chiave]}")
    voci[chiave] = r["codice"]

alloc = RADICE / "dati/allocazioni.csv"
if alloc.exists():
    with open(alloc, encoding="utf-8") as f:
        righe = list(csv.DictReader(f))
    usato = {}
    for r in righe:
        usato[r["copertura"]] = usato.get(r["copertura"], 0.0) + float(r["importo"])
    for r in M.COPERTURE:
        cap = float(r["nominale"]) * float(r["tasso_prudente"])
        if usato.get(r["codice"], 0.0) > cap + 1e-6:
            errori.append(f"{r['codice']}: allocati {usato[r['codice']]:.2f} oltre il valore prudente {cap:.2f}")

for y in M.Y:
    m = M.margine_fase1("prudente", y)
    if m < -1e-6:
        errori.append(f"prudente {y}: margine negativo {m:.2f}")
    if M.copertura("prudente", y, solo_p1=True) < M.p1(y) * M.MULT["prudente"] - 1e-6:
        errori.append(f"prudente {y}: Priorita 1 non coperta senza azzardo e patrimonio pubblico")

rinviate = sum(float(v["costo_regime"]) for v in M.CODA if "Priorita 2 rinviata" in v["note"])
if abs(rinviate - M.P2_RINVIATA) > 0.05:
    errori.append(f"coda: voci rinviate {rinviate:.2f} diverse dalla Priorita 2 rinviata {M.P2_RINVIATA:.2f}")

if errori:
    print("\n".join(errori))
    sys.exit(1)
print(f"Coperture: {len(M.COPERTURE)} voci, nessun doppio conteggio. Prudente >= 0 in ogni anno. "
      f"Priorita 2 rinviata {M.P2_RINVIATA:.2f} = voci di coda {rinviate:.2f}.")
