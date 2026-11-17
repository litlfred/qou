#!/usr/bin/env python3
"""80-dps mpmath probe for Round 77:
- qou-px38: QOU.MassTheory.UICGateLP.complementarySlackness_diagonal_active_forces_zero
- qou-i4pz: QOU.MassTheory.DeuteronFirstOrderCluster.secondDiff_and_cluster3_zero_of_additive
- qou-v7qj: QOU.QBeta.ECatLPDualRadical.dual_price_zero_of_diagonal_gram_cost
- qou-rpj5: QOU.AlgebraicSubstrate.squeeze_sub_of_face_separation
- qou-yez0: QOU.MassTheory.sum_const_eq_sqrt_card_mul_sum_sq
"""

from __future__ import annotations
import hashlib
import json
import pathlib
import sys
from mpmath import mp

mp.dps = 80


def check_uic_gate_diagonal_active() -> dict[str, object]:
    # Diagonal Gram G = diag(1, 1), primal x = (1, 0), dual multipliers s = (0, 2), cost t = (-1, 1)
    g_diag = [mp.mpf("1"), mp.mpf("1")]
    x_vec = [mp.mpf("1"), mp.mpf("0")]
    s_vec = [mp.mpf("0"), mp.mpf("2")]
    t_vec = [mp.mpf("-1"), mp.mpf("1")]
    cs_residuals = [abs(s_vec[i] * g_diag[i] * x_vec[i]) for i in range(2)]
    max_cs = max(cs_residuals)
    active_idx = 1
    passed = (
        max_cs < mp.mpf("10") ** (-75)
        and s_vec[active_idx] > mp.mpf("0")
        and g_diag[active_idx] != mp.mpf("0")
        and x_vec[active_idx] == mp.mpf("0")
        and t_vec[active_idx] > mp.mpf("0")
    )
    return {
        "bean": "qou-px38",
        "theorem": "QOU.MassTheory.UICGateLP.complementarySlackness_diagonal_active_forces_zero",
        "max_cs_residual": mp.nstr(max_cs, 80),
        "active_primal_coord": mp.nstr(x_vec[active_idx], 80),
        "passed": passed,
    }


def check_deuteron_first_order_additive() -> dict[str, object]:
    e0 = mp.mpf("13")
    g0 = mp.mpf("7")
    ga = mp.mpf("19")
    gb = mp.mpf("31")
    gab = g0 + (ga - g0) + (gb - g0)
    first_a = ga - g0
    first_b = gb - g0
    second_diff = gab - ga - gb + g0
    cluster3 = e0 * (ga + gb - g0 - gab)
    passed = (
        abs(second_diff) < mp.mpf("10") ** (-75)
        and abs(cluster3) < mp.mpf("10") ** (-75)
        and abs((gab - g0) - (first_a + first_b)) < mp.mpf("10") ** (-75)
    )
    return {
        "bean": "qou-i4pz",
        "theorem": "QOU.MassTheory.DeuteronFirstOrderCluster.secondDiff_and_cluster3_zero_of_additive",
        "second_diff": mp.nstr(second_diff, 80),
        "cluster3": mp.nstr(cluster3, 80),
        "passed": passed,
    }


def check_ecat_lp_dual_radical_zero() -> dict[str, object]:
    q0 = mp.mpf("11099806389098548918") / mp.mpf("10000000000000000000")
    two_q = q0 + (mp.mpf("1") / q0)
    y21 = mp.mpf("1") / (two_q ** 2)
    y3 = mp.mpf("1") - mp.mpf("2") * y21
    y13 = mp.mpf("0")
    g_diag = [y3, mp.mpf("2") * y21, y13]
    u_vec = [mp.mpf("3") / mp.mpf("5"), mp.mpf("7") / mp.mpf("11"), mp.mpf("13") / mp.mpf("17")]
    v_rad = [mp.mpf("0"), mp.mpf("0"), mp.mpf("1")]
    one_vec = [mp.mpf("1"), mp.mpf("1"), mp.mpf("1")]
    t_vec = [g_diag[j] * u_vec[j] for j in range(3)]
    tv_inner = sum((t_vec[j] * v_rad[j] for j in range(3)), mp.mpf("0"))
    one_v_inner = sum((one_vec[j] * v_rad[j] for j in range(3)), mp.mpf("0"))
    y0 = tv_inner / one_v_inner
    passed = (abs(tv_inner) < mp.mpf("10") ** (-75)) and (abs(y0) < mp.mpf("10") ** (-75))
    return {
        "bean": "qou-v7qj",
        "theorem": "QOU.QBeta.ECatLPDualRadical.dual_price_zero_of_diagonal_gram_cost",
        "tv_inner": mp.nstr(tv_inner, 80),
        "y0_shadow_price": mp.nstr(y0, 80),
        "passed": passed,
    }


def check_polyhedral_domination_squeeze_sub() -> dict[str, object]:
    # 2D polygon points (x, y) projected by supporting functional phi(x, y) = 3x + 5y
    val_cost = (mp.mpf("1"), mp.mpf("2"))
    val_budget = (mp.mpf("4"), mp.mpf("3"))
    phi_cost = mp.mpf("3") * val_cost[0] + mp.mpf("5") * val_cost[1]
    phi_budget = mp.mpf("3") * val_budget[0] + mp.mpf("5") * val_budget[1]
    separates_cb = phi_cost < phi_budget
    separates_bc = phi_budget < phi_cost
    passed = bool(separates_cb and (not separates_bc) and (phi_cost != phi_budget))
    return {
        "bean": "qou-rpj5",
        "theorem": "QOU.AlgebraicSubstrate.squeeze_sub_of_face_separation",
        "phi_cost": mp.nstr(phi_cost, 80),
        "phi_budget": mp.nstr(phi_budget, 80),
        "passed": passed,
    }


def check_magnus_sum_abs_eig_tightness() -> dict[str, object]:
    c = mp.mpf("19") / mp.mpf("23")
    dim = 6
    lhs = mp.mpf(dim) * c
    rhs = mp.sqrt(mp.mpf(dim) * (mp.mpf(dim) * (c ** 2)))
    res = abs(lhs - rhs)
    passed = res < mp.mpf("10") ** (-75)
    return {
        "bean": "qou-yez0",
        "theorem": "QOU.MassTheory.sum_const_eq_sqrt_card_mul_sum_sq",
        "lhs": mp.nstr(lhs, 80),
        "rhs": mp.nstr(rhs, 80),
        "residual": mp.nstr(res, 80),
        "passed": passed,
    }


def main() -> int:
    script_path = pathlib.Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    checks = [
        check_uic_gate_diagonal_active(),
        check_deuteron_first_order_additive(),
        check_ecat_lp_dual_radical_zero(),
        check_polyhedral_domination_squeeze_sub(),
        check_magnus_sum_abs_eig_tightness(),
    ]
    all_passed = all(bool(c["passed"]) for c in checks)
    payload = {
        "probe": "uicgate_deuteron1st_ecatrad_polydom_magnusbound_probe",
        "dps": str(mp.dps),
        "scriptHash": script_hash,
        "allPassed": all_passed,
        "checks": checks,
    }
    print(json.dumps(payload, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
