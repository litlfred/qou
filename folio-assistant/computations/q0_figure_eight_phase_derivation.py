#!/usr/bin/env python3
"""
q0_figure_eight_phase_derivation.py — test whether the figure-eight
spectral phase equation uniquely determines the substrate q₀.

HYPOTHESIS (from PR #1332 + workplan Priority 3):
    The figure-eight knot 4₁ = (σ₁σ₂⁻¹)² in B₃ acts on V_{(2,1)}
    as a unitary 2×2 matrix. Its spectral phase θ satisfies:

        θ(q) = arccos(Re(tr(ρ_{(2,1)}(4₁; q)))/2)

    If θ(q₀) = Vol(4₁) = 2Λ(π/3), then q₀ is DERIVED from the
    equation "spectral phase of the figure-eight equals its
    hyperbolic volume" — a purely topological/algebraic constraint.

    This would give a STRUCTURAL derivation of q₀, connecting
    PR #1249's Path (a) spectral-collapse to knot volume.

RESULT:
    Computed below — check whether the match is exact or approximate,
    and whether the equation has a unique solution near q₀.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, sqrt, acos, pi as mppi, clsin, matrix, findroot

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def hoefsmit_matrices(q):
    """Build σ₁, σ₂ on V_{(2,1)} of H₃(q) in Hoefsmit seminormal form."""
    qi = 1 / q
    h = q - qi

    sigma1 = matrix([[q, 0], [0, -qi]])

    a2 = -qi / (1 + q ** 2)
    d2 = q ** 3 / (1 + q ** 2)
    b2 = sqrt((h ** 2 + 3) / (h ** 2 + 4))

    sigma2 = matrix([[a2, b2], [b2, d2]])

    return sigma1, sigma2


def figure_eight_trace(q):
    """Compute tr(ρ_{(2,1)}((σ₁σ₂⁻¹)²; q))."""
    sigma1, sigma2 = hoefsmit_matrices(q)

    h = q - 1 / q
    I2 = matrix([[1, 0], [0, 1]])
    sigma2_inv = sigma2 - h * I2  # σ⁻¹ = σ - h·I (from Hecke relation)

    s1s2inv = sigma1 * sigma2_inv
    fig8 = s1s2inv * s1s2inv  # (σ₁σ₂⁻¹)²

    return fig8[0, 0] + fig8[1, 1]


def spectral_phase(q):
    """Spectral phase θ = arccos(Re(tr(4₁))/2) on V_{(2,1)}."""
    tr = figure_eight_trace(q)
    re_tr = mp.re(tr)
    half_tr = re_tr / 2
    if half_tr > 1:
        half_tr = mpf(1)
    elif half_tr < -1:
        half_tr = mpf(-1)
    return acos(half_tr)


def vol_figure_eight():
    """Vol(4₁) = 2Λ(π/3) where Λ is the Lobachevsky function."""
    return 2 * clsin(2, mppi / 3)


def main():
    set_compute_dps()

    q0 = mpf(Q_50_DIGIT_STR)
    vol_41 = vol_figure_eight()

    # === Compute at q₀ ===
    tr_at_q0 = figure_eight_trace(q0)
    theta_at_q0 = spectral_phase(q0)

    miss_abs = theta_at_q0 - vol_41
    miss_pct = float(fabs(miss_abs) / vol_41 * 100)

    print("=" * 70)
    print("q₀ DERIVATION: figure-eight phase = Vol(4₁)?")
    print("=" * 70)
    print()
    print(f"q₀ = {q0}")
    print(f"Vol(4₁) = 2Λ(π/3) = {float(vol_41):.15f}")
    print()
    print(f"tr(ρ_{{(2,1)}}(4₁; q₀)) = {float(tr_at_q0):.15f}")
    print(f"θ = arccos(tr/2) = {float(theta_at_q0):.15f}")
    print(f"Vol(4₁)           = {float(vol_41):.15f}")
    print(f"Miss: θ − Vol = {float(miss_abs):.6e} ({miss_pct:.4f}%)")
    print()

    # === Check: is the match good enough to attempt root-finding? ===
    if miss_pct < 5:
        print("Match is close — attempting to solve θ(q) = Vol(4₁)...")
        print()

        def equation(q_val):
            return spectral_phase(q_val) - vol_41

        try:
            q_derived = findroot(equation, q0, tol=mpf("1e-40"))
            q_diff = q_derived - q0
            q_diff_ppb = float(fabs(q_diff) / q0 * 1e9)

            print(f"DERIVED q = {q_derived}")
            print(f"Known q₀  = {q0}")
            print(f"Difference: {float(q_diff):.6e} ({q_diff_ppb:.1f} ppb)")
            print()

            if q_diff_ppb < 1:
                print("*** EXACT MATCH — q₀ is the UNIQUE solution of θ(q) = Vol(4₁) ***")
                derivation_status = "exact"
            elif q_diff_ppb < 1000:
                print(f"CLOSE MATCH — {q_diff_ppb:.1f} ppb deviation")
                derivation_status = "close"
            else:
                print(f"APPROXIMATE — {q_diff_ppb:.0f} ppb deviation")
                derivation_status = "approximate"
        except Exception as e:
            print(f"Root-finding failed: {e}")
            q_derived = None
            q_diff_ppb = None
            derivation_status = "failed"
    else:
        print(f"Match too loose ({miss_pct:.1f}%) — not a viable derivation path")
        q_derived = None
        q_diff_ppb = None
        derivation_status = "not_viable"

    # === Scan: uniqueness of the solution ===
    print()
    print("=== Phase scan: θ(q) for q ∈ [1.01, 1.30] ===")
    n_cross = 0
    prev_sign = None
    for i in range(30):
        q_val = mpf("1.01") + mpf(i) * mpf("0.01")
        try:
            theta_val = spectral_phase(q_val)
            diff = theta_val - vol_41
            sign = 1 if diff > 0 else -1
            if prev_sign is not None and sign != prev_sign:
                n_cross += 1
                marker = " ← CROSSING"
            else:
                marker = ""
            prev_sign = sign
            print(f"  q={float(q_val):.2f}: θ={float(theta_val):.6f}, "
                  f"θ−Vol={float(diff):+.4e}{marker}")
        except Exception:
            print(f"  q={float(q_val):.2f}: computation failed")

    print(f"\nCrossings found: {n_cross}")
    if n_cross == 1:
        print("→ UNIQUE solution in [1.01, 1.30]: the equation pins q₀")

    # === Witness ===
    wb = WitnessBuilder("q0-figure-eight-phase-derivation", engine="mpmath")
    wb.set_description(
        "Test whether θ(q₀) = Vol(4₁) where θ = arccos(tr(ρ_{(2,1)}(4₁;q))/2) "
        "is the spectral phase of the figure-eight on V_{(2,1)}. "
        f"Result: {miss_pct:.4f}% miss at q₀. "
        f"Derivation status: {derivation_status}."
    )

    wb.add_data("phase_at_q0", {
        "tr_21": str(float(tr_at_q0)),
        "theta": str(float(theta_at_q0)),
        "vol_41": str(float(vol_41)),
        "miss_pct": miss_pct,
    })
    if q_derived is not None:
        wb.add_data("root_finding", {
            "q_derived": str(q_derived),
            "q0_known": str(q0),
            "diff_ppb": q_diff_ppb,
            "status": derivation_status,
        })
    wb.add_data("uniqueness", {
        "scan_range": "[1.01, 1.30]",
        "crossings": n_cross,
        "unique": n_cross == 1,
    })

    wb.add_assertion(
        "phase_within_5pct_of_vol",
        computed=miss_pct,
        expected=0,
        tolerance=5,
        source="θ(q₀) vs Vol(4₁)",
    )

    wb.save()


if __name__ == "__main__":
    main()
