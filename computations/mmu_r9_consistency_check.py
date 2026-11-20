#!/usr/bin/env python3
"""mmu_r9_consistency_check.py — R9 hbar_q^6 * q / 5 m_μ closure check.

The 30-candidate NEGATIVE bracket for m_μ categorical corrections
identified R9 = `ℏ_q^6 × q / 5` as the closest single-formula candidate
at 1,152 ppm vs target δ = 2.098e-7. The Kashiwara cos-factor pivot
(10 more candidates) didn't improve on R9.

CRITICAL RE-ANALYSIS: R9's miss vs target is BELOW the CODATA σ_exp
propagated uncertainty on δ. This script makes the comparison precise
and documents R9's status as a Δ_λ-gate caution candidate.

What this script computes:
  1. m_μ_pred_bare = m_e × Vol(4_1) / ℏ_q²  (production formula)
  2. m_μ_pred_R9   = m_e × Vol(4_1) / ℏ_q² × (1 - ℏ_q^6 × q / 5)
  3. Compare both to CODATA m_μ + σ_exp:
       - bare miss-factor (currently 963.6× per dashboard)
       - R9 miss-factor (the test)
  4. Document the Δ_λ-gate audit:
       - Is "× q / 5" a derived form or a 2-parameter fit?
       - The "q" multiplier and "5" divisor were chosen empirically
         to land near target — this is a FIT pattern
       - But the form IS structurally suggestive (q = single q-factor;
         5 = T(2,5) crossing number for muon torus knot)
       - Without a Lean derivation, R9 is at best a "near-match" tier
         in the qbeta-style {derived / cal-anchored / near-match} ladder

VERDICT framework:
  - R9 within CODATA experimental uncertainty → empirically consistent
  - R9 closes 100× L2 if it's the right formula → would be SIGNIFICANT
  - But Δ_λ-gate forbids fitted forms in production
  - Report R9 as a near-match candidate for owner direction on whether
    to formally pursue Lean derivation
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from knot_volumes import vol_at  # noqa: E402 — canonical volume registry

# Vol(4_1) is EXCISED, not corrected (bean qou-ckbv, 2026-08-30).
# This file carried VOL_4_1_STR = "2.0298832128193072500115970029" -- 29
# digits printed, 19 correct, the same 20-digit carrier bean qou-f8lit
# tracks. Vol(4_1) has a closed form, 2*Cl_2(pi/3); a literal for it can
# only ever be a truncation of something the machine can compute exactly,
# so the fix is deletion rather than re-transcription.

# CODATA 2022 values for direct cross-check
M_E_CODATA_MEV = "0.51099895069"
M_MU_CODATA_MEV = "105.6583755"
M_MU_SIGMA_EXP_MEV = "2.3e-6"


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("mmu-r9-consistency-check", engine="mpmath")

    q_mp = Q_MP
    me = mpf(M_E_CODATA_MEV)
    m_mu_codata = mpf(M_MU_CODATA_MEV)
    sigma_exp = mpf(M_MU_SIGMA_EXP_MEV)
    vol_4_1 = vol_at("4_1")

    hbar_q = (q_mp - 1) / q_mp
    hbar_q_sq = hbar_q ** 2

    # Bare production formula
    m_mu_pred_bare = me * vol_4_1 / hbar_q_sq
    bare_err = m_mu_pred_bare - m_mu_codata
    bare_err_ppb = float(bare_err / m_mu_codata * 1e9)

    # R9 corrected prediction
    delta_r9 = hbar_q ** 6 * q_mp / 5
    m_mu_pred_r9 = me * vol_4_1 / hbar_q_sq * (1 - delta_r9)
    r9_err = m_mu_pred_r9 - m_mu_codata
    r9_err_ppb = float(r9_err / m_mu_codata * 1e9)

    # 100x L2 target
    sigma_exp_ppb = float(sigma_exp / m_mu_codata * 1e9)
    target_100x_ppb = sigma_exp_ppb / 100

    bare_miss_factor = float(abs(bare_err_ppb) / target_100x_ppb)
    r9_miss_factor = float(abs(r9_err_ppb) / target_100x_ppb)

    print("=" * 76)
    print(" m_μ R9 consistency check — does ℏ_q^6·q/5 close to 100× L2?")
    print("=" * 76)
    print()
    print(f"  q₀         = {mp.nstr(q_mp, 14)}")
    print(f"  ℏ_q        = {mp.nstr(hbar_q, 14)}")
    print(f"  ℏ_q²       = {mp.nstr(hbar_q_sq, 14)}")
    print(f"  Vol(4_1)   = {mp.nstr(vol_4_1, 18)}")
    print()
    print(f"  CODATA m_μ = {mp.nstr(m_mu_codata, 12)} MeV")
    print(f"  σ_exp      = {mp.nstr(sigma_exp, 6)} MeV = {sigma_exp_ppb:.2f} ppb")
    print(f"  100× tgt   = {target_100x_ppb:.4f} ppb")
    print()
    print("─" * 76)
    print(" Bare formula: m_μ = m_e × Vol(4_1) / ℏ_q²")
    print("─" * 76)
    print(f"  m_μ_bare     = {mp.nstr(m_mu_pred_bare, 14)} MeV")
    print(f"  err vs CODATA = {bare_err_ppb:+.4f} ppb")
    print(f"  miss factor   = {bare_miss_factor:.2f}× (target = 1×)")
    print()
    print("─" * 76)
    print(" R9 correction: m_μ = m_e × Vol(4_1) / ℏ_q² × (1 - ℏ_q^6·q/5)")
    print("─" * 76)
    print(f"  δ_R9          = {mp.nstr(delta_r9, 12)}")
    print(f"  m_μ_R9        = {mp.nstr(m_mu_pred_r9, 14)} MeV")
    print(f"  err vs CODATA = {r9_err_ppb:+.4f} ppb")
    print(f"  miss factor   = {r9_miss_factor:.2f}× (target = 1×)")
    print()
    print("─" * 76)
    print(" VERDICT — Δ_λ-gate audit")
    print("─" * 76)

    r9_within_exp = abs(r9_err_ppb) <= sigma_exp_ppb
    r9_meets_l2 = r9_miss_factor <= 1.0
    improvement = bare_miss_factor / r9_miss_factor if r9_miss_factor > 0 else float("inf")

    if r9_meets_l2:
        print(f"  ✓ R9 MEETS L2 100× target ({r9_miss_factor:.3f}× vs 1× gate)")
    else:
        print(f"  ✗ R9 misses L2 100× target ({r9_miss_factor:.3f}× vs 1× gate)")

    if r9_within_exp:
        print(f"  ✓ R9 within CODATA σ_exp ({abs(r9_err_ppb):.3f} ppb vs σ_exp={sigma_exp_ppb:.2f} ppb)")
    else:
        print(f"  ✗ R9 outside CODATA σ_exp ({abs(r9_err_ppb):.3f} ppb vs σ_exp={sigma_exp_ppb:.2f} ppb)")

    print(f"  R9 improves bare prediction by {improvement:.1f}×")
    print()
    print("  Δ_λ-gate caveat: 'ℏ_q^6 × q / 5' is a 2-parameter fit pattern:")
    print("    - 'q' multiplier chosen empirically (anti-bar-invariant; unusual)")
    print("    - '5' divisor coincides with T(2,5) muon torus knot crossings")
    print("    - No Lean derivation; structurally suggestive but not derived")
    print()
    print("  Status: R9 = 'near-match' tier. Promotion to 'derived' requires:")
    print("    1. Lean theorem identifying ℏ_q^6 categorical origin")
    print("    2. Lean theorem identifying 'q × (1/5)' as a T(2,5)-derived factor")
    print("    3. (Optional) Cross-anchor consistency check at lepton/tau levels")

    # Assertions
    wb.add_assertion(
        "r9_within_codata_sigma_exp",
        computed=r9_within_exp,
        expected=True,
        source="R9's residual error against CODATA m_μ should be ≤ σ_exp = 21.77 ppb "
               "if R9 is an experimentally-consistent candidate.",
    )
    wb.add_assertion(
        "r9_meets_100x_l2_target",
        computed=r9_meets_l2,
        expected=True,
        source="R9's residual error against CODATA m_μ should be ≤ σ_exp/100 = 0.2177 "
               "ppb for the 100× L2 target.",
    )

    wb.add_data("q_substrate", mp.nstr(q_mp, 30))
    wb.add_data("m_mu_codata_MeV", mp.nstr(m_mu_codata, 30))
    wb.add_data("sigma_exp_MeV", mp.nstr(sigma_exp, 30))
    wb.add_data("sigma_exp_ppb", sigma_exp_ppb)
    wb.add_data("target_100x_ppb", target_100x_ppb)
    wb.add_data("m_mu_pred_bare_MeV", mp.nstr(m_mu_pred_bare, 30))
    wb.add_data("bare_err_ppb", bare_err_ppb)
    wb.add_data("bare_miss_factor", bare_miss_factor)
    wb.add_data("delta_r9", mp.nstr(delta_r9, 30))
    wb.add_data("m_mu_pred_r9_MeV", mp.nstr(m_mu_pred_r9, 30))
    wb.add_data("r9_err_ppb", r9_err_ppb)
    wb.add_data("r9_miss_factor", r9_miss_factor)
    wb.add_data("improvement_factor", improvement)
    wb.add_data("r9_within_codata_sigma_exp", r9_within_exp)
    wb.add_data("r9_meets_l2_100x", r9_meets_l2)
    wb.add_data("delta_lambda_gate_status", "near-match (fit pattern, not derived)")
    wb.add_data("derivation_status", (
        "R9 = ℏ_q^6 × q / 5 is empirically suggestive but NOT structurally derived. "
        "The 'q' multiplier (anti-bar-invariant) and '5' divisor (matching T(2,5) "
        "muon knot crossings) hint at categorical content but have no Lean theorem "
        "yet. Promotion from 'near-match' to 'derived' requires: (1) Lean ℏ_q^6 "
        "categorical origin, (2) Lean q × (1/5) T(2,5)-factor derivation, "
        "(3) cross-anchor electron/tau consistency check."
    ))

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"all {'passed' if all(a.passed for a in wb.assertions) else 'FAILED'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
