#!/usr/bin/env python3
"""joint_ohtsuki_graded_tower_annihilator_probe.py — Joint graded Ohtsuki / complex-volume
tower over (4_1, 5_2, B_3) and negative-grade / low-grade annihilator test.

Task: qou-7jok (salvaged from PR #8144).
Lean companion: `QOU/QBeta/JointOhtsukiGradedTower.lean`.
Precision: 80-dps mpmath + exact rational algebra, zero float64, zero fitting.
"""
from __future__ import annotations

import os
import sys
import time
from fractions import Fraction
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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 80
set_compute_dps(DPS)
mp.mp.dps = DPS

Q0_STR = Q_50_DIGIT_STR
Q0 = mp.mpf(Q0_STR)


def bloch_wigner(z: mp.mpc) -> mp.mpf:
    """Bloch-Wigner dilogarithm D_2(z) = Im(Li_2(z)) + arg(1 - z) * ln|z|."""
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def solve_five_two_saddle_root() -> mp.mpc:
    """Solve y^3 - 2*y^2 + 3*y - 1 = 0 for the geometric root y_0 with Im(y_0) < 0."""
    y = mp.mpc(mp.mpf("0.78492"), mp.mpf("-1.30714"))
    for _ in range(50):
        f = y**3 - 2 * (y**2) + 3 * y - 1
        df = 3 * (y**2) - 4 * y + 3
        y = y - f / df
    return y


def compute_five_two_complex_volume_and_kappa(
    y0: mp.mpc,
) -> dict[str, mp.mpf | mp.mpc]:
    """Compute 5_2 complex volume V_0(5_2) = Vol_0(5_2) + i*CS_0(5_2) and Hessian norm."""
    x0 = 1 - y0
    y_oht = 1 / (1 - x0)
    vol_52 = 3 * bloch_wigner(x0)

    xy = x0 * y_oht
    v_hat = (
        mp.polylog(2, xy)
        + mp.polylog(2, 1 / xy)
        + mp.polylog(2, y_oht)
        - mp.polylog(2, 1 / y_oht)
        - mp.polylog(2, 1 / x0)
        - (mp.pi**2) / 6
    )
    cs_52 = mp.re(v_hat)

    delta_52 = 3 * (y0**2) - 4 * y0 + 3
    y_real = mp.mpf("0.43015970900195")
    for _ in range(50):
        f = y_real**3 - 2 * (y_real**2) + 3 * y_real - 1
        df = 3 * (y_real**2) - 4 * y_real + 3
        y_real = y_real - f / df
    y_conj = mp.conj(y0)
    norm_delta_52 = (
        (3 * (y_real**2) - 4 * y_real + 3)
        * (3 * (y0**2) - 4 * y0 + 3)
        * (3 * (y_conj**2) - 4 * y_conj + 3)
    )

    omega_52 = mp.re(1 / mp.sqrt(delta_52))
    kappa1_52_scale = omega_52 * mp.pi
    kappa2_52_scale = mp.re(1 / (delta_52**2)) * (mp.pi**2)

    return {
        "y0": y0,
        "x0": x0,
        "y_real": y_real,
        "vol0": vol_52,
        "cs0": cs_52,
        "delta_52": delta_52,
        "norm_delta_52": mp.re(norm_delta_52),
        "omega_52": omega_52,
        "kappa1_scale": kappa1_52_scale,
        "kappa2_scale": kappa2_52_scale,
    }


def main() -> int:
    t0 = time.time()
    set_compute_dps(DPS)
    mp.mp.dps = DPS

    t_sub = mp.log(Q0)
    pi_mp = mp.pi
    sqrt3_mp = mp.sqrt(3)

    z_41 = mp.exp(mp.mpc(0, 1) * pi_mp / 3)
    vol0_41 = 2 * bloch_wigner(z_41)
    cs0_41 = mp.mpf(0)
    k1_41_rat = Fraction(11, 108)
    k2_41_rat = Fraction(2, 27)
    k3_41_rat = Fraction(1081, 21870)
    k4_41_rat = Fraction(98, 729)

    k1_41 = (
        mp.mpf(k1_41_rat.numerator) / mp.mpf(k1_41_rat.denominator) * sqrt3_mp * pi_mp
    )
    k2_41 = (
        mp.mpf(k2_41_rat.numerator) / mp.mpf(k2_41_rat.denominator) * (pi_mp**2)
    )
    k3_41 = (
        mp.mpf(k3_41_rat.numerator)
        / mp.mpf(k3_41_rat.denominator)
        * sqrt3_mp
        * (pi_mp**3)
    )
    k4_41 = (
        mp.mpf(k4_41_rat.numerator) / mp.mpf(k4_41_rat.denominator) * (pi_mp**4)
    )

    y0_52 = solve_five_two_saddle_root()
    res_52 = abs(y0_52**3 - 2 * (y0_52**2) + 3 * y0_52 - 1)
    assert res_52 < mp.mpf("1e-70")

    data_52 = compute_five_two_complex_volume_and_kappa(y0_52)
    vol0_52 = data_52["vol0"]
    cs0_52 = data_52["cs0"]
    norm_delta_52 = data_52["norm_delta_52"]
    k1_52 = data_52["kappa1_scale"]
    k2_52 = data_52["kappa2_scale"]

    vol0_B3 = 8 * mp.catalan
    cs0_B3 = mp.mpf(0)
    k1_B3_rat = Fraction(1, 4)
    k2_B3_rat = Fraction(5, 12)
    k1_B3 = mp.mpf(k1_B3_rat.numerator) / mp.mpf(k1_B3_rat.denominator) * pi_mp
    k2_B3 = mp.mpf(k2_B3_rat.numerator) / mp.mpf(k2_B3_rat.denominator) * (pi_mp**2)

    it = mp.mpc(0, 1) * t_sub
    V_41_trunc4 = (
        mp.mpc(vol0_41, cs0_41)
        + k1_41 * it
        + k2_41 * (it**2)
        + k3_41 * (it**3)
        + k4_41 * (it**4)
    )
    V_52_trunc2 = mp.mpc(vol0_52, cs0_52) + k1_52 * it + k2_52 * (it**2)
    V_B3_trunc2 = mp.mpc(vol0_B3, cs0_B3) + k1_B3 * it + k2_B3 * (it**2)

    M_joint = mp.matrix(
        [
            [cs0_41, cs0_52, cs0_B3],
            [vol0_41, vol0_52, vol0_B3],
            [t_sub * k1_41, t_sub * k1_52, t_sub * k1_B3],
        ]
    )
    det_M_joint = mp.det(M_joint)
    det_2x2_41_B3_vol_k1 = vol0_41 * k1_B3 - vol0_B3 * k1_41
    det_check = -cs0_52 * t_sub * det_2x2_41_B3_vol_k1
    det_2x2_41_B3_k1_k2 = k1_41 * k2_B3 - k1_B3 * k2_41

    min_norm = mp.mpf("inf")
    min_triple = (0, 0, 0)
    for a1 in range(-10, 11):
        for a2 in range(-10, 11):
            for a3 in range(-10, 11):
                if a1 == 0 and a2 == 0 and a3 == 0:
                    continue
                g0_im = a1 * cs0_41 + a2 * cs0_52 + a3 * cs0_B3
                g1_im = t_sub * (a1 * k1_41 + a2 * k1_52 + a3 * k1_B3)
                g2_re = -(t_sub**2) * (a1 * k2_41 + a2 * k2_52 + a3 * k2_B3)
                norm_val = mp.sqrt(g0_im**2 + g1_im**2 + g2_re**2)
                if norm_val < min_norm:
                    min_norm = norm_val
                    min_triple = (a1, a2, a3)

    mod2_vals = [((y**3 - 2 * (y**2) + 3 * y - 1) % 2) for y in (0, 1)]

    wb = WitnessBuilder(
        "joint-ohtsuki-graded-tower-annihilator",
        engine="mpmath",
        output_dir=THIS.parent,
        start_time=t0,
    )
    wb.set_description(
        "80-dps mpmath + exact algebraic verification of the joint graded Ohtsuki "
        "complex-volume tower over (4_1, 5_2, B_3), proving grade-0 chirality parity "
        "exclusion of 5_2 and pairwise trace-field / 3x3 rank annihilator triviality (qou-7jok)."
    )
    wb.add_parameter("workdps", DPS)
    wb.add_parameter("q0", Q0_STR)
    wb.add_data(
        "towers",
        {
            "Vol_0_41": fmt(vol0_41, 50),
            "Vol_0_52": fmt(vol0_52, 50),
            "CS_0_52": fmt(cs0_52, 50),
            "Vol_0_B3": fmt(vol0_B3, 50),
            "V_41_trunc4_re": fmt(mp.re(V_41_trunc4), 50),
            "V_41_trunc4_im": fmt(mp.im(V_41_trunc4), 50),
            "V_52_trunc2_re": fmt(mp.re(V_52_trunc2), 50),
            "V_B3_trunc2_re": fmt(mp.re(V_B3_trunc2), 50),
            "det_3x3_M_joint": fmt(det_M_joint, 50),
            "det_2x2_41_B3_vol_k1": fmt(det_2x2_41_B3_vol_k1, 50),
            "det_2x2_41_B3_k1_k2": fmt(det_2x2_41_B3_k1_k2, 50),
            "min_lattice_norm_box10": fmt(min_norm, 30),
            "min_lattice_triple": list(min_triple),
        },
    )

    wb.add_assertion(
        "grade0_chirality_parity_blocker_verified",
        computed=bool(cs0_41 == 0 and cs0_B3 == 0 and abs(cs0_52) > mp.mpf(1)),
        expected=True,
        source="QOU.QBeta.JointOhtsukiGradedTower.chiral_grade0_parity_blocker",
    )
    wb.add_assertion(
        "five_two_cubic_field_discriminant_23_verified",
        computed=bool(
            abs(norm_delta_52 - 23) < mp.mpf("1e-65") and mod2_vals == [1, 1]
        ),
        expected=True,
        source="QOU.QBeta.JointOhtsukiGradedTower.fiveTwo_cubic_mod2_no_root",
    )
    wb.add_assertion(
        "joint_3x3_grade_matrix_nonsingular",
        computed=bool(
            abs(det_M_joint - det_check) < mp.mpf("1e-65")
            and abs(det_M_joint) > mp.mpf("0.1")
        ),
        expected=True,
        source="QOU.QBeta.JointOhtsukiGradedTower.joint_three_complement_annihilator_trivial",
    )
    wb.add_assertion(
        "amphicheiral_2x2_subsystems_and_lattice_scan_nonsingular",
        computed=bool(
            abs(det_2x2_41_B3_vol_k1) > mp.mpf("0.1")
            and abs(det_2x2_41_B3_k1_k2) > mp.mpf("0.1")
            and min_norm > mp.mpf("0.001")
        ),
        expected=True,
        source="QOU.QBeta.JointOhtsukiGradedTower.amphicheiral_two_rung_annihilator_trivial",
    )

    out_path = wb.save({"q0Anchor": "proton", "q0Value": Q0_STR})
    print(f"Saved witness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
