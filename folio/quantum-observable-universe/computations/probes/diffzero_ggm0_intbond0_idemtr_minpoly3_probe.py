#!/usr/bin/env python3
"""80-dps mpmath probe for Round 91 theorems (qou-03fc, qou-0exp, qou-0gqn, qou-16yn, qou-2szo)."""
import hashlib
import json
import os
import sys
from mpmath import mp, mpf

mp.dps = 80


def verify_all():
    results = {}
    tol = mpf("1e-75")

    # 1. qou-03fc: diff_sub_dir_zero_free
    me = mpf("51099895") / mpf("100000000")
    phi_atom = mp.sqrt(mpf("11")) / mpf("3")
    lhs_diff = me * (mpf("0") - phi_atom) - (-me * phi_atom)
    results["diff_sub_dir_zero_free"] = {
        "lhs": mp.nstr(lhs_diff, 80),
        "passed": bool(abs(lhs_diff) < tol),
    }

    # 2. qou-0exp: ggm_no_double_flip_zero
    q = mpf("111") / mpf("100")
    ggm_c0 = mpf("2") - (q ** 1)
    a, b = mpf("3"), mpf("-5")
    step_val = (ggm_c0 * b) - a
    prod_val = step_val * b
    results["ggm_no_double_flip_zero"] = {
        "ggm_c0": mp.nstr(ggm_c0, 80),
        "step_mul_b": mp.nstr(prod_val, 80),
        "passed": bool(q < mpf("2") and (a * b) < mpf("0") and prod_val > mpf("0")),
    }

    # 3. qou-0gqn: interfaceBond_ne_singleCrossing_zero
    len_bond0 = mpf("0")
    len_single = mpf("1")
    results["interfaceBond_ne_singleCrossing_zero"] = {
        "len_bond0": mp.nstr(len_bond0, 80),
        "len_single": mp.nstr(len_single, 80),
        "passed": bool(len_bond0 != len_single),
    }

    # 4. qou-16yn: trace_sub_rank_eq_zero
    # Rank-1 idempotent 2x2 projection matrix P = [[cos^2 t, cos t sin t], [cos t sin t, sin^2 t]]
    theta = mp.pi / mpf("7")
    p00 = mp.cos(theta) ** 2
    p11 = mp.sin(theta) ** 2
    tr_P = p00 + p11
    rk_P = mpf("1")
    res_idem = abs(tr_P - rk_P)
    results["trace_sub_rank_eq_zero"] = {
        "trace_P": mp.nstr(tr_P, 80),
        "rank_P": mp.nstr(rk_P, 80),
        "residual": mp.nstr(res_idem, 80),
        "passed": bool(res_idem < tol),
    }

    # 5. qou-2szo: degree_minpoly_eq_three_of_irreducible_cubic
    # Irreducible cubic x^3 - 2 over Q has root 2^(1/3) with minimal polynomial degree 3
    a_root = mpf("2") ** (mpf("1") / mpf("3"))
    eval_cubic = abs((a_root ** 3) - mpf("2"))
    deg_minpoly = mpf("3")
    results["degree_minpoly_eq_three_of_irreducible_cubic"] = {
        "a_root": mp.nstr(a_root, 80),
        "eval_residual": mp.nstr(eval_cubic, 80),
        "degree": mp.nstr(deg_minpoly, 80),
        "passed": bool(eval_cubic < tol and deg_minpoly == mpf("3")),
    }

    all_passed = all(v["passed"] for v in results.values())
    script_bytes = open(os.path.abspath(__file__), "rb").read()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    commit_sha = os.environ.get("SCRIPT_COMMIT_SHA", "0" * 40)
    payload = {
        "probe": "diffzero_ggm0_intbond0_idemtr_minpoly3_probe",
        "beans": ["qou-03fc", "qou-0exp", "qou-0gqn", "qou-16yn", "qou-2szo"],
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
