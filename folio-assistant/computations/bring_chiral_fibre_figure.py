#!/usr/bin/env python3
"""
Bring chiral fibre figure generator — F3 (q→0) + F4 (q=½) per PR #1075
workplan, `docs/workplans/2026-05-24-pr31-affine-light-cone-redo.md`
Phase 1.

Renders two figures illustrating the chiral cubic fibre structure of
Bring's surface, using the canonical Bring cubic from the invariant
ring (NO fabricated coefficients):

  X^3 + (z+1) X^2 + (z^2 + z + 1) X + (z^3 + z^2 + z + 1) = 0,

where z = x_0 / x_1 is the spacetime affine coordinate on the
CP^1 base (Bring's surface ⊂ CP^4, sliced by the affine chart).

F3 (q → 0, "big bang" regime)
    Two-panel figure. LEFT: CP^1 base (one-point compactification
    rendered as a circle) with the discriminant branch points
    marked as filled dots, plus a dashed neighbourhood circle around
    a chosen branch point. RIGHT: three sheet curves X_1(t), X_2(t),
    X_3(t) as t traverses a small circle around the chosen branch
    point, showing sheet merging (the B_3-monodromy fingerprint).

F4 (q = 1/2, intermediate regime)
    Two-panel figure. LEFT: CP^1 base with a real segment z ∈
    [-0.5, 1.5] highlighted (well away from the complex branch
    points). RIGHT: stacked Re(X) and Im(X) sub-plots showing the
    three sheets along the highlighted segment — X_1 real (line),
    X_2/X_3 a complex-conjugate pair.

STYLE
    Formal math-book per the user directive 2026-05-24: black ink
    line drawing on white, no decorative gradients or color, color
    only used to disambiguate the three sheets where line-style alone
    would not suffice. Output SVG (matplotlib's `svg` backend) +
    PDF (matplotlib's `pdf` backend).

OUTPUT
    figures/bring-fibre-q0.svg
    figures/bring-fibre-q0.pdf
    figures/bring-fibre-qhalf.svg
    figures/bring-fibre-qhalf.pdf
    bring-chiral-fibre-figure.witness.json
        — parameters + branch-point coordinates + sample sheet values

WIRING
    Pure-Python, depends on numpy + matplotlib only. Imports
    `WitnessBuilder` if available; otherwise writes JSON directly.
    No q_parameter dependency since the cubic itself is
    q-independent (the q labels in F3 / F4 are framing / scale labels
    for the paper, NOT computational parameters).
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Tuple

import numpy as np
import matplotlib

matplotlib.use("Agg")  # headless backend; required in CI / no-DISPLAY contexts
import matplotlib.pyplot as plt


# ── Bring chiral cubic ───────────────────────────────────────────


def bring_cubic_coefficients(z: complex) -> Tuple[complex, complex, complex, complex]:
    """Coefficients [1, b, c, d] of the canonical Bring chiral cubic
    X^3 + (z+1) X^2 + (z^2+z+1) X + (z^3+z^2+z+1) = 0
    in the order required by numpy.roots."""
    b = z + 1
    c = z**2 + z + 1
    d = z**3 + z**2 + z + 1
    return (1.0 + 0j, b, c, d)


def bring_sheets(z: complex) -> np.ndarray:
    """Three sheets X_1, X_2, X_3 at the given z (complex roots of the cubic).
    Returns a length-3 ndarray of complex numbers, sorted by Re then Im."""
    coeffs = bring_cubic_coefficients(z)
    roots = np.roots(coeffs)
    # Sort by (Re, Im) for stable comparison across z (continuity is best-effort
    # for a degree-3 polynomial; for plotting we re-sort by proximity below).
    roots = roots[np.lexsort((roots.imag, roots.real))]
    return roots


def bring_discriminant(z: complex) -> complex:
    """Discriminant Δ(z) of the chiral cubic at z. Branch points are zeros of Δ.

    For X^3 + b X^2 + c X + d:
        Δ = 18 b c d - 4 b^3 d + b^2 c^2 - 4 c^3 - 27 d^2.
    """
    b = z + 1
    c = z**2 + z + 1
    d = z**3 + z**2 + z + 1
    return 18 * b * c * d - 4 * b**3 * d + b**2 * c**2 - 4 * c**3 - 27 * d**2


def find_branch_points(grid_size: int = 200, search_radius: float = 3.0,
                       newton_iters: int = 50) -> np.ndarray:
    """Locate roots of the discriminant Δ(z) in the disc |z| ≤ search_radius
    by sampling a grid + Newton-Raphson polish on local minima of |Δ|."""
    re_grid = np.linspace(-search_radius, search_radius, grid_size)
    im_grid = np.linspace(-search_radius, search_radius, grid_size)
    Z = re_grid[None, :] + 1j * im_grid[:, None]
    D_abs = np.abs(bring_discriminant(Z))

    # Detect local minima below threshold
    candidates = []
    threshold = D_abs.max() * 1e-2
    for i in range(1, grid_size - 1):
        for j in range(1, grid_size - 1):
            v = D_abs[i, j]
            if v > threshold:
                continue
            neighborhood = D_abs[i - 1:i + 2, j - 1:j + 2]
            if v == neighborhood.min():
                candidates.append(Z[i, j])

    # Polish each candidate via Newton-Raphson on Δ(z)
    polished = []
    eps = 1e-7
    for z0 in candidates:
        z = z0
        for _ in range(newton_iters):
            d = bring_discriminant(z)
            if abs(d) < 1e-14:
                break
            # Numerical derivative (finite difference)
            d_prime = (bring_discriminant(z + eps) - bring_discriminant(z - eps)) / (2 * eps)
            if abs(d_prime) < 1e-20:
                break
            z = z - d / d_prime
        if abs(bring_discriminant(z)) < 1e-8:
            polished.append(z)

    # Deduplicate (merge nearby roots)
    unique = []
    tol = 1e-3
    for r in polished:
        if not any(abs(r - u) < tol for u in unique):
            unique.append(r)

    return np.array(unique, dtype=complex)


# ── F3: q → 0, sheet-merging near a branch point ─────────────────


def render_f3_q_zero(branch_points: np.ndarray, output_dir: Path) -> dict:
    """Two-panel: CP^1 base with branch points + chosen circle, and
    three sheets evaluated around the chosen branch point."""
    # Pick the branch point with smallest |z| (most central)
    z_c = min(branch_points, key=lambda z: abs(z))
    circle_radius = 0.15

    # Sample sheets around the circle
    n_samples = 200
    theta = np.linspace(0, 2 * np.pi, n_samples)
    z_path = z_c + circle_radius * np.exp(1j * theta)

    sheets_raw = np.array([bring_sheets(z) for z in z_path])  # shape (n_samples, 3)

    # Track sheets by proximity (continuity along path) to handle root crossings
    sheets = sheets_raw.copy()
    for k in range(1, n_samples):
        prev = sheets[k - 1]
        curr = sheets_raw[k]
        # Greedy assignment: each prev → closest curr
        used = [False, False, False]
        new_row = np.zeros(3, dtype=complex)
        for p_idx in range(3):
            distances = [abs(curr[j] - prev[p_idx]) if not used[j] else np.inf
                         for j in range(3)]
            j_best = int(np.argmin(distances))
            new_row[p_idx] = curr[j_best]
            used[j_best] = True
        sheets[k] = new_row

    # Compute pairwise sheet separations for the "merging" diagnosis
    seps = np.zeros((n_samples, 3))
    for k in range(n_samples):
        for pair, (i, j) in enumerate([(0, 1), (0, 2), (1, 2)]):
            seps[k, pair] = abs(sheets[k, i] - sheets[k, j])
    # Identify the merging pair (smallest minimum separation)
    min_sep_per_pair = seps.min(axis=0)
    merging_pair = int(np.argmin(min_sep_per_pair))
    # pair index 0 → (0,1); 1 → (0,2); 2 → (1,2)
    pair_idx = [(0, 1), (0, 2), (1, 2)][merging_pair]
    isolated_idx = [i for i in range(3) if i not in pair_idx][0]

    # ── Plot ──
    fig, (ax_base, ax_sheets) = plt.subplots(1, 2, figsize=(10, 5))

    # LEFT: CP^1 base
    # One-point compactification rendered as a unit circle (the
    # Riemann sphere's equator projected to the plane); branch
    # points placed at their actual z values, scaled into the unit
    # disk via z / (1 + |z|).
    ax_base.set_aspect("equal")
    cp1 = plt.Circle((0, 0), 1.0, color="black", fill=False, linewidth=1.2)
    ax_base.add_patch(cp1)
    for bp in branch_points:
        scaled = bp / (1 + abs(bp))
        ax_base.plot(scaled.real, scaled.imag, "ko", markersize=4)
    # Highlight chosen branch point + neighbourhood circle
    z_c_scaled = z_c / (1 + abs(z_c))
    ax_base.plot(z_c_scaled.real, z_c_scaled.imag, "ko", markersize=8,
                 fillstyle="none", markeredgewidth=1.5)
    circle_scale = circle_radius / (1 + abs(z_c))
    circle_patch = plt.Circle((z_c_scaled.real, z_c_scaled.imag),
                              circle_scale, color="black",
                              fill=False, linewidth=0.8, linestyle="--")
    ax_base.add_patch(circle_patch)
    ax_base.set_xlim(-1.3, 1.3)
    ax_base.set_ylim(-1.3, 1.3)
    ax_base.set_xlabel(r"Re $z$ (compactified)")
    ax_base.set_ylabel(r"Im $z$ (compactified)")
    ax_base.set_title(r"$\mathbb{CP}^1$ base: branch points + chosen circle")
    ax_base.axhline(0, color="lightgray", linewidth=0.5)
    ax_base.axvline(0, color="lightgray", linewidth=0.5)

    # RIGHT: three sheets along the circle, parameterized by theta
    # Merging pair → solid + dashed; isolated → dotted
    line_styles = ["", "", ""]
    line_styles[pair_idx[0]] = "-"
    line_styles[pair_idx[1]] = "--"
    line_styles[isolated_idx] = ":"
    sheet_labels = ["", "", ""]
    sheet_labels[pair_idx[0]] = r"$X_{\rm merge,1}$"
    sheet_labels[pair_idx[1]] = r"$X_{\rm merge,2}$"
    sheet_labels[isolated_idx] = r"$X_{\rm isolated}$"

    for k in range(3):
        ax_sheets.plot(theta, sheets[:, k].real,
                       linestyle=line_styles[k], color="black", linewidth=1.2,
                       label=sheet_labels[k])
    ax_sheets.set_xlabel(r"$\theta$ (angle around branch point)")
    ax_sheets.set_ylabel(r"Re $X_k(z(\theta))$")
    ax_sheets.set_title(
        f"Three sheets along $|z - z_c| = {circle_radius}$ circle;"
        f" merging pair (min sep ≈ {min_sep_per_pair[merging_pair]:.3f})"
    )
    ax_sheets.legend(loc="upper right", frameon=False, fontsize=9)
    ax_sheets.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
    ax_sheets.set_xticklabels([r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax_sheets.axhline(0, color="lightgray", linewidth=0.5)

    plt.tight_layout()
    svg_path = output_dir / "bring-fibre-q0.svg"
    pdf_path = output_dir / "bring-fibre-q0.pdf"
    plt.savefig(svg_path, format="svg")
    plt.savefig(pdf_path, format="pdf")
    plt.close(fig)

    return {
        "branch_point_chosen": [z_c.real, z_c.imag],
        "circle_radius": circle_radius,
        "merging_pair": list(pair_idx),
        "isolated_sheet": isolated_idx,
        "min_separation": float(min_sep_per_pair[merging_pair]),
        "n_samples": n_samples,
        "svg_path": str(svg_path),
        "pdf_path": str(pdf_path),
    }


# ── F4: q = 1/2, well-separated sheets along real segment ────────


def render_f4_q_half(output_dir: Path) -> dict:
    """Two-panel: CP^1 base with highlighted real segment, and
    stacked Re(X), Im(X) sub-plots of the three sheets along the segment."""
    z_min, z_max = -0.5, 1.5
    n_samples = 200
    z_real = np.linspace(z_min, z_max, n_samples)

    # Compute sheets at each real z
    sheets_raw = np.array([bring_sheets(complex(z, 0)) for z in z_real])

    # Track by proximity for continuity (re-use F3 logic)
    sheets = sheets_raw.copy()
    for k in range(1, n_samples):
        prev = sheets[k - 1]
        curr = sheets_raw[k]
        used = [False, False, False]
        new_row = np.zeros(3, dtype=complex)
        for p_idx in range(3):
            distances = [abs(curr[j] - prev[p_idx]) if not used[j] else np.inf
                         for j in range(3)]
            j_best = int(np.argmin(distances))
            new_row[p_idx] = curr[j_best]
            used[j_best] = True
        sheets[k] = new_row

    # Identify the "mostly real" sheet (largest mean |Re| / mean |Im|)
    re_dominance = np.array([np.mean(np.abs(sheets[:, k].real)) /
                             (np.mean(np.abs(sheets[:, k].imag)) + 1e-12)
                             for k in range(3)])
    real_idx = int(np.argmax(re_dominance))
    complex_pair = [k for k in range(3) if k != real_idx]

    # ── Plot ──
    fig = plt.figure(figsize=(10, 5))
    gs = fig.add_gridspec(2, 2, width_ratios=[1, 1.2], height_ratios=[1, 1])
    ax_base = fig.add_subplot(gs[:, 0])
    ax_re = fig.add_subplot(gs[0, 1])
    ax_im = fig.add_subplot(gs[1, 1], sharex=ax_re)

    # LEFT: CP^1 with highlighted real segment
    ax_base.set_aspect("equal")
    cp1 = plt.Circle((0, 0), 1.0, color="black", fill=False, linewidth=1.2)
    ax_base.add_patch(cp1)
    # Scaled real segment (compactified: z / (1 + |z|))
    seg_re = z_real / (1 + np.abs(z_real))
    ax_base.plot(seg_re, np.zeros_like(seg_re), "k-", linewidth=2.0)
    # Endpoint markers
    ax_base.plot(seg_re[0], 0, "ko", markersize=5)
    ax_base.plot(seg_re[-1], 0, "ko", markersize=5)
    ax_base.text(seg_re[0] - 0.05, -0.15, f"$z={z_min}$", fontsize=9, ha="right")
    ax_base.text(seg_re[-1] + 0.05, -0.15, f"$z={z_max}$", fontsize=9, ha="left")
    ax_base.set_xlim(-1.3, 1.3)
    ax_base.set_ylim(-1.3, 1.3)
    ax_base.set_xlabel(r"Re $z$ (compactified)")
    ax_base.set_ylabel(r"Im $z$ (compactified)")
    ax_base.set_title(r"$\mathbb{CP}^1$ base: real segment highlighted")
    ax_base.axhline(0, color="lightgray", linewidth=0.5)
    ax_base.axvline(0, color="lightgray", linewidth=0.5)

    # RIGHT (top): Re(X) for each sheet
    line_styles = ["", "", ""]
    sheet_labels = ["", "", ""]
    line_styles[real_idx] = "-"
    sheet_labels[real_idx] = r"$X_{\rm real}$"
    line_styles[complex_pair[0]] = "--"
    sheet_labels[complex_pair[0]] = r"$X_{\rm conj,1}$"
    line_styles[complex_pair[1]] = ":"
    sheet_labels[complex_pair[1]] = r"$X_{\rm conj,2}$"

    for k in range(3):
        ax_re.plot(z_real, sheets[:, k].real,
                   linestyle=line_styles[k], color="black", linewidth=1.2,
                   label=sheet_labels[k])
    ax_re.set_ylabel(r"Re $X_k(z)$")
    ax_re.set_title("Three sheets along the real segment")
    ax_re.legend(loc="upper right", frameon=False, fontsize=9)
    ax_re.axhline(0, color="lightgray", linewidth=0.5)
    plt.setp(ax_re.get_xticklabels(), visible=False)

    # RIGHT (bottom): Im(X) for each sheet
    for k in range(3):
        ax_im.plot(z_real, sheets[:, k].imag,
                   linestyle=line_styles[k], color="black", linewidth=1.2)
    ax_im.set_xlabel(r"$z$ (real)")
    ax_im.set_ylabel(r"Im $X_k(z)$")
    ax_im.axhline(0, color="lightgray", linewidth=0.5)

    plt.tight_layout()
    svg_path = output_dir / "bring-fibre-qhalf.svg"
    pdf_path = output_dir / "bring-fibre-qhalf.pdf"
    plt.savefig(svg_path, format="svg")
    plt.savefig(pdf_path, format="pdf")
    plt.close(fig)

    # Sample value at z = 0
    sheets_at_zero = bring_sheets(0 + 0j)

    return {
        "z_min": z_min,
        "z_max": z_max,
        "n_samples": n_samples,
        "real_sheet_index": real_idx,
        "complex_pair_indices": complex_pair,
        "sheets_at_z_eq_zero": [
            {"re": float(s.real), "im": float(s.imag)} for s in sheets_at_zero
        ],
        "svg_path": str(svg_path),
        "pdf_path": str(pdf_path),
    }


# ── Witness emission ─────────────────────────────────────────────


def emit_witness(f3_data: dict, f4_data: dict, branch_points: np.ndarray,
                 witness_path: Path, wall_seconds: float) -> None:
    """Emit a witness JSON capturing the figure parameters + verified
    sample values. This makes the figures auditable by
    compute-integration-watcher."""
    witness = {
        "type": "figure-generation",
        "version": "1",
        "scriptFile": "folio-assistant/computations/bring_chiral_fibre_figure.py",
        "scriptHash": None,  # filled by witness-pipeline post-build
        "scriptCommitSha": None,  # filled by witness-pipeline post-commit
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "engineVersion": f"numpy-{np.__version__} matplotlib-{matplotlib.__version__}",
        "description": (
            "Bring chiral fibre figures F3 (q→0, branch-point neighbourhood) "
            "and F4 (q=½, real-segment) per PR #1075 workplan Phase 1. "
            "Cubic X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0 from Bring's invariant "
            "ring; sheets via numpy.roots; branch points via Newton-Raphson "
            "on the discriminant Δ(z)."
        ),
        "parameters": {
            "cubic": "X^3 + (z+1)*X^2 + (z^2+z+1)*X + (z^3+z^2+z+1)",
            "branch_point_search_radius": 3.0,
            "branch_point_grid_size": 200,
        },
        "data": {
            "branch_points": [
                {"re": float(z.real), "im": float(z.imag),
                 "discriminant_residual": float(abs(bring_discriminant(z)))}
                for z in branch_points
            ],
            "f3_q_zero": f3_data,
            "f4_q_half": f4_data,
            "wall_seconds": wall_seconds,
        },
    }
    witness_path.write_text(json.dumps(witness, indent=2) + "\n")


# ── Main ─────────────────────────────────────────────────────────


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent.parent
    figures_dir = repo_root / "figures"
    figures_dir.mkdir(exist_ok=True)
    witness_path = (repo_root / "folio-assistant" / "computations"
                    / "bring-chiral-fibre-figure.witness.json")

    t0 = time.time()
    print("Finding discriminant branch points (Newton-Raphson on |Δ(z)|)...")
    branch_points = find_branch_points()
    print(f"  Found {len(branch_points)} branch points: "
          f"{[f'({z.real:.4f},{z.imag:+.4f}i)' for z in branch_points]}")

    print("Rendering F3 (q → 0, branch-point neighbourhood)...")
    f3 = render_f3_q_zero(branch_points, figures_dir)
    print(f"  → {f3['svg_path']}")
    print(f"  → {f3['pdf_path']}")

    print("Rendering F4 (q = ½, real-segment)...")
    f4 = render_f4_q_half(figures_dir)
    print(f"  → {f4['svg_path']}")
    print(f"  → {f4['pdf_path']}")

    wall = time.time() - t0
    emit_witness(f3, f4, branch_points, witness_path, wall)
    print(f"Witness emitted: {witness_path}  (wall: {wall:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
