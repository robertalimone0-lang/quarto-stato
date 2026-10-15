"""Segnala ogni numero nei capitoli che non proviene da fonti.yaml o dal modello.

Accettati: shortcode {{< dato ... >}}, codice inline `{python} ...`, blocchi di codice,
anni (1900-2099), date complete, riferimenti normativi (art., comma, legge, n., ...),
numerazione di elenchi e codici (F1-R01, Q01, COP01).
Uso: python strumenti/controlla_fonti.py [--rigoroso]   (con --rigoroso esce con errore)
"""
import re
import sys
from pathlib import Path

import yaml

RADICE = Path(__file__).resolve().parents[1]
MESI = "gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre"
PREFISSI_NORMATIVI = re.compile(
    r"(art\.|artt\.|articol[oi]|comm[ai]|letter[ae]|lett\.|L\.|legge|D\.Lgs\.|DL|D\.L\.|d\.lgs\.|n\.|regolamento|"
    r"direttiva|sentenz[ae]|Riforma|Riforme|punto|capitolo|paragrafo|par\.|Cost\.|Costituzione|C-|cause|causa|"
    r"Fase|fase|gradino|classe|[Ss]ettiman[ae]|DM|A\.S\.|XVIII|Q|F\d-R|COP|L|M|C|X|V|D|S|I)\s*$"
)
NUMERO = re.compile(r"(?<![\w.,])(\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?)(\s*%)?")


def ripulisci(testo):
    testo = re.sub(r"^---\n.*?\n---\n", "", testo, flags=re.S)
    testo = re.sub(r"```.*?```", "", testo, flags=re.S)
    testo = re.sub(r"`\{python\}[^`]*`", "", testo)
    testo = re.sub(r"\{\{<.*?>\}\}", "", testo)
    testo = re.sub(r"\]\([^)]*\)", "]", testo)
    testo = re.sub(r"https?://\S+", "", testo)
    testo = re.sub(r"\{#[^}]*\}", "", testo)
    testo = re.sub(r"@\w[\w-]*", "", testo)
    return testo


def sospetti(riga):
    out = []
    for m in NUMERO.finditer(riga):
        tok, pct = m.group(1), m.group(2)
        prima = riga[: m.start()]
        dopo = riga[m.end(): m.end() + 15]
        valore = tok.replace(".", "").replace(",", ".")
        if not pct and re.fullmatch(r"(19|20)\d\d", tok):
            continue  # anno
        if re.match(rf"\s*({MESI})\b", dopo):
            continue  # giorno di una data
        if not pct and "," not in tok and re.match(r"\s*(,\s*\d+\s*)*(e\s+\d+\s+)?(mesi|mese|giorni|giorno|anni|anno|ore)\b", riga[m.end():m.end()+30]):
            continue  # durate ed eta (12 mesi, tra 16 e 74 anni)
        if not pct and re.match(r"\s*e\s+\d+\s+(mesi|anni|giorni)", dopo):
            continue
        if PREFISSI_NORMATIVI.search(prima[-14:]):
            continue
        if re.match(r"^\s*\d+\.\s", riga) and m.start() < 4:
            continue  # elenco numerato
        if re.match(r"^\|\s*\d+\s*\|", riga) and m.start() < 6:
            continue  # numero della settimana nella prima colonna di una tabella
        if re.match(r"\s*/\s*\d", dopo) or re.search(r"\d\s*/\s*$", prima):
            continue  # numero di legge del tipo 243/2012
        if not pct and "," not in tok and float(valore) < 10 and not re.search(r"(miliard|milion|euro|punt)", dopo):
            continue  # piccoli interi nel discorso (tre scenari, 4 gradini)
        out.append(tok + (pct or ""))
    return out


def main():
    rigoroso = "--rigoroso" in sys.argv
    fonti = yaml.safe_load((RADICE / "dati/fonti.yaml").read_text(encoding="utf-8"))["fonti"]
    problemi = 0
    for codice, v in fonti.items():
        mancanti = [k for k in ("valore", "unita", "fonte", "url", "data", "stato") if k not in v]
        if mancanti:
            print(f"fonti.yaml: {codice} senza {', '.join(mancanti)}")
            problemi += 1
    da_validare = [c for c, v in fonti.items() if v.get("stato") != "verificato"]
    for qmd in sorted((RADICE / "capitoli").glob("*.qmd")):
        testo = qmd.read_text(encoding="utf-8")
        for codice in re.findall(r"\{\{<\s*dato\s+(\w+)", testo):
            if codice not in fonti:
                print(f"{qmd.name}: dato {codice} assente da fonti.yaml")
                problemi += 1
        for n, riga in enumerate(ripulisci(testo).splitlines(), 1):
            for tok in sospetti(riga):
                print(f"{qmd.name}:{n}: numero senza fonte: {tok}")
                problemi += 1
    print(f"\nVoci del registro: {len(fonti)}; da validare: {len(da_validare)}; segnalazioni: {problemi}")
    if rigoroso and problemi:
        sys.exit(1)


if __name__ == "__main__":
    main()
