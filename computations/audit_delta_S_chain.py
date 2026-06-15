#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
═══════════════════════════════════════════════════════════════

Audit: ΔS(n−p) = (Q_β + m_e)/m_e / (Vol(ℬ_3)/ℏ_q²) — derivation chain.

Verifies that the 1015 ppm residual in `derive_m_baryon_volume_form.py`'s
ΔS_derived vs ΔS_empirical_target is NOT a coincidence: it is
algebraically forced by Q_β's closed-form residual against AME.

CHAIN:
  1. Definitionally, m_n - m_p = Q_β + m_e  (neutron β-decay Q-value).
  2. So (m_n - m_p)/m_e = Q_β/m_e + 1.
  3. The Vol-form mass formula gives the empirical λ_scale target as
       m_n/m_e = (Vol(ℬ_3)/ℏ_q²) · λ_scale_n + S(n)
       m_p/m_e = (Vol(ℬ_3)/ℏ_q²) · λ_scale_p + S(p)
     Subtracting:
       (m_n - m_p)/m_e = (Vol(ℬ_3)/ℏ_q²) · Δλ + ΔS,    ΔS = S(n) - S(p)
     If Δλ ≈ 0 (single-Borromean-baryon ansatz: λ shared across (p,n,3-k)
     orientations), then
       ΔS = (m_n - m_p)/m_e / (Vol(ℬ_3)/ℏ_q²)
          = (Q_β + m_e)/m_e / (Vol(ℬ_3)/ℏ_q²).        (*)
  4. Q_β is predicted from CAL-1+CAL-2 via prop:neutron-qvalue-symbolic:
       Q_β_pred = m_e · |q² - 2q - 1| · (q + 1) / (2 q³)
     This has its own residual ε_Q := Q_β_pred / Q_β_AME - 1.
  5. (*) under Q_β_pred has residual
       ΔS_derived / ΔS_target - 1
        = (Q_β_pred - Q_β_AME) / (m_n - m_p)
        = ε_Q · Q_β_AME / (m_n - m_p)
        = ε_Q · Q_β_AME / (Q_β_AME + m_e)            ← Q_β/(Q_β + m_e)
        ≈ ε_Q · 0.605                              (damping factor)

So ε_ΔS = 0.605 · ε_Q. If ε_Q ≈ +1680 ppm then ε_ΔS ≈ +1015 ppm — the
observed value.

This script verifies the chain numerically at 50 dps.

Output: `delta-S-chain-audit.witness.json`
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402

from _precision import set_compute_dps, fmt
set_compute_dps()  # mp.mp.dps via QOU_COMPUTE_DPS (default 50)
from experimental_constants import VOL_BORROMEAN_50DPS_STR  # noqa: E402

VOL_BORROMEAN = mp.mpf(VOL_BORROMEAN_50DPS_STR)


def _q_0_50dps() -> mp.mpf:
    with (_pb.witness_path("q-pinning-50-digit.witness.json", HERE)).open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def _q_beta_closed_form(q: mp.mpf) -> mp.mpf:
    """Q_β predicted from CAL-1 m_e + CAL-2 q_0 (prop:neutron-qvalue-symbolic)."""
    return M_E_MEV * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


def main() -> int:
    q = _q_0_50dps()
    hbar_q = (q - 1) / q
    hbar_q2 = hbar_q ** 2
    V = VOL_BORROMEAN / hbar_q2

    m_e = mp.mpf(str(M_E_MEV))
    m_p = mp.mpf(str(M_P_MEV_VALIDATION))
    m_n = mp.mpf(str(M_N_MEV_VALIDATION))

    Q_beta_AME = m_n - m_p - m_e
    Q_beta_pred = _q_beta_closed_form(q)

    eps_Q = Q_beta_pred / Q_beta_AME - 1
    damping = Q_beta_AME / (Q_beta_AME + m_e)

    delta_S_target  = (m_n - m_p) / m_e / V
    delta_S_derived = (Q_beta_pred + m_e) / m_e / V

    eps_delta_S = delta_S_derived / delta_S_target - 1
    eps_delta_S_predicted = damping * eps_Q

    print("=" * 78)
    print("  ΔS(n−p) chain audit — verify the Q_β-residual propagation")
    print("=" * 78)
    print()
    print(f"  q_0          = {mp.nstr(q, 14)}")
    print(f"  Vol(ℬ_3)/ℏ_q² = {mp.nstr(V, 14)}  (exact under CAL-2)")
    print()
    print(f"  Q_β values:")
    print(f"    AME:        {mp.nstr(Q_beta_AME, 16)} MeV")
    print(f"    predicted:  {mp.nstr(Q_beta_pred, 16)} MeV")
    print(f"    ε_Q = Q_β_pred/Q_β_AME − 1 = {mp.nstr(eps_Q, 8)}  "
          f"(= {mp.nstr(eps_Q * 1e6, 6)} ppm)")
    print()
    print(f"  ΔS values:")
    print(f"    target (from CODATA):           {mp.nstr(delta_S_target, 14)}")
    print(f"    derived (from Q_β_pred):        {mp.nstr(delta_S_derived, 14)}")
    print(f"    ε_ΔS = derived/target − 1     = {mp.nstr(eps_delta_S, 8)}  "
          f"(= {mp.nstr(eps_delta_S * 1e6, 6)} ppm)")
    print()
    print(f"  Damping factor (algebraic):")
    print(f"    Q_β_AME / (Q_β_AME + m_e) = {mp.nstr(damping, 14)}")
    print(f"  Predicted ε_ΔS = damping · ε_Q = {mp.nstr(eps_delta_S_predicted, 8)} "
          f"(= {mp.nstr(eps_delta_S_predicted * 1e6, 6)} ppm)")
    print()

    chain_match = mp.fabs(eps_delta_S - eps_delta_S_predicted) / mp.fabs(eps_delta_S)
    # Threshold scales with the global mpmath precision floor (dps).
    # 10 digits of headroom below the dps floor catches genuine algebraic
    # mismatch while ignoring numerical noise in the last few mp digits.
    chain_threshold = mp.mpf(10) ** (-mp.mp.dps + 10)
    print(f"  Chain match: |ε_ΔS − damping · ε_Q| / |ε_ΔS| = {mp.nstr(chain_match, 6)}")
    print(f"  Threshold (10^(-dps+10) at dps={mp.mp.dps})       = {mp.nstr(chain_threshold, 6)}")
    print()
    if chain_match < chain_threshold:
        verdict = ("CHAIN VERIFIED EXACTLY: ε_ΔS = (Q_β/(Q_β+m_e)) · ε_Q. The "
                   "1015 ppm ΔS residual is the Q_β closed-form residual "
                   "damped by Q_β/(Q_β+m_e) ≈ 0.605. NOT a coincidence.")
    else:
        verdict = (f"Chain match imperfect (rel err {float(chain_match):.4e}) — "
                   f"there is some additional residual not captured by ε_Q.")
    print(f"  VERDICT: {verdict}")

    # Predict the ΔS residual under hypothetical Q_β closed-form tightening
    print()
    print(f"  ΔS precision if Q_β closed form is tightened:")
    for tighter_eps_Q_ppm in [1000, 100, 10, 1, 0.1, 0.01]:
        predicted_eps_dS_ppm = float(damping) * tighter_eps_Q_ppm
        print(f"    ε_Q = {tighter_eps_Q_ppm:>8.2f} ppm  →  "
              f"ε_ΔS ≈ {predicted_eps_dS_ppm:>8.4f} ppm")
    print()
    print(f"  ⇒ For 1 ppb on ΔS (10⁻³ ppm), need Q_β closed form to "
          f"~{float(1e-3 / damping):.4f} ppm precision.")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "delta-S-chain-audit",
        {
            "description": (
                "Audit of the ΔS = (Q_β + m_e)/m_e / (Vol(ℬ_3)/ℏ_q²) "
                "derivation chain. Verifies algebraically that the 1015 ppm "
                "ΔS residual in `derive_m_baryon_volume_form.py` is NOT "
                "coincidental — it equals the Q_β closed-form residual "
                "damped by the algebraic factor Q_β/(Q_β + m_e) ≈ 0.605. "
                "Implication: tightening Q_β's closed form propagates "
                "directly to ΔS precision."
            ),
            "data": {
                "q_0_50dps": fmt(q),
                "Vol_Borromean_over_hbar_q_squared": fmt(V),
                "Q_beta_AME_MeV": fmt(Q_beta_AME),
                "Q_beta_predicted_closed_form_MeV": fmt(Q_beta_pred),
                "eps_Q_pct": float(eps_Q * 100),
                "eps_Q_ppm": float(eps_Q * 1e6),
                "delta_S_target_dimensionless": fmt(delta_S_target),
                "delta_S_derived_dimensionless": fmt(delta_S_derived),
                "eps_delta_S_pct": float(eps_delta_S * 100),
                "eps_delta_S_ppm": float(eps_delta_S * 1e6),
                "damping_factor_Q_beta_over_Q_beta_plus_m_e": fmt(damping),
                "predicted_eps_delta_S_from_damping_x_eps_Q": fmt(eps_delta_S_predicted),
                "predicted_eps_delta_S_ppm": float(eps_delta_S_predicted * 1e6),
                "chain_match_relative_error": fmt(chain_match),
                "verdict": verdict,
                "Q_beta_precision_for_1_ppb_on_delta_S": float(1e-3 / damping),
            },
        },
        script_path=__file__,
        engine="mpmath",
    )
    out_path = builder.save()
    print(f"\n  Witness: {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
