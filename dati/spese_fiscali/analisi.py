"""Analisi distributiva delle spese fiscali IRPEF e riserva condizionata.

Fonti: Dipartimento delle Finanze, statistiche sulle dichiarazioni 2025 (anno d'imposta 2024),
tavole per ventili e per classi di reddito complessivo (cartella tavole/, scaricate con
strumenti/scarica_tavole_df.sh); MEF, Rapporto annuale sulle spese fiscali 2025 (costi ufficiali).
Ammontari delle tavole in migliaia di euro. Decili = coppie di ventili.
"""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "tavole"
CONTRIBUENTI = 42.8e6  # contribuenti IRPEF, dichiarazioni 2025 (Dipartimento delle Finanze)
# estremo superiore dei ventili di reddito complessivo, euro (tavole DF)
SOGLIE_VENTILI = [344, 1941, 5012, 7992, 9895, 12324, 14574, 16872, 19068, 21195, 23199, 24975,
                  26915, 29100, 31470, 34191, 38118, 44489, 61431, None]
COSTI_UFFICIALI = {  # MEF, Rapporto spese fiscali 2025, milioni di euro annui
    "cedolare_secca": 3353.9,
    "regime_forfettario": 3490.8,
    "pir": 103.0,
}
FORFETTARIO_BENEFICIARI, FORFETTARIO_PRO_CAPITE = 2_033_091, 1717.0
TETTO_L207_PER_COORTE = 0.079  # miliardi per annualita di spese: crescita annua del gettito IRPEF nella relazione tecnica della L. 207/2024 (dedotto)


def _num(x):
    x = x.strip()
    if x in ("", "***"):
        return 0.0
    return float(x.replace(".", "").replace(",", "."))


def _tavola(nome):
    righe = (DIR / nome).read_text(encoding="utf-8-sig").splitlines()
    inizio = next(i for i, r in enumerate(righe) if ";Codice;" in r)
    intest = righe[inizio].split(";")
    dati = []
    for r in righe[inizio + 1:]:
        f = r.split(";")
        if not f[0] or f[0].startswith("TOTALE"):
            break
        dati.append(f)
    return intest, dati


def ventili(codice, colonna):
    intest, dati = _tavola(f"v_{codice}.csv")
    i = intest.index(colonna + " - Ammontare")
    return [_num(f[i]) * 1000 for f in dati if f[0].endswith("ventile")]


def aliquota_marginale(v):
    s = SOGLIE_VENTILI[v - 1]
    if s is not None and s < 8500:
        return 0.0
    return 0.23 if s is not None and s <= 28000 else 0.35 if s is not None and s <= 50000 else 0.43


VOCI = [  # (codice tavola, colonna DF, fattore di beneficio: numero o "marginale", etichetta, esclusione)
    ("2025AAPFTOT020803", "Detrazioni per spese recupero patrimonio edilizio (sez. III-A del quadro RP)", 1, "Recupero del patrimonio edilizio", ""),
    ("2025AAPFTOT020803", "Detrazioni per interventi finalizzati al risparmio energetico (sez. IV del quadro RP)", 1, "Risparmio energetico", ""),
    ("2025AAPFTOT020803", "Detrazioni arredo, giovani coppie, IVA acquisto abit. classe A/B e altre spese (sez.III C quadro RP)", 1, "Arredo e altre spese abitative", ""),
    ("2025AAPFTOT020703", "Previdenza complementare", "marginale", "Previdenza complementare", "esclusa: adesione automatica (Riforma 7)"),
    ("2025AAPFTOT020803", "Detrazioni per carichi di famiglia", 1, "Carichi di famiglia", "esclusa: famiglia"),
    ("2025AAPFTOT020803", "Detrazioni per redditi di lavoro dipendente, pensione e redditi assimilati", 1, "Lavoro dipendente e pensione", "esclusa"),
    ("2025AAPFTOT020803", "Detrazioni per canoni di locazione e affitto terreni (sez. V del quadro RP)", 1, "Canoni di locazione", "esclusa: redditi bassi"),
    ("2025AAPFTOT020903", "Totale spese sanitarie, spese sanitarie per portatori di handicap e acquisto cani guida", 0.19, "Spese sanitarie", "tutelata sotto soglia ISEE"),
    ("2025AAPFTOT020903", "Interessi mutui ipotecari abitazione principale stipulati ante 31/12/21", 0.19, "Interessi mutui prima casa", ""),
    ("2025AAPFTOT020903", "Spese per istruzione universitaria", 0.19, "Istruzione universitaria", ""),
    ("2025AAPFTOT020903", "Spese per istruzione non universitaria", 0.19, "Istruzione non universitaria", ""),
    ("2025AAPFTOT020903", "Spese per addetti assistenza personale", 0.19, "Addetti all'assistenza personale", "esclusa: non autosufficienza"),
    ("2025AAPFTOT020703", "Contributi servizi domestici e familiari", "marginale", "Contributi colf e badanti", "esclusa: cura"),
    ("2025AAPFTOT020703", "Assegno al coniuge", "marginale", "Assegno al coniuge", "esclusa: obbligo giuridico"),
]


def decili(codice, colonna, fattore):
    v = ventili(codice, colonna)
    ben = [x * (aliquota_marginale(k + 1) if fattore == "marginale" else fattore) for k, x in enumerate(v)]
    return [ben[2 * d] + ben[2 * d + 1] for d in range(10)]


def tabella_decili():
    out = []
    for cod, col, fat, lab, escl in VOCI:
        d = decili(cod, col, fat)
        tot = sum(d)
        out.append(dict(voce=lab, totale_mln=tot / 1e6, quota_d10=d[9] / tot, quota_d9_d10=(d[8] + d[9]) / tot,
                        pro_capite=[x / (CONTRIBUENTI / 10) for x in d], esclusione=escl))
    return sorted(out, key=lambda r: -r["quota_d10"])


def cedolare_decili():
    """Distribuzione del beneficio della cedolare: imponibile x (aliquota marginale + addizionali - aliquota cedolare)."""
    cod = "2025AAPFTOT020403"
    ben = [0.0] * 20
    for col, aliq in (("Imponibile Cedolare secca al 21% (Redditi dei fabbricati)", 0.21),
                      ("Imponibile Cedolare secca al 10% (Redditi dei fabbricati)", 0.10),
                      ("Imponibile Cedolare secca al 26% (Redditi dei fabbricati)", 0.26)):
        for k, x in enumerate(ventili(cod, col)):
            m = aliquota_marginale(k + 1)
            ben[k] += max(0.0, (m + 0.02 if m else 0.0) - aliq) * x
    d = [ben[2 * i] + ben[2 * i + 1] for i in range(10)]
    tot = sum(d)
    return dict(quote=[x / tot for x in d], costo_ufficiale_mln=COSTI_UFFICIALI["cedolare_secca"])


# ---------- curva continua sui bonus edilizi ed energetici ----------
CLASSI_OLTRE_60 = [  # punto medio (migliaia di euro) della classe di reddito complessivo
    ("da 60.000 a 70.000", 65), ("da 70.000 a 75.000", 72.5), ("da 75.000 a 80.000", 77.5), ("da 80.000 a 90.000", 85),
    ("da 90.000 a 100.000", 95), ("da 100.000 a 120.000", 110), ("da 120.000 a 150.000", 135),
    ("da 150.000 a 200.000", 175), ("da 200.000 a 300.000", 250), ("oltre 300.000", 400)]
COLONNE_RISERVA = [
    "Detrazioni per spese recupero patrimonio edilizio (sez. III-A del quadro RP)",
    "Detrazioni per interventi finalizzati al risparmio energetico (sez. IV del quadro RP)",
    "Detrazioni arredo, giovani coppie, IVA acquisto abit. classe A/B e altre spese (sez.III C quadro RP)",
]


def riduzione(reddito_migliaia, inizio=60, pieno=150, massimo=1.0):
    return massimo * min(1.0, max(0.0, (reddito_migliaia - inizio) / (pieno - inizio)))


def gettito_curva(massimo=1.0, phi=0.55):
    """Miliardi: (stock 2024 oltre 60.000, gettito sullo stock, gettito a regime sulle sole spese nuove, per coorte netto del tetto)."""
    intest, dati = _tavola("c_2025AAPFTOT020802.csv")
    idx = [intest.index(c + " - Ammontare") for c in COLONNE_RISERVA]
    righe = {f[0]: f for f in dati}
    stock = curva = 0.0
    for nome, mid in CLASSI_OLTRE_60:
        a = sum(_num(righe[nome][i]) for i in idx) * 1000 / 1e9
        stock += a
        curva += riduzione(mid, massimo=massimo) * a
    regime = curva * phi
    return dict(stock=stock, curva_su_stock=curva, regime_spese_nuove=regime,
                coorte_netta=regime / 10 - TETTO_L207_PER_COORTE)


def profilo_curva(anni, primo_anno=2028, **kw):
    c = gettito_curva(**kw)["coorte_netta"]
    return {y: max(0, y - primo_anno + 1) * c if y >= primo_anno else 0.0 for y in anni}
