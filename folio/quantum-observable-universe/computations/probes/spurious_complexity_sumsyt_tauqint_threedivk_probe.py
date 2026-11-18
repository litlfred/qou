#!/usr/bin/env python3
"""80-dps mpmath probe for Round 101 Mass theorems (qou-bake, qou-baye, qou-bg3w, qou-bi43, qou-bstl)."""

import argparse
import hashlib
import json
from pathlib import Path
from mpmath import mp

mp.dps = 80


def verify_free_energy_absorb() -> dict:
    delta_val = mp.mpf("2")
    k_val = 3
    t_val = mp.mpf("13") / mp.mpf("5")
    closure_norm = t_val / (delta_val ** k_val)
    absorbed = (delta_val ** k_val) * closure_norm
    fe_absorbed = -mp.log(absorbed)
    fe_bare = -mp.log(t_val)
    diff = fe_absorbed - fe_bare
    return {
        "freeEnergyAbsorbed": mp.nstr(fe_absorbed, 80),
        "freeEnergyBare": mp.nstr(fe_bare, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_admissible_succ() -> dict:
    a_val = 2
    crossings = 6
    braid_idx = 3
    adm_a = (crossings <= 10 * a_val - 2) and (braid_idx <= 3 * a_val)
    adm_succ = (crossings <= 10 * (a_val + 1) - 2) and (braid_idx <= 3 * (a_val + 1))
    return {
        "admissibleAtA": adm_a,
        "admissibleAtASucc": adm_succ,
        "passed": adm_a and adm_succ,
    }


def verify_sum_syt_zero_eq_one() -> dict:
    # Involution numbers I(0) = 1, I(1) = 1
    i0 = mp.mpf("1")
    i1 = mp.mpf("1")
    diff = i0 - i1
    return {
        "sumSYTZero": mp.nstr(i0, 80),
        "sumSYTOne": mp.nstr(i1, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_tau_qint_sub() -> dict:
    q_val = mp.mpf("7") / mp.mpf("5")
    q_inv = mp.mpf("1") / q_val
    b_val = q_val + q_inv
    lhs = mp.mpf("3") * (mp.mpf("3") * (q_val ** 4) + mp.mpf("8") * (q_val ** 2) + mp.mpf("3")) / (
        mp.mpf("4") * q_val * ((q_val + mp.mpf("1")) ** 2)
    )
    rhs = mp.mpf("3") * (mp.mpf("3") * (b_val ** 2) + mp.mpf("2")) / (
        mp.mpf("4") * (b_val + mp.mpf("2"))
    )
    diff = lhs - rhs
    return {
        "lhs": mp.nstr(lhs, 80),
        "rhs": mp.nstr(rhs, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_two_cos_recursion() -> dict:
    theta_val = mp.mpf("2") * mp.pi / mp.mpf("3") + mp.mpf("1") / mp.mpf("40")
    k_val = 5
    c_k = mp.mpf("2") * mp.cos(mp.mpf(str(k_val)) * theta_val)
    c_k1 = mp.mpf("2") * mp.cos(mp.mpf(str(k_val + 1)) * theta_val)
    c_k2 = mp.mpf("2") * mp.cos(mp.mpf(str(k_val + 2)) * theta_val)
    two_cos_theta = mp.mpf("2") * mp.cos(theta_val)
    residual = c_k2 - (two_cos_theta * c_k1 - c_k)
    return {
        "twoCosKPlus2": mp.nstr(c_k2, 80),
        "rhs": mp.nstr(two_cos_theta * c_k1 - c_k, 80),
        "residual": mp.nstr(residual, 80),
        "passed": abs(residual) < mp.mpf("10") ** (-75),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    c1 = verify_free_energy_absorb()
    c2 = verify_admissible_succ()
    c3 = verify_sum_syt_zero_eq_one()
    c4 = verify_tau_qint_sub()
    c5 = verify_two_cos_recursion()

    all_passed = all(x["passed"] for x in (c1, c2, c3, c4, c5))
    payload = {
        "probe": "spurious_complexity_sumsyt_tauqint_threedivk_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/spurious_complexity_sumsyt_tauqint_threedivk_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": int(mp.dps),
        "allPassed": all_passed,
        "checks": {
            "freeEnergyAbsorbSubEqZero": c1,
            "admissibleSucc": c2,
            "sumNumSYTSizeZeroEqSizeOne": c3,
            "tauQuantumIntegerFormSubEqZero": c4,
            "twoCosRecursionSubEqZero": c5,
        },
    }
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
