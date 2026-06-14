#!/usr/bin/env python3
"""3D color-tube render of the proton vs neutron as oriented Borromean rings.

Faithful to `content/.../observations/borromean-quark.md`:

  - A baryon is the Borromean link B_3 of three unknots (neutrinos)
    threaded through the (r, g, b) coral tubes of Bring's surface.
  - Up vs down quark = CROSSING ORIENTATION within B_3:
        up   u  ->  positive crossing (sigma_i)      orientation +
        down d  ->  negative crossing (sigma_i^{-1}) orientation -
  - proton  uud = 2+1 partition  (signs +,+,-)  net +1
    neutron udd = 1+2 partition  (signs +,-,-)  net -1
  - The net crossing-orientation sign is the triple Milnor invariant
    mu-bar_123 = +-1  ->  the chiral asymmetry between p and n.

IMPORTANT (per the .md): crossing orientation is NOT writhe; each strand
has self-writhe zero.  So orientation is drawn as a DIRECTION ARROW along
each tube (traversal sense), never as a helical self-twist of the tube.

The unoriented geometry of p and n is identical (both Borromean); only the
orientation decoration (which tube is u vs d) differs.  Between proton and
neutron exactly ONE tube (green) flips u -> d.

Output: scripts/knot-plots/proton-neutron-color-tubes-3d.png
Usage:  python3 scripts/knot-plots/proton-neutron-color-tubes-3d.py
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

DEFAULT_OUT = Path(__file__).parent / "proton-neutron-color-tubes-3d.png"

# Color-charge palette for the three coral tubes (r, g, b).
TUBE_RGB = {
    "r": (0.86, 0.20, 0.22),
    "g": (0.18, 0.62, 0.28),
    "b": (0.20, 0.42, 0.86),
}

# Borromean ellipse semi-axes.  Aspect ratio ~ golden ratio makes the three
# mutually perpendicular ellipses a genuine Borromean link (no two linked,
# all three inseparable).
A, B = 1.65, 1.02
TUBE_R = 0.16          # tube radius
N_CURVE = 240          # samples along each ellipse
M_RING = 18            # cross-section resolution


def borromean_curves() -> dict[str, np.ndarray]:
    """Three mutually perpendicular golden-ratio ellipses = Borromean rings.

    Returns {color_key: (N_CURVE, 3) array}.  Component order r, g, b sits in
    the yz-, zx-, xy-planes respectively.
    """
    t = np.linspace(0.0, 2.0 * np.pi, N_CURVE, endpoint=False)
    ct, st = np.cos(t), np.sin(t)
    zero = np.zeros_like(t)
    red = np.stack([zero, A * ct, B * st], axis=1)        # yz-plane
    green = np.stack([B * st, zero, A * ct], axis=1)       # zx-plane
    blue = np.stack([A * ct, B * st, zero], axis=1)        # xy-plane
    return {"r": red, "g": green, "b": blue}


def parallel_transport_frame(curve: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Tangent + two parallel-transported normals for a closed curve.

    Parallel transport keeps the cross-section from spinning (no spurious
    self-twist), honouring the .md's 'self-writhe zero' for each strand.
    """
    n = len(curve)
    nxt = np.roll(curve, -1, axis=0)
    prv = np.roll(curve, 1, axis=0)
    tang = nxt - prv
    tang /= np.linalg.norm(tang, axis=1, keepdims=True)

    # Seed a normal perpendicular to the first tangent.
    seed = np.array([0.0, 0.0, 1.0])
    if abs(np.dot(seed, tang[0])) > 0.9:
        seed = np.array([0.0, 1.0, 0.0])
    n1 = np.zeros_like(curve)
    n1[0] = seed - np.dot(seed, tang[0]) * tang[0]
    n1[0] /= np.linalg.norm(n1[0])

    # Transport the normal along the curve by rotating with each tangent step.
    for i in range(1, n):
        v = n1[i - 1] - np.dot(n1[i - 1], tang[i]) * tang[i]
        nv = np.linalg.norm(v)
        n1[i] = v / nv if nv > 1e-12 else n1[i - 1]
    n2 = np.cross(tang, n1)
    return tang, n1, n2


def tube_quads(curve: np.ndarray, radius: float) -> list[np.ndarray]:
    """Build quad faces of a tube swept along a closed curve."""
    tang, n1, n2 = parallel_transport_frame(curve)
    theta = np.linspace(0.0, 2.0 * np.pi, M_RING, endpoint=False)
    ct, st = np.cos(theta), np.sin(theta)
    # ring[i] : (M_RING, 3) cross-section circle at curve[i]
    rings = (
        curve[:, None, :]
        + radius * (ct[None, :, None] * n1[:, None, :]
                    + st[None, :, None] * n2[:, None, :])
    )
    n = len(curve)
    faces = []
    for i in range(n):
        j = (i + 1) % n
        for k in range(M_RING):
            kk = (k + 1) % M_RING
            faces.append(np.array([rings[i, k], rings[i, kk],
                                    rings[j, kk], rings[j, k]]))
    return faces


def shade(rgb, faces):
    """Cheap lambert-ish shading so the tube reads as 3D."""
    light = np.array([0.4, 0.5, 1.0])
    light /= np.linalg.norm(light)
    out = []
    base = np.array(rgb)
    for f in faces:
        nrm = np.cross(f[1] - f[0], f[2] - f[0])
        ln = np.linalg.norm(nrm)
        lam = 0.55 + 0.45 * max(0.0, np.dot(nrm / ln, light)) if ln > 1e-12 else 0.7
        out.append(tuple(np.clip(base * lam, 0, 1)))
    return out


def draw_baryon(ax, flavors: dict[str, str], title: str, flip_key: str | None = None):
    """Draw one baryon: 3 color tubes + orientation arrows + labels.

    flavors maps color key -> 'u' or 'd'.  u = orientation +1, d = -1.
    flip_key (optional) highlights the tube whose orientation differs from
    the proton (the chiral-asymmetry carrier).
    """
    curves = borromean_curves()
    all_faces, all_colors = [], []
    for ck in ("r", "g", "b"):
        faces = tube_quads(curves[ck], TUBE_R)
        all_faces.extend(faces)
        all_colors.extend(shade(TUBE_RGB[ck], faces))

    # One Poly3DCollection for all tubes => correct per-polygon depth sort,
    # so the Borromean over/under crossings render correctly.
    coll = Poly3DCollection(all_faces, facecolors=all_colors,
                            edgecolors="none", linewidths=0)
    coll.set_sort_zpos(0)
    ax.add_collection3d(coll)

    # Orientation arrows: traversal direction = +tangent for u, -tangent for d.
    # Many bold arrows per tube so the "flow direction" (= quark chirality) is
    # unmistakable; the tube that flips between p and n visibly reverses.
    n_arrows = 8
    for ck in ("r", "g", "b"):
        c = curves[ck]
        tang, _, _ = parallel_transport_frame(c)
        sign = +1.0 if flavors[ck] == "u" else -1.0
        acolor = "#111111" if ck != flip_key else "#ff8800"
        for a in range(n_arrows):
            idx = (a * N_CURVE) // n_arrows
            p = c[idx]
            d = sign * tang[idx] * 0.62
            ax.quiver(p[0], p[1], p[2], d[0], d[1], d[2],
                      color=acolor, linewidth=2.4 if ck == flip_key else 1.8,
                      arrow_length_ratio=0.55, zorder=10)

    # Per-tube flavor label at a representative point.
    for ck in ("r", "g", "b"):
        c = curves[ck]
        p = c[N_CURVE // 12]
        fl = flavors[ck]
        sgn = "+" if fl == "u" else "-"
        lab = f"${fl}_{{{ck}}}\\,({sgn})$"
        if ck == flip_key:
            lab += r"  $\Leftarrow$ flips"
        ax.text(p[0] * 1.20, p[1] * 1.20, p[2] * 1.20, lab,
                fontsize=12, fontweight="bold",
                color="#ff8800" if ck == flip_key
                else tuple(np.clip(np.array(TUBE_RGB[ck]) * 0.8, 0, 1)),
                ha="center", va="center")

    net = sum(+1 if flavors[ck] == "u" else -1 for ck in ("r", "g", "b"))
    ax.set_title(f"{title}\n"
                 f"$\\bar\\mu_{{123}} = {net:+d}$  "
                 f"(net crossing orientation = chiral charge)",
                 fontsize=12, pad=2)

    lim = A + 0.3
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.view_init(elev=22, azim=35)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", "-o", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    fig = plt.figure(figsize=(12, 6.4))

    # proton uud : r=u, g=u, b=d   -> (+,+,-) net +1
    axp = fig.add_subplot(1, 2, 1, projection="3d")
    draw_baryon(axp, {"r": "u", "g": "u", "b": "d"},
                r"Proton $\mathfrak{p}=[u,u,d]$")

    # neutron udd : r=u, g=d, b=d  -> (+,-,-) net -1  (green tube flips u->d)
    axn = fig.add_subplot(1, 2, 2, projection="3d")
    draw_baryon(axn, {"r": "u", "g": "d", "b": "d"},
                r"Neutron $\mathfrak{n}=[u,d,d]$", flip_key="g")

    fig.suptitle(
        "Proton vs Neutron: oriented Borromean color tubes\n"
        "same unoriented link  ·  chiral asymmetry = orientation of the "
        "green tube (u$\\to$d), flipping $\\bar\\mu_{123}$ from $+1$ to $-1$",
        fontsize=13, fontweight="bold", y=1.02,
    )
    fig.tight_layout()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print(f"  wrote {args.output}")


if __name__ == "__main__":
    main()
