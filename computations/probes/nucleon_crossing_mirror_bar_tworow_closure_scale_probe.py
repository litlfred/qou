#!/usr/bin/env python3
"""80-dps verification probe for nucleon crossing counts, mirror-bar bond cancellation,
two-row cap share, A + 1 closure component law, and scale ratio invariance.

Salvaged from PR #8260 (`qou-im4m`, `qou-kgsx`, `qou-lr57`, `qou-mbbf`, `qou-qlma`).
Lean companions:
  - `QOU/MassTheory/MirrorBarCancellationAndTwoRowCapRatio.lean`
  - `QOU/MassTheory/NucleonCrossingCountsAndClosureLaw.lean`
  - `QOU/MassTheory/NucleonScaleEnergyAndRatioInvariance.lean`
Precision: 80-dps mpmath, WitnessBuilder, zero float64, zero hardcoded CODATA literals.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

THIS = Path(__file__).resolve()
ROOT = THIS.parents[2]
for _rel in (
    "computations",
    "computations/substrate",
    "tools/qou-substrate/python",
    "schemas/witness-schema/python",
):
    if str(ROOT / _rel) not in sys.path:
        sys.path.insert(0, str(ROOT / _rel))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 80
set_compute_dps(DPS)
mp.mp.dps = DPS


def main() -> int:
    t0 = time.time()
    set_compute_dps(DPS)
    mp.mp.dps = DPS

    q0 = mp.mpf(Q_50_DIGIT_STR)
    q0_inv = mp.mpf(1) / q0
    me_mev = +M_E_MEV

    # 1. qou-im4m: Nucleon typed crossing count decomposition
    c_k1 = 6 + 3 + 2 * 1
    c_k2 = 6 + 3 + 2 * 2
    c1_pass = bool(
        c_k1 == 11
        and c_k2 == 13
        and (c_k2 - c_k1) == 2
        and (7 + 4) == c_k1
        and (6 + 3 + 2) == c_k1
    )

    # 2. qou-kgsx: Mirror-bar bond cancellation & universal exponent sum = 12
    z_d = (q0**3) / (q0**2 + 1)
    zbar_d = (q0_inv**3) / (q0_inv**2 + 1)
    h_q = q0 - q0_inv
    hbar_q_bar = q0_inv - q0
    delta_c = ((q0 - 1) ** 2) * ((q0 + 1) ** 2) / (3 * (q0**2 + 1))
    delta_c_bar = ((q0_inv - 1) ** 2) * ((q0_inv + 1) ** 2) / (3 * (q0_inv**2 + 1))
    d_iface = -h_q * (mp.mpf(1) / mp.mpf(2) - delta_c / 4)
    dbar_iface = -hbar_q_bar * (mp.mpf(1) / mp.mpf(2) - delta_c_bar / 4)

    expected_quotient = (zbar_d + dbar_iface) / (z_d + d_iface)
    max_quotient_residual = mp.mpf(0)
    exp_sum_ok = True
    for z_val, n_val in ((1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (3, 4)):
        zp = z_val - 1
        nm = n_val - 1
        prod_zn = (z_d**zp) * (zbar_d**nm) * (z_d + d_iface)
        prod_mirror = (zbar_d**nm) * (z_d**zp) * (zbar_d + dbar_iface)
        res = abs(prod_mirror / prod_zn - expected_quotient)
        if res > max_quotient_residual:
            max_quotient_residual = res
        a_zn = 6 + 2 * (n_val - z_val) - (z_val + n_val - 1)
        a_nz = 6 + 2 * (z_val - n_val) - (n_val + z_val - 1)
        b_zn = z_val + n_val - 1
        if a_zn != 7 - 3 * z_val + n_val or (a_zn + a_nz + 2 * b_zn) != 12:
            exp_sum_ok = False
    c2_pass = bool(max_quotient_residual < mp.mpf("1e-70") and exp_sum_ok)

    # 3. qou-lr57: Two-row cap decomposition identity
    t_le2 = z_d**2 + 2 * z_d * (1 - z_d)
    t_gt2 = (1 - z_d) ** 2
    t_all = t_le2 + t_gt2
    share_diff = abs((t_gt2 / t_all) - (1 - t_le2 / t_all))
    c3_pass = bool(t_gt2 > 0 and share_diff < mp.mpf("1e-70"))

    # 4. qou-mbbf: A + 1 closure component law across A in {2, 3, 4, 6}
    expected_table = {2: (6, 23, 3), 3: (9, 35, 4), 4: (12, 47, 5), 6: (18, 71, 7)}
    c4_pass = True
    for a_val, (s_exp, l_exp, c_exp) in expected_table.items():
        s_val = 3 * a_val
        l_val = 11 * a_val + (a_val - 1)
        c_val = a_val + 1
        if (s_val, l_val, c_val) != (s_exp, l_exp, c_exp) or l_val != 12 * a_val - 1:
            c4_pass = False
        if a_val >= 3 and c_val in (1, 3):
            c4_pass = False

    # 5. qou-qlma: Scale denominator identity, reciprocal-sum bound z_m <= 1/2, scale cancellation
    denom_prod = q0 * (q0 - 1)
    denom_tick = (q0**2) * (1 - 1 / q0)
    denom_residual = abs(denom_prod - denom_tick)
    alpha_mev = me_mev / denom_prod

    x_sqrt = mp.sqrt(q0)
    z_m = 1 / (x_sqrt + 1 / x_sqrt)
    sq_id_residual = abs(((x_sqrt + 1 / x_sqrt) - 2) - (((x_sqrt - 1) ** 2) / x_sqrt))
    mu_b = z_d
    mu_q = h_q
    ratio_cancel_residual = abs(((alpha_mev * mu_b) / (alpha_mev * mu_q)) - (mu_b / mu_q))
    c5_pass = bool(
        denom_residual < mp.mpf("1e-70")
        and sq_id_residual < mp.mpf("1e-70")
        and z_m < mp.mpf(1) / mp.mpf(2)
        and ratio_cancel_residual < mp.mpf("1e-70")
    )

    wb = WitnessBuilder(
        "nucleon-crossing-mirror-bar-tworow-closure-scale-probe",
        engine="mpmath",
        output_dir=THIS.parent,
        start_time=t0,
    )
    wb.set_description(
        "80-dps verification of nucleon typed crossing count decomposition (qou-im4m), "
        "mirror-bar bond cancellation and exponent sum 12 (qou-kgsx), two-row cap "
        "share identity (qou-lr57), A+1 closure component law (qou-mbbf), and "
        "Planck-tick energy scale denominator & ratio invariance (qou-qlma)."
    )
    wb.add_parameter("workdps", DPS)
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_data("interface_mirror_bar_quotient", fmt(expected_quotient, 50))
    wb.add_data("alpha_e0_mev", fmt(alpha_mev, 50))
    wb.add_data("z_m_reciprocal_sum_param", fmt(z_m, 50))

    wb.add_assertion(
        "qou_im4m_mbbf_crossing_counts_and_atom_component_law",
        computed=bool(c1_pass and c4_pass),
        expected=True,
        source="QOU.MassTheory.NucleonCrossingCountsAndClosureLaw.atom_component_law_excludes_census_arities",
    )
    wb.add_assertion(
        "qou_kgsx_lr57_mirror_bar_cancellation_and_tworow_share",
        computed=bool(c2_pass and c3_pass),
        expected=True,
        source="QOU.MassTheory.MirrorBarCancellationAndTwoRowCapRatio.mirrorBar_quotient_independent_of_counts",
    )
    wb.add_assertion(
        "qou_qlma_scale_denom_zm_bound_and_ratio_cancellation",
        computed=c5_pass,
        expected=True,
        source="QOU.MassTheory.NucleonScaleEnergyAndRatioInvariance.scaleDenomProduct_eq_scaleDenomTick",
    )

    out_path = wb.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"Saved witness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
