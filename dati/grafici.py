"""Grafici generati nella build. Colori sobri, leggibili anche in stampa."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

INK, MUTED, ACCENT, SOFT = "#1f2933", "#52606d", "#1f5f8b", "#e4ecf3"


def _box(ax, x, y, w, h, testo, colore=SOFT, bordo=ACCENT, size=9):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.02",
                                fc=colore, ec=bordo, lw=1.2))
    ax.text(x + w / 2, y + h / 2, testo, ha="center", va="center", fontsize=size, color=INK, wrap=True)


def _freccia(ax, x0, y0, x1, y1, etichetta=None):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.2))
    if etichetta:
        ax.text((x0 + x1) / 2 + 0.01, (y0 + y1) / 2, etichetta, fontsize=8, color=MUTED, ha="left", va="center")


def flusso_attivazione():
    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    _box(ax, 0.02, 0.80, 0.30, 0.15, "Leve di entrata\nevasione, regolarizzazione,\nrientri, cannabis, risparmi")
    _box(ax, 0.36, 0.80, 0.30, 0.15, "Coperture di Fase 1\noltre lo scenario prudente\n(eccedenza a consuntivo)")
    _box(ax, 0.70, 0.80, 0.28, 0.15, "Contributi di emersi\ne regolarizzati")
    _box(ax, 0.10, 0.52, 0.56, 0.16, "Certificazione UPB\nmedia mobile di quattro trimestri, dati di cassa\nconferma annuale sul consuntivo", colore="#ffffff")
    _box(ax, 0.02, 0.18, 0.30, 0.18, "Coda di attivazione\nQ01–Q15, soglia 110%\nscorrimento con prenotazione")
    _box(ax, 0.36, 0.18, 0.30, 0.18, "Gettito delle leve\nrimasto libero:\n50% IRPEF, 30% debito, 20% riserva")
    _box(ax, 0.70, 0.18, 0.28, 0.18, "Riduzione del debito\no saldo INPS")
    _freccia(ax, 0.17, 0.80, 0.25, 0.68)
    _freccia(ax, 0.51, 0.80, 0.45, 0.68, "50%")
    _freccia(ax, 0.62, 0.80, 0.80, 0.36, "50% al debito")
    _freccia(ax, 0.84, 0.80, 0.84, 0.36)
    _freccia(ax, 0.25, 0.52, 0.17, 0.36, "prima la coda")
    _freccia(ax, 0.45, 0.52, 0.51, 0.36, "poi il resto")
    _freccia(ax, 0.66, 0.27, 0.70, 0.27)
    ax.text(0.02, 0.05, "Reversibilità: due anni di gettito certificato sotto il costo delle misure attivate "
            "sospendono le attivazioni e attingono alla riserva.", fontsize=8, color=MUTED)
    fig.tight_layout()
    return fig
