#!/usr/bin/env python3
# polynomial_q_not_applicable: assembly script; consumes upstream
# β-decay-energy-scale witness + derived_masses module.
"""Emit the FULL-chain Q_β prediction witness.

Per owner directive 2026-05-10: "do not use LO -- use full. look at
discussion on observable vs nonobservable energy in case of beta decay."

This script produces `q-beta-predicted.witness.json` recording:

  * E_0 from the FULL chain: m_e / (q_0 (q_0 - 1)) ≈ 4.186 MeV
    — derived from CAL-1 m_e + CAL-2 q_0 only; CAL-3 𝔇_π is the
    OUTPUT, not an input.
  * Q_β predicted (single-wrap symbolic closed form):
        Q_β = m_e · |q_0² - 2q_0 - 1| · (q_0 + 1) / (2 q_0³)
            ≈ 0.7836 MeV — vs CODATA 0.7823 MeV (+0.168% /
        +1.31 keV residual)
  * The typed-crossings 6-term form Q_β ≈ 0.788 MeV (+0.747%)
    is retained in the witness as a legacy cross-check only;
    the single-wrap closed form is 4.46× tighter and is the
    canonical prediction.
  * Observable / virtual decomposition (ℓ ≥ 2 vs ℓ < 2) is
    reported on the typed-crossings basis where it is well-
    defined: Q_obs ≈ 0.461 MeV (58.46% — Hopf links + trefoil),
    Q_virt ≈ 0.327 MeV (41.54% — γ + σ_0 + σ_1). At single
    wrap the L_± and e^- channels cancel exactly between proton
    and neutron, so the entire Q-value lives in γ + σ_0 + σ_1.

References:
  * `prop:beta-decay-energy-scale`
    (content/quantum-observable-universe/particle-interactions/
     beta-decay-energy-scale.md)
  * `prop:meson-to-proton-via-borromean`
    (content/quantum-observable-universe/archimedean-universe/
     meson-to-proton-via-borromean.md)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

import mpmath as mp

# Set 50 dps BEFORE importing codata_constants — its mp.mpf
# constants are built at import time and otherwise inherit the
# default 15 dps (per Copilot review on PR #639 q-beta-predicted.
# witness.json:8 / 10 — fixes binary-rounded m_e_MeV strings AND
# lets the WitnessBuilder timer below cover the full computation).
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import derived_masses as dm  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

OUT = HERE / "q-beta-predicted.witness.json"


def main() -> int:
    # Instantiate WitnessBuilder at the TOP of main so durationMs
    # captures the full symbolic + numerical work (per Copilot
    # review on q-beta-predicted.witness.json:10 — previously
    # wrap_legacy was called at the END, giving durationMs = 0).
    builder = WitnessBuilder("q-beta-predicted", engine="mpmath")

    # Measure full end-to-end runtime (per Copilot review note on
    # under-reporting; covers all symbolic + numerical work below
    # plus the JSON write).
    t_start = time.time()

    summary = dm.derivation_summary()
    e0_full = dm.e_0_full_mev()
    e0_cal = dm.e_0_calibrated_mev()
    q_pred = dm.q_beta_predicted_mev()  # single-wrap symbolic
    q_pred_tc = dm.q_beta_predicted_typed_crossing_mev()  # legacy 6-term
    q_obs = dm.q_beta_observable_mev()
    q_virt = dm.q_beta_virtual_mev()
    q_codata = mp.mpf(str(Q_BETA_MEV))

    # Sanity: q_obs + q_virt is computed on the typed-crossings 6-term
    # basis (Δ(net) = Δ(obs) + Δ(virt)), so it should equal q_pred_tc
    # within rounding — NOT q_pred (the single-wrap closed form is
    # ≈4.5 keV lower, an expected typed-crossings-vs-single-wrap
    # mismatch, not a rounding residual).
    sum_check = q_obs + q_virt
    sum_residual_mev = abs(sum_check - q_pred_tc)

    # Set top-level metadata on the existing builder (instantiated
    # at the top of main so durationMs covers full runtime).
    builder.set_description(
        "FULL-chain Q_β prediction per prop:beta-decay-energy-scale. "
        "E_0 derived from CAL-1 m_e + CAL-2 q_0 only (no CAL-3 input); "
        "Q_β predicted via |Δ(net)| · E_0; observable/virtual split by "
        "Coxeter length ℓ ≥ 2 (Hopf links + trefoil) vs ℓ < 2 (γ + σ_0 "
        "+ σ_1). Owner directive 2026-05-10: do not use LO; use FULL."
    )
    builder.set_content_block("rem:beta-decay-energy-scale")
    builder.set_audit_only(
        "docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md"
    )

    # Build the legacy 'out' payload (without engine/scriptFile/
    # computedAt/durationMs/assertions/allPassed — those are auto-
    # supplied by the builder; assertions are routed via add_assertion
    # below).
    out = {
        "calibration_inputs_used": [
            "CAL-1 (m_e_MeV from codata_constants)",
            "CAL-2 (q_0 from q-pinning-50-digit.witness.json)",
        ],
        "calibration_inputs_NOT_used": [
            "CAL-3 (Q_β) — predicted, not consumed",
            "CODATA m_p, m_n, m_4He, etc. — predictions, not inputs "
            "(per Workplan 0a discipline)",
        ],
        "parameters": {
            "m_e_MeV": str(M_E_MEV),
            "q_0_50dps": str(dm._q_0()),
        },
        "data": {
            "energy_scale_E_0": {
                "E_0_full_MeV": str(e0_full),
                "E_0_full_formula": "m_e / (q_0 (q_0 - 1)) = m_e c_q² ℏ_q",
                "E_0_calibrated_MeV": str(e0_cal),
                "E_0_calibrated_formula": "Q_β_CODATA / |Δ(net)|",
                "agreement_pct": str(
                    (e0_full - e0_cal) / e0_cal * 100
                ),
                "residual_attribution": (
                    "0.75% residual is the brane-tower correction: the "
                    "derived expression uses single-level c_q² ℏ_q, while "
                    "the calibrated value implicitly includes the full "
                    "tower of n and p (per beta-decay-energy-scale.md "
                    "§Calibration cross-check)."
                ),
            },
            "q_beta_prediction": {
                "Q_beta_pred_MeV": str(q_pred),
                "Q_beta_pred_formula": (
                    "Q_β = m_e · |q² - 2q - 1| · (q+1) / (2q³)  "
                    "(single-wrap symbolic form per "
                    "prop:neutron-qvalue-symbolic). The L_± and e^- "
                    "contributions cancel exactly at single wrap; "
                    "Q-value comes entirely from γ + σ_0 + σ_1 "
                    "channels."
                ),
                "Q_beta_codata_MeV": str(q_codata),
                "err_pct": str((q_pred - q_codata) / q_codata * 100),
                "err_keV": float((q_pred - q_codata) * 1000),
                "err_ppb": float((q_pred - q_codata) / q_codata * 1e9),
                "residual_attribution": (
                    "+0.17% / +1.31 keV is the brane-tower truncation "
                    "residual: derived E_0 = m_e/(q(q-1)) is the "
                    "single-level Planck-tick approximation; exact "
                    "tower-summed E_0 absorbs this 0.17%. Closure "
                    "path: Workplan 2 Phase 2 50-dps m_e_Hecke lift."
                ),
            },
            "q_beta_typed_crossings_legacy": {
                "Q_beta_pred_MeV": str(q_pred_tc),
                "Q_beta_pred_formula": "|Δ(net)| · E_0_full  (typed-crossings 6-term, Δ(net) = -0.18829 from beta-decay-energy-scale.witness.json)",
                "err_pct": str((q_pred_tc - q_codata) / q_codata * 100),
                "comment": (
                    "Legacy 6-term decomposition that gave +0.747% "
                    "error (the L_± and e^- channels picked up small "
                    "asymmetric contributions that exactly cancel at "
                    "single wrap). Replaced by the single-wrap "
                    "symbolic form above (4.5x improvement). Kept "
                    "here only for cross-check."
                ),
            },
            "observable_virtual_split": {
                "Q_observable_MeV": str(q_obs),
                "Q_observable_formula": "|Δ(obs)| · E_0  (ℓ ≥ 2 terms: Hopf links L_±, trefoil e^-)",
                "Q_observable_fraction": float(q_obs / q_pred),
                "Q_virtual_MeV": str(q_virt),
                "Q_virtual_formula": "|Δ(virt)| · E_0  (ℓ < 2 terms: γ, σ_0, σ_1)",
                "Q_virtual_fraction": float(q_virt / q_pred),
                "sum_obs_plus_virt_MeV": str(sum_check),
                "sum_residual_MeV": float(sum_residual_mev),
                "physical_interpretation": (
                    "Observable component (58.46%) is the topologically "
                    "non-trivial part — physical kinetic energy released "
                    "in the β-decay event. Virtual component (41.54%) is "
                    "the gauge / vacuum-debt contribution that cancels "
                    "in asymptotic states. See beta-decay-energy-scale.md "
                    "§'Observable vs virtual: Q_{≥2}'."
                ),
            },
        },
        "summary_for_humans": summary,
    }

    # Route the three assertions through builder.add_assertion so they
    # appear in the witness `assertions` array (per Copilot review on
    # q-beta-predicted.witness.json:8 — wrap_legacy was previously
    # routing them into _extra_top_level where they vanished from the
    # standard schema).
    builder.add_assertion(
        "Q_beta_pred_within_0.5_pct_of_codata",
        computed=float(abs(q_pred - q_codata) / q_codata),
        expected=0.0,
        tolerance=0.005,
    )
    builder.add_assertion(
        "Q_beta_pred_residual_under_2_keV",
        computed=float(abs(q_pred - q_codata) * 1000),
        expected=0.0,
        tolerance=2.0,
    )
    builder.add_assertion(
        "single_wrap_beats_typed_crossings",
        computed=float(abs(q_pred - q_codata)),
        expected=0.0,
        tolerance=float(abs(q_pred_tc - q_codata)),
    )

    # Route every remaining `out` key onto the builder via the
    # `_extra_top_level` channel so the on-disk layout preserves the
    # custom keys (calibration_inputs_used, parameters, data, etc.).
    for k, v in out.items():
        builder._extra_top_level[k] = v

    saved = builder.save()
    print(f"Wrote {saved.name}")
    print(f"  E_0 full       = {mp.nstr(e0_full, 8)} MeV  (derived, CAL-1 + CAL-2 only)")
    print(f"  E_0 calibrated = {mp.nstr(e0_cal, 8)} MeV  (CODATA Q_β / |Δ(net)|)")
    print(f"  Q_β predicted (single-wrap symbolic) = {mp.nstr(q_pred, 8)} MeV")
    print(f"  Q_β CODATA                            = {mp.nstr(q_codata, 8)} MeV")
    print(f"  err                                   = {float((q_pred - q_codata) / q_codata * 100):+.4f} %  ({float((q_pred - q_codata) * 1000):+.2f} keV)")
    print(f"  Q_β typed-crossings (legacy)          = {mp.nstr(q_pred_tc, 8)} MeV ({float((q_pred_tc - q_codata)/q_codata*100):+.4f}%)")
    print(f"  improvement single-wrap vs typed       = {float(abs(q_pred_tc - q_codata) / abs(q_pred - q_codata)):.2f}x")
    print(f"  Observable Q (typed-cross basis, ℓ ≥ 2) = {mp.nstr(q_obs, 8)} MeV ({float(q_obs / q_pred_tc) * 100:.2f}% of typed-cross)")
    all_passed = all(a.passed for a in builder.assertions)
    print(f"  All assertions passed: {all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
