#!/usr/bin/env python3
r"""Proton vs neutron from the REAL Bring color-tube coordinates, parameterized by q.

Nothing here is an ad-hoc embedding.  Every curve is computed from the
color-tube cubic of Bring's surface and the substrate parameter q.

DERIVATION CHAIN (all corpus-sourced, file refs below)
------------------------------------------------------
1. Color-tube coordinates  (brings-surface/color-tube-coordinates.md,
   color-tube-cubic.md): at spacetime ratio z = x0/x1 the three color
   charges r,g,b are the three roots c of the color-tube cubic

       c^3 + (4z+1)c^2 + (6z^2+3z+1)c + (4z^3+3z^2+2z+1) = 0.

   At the classical point z=0 the roots are exactly {-1, +i, -i}.

2. q enters explicitly (brings-surface/descartes-elliptic-curve.md):
   the coral fibre is the elliptic curve E_q with

       z(q) = sqrt(q) - 1/sqrt(q).

   At the substrate q0 = 1.1099785955 (qou_substrate.q_at, proton-anchored)
   => z0 = 0.10439, j(E_q0) = 129.9, Delta = -18.95.

3. The three color tubes = the three root branches c_r(z), c_g(z), c_b(z)
   tracked continuously as z runs around a worldline loop |z| = R in the
   base P^1.  The roots BRAID by the cubic's monodromy around the singular
   fibres (= the discriminant zeros).  Per coral-elliptic.md this monodromy
   recovers the trefoil holonomy generators H1,H2.  This is the genuine
   "coral" of twisted color tubes, not a drawn Borromean cartoon.

4. p vs n appear PHYSICALLY DIFFERENT via the color weighting
   (probe_k_ud_bring_color_tube_empirical_baseline.py):

       w(q,k) = 1 / (1 - h_q * q^(10+k)),   h_q = (q-1)/q,

   up-tube -> k=0 (reference), down-tube -> k=k_ud.  Tube radius is set by
   this weight, so:
       proton  (u,u,d): two u-tubes + one d-tube
       neutron (u,d,d): one u-tube + two d-tubes
   The d-tube is heavier (k_ud>0 => thicker), so the proton and neutron
   carry visibly different color-weight distributions.

HONESTY CAVEAT (do not oversell)
--------------------------------
The flavor-displacement exponent k_ud is an EXPLORATORY empirical baseline
(audit-only).  At q0 the implied m_d/m_u is ~1.0-1.17 across k in {-3..3},
which does NOT reach PDG 2.16 -- the *direction* (down heavier) is right,
the *magnitude* is not yet categorically derived.  The exact W_{c1,c2}
weighting is conjectural (conj:s5-so3-fiber-action).  Radius is drawn
proportional to (weight)^GAIN purely so the modest weight gap is legible;
GAIN is a display knob, not physics.

Output: scripts/knot-plots/proton-neutron-bring-color-tubes-q.png
Usage:  python3 scripts/knot-plots/proton-neutron-bring-color-tubes-q.py
        python3 ... --q 1.25         # see the tubes at a different q
        python3 ... --k-ud 2 --gain 3
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

DEFAULT_OUT = Path(__file__).parent / "proton-neutron-bring-color-tubes-q.png"

# Substrate parameter q0 (proton-anchored; qou_substrate.constants.q_at(50)).
Q0 = 1.1099785955418

TUBE_RGB = {
    "r": (0.86, 0.20, 0.22),
    "g": (0.18, 0.62, 0.28),
    "b": (0.20, 0.42, 0.86),
}

LOOP_R = 1.0            # worldline loop radius |z| = R that braids the roots
N_CURVE = 320           # samples along the loop
M_RING = 14             # tube cross-section resolution
BASE_TUBE_R = 0.045     # baseline tube radius (before weight scaling)


# ── Bring color-tube geometry ────────────────────────────────────────

def z_of_q(q: float) -> float:
    """Spacetime ratio of the coral fibre E_q (descartes-elliptic-curve.md)."""
    s = np.sqrt(q)
    return s - 1.0 / s


def cubic_roots(z: complex) -> np.ndarray:
    """Three roots c_r,c_g,c_b of the color-tube cubic at parameter z."""
    return np.roots([1.0, 4 * z + 1, 6 * z ** 2 + 3 * z + 1,
                     4 * z ** 3 + 3 * z ** 2 + 2 * z + 1])


def track_roots(loop_r: float, n: int) -> np.ndarray:
    """Continuously match the 3 roots as z runs the loop z = loop_r*e^{i phi}.

    Returns (n, 3) complex array; column j is one color tube's trajectory.
    """
    phi = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    zc = loop_r * np.exp(1j * phi)
    out = np.zeros((n, 3), dtype=complex)
    out[0] = cubic_roots(zc[0])
    for i in range(1, n):
        cand = cubic_roots(zc[i])
        prev = out[i - 1]
        used = [False, False, False]
        for a in range(3):
            d = [abs(cand[b] - prev[a]) if not used[b] else 1e18 for b in range(3)]
            b = int(np.argmin(d))
            used[b] = True
            out[i, a] = cand[b]
    return out


def color_order(first_roots: np.ndarray) -> list[int]:
    """Assign strand columns to (r, g, b) by a fixed rule at phi=0:
    most-negative real part -> r; of the rest, larger imag -> g, other -> b."""
    idx = list(range(3))
    r = min(idx, key=lambda j: first_roots[j].real)
    rest = [j for j in idx if j != r]
    g, b = sorted(rest, key=lambda j: -first_roots[j].imag)
    return [r, g, b]  # columns for r, g, b


# ── q-dependent color weighting (p vs n physical difference) ──────────

def bring_weight(q: float, k: int) -> float:
    """w(q,k) = 1/(1 - h_q q^{10+k}); h_q=(q-1)/q. up->k=0, down->k=k_ud."""
    h_q = (q - 1.0) / q
    return 1.0 / (1.0 - h_q * q ** (10 + k))


# ── tube meshing ─────────────────────────────────────────────────────

def parallel_transport_frame(curve: np.ndarray):
    n = len(curve)
    tang = np.roll(curve, -1, 0) - np.roll(curve, 1, 0)
    tang /= np.linalg.norm(tang, axis=1, keepdims=True)
    seed = np.array([0.0, 0.0, 1.0])
    if abs(np.dot(seed, tang[0])) > 0.9:
        seed = np.array([0.0, 1.0, 0.0])
    n1 = np.zeros_like(curve)
    n1[0] = seed - np.dot(seed, tang[0]) * tang[0]
    n1[0] /= np.linalg.norm(n1[0])
    for i in range(1, n):
        v = n1[i - 1] - np.dot(n1[i - 1], tang[i]) * tang[i]
        nv = np.linalg.norm(v)
        n1[i] = v / nv if nv > 1e-12 else n1[i - 1]
    n2 = np.cross(tang, n1)
    return n1, n2


def tube_faces(curve: np.ndarray, radius: float, closed: bool):
    n1, n2 = parallel_transport_frame(curve)
    theta = np.linspace(0.0, 2.0 * np.pi, M_RING, endpoint=False)
    ct, st = np.cos(theta), np.sin(theta)
    rings = (curve[:, None, :]
             + radius * (ct[None, :, None] * n1[:, None, :]
                         + st[None, :, None] * n2[:, None, :]))
    n = len(curve)
    last = n if closed else n - 1
    faces = []
    for i in range(last):
        j = (i + 1) % n
        for k in range(M_RING):
            kk = (k + 1) % M_RING
            faces.append([rings[i, k], rings[i, kk], rings[j, kk], rings[j, k]])
    return faces


def shade(rgb, faces):
    light = np.array([0.4, 0.55, 1.0])
    light /= np.linalg.norm(light)
    base = np.array(rgb)
    out = []
    for f in faces:
        f = np.asarray(f)
        nrm = np.cross(f[1] - f[0], f[2] - f[0])
        ln = np.linalg.norm(nrm)
        lam = 0.55 + 0.45 * max(0.0, float(np.dot(nrm / ln, light))) if ln > 1e-12 else 0.7
        out.append(tuple(np.clip(base * lam, 0, 1)))
    return out


# ── panel ────────────────────────────────────────────────────────────

def draw_panel(ax, tracks, cols, flavors, q, k_ud, gain, title):
    # Build 3D space curves: (Re c, Im c, height) where height = loop phase.
    n = tracks.shape[0]
    span = max(tracks.real.max() - tracks.real.min(),
               tracks.imag.max() - tracks.imag.min())
    height = np.linspace(-0.6 * span, 0.6 * span, n)

    w0 = bring_weight(q, 0)
    all_faces, all_colors = [], []
    for ck in ("r", "g", "b"):
        col = cols[ck]
        c = tracks[:, col]
        curve = np.stack([c.real, c.imag, height], axis=1)
        wk = bring_weight(q, 0 if flavors[ck] == "u" else k_ud)
        radius = BASE_TUBE_R * (wk / w0) ** gain
        faces = tube_faces(curve, radius, closed=False)
        all_faces.extend(faces)
        all_colors.extend(shade(TUBE_RGB[ck], faces))

    coll = Poly3DCollection(all_faces, facecolors=all_colors,
                            edgecolors="none", linewidths=0)
    ax.add_collection3d(coll)

    # Per-tube flavor + weight label near the top of each strand.
    for ck in ("r", "g", "b"):
        col = cols[ck]
        c = tracks[:, col]
        wk = bring_weight(q, 0 if flavors[ck] == "u" else k_ud)
        x, y, zt = c.real[-1], c.imag[-1], height[-1]
        ax.text(x, y, zt + 0.15 * span,
                f"${flavors[ck]}_{ck}$  w={wk:.3f}",
                fontsize=9, fontweight="bold",
                color=tuple(np.clip(np.array(TUBE_RGB[ck]) * 0.8, 0, 1)),
                ha="center")

    net = sum(bring_weight(q, 0 if flavors[ck] == "u" else k_ud)
              for ck in ("r", "g", "b"))
    ax.set_title(f"{title}\nflavors {''.join(flavors[c] for c in 'rgb')}   "
                 f"$\\Sigma w = {net:.3f}$",
                 fontsize=11, pad=0)
    lim = 0.6 * span + 0.4
    ax.set_xlim(-span / 2 - 0.4, span / 2 + 0.4)
    ax.set_ylim(-span / 2 - 0.4, span / 2 + 0.4)
    ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1.25))
    ax.set_axis_off()
    ax.view_init(elev=12, azim=35)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--q", type=float, default=Q0, help="substrate parameter q")
    ap.add_argument("--k-ud", type=int, default=3, help="flavor-displacement exponent")
    ap.add_argument("--gain", type=float, default=3.0, help="radius<-weight display gain")
    ap.add_argument("--output", "-o", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    q, k_ud, gain = args.q, args.k_ud, args.gain
    z0 = z_of_q(q)
    tracks = track_roots(LOOP_R, N_CURVE)
    cols_list = color_order(tracks[0])
    cols = {"r": cols_list[0], "g": cols_list[1], "b": cols_list[2]}

    w0, wk = bring_weight(q, 0), bring_weight(q, k_ud)
    md_mu = (1 - (q - 1) / q * q ** 10) / (1 - (q - 1) / q * q ** (10 + k_ud))
    roots_q0 = np.round(cubic_roots(z0), 3)

    fig = plt.figure(figsize=(12.5, 6.8))
    axp = fig.add_subplot(1, 2, 1, projection="3d")
    draw_panel(axp, tracks, cols, {"r": "u", "g": "u", "b": "d"},
               q, k_ud, gain, r"Proton $\mathfrak{p}=[u,u,d]$")
    axn = fig.add_subplot(1, 2, 2, projection="3d")
    draw_panel(axn, tracks, cols, {"r": "u", "g": "d", "b": "d"},
               q, k_ud, gain, r"Neutron $\mathfrak{n}=[u,d,d]$")

    fig.suptitle(
        "Proton vs Neutron — Bring color-tube roots, parameterized by $q$\n"
        f"$q_0={q:.7f}$   $z_0=\\sqrt{{q}}-1/\\sqrt{{q}}={z0:.5f}$   "
        f"$j(\\mathcal{{E}}_{{q_0}})=129.9$   roots$(q_0)=\\{{{roots_q0[0]},"
        f"{roots_q0[1]},{roots_q0[2]}\\}}$\n"
        f"color weights at $q_0$: $w_u={w0:.3f}$, $w_d={wk:.3f}$ "
        f"($k_{{ud}}={k_ud:+d}$, EXPLORATORY: implied $m_d/m_u={md_mu:.2f}$ "
        f"vs PDG 2.16; radius $\\propto w^{{{gain:g}}}$ for legibility)",
        fontsize=10.5, y=1.02)
    fig.tight_layout()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  wrote {args.output}")
    print(f"  q={q:.7f}  z0={z0:.5f}  roots(q0)={roots_q0.tolist()}")
    print(f"  w_u={w0:.5f}  w_d(k={k_ud:+d})={wk:.5f}  implied m_d/m_u={md_mu:.4f}")


if __name__ == "__main__":
    main()
