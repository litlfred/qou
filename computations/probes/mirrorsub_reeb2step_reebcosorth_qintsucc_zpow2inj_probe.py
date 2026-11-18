#!/usr/bin/env python3
"""80-dps mpmath probe for Round 80 theorems (r18k, t886, uer8, xbz0, qou-yuyz).

Checks:
1. binding_formula_sub_of_same_re (r18k): A*Im(V41(u1)) - A*Im(V41(u2)) == A*cuspModulus*(u2.im^2 - u1.im^2) for u1.re == u2.re at 80 dps.
2. reeb_tower_sinh_two_step (t886): sinh(a + 2*eta) + sinh(a - 2*eta) == (4*cosh(eta)^2 - 2)*sinh(a) at 80 dps.
3. reebCos_dim_sq_weighted_sum_zero (uer8): sum_{l in A5} dim(l)^2 * reebCos(l) == 0 at 80 dps.
4. qInt_succ (xbz0): (q^(n+1) - 1)/(q - 1) == q * (q^n - 1)/(q - 1) + 1 at 80 dps.
5. zpow_two_mul_injective_of_not_root_of_unity (qou-yuyz): log(q^(2*a)) / (2*log(q)) == a at 80 dps.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from mpmath import mp

mp.dps = 80


def run_checks() -> dict:
    tol = mp.mpf("1e-75")

    # 1. r18k: binding_formula_sub_of_same_re
    a_val = mp.mpf("3")
    cusp_mod = mp.sqrt(mp.mpf("3")) / mp.mpf("4")
    re_shared = mp.mpf("7") / mp.mpf("13")
    im1 = mp.mpf("5") / mp.mpf("11")
    im2 = mp.mpf("9") / mp.mpf("17")
    v1_im = cusp_mod * ((re_shared ** 2) - (im1 ** 2))
    v2_im = cusp_mod * ((re_shared ** 2) - (im2 ** 2))
    lhs1 = a_val * v1_im - a_val * v2_im
    rhs1 = a_val * cusp_mod * ((im2 ** 2) - (im1 ** 2))
    c1_res = abs(lhs1 - rhs1)
    c1_pass = bool(c1_res < tol)

    # 2. t886: reeb_tower_sinh_two_step
    a_arg = mp.mpf("19") / mp.mpf("23")
    eta_arg = mp.mpf("3") / mp.mpf("7")
    lhs2 = mp.sinh(a_arg + mp.mpf("2") * eta_arg) + mp.sinh(a_arg - mp.mpf("2") * eta_arg)
    rhs2 = (mp.mpf("4") * (mp.cosh(eta_arg) ** 2) - mp.mpf("2")) * mp.sinh(a_arg)
    c2_res = abs(lhs2 - rhs2)
    c2_pass = bool(c2_res < tol)

    # 3. uer8: reebCos_dim_sq_weighted_sum_zero
    s5 = mp.sqrt(mp.mpf("5"))
    cos_a = mp.mpf("1")
    cos_t1 = (mp.mpf("1") + s5) / mp.mpf("6")
    cos_t2 = (mp.mpf("1") - s5) / mp.mpf("6")
    cos_g = -mp.mpf("1") / mp.mpf("4")
    cos_h = mp.mpf("0")
    weighted_sum = (
        (mp.mpf("1") ** 2) * cos_a
        + (mp.mpf("3") ** 2) * cos_t1
        + (mp.mpf("3") ** 2) * cos_t2
        + (mp.mpf("4") ** 2) * cos_g
        + (mp.mpf("5") ** 2) * cos_h
    )
    c3_res = abs(weighted_sum)
    c3_pass = bool(c3_res < tol)

    # 4. xbz0: qInt_succ
    q_val = mp.mpf("37") / mp.mpf("31")
    n_val = 7
    qint_n = ((q_val ** n_val) - mp.mpf("1")) / (q_val - mp.mpf("1"))
    qint_n1 = ((q_val ** (n_val + 1)) - mp.mpf("1")) / (q_val - mp.mpf("1"))
    c4_res = abs(qint_n1 - (q_val * qint_n + mp.mpf("1")))
    c4_pass = bool(c4_res < tol)

    # 5. qou-yuyz: zpow_two_mul_injective_of_not_root_of_unity
    a_exp = mp.mpf("9")
    eig_val = q_val ** (mp.mpf("2") * a_exp)
    recovered_a = mp.log(eig_val) / (mp.mpf("2") * mp.log(q_val))
    c5_res = abs(recovered_a - a_exp)
    c5_pass = bool(c5_res < tol)

    checks = [
        {"id": "r18k_binding_formula_sub_of_same_re", "residual": mp.nstr(c1_res, 25), "passed": c1_pass},
        {"id": "t886_reeb_tower_sinh_two_step", "residual": mp.nstr(c2_res, 25), "passed": c2_pass},
        {"id": "uer8_reebCos_dim_sq_weighted_sum_zero", "residual": mp.nstr(c3_res, 25), "passed": c3_pass},
        {"id": "xbz0_qInt_succ", "residual": mp.nstr(c4_res, 25), "passed": c4_pass},
        {"id": "qou_yuyz_zpow_two_mul_injective", "residual": mp.nstr(c5_res, 25), "passed": c5_pass},
    ]
    return {
        "dps": 80,
        "allPassed": all(c["passed"] for c in checks),
        "checks": checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", default="0000000000000000000000000000000000000000")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    res = run_checks()
    payload = {
        "probe": "computations/probes/mirrorsub_reeb2step_reebcosorth_qintsucc_zpow2inj_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_hash,
        "dps": res["dps"],
        "allPassed": res["allPassed"],
        "checks": res["checks"],
    }
    out_text = json.dumps(payload, indent=2) + "\n"
    if args.out:
        Path(args.out).write_text(out_text, encoding="utf-8")
    else:
        print(out_text, end="")


if __name__ == "__main__":
    main()
