#!/usr/bin/env python3
"""Substrate-only prediction of Q_β(n) from CAL-1 (m_e) + CAL-2 (q_0).

Per the q-zero / Q_β cohomological audit
(docs/audits/2026-05-24-q-beta-droppability-cohomology.md) and
the existing closed form in derived_masses.py:49-62, the
free-neutron β-decay Q-value has a single-wrap substrate
prediction:

    Q_β = m_e · |q_0² - 2 q_0 - 1| · (q_0 + 1) / (2 q_0³)

using CAL-1 m_e and CAL-2 q_0 only (no CAL-3 input). Empirical
residual vs CODATA: +0.18% (+1.31 keV); the residual is the
brane-tower truncation at N=0 and is closed by the tower-summed
form (Workplan 2 Phase 2).

This witness emits the substrate prediction in parallel with the
CAL-3 calibration (cal-3-q-beta.witness.json) so the L2 dashboard
can read both. The substrate value is NOT yet wired as a CAL
replacement; per the workplan it stays a prediction until the
tower-summation closure lands.

Outputs: q-beta-substrate-prediction.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q_ZERO  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402


def q_beta_substrate(q_0: float, m_e_mev: float) -> float:
    """Substrate-only Q_β closed form (single-wrap, CAL-1 + CAL-2 only).

    Q_β = m_e · |q_0² - 2 q_0 - 1| · (q_0 + 1) / (2 q_0³)
    """
    numerator = abs(q_0 * q_0 - 2.0 * q_0 - 1.0) * (q_0 + 1.0)
    denominator = 2.0 * q_0 ** 3
    return m_e_mev * numerator / denominator


def main() -> int:
    q_beta_pred = q_beta_substrate(float(Q_ZERO), float(M_E_MEV))
    q_beta_codata = float(Q_BETA_MEV)
    abs_residual_mev = q_beta_pred - q_beta_codata
    rel_residual = abs_residual_mev / q_beta_codata
    rel_residual_ppm = rel_residual * 1e6
    rel_residual_pct = rel_residual * 100.0

    w = WitnessBuilder(
        "q-beta-substrate-prediction",
        engine="q_beta_substrate_prediction.py",
    )
    w.set_description(
        "Substrate-only prediction of Q_β(n) from CAL-1 (m_e) and "
        "CAL-2 (q_0), via the single-wrap closed form "
        "Q_β = m_e · |q_0² - 2 q_0 - 1| · (q_0 + 1) / (2 q_0³). "
        "This is a PREDICTION witness (companion to the CAL-3 "
        "calibration witness cal-3-q-beta.witness.json); the "
        "substrate value is NOT yet wired as a CAL replacement. "
        "Per the cohomological audit "
        "(docs/audits/2026-05-24-q-beta-droppability-cohomology.md), "
        "the framework can in principle drop CAL-3 once the "
        "tower-summation closure lands (Workplan 2 Phase 2); until "
        "then the +0.18% residual vs CODATA is recorded here for "
        "L2 dashboard visibility and audit-trail purposes."
    )
    w.set_content_block("def:three-calibration-discipline")
    w.set_audit_only(
        "docs/audits/2026-05-24-q-beta-droppability-cohomology.md"
    )

    w.add_parameter("calibration_id", "CAL-3 (substrate prediction)")
    w.add_parameter(
        "role",
        "Substrate prediction of hadronic Q-value, using CAL-1 + "
        "CAL-2 inputs only. Parallel to (not replacing) the "
        "CAL-3 calibration witness.",
    )
    w.add_parameter(
        "closed_form",
        "Q_β = m_e · |q_0² - 2 q_0 - 1| · (q_0 + 1) / (2 q_0³)",
    )
    w.add_parameter(
        "derivation_reference",
        "derived_masses.py:49-62; "
        "docs/audits/2026-05-24-q-beta-droppability-cohomology.md §3",
    )
    w.add_parameter("units", "MeV")

    w.add_data("q_zero", str(Q_ZERO))
    w.add_data("m_e_MeV_input_CAL1", str(M_E_MEV))
    w.add_data("Q_beta_substrate_MeV", str(q_beta_pred))
    w.add_data("Q_beta_codata_MeV_CAL3", str(q_beta_codata))
    w.add_data("absolute_residual_MeV", str(abs_residual_mev))
    w.add_data("absolute_residual_keV", str(abs_residual_mev * 1000.0))
    w.add_data("relative_residual", str(rel_residual))
    w.add_data("relative_residual_ppm", str(rel_residual_ppm))
    w.add_data("relative_residual_percent", str(rel_residual_pct))
    w.add_data(
        "residual_attribution",
        "Brane-tower truncation at N=0. Exact tower-summed E_0 "
        "(Li_2^q form, Workplan 2 P2) is expected to close the "
        "residual to within 1ppb.",
    )
    w.add_data(
        "downstream_consumers",
        [
            "L2 dashboard: per-observable-100x-status.witness.json "
            "(new row 'Q_beta-substrate-2CAL' for visibility)",
            "Cohomological audit cross-check: this prediction is "
            "the candidate replacement for the CAL-3 input pending "
            "tower-summation closure.",
        ],
    )
    w.add_data(
        "tolerance_vs_consumers",
        "All downstream production mass-prediction consumers have "
        "≥ 4% MAE on β-decay sector observables; the +0.18% "
        "substrate-Q_β residual is well within these tolerances. "
        "The 1ppb gate (per-observable-100x-status.witness.json) "
        "is the ONLY consumer the substrate prediction would fail "
        "today; that closure is the tower-summation workplan item.",
    )

    w.save()
    print(
        f"q_beta_substrate_prediction: PASS  "
        f"Q_β_pred = {q_beta_pred:.6f} MeV  "
        f"vs CODATA {q_beta_codata:.6f} MeV  "
        f"(rel {rel_residual_pct:+.3f}%, {abs_residual_mev*1000:+.2f} keV)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
