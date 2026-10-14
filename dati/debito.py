"""Modello del debito pubblico (Sezione 1), ricostruito dal file Excel delle sorgenti.

d(t) = d(t-1) * (1 + i) / (1 + g) - s + SF
Base: quadro tendenziale del DPFP del 2 ottobre 2026; il programmatico (con la clausola
di salvaguardia nazionale per difesa ed energia) e uno scenario di confronto.
Tasso implicito i = interessi(t) * (1 + g) / d(t-1), con interessi = indebitamento + saldo primario.
Stock-flussi SF ricavato come residuo fino al 2029; dal 2030 zero. Dal 2030 g e s invariati al 2029.
"""
try:
    from . import modello as M
except ImportError:
    import modello as M

ANNI = list(range(2025, 2033))


def _quadro(nome, m=None):
    q = {int(r["anno"]): r for r in (m or M).DPFP if r["quadro"] == nome}
    d = {y: float(q[y]["debito_pil"]) / 100 for y in q}
    g = {y: float(q[y]["crescita_pil_nominale"]) / 100 for y in q}
    s = {y: float(q[y]["saldo_primario"]) / 100 for y in q}
    n = {y: float(q[y]["indebitamento_netto"]) / 100 for y in q}
    i, sf = {}, {}
    for y in range(2026, 2030):
        i[y] = (n[y] + s[y]) * (1 + g[y]) / d[y - 1]
        sf[y] = d[y] - d[y - 1] * (1 + i[y]) / (1 + g[y]) + s[y]
    for y in range(2030, 2033):
        g[y], s[y], i[y], sf[y] = g[2029], s[2029], i[2029], 0.0
    return d, g, s, i, sf


def percorso(quadro="tendenziale", ds=None, dg=0.0, dg_da=2029, shock=0.0, shock_da=2028, vita=7.9, m=None):
    """Debito/PIL in percentuale. ds: avanzo aggiuntivo in quota di PIL per anno. m: quadro (None = programma)."""
    d0, g, s, i, sf = _quadro(quadro, m)
    d = {2025: d0[2025]}
    for y in range(2026, 2033):
        gg = g[y] + (dg if y >= dg_da else 0.0)
        ii = i[y] + shock * min(1.0, max(0, y - shock_da + 1) / vita)
        d[y] = d[y - 1] * (1 + ii) / (1 + gg) - (s[y] + (ds or {}).get(y, 0.0)) + sf[y]
    return {y: 100 * v for y, v in d.items()}


def avanzo_programma(s, confronto=False, m=None):
    m = m or M
    _, fl = m.flussi(s, confronto)
    return {y: fl[y]["saldo"] / m.PIL[y] for y in m.Y}


def avanzo_avverso_con_salvaguardia(m=None):
    m = m or M
    _, fl = m.flussi("avverso")
    sv = m.salvaguardia()
    return {y: (fl[y]["saldo"] + sv[y]["g2"] + sv[y]["g3"] + sv[y]["g4"]) / m.PIL[y] for y in m.Y}


def scenari(m=None):
    t = percorso(m=m)
    out = {"Tendenziale DPFP": t, "Programmatico DPFP (confronto)": percorso("programmatico", m=m)}
    out["Programma, centrale"] = percorso(ds=avanzo_programma("centrale", m=m), m=m)
    out["Programma, prudente"] = percorso(ds=avanzo_programma("prudente", m=m), m=m)
    out["Programma, avverso con salvaguardia"] = percorso(ds=avanzo_avverso_con_salvaguardia(m), m=m)
    out["Programma, centrale con piu crescita"] = percorso(ds=avanzo_programma("centrale", m=m), dg=0.003, m=m)
    out["Programma, centrale con stress sui tassi"] = percorso(ds=avanzo_programma("centrale", m=m), shock=0.01, m=m)
    return out


if __name__ == "__main__":
    for k, v in scenari().items():
        print(f"{k:42s} 2031 {v[2031]:6.2f}  2032 {v[2032]:6.2f}")
