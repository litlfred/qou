#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 109 BraidKnot theorems (qou-k9yt, qou-kt8o, qou-l1gv, qou-lsib, qou-m8s9)."""

import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def check_card_garnirshape_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    cases = [([3, 3], 0, 1), ([4, 3, 2], 1, 1), ([5, 4, 2], 0, 2)]
    checks = []
    for rows, i, j in cases:
        orig_card = sum(rows)
        li = rows[i]
        li1 = rows[i + 1]
        garnir_comp = rows[:i] + [j, li + 1, li1 - j - 1] + rows[i + 2:]
        garnir_card = sum(garnir_comp)
        residual = mp.mpf(str(garnir_card)) - mp.mpf(str(orig_card))
        passed = bool(abs(residual) <= mp.power(mp.mpf("10"), -70))
        checks.append({
            "rows": str(rows),
            "node": f"({i},{j})",
            "residual": mp.nstr(residual, 30),
            "passed": passed,
        })
    return {
        "theorem": "card_garnirShape_sub_eq_zero",
        "bean": "qou-k9yt",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_linear_sub_excess_slack_nonneg() -> dict:
    mp.mp.dps = 80
    c = mp.mpf("5") / mp.mpf("2")
    l_val = mp.mpf("3")
    y0 = mp.mpf("2")
    checks = []
    for y_str in ["1", "2", "11/4", "4"]:
        y = mp.mpf(y_str.split("/")[0]) / mp.mpf(y_str.split("/")[1]) if "/" in y_str else mp.mpf(y_str)
        excess = max(mp.mpf("0"), mp.power(y, 2) - mp.power(y0, 2))
        lhs = c * y - (l_val / mp.mpf("2")) * excess
        rhs = c * y0 + mp.power(c, 2) / (mp.mpf("2") * l_val)
        slack = rhs - lhs
        passed = bool(slack >= mp.mpf("0"))
        checks.append({
            "y": y_str,
            "slack": mp.nstr(slack, 30),
            "passed": passed,
        })
    return {
        "theorem": "linear_sub_excess_slack_nonneg",
        "bean": "qou-kt8o",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def std_two_matrices(q: mp.mpf) -> tuple:
    q_inv = mp.mpf("1") / q
    s0 = mp.matrix([[q, mp.mpf("1")], [mp.mpf("0"), -q_inv]])
    s1 = mp.matrix([[-q_inv, mp.mpf("0")], [mp.mpf("1"), q]])
    l1 = s0 ** 2
    l2 = s1 * l1 * s1
    return s0, s1, l1, l2


def check_jmraw_comm_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    checks = []
    for q_str in ["3/2", "7/5"]:
        q = mp.mpf(q_str.split("/")[0]) / mp.mpf(q_str.split("/")[1])
        _, _, l1, l2 = std_two_matrices(q)
        comm = l1 * l2 - l2 * l1
        frob = mp.sqrt(sum(mp.power(abs(comm[r, c]), 2) for r in range(2) for c in range(2)))
        passed = bool(frob <= mp.power(mp.mpf("10"), -70))
        checks.append({
            "q": q_str,
            "comm_norm": mp.nstr(frob, 30),
            "passed": passed,
        })
    return {
        "theorem": "jmRaw_comm_sub_eq_zero",
        "bean": "qou-l1gv",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_stdtwobelow3_twist_sub_one_eq_zero() -> dict:
    mp.mp.dps = 80
    checks = []
    for q_str in ["2", "5/3", "9/7"]:
        q = mp.mpf(q_str.split("/")[0]) / mp.mpf(q_str.split("/")[1]) if "/" in q_str else mp.mpf(q_str)
        s0, s1, _, _ = std_two_matrices(q)
        twist = (s0 * s1) ** 3
        ident = mp.eye(2)
        diff = twist - ident
        frob = mp.sqrt(sum(mp.power(abs(diff[r, c]), 2) for r in range(2) for c in range(2)))
        passed = bool(frob <= mp.power(mp.mpf("10"), -70))
        checks.append({
            "q": q_str,
            "residual_norm": mp.nstr(frob, 30),
            "passed": passed,
        })
    return {
        "theorem": "stdTwoBelow3_twist_sub_one_eq_zero",
        "bean": "qou-lsib",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_jmraw_one_comm_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    q = mp.mpf("11") / mp.mpf("6")
    _, _, l1, l2 = std_two_matrices(q)
    diff = l1 * l2 - l2 * l1
    frob = mp.sqrt(sum(mp.power(abs(diff[r, c]), 2) for r in range(2) for c in range(2)))
    passed = bool(frob <= mp.power(mp.mpf("10"), -70))
    return {
        "theorem": "jmRaw_one_comm_sub_eq_zero",
        "bean": "qou-m8s9",
        "passed": passed,
        "residual_norm": mp.nstr(frob, 30),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    results = [
        check_card_garnirshape_sub_eq_zero(),
        check_linear_sub_excess_slack_nonneg(),
        check_jmraw_comm_sub_eq_zero(),
        check_stdtwobelow3_twist_sub_one_eq_zero(),
        check_jmraw_one_comm_sub_eq_zero(),
    ]
    all_passed = all(r["passed"] for r in results)

    payload = {
        "probe": "garnircard_hardwall_heckejmcomm_hecketheta_heckereduction_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/garnircard_hardwall_heckejmcomm_hecketheta_heckereduction_probe.py",
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
