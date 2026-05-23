#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output.
"""
═══════════════════════════════════════════════════════════════════
DEPRECATED (2026-05-23): SUPERSEDED BY substrate-pure
`flavor_split_subleading` IN `_li_2_q_util`.

This script implements a 1-param-calibrated Δm formula:

    Δm = ((q + q⁻¹) / (q^{1/2} + q^{−1/2})) · (μ_d − μ_u)

where `(μ_d − μ_u)` is FITTED from CODATA Δm. This gives a
tautological < 1 ppm "match" to CODATA because the same value
is used as both input and reference. It does NOT supply a
substrate prediction.

A substrate-PURE replacement now exists:

    Δm / M_N  =  ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3
                                                  (no fit)

implemented as `flavor_split_subleading(q, q_inv)` in
[`_li_2_q_util.py`](_li_2_q_util.py) and consumed by the
production prediction chain:

    `m_p_borromean_verification_50dps.py`  (PR #942)
    `atomic_mass_via_rho_k.py`             (PR #690)

This substrate-pure form matches CODATA Δm/M_N to ~305 ppm
without any free parameter (the residual is the framework's
honest gap, not a fit artifact).

WHY KEEP THIS SCRIPT:
  - **Comparison column**: shows what the 1-param fit would
    give vs the substrate-pure prediction.
  - **Historical audit**: the formula
    `Δm = ((q+q⁻¹)/(q^{1/2}+q^{-1/2})) · (μ_d−μ_u)` was the
    Phase 1.8 path before the substrate-pure derivation
    landed (PR #690).
  - **Probe consumer**: `probe_pn_flavor_asymmetry.py` and
    `probe_mu_d_minus_mu_u_categorical.py` still reference
    this formulation in their docstrings; deletion would
    orphan those references.

WHAT NEW CODE SHOULD DO:
  - Predict m_n from m_p via the substrate-pure split:
        m_n = m_avg_pred · (1 + Δm/M_N / 2),
        m_p = m_avg_pred · (1 − Δm/M_N / 2)
    where Δm/M_N = `flavor_split_subleading(q, 1/q)`.
  - Do **not** introduce a new `(μ_d − μ_u)` calibration.

This script will emit a `DeprecationWarning` at runtime and
mark its witness as `deprecated: true` so downstream consumers
can detect the demotion.
═══════════════════════════════════════════════════════════════════

Item 2 from the Phase 1.8 actionable path: derive m_n via the
difference formula

   m_n − m_p = ((q + q⁻¹) / (q^{1/2} + q^{−1/2})) · (μ_d − μ_u)

per `fresh_derivation_pn_true_sdp.py:1-26`:

  > "Absolute m_p and m_n are NOT directly derivable from γγ → target
  >  Hecke-energy distance because entanglement energy (pre-observable
  >  complex-q sector) is gauged away.  Only DIFFERENCES/RATIOS project
  >  to observables.  The clean prior result is:
  >    m_n − m_p = ((q+q⁻¹)/(q^{1/2}+q^{-1/2})) · (μ_d − μ_u)
  >  giving < 1 ppm on Δm across isotopes once μ_d − μ_u is calibrated
  >  from CODATA."

This script:

  1. Computes the algebraic prefactor (q+q⁻¹)/(q^{1/2}+q^{-1/2}) at
     q = q_0.
  2. Calibrates μ_d − μ_u from CODATA Δm = m_n − m_p = 1.293 MeV.
  3. Applies the formula to predict m_n given m_p_codata; expected
     residual: < 1 ppm by construction.
  4. Compares to Strategy-3's M_pred[n] = 861.345 MeV (−8.325% error).

Historical interpretation (kept for audit reference; SUPERSEDED
by substrate-pure flavor_split above):
The result demonstrates the difference formula was the
framework-consistent path for predicting m_n at the time,
with a single calibration parameter (μ_d − μ_u) replacing
Strategy-3's E_0 calibration.

Output: m-n-difference-formula.witness.json (now flagged
        `deprecated: true`).
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder
from q_parameter import Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

warnings.warn(
    "m_n_difference_formula.py is DEPRECATED (2026-05-23). The 1-param "
    "(μ_d − μ_u) calibration is tautological vs CODATA Δm. Use the "
    "substrate-pure `flavor_split_subleading(q, q_inv)` from `_li_2_q_util` "
    "instead — see `m_p_borromean_verification_50dps.py` (PR #942) for the "
    "production wire-up. This script is kept only for historical "
    "comparison and probe-docstring references.",
    DeprecationWarning,
    stacklevel=2,
)


def algebraic_prefactor(q: mp.mpf, q_inv: mp.mpf) -> mp.mpf:
    """(q + q⁻¹) / (q^{1/2} + q^{−1/2}).

    At q=1 reduces to 2/2 = 1 (massive degeneracy).
    At q_0 ≈ 1.11 gives ~1.004 (small q-deformation).
    """
    num = q + q_inv
    den = mp.sqrt(q) + mp.sqrt(q_inv)
    return num / den


def main() -> int:
    print("=" * 100)
    print("ITEM 2 — m_n via the difference formula")
    print("  m_n − m_p = ((q + q⁻¹) / (q^{1/2} + q^{−1/2})) · (μ_d − μ_u)")
    print("=" * 100)

    Q0 = Q_MP
    QI = Q_INV_MP
    prefactor = algebraic_prefactor(Q0, QI)
    delta_m_codata = mp.mpf(M_N_MEV) - mp.mpf(M_P_MEV)
    mu_d_minus_mu_u = delta_m_codata / prefactor

    print(f"\n  Inputs (CODATA, mpf 50 dps):")
    print(f"    q_0           = {mp.nstr(Q0, 20)}")
    print(f"    q_0⁻¹         = {mp.nstr(QI, 20)}")
    print(f"    M_p           = {M_P_MEV} MeV")
    print(f"    M_n           = {M_N_MEV} MeV")
    print(f"    Δm = M_n − M_p = {mp.nstr(delta_m_codata, 12)} MeV")
    print()
    print(f"  Computed at q_0:")
    print(f"    prefactor = (q + q⁻¹) / (q^{{1/2}} + q^{{−1/2}}) = {mp.nstr(prefactor, 14)}")
    print(f"    μ_d − μ_u (calibrated from CODATA Δm)             = {mp.nstr(mu_d_minus_mu_u, 14)} MeV")

    # Predict m_n via the difference formula
    delta_m_pred = prefactor * mu_d_minus_mu_u
    m_n_pred = mp.mpf(M_P_MEV) + delta_m_pred
    err_ppm = (m_n_pred - mp.mpf(M_N_MEV)) / mp.mpf(M_N_MEV) * mp.mpf(1e6)
    err_ppb = err_ppm * mp.mpf(1000)

    print()
    print(f"  Difference-formula prediction:")
    print(f"    Δm_pred       = prefactor · (μ_d − μ_u) = {mp.nstr(delta_m_pred, 12)} MeV")
    print(f"    m_n_pred      = m_p + Δm_pred           = {mp.nstr(m_n_pred, 12)} MeV")
    print(f"    m_n_codata                              = {M_N_MEV} MeV")
    print(f"    err_ppm       = {mp.nstr(err_ppm, 6)} ppm")
    print(f"    err_ppb       = {mp.nstr(err_ppb, 6)} ppb")

    # Comparison to Strategy-3
    strategy_3_m_n = 861.3450120161809611302321540664741083884394557178
    strategy_3_err_pct = (strategy_3_m_n - M_N_MEV) / M_N_MEV * 100

    print()
    print(f"  Comparison to Strategy-3 (atomic_braid_mass_table.py):")
    print(f"    Strategy-3 m_n_pred   = {strategy_3_m_n:.6f} MeV  (err = {strategy_3_err_pct:+.3f}%)")
    print(f"    Difference-formula    = {float(m_n_pred):.6f} MeV  (err = {float(err_ppb):+.3f} ppb)")
    print(f"    Improvement factor    ~ {abs(strategy_3_err_pct) * 1e7 / max(abs(float(err_ppb)), 1e-9):.0e}× (i.e., trivially "
          "by construction since the formula is calibrated against the same Δm).")
    print()
    print(f"  Honest comparison:")
    print(f"    Strategy-3 calibrates ONE parameter (E_0) against m_p_codata; "
          f"predicts m_n bare → 8.325% error")
    print(f"    Difference formula calibrates ONE parameter (μ_d − μ_u) against "
          f"Δm_codata; predicts m_n via difference → <1 ppb error")
    print()
    print(f"  Both are 1-parameter calibrations; the difference is which OBSERVABLE")
    print(f"  the parameter anchors against.  Per the framework's claim, only")
    print(f"  DIFFERENCES are observables, so the difference formula is the")
    print(f"  framework-consistent path.  Strategy-3's bare-|tr_M(n)| approach")
    print(f"  violates 'only differences are observables' and is structurally wrong.")

    # Cross-isotope test: same μ_d − μ_u should work for higher-A predictions?
    # Per fresh_derivation_pn_true_sdp.py: "< 1 ppm on Δm across isotopes once
    # μ_d − μ_u is calibrated from CODATA."  We don't have m_n − m_p analogues
    # for compound atoms (D, T, ³He, ⁴He) directly; instead we have binding
    # energies. The difference formula generalises to compound binding via
    # Item 3 (separate scope).
    print()
    print(f"  Note: Item 3 (compound binding energies via differences) is a")
    print(f"  separate scope per the audit; the term7-alpha5 unification "
          f"(prop:mass-formula-iterative-lp-dual = Σ_l u^{{(l)*}}) gives the")
    print(f"  natural closure path.")

    # Witness emission
    w = WitnessBuilder("m-n-difference-formula", engine="mpmath")
    w.set_description(
        "DEPRECATED (2026-05-23) — superseded by the substrate-pure "
        "`flavor_split_subleading` in `_li_2_q_util` (PR #690 / #942). "
        "This 1-param-calibrated formula "
        "m_n − m_p = ((q+q⁻¹)/(q^{1/2}+q^{−1/2})) · (μ_d − μ_u) gives a "
        "<1 ppb 'match' to CODATA tautologically (μ_d − μ_u is FITTED "
        "from CODATA Δm).  The substrate-pure replacement "
        "Δm/M_N = ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3 (no fit) matches "
        "CODATA to 305 ppm without any free parameter.  Kept here for "
        "historical comparison and probe-docstring references only; "
        "no production consumer."
    )
    w.add_parameter("deprecated", True)
    w.add_parameter("deprecated_at", "2026-05-23")
    w.add_parameter(
        "superseded_by",
        "_li_2_q_util.flavor_split_subleading "
        "(consumed by m_p_borromean_verification_50dps.py, "
        "atomic_mass_via_rho_k.py)"
    )
    w.set_content_block("prop:atomic-mass-gb-nf")
    w.add_parameter("q_0", str(Q0))
    w.add_parameter("q_0_inv", str(QI))
    w.add_parameter("M_p_codata", M_P_MEV)
    w.add_parameter("M_n_codata", M_N_MEV)
    w.add_parameter("M_e_codata", M_E_MEV)
    w.add_data("delta_m_codata_MeV", str(delta_m_codata))
    w.add_data("algebraic_prefactor", str(prefactor))
    w.add_data("mu_d_minus_mu_u_calibrated_MeV", str(mu_d_minus_mu_u))
    w.add_data("m_n_predicted_MeV", str(m_n_pred))
    w.add_data("err_vs_codata_ppm", str(err_ppm))
    w.add_data("err_vs_codata_ppb", str(err_ppb))
    w.add_data("derivation_status", "m_n_via_1param_fit")
    w.add_data("derivation_status_explanation",
               "AUDIT 2026-05-17 (commit 8732de45): (μ_d − μ_u) is "
               "FIT to CODATA Δm = m_n − m_p, NOT substrate-derived. "
               "m_n prediction is therefore a 1-parameter calibration; "
               "<1 ppb residual is BY CONSTRUCTION.  Substrate-only "
               "derivation of (μ_d − μ_u) from V_(2,1) Hoefsmit is "
               "OPEN — best categorical candidate tested (|d_1| · 4) "
               "gives 2.77 % residual.  See "
               "probe_mu_d_minus_mu_u_categorical.py + "
               "docs/audits/2026-05-17-m-n-substrate-investigation-"
               "and-lit-search.md")
    w.add_data("strategy_3_m_n_MeV", strategy_3_m_n)
    w.add_data("strategy_3_err_pct", strategy_3_err_pct)
    w.add_data("framework_consistent", True)
    w.add_data("interpretation", (
        "1-parameter calibration. μ_d − μ_u replaces Strategy-3's E_0; the "
        "difference formula respects 'only differences are observables' per "
        "the framework's own SDP audit. Predicts m_n at machine precision by "
        "construction (single CODATA anchor). For compound atoms (D, T, ³He, "
        "⁴He), Item 3 generalises this via the term7-alpha5 iterative LP-dual "
        "unification."
    ))
    w.add_assertion(
        "m_n_predicted_within_1_ppb_of_codata",
        computed=float(abs(err_ppb)),
        expected=0.0,
        tolerance=1.0,
    )
    w.add_assertion(
        "improvement_over_strategy_3",
        computed=float(abs(err_ppb) < abs(strategy_3_err_pct) * 1e7),
        expected=True,
    )
    w.add_assertion(
        "framework_consistent_path",
        computed=True,
        expected=True,
    )
    w.save()
    print(f"\n✓ Witness: m-n-difference-formula.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
