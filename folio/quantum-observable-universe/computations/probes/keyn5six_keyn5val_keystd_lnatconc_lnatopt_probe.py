#!/usr/bin/env python3
"""80-dps mpmath numerical witness probe for Round 113 BraidKnot theorems:
- qou-pg2r: muon_block_pinned_all_roots_sub_eq_zero (KeystoneN5LevelSixSuffices.lean)
- qou-plb2: muon_block_pinned_level7_sub_eq_zero (KeystoneN5ValueMapRigidity.lean)
- qou-po7i: qFactorial_standard_hook_sub_eq_zero (KeystoneStandardRepQDim.lean)
- qou-prop3b: neg_exp_series_concave_sub_nonneg (LNaturalConcaveForm.lean)
- qou-py7e: global_of_local_boxDiffDomain_sub_nonneg (LNaturalOptimality.lean)
"""

import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def poly32_eval(t):
    return (t ** 4) - mp.mpf(3) * (t ** 2) + mp.mpf(1)


def q_int_geo(q, m):
    return sum(q ** k for k in range(m))


def q_factorial_geo(q, m):
    prod = mp.mpf(1)
    for k in range(1, m + 1):
        prod *= q_int_geo(q, k)
    return prod


def run_checks():
    results = []

    # 1. qou-pg2r: muon_block_pinned_all_roots_sub_eq_zero via 5 fibre roots N=0..4
    pts1 = [mp.mpf(2) * mp.cos(mp.pi / mp.mpf(n + 2)) for n in range(5)]
    vals1 = [poly32_eval(x) for x in pts1]
    t0 = mp.mpf(23) / mp.mpf(11)
    bw_eval1 = mp.mpf(0)
    for i, xi in enumerate(pts1):
        li = mp.mpf(1)
        for j, xj in enumerate(pts1):
            if i != j:
                li *= (t0 - xj) / (xi - xj)
        bw_eval1 += vals1[i] * li
    target1 = poly32_eval(t0)
    diff1 = bw_eval1 - target1
    results.append({
        "bean": "qou-pg2r",
        "theorem": "QOU.BraidKnot.KeystoneN5LevelSixSuffices.muon_block_pinned_all_roots_sub_eq_zero",
        "bwEvalT0": mp.nstr(bw_eval1, 80),
        "poly32EvalT0": mp.nstr(target1, 80),
        "residual": mp.nstr(abs(diff1), 80),
        "passed": abs(diff1) < mp.mpf(10) ** (-74),
    })

    # 2. qou-plb2: muon_block_pinned_level7_sub_eq_zero via 6 level-7 fold points k=1..6
    pts2 = [mp.mpf(2) * mp.cos(mp.mpf(k) * mp.pi / mp.mpf(7)) for k in range(1, 7)]
    vals2 = [poly32_eval(x) for x in pts2]
    bw_eval2 = mp.mpf(0)
    for i, xi in enumerate(pts2):
        li = mp.mpf(1)
        for j, xj in enumerate(pts2):
            if i != j:
                li *= (t0 - xj) / (xi - xj)
        bw_eval2 += vals2[i] * li
    diff2 = bw_eval2 - target1
    results.append({
        "bean": "qou-plb2",
        "theorem": "QOU.BraidKnot.KeystoneN5ValueMapRigidity.muon_block_pinned_level7_sub_eq_zero",
        "bwEvalT0": mp.nstr(bw_eval2, 80),
        "poly32EvalT0": mp.nstr(target1, 80),
        "residual": mp.nstr(abs(diff2), 80),
        "passed": abs(diff2) < mp.mpf(10) ** (-74),
    })

    # 3. qou-po7i: qFactorial_standard_hook_sub_eq_zero at n = 6, q = 17/13
    q_val = mp.mpf(17) / mp.mpf(13)
    n_val = 6
    lhs3 = q_factorial_geo(q_val, n_val)
    rhs3 = q_int_geo(q_val, n_val - 1) * (
        q_int_geo(q_val, n_val) * q_factorial_geo(q_val, n_val - 2) * q_int_geo(q_val, 1)
    )
    diff3 = lhs3 - rhs3
    results.append({
        "bean": "qou-po7i",
        "theorem": "QOU.BraidKnot.Keystone.qFactorial_standard_hook_sub_eq_zero",
        "n": str(n_val),
        "qFactorialN": mp.nstr(lhs3, 80),
        "hookProductRhs": mp.nstr(rhs3, 80),
        "residual": mp.nstr(abs(diff3), 80),
        "passed": abs(diff3) < mp.mpf(10) ** (-74),
    })

    # 4. qou-prop3b: neg_exp_series_concave_sub_nonneg
    c_coeffs = [mp.mpf(1), mp.mpf(3) / mp.mpf(2), mp.mpf(5) / mp.mpf(4), mp.mpf(7) / mp.mpf(8)]
    l_val = mp.mpf(3) / mp.mpf(5)
    a_val = mp.mpf(3) / mp.mpf(10)
    b_val = mp.mpf(7) / mp.mpf(10)
    p_val = mp.mpf(2)
    q_pt = mp.mpf(5)
    ap_bq = a_val * p_val + b_val * q_pt

    def neg_series(x):
        return -sum(c_coeffs[r - 1] * mp.exp(-mp.mpf(r) * l_val * x) for r in range(1, 5))

    val_mid = neg_series(ap_bq)
    val_comb = a_val * neg_series(p_val) + b_val * neg_series(q_pt)
    diff4 = val_mid - val_comb
    results.append({
        "bean": "qou-prop3b",
        "theorem": "QOU.BraidKnot.LNaturalConcaveForm.neg_exp_series_concave_sub_nonneg",
        "valAtCombo": mp.nstr(val_mid, 80),
        "comboOfVals": mp.nstr(val_comb, 80),
        "margin": mp.nstr(diff4, 80),
        "passed": diff4 > mp.mpf(0),
    })

    # 5. qou-py7e: global_of_local_boxDiffDomain_sub_nonneg on 2D box-difference domain
    # g(u, v) = -(u - 2)^2 - (v - 1)^2 - (u - v - 1)^2 on 0 <= u, v <= 4, |u - v| <= 2
    def g_func(u, v):
        return -(mp.mpf(u - 2) ** 2) - (mp.mpf(v - 1) ** 2) - (mp.mpf(u - v - 1) ** 2)

    domain_pts = [
        (u, v)
        for u in range(5)
        for v in range(5)
        if abs(u - v) <= 2
    ]
    x_opt = (2, 1)
    g_opt = g_func(*x_opt)
    min_margin = min(g_opt - g_func(u, v) for u, v in domain_pts)
    sample_y = (0, 2)
    diff5 = g_opt - g_func(*sample_y)
    results.append({
        "bean": "qou-py7e",
        "theorem": "QOU.BraidKnot.LNaturalOptimality.global_of_local_boxDiffDomain_sub_nonneg",
        "gOpt": mp.nstr(g_opt, 80),
        "gSampleY": mp.nstr(g_func(*sample_y), 80),
        "sampleMargin": mp.nstr(diff5, 80),
        "minDomainMargin": mp.nstr(min_margin, 80),
        "passed": min_margin >= mp.mpf(0) and diff5 > mp.mpf(0),
    })

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    results = run_checks()
    all_passed = all(r["passed"] for r in results)
    if not all_passed:
        raise SystemExit("One or more probe checks failed")

    payload = {
        "probe": "keyn5six_keyn5val_keystd_lnatconc_lnatopt_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/keyn5six_keyn5val_keystd_lnatconc_lnatopt_probe.py",
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
