"""lafp — the small plotting toolkit used throughout the book.

Every figure in the book is produced by the code printed next to it, and that
code needs only numpy, matplotlib and this file.  Put lafp.py next to your
notebook (or anywhere on your PYTHONPATH) and call `setup()` once.
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Ellipse, Circle

# ---------------------------------------------------------------- colours
INK   = "#1f2430"
BLUE  = "#2f5d9b"
RED   = "#c8443a"
TEAL  = "#16857a"
GOLD  = "#d9961a"
PLUM  = "#7b4f9d"
GREEN = "#5b8f2a"
ORANGE= "#e0762b"
SKY   = "#6aa6d6"
ROSE  = "#e08aa0"
GRAY  = "#8b909a"
LIGHT = "#e8e9ec"
PALETTE = [BLUE, RED, TEAL, GOLD, PLUM, GREEN, ORANGE, SKY, ROSE, GRAY]
CMAP = "RdBu_r"          # diverging map for signed matrices
SEQ  = "viridis"         # sequential map

W = 4.6                  # full text width of the printed page, in inches


def setup(serif=True):
    """Apply the book's plotting style (safe to call more than once)."""
    try:  # use the book's typeface if it is installed; otherwise fall back quietly
        from matplotlib import font_manager as fm
        import os, glob
        here = os.path.dirname(os.path.abspath(__file__))
        for f in glob.glob(os.path.join(here, "..", "fonts", "*.ttf")):
            fm.fontManager.addfont(f)
    except Exception:
        pass
    fams = [f.name for f in mpl.font_manager.fontManager.ttflist]
    body = "Source Serif 4" if ("Source Serif 4" in fams and serif) else "DejaVu Serif"
    mpl.rcParams.update({
        "figure.figsize": (W, 2.6), "figure.dpi": 110, "savefig.dpi": 220,
        "font.family": "serif", "font.serif": [body, "DejaVu Serif"],
        "font.size": 7.5, "axes.titlesize": 8, "axes.labelsize": 7.5,
        "xtick.labelsize": 6.5, "ytick.labelsize": 6.5, "legend.fontsize": 6.5,
        "mathtext.fontset": "custom", "mathtext.rm": body, "mathtext.it": body + ":italic",
        "mathtext.bf": body + ":bold", "mathtext.fallback": "stix",
        "axes.edgecolor": "#5a5f69", "axes.linewidth": 0.6, "axes.labelcolor": INK,
        "text.color": INK, "xtick.color": "#5a5f69", "ytick.color": "#5a5f69",
        "xtick.major.width": 0.5, "ytick.major.width": 0.5,
        "xtick.major.size": 2.5, "ytick.major.size": 2.5,
        "axes.prop_cycle": mpl.cycler(color=PALETTE),
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": False, "grid.color": LIGHT, "grid.linewidth": 0.5,
        "lines.linewidth": 1.2, "lines.markersize": 3.5,
        "legend.frameon": False, "figure.constrained_layout.use": True,
        "axes.titleweight": "semibold", "axes.titlepad": 4,
        "svg.fonttype": "path", "image.cmap": SEQ,
    })


def plane(ax, lim=3, grid=True, ticks=False):
    """Prepare an axis as a Cartesian plane with the origin at the centre."""
    if np.isscalar(lim):
        lim = (-lim, lim, -lim, lim)
    ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3])
    ax.set_aspect("equal")
    for s in ("left", "bottom"):
        ax.spines[s].set_position("zero"); ax.spines[s].set_color("#9aa0a8")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    if grid:
        for x in np.arange(np.ceil(lim[0]), np.floor(lim[1]) + 1):
            ax.axvline(x, color=LIGHT, lw=0.5, zorder=0)
        for y in np.arange(np.ceil(lim[2]), np.floor(lim[3]) + 1):
            ax.axhline(y, color=LIGHT, lw=0.5, zorder=0)
    if not ticks:
        ax.set_xticks([]); ax.set_yticks([])
    return ax


def arrow(ax, v, origin=(0, 0), color=BLUE, label=None, lw=1.4, offset=(0.08, 0.08),
          fs=8, ls="-", alpha=1.0, z=3):
    """Draw the vector v as an arrow starting at origin, with an optional label."""
    o = np.asarray(origin, float); v = np.asarray(v, float)
    a = FancyArrowPatch(o, o + v, arrowstyle="-|>", mutation_scale=7, lw=lw,
                        color=color, linestyle=ls, alpha=alpha, zorder=z,
                        shrinkA=0, shrinkB=0)
    ax.add_patch(a)
    if label:
        ax.text(*(o + v + np.asarray(offset)), label, color=color, fontsize=fs,
                ha="center", va="center", zorder=z + 1)
    return a


def grid_image(ax, A, lim=2, n=9, color=BLUE, lw=0.6, alpha=0.9, base=True):
    """Draw the image under the 2x2 matrix A of a square grid of lines."""
    A = np.asarray(A, float)
    t = np.linspace(-lim, lim, 200)
    for c in np.linspace(-lim, lim, n):
        for P in (np.vstack([t, c + 0 * t]), np.vstack([c + 0 * t, t])):
            if base:
                ax.plot(*P, color=LIGHT, lw=0.5, zorder=0)
            Q = A @ P
            ax.plot(*Q, color=color, lw=lw, alpha=alpha, zorder=1)


def circle_image(ax, A, color=RED, lw=1.3, fill=0.12, n=400, **kw):
    """Draw the image under A of the unit circle (an ellipse when A is invertible)."""
    th = np.linspace(0, 2 * np.pi, n)
    P = np.asarray(A, float) @ np.vstack([np.cos(th), np.sin(th)])
    ax.plot(*P, color=color, lw=lw, **kw)
    if fill:
        ax.fill(*P, color=color, alpha=fill, lw=0)
    return P


def unit_circle(ax, color=GRAY, lw=0.8, ls="--"):
    th = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(th), np.sin(th), color=color, lw=lw, ls=ls)


def heat(ax, M, annot=True, fmt="{:.2g}", cmap=CMAP, vmax=None, fs=6, labels=False):
    """Show a matrix as a coloured grid, optionally printing its entries."""
    M = np.asarray(M, float)
    v = vmax if vmax is not None else (np.abs(M).max() or 1.0)
    im = ax.imshow(M, cmap=cmap, vmin=-v if cmap == CMAP else None, vmax=v)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(True); s.set_color("#c6c9cf")
    if annot and M.size <= 144:
        for (i, j), x in np.ndenumerate(M):
            c = "white" if abs(x) > 0.6 * v else INK
            ax.text(j, i, fmt.format(x), ha="center", va="center", fontsize=fs, color=c)
    return im


def label_point(ax, p, s, color=INK, dx=0.08, dy=0.08, fs=7.5, **kw):
    ax.plot(*p, "o", color=color, ms=3, zorder=5)
    ax.text(p[0] + dx, p[1] + dy, s, color=color, fontsize=fs, **kw)


def span_line(ax, v, lim=3, color=GRAY, lw=0.9, ls="-", alpha=0.8, label=None):
    """Draw the line spanned by v through the origin."""
    v = np.asarray(v, float); v = v / np.linalg.norm(v)
    t = np.array([-3 * lim, 3 * lim])
    ax.plot(t * v[0], t * v[1], color=color, lw=lw, ls=ls, alpha=alpha, label=label)


def ax3d(fig=None, pos=111, elev=22, azim=-58, lim=1.5):
    fig = fig or plt.figure(figsize=(W * 0.55, W * 0.5))
    ax = fig.add_subplot(pos, projection="3d")
    ax.view_init(elev=elev, azim=azim)
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor((1, 1, 1, 0)); a.pane.set_edgecolor(LIGHT)
        a._axinfo["grid"]["color"] = LIGHT; a._axinfo["grid"]["linewidth"] = 0.4
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    ax.tick_params(labelsize=5, pad=0)
    return ax


def arrow3d(ax, v, origin=(0, 0, 0), color=BLUE, label=None, lw=1.4, fs=8):
    o = np.asarray(origin, float); v = np.asarray(v, float)
    ax.quiver(*o, *v, color=color, lw=lw, arrow_length_ratio=0.12)
    if label:
        ax.text(*(o + 1.08 * v), label, color=color, fontsize=fs)


def plane3d(ax, n, d=0, lim=1.4, color=SKY, alpha=0.25, res=2):
    """Shade the plane n . x = d inside a cube of half-width lim."""
    n = np.asarray(n, float)
    k = int(np.argmax(np.abs(n)))
    i, j = [m for m in range(3) if m != k]
    u, w = np.meshgrid(np.linspace(-lim, lim, res), np.linspace(-lim, lim, res))
    P = np.zeros((3,) + u.shape); P[i] = u; P[j] = w
    P[k] = (d - n[i] * u - n[j] * w) / n[k]
    ax.plot_surface(P[0], P[1], P[2], color=color, alpha=alpha, lw=0, shade=False)


def stem_spectrum(ax, vals, color=BLUE, label=None, marker="o"):
    vals = np.asarray(vals)
    ml, sl, bl = ax.stem(np.arange(1, len(vals) + 1), vals, label=label)
    plt.setp(ml, color=color, markersize=3, marker=marker); plt.setp(sl, color=color, lw=0.9)
    plt.setp(bl, color=LIGHT, lw=0.6)


def complex_plane(ax, lim=2.5, ticks=True):
    plane(ax, lim, grid=False, ticks=ticks)
    ax.set_xlabel("Re", loc="right", fontsize=6.5); ax.set_ylabel("Im", loc="top", fontsize=6.5)
    return ax


def caption_note(ax, s, xy=(0.02, 0.97), fs=6.5, color=GRAY):
    ax.text(*xy, s, transform=ax.transAxes, fontsize=fs, color=color, va="top")


setup()
