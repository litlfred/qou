#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 92 theorems (qou-172h, qou-1w90, qou-26f2, qou-2cyi, qou-2cz1).

Verifies:
1. jetBinding_self_le (qou-172h):
   jetBinding(me, aD, w, A) <= jetBinding(me, aD, w, A) and strict difference == 0
   evaluated with transcendental weights at 80 decimal places.
2. partialSum_zero_lt_zero_of_term_neg (qou-1w90):
   For term(aD, w, n) = aD(n) * w(n) < 0, 0 + term(aD, w, n) < 0.
3. ratio_invariant_sub_eq_zero (qou-26f2):
   For c != 0 and b != 0, (c * a) / (c * b) - a / b = 0.
4. unit_modulus_zero_ne_real_gt_one (qou-2cyi):
   |exp(0 * i)| = 1 != q for q > 1.
5. correction_zero_of_eps_self (qou-2cz1):
   For 1 - e != 0, log((1 - e) / (1 - e)) / D = 0.
"""

import hashlib
import json
import os
import sys
from mpmath import mp, mpf

mp.dps = 80


def run_probe(commit_sha: str) -> dict:
    script_path = os.path.abspath(__file__)
    with open(script_path, "rb") as f:
        script_sha256 = hashlib.sha256(f.read()).hexdigest()

    tol = mpf("1e-75")
    checks = []

    # 1. jetBinding_self_le (qou-172h)
    me = mp.pi / mpf("11")
    aD = [mp.e / mpf("5"), mp.sqrt(mpf("3")) / mpf("7"), mp.catalan / mpf("4"), mp.ln2 / mpf("3")]
    w = [mpf("1") / mpf("2"), mp.pi / mpf("13"), mp.sqrt(mpf("5")) / mpf("9"), mp.e / mpf("17")]
    jb_val = me * sum(aD[k] * w[k] for k in range(len(aD)))
    jb_diff = abs(jb_val - jb_val)
    c1_pass = bool((jb_val <= jb_val) and (jb_diff == mpf("0")) and (jb_val > mpf("0")))
    checks.append({
        "id": "jetBinding_self_le_qou_172h",
        "bean": "qou-172h",
        "theorem": "QOU.Mass.jetBinding_self_le",
        "jetBinding_val": mp.nstr(jb_val, 80),
        "self_diff": mp.nstr(jb_diff, 80),
        "passed": c1_pass,
    })

    # 2. partialSum_zero_lt_zero_of_term_neg (qou-1w90)
    aD_n = -mp.pi / mpf("7")
    w_n = mp.e / mpf("3")
    term_n = aD_n * w_n
    zero_plus_term = mpf("0") + term_n
    c2_pass = bool((term_n < mpf("0")) and (zero_plus_term < mpf("0")) and abs(zero_plus_term - term_n) == mpf("0"))
    checks.append({
        "id": "partialSum_zero_lt_zero_of_term_neg_qou_1w90",
        "bean": "qou-1w90",
        "theorem": "QOU.Mass.partialSum_zero_lt_zero_of_term_neg",
        "term_n": mp.nstr(term_n, 80),
        "zero_plus_term": mp.nstr(zero_plus_term, 80),
        "passed": c2_pass,
    })

    # 3. ratio_invariant_sub_eq_zero (qou-26f2)
    c_val = mp.pi + mp.sqrt(mpf("2"))
    a_val = mp.e * mp.ln2
    b_val = mp.sqrt(mpf("7")) + mp.catalan
    lhs_ratio = (c_val * a_val) / (c_val * b_val)
    rhs_ratio = a_val / b_val
    ratio_diff = abs(lhs_ratio - rhs_ratio)
    c3_pass = bool(ratio_diff < tol)
    checks.append({
        "id": "ratio_invariant_sub_eq_zero_qou_26f2",
        "bean": "qou-26f2",
        "theorem": "QOU.Mass.ratio_invariant_sub_eq_zero",
        "lhs_ratio": mp.nstr(lhs_ratio, 80),
        "rhs_ratio": mp.nstr(rhs_ratio, 80),
        "abs_diff": mp.nstr(ratio_diff, 80),
        "passed": c3_pass,
    })

    # 4. unit_modulus_zero_ne_real_gt_one (qou-2cyi)
    z0 = mp.exp(mpf("0") * mp.j)
    mod_z0 = abs(z0)
    q_val = mpf("1") + mp.pi / mpf("9")
    gap_q = q_val - mod_z0
    c4_pass = bool((abs(mod_z0 - mpf("1")) == mpf("0")) and (q_val > mpf("1")) and (gap_q > mpf("0")))
    checks.append({
        "id": "unit_modulus_zero_ne_real_gt_one_qou_2cyi",
        "bean": "qou-2cyi",
        "theorem": "QOU.Mass.unit_modulus_zero_ne_real_gt_one",
        "modulus_exp_zero": mp.nstr(mod_z0, 80),
        "q_val": mp.nstr(q_val, 80),
        "gap_q_minus_modulus": mp.nstr(gap_q, 80),
        "passed": c4_pass,
    })

    # 5. correction_zero_of_eps_self (qou-2cz1)
    e_val = mp.pi / mpf("13")
    D_val = mp.sqrt(mpf("11"))
    one_minus_e = mpf("1") - e_val
    corr_val = mp.log(one_minus_e / one_minus_e) / D_val
    c5_pass = bool((one_minus_e != mpf("0")) and (abs(corr_val) < tol))
    checks.append({
        "id": "correction_zero_of_eps_self_qou_2cz1",
        "bean": "qou-2cz1",
        "theorem": "QOU.Mass.correction_zero_of_eps_self",
        "one_minus_e": mp.nstr(one_minus_e, 80),
        "correction_val": mp.nstr(corr_val, 80),
        "passed": c5_pass,
    })

    all_passed = all(c["passed"] for c in checks)
    return {
        "probe": "jetmono-jetsign-kzratio-kzunit-kappacorr-probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/jetmono_jetsign_kzratio_kzunit_kappacorr_probe.py",
        "scriptCommitSha": commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": "80",
        "allPassed": all_passed,
        "checks": checks,
    }


if __name__ == "__main__":
    sha = sys.argv[1] if len(sys.argv) > 1 else "0000000000000000000000000000000000000000"
    out = run_probe(sha)
    print(json.dumps(out, indent=2))
    sys.exit(0 if out["allPassed"] else 1)
