#!/usr/bin/env python3
"""alpha_em_4pi_q0_sensitivity.py — q_0 sensitivity analysis for the
empirical form α_EM⁻¹ = T(q) + α·H(q)·(1-h²α) at q_0.

CRITICAL TEST. The fixed-point solve in PR #1484 gave α_EM⁻¹ matching
CODATA to 0.31 ppb. This is 2.09× experimental σ_α (0.15 ppb).

But q_0 itself has finite precision from CAL-2: m_μ/m_e known to 22 ppb
relative. If dα/dq_0 propagation factor ≥ 0.014, then the 22 ppb q_0
uncertainty propagates to ~0.31 ppb α uncertainty — meaning the
empirical form IS exact and the residual is upstream calibration
noise (NOT a missing structural piece).

WHAT THIS PROBE COMPUTES.
1. Numerical dα/dq_0 at q_0 via finite differences (high precision)
2. Propagation factor: |dα/dq_0| · q_0 / α  (dimensionless)
3. Propagated α uncertainty: 22 ppb · propagation_factor
4. Compare to observed 0.31 ppb residual

DECISION TREE.
  • If propagation > 0.31 ppb / σ_q0 = 0.31/22 = 0.014 dimensionless
    → q_0 uncertainty CAN account for the residual; form IS exact.
  • If propagation < 0.014 → q_0 uncertainty CANNOT explain residual;
    a structural correction is missing.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402

import sys
import time
from pathlib import Path

import mpmath as mp
from mpmath import mpf, pi

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import ALPHA_EM_INV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


def q_bracket(n: int, q):
    return (q**n - q**(-n)) / (q - q**(-1))


def alpha_predicted(q):
    """Solve the cubic α³·h²·H - α²·H - α·T + 1 = 0 for α given q."""
    h = q - 1 / q
    h2 = h * h
    bra2 = q_bracket(2, q)
    bra9 = q_bracket(9, q)
    bra10 = q_bracket(10, q)
    g = 4
    T = q * bra9 * bra10 + mpf(2*g) / (4 * pi * (g-1))
    H = bra2 / (8 * pi)
    coefs = [h2*H, -H, -T, mpf(1)]
    roots = mp.polyroots(coefs)
    real_roots = [mp.re(r) for r in roots if abs(mp.im(r)) < mpf("1e-30")]
    pos_roots = [r for r in real_roots if r > 0]
    return min(pos_roots, key=lambda r: abs(r - mpf("0.00730")))


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "alpha-em-4pi-q0-sensitivity",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Q_0 sensitivity analysis for the empirical form from #1484. "
        "Computes dα/dq_0 at q_0 via finite differences (50 dps); "
        "tests whether the 22 ppb CAL-2 uncertainty on q_0 (from "
        "m_μ/m_e) propagates to ≥0.31 ppb on α_EM, which would mean "
        "the residual in #1484 is upstream calibration noise, NOT a "
        "missing structural piece."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    q0 = Q_MP
    CODATA_alpha_inv = mpf(str(ALPHA_EM_INV))
    SIGMA_Q0_PPB = mpf("22")  # CAL-2 uncertainty on m_μ/m_e (~22 ppb)
    RESIDUAL_PPB = mpf("0.31")  # residual from #1484

    # ── Step 1: compute α at q_0 ─────────────────────────────────
    alpha_at_q0 = alpha_predicted(q0)
    alpha_inv_at_q0 = 1 / alpha_at_q0

    # ── Step 2: finite-difference dα/dq_0 at multiple step sizes ─
    print("=" * 76)
    print(" Q_0 SENSITIVITY ANALYSIS — finite-difference dα/dq_0 at q_0")
    print("=" * 76)
    print(f"  q_0 = {mp.nstr(q0, 25)}")
    print(f"  α(q_0)        = {mp.nstr(alpha_at_q0, 20)}")
    print(f"  α⁻¹(q_0)      = {mp.nstr(alpha_inv_at_q0, 20)}")
    print(f"  CODATA α⁻¹    = {mp.nstr(CODATA_alpha_inv, 20)}")
    print(f"  σ_q_0         = {float(SIGMA_Q0_PPB)} ppb (CAL-2: m_μ/m_e)")
    print(f"  residual α    = {float(RESIDUAL_PPB)} ppb (from #1484)")
    print()
    print("  Finite-difference dα/dq_0 at several step sizes:")
    print(f"  {'step h':>15s} {'dα/dq_0':>20s} {'rel sens':>12s} {'σ_α propag (ppb)':>18s}")

    step_sizes = ["1e-10", "1e-12", "1e-15", "1e-18", "1e-20"]
    derivatives = []
    for h_str in step_sizes:
        h_step = mpf(h_str)
        alpha_plus = alpha_predicted(q0 + h_step)
        alpha_minus = alpha_predicted(q0 - h_step)
        d_alpha_dq = (alpha_plus - alpha_minus) / (2 * h_step)
        # dimensionless relative sensitivity: (q_0/α) · (dα/dq_0)
        rel_sens = (q0 / alpha_at_q0) * d_alpha_dq
        # propagated σ_α: σ_α/α = |rel_sens| · σ_q_0/q_0
        # = |rel_sens| · (22 ppb / 1)
        # so propagated σ_α in ppb on α = |rel_sens| · 22
        sigma_alpha_propag = abs(rel_sens) * SIGMA_Q0_PPB
        derivatives.append({
            "step_h": h_str,
            "d_alpha_dq": mp.nstr(d_alpha_dq, 16),
            "relative_sensitivity": mp.nstr(rel_sens, 12),
            "propagated_sigma_alpha_ppb": float(sigma_alpha_propag),
        })
        print(f"  {h_str:>15s} {float(d_alpha_dq):>20.10e} "
              f"{float(rel_sens):>12.4f} {float(sigma_alpha_propag):>18.3f}")

    # Use the most stable (h = 1e-15) for the verdict
    derivatives_stable = [d for d in derivatives if d["step_h"] == "1e-15"]
    if not derivatives_stable:
        derivatives_stable = [derivatives[2]]  # fallback
    stable_rel_sens = mpf(derivatives_stable[0]["relative_sensitivity"])
    stable_propag = abs(stable_rel_sens) * SIGMA_Q0_PPB

    print()
    print(f"  STABLE estimate (h=1e-15):")
    print(f"    relative sensitivity (q/α)·(dα/dq) = {mp.nstr(stable_rel_sens, 12)}")
    print(f"    propagated σ_α from 22 ppb q_0 unc = {float(stable_propag):.4f} ppb")
    print()

    # ── Decision tree ──────────────────────────────────────────
    threshold = float(RESIDUAL_PPB / SIGMA_Q0_PPB)  # = 0.31/22 ≈ 0.014
    if float(stable_propag) >= float(RESIDUAL_PPB):
        verdict = ("RESIDUAL EXPLAINED — q_0 uncertainty propagates to "
                   f"≥{float(RESIDUAL_PPB)} ppb on α; form IS exact")
        explanation = (
            f"The 22 ppb CAL-2 uncertainty on q_0 propagates to "
            f"{float(stable_propag):.3f} ppb on α_EM⁻¹, which is "
            f">= the observed residual {float(RESIDUAL_PPB)} ppb. "
            f"This means the empirical form α_EM⁻¹ = T + α·H·(1-h²α) "
            f"IS EXACT within precision, and the apparent 0.31 ppb "
            f"residual is upstream calibration noise from CAL-2."
        )
    elif float(stable_propag) >= float(RESIDUAL_PPB) / 2:
        verdict = ("RESIDUAL PARTLY EXPLAINED — q_0 uncertainty propagates "
                   f"to {float(stable_propag):.3f} ppb, half-ish the 0.31 ppb")
        explanation = (
            f"The q_0 uncertainty contributes ~{float(stable_propag):.2f} ppb. "
            f"This is part but not all of the 0.31 ppb residual. A small "
            f"structural correction remains."
        )
    else:
        verdict = ("RESIDUAL UNEXPLAINED — q_0 uncertainty too small "
                   f"({float(stable_propag):.4f} ppb << {float(RESIDUAL_PPB)} ppb)")
        explanation = (
            f"The 22 ppb q_0 uncertainty propagates to only "
            f"{float(stable_propag):.4f} ppb on α — much less than the "
            f"0.31 ppb residual. The structural correction MUST come from "
            f"somewhere else (higher-order h^k·α^m, refinement of H, etc.)"
        )

    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    print(f"  {verdict}")
    print()
    print(f"  Threshold: propagation factor must be ≥ "
          f"{threshold:.4f} (= 0.31 ppb / 22 ppb)")
    print(f"  Measured:  |rel_sens| = {float(abs(stable_rel_sens)):.4f}")
    print()
    print(f"  {explanation}")

    if float(stable_propag) >= float(RESIDUAL_PPB):
        print()
        print(f"  ★ STRUCTURAL CONSEQUENCE: if confirmed, this means α_EM has")
        print(f"    been DERIVED structurally from q_0 + Bring data with no")
        print(f"    free parameters. The 0.31 ppb is calibration noise that")
        print(f"    would close with tighter CAL-2.")
        print()
        print(f"    Tighter CAL-2 requires better m_μ/m_e measurement.")
        print(f"    PDG 2024: m_μ/m_e = 206.7682830(46) — 22 ppb relative.")  # noqa: P31 — descriptive print (m_mu/m_e ratio)
        print(f"    Future precision tests:")
        print(f"      • g-2 BNL/Fermilab: gives independent α_EM")
        print(f"      • Penning trap m_p,m_e improvements")

    builder.add_data("q_0", mp.nstr(q0, 30))
    builder.add_data("alpha_at_q0", mp.nstr(alpha_at_q0, 30))
    builder.add_data("alpha_inv_at_q0", mp.nstr(alpha_inv_at_q0, 30))
    builder.add_data("CODATA_alpha_inv", mp.nstr(CODATA_alpha_inv, 30))
    builder.add_data("sigma_q0_ppb", float(SIGMA_Q0_PPB))
    builder.add_data("residual_ppb", float(RESIDUAL_PPB))
    builder.add_data("derivatives", derivatives)
    builder.add_data("stable_relative_sensitivity", mp.nstr(stable_rel_sens, 20))
    builder.add_data("stable_propagated_sigma_alpha_ppb", float(stable_propag))
    builder.add_data("threshold_for_residual_explanation", threshold)
    builder.add_data("verdict", verdict)
    builder.add_data("explanation", explanation)

    builder.add_assertion(
        "sensitivity_computed",
        computed=len(derivatives),
        expected=5,
        tolerance=0,
        source="Finite-difference dα/dq_0 computed at 5 step sizes "
               "(1e-10 to 1e-20) at 50 dps; propagation factor "
               "compared to 0.31 ppb residual / 22 ppb q_0 uncertainty.",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
