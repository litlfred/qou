#!/usr/bin/env python3
"""80-dps mpmath probe for Round 102 Mass theorems (qou-cdj8, qou-cdjd, qou-cdvx, qou-cm7l, qou-cvx9)."""

import argparse
import hashlib
import json
from pathlib import Path
from mpmath import mp

mp.dps = 80


def verify_cos_q_mul_inflection() -> dict:
    q_val = mp.mpf("3")
    k_val = mp.mpf("2")
    arg = q_val * ((mp.mpf("2") * k_val + mp.mpf("1")) * mp.pi / q_val)
    c_val = mp.cos(arg)
    residual = c_val + mp.mpf("1")
    return {
        "cosValue": mp.nstr(c_val, 80),
        "residual": mp.nstr(residual, 80),
        "passed": abs(residual) < mp.mpf("10") ** (-75),
    }


def verify_norm_exp_two_pi_i() -> dict:
    mu_re = mp.mpf("3") / mp.mpf("7")
    mu_im = -mp.mpf("2") / mp.mpf("5")
    mu_val = mp.mpc(mu_re, mu_im)
    lhs = abs(mp.exp(mp.mpf("2") * mp.pi * mp.mpc("0", "1") * mu_val))
    rhs = mp.exp(-(mp.mpf("2") * mp.pi * mu_im))
    diff = lhs - rhs
    return {
        "normExp": mp.nstr(lhs, 80),
        "realExp": mp.nstr(rhs, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_cross_sum_sub() -> dict:
    g_p, g_n = mp.mpf("11") / mp.mpf("3"), mp.mpf("5") / mp.mpf("2")
    k_p, k_n = mp.mpf("7") / mp.mpf("4"), mp.mpf("13") / mp.mpf("6")
    f_pn = g_p + k_n
    f_np = g_n + k_p
    f_pp = g_p + k_p
    f_nn = g_n + k_n
    diff = (f_pn + f_np) - (f_pp + f_nn)
    return {
        "crossSum": mp.nstr(f_pn + f_np, 80),
        "diagSum": mp.nstr(f_pp + f_nn, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_two_row_catalan() -> dict:
    # For n = 6, Catalan C_6 = 132, two-row ballot numbers f(6,k) for k=0..3: 1, 5, 9, 5 -> 1+25+81+25 = 132
    n_val = 6
    sq_sum = mp.mpf("0")
    for k in range(n_val // 2 + 1):
        c_nk = mp.binomial(n_val, k)
        c_nk1 = mp.mpf("0") if k == 0 else mp.binomial(n_val, k - 1)
        f_nk = c_nk - c_nk1
        sq_sum += f_nk ** 2
    cat_n = mp.binomial(2 * n_val, n_val) / mp.mpf(str(n_val + 1))
    diff = sq_sum - cat_n
    return {
        "sqSum": mp.nstr(sq_sum, 80),
        "catalan": mp.nstr(cat_n, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_symmetry_curvature_ne_zero() -> dict:
    bpp = mp.mpf("3") / mp.mpf("2")
    bnn = mp.mpf("5") / mp.mpf("2")
    bpn = (bpp + bnn) / mp.mpf("2") + mp.mpf("1") / mp.mpf("10")
    curv = (-mp.log(bpp)) + (-mp.log(bnn)) - mp.mpf("2") * (-mp.log(bpn))
    return {
        "curvature": mp.nstr(curv, 80),
        "passed": curv > mp.mpf("0"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    c1 = verify_cos_q_mul_inflection()
    c2 = verify_norm_exp_two_pi_i()
    c3 = verify_cross_sum_sub()
    c4 = verify_two_row_catalan()
    c5 = verify_symmetry_curvature_ne_zero()

    all_passed = all(x["passed"] for x in (c1, c2, c3, c4, c5))
    payload = {
        "probe": "torusinfl_twisted_twobody_tworow_uiccurv_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/torusinfl_twisted_twobody_tworow_uiccurv_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": int(mp.dps),
        "allPassed": all_passed,
        "checks": {
            "cosQMulInflectionAddOneEqZero": c1,
            "normExpTwoPiIMulSubEqZero": c2,
            "crossSumSubEqZero": c3,
            "twoRowSumSqSubCatalanEqZero": c4,
            "symmetryCurvatureNeZero": c5,
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
