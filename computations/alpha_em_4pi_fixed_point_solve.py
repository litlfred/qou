#!/usr/bin/env python3
"""alpha_em_4pi_fixed_point_solve.py — self-consistent fixed-point
derivation of α_EM from the empirical form:

  α_EM⁻¹ = T(q) + α_EM · H(q) · (1 - h²·α_EM + O(α²))

where T = q·[9]_q·[10]_q + 2/(3π) (proven; PR #1444 merged)
and H = [2]_q/(8π) (empirical structural candidate from #1477).

If H · (1 - h²·α) is the correct categorical form for α/(4π), then α_EM
is the UNIQUE FIXED-POINT solving the cubic:

  α²·H - α³·h²·H = 1 - T·α
  -h²·H·α³ + H·α² + T·α - 1 = 0

This probe solves this cubic at q_0 (numerically, 50 dps) and compares
the predicted α_EM⁻¹ to CODATA. If the residual is < experimental σ_α
= 0.15 ppb, that's a STRUCTURAL DERIVATION OF α — the framework
generates both the tree term AND the next-order coefficient AND α
itself from q_0 + Bring data alone.

Three forms tested:
  (A) α_EM⁻¹ = T + α·H                       (no q-correction; quadratic in α)
  (B) α_EM⁻¹ = T + α·H·(1 - h²·α)           (Schwinger correction; cubic)
  (C) α_EM⁻¹ = T + α·H·(1 - h²·α + h⁴·α²)   (next term in expansion; quartic)

Compares predicted α_EM⁻¹ to CODATA 137.035999084 at each level.
Honest verdict: which form (if any) closes to ≤0.15 ppb experimental σ.

This is the framework's HARDEST honesty test — if it solves α from q_0
+ Bring with no extra free parameters, the categorical derivation of
α is complete.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp
from mpmath import mpf, pi, polyroots

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import ALPHA_EM_INV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def q_bracket(n: int, q):
    return (q**n - q**(-n)) / (q - q**(-1))


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "alpha-em-4pi-fixed-point-solve",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Self-consistent fixed-point derivation of α_EM at q_0 using "
        "the empirical form α⁻¹ = T + α·H·(1-h²·α+O(α²)) from #1477 "
        "and #1480. Solves the resulting polynomial in α numerically "
        "at 50 dps; compares to CODATA. If residual < experimental "
        "σ_α (0.15 ppb), this constitutes a structural derivation of "
        "α from q_0 + Bring data with no free parameters."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    q = mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    h2 = h * h
    bra2 = q_bracket(2, q)
    bra9 = q_bracket(9, q)
    bra10 = q_bracket(10, q)
    g = 4

    T = q * bra9 * bra10 + mpf(2 * g) / (4 * pi * (g - 1))  # tree + zero_mode
    H = bra2 / (8 * pi)

    CODATA_alpha_inv = mpf(str(ALPHA_EM_INV))
    SIGMA_PPB = mpf("0.15")  # CODATA experimental σ_α (0.15 ppb)

    print("=" * 76)
    print(" SELF-CONSISTENT FIXED-POINT SOLVE for α_EM at q_0")
    print("=" * 76)
    print(f"  q₀ = {float(q):.14f}")
    print(f"  T = tree + zero_mode = {mp.nstr(T, 18)}")
    print(f"  H = [2]_q/(8π)       = {mp.nstr(H, 18)}")
    print(f"  h² = (q-q⁻¹)²        = {mp.nstr(h2, 18)}")
    print(f"  CODATA α_EM⁻¹        = {mp.nstr(CODATA_alpha_inv, 18)}")
    print(f"  experimental σ_α     = {float(SIGMA_PPB)} ppb")
    print()

    def report(label, alpha_solved, formula):
        """Compare solved α to CODATA, print residual in ppb."""
        alpha_inv = 1 / alpha_solved
        residual_ppb = float((alpha_inv - CODATA_alpha_inv) / CODATA_alpha_inv * 1e9)
        verdict = (
            "DERIVED" if abs(residual_ppb) < float(SIGMA_PPB)
            else "NEAR-DERIVED" if abs(residual_ppb) < 10*float(SIGMA_PPB)
            else f"OFF (~{abs(residual_ppb):.0f} ppb)"
        )
        print(f"  {label}")
        print(f"     formula:  {formula}")
        print(f"     α_solved   = {mp.nstr(alpha_solved, 18)}")
        print(f"     α⁻¹_solved = {mp.nstr(alpha_inv, 18)}")
        print(f"     residual   = {residual_ppb:+.6f} ppb vs CODATA")
        print(f"     vs σ_α     = {abs(residual_ppb)/float(SIGMA_PPB):.2f}× experimental σ")
        print(f"     verdict    = {verdict}")
        print()
        return {
            "label": label, "formula": formula,
            "alpha_solved": mp.nstr(alpha_solved, 30),
            "alpha_inv_solved": mp.nstr(alpha_inv, 30),
            "residual_ppb": residual_ppb,
            "ratio_to_sigma": float(abs(residual_ppb)/float(SIGMA_PPB)),
            "verdict": verdict,
        }

    results = {}

    # ── Form A: quadratic (no q-correction) ──────────────────
    # α²·H + α·T - 1 = 0  →  α = (-T + √(T²+4H)) / (2H)
    discA = T**2 + 4*H
    sqrtA = mp.sqrt(discA)
    alpha_A = (-T + sqrtA) / (2*H)
    results["A_quadratic"] = report(
        "Form A — quadratic (no q-correction)",
        alpha_A, "α²·H + α·T - 1 = 0  ⇒  α = (-T + √(T²+4H)) / (2H)"
    )

    # ── Form B: cubic with -h²·α correction ──────────────────
    # α_EM⁻¹ = T + α·H·(1-h²·α)
    # 1/α = T + α·H - h²·H·α²
    # 1 = T·α + α²·H - h²·H·α³
    # h²·H·α³ - H·α² - T·α + 1 = 0
    # mpmath polyroots wants coefficients of highest power first:
    coefsB = [h2*H, -H, -T, mpf(1)]
    rootsB = mp.polyroots(coefsB)
    # Pick the positive real root closest to 1/137 ≈ 0.0073
    real_rootsB = [r for r in rootsB
                   if abs(mp.im(r)) < mpf("1e-30")]
    real_rootsB = [mp.re(r) for r in real_rootsB]
    pos_rootsB = [r for r in real_rootsB if r > 0]
    alpha_B = min(pos_rootsB, key=lambda r: abs(r - mpf("0.00730")))
    results["B_cubic_schwinger"] = report(
        "Form B — cubic with -h²·α correction (Schwinger)",
        alpha_B,
        "α³·h²·H - α²·H - T·α + 1 = 0  ⇒  α from polyroots"
    )

    # ── Form C: quartic with -h²·α + h⁴·α² correction ────────
    # α_EM⁻¹ = T + α·H·(1 - h²·α + h⁴·α²)
    # 1/α = T + α·H - h²·H·α² + h⁴·H·α³
    # 1 = T·α + α²·H - h²·H·α³ + h⁴·H·α⁴
    # -h⁴·H·α⁴ + h²·H·α³ - H·α² - T·α + 1 = 0
    # Multiply by -1: h⁴·H·α⁴ - h²·H·α³ + H·α² + T·α - 1 = 0
    coefsC = [h2**2 * H, -h2*H, H, T, mpf(-1)]
    rootsC = mp.polyroots(coefsC)
    real_rootsC = [mp.re(r) for r in rootsC if abs(mp.im(r)) < mpf("1e-30")]
    pos_rootsC = [r for r in real_rootsC if r > 0]
    if pos_rootsC:
        alpha_C = min(pos_rootsC, key=lambda r: abs(r - mpf("0.00730")))
        results["C_quartic_schwinger_extended"] = report(
            "Form C — quartic with -h²·α + h⁴·α² correction",
            alpha_C,
            "h⁴·H·α⁴ - h²·H·α³ + H·α² + T·α - 1 = 0  ⇒  α from polyroots"
        )
    else:
        print("  Form C: no positive real root found.")

    # ── Honest verdict ──────────────────────────────────────
    print("=" * 76)
    print(" Honest verdict")
    print("=" * 76)
    best = min(results.values(), key=lambda r: abs(r["residual_ppb"]))
    print(f"  Best form: {best['label']}")
    print(f"     residual = {best['residual_ppb']:+.4f} ppb")
    print(f"     vs σ_α   = {best['ratio_to_sigma']:.2f}× experimental σ")
    print(f"     verdict  = {best['verdict']}")
    print()
    if best["verdict"] == "DERIVED":
        print(f"  ✓✓ STRUCTURAL DERIVATION OF α_EM:")
        print(f"     The fixed-point solution of {best['formula']}")
        print(f"     gives α_EM matching CODATA to within experimental σ_α.")
        print(f"     This closes the categorical derivation: q_0 + Bring data")
        print(f"     → α_EM no free parameters.")
    elif best["verdict"] == "NEAR-DERIVED":
        print(f"  ~  NEAR-DERIVED: within 10× experimental σ but not within σ.")
        print(f"     The fixed-point form captures α to {best['ratio_to_sigma']:.1f}× σ.")
        print(f"     Closing requires either:")
        print(f"       • higher-order term (α³·H·k(q) for some k)")
        print(f"       • refinement of H (the [2]_q/(8π) leading coefficient)")
        print(f"       • CAL-2 (q_0 = m_μ/m_e) precision tightening")
    else:
        print(f"  ✗ OFF by {abs(best['residual_ppb']):.0f} ppb (>> σ_α=0.15 ppb).")
        print(f"     The H·(1-h²α) form alone does not derive α_EM.")
        print(f"     The remaining residual indicates missing structural content.")

    builder.add_data("q_0", mp.nstr(q, 30))
    builder.add_data("T_tree_plus_zero_mode", mp.nstr(T, 30))
    builder.add_data("H_value", mp.nstr(H, 30))
    builder.add_data("h_squared", mp.nstr(h2, 30))
    builder.add_data("CODATA_alpha_inv", mp.nstr(CODATA_alpha_inv, 30))
    builder.add_data("experimental_sigma_ppb", float(SIGMA_PPB))
    builder.add_data("forms_solved", results)
    builder.add_data("best", best)

    builder.add_assertion(
        "fixed_point_forms_solved",
        computed=len(results),
        expected=3,
        tolerance=0,
        source="Three self-consistent fixed-point forms (A quadratic, "
               "B cubic, C quartic) solved at q_0 (50 dps) and "
               "compared to CODATA α_EM⁻¹.",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
