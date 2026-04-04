#!/usr/bin/env python3
"""
Generate publication-quality knot diagram SVGs for the QOU paper.

Produces clean knot projections with proper over/under crossings,
matching the knot-particle dictionary (§4 knot-notation-convention).

Knot types generated:
  - Unknot (0_1)        → neutrino
  - Trefoil (3_1)       → electron  (torus knot T_{2,3})
  - Figure-eight (4_1)  → muon
  - Cinquefoil (5_1)    → tau       (torus knot T_{2,5})
  - Torus knot T_{2,7}  → charm     (7_1)
  - Torus knot T_{3,4}  → top       (8_{19})
  - Hopf link (L2a1)    → gluon
  - Borromean rings      → baryon binding

Output: scripts/knot-plots/<name>.svg

Usage:
  python3 scripts/generate-knot-plots.py
  python3 scripts/generate-knot-plots.py --output content/.../rendered/
  python3 scripts/generate-knot-plots.py --knot trefoil
"""

import argparse
import os
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from pathlib import Path


# ── Configuration ────────────────────────────────────────────────────

DEFAULT_OUTPUT = Path(__file__).parent / "knot-plots"

# Color palette matching the paper's style
COLORS = {
    "knot_primary": "#2255aa",
    "knot_secondary": "#aa2255",
    "knot_tertiary": "#22aa55",
    "crossing_bg": "white",
    "link_a": "#2255aa",
    "link_b": "#cc4422",
    "link_c": "#22aa55",
}

LINEWIDTH = 2.8
GAP_WIDTH = 5.0  # width of crossing gap (in linewidths)
FIG_SIZE = (3.0, 3.0)
DPI = 150


# ── Torus knot parametric curve ──────────────────────────────────────

def torus_knot_3d(p: int, n: int, num_points: int = 2000,
                  R: float = 2.0, r: float = 0.8):
    """
    Parametric curve for T_{p,n} torus knot in 3D.
    Winds p times around the hole and n times around the tube.
    """
    t = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = (R + r * np.cos(n * t)) * np.cos(p * t)
    y = (R + r * np.cos(n * t)) * np.sin(p * t)
    z = r * np.sin(n * t)
    return x, y, z, t


def project_knot(x, y, z, angle_x=0.3, angle_z=0.0):
    """Project 3D knot to 2D with a slight tilt for good crossing visibility."""
    # Rotate around x-axis
    y2 = y * np.cos(angle_x) - z * np.sin(angle_x)
    z2 = y * np.sin(angle_x) + z * np.cos(angle_x)
    # Rotate around z-axis
    x3 = x * np.cos(angle_z) - y2 * np.sin(angle_z)
    y3 = x * np.sin(angle_z) + y2 * np.cos(angle_z)
    return x3, y3, z2


# ── Crossing detection ──────────────────────────────────────────────

def find_crossings(x, y, z, threshold=0.15):
    """
    Find approximate crossing locations in the 2D projection.
    Returns list of (i, j, over_idx) where i is the over-strand index
    and j is the under-strand index at the crossing point.
    """
    n = len(x)
    crossings = []
    # Coarse grid search
    step = max(1, n // 400)
    for i in range(0, n, step):
        for j in range(i + n // 8, n, step):
            if abs(j - i) < n // 8 or abs(j - i) > 7 * n // 8:
                continue
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            dist = math.sqrt(dx * dx + dy * dy)
            if dist < threshold:
                # Higher z is the over-strand
                over = i if z[i] > z[j] else j
                under = j if over == i else i
                # Check not too close to existing crossing
                is_dup = False
                for ci, cj, _ in crossings:
                    if (abs(ci - i) < n // 16 and abs(cj - j) < n // 16):
                        is_dup = True
                        break
                    if (abs(ci - j) < n // 16 and abs(cj - i) < n // 16):
                        is_dup = True
                        break
                if not is_dup:
                    crossings.append((over, under, over))
    return crossings


# ── Drawing functions ────────────────────────────────────────────────

def draw_knot_with_crossings(ax, x, y, z, color=COLORS["knot_primary"],
                             lw=LINEWIDTH, label=None):
    """
    Draw a knot projection with proper crossing gaps.
    The under-strand gets a white gap at each crossing.
    """
    n = len(x)
    crossings = find_crossings(x, y, z)

    # Build a mask for gap regions (under-strand near crossings)
    gap_mask = np.zeros(n, dtype=bool)
    gap_radius = max(8, n // 120)

    for over_i, under_i, _ in crossings:
        lo = (under_i - gap_radius) % n
        hi = (under_i + gap_radius) % n
        if lo < hi:
            gap_mask[lo:hi] = True
        else:
            gap_mask[lo:] = True
            gap_mask[:hi] = True

    # Draw the under-strand segments (with gaps)
    # First draw white background for gap effect
    for over_i, under_i, _ in crossings:
        lo = max(0, under_i - gap_radius - 2)
        hi = min(n, under_i + gap_radius + 2)
        indices = list(range(lo, hi))
        ax.plot(x[indices], y[indices], color="white",
                linewidth=lw + GAP_WIDTH, solid_capstyle="round", zorder=1)

    # Draw the full knot curve in segments
    # Split at gaps for clean rendering
    segments = []
    current_segment = []
    for i in range(n):
        if not gap_mask[i]:
            current_segment.append(i)
        else:
            if current_segment:
                segments.append(current_segment)
            current_segment = []
    if current_segment:
        # Connect last to first if no gap between them
        if segments and not gap_mask[0]:
            segments[0] = current_segment + segments[0]
        else:
            segments.append(current_segment)

    for seg in segments:
        if len(seg) < 2:
            continue
        ax.plot(x[seg], y[seg], color=color, linewidth=lw,
                solid_capstyle="round", zorder=2)

    # Draw over-strands on top
    for over_i, under_i, _ in crossings:
        lo = max(0, over_i - gap_radius)
        hi = min(n, over_i + gap_radius)
        indices = list(range(lo, hi))
        if len(indices) > 1:
            ax.plot(x[indices], y[indices], color=color, linewidth=lw,
                    solid_capstyle="round", zorder=3)


def setup_axes(ax):
    """Configure axes for clean knot diagram output."""
    ax.set_aspect("equal")
    ax.axis("off")
    ax.margins(0.1)


def save_svg(fig, path: Path, name: str):
    """Save figure as SVG."""
    path.mkdir(parents=True, exist_ok=True)
    filepath = path / f"{name}.svg"
    fig.savefig(filepath, format="svg", bbox_inches="tight",
                transparent=True, pad_inches=0.05)
    plt.close(fig)
    print(f"  ✓ {filepath}")
    return filepath


# ── Individual knot generators ───────────────────────────────────────

def generate_unknot(output: Path):
    """Unknot (0_1) — neutrino."""
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    t = np.linspace(0, 2 * np.pi, 200)
    x = np.cos(t)
    y = np.sin(t)
    ax.plot(x, y, color=COLORS["knot_primary"], linewidth=LINEWIDTH,
            solid_capstyle="round")
    setup_axes(ax)
    return save_svg(fig, output, "unknot-0_1")


def generate_trefoil(output: Path):
    """Trefoil knot (3_1) — electron. Torus knot T_{2,3}."""
    x, y, z, _ = torus_knot_3d(2, 3, num_points=2000)
    xp, yp, zp = project_knot(x, y, z, angle_x=0.35)

    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_knot_with_crossings(ax, xp, yp, zp, color=COLORS["knot_primary"])
    setup_axes(ax)
    return save_svg(fig, output, "trefoil-3_1")


def generate_figure_eight(output: Path):
    """Figure-eight knot (4_1) — muon. Parametric projection."""
    t = np.linspace(0, 2 * np.pi, 2000, endpoint=False)
    # Classic figure-eight parametrization (Lissajous-like)
    x = (2 + np.cos(2 * t)) * np.cos(3 * t)
    y = (2 + np.cos(2 * t)) * np.sin(3 * t)
    z = np.sin(4 * t)

    xp, yp, zp = project_knot(x, y, z, angle_x=0.2)

    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_knot_with_crossings(ax, xp, yp, zp, color=COLORS["knot_primary"])
    setup_axes(ax)
    return save_svg(fig, output, "figure-eight-4_1")


def generate_cinquefoil(output: Path):
    """Cinquefoil knot (5_1) — tau. Torus knot T_{2,5}."""
    x, y, z, _ = torus_knot_3d(2, 5, num_points=2000)
    xp, yp, zp = project_knot(x, y, z, angle_x=0.35)

    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_knot_with_crossings(ax, xp, yp, zp, color=COLORS["knot_primary"])
    setup_axes(ax)
    return save_svg(fig, output, "cinquefoil-5_1")


def generate_torus_2_7(output: Path):
    """T_{2,7} torus knot (7_1) — charm quark."""
    x, y, z, _ = torus_knot_3d(2, 7, num_points=3000)
    xp, yp, zp = project_knot(x, y, z, angle_x=0.35)

    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_knot_with_crossings(ax, xp, yp, zp, color=COLORS["knot_primary"])
    setup_axes(ax)
    return save_svg(fig, output, "torus-2_7-knot")


def generate_torus_3_4(output: Path):
    """T_{3,4} torus knot (8_{19}) — top quark."""
    x, y, z, _ = torus_knot_3d(3, 4, num_points=3000)
    xp, yp, zp = project_knot(x, y, z, angle_x=0.4)

    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_knot_with_crossings(ax, xp, yp, zp, color=COLORS["knot_primary"])
    setup_axes(ax)
    return save_svg(fig, output, "torus-3_4-knot")


def generate_hopf_link(output: Path):
    """Hopf link (L2a1) — gluon. Two linked unknots."""
    t = np.linspace(0, 2 * np.pi, 1000, endpoint=False)

    # Two linked circles (Hopf link as T_{2,2} components)
    R, r = 1.5, 0.7
    # Component 1: circle in xz-plane, shifted
    x1 = R * np.cos(t)
    y1 = r * np.sin(t)
    z1 = np.zeros_like(t)

    # Component 2: circle in yz-plane, shifted and linked
    x2 = r * np.sin(t)
    y2 = R * np.cos(t)
    z2 = r * np.cos(t) * 0.3

    # Tilt both for nice projection
    x1p, y1p, z1p = project_knot(x1, y1, z1, angle_x=0.5)
    x2p, y2p, z2p = project_knot(x2, y2, z2, angle_x=0.5)

    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)

    # Draw with manual crossing handling for the link
    # Component 1 (behind)
    ax.plot(x1p, y1p, color=COLORS["link_a"], linewidth=LINEWIDTH,
            solid_capstyle="round", zorder=1, alpha=0.95)
    # Component 2 (in front at crossings)
    ax.plot(x2p, y2p, color=COLORS["link_b"], linewidth=LINEWIDTH,
            solid_capstyle="round", zorder=2, alpha=0.95)

    setup_axes(ax)
    return save_svg(fig, output, "hopf-link-L2a1")


def generate_borromean(output: Path):
    """Borromean rings — baryon binding (three mutually linked unknots)."""
    t = np.linspace(0, 2 * np.pi, 1000, endpoint=False)
    R = 1.5

    # Three orthogonal circles
    # Circle 1: xy-plane
    x1 = R * np.cos(t)
    y1 = R * np.sin(t)
    z1 = np.zeros_like(t)

    # Circle 2: xz-plane
    x2 = R * np.cos(t)
    y2 = np.zeros_like(t)
    z2 = R * np.sin(t)

    # Circle 3: yz-plane
    x3 = np.zeros_like(t)
    y3 = R * np.cos(t)
    z3 = R * np.sin(t)

    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)

    for xs, ys, zs, color, zo in [
        (x1, y1, z1, COLORS["link_a"], 1),
        (x2, y2, z2, COLORS["link_b"], 2),
        (x3, y3, z3, COLORS["link_c"], 3),
    ]:
        xp, yp, zp = project_knot(xs, ys, zs, angle_x=0.55, angle_z=0.3)
        ax.plot(xp, yp, color=color, linewidth=LINEWIDTH,
                solid_capstyle="round", zorder=zo, alpha=0.9)

    setup_axes(ax)
    return save_svg(fig, output, "borromean-rings")


def generate_mirror_pair(output: Path):
    """
    Trefoil chirality pair — electron/positron.
    Left trefoil (T_{2,3}) and right trefoil (T_{2,-3}) side by side.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.0, 3.0))

    # Left trefoil
    x, y, z, _ = torus_knot_3d(2, 3, num_points=2000)
    xp, yp, zp = project_knot(x, y, z, angle_x=0.35)
    draw_knot_with_crossings(ax1, xp, yp, zp, color=COLORS["knot_primary"])
    ax1.set_title(r"$T_{2,3}$ (electron $e^-$)", fontsize=10, pad=8)
    setup_axes(ax1)

    # Right trefoil (mirror)
    draw_knot_with_crossings(ax2, -xp, yp, zp, color=COLORS["knot_secondary"])
    ax2.set_title(r"$T_{2,3}^{\sigma}$ (positron $e^+$)", fontsize=10, pad=8)
    setup_axes(ax2)

    fig.tight_layout()
    return save_svg(fig, output, "trefoil-chirality-pair")


def generate_particle_gallery(output: Path):
    """
    Complete knot-particle dictionary as a single figure.
    Layout: 2 rows x 4 columns showing all fundamental particle knots.
    """
    fig, axes = plt.subplots(2, 4, figsize=(12, 6))

    knots = [
        # (title, generator_params, ax_position)
        ("Photon $\\gamma$\n(empty)", None, (0, 0)),
        ("Neutrino $\\nu$\n(unknot $0_1$)", "unknot", (0, 1)),
        ("Gluon $g$\n(Hopf link)", "hopf", (0, 2)),
        ("Electron $e^-$\n($3_1$, $T_{2,3}$)", (2, 3), (0, 3)),
        ("Muon $\\mu$\n($4_1$, fig-eight)", "figure_eight", (1, 0)),
        ("Tau $\\tau$\n($5_1$, $T_{2,5}$)", (2, 5), (1, 1)),
        ("Charm $c$\n($7_1$, $T_{2,7}$)", (2, 7), (1, 2)),
        ("Top $t$\n($8_{19}$, $T_{3,4}$)", (3, 4), (1, 3)),
    ]

    for title, params, (row, col) in knots:
        ax = axes[row, col]

        if params is None:
            # Photon — empty/point
            ax.plot(0, 0, "o", color=COLORS["knot_primary"], markersize=8)
            ax.set_xlim(-1, 1)
            ax.set_ylim(-1, 1)
        elif params == "unknot":
            theta = np.linspace(0, 2 * np.pi, 200)
            ax.plot(np.cos(theta), np.sin(theta),
                    color=COLORS["knot_primary"], linewidth=LINEWIDTH)
        elif params == "hopf":
            theta = np.linspace(0, 2 * np.pi, 500)
            R, r_val = 1.2, 0.6
            x1 = R * np.cos(theta)
            y1 = r_val * np.sin(theta)
            x2 = r_val * np.sin(theta)
            y2 = R * np.cos(theta)
            x1p, y1p, _ = project_knot(x1, y1, np.zeros_like(theta), 0.5)
            x2p, y2p, _ = project_knot(x2, y2,
                                       r_val * np.cos(theta) * 0.3, 0.5)
            ax.plot(x1p, y1p, color=COLORS["link_a"],
                    linewidth=LINEWIDTH - 0.5)
            ax.plot(x2p, y2p, color=COLORS["link_b"],
                    linewidth=LINEWIDTH - 0.5)
        elif params == "figure_eight":
            theta = np.linspace(0, 2 * np.pi, 2000, endpoint=False)
            xf = (2 + np.cos(2 * theta)) * np.cos(3 * theta)
            yf = (2 + np.cos(2 * theta)) * np.sin(3 * theta)
            zf = np.sin(4 * theta)
            xp, yp, zp = project_knot(xf, yf, zf, angle_x=0.2)
            draw_knot_with_crossings(ax, xp, yp, zp,
                                     color=COLORS["knot_primary"],
                                     lw=LINEWIDTH - 0.5)
        elif isinstance(params, tuple):
            p, n = params
            x3d, y3d, z3d, _ = torus_knot_3d(p, n, num_points=2500)
            xp, yp, zp = project_knot(x3d, y3d, z3d, angle_x=0.35)
            draw_knot_with_crossings(ax, xp, yp, zp,
                                     color=COLORS["knot_primary"],
                                     lw=LINEWIDTH - 0.5)

        ax.set_title(title, fontsize=9, pad=6)
        setup_axes(ax)

    fig.suptitle("Knot–Particle Dictionary", fontsize=13, y=1.02,
                 fontweight="bold")
    fig.tight_layout()
    return save_svg(fig, output, "knot-particle-gallery")


# ── Main ─────────────────────────────────────────────────────────────

KNOT_GENERATORS = {
    "unknot": generate_unknot,
    "trefoil": generate_trefoil,
    "figure-eight": generate_figure_eight,
    "cinquefoil": generate_cinquefoil,
    "torus-2-7": generate_torus_2_7,
    "torus-3-4": generate_torus_3_4,
    "hopf-link": generate_hopf_link,
    "borromean": generate_borromean,
    "chirality-pair": generate_mirror_pair,
    "gallery": generate_particle_gallery,
}


def main():
    parser = argparse.ArgumentParser(
        description="Generate knot diagram SVGs for QOU paper")
    parser.add_argument(
        "--output", "-o", type=Path, default=DEFAULT_OUTPUT,
        help="Output directory for SVG files")
    parser.add_argument(
        "--knot", "-k", type=str, default=None,
        choices=list(KNOT_GENERATORS.keys()),
        help="Generate a specific knot (default: all)")
    parser.add_argument(
        "--list", action="store_true",
        help="List available knot types")
    args = parser.parse_args()

    if args.list:
        print("Available knot types:")
        for name in KNOT_GENERATORS:
            print(f"  {name}")
        return

    print(f"Generating knot plots → {args.output}/")

    if args.knot:
        KNOT_GENERATORS[args.knot](args.output)
    else:
        for name, gen_fn in KNOT_GENERATORS.items():
            gen_fn(args.output)

    print("\nDone. SVGs ready for inclusion in content blocks.")


if __name__ == "__main__":
    main()
