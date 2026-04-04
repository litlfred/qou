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
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
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
GAP_WIDTH = 5.0  # absolute gap width in points, added to linewidth
FIG_SIZE = (3.0, 3.0)


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


def figure_eight_3d(num_points: int = 2000, R: float = 2.0, r: float = 1.0):
    """Parametric curve for the figure-eight knot (4_1)."""
    t = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = (R + r * np.cos(2 * t)) * np.cos(3 * t)
    y = (R + r * np.cos(2 * t)) * np.sin(3 * t)
    z = r * np.sin(4 * t)
    return x, y, z


def project_knot(x, y, z, angle_x=0.3, angle_y=0.2, angle_z=0.0):
    """Project 3D knot to 2D via successive rotations (Euler angles)."""
    # Rotate around x-axis
    y2 = y * np.cos(angle_x) - z * np.sin(angle_x)
    z2 = y * np.sin(angle_x) + z * np.cos(angle_x)
    # Rotate around y-axis
    x2 = x * np.cos(angle_y) + z2 * np.sin(angle_y)
    z3 = -x * np.sin(angle_y) + z2 * np.cos(angle_y)
    # Rotate around z-axis
    x3 = x2 * np.cos(angle_z) - y2 * np.sin(angle_z)
    y3 = x2 * np.sin(angle_z) + y2 * np.cos(angle_z)
    return x3, y3, z3


# ── Crossing detection ──────────────────────────────────────────────

def find_crossings(x, y, z, threshold=None):
    """
    Find approximate crossing locations in the 2D projection.
    Returns list of (over_idx, under_idx) tuples.

    The threshold is auto-derived from the curve's bounding box if not
    provided, making detection robust to changes in scale or point count.
    """
    n = len(x)
    if threshold is None:
        bbox = max(x.max() - x.min(), y.max() - y.min())
        threshold = bbox * 0.04  # ~4% of bounding box

    crossings = []
    min_sep = max(3, n // 200)  # minimum index separation for dedup
    skip_near = max(3, n // 8)  # skip neighbors on the curve

    step = max(1, n // 400)
    for i in range(0, n, step):
        for j in range(i + skip_near, n, step):
            if abs(j - i) < skip_near or abs(j - i) > n - skip_near:
                continue
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            dist = math.sqrt(dx * dx + dy * dy)
            if dist < threshold:
                over = i if z[i] > z[j] else j
                under = j if over == i else i
                # Deduplicate nearby crossings
                is_dup = False
                for co, cu in crossings:
                    if (abs(co - over) < min_sep and abs(cu - under) < min_sep):
                        is_dup = True
                        break
                    if (abs(co - under) < min_sep and abs(cu - over) < min_sep):
                        is_dup = True
                        break
                if not is_dup:
                    crossings.append((over, under))
    return crossings


# ── Drawing functions ────────────────────────────────────────────────

def draw_knot_with_crossings(ax, x, y, z, color=COLORS["knot_primary"],
                             lw=LINEWIDTH):
    """
    Draw a knot projection with proper crossing gaps.
    The under-strand gets a white gap at each crossing.
    """
    n = len(x)
    crossings = find_crossings(x, y, z)

    # Build a mask for gap regions (under-strand near crossings)
    gap_mask = np.zeros(n, dtype=bool)
    gap_radius = max(8, n // 120)

    for over_i, under_i in crossings:
        lo = (under_i - gap_radius) % n
        hi = (under_i + gap_radius) % n
        if lo < hi:
            gap_mask[lo:hi] = True
        else:
            gap_mask[lo:] = True
            gap_mask[:hi] = True

    # Draw white background for gap effect (with wrap-around)
    for _, under_i in crossings:
        indices = np.arange(
            under_i - gap_radius - 2, under_i + gap_radius + 3
        ) % n
        ax.plot(x[indices], y[indices], color=COLORS["crossing_bg"],
                linewidth=lw + GAP_WIDTH, solid_capstyle="round", zorder=1)

    # Draw the knot curve in segments, splitting at gaps
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
    for over_i, _ in crossings:
        indices = np.arange(
            over_i - gap_radius, over_i + gap_radius
        ) % n
        if len(indices) > 1:
            ax.plot(x[indices], y[indices], color=color, linewidth=lw,
                    solid_capstyle="round", zorder=3)


def draw_link_component_with_crossings(ax, x, y, z, all_x, all_y, all_z,
                                        color, lw=LINEWIDTH):
    """
    Draw one component of a multi-component link with proper crossings
    against ALL components (including other ones).

    (all_x, all_y, all_z) is the concatenation of every component's points.
    (x, y, z) is this component's points. The function finds where this
    component passes under other components and draws gaps.
    """
    n = len(x)
    na = len(all_x)

    gap_radius = max(6, n // 100)
    bbox = max(all_x.max() - all_x.min(), all_y.max() - all_y.min())
    threshold = bbox * 0.045

    # Find crossings between this component and all points
    gap_mask = np.zeros(n, dtype=bool)
    step = max(1, n // 300)

    for i in range(0, n, step):
        for j in range(0, na, step):
            dx = x[i] - all_x[j]
            dy = y[i] - all_y[j]
            dist = math.sqrt(dx * dx + dy * dy)
            if dist < threshold:
                # Skip self-crossings of nearby points
                # (handled by same-index proximity)
                if z[i] < all_z[j]:
                    # This component is UNDER at this point → gap
                    lo = (i - gap_radius) % n
                    hi = (i + gap_radius) % n
                    if lo < hi:
                        gap_mask[lo:hi] = True
                    else:
                        gap_mask[lo:] = True
                        gap_mask[:hi] = True

    # Draw white gaps
    gap_indices = np.where(gap_mask)[0]
    if len(gap_indices) > 0:
        # Find contiguous gap runs
        runs = np.split(gap_indices, np.where(np.diff(gap_indices) > 1)[0] + 1)
        for run in runs:
            expanded = np.arange(run[0] - 2, run[-1] + 3) % n
            ax.plot(x[expanded], y[expanded], color="white",
                    linewidth=lw + GAP_WIDTH, solid_capstyle="round", zorder=1)

    # Draw the curve in segments
    segments = []
    current = []
    for i in range(n):
        if not gap_mask[i]:
            current.append(i)
        else:
            if current:
                segments.append(current)
            current = []
    if current:
        if segments and not gap_mask[0]:
            segments[0] = current + segments[0]
        else:
            segments.append(current)

    for seg in segments:
        if len(seg) < 2:
            continue
        ax.plot(x[seg], y[seg], color=color, linewidth=lw,
                solid_capstyle="round", zorder=2)


def setup_axes(ax):
    """Configure axes for clean knot diagram output."""
    ax.set_aspect("equal")
    ax.axis("off")
    ax.margins(0.1)


def save_svg(fig, path: Path, name: str):
    """Save figure as SVG with deterministic metadata."""
    path.mkdir(parents=True, exist_ok=True)
    filepath = path / f"{name}.svg"
    fig.savefig(filepath, format="svg", bbox_inches="tight",
                transparent=True, pad_inches=0.05,
                metadata={"Date": None})
    plt.close(fig)
    print(f"  ✓ {filepath}")
    return filepath


# ── Reusable drawing helpers (used by both individual and gallery) ───

def draw_unknot_on_ax(ax, color=COLORS["knot_primary"], lw=LINEWIDTH):
    """Draw an unknot (simple circle) on the given axes."""
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(t), np.sin(t), color=color, linewidth=lw,
            solid_capstyle="round")


def draw_torus_knot_on_ax(ax, p, n, color=COLORS["knot_primary"],
                           lw=LINEWIDTH, num_points=2000, angle_x=0.35):
    """Draw a torus knot T_{p,n} on the given axes."""
    x, y, z, _ = torus_knot_3d(p, n, num_points=num_points)
    xp, yp, zp = project_knot(x, y, z, angle_x=angle_x, angle_y=0.0)
    draw_knot_with_crossings(ax, xp, yp, zp, color=color, lw=lw)


def draw_figure_eight_on_ax(ax, color=COLORS["knot_primary"], lw=LINEWIDTH):
    """Draw a figure-eight knot on the given axes."""
    x, y, z = figure_eight_3d(2000)
    xp, yp, zp = project_knot(x, y, z, angle_x=0.2, angle_y=0.0)
    draw_knot_with_crossings(ax, xp, yp, zp, color=color, lw=lw)


def draw_hopf_link_on_ax(ax, lw=LINEWIDTH):
    """Draw a Hopf link with proper inter-component crossings."""
    t = np.linspace(0, 2 * np.pi, 800, endpoint=False)
    R, r = 1.5, 0.7

    # Component 1: tilted circle
    x1 = R * np.cos(t)
    y1 = r * np.sin(t)
    z1 = 0.3 * np.sin(t)

    # Component 2: orthogonal tilted circle, linked through component 1
    x2 = r * np.sin(t)
    y2 = R * np.cos(t)
    z2 = 0.3 * np.cos(t)

    # Project both
    x1p, y1p, z1p = project_knot(x1, y1, z1, angle_x=0.5, angle_y=0.0)
    x2p, y2p, z2p = project_knot(x2, y2, z2, angle_x=0.5, angle_y=0.0)

    # Concatenate all points for inter-component crossing detection
    all_x = np.concatenate([x1p, x2p])
    all_y = np.concatenate([y1p, y2p])
    all_z = np.concatenate([z1p, z2p])

    draw_link_component_with_crossings(
        ax, x1p, y1p, z1p, all_x, all_y, all_z, COLORS["link_a"], lw)
    draw_link_component_with_crossings(
        ax, x2p, y2p, z2p, all_x, all_y, all_z, COLORS["link_b"], lw)


def draw_borromean_on_ax(ax, lw=LINEWIDTH):
    """
    Draw Borromean rings — three pairwise-unlinked rings that are
    collectively inseparable.

    Uses offset ellipses (not centered orthogonal circles, which
    would be mutually Hopf-linked).  The standard Borromean
    construction places three coplanar ellipses at 120° with
    alternating over/under at each pairwise intersection.
    """
    t = np.linspace(0, 2 * np.pi, 800, endpoint=False)
    R = 1.4
    r_minor = 0.85

    # Three ellipses at 120° offsets, slightly shifted so each pair
    # intersects but no pair is linked.
    components = []
    for k, color in enumerate([COLORS["link_a"], COLORS["link_b"],
                                COLORS["link_c"]]):
        angle = k * 2 * np.pi / 3
        # Ellipse in its local frame
        ex = R * np.cos(t)
        ey = r_minor * np.sin(t)
        ez = np.zeros_like(t)

        # Rotate into position (tilted so they interlock in 3D)
        ca, sa = np.cos(angle), np.sin(angle)
        # Rotate around z by angle, then tilt around x
        tilt = 0.55
        ct, st = np.cos(tilt), np.sin(tilt)

        x = ca * ex - sa * (ey * ct)
        y = sa * ex + ca * (ey * ct)
        z = ey * st + 0.15 * np.sin(2 * t + k * 2.1)  # slight z-wobble

        # Offset center so rings interleave
        x += 0.3 * np.cos(angle)
        y += 0.3 * np.sin(angle)

        xp, yp, zp = project_knot(x, y, z, angle_x=0.35,
                                   angle_y=0.25, angle_z=0.0)
        components.append((xp, yp, zp, color))

    # Concatenate all for inter-component crossing detection
    all_x = np.concatenate([c[0] for c in components])
    all_y = np.concatenate([c[1] for c in components])
    all_z = np.concatenate([c[2] for c in components])

    for xp, yp, zp, color in components:
        draw_link_component_with_crossings(
            ax, xp, yp, zp, all_x, all_y, all_z, color, lw)


# ── Individual knot generators ───────────────────────────────────────

def generate_unknot(output: Path):
    """Unknot (0_1) — neutrino."""
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_unknot_on_ax(ax)
    setup_axes(ax)
    return save_svg(fig, output, "unknot-0_1")


def generate_trefoil(output: Path):
    """Trefoil knot (3_1) — electron. Torus knot T_{2,3}."""
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_torus_knot_on_ax(ax, 2, 3)
    setup_axes(ax)
    return save_svg(fig, output, "trefoil-3_1")


def generate_figure_eight(output: Path):
    """Figure-eight knot (4_1) — muon."""
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_figure_eight_on_ax(ax)
    setup_axes(ax)
    return save_svg(fig, output, "figure-eight-4_1")


def generate_cinquefoil(output: Path):
    """Cinquefoil knot (5_1) — tau. Torus knot T_{2,5}."""
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_torus_knot_on_ax(ax, 2, 5)
    setup_axes(ax)
    return save_svg(fig, output, "cinquefoil-5_1")


def generate_torus_2_7(output: Path):
    """T_{2,7} torus knot (7_1) — charm quark."""
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_torus_knot_on_ax(ax, 2, 7, num_points=3000)
    setup_axes(ax)
    return save_svg(fig, output, "torus-2_7-knot")


def generate_torus_3_4(output: Path):
    """T_{3,4} torus knot (8_{19}) — top quark."""
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_torus_knot_on_ax(ax, 3, 4, num_points=3000, angle_x=0.4)
    setup_axes(ax)
    return save_svg(fig, output, "torus-3_4-knot")


def generate_hopf_link(output: Path):
    """Hopf link (L2a1) — gluon. Two linked unknots."""
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_hopf_link_on_ax(ax)
    setup_axes(ax)
    return save_svg(fig, output, "hopf-link-L2a1")


def generate_borromean(output: Path):
    """Borromean rings — baryon binding."""
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE)
    draw_borromean_on_ax(ax)
    setup_axes(ax)
    return save_svg(fig, output, "borromean-rings")


def generate_mirror_pair(output: Path):
    """
    Trefoil chirality pair — electron/positron.
    Left trefoil (T_{2,3}) and right trefoil (T_{2,-3}) side by side.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.0, 3.0))

    x, y, z, _ = torus_knot_3d(2, 3, num_points=2000)
    xp, yp, zp = project_knot(x, y, z, angle_x=0.35, angle_y=0.0)
    draw_knot_with_crossings(ax1, xp, yp, zp, color=COLORS["knot_primary"])
    ax1.set_title(r"$T_{2,3}$ (electron $e^-$)", fontsize=10, pad=8)
    setup_axes(ax1)

    draw_knot_with_crossings(ax2, -xp, yp, zp, color=COLORS["knot_secondary"])
    ax2.set_title(r"$T_{2,3}^{\sigma}$ (positron $e^+$)", fontsize=10, pad=8)
    setup_axes(ax2)

    fig.tight_layout()
    return save_svg(fig, output, "trefoil-chirality-pair")


def generate_particle_gallery(output: Path):
    """
    Complete knot-particle dictionary as a single figure.
    Layout: 2 rows x 4 columns showing all fundamental particle knots.
    Uses the shared drawing helpers to avoid duplicating logic.
    """
    fig, axes = plt.subplots(2, 4, figsize=(12, 6))
    lw = LINEWIDTH - 0.5

    knots = [
        ("Photon $\\gamma$\n(empty)", "photon", (0, 0)),
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

        if params == "photon":
            ax.plot(0, 0, "o", color=COLORS["knot_primary"], markersize=8)
            ax.set_xlim(-1, 1)
            ax.set_ylim(-1, 1)
        elif params == "unknot":
            draw_unknot_on_ax(ax, lw=lw)
        elif params == "hopf":
            draw_hopf_link_on_ax(ax, lw=lw)
        elif params == "figure_eight":
            draw_figure_eight_on_ax(ax, lw=lw)
        elif isinstance(params, tuple):
            p, n = params
            draw_torus_knot_on_ax(ax, p, n, lw=lw, num_points=2500)

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
