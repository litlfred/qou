#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 68 Nuclear Binding, Mass Theory & Regulator theorems.

Covers:
  - qou-tbpl: QOU.Mass.TwoBodyInterfaceBond.cross_difference_eq_zero
  - qou-v0yw: QOU.Mass.CoordinationSurfaceDeficit.bondCount_deficit_and_uniform_eq
  - qou-uh5f: QOU.MobiusRegulator.bfhwRegulator_sub_msRegulator_eq_neg_four
  - qou-sv7h: QOU.MassTheory.BlockSDPNondegeneracy.net_and_obj_add
  - qou-ix0x: QOU.Mass.MilnorCarriesOrderNotMagnitude.geometric_order_step_diff_and_hankel_zero
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

    # 1. qou-tbpl: TwoBodyInterfaceBond.cross_difference_eq_zero & traceFactorisation
    E0 = mp.mpf(2656) / mp.mpf(1000)
    tL0_p, tL0_n = mp.mpf(7) / mp.mpf(5), mp.mpf(9) / mp.mpf(5)
    tR0_p, tR0_n = mp.mpf(11) / mp.mpf(7), mp.mpf(13) / mp.mpf(7)
    tL_p, tL_n = mp.mpf(6) / mp.mpf(5), mp.mpf(8) / mp.mpf(5)
    tR_p, tR_n = mp.mpf(10) / mp.mpf(7), mp.mpf(12) / mp.mpf(7)

    def f_sep(a_L0: mp.mpf, a_L: mp.mpf, b_R0: mp.mpf, b_R: mp.mpf) -> mp.mpf:
        return E0 * mp.log((a_L0 * b_R0) / (a_L * b_R))

    f_pn = f_sep(tL0_p, tL_p, tR0_n, tR_n)
    f_np = f_sep(tL0_n, tL_n, tR0_p, tR_p)
    f_pp = f_sep(tL0_p, tL_p, tR0_p, tR_p)
    f_nn = f_sep(tL0_n, tL_n, tR0_n, tR_n)
    cross_diff = abs((f_pn + f_np) - (f_pp + f_nn))
    g_p, g_n = Fraction(5, 3), Fraction(11, 7)
    k_p, k_n = Fraction(2, 5), Fraction(9, 4)
    exact_cross_diff = ((g_p + k_n) + (g_n + k_p)) - ((g_p + k_p) + (g_n + k_n))
    passed_1 = (cross_diff < tol and exact_cross_diff == 0)
    checks.append({
        "name": "cross_difference_eq_zero",
        "bean": "qou-tbpl",
        "exactCrossDiff": str(exact_cross_diff),
        "logTraceCrossResidual80dps": mp.nstr(cross_diff, 25),
        "passed": bool(passed_1),
    })

    # 2. qou-v0yw: CoordinationSurfaceDeficit.bondCount_deficit_and_uniform_eq
    k_deg = Fraction(12, 1)
    k_surf = Fraction(8, 1)
    A_int = Fraction(16, 1)
    A_surf = Fraction(12, 1)
    A_tot = A_int + A_surf
    bond_count = (k_deg * A_int + k_surf * A_surf) / 2
    plateau_count = k_deg * A_tot / 2
    deficit_lhs = plateau_count - bond_count
    deficit_rhs = (k_deg - k_surf) * A_surf / 2
    uniform_count = (k_deg * A_int + k_deg * A_surf) / 2
    A_mp = mp.mpf(28)
    c_mp = mp.mpf(3)
    Asurf_mp = c_mp * (A_mp ** (mp.mpf(2) / mp.mpf(3)))
    Aint_mp = A_mp - Asurf_mp
    eps_mp = mp.mpf(7) / mp.mpf(3)
    bc_mp = (mp.mpf(12) * Aint_mp + mp.mpf(8) * Asurf_mp) / mp.mpf(2)
    per_nuc_lhs = eps_mp * bc_mp / A_mp
    per_nuc_rhs = eps_mp * mp.mpf(12) / mp.mpf(2) - (eps_mp * c_mp * mp.mpf(4) / mp.mpf(2)) * (A_mp ** (-mp.mpf(1) / mp.mpf(3)))
    semf_res = abs(per_nuc_lhs - per_nuc_rhs)
    passed_2 = (deficit_lhs == deficit_rhs and uniform_count == plateau_count and semf_res < tol)
    checks.append({
        "name": "bondCount_deficit_and_uniform_eq",
        "bean": "qou-v0yw",
        "bondDeficit": str(deficit_lhs),
        "uniformBondCount": str(uniform_count),
        "semfSurfaceLawResidual80dps": mp.nstr(semf_res, 25),
        "passed": bool(passed_2),
    })

    # 3. qou-uh5f: MobiusRegulator.bfhwRegulator_sub_msRegulator_eq_neg_four
    ell = mp.mpf(2) * mp.pi
    eps = mp.mpf(1) / mp.mpf(137)
    inner_int = mp.mpf(1) / eps - mp.mpf(1) / (ell / mp.mpf(2))
    bfhw_reg = ell * (mp.mpf(2) * inner_int)
    ms_reg = mp.mpf(2) * ell / eps
    reg_diff_res = abs((bfhw_reg - ms_reg) - (-mp.mpf(4)))
    ell_q = Fraction(17, 5)
    eps_q = Fraction(1, 23)
    bfhw_q = ell_q * 2 * (1 / eps_q - 2 / ell_q)
    ms_q = 2 * ell_q / eps_q
    passed_3 = (reg_diff_res < tol and bfhw_q - ms_q == -4)
    checks.append({
        "name": "bfhwRegulator_sub_msRegulator_eq_neg_four",
        "bean": "qou-uh5f",
        "exactDifference": str(bfhw_q - ms_q),
        "regulatorResidual80dps": mp.nstr(reg_diff_res, 25),
        "passed": bool(passed_3),
    })

    # 4. qou-sv7h: BlockSDPNondegeneracy.net_and_obj_add
    beta_star = mp.log(mp.mpf(2)) / mp.mpf(7)
    q = mp.exp(-beta_star)
    y_vec = [q ** 2, mp.mpf(2) * q, (mp.mpf(1) + q) ** 2]
    t1_vec = [mp.mpf(3) / mp.mpf(7), mp.mpf(5) / mp.mpf(11), mp.mpf(2) / mp.mpf(13)]
    t2_vec = [mp.mpf(4) / mp.mpf(7), mp.mpf(6) / mp.mpf(11), mp.mpf(11) / mp.mpf(13)]
    t_sum = [a + b for a, b in zip(t1_vec, t2_vec)]
    net_lhs = sum(t_sum)
    net_rhs = sum(t1_vec) + sum(t2_vec)
    obj_lhs = sum(y * t for y, t in zip(y_vec, t_sum))
    obj_rhs = sum(y * t for y, t in zip(y_vec, t1_vec)) + sum(y * t for y, t in zip(y_vec, t2_vec))
    sdp_res = abs(net_lhs - net_rhs) + abs(obj_lhs - obj_rhs)
    passed_4 = (sdp_res < tol and obj_lhs > 0)
    checks.append({
        "name": "net_and_obj_add",
        "bean": "qou-sv7h",
        "netSum": mp.nstr(net_lhs, 25),
        "additivityResidual80dps": mp.nstr(sdp_res, 25),
        "passed": bool(passed_4),
    })

    # 5. qou-ix0x: MilnorCarriesOrderNotMagnitude.geometric_order_step_diff_and_hankel_zero
    g_val = Fraction(3, 5)
    b2, b3, b4 = g_val ** 2, g_val ** 4, g_val ** 6
    step_lhs = (b4 - b3) * b2
    step_rhs = (b3 - b2) * b3
    hankel = b2 * b4 - b3 ** 2
    g_mp = mp.exp(-beta_star)
    b2_mp, b3_mp, b4_mp = g_mp ** 2, g_mp ** 4, g_mp ** 6
    step_res = abs((b4_mp - b3_mp) * b2_mp - (b3_mp - b2_mp) * b3_mp)
    hankel_res = abs(b2_mp * b4_mp - b3_mp ** 2)
    passed_5 = (step_lhs == step_rhs and hankel == 0 and step_res < tol and hankel_res < tol)
    checks.append({
        "name": "geometric_order_step_diff_and_hankel_zero",
        "bean": "qou-ix0x",
        "exactStepProduct": str(step_lhs),
        "exactHankelDefect": str(hankel),
        "hankelResidual80dps": mp.nstr(step_res + hankel_res, 25),
        "passed": bool(passed_5),
    })

    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--output", default="test/results/witnesses/twobody-deficit-regulator-sdp-milnor.witness.json")
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    checks = run_checks()
    if not all(bool(c["passed"]) for c in checks):
        raise SystemExit("One or more probe checks failed!")

    witness = {
        "schemaVersion": "1.0",
        "witnessId": "twobody-deficit-regulator-sdp-milnor",
        "scriptPath": "computations/probes/twobody_deficit_regulator_sdp_milnor_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_hash,
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dps": "80",
        "beans": [
            "qou-tbpl",
            "qou-v0yw",
            "qou-uh5f",
            "qou-sv7h",
            "qou-ix0x",
        ],
        "theorems": [
            "QOU.Mass.TwoBodyInterfaceBond.cross_difference_eq_zero",
            "QOU.Mass.CoordinationSurfaceDeficit.bondCount_deficit_and_uniform_eq",
            "QOU.MobiusRegulator.bfhwRegulator_sub_msRegulator_eq_neg_four",
            "QOU.MassTheory.BlockSDPNondegeneracy.net_and_obj_add",
            "QOU.Mass.MilnorCarriesOrderNotMagnitude.geometric_order_step_diff_and_hankel_zero",
        ],
        "allPassed": True,
        "checks": checks,
    }
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
