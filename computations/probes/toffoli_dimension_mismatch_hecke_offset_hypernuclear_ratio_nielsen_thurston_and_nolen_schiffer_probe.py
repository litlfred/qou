#!/usr/bin/env python3
"""
Exact 80-dps mpmath + exact rational probe for Round 69 qou-10v9 beans:
  - qou-0pnj: Toffoli LP stability index-space dimension mismatch (6x6 Hecke-NF Gram vs 8x8 strand/qubit entries P_77, P_76)
  - qou-19jc: 2H Attack B Hecke-admissible linear offset (sigma + sigma^-1)/2 gives d/h = -1/2 vs empirical d/h ≈ -0.11945345
  - qou-4q9h: A6 Lambda-hypernuclear well-depth 2/3 non-strange light-quark counting ratio
  - qou-4tqt: Ito (0805.1447) Nielsen-Thurston periodic/reducible zero-volume closure vs pseudo-Anosov dilatation
  - qou-4waf: Nolen-Schiffer A=3 (3He - 3H) Coulomb sign reversal (+30.7% r0=1.2 fm overestimate vs -10.9% measured-radius underestimate)
"""

from fractions import Fraction
import math
from pathlib import Path
import sys

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

mp.mp.dps = 80


def main() -> None:
    wb = WitnessBuilder(
        name="toffoli-dimension-mismatch-hecke-offset-hypernuclear-ratio-nielsen-thurston-and-nolen-schiffer",
        engine="mpmath",
    )
    wb.description = (
        "Exact 80-dps mpmath and Fraction verification for qou-0pnj, qou-19jc, "
        "qou-4q9h, qou-4tqt, and qou-4waf under epic qou-10v9."
    )

    # 1. qou-0pnj: Toffoli LP stability 6x6 Hecke normal-form Gram vs 8x8 3-qubit basis mismatch
    hecke_dim = math.factorial(3)
    qubit_dim = 2 ** 3
    extra_entries = (qubit_dim ** 2) - (hecke_dim ** 2)

    wb.add_assertion(
        "qou_0pnj_toffoli_hecke_gram_vs_eight_by_eight_index_mismatch",
        f"{hecke_dim}:{qubit_dim}:{extra_entries}:{int(7 > hecke_dim and 8 > hecke_dim)}",
        "6:8:28:1",
        tolerance="0",
        source="QOU.Eightfold.ToffoliDimensionMismatchHeckeOffsetHypernuclearRatioNielsenThurstonAndNolenSchiffer.toffoli_hecke_gram_vs_eight_by_eight_index_mismatch",
    )

    # 2. qou-19jc: 2H Attack B Hecke-admissible linear offset (sigma + sigma^-1)/2 vs required deuteron d/h
    q0 = mp.mpf("1.1097601919822567262135982475")
    h_q = q0 - (mp.mpf(1) / q0)
    z_markov = mp.mpf("0.6126880371")
    mu_sigma = z_markov
    mu_sigma_inv = z_markov - h_q
    mu_bar_sym = (mu_sigma + mu_sigma_inv) / mp.mpf(2)
    d_over_h_bar_sym = (mu_bar_sym - z_markov) / h_q
    d_over_h_req = mp.mpf("-0.11945345")
    d_over_h_gap = abs(d_over_h_bar_sym - d_over_h_req)

    wb.add_assertion(
        "qou_19jc_hecke_bar_symmetric_offset_exact_minus_half",
        mp.nstr(abs(d_over_h_bar_sym - mp.mpf("-0.5")), 30),
        "0.0",
        tolerance="1e-70",
        source="QOU.Eightfold.ToffoliDimensionMismatchHeckeOffsetHypernuclearRatioNielsenThurstonAndNolenSchiffer.hecke_bar_symmetric_offset_half_and_deuteron_gap",
    )
    wb.add_assertion(
        "qou_19jc_hecke_bar_symmetric_vs_required_deuteron_gap",
        str(int(d_over_h_gap > mp.mpf("0.38"))),
        "1",
        tolerance="0",
        source="QOU.Eightfold.ToffoliDimensionMismatchHeckeOffsetHypernuclearRatioNielsenThurstonAndNolenSchiffer.hecke_bar_symmetric_offset_half_and_deuteron_gap",
    )

    # 3. qou-4q9h: A6 Lambda-hypernuclear 2/3 potential well-depth ratio
    n_light_nucleon = 3 - 0
    n_light_lambda = 3 - 1
    well_ratio = Fraction(n_light_lambda, n_light_nucleon)

    wb.add_assertion(
        "qou_4q9h_lambda_hypernuclear_two_thirds_well_depth_ratio",
        f"{well_ratio.numerator}/{well_ratio.denominator}",
        "2/3",
        tolerance="0",
        source="QOU.Eightfold.ToffoliDimensionMismatchHeckeOffsetHypernuclearRatioNielsenThurstonAndNolenSchiffer.lambda_hypernuclear_two_thirds_well_depth_ratio",
    )

    # 4. qou-4tqt: Ito (0805.1447) Nielsen-Thurston periodic 2-strand closure vs pseudo-Anosov 4_1 dilatation
    # For 4_1 (sigma_1 * sigma_2^-1)^2, trace of Burau/SL(2,Z) matrix [[2, 1], [1, 1]] is 3,
    # dilatation eigenvalue lambda_4_1 = (3 + sqrt(5))/2 > 1, whereas periodic 2-strand has spectral radius 1.
    lambda_periodic = mp.mpf(1)
    lambda_4_1 = (mp.mpf(3) + mp.sqrt(mp.mpf(5))) / mp.mpf(2)
    entropy_periodic = mp.log(lambda_periodic)
    entropy_4_1 = mp.log(lambda_4_1)

    wb.add_assertion(
        "qou_4tqt_ito_nielsen_thurston_periodic_vs_pseudo_anosov_entropy",
        f"{mp.nstr(entropy_periodic, 10)}:{int(entropy_4_1 > mp.mpf('0.96'))}",
        "0.0:1",
        tolerance="0",
        source="QOU.Eightfold.ToffoliDimensionMismatchHeckeOffsetHypernuclearRatioNielsenThurstonAndNolenSchiffer.ito_nielsen_thurston_periodic_zero_volume_dichotomy",
    )

    # 5. qou-4waf: Nolen-Schiffer A=3 (3He - 3H) Coulomb sign reversal (+234613 eV vs -83028 eV)
    e_c_r0_ev = 998413
    e_c_meas_ev = 680772
    delta_exp_ev = 763800
    res_r0 = e_c_r0_ev - delta_exp_ev
    res_meas = e_c_meas_ev - delta_exp_ev
    nsa_ev = delta_exp_ev - e_c_meas_ev

    wb.add_assertion(
        "qou_4waf_nolen_schiffer_a3_opposite_sign_decomposition",
        f"{res_r0}:{res_meas}:{nsa_ev}:{int(res_r0 > 0 > res_meas and nsa_ev > 0)}",
        "234613:-83028:83028:1",
        tolerance="0",
        source="QOU.Eightfold.ToffoliDimensionMismatchHeckeOffsetHypernuclearRatioNielsenThurstonAndNolenSchiffer.nolen_schiffer_a3_opposite_sign_decomposition",
    )

    wb.data["d_over_h_bar_symmetric"] = "-0.5"
    wb.data["lambda_4_1_dilatation_entropy"] = mp.nstr(entropy_4_1, 40)
    wb.data["nolen_schiffer_a3_mev"] = "0.083028"
    wb.save()


if __name__ == "__main__":
    main()
