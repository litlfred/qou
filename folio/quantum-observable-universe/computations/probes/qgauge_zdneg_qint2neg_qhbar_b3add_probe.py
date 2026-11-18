#!/usr/bin/env python3
"""80-dps mpmath probe for Round 88 theorems (qou-59i6, qou-7p7d, qou-8du0, qou-8hw1, qou-bmz8)."""
import hashlib
import json
import os
import sys
from mpmath import mp, mpf

mp.dps = 80


def verify_all():
    results = {}
    tol = mpf("1e-75")

    # 1. qou-59i6: scalar_gauge_self
    s = mp.pi / mpf("3")
    A_entries = [mpf("2"), mpf("-5"), mpf("7"), mpf("11")]
    B_entries = [(s / s) * x for x in A_entries]
    max_diff_gauge = max(abs(b - a) for a, b in zip(A_entries, B_entries))
    results["scalar_gauge_self"] = {
        "s": mp.nstr(s, 80),
        "max_diff": mp.nstr(max_diff_gauge, 80),
        "passed": bool(max_diff_gauge < tol),
    }

    # 2. qou-7p7d: zJ_one_eq_zD_one
    q1 = mpf("1")
    zJ_1 = (mpf("3") * q1 - (mpf("1") / q1)) / mpf("4")
    zD_1 = (q1 ** 3) / (q1 ** 2 + mpf("1"))
    res_z1 = abs(zJ_1 - zD_1)
    results["zJ_one_eq_zD_one"] = {
        "zJ_1": mp.nstr(zJ_1, 80),
        "zD_1": mp.nstr(zD_1, 80),
        "residual": mp.nstr(res_z1, 80),
        "passed": bool(res_z1 == mpf("0")),
    }

    # 3. qou-8du0: zSL3_ne_zSL2
    q = mpf("111") / mpf("100")
    qint2 = q + (mpf("1") / q)
    qint3 = (q ** 2) + mpf("1") + (mpf("1") / (q ** 2))
    qint4 = (q ** 3) + q + (mpf("1") / q) + (mpf("1") / (q ** 3))
    zSL2 = (q * qint3 - (mpf("1") / q)) / (qint2 ** 2)
    zSL3 = (q * (qint3 * qint4 / qint2) - (mpf("1") / q) * qint3) / (qint3 ** 2)
    gap_sl = abs(zSL3 - zSL2)
    results["zSL3_ne_zSL2"] = {
        "q": mp.nstr(q, 80),
        "zSL2": mp.nstr(zSL2, 80),
        "zSL3": mp.nstr(zSL3, 80),
        "abs_gap": mp.nstr(gap_sl, 80),
        "passed": bool(gap_sl > mpf("1e-5")),
    }

    # 4. qou-8hw1: saddle_offset_at_one
    w = mp.sqrt(mpf("19")) / mpf("5")
    hbar_1 = mpf("1") - (mpf("1") / q1)
    lhs_off = (w / q1) - w
    rhs_off = -hbar_1 * w
    res_off = abs(lhs_off - rhs_off)
    results["saddle_offset_at_one"] = {
        "w": mp.nstr(w, 80),
        "lhs": mp.nstr(lhs_off, 80),
        "rhs": mp.nstr(rhs_off, 80),
        "residual": mp.nstr(res_off, 80),
        "passed": bool(res_off == mpf("0") and lhs_off == mpf("0")),
    }

    # 5. qou-bmz8: b3Contrib_scale
    gamma = mp.pi / mpf("11")
    f2, f3 = mp.sqrt(mpf("2")), mp.sqrt(mpf("5"))
    lhs_b3 = (gamma * f3) - mpf("3") * (gamma * f2)
    rhs_b3 = gamma * (f3 - mpf("3") * f2)
    res_b3 = abs(lhs_b3 - rhs_b3)
    results["b3Contrib_scale"] = {
        "lhs": mp.nstr(lhs_b3, 80),
        "rhs": mp.nstr(rhs_b3, 80),
        "residual": mp.nstr(res_b3, 80),
        "passed": bool(res_b3 < tol),
    }

    all_passed = all(v["passed"] for v in results.values())
    script_bytes = open(os.path.abspath(__file__), "rb").read()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    commit_sha = os.environ.get("SCRIPT_COMMIT_SHA", "0" * 40)
    payload = {
        "probe": "qgauge_zdneg_qint2neg_qhbar_b3add_probe",
        "beans": ["qou-59i6", "qou-7p7d", "qou-8du0", "qou-8hw1", "qou-bmz8"],
        "dps": "80",
        "scriptCommitSha": commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "allPassed": all_passed,
        "results": results,
    }
    return payload


if __name__ == "__main__":
    out = verify_all()
    print(json.dumps(out, indent=2, sort_keys=True))
    if not out["allPassed"]:
        sys.exit(1)
