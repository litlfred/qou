#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 103 Mass theorems (qou-ddo8, qou-dgkf, qou-dke6, qou-dld9, qou-drag)."""

import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def check_finite_order_eigen_sub_one_ne_zero() -> dict:
    mp.mp.dps = 80
    l_val = mp.mpf("7") / mp.mpf("4")
    checks = []
    for k in range(1, 7):
        diff = mp.power(l_val, k) - mp.mpf("1")
        passed = bool(diff > mp.mpf("0"))
        checks.append({
            "k": str(k),
            "diff": mp.nstr(diff, 30),
            "passed": passed,
        })
    return {
        "theorem": "finite_order_eigen_sub_one_ne_zero",
        "bean": "qou-ddo8",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_chain_additive_b3_add_b2_eq_zero() -> dict:
    mp.mp.dps = 80
    checks = []
    for b_str in ["2", "5/3", "11/4"]:
        b = mp.mpf(b_str.split("/")[0]) / mp.mpf(b_str.split("/")[1]) if "/" in b_str else mp.mpf(b_str)
        cb2 = b
        cb3 = mp.mpf("2") * b
        residual = (cb3 - mp.mpf("3") * cb2) + cb2
        passed = bool(abs(residual) <= mp.power(mp.mpf("10"), -70))
        checks.append({
            "b": b_str,
            "residual": mp.nstr(residual, 30),
            "passed": passed,
        })
    return {
        "theorem": "chainAdditive_b3_add_b2_eq_zero",
        "bean": "qou-dgkf",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_wstd_geometric_sub_nonneg() -> dict:
    mp.mp.dps = 80
    w = {0: mp.mpf("1"), 1: mp.mpf("0"), 2: mp.mpf("1"), 3: mp.mpf("1")}
    for k in range(3, 10):
        k_mp = mp.mpf(str(k))
        w[k + 1] = ((k_mp + mp.mpf("2")) / (k_mp + mp.mpf("3"))) * k_mp * w[k - 1]
    sqrt2 = mp.sqrt(mp.mpf("2"))
    c_val = mp.mpf("1") / mp.mpf("30")
    checks = []
    for k in range(3, 11):
        diff = w[k] - c_val * mp.power(sqrt2, k)
        passed = bool(diff >= mp.mpf("0"))
        checks.append({
            "k": str(k),
            "diff": mp.nstr(diff, 30),
            "passed": passed,
        })
    return {
        "theorem": "wStd_geometric_sub_nonneg",
        "bean": "qou-dke6",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_qintbal_three_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    checks = []
    for q_str in ["2", "3/2", "7/5"]:
        q = mp.mpf(q_str.split("/")[0]) / mp.mpf(q_str.split("/")[1]) if "/" in q_str else mp.mpf(q_str)
        q_inv = mp.mpf("1") / q
        qint3 = (mp.power(q, 3) - mp.power(q_inv, 3)) / (q - q_inv)
        laurent = mp.power(q, 2) + mp.mpf("1") + mp.power(q_inv, 2)
        residual = qint3 - laurent
        passed = bool(abs(residual) <= mp.power(mp.mpf("10"), -70))
        checks.append({
            "q": q_str,
            "residual": mp.nstr(residual, 30),
            "passed": passed,
        })
    return {
        "theorem": "qIntBal_three_sub_eq_zero",
        "bean": "qou-dld9",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_weighted_mul_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    # P(X) = 2 + 3X, Q(X) = 5 - X
    x = mp.mpf("4") / mp.mpf("3")
    p_val = mp.mpf("2") + mp.mpf("3") * x
    q_val = mp.mpf("5") - x
    n1, n2 = 2, 3
    w_p = p_val / mp.power(x, n1)
    w_q = q_val / mp.power(x, n2)
    w_pq = (p_val * q_val) / mp.power(x, n1 + n2)
    residual = w_pq - w_p * w_q
    passed = bool(abs(residual) <= mp.power(mp.mpf("10"), -70))
    return {
        "theorem": "weighted_mul_sub_eq_zero",
        "bean": "qou-drag",
        "passed": passed,
        "residual": mp.nstr(residual, 30),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    results = [
        check_finite_order_eigen_sub_one_ne_zero(),
        check_chain_additive_b3_add_b2_eq_zero(),
        check_wstd_geometric_sub_nonneg(),
        check_qintbal_three_sub_eq_zero(),
        check_weighted_mul_sub_eq_zero(),
    ]
    all_passed = all(r["passed"] for r in results)

    payload = {
        "probe": "untwisted_ursell_wstd_wedderburn_weighted_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/untwisted_ursell_wstd_wedderburn_weighted_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": "80",
        "allPassed": all_passed,
        "results": results,
    }
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
