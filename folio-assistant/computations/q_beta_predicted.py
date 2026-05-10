#!/usr/bin/env python3
# polynomial_q_not_applicable: assembly script; consumes upstream
# β-decay-energy-scale witness + derived_masses module.
"""Emit the FULL-chain Q_β prediction witness.

Per owner directive 2026-05-10: "do not use LO -- use full. look at
discussion on observable vs nonobservable energy in case of beta decay."

This script produces `q-beta-predicted.witness.json` recording:

  * E_0 from the FULL chain: m_e / (q_0 (q_0 - 1)) ≈ 4.186 MeV
    — derived from CAL-1 m_e + CAL-2 q_0 only; CAL-3 Q_β is the
    OUTPUT, not an input.
  * Q_β predicted = |Δ(net)| · E_0 ≈ 0.788 MeV
    — vs CODATA 0.782 MeV (0.75% framework prediction).
  * Observable / virtual decomposition (ℓ ≥ 2 vs ℓ < 2):
    Q_obs ≈ 0.461 MeV (58.46% — Hopf links + trefoil)
    Q_virt ≈ 0.327 MeV (41.54% — γ + σ_0 + σ_1)

References:
  * `prop:beta-decay-energy-scale`
    (content/quantum-observable-universe/particle-interactions/
     beta-decay-energy-scale.md)
  * `prop:meson-to-proton-via-borromean`
    (content/quantum-observable-universe/descartes-universe/
     meson-to-proton-via-borromean.md)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import derived_masses as dm  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402

OUT = HERE / "q-beta-predicted.witness.json"


def main() -> int:
    mp.mp.dps = 50

    t_start = time.time()
    summary = dm.derivation_summary()
    duration_ms = int((time.time() - t_start) * 1000)

    e0_full = dm.e_0_full_mev()
    e0_cal = dm.e_0_calibrated_mev()
    q_pred = dm.q_beta_predicted_mev()
    q_obs = dm.q_beta_observable_mev()
    q_virt = dm.q_beta_virtual_mev()
    q_codata = mp.mpf(str(Q_BETA_MEV))

    # Sanity: q_obs + q_virt should equal q_pred within rounding.
    sum_check = q_obs + q_virt
    sum_residual_mev = abs(sum_check - q_pred)

    out = {
        "engine": "mpmath",
        "engineVersion": "mpmath 1.3.0",
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
        "computation": "q-beta-predicted",
        "scriptFile": "q_beta_predicted.py",
        "description": (
            "FULL-chain Q_β prediction per prop:beta-decay-energy-scale. "
            "E_0 derived from CAL-1 m_e + CAL-2 q_0 only (no CAL-3 input); "
            "Q_β predicted via |Δ(net)| · E_0; observable/virtual split by "
            "Coxeter length ℓ ≥ 2 (Hopf links + trefoil) vs ℓ < 2 (γ + σ_0 "
            "+ σ_1). Owner directive 2026-05-10: do not use LO; use FULL."
        ),
        "contentBlock": "prop:beta-decay-energy-scale",
        "auditOnly": (
            "docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md"
        ),
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
                "Q_beta_pred_formula": "|Δ(net)| · E_0_full",
                "Q_beta_codata_MeV": str(q_codata),
                "err_pct": str((q_pred - q_codata) / q_codata * 100),
                "err_ppb": float((q_pred - q_codata) / q_codata * 1e9),
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
        "assertions": [
            {
                "name": "Q_beta_pred_within_1_pct_of_codata",
                "computed": float(abs(q_pred - q_codata) / q_codata),
                "expected": 0.01,
                "passed": float(abs(q_pred - q_codata) / q_codata) < 0.01,
                "tolerance": 0.01,
            },
            {
                "name": "obs_plus_virt_equals_pred",
                "computed": float(sum_residual_mev),
                "expected": 1e-15,
                "passed": float(sum_residual_mev) < 1e-12,
                "tolerance": 1e-12,
            },
            {
                "name": "observable_fraction_around_0.585",
                "computed": float(q_obs / q_pred),
                "expected": 0.585,
                "passed": abs(float(q_obs / q_pred) - 0.585) < 0.01,
                "tolerance": 0.01,
            },
        ],
        "allPassed": True,
        "durationMs": duration_ms,
        "summary_for_humans": summary,
    }
    out["allPassed"] = all(a["passed"] for a in out["assertions"])

    OUT.write_text(json.dumps(out, indent=2))
    print(f"Wrote {OUT.name}")
    print(f"  E_0 full       = {mp.nstr(e0_full, 8)} MeV  (derived, CAL-1 + CAL-2 only)")
    print(f"  E_0 calibrated = {mp.nstr(e0_cal, 8)} MeV  (CODATA Q_β / |Δ(net)|)")
    print(f"  Q_β predicted  = {mp.nstr(q_pred, 8)} MeV  (vs CODATA {mp.nstr(q_codata, 8)})")
    print(f"  err            = {float((q_pred - q_codata) / q_codata * 100):+.4f} %")
    print(f"  Q_obs (ℓ ≥ 2)  = {mp.nstr(q_obs, 8)} MeV  ({float(q_obs / q_pred) * 100:.2f} %)")
    print(f"  Q_virt (ℓ < 2) = {mp.nstr(q_virt, 8)} MeV  ({float(q_virt / q_pred) * 100:.2f} %)")
    print(f"  All assertions passed: {out['allPassed']}")
    return 0 if out["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
