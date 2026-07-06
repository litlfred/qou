#!/usr/bin/env python3
"""
Affine light-cone figure generator — F1 of PR #1075 workplan Phase 2.

Renders the affine light-cone wedge over the Bring chiral cubic
brane in formal math-book style per the author directive 2026-05-24.

GEOMETRY

The "brane" is the locus of the canonical Bring chiral cubic

    X^3 + (z+1) X^2 + (z^2+z+1) X + (z^3+z^2+z+1) = 0

restricted to the real segment of the spacetime affine chart
z = x_0/x_1 ∈ CP^1, picking the real sheet X(z) (the cubic has
one real root + a complex-conjugate pair in the chosen interval).

The figure plots (z, X(z)) as the brane curve in 2D. The
"affine light cone" is an open wedge with vertex at one end of
the real segment ("vertex" = big-bang regime, z = z_vertex) and
opening toward the other end ("horizon" = heat-death regime,
z = z_horizon). The observer at the substrate q_0 sits on the
brane at z = q_0.

The Euler-characteristic annotation χ(A) = −6 (equivalently
χ(Σ_4) = −6 for Bring's surface) is placed in a corner box per
the recipe.

STYLE

Formal math-book per author directive 2026-05-24:
  - Black ink on white
  - Bring curve = single thick line (X_real sheet, in 2D)
  - Light cone = two thin straight lines bounding the wedge
  - Observer = small filled black dot, label "observer"
  - Annotations as plain marginal text + corner box
  - NO gradient, NO decorative color
  - q_0 marked as a vertical dotted line at substrate

OUTPUT

  figures/affine-light-cone.svg
  figures/affine-light-cone.pdf

WITNESS

  computations/affine-light-cone-figure.witness.json
  emitted via WitnessBuilder (standard ComputationWitness shape per
  PR #1108 review).
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path
from typing import Tuple

# sys.path bootstrap for witness_base + q_parameter
_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

from witness_base import WitnessBuilder  # noqa: E402

# Try to import the substrate q_0 from the canonical module. If not
# available (qou_substrate not on sys.path), fall back to a documented
# approximation (still correct to 4 sig figs).
try:
    from q_parameter import Q as _Q_SUBSTRATE
    Q0_FLOAT: float = float(_Q_SUBSTRATE)
    Q0_SOURCE: str = "q_parameter.Q (canonical)"
except Exception:
    Q0_FLOAT = 1.10998  # CODATA m_μ/m_e + Vol(4_1) derivation; ~5 sig figs
    Q0_SOURCE = "approx 1.10998 (q_parameter unavailable)"


# ── Module constants ─────────────────────────────────────────────

# Real-z interval over which to draw the brane. Chosen to avoid the
# 6 complex branch points of the chiral cubic (the closest pair to
# the real axis is z ≈ -0.975 ± 0.223i; staying within ±2 keeps real
# z well away from the branch locus). Z_HORIZON > Z_VERTEX by
# convention (light cone opens leftward → rightward).
Z_VERTEX: float = -1.5
Z_HORIZON: float = 2.5
N_SAMPLES: int = 500

# Light-cone slope (in (z, X)-space). Two straight lines from the
# vertex (z_v, X(z_v)) to two points on the horizon ±OPENING vertical
# offset. The opening half-angle is set so the wedge is visually
# distinct from the brane curve.
LIGHT_CONE_OPENING: float = 1.5


import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ── Bring chiral cubic — same as bring_chiral_fibre_figure.py ────


def bring_real_sheet(z: float) -> float:
    """Real root of X^3 + (z+1) X^2 + (z^2+z+1) X + (z^3+z^2+z+1) = 0
    at the given real z. For the z-interval used here, exactly one real
    root exists (the cubic has discriminant < 0 → one real + complex
    pair). Returns the real root (or its real part if a fluctuation in
    numpy.roots produces a tiny imaginary component)."""
    coeffs = [1.0, z + 1, z**2 + z + 1, z**3 + z**2 + z + 1]
    roots = np.roots(coeffs)
    # Pick the root with smallest |Im| (the real root)
    best = min(roots, key=lambda r: abs(r.imag))
    return float(best.real)


def render_affine_light_cone(output_dir: Path) -> dict:
    """Two-panel-free, single-figure rendering of the affine light cone.

    Returns a dict with the figure parameters + observer location +
    output paths, suitable for embedding in the WitnessBuilder data.
    """
    # Brane curve: (z, X(z)) along the real z-interval
    z_grid = np.linspace(Z_VERTEX, Z_HORIZON, N_SAMPLES)
    X_grid = np.array([bring_real_sheet(z) for z in z_grid])

    # Observer at q_0
    q0 = float(Q0_FLOAT)
    X_observer = bring_real_sheet(q0)

    # Endpoints
    X_vertex = bring_real_sheet(Z_VERTEX)
    X_horizon = bring_real_sheet(Z_HORIZON)

    # Light cone: two straight lines from (Z_VERTEX, X_vertex) opening
    # toward (Z_HORIZON, X_horizon ± LIGHT_CONE_OPENING).
    cone_top_end = (Z_HORIZON, X_horizon + LIGHT_CONE_OPENING)
    cone_bot_end = (Z_HORIZON, X_horizon - LIGHT_CONE_OPENING)

    # ── Plot ──
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_aspect("auto")

    # Brane curve (thick solid black)
    ax.plot(z_grid, X_grid, "k-", linewidth=2.0, label="brane (Bring's surface)")

    # Light cone (two thin straight lines)
    ax.plot([Z_VERTEX, cone_top_end[0]], [X_vertex, cone_top_end[1]],
            "k-", linewidth=0.7, label="affine light cone")
    ax.plot([Z_VERTEX, cone_bot_end[0]], [X_vertex, cone_bot_end[1]],
            "k-", linewidth=0.7)

    # Vertex marker (small filled square at the cone apex)
    ax.plot(Z_VERTEX, X_vertex, "ks", markersize=6,
            markerfacecolor="black", markeredgewidth=0)
    ax.text(Z_VERTEX - 0.05, X_vertex + 0.35,
            f"vertex (big bang)\n$z = {Z_VERTEX}$", fontsize=9,
            ha="right", va="bottom")

    # Horizon marker (small filled square at the right end)
    ax.plot(Z_HORIZON, X_horizon, "ks", markersize=6,
            markerfacecolor="black", markeredgewidth=0)
    ax.text(Z_HORIZON + 0.05, X_horizon - 0.3,
            f"horizon (heat death)\n$z = {Z_HORIZON}$", fontsize=9,
            ha="left", va="top")

    # Observer marker (small filled black circle)
    ax.plot(q0, X_observer, "ko", markersize=7)
    ax.annotate("observer",
                xy=(q0, X_observer),
                xytext=(q0 + 0.3, X_observer + 0.4),
                fontsize=10,
                arrowprops=dict(arrowstyle="-", color="black", lw=0.5))

    # Substrate marker: vertical dotted line at q_0
    ax.axvline(q0, color="gray", linewidth=0.5, linestyle=":")
    ax.text(q0 + 0.02, ax.get_ylim()[1] * 0.95 if False else X_observer - 2.5,
            f"$q_0 \\approx {q0:.4f}$", fontsize=9, color="gray",
            ha="left", va="top")

    # Euler characteristic annotation (corner box)
    ax.text(0.97, 0.04,
            r"$\chi(A) = -6$" + "\n" + r"(Bring's surface $\Sigma_4$)",
            transform=ax.transAxes,
            fontsize=10, ha="right", va="bottom",
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black",
                      facecolor="white", linewidth=0.8))

    ax.set_xlabel(r"$z = x_0 / x_1 \in \mathbb{CP}^1$ (spacetime affine chart)")
    ax.set_ylabel(r"$X(z)$ (real sheet of Bring's chiral cubic)")
    ax.set_title("Affine light cone on Bring's brane (formal math-book style)")
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    ax.axhline(0, color="lightgray", linewidth=0.4)

    plt.tight_layout()
    svg_path = output_dir / "affine-light-cone.svg"
    pdf_path = output_dir / "affine-light-cone.pdf"
    plt.savefig(svg_path, format="svg")
    plt.savefig(pdf_path, format="pdf")
    plt.close(fig)

    return {
        "z_vertex": Z_VERTEX,
        "z_horizon": Z_HORIZON,
        "n_samples": N_SAMPLES,
        "light_cone_opening": LIGHT_CONE_OPENING,
        "q0": q0,
        "q0_source": Q0_SOURCE,
        "X_at_z_vertex": float(X_vertex),
        "X_at_z_horizon": float(X_horizon),
        "X_at_q0_observer": float(X_observer),
        "chi_label": "chi(A) = -6 (= chi(Sigma_4) for Bring's surface)",
        "svg_path": str(svg_path),
        "pdf_path": str(pdf_path),
    }


def _to_repo_relative(p: str, repo_root: Path) -> str:
    """Repo-relative path conversion."""
    try:
        return str(Path(p).resolve().relative_to(repo_root.resolve()))
    except ValueError:
        return p


def emit_witness(f1_data: dict, output_dir: Path, repo_root: Path,
                 start_monotonic: float) -> Path:
    """Emit standard ComputationWitness via WitnessBuilder."""
    f1_rel = {**f1_data,
              "svg_path": _to_repo_relative(f1_data["svg_path"], repo_root),
              "pdf_path": _to_repo_relative(f1_data["pdf_path"], repo_root)}
    wb = (
        WitnessBuilder(
            "affine-light-cone-figure",
            engine="python",
            engine_version=(
                f"numpy-{np.__version__} matplotlib-{matplotlib.__version__}"
            ),
            output_dir=output_dir,
            start_time=start_monotonic,
            _script_path=Path(__file__).resolve(),
        )
        .set_description(
            "Affine light-cone figure F1 per PR #1075 workplan Phase 2. "
            "Brane = Bring chiral cubic real-sheet locus over a real "
            "z-interval; affine light cone = two-line wedge from "
            "big-bang vertex to heat-death horizon; observer marker "
            "at the substrate q_0. Formal math-book style: black ink, "
            "no gradients, line styles only."
        )
        .add_parameter("cubic", "X^3 + (z+1)*X^2 + (z^2+z+1)*X + (z^3+z^2+z+1)")
        .add_parameter("z_vertex", Z_VERTEX)
        .add_parameter("z_horizon", Z_HORIZON)
        .add_parameter("n_samples", N_SAMPLES)
        .add_parameter("light_cone_opening", LIGHT_CONE_OPENING)
        .add_parameter("q0", Q0_FLOAT)
        .add_parameter("q0_source", Q0_SOURCE)
        .add_data("f1_affine_light_cone", f1_rel)
    )
    return wb.save()


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent.parent
    figures_dir = repo_root / "figures"
    figures_dir.mkdir(exist_ok=True)
    output_dir = repo_root / "folio-assistant" / "computations"

    start_monotonic = time.monotonic()
    t0_wall = time.time()
    print(f"Rendering F1 (affine light cone over Bring brane; q_0 = {Q0_FLOAT})...")
    f1 = render_affine_light_cone(figures_dir)
    print(f"  → {f1['svg_path']}")
    print(f"  → {f1['pdf_path']}")
    print(f"  brane endpoints: ({Z_VERTEX:.3f}, {f1['X_at_z_vertex']:.4f})"
          f" → ({Z_HORIZON:.3f}, {f1['X_at_z_horizon']:.4f})")
    print(f"  observer at q_0: ({Q0_FLOAT:.4f}, {f1['X_at_q0_observer']:.4f})")

    wall = time.time() - t0_wall
    witness_path = emit_witness(f1, output_dir, repo_root, start_monotonic)
    print(f"Witness emitted: {witness_path}  (wall: {wall:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
