#!/usr/bin/env python3
"""Generator for the CAL-3 calibration witness (cal-3-q-beta.witness.json).

Replaces the prior hand-authored witness with a script-generated one
sourced from `codata_2022_source.Q_BETA_MEV_AME`.  Per the 2026-05-23
CODATA precision-pipeline audit recommendation #4: "Replace
cal-3-q-beta.witness.json storage with a generator from
codata_2022_source.py — eliminates the chance of the witness drifting
from CODATA when an edition update lands."

The witness structure and downstream-consumer list are preserved
verbatim from the prior hand-authored version.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from codata_2022_source import (  # noqa: E402
    Q_BETA_MEV_AME,
    Q_BETA_MEV_AME_ERR,
)


def main() -> int:
    # engine must be a witness-schema enum value; the CODATA-2022
    # provenance is recorded as a parameter below.
    w = WitnessBuilder("cal-3-q-beta", engine="python")
    w.add_parameter("source", "CODATA 2022 (Q_beta(n) primary definition)")
    w.set_description(
        "CAL-3 calibration input: free-neutron β-decay Q-value Q_β(n). "
        "Per the QOU three-calibration discipline "
        "(folio/quantum-observable-universe/braids-and-knots/"
        "three-calibration-inputs.md), Q_β(n) is one of exactly three "
        "external inputs to the framework — alongside m_e (CAL-1) and "
        "m_μ/m_e (CAL-2) — used to fix the hadronic energy scale E_0 "
        "via E_0 = Q_β(n) / |Δ(net)|, where Δ(net) = h(h-2)/2 is the "
        "symbolic NF difference between neutron and proton braids. "
        "This witness exists so codata_constants.py loads the CAL-3 "
        "value from a source-of-truth JSON instead of hardcoding it. "
        "Q_β here is the PRIMARY DEFINITION of the input; it must agree "
        "(within combined CODATA σ) with the algebraic identity "
        "m_n - m_p - m_e computed from the validation witness, but that "
        "identity is a CONSISTENCY CHECK, not the definition."
    )
    w.set_content_block("def:three-calibration-discipline")
    w.set_audit_only("docs/audits/2026-05-10-1ppb-workplan-update.md")

    w.add_parameter("calibration_id", "CAL-3")
    w.add_parameter(
        "role",
        "Hadronic energy scale E_0 via E_0 = Q_β(n) / |Δ(net)|",
    )
    w.add_parameter(
        "data_source",
        "PDG 2024 free-neutron β-decay Q-value (n → p + e⁻ + ν̄_e), "
        "consistent with AME 2020 mass-difference computation. "
        "Sourced from codata_2022_source.Q_BETA_MEV_AME.",
    )
    w.add_parameter(
        "uncertainty_convention",
        "one-sigma combined standard uncertainty, k=1",
    )
    w.add_parameter("units", "MeV")

    w.add_data("Q_beta_n_MeV", str(Q_BETA_MEV_AME))
    w.add_data("Q_beta_n_MeV_err", str(Q_BETA_MEV_AME_ERR))
    w.add_data(
        "Q_beta_n_MeV_quoted",
        "0.78233341(61) MeV (PDG 2024 / AME 2020 cross-check)",
    )
    w.add_data("decay_channel", "n → p + e⁻ + ν̄_e")
    w.add_data("downstream_consumers", [
        "codata_constants.Q_BETA_MEV",
        "E_0_MeV anchor in canonical-mass-table.witness.json",
        "free_neutron_decay.py NF-coefficient extraction",
        "c_alpha_from_Q_beta_trace.py β-chain α-cluster derivation",
        "neutron-gap-probes-round3.witness.json 3-input mass split: "
        "m_n_pred = m_p_pred + Q_β + m_e",
    ])

    out = w.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
