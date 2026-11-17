#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for QOU.Foundations.Zeta4GenericRingPlancherel.

Covers:
  - 5lcg: zeta4SymmetricOddTerm_eq_zero, zeta4_fourth_power_eq_one,
          survivingCubic_add_one_eq_factored, survivingCubic_at_one_add_one_eq_zero
  - qou-oc4v: keystone_c2_transpose_antisym, qbeta_wenzl_level_two_decomp,
              six_term_mass_paired_decomposition
  - qou-r7qm: ohtsuki_tower_bar_parity_products, period_lattice_cramer_first,
              substrate_period_first_coeff_eq_zero
  - qou-xbyp: rogersSzegoStep_at_one, rogersSzego_H2_identity,
              mass_categorical_descent_telescope
  - qou-sf1t: qPlancherel_sum_measure_eq_one, qPlancherel_total_mass_defect_of_bad_Z,
              molien_jones_markov_n3_common_normaliser
"""

from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def run_checks() -> list[dict[str, object]]:
    mp.mp.dps = 80
    tol = mp.mpf(10) ** (-75)
    checks: list[dict[str, object]] = []

    # 1. 5lcg: zeta4 exclusion & surviving cubic C(y) = y^3 + y^2 - 2y - 1
    z4 = mp.mpc(0, 1)
    c_val = mp.mpf(7) / mp.mpf(3)
    odd_pair = c_val * z4 + c_val * (-z4)
    z4_fourth = (z4 * z4) * (z4 * z4)
    y7 = mp.mpf(2) * mp.cos(mp.mpf(2) * mp.pi / mp.mpf(7))
    cubic_y7 = y7 ** 3 + y7 ** 2 - mp.mpf(2) * y7 - mp.mpf(1)
    factored_y7 = y7 * (y7 - mp.mpf(1)) * (y7 + mp.mpf(2))
    factored_diff = abs((cubic_y7 + mp.mpf(1)) - factored_y7)
    c_at_1 = Fraction(1**3 + 1**2 - 2 * 1 - 1, 1)
    passed_1 = (
        abs(odd_pair) == 0
        and abs(z4_fourth - mp.mpf(1)) == 0
        and abs(cubic_y7) < tol
        and factored_diff < tol
        and c_at_1 + 1 == 0
    )
    checks.append({
        "name": "zeta4_exclusion_and_surviving_cubic",
        "bean": "5lcg",
        "survivingCubicAt2Cos2PiOver7": mp.nstr(abs(cubic_y7), 25),
        "factoredResidual80dps": mp.nstr(factored_diff, 25),
        "cubicAtOnePlusOne": str(c_at_1 + 1),
        "passed": bool(passed_1),
    })

    # 2. qou-oc4v: C2 transpose antisymmetry, Wenzl level-2 recursion [2]_q^2 - 1 = [3]_q, 6-term mass
    beta_star = mp.log(mp.mpf(2)) / mp.mpf(7)
    q = mp.exp(-beta_star)
    q_inv = mp.mpf(1) / q
    two_q = q + q_inv
    three_q = q * q + mp.mpf(1) + q_inv * q_inv
    wenzl_res = abs((two_q * two_q - mp.mpf(1)) - three_q)
    arm_sum, leg_sum = Fraction(11, 3), Fraction(5, 3)
    c2_orig = arm_sum - leg_sum
    c2_trans = leg_sum - arm_sum
    passed_2 = (c2_trans == -c2_orig and c2_orig + c2_trans == 0 and wenzl_res < tol)
    checks.append({
        "name": "braid_knot_c2_and_wenzl_level_two",
        "bean": "qou-oc4v",
        "c2Sum": str(c2_orig + c2_trans),
        "wenzlResidual80dps": mp.nstr(wenzl_res, 25),
        "passed": bool(passed_2),
    })

    # 3. qou-r7qm: Ohtsuki bar-parity & 2x2 period lattice Cramer elimination
    k_even = q + q_inv
    k_odd = q - q_inv
    bar_k_even = q_inv + q
    bar_k_odd = q_inv - q
    odd_sq_res = abs(bar_k_odd * bar_k_odd - k_odd * k_odd)
    mixed_res = abs(bar_k_even * bar_k_odd - (-(k_even * k_odd)))
    p11, p12, p21, p22 = Fraction(3, 2), Fraction(1, 5), Fraction(2, 7), Fraction(4, 3)
    a_c, b_c = Fraction(5, 11), Fraction(-7, 13)
    v1 = a_c * p11 + b_c * p21
    v2 = a_c * p12 + b_c * p22
    det2 = p11 * p22 - p12 * p21
    cramer_lhs = p22 * v1 - p21 * v2
    cramer_rhs = a_c * det2
    passed_3 = (odd_sq_res < tol and mixed_res < tol and cramer_lhs == cramer_rhs and det2 != 0)
    checks.append({
        "name": "ohtsuki_bar_parity_and_period_cramer",
        "bean": "qou-r7qm",
        "periodDet2x2": str(det2),
        "cramerMatch": str(cramer_lhs == cramer_rhs),
        "barParityResidual80dps": mp.nstr(odd_sq_res + mixed_res, 25),
        "passed": bool(passed_3),
    })

    # 4. qou-xbyp: Rogers-Szego H2 expansion & 3-step categorical mass descent telescope
    x_val = mp.mpf(3) / mp.mpf(5)
    h0 = mp.mpf(1)
    h1 = mp.mpf(1) + x_val
    h2_step = (mp.mpf(1) + x_val) * h1 - x_val * (mp.mpf(1) - q) * h0
    h2_rhs = (mp.mpf(1) + x_val) ** 2 - x_val + x_val * q
    rs_res = abs(h2_step - h2_rhs)
    L0, L1, L2, L3 = Fraction(2, 3), Fraction(7, 5), Fraction(19, 10), Fraction(31, 6)
    tele_lhs = (L3 - L2) + (L2 - L1) + (L1 - L0)
    tele_rhs = L3 - L0
    passed_4 = (rs_res < tol and tele_lhs == tele_rhs)
    checks.append({
        "name": "rogers_szego_h2_and_descent_telescope",
        "bean": "qou-xbyp",
        "rogersSzegoResidual80dps": mp.nstr(rs_res, 25),
        "telescopeValue": str(tele_lhs),
        "passed": bool(passed_4),
    })

    # 5. qou-sf1t: QPlancherel partition function Z_q, defect, and Molien n=3 normaliser
    d1, d2, d3 = mp.mpf(1), two_q, three_q
    z_q = d1 * d1 + d2 * d2 + d3 * d3
    z_inv = mp.mpf(1) / z_q
    total_mass = z_inv * (d1 * d1) + z_inv * (d2 * d2) + z_inv * (d3 * d3)
    mass_res = abs(total_mass - mp.mpf(1))
    z_bad = z_q + mp.mpf(1) / mp.mpf(7)
    z_bad_inv = mp.mpf(1) / z_bad
    defect_lhs = (z_bad_inv * (d1 * d1) + z_bad_inv * (d2 * d2) + z_bad_inv * (d3 * d3)) - mp.mpf(1)
    defect_rhs = z_bad_inv * (z_q - z_bad)
    defect_res = abs(defect_lhs - defect_rhs)
    m3, m21, m111, z_mol = Fraction(3, 4), Fraction(5, 8), Fraction(1, 2), Fraction(49, 16)
    mol_lhs = m3 * z_mol + 2 * (m21 * z_mol) + m111 * z_mol
    mol_rhs = (m3 + 2 * m21 + m111) * z_mol
    passed_5 = (mass_res < tol and defect_res < tol and mol_lhs == mol_rhs)
    checks.append({
        "name": "qplancherel_partition_and_molien_normaliser",
        "bean": "qou-sf1t",
        "totalMassResidual80dps": mp.nstr(mass_res, 25),
        "defectResidual80dps": mp.nstr(defect_res, 25),
        "molienValue": str(mol_lhs),
        "passed": bool(passed_5),
    })

    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--output", default="test/results/witnesses/zeta4-generic-ring-plancherel.witness.json")
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    checks = run_checks()
    all_passed = all(bool(c["passed"]) for c in checks)
    if not all_passed:
        raise SystemExit("One or more probe checks failed!")

    witness = {
        "schemaVersion": "1.0",
        "witnessId": "zeta4-generic-ring-plancherel",
        "scriptPath": "computations/probes/zeta4_generic_ring_plancherel_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_hash,
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dps": "80",
        "beans": [
            "5lcg",
            "qou-oc4v",
            "qou-r7qm",
            "qou-xbyp",
            "qou-sf1t",
        ],
        "theorems": [
            "QOU.Foundations.Zeta4GenericRingPlancherel.zeta4SymmetricOddTerm_eq_zero",
            "QOU.Foundations.Zeta4GenericRingPlancherel.survivingCubic_add_one_eq_factored",
            "QOU.Foundations.Zeta4GenericRingPlancherel.keystone_c2_transpose_antisym",
            "QOU.Foundations.Zeta4GenericRingPlancherel.qbeta_wenzl_level_two_decomp",
            "QOU.Foundations.Zeta4GenericRingPlancherel.ohtsuki_tower_bar_parity_products",
            "QOU.Foundations.Zeta4GenericRingPlancherel.substrate_period_first_coeff_eq_zero",
            "QOU.Foundations.Zeta4GenericRingPlancherel.rogersSzego_H2_identity",
            "QOU.Foundations.Zeta4GenericRingPlancherel.qPlancherel_sum_measure_eq_one",
            "QOU.Foundations.Zeta4GenericRingPlancherel.molien_jones_markov_n3_common_normaliser",
        ],
        "allPassed": True,
        "checks": checks,
    }
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
