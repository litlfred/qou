#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical verification of an algebraic
# bridge identity; no symbolic-q output.
"""Numerical witness for `prop:q-beta-spectral-bridge`.

Verifies, at 50-dps mpmath precision, the leading-order bridge
identity between Form A (NF-counit basis) and Form B (transfer-
matrix eigenfunction basis) for the free-neutron Q-value:

    Form A:  |Δ(net)| = |h (2 - h) / 2|        where h = q − q⁻¹
    Form B:  ln(1 + z h)                       where z = 1/(√q + 1/√q)
    Bridge:  Form A / Form B = 1/z + (z-1) h / (2 z) + O(h²)

The witness:
  1. Loads CAL-2 q_0 from `q-pinning-50-digit.witness.json`.
  2. Computes h, z, Form A, Form B at 50 dps.
  3. Computes the predicted leading-order bridge ratio
     `1/z + (z-1) h / (2 z)`.
  4. Computes the actual ratio `Form A / Form B`.
  5. Asserts |predicted - actual| ≤ h² (the O(h²) Taylor remainder).
  6. Converts both presentations to MeV via E_0 = m_e / (q (q-1)),
     verifying that Q_β^A and Q_β^B agree to within the same O(h²)
     tolerance after the 1/z normalization is applied to Form B.

This script is **diagnostic-only**: it does not feed any predictor;
it ratifies the algebraic identity that links the two existing
predictors (`q_beta_predicted_mev` in `derived_masses.py` for
Form A; the transfer-matrix witness data for Form B).

Output: `q-beta-spectral-bridge.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

# Set 50 dps BEFORE importing modules that build mp.mpf constants at
# import time (codata_constants does this). Otherwise constants are
# parsed at the default 15 dps and the witness JSON shows
# binary-rounding artifacts at high precision (per Copilot review on
# PR #639).
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import M_E_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

Q_PINNING = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)


def _load_q_0() -> mp.mpf:
    """CAL-2 q_0 from the canonical pinning witness."""
    with Q_PINNING.open() as fh:
        return mp.mpf(json.load(fh)["derived_50_digit"]["q"])


def main() -> int:
    # dps already set at module import (see top of file).
    w = WitnessBuilder("q-beta-spectral-bridge", engine="mpmath")

    q = _load_q_0()
    h = q - 1 / q
    sqrt_q = mp.sqrt(q)
    z = 1 / (sqrt_q + 1 / sqrt_q)

    # Form A: |Δ(net)| = |h (2 - h) / 2|
    form_a = abs(h * (2 - h) / 2)

    # Form B (algebraic leading-order, equivalent to ln(V_pp/V_nn)
    # to O(h²) after the eigenfunction-basis change).
    form_b = mp.log(1 + z * h)

    # Predicted bridge at leading order: 1/z + (z - 1) h / (2 z)
    predicted = 1 / z + (z - 1) * h / (2 * z)
    actual = form_a / form_b
    bridge_residual = abs(predicted - actual)
    h_squared = h * h

    # Convert both to MeV via the same E_0 derivation
    # (derived from CAL-1 m_e + CAL-2 q_0; no CAL-3 input).
    m_e = M_E_MEV
    e_0 = m_e / (q * (q - 1))
    q_beta_form_a_mev = form_a * e_0
    q_beta_form_b_mev = form_b * e_0 / z  # 1/z normalization
    q_beta_agreement_mev = abs(q_beta_form_a_mev - q_beta_form_b_mev)

    print("=" * 78)
    print("Q_β SPECTRAL BRIDGE — 50 dps numerical witness")
    print("=" * 78)
    print(f"  q_0           = {mp.nstr(q, 16)}")
    print(f"  h = q - q⁻¹   = {mp.nstr(h, 16)}")
    print(f"  z (Markov)    = {mp.nstr(z, 16)}")
    print(f"  h²            = {mp.nstr(h_squared, 16)}")
    print()
    print(f"  Form A   |Δ(net)|             = {mp.nstr(form_a, 16)}")
    print(f"  Form B   ln(1 + z·h)          = {mp.nstr(form_b, 16)}")
    print(f"  predicted 1/z + (z-1)h/(2z)   = {mp.nstr(predicted, 16)}")
    print(f"  actual    Form A / Form B     = {mp.nstr(actual, 16)}")
    print(f"  |predicted − actual|          = {mp.nstr(bridge_residual, 6)}")
    print(f"  O(h²) tolerance               = {mp.nstr(h_squared, 6)}")
    print()
    print(f"  Q_β^A (MeV)  |Δ(net)|·E_0     = {mp.nstr(q_beta_form_a_mev, 12)}")
    print(f"  Q_β^B (MeV)  ln(1+zh)·E_0/z   = {mp.nstr(q_beta_form_b_mev, 12)}")
    print(f"  |Q_β^A − Q_β^B| (MeV)         = {mp.nstr(q_beta_agreement_mev, 6)}")

    w.set_content_block("prop:q-beta-spectral-bridge")
    w.set_description(
        "Numerical witness for the leading-order bridge identity "
        "Form A / Form B = 1/z + (z-1) h / (2 z) + O(h²) of "
        "prop:q-beta-spectral-bridge. Form A is the NF-counit |Δ(net)| "
        "= |h(2-h)/2|; Form B is the eigenfunction-basis log-ratio "
        "ln(V_pp/V_nn), which at single wrap reduces to ln(1 + z h) "
        "via the Markov-traced volume identity in "
        "prop:beta-decay-transfer-matrix. Both forms map onto MeV via "
        "the same E_0 = m_e / (q (q-1)) derived from CAL-1 + CAL-2 only; "
        "Form B carries an additional 1/z Markov-Jones normalization "
        "(NOT a calibration knob). The residual |predicted - actual| "
        "is bounded by h² (the Taylor O(h²) remainder)."
    )
    w.add_parameter("q_0_50dps", str(q))
    w.add_parameter("m_e_MeV", str(m_e))
    w.add_data("h", str(h))
    w.add_data("z_markov_jones", str(z))
    w.add_data("h_squared_tolerance", str(h_squared))
    w.add_data("form_a_delta_net", str(form_a))
    w.add_data("form_b_log_one_plus_zh", str(form_b))
    w.add_data("predicted_bridge_ratio", str(predicted))
    w.add_data("actual_bridge_ratio", str(actual))
    w.add_data("bridge_residual", str(bridge_residual))
    w.add_data("E_0_MeV", str(e_0))
    w.add_data("Q_beta_form_a_MeV", str(q_beta_form_a_mev))
    w.add_data("Q_beta_form_b_MeV", str(q_beta_form_b_mev))
    w.add_data("Q_beta_agreement_MeV", str(q_beta_agreement_mev))
    w.add_assertion(
        "bridge_residual_within_O_h_squared",
        computed=float(bridge_residual),
        expected=0.0,
        tolerance=float(h_squared),
    )
    w.add_assertion(
        "Q_beta_form_a_form_b_agree_within_O_h_squared_MeV",
        computed=float(q_beta_agreement_mev),
        expected=0.0,
        # h² · E_0 is the propagated MeV tolerance.
        tolerance=float(h_squared * e_0),
    )
    out = w.save()
    print(f"\nWrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
