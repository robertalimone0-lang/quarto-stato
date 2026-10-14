"""Formattazione italiana dei numeri per il testo e le tabelle generate."""


def it(x, dec=1, segno=False):
    s = f"{abs(x):,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if x < 0 and float(f"{abs(x):.{dec}f}") != 0:
        return "−" + s
    return ("+" if segno and x > 0 else "") + s


def tabella_md(intestazioni, righe):
    out = ["| " + " | ".join(intestazioni) + " |", "|" + "|".join("---" for _ in intestazioni) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in righe]
    return "\n".join(out)
