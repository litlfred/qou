#!/usr/bin/env python3
"""
Exact 80-dps mpmath + exact rational probe for Round 70 qou-10v9 beans:
  - qou-4e5k: Deuteron tr_M witness discrepancy (1.41e-4 relative on D vs ~7e-8 pin straddle on p, n)
  - qou-742w: M1 leading constant RHO_INF = 0.979796195657 vs 2*sqrt(6)/5 squared inequality
  - qou-9bei: He/Nu SDP saturation n=6 partition support (8 exact zeros vs 3 positive blocks) and threshold stability
  - qou-cblw: p-n interface factor colour-weighted z - h*(1/2 - delta/4) vs colour-blind z - h/2
  - qou-fv0s: Ternary sign wire format {-1, 0, +1} non-injectivity on 4 crossing kinds (R3 colour-weight loss)
"""

from fractions import Fraction
from pathlib import Path
import sys

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

mp.mp.dps = 80


def main() -> None:
    wb = WitnessBuilder(
        name="deuteron-trace-discrepancy-m1-rho-constant-sdp-zero-threshold-pn-colour-factor-and-sign-wire-loss",
        engine="mpmath",
    )
    wb.description = (
        "Exact 80-dps mpmath and Fraction verification for qou-4e5k, qou-742w, "
        "qou-9bei, qou-cblw, and qou-fv0s under epic qou-10v9."
    )

    # 1. qou-4e5k: Deuteron tr_M discrepancy vs proton/neutron pin straddle
    tr_p_a = mp.mpf("1.145759692457300869689")
    tr_p_b = mp.mpf("1.145759782287835504726")
    tr_d_a = mp.mpf("0.575172243917771870827")
    tr_d_b = mp.mpf("0.575090958682446712092")

    rel_p = abs(tr_p_b - tr_p_a) / tr_p_a
    rel_d = abs(tr_d_a - tr_d_b) / tr_d_a
    ratio_d_to_p = rel_d / rel_p

    wb.add_assertion(
        "qou_4e5k_deuteron_tr_m_discrepancy_exceeds_pin_straddle",
        f"{int(rel_d > mp.mpf('1.4e-4'))}:{int(ratio_d_to_p > mp.mpf('1800'))}",
        "1:1",
        tolerance="0",
        source="QOU.Eightfold.DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.deuteron_tr_m_discrepancy_exceeds_pin_straddle",
    )

    # 2. qou-742w: M1 leading constant RHO_INF literal vs 2*sqrt(6)/5
    rho_lit = mp.mpf("0.979796195657")
    rho_alg = mp.mpf(2) * mp.sqrt(mp.mpf(6)) / mp.mpf(5)
    sq_diff_24 = 979796195657 ** 2 - 960000000000000000000000

    wb.add_assertion(
        "qou_742w_m1_rho_inf_literal_ne_two_sqrt_six_over_five",
        f"{sq_diff_24}:{int(abs(rho_lit - rho_alg) > mp.mpf('2.9e-7'))}",
        "585023930225661649:1",
        tolerance="0",
        source="QOU.Eightfold.DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.m1_rho_inf_literal_ne_two_sqrt_six_over_five",
    )

    # 3. qou-9bei: He/Nu SDP saturation n=6 partition zero-block threshold stability
    tau_floor = mp.mpf("1e-30")
    sample_weights = [
        mp.mpf("-3.2e-53"),
        mp.mpf("-1.1e-53"),
        mp.mpf("-4.5e-54"),
        mp.mpf("0.0"),
        mp.mpf("0.0"),
        mp.mpf("0.0"),
        mp.mpf("1.8e-53"),
        mp.mpf("2.9e-53"),
        mp.mpf("0.0142"),
        mp.mpf("0.0485"),
        mp.mpf("0.1123"),
    ]
    neg_unthresholded = sum(1 for y in sample_weights if y < 0)
    neg_thresholded = sum(1 for y in sample_weights if y < -tau_floor)
    zero_residue_count = sum(1 for y in sample_weights if abs(y) <= tau_floor)

    wb.add_assertion(
        "qou_9bei_sdp_saturation_threshold_eliminates_pin_residue_false_negatives",
        f"{len(sample_weights)}:{neg_unthresholded}:{neg_thresholded}:{zero_residue_count}",
        "11:3:0:8",
        tolerance="0",
        source="QOU.Eightfold.DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.sdp_saturation_threshold_eliminates_pin_residue_false_negatives",
    )

    # 4. qou-cblw: Colour-weighted vs colour-blind p-n interface factor
    z_val = Fraction(6126880371, 10000000000)
    h_val = Fraction(2090602987, 10000000000)
    delta_val = Fraction(1, 3)
    w_canon = z_val - h_val * (Fraction(1, 2) - delta_val / Fraction(4, 1))
    w_blind = z_val - h_val / Fraction(2, 1)
    four_diff = 4 * (w_canon - w_blind)
    expected_four_diff = h_val * delta_val

    wb.add_assertion(
        "qou_cblw_pn_interface_colour_weighted_minus_blind_identity",
        str(int(four_diff == expected_four_diff and four_diff > 0)),
        "1",
        tolerance="0",
        source="QOU.Eightfold.DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.pn_interface_colour_weighted_minus_blind_identity",
    )

    # 5. qou-fv0s: Ternary sign wire format {-1, 0, +1} non-injectivity on 4 crossing kinds
    wire_map = {
        "positive": 1,
        "negative": -1,
        "averaged": 0,
        "averaged_weighted": 0,
    }
    distinct_inputs = len(wire_map)
    distinct_outputs = len(set(wire_map.values()))

    wb.add_assertion(
        "qou_fv0s_sign_wire_format_collapses_averaged_and_averaged_weighted",
        f"{distinct_inputs}:{distinct_outputs}:{int(wire_map['averaged'] == wire_map['averaged_weighted'] == 0)}",
        "4:3:1",
        tolerance="0",
        source="QOU.Eightfold.DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.sign_wire_format_collapses_averaged_and_averaged_weighted",
    )

    wb.data["deuteron_relative_discrepancy"] = mp.nstr(rel_d, 40)
    wb.data["rho_inf_vs_two_sqrt6_over_5_diff"] = mp.nstr(rho_lit - rho_alg, 40)
    wb.save()


if __name__ == "__main__":
    main()
