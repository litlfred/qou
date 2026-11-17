#!/usr/bin/env python3
"""80-dps mpmath probe for Round 79 theorems (qou-vdvE, qou-w49j, qou-xapv, qou-zcjg, thb7).

Checks:
1. cSigma_pow_four_mul_sq_abs_cot_div_two (qou-vdvE): cSigma(5*pi/6)^4 * (|cot(5*pi/6)|/2)^2 == 1/4 at 80 dps.
2. s_channel_eq_zero_of_sq_eq (qou-w49j): A_omega * cuspModulus * (log(q0)^2 - theta^2) == 0 at theta^2 = log(q0)^2 at 80 dps.
3. ArchimedeanMassIdentity.weighted_integrand_nonneg (qou-xapv): u(p) * (grad(p) * levi(p)) >= 0 for u(p) >= 0 and integrand >= 0 at 80 dps.
4. rossmann_cc_double_even_eq_dim_add_target (qou-zcjg): 2 * e == dim + target for single-parity (e, o) at 80 dps.
5. cube_lever_static_recovery (thb7): u^3 * (f'/u^3 - 3*(u'/u)*(f/u^3)) + 3*(u'/u)*f == f' at 80 dps.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from mpmath import mp

mp.dps = 80


def c_sigma(theta: mp.mpf) -> mp.mpf:
    return (mp.mpf("2") * mp.sin(theta)) / mp.sqrt(abs(mp.cos(theta) / mp.sin(theta)))


def run_checks() -> dict:
    tol = mp.mpf("1e-75")

    # 1. qou-vdvE: cSigma_pow_four_mul_sq_abs_cot_div_two
    theta_sad = (mp.mpf("5") * mp.pi) / mp.mpf("6")
    cs_val = c_sigma(theta_sad)
    cot_half = abs(mp.cos(theta_sad) / mp.sin(theta_sad)) / mp.mpf("2")
    c1_res = abs((cs_val ** 4) * (cot_half ** 2) - (mp.mpf("1") / mp.mpf("4")))
    c1_pass = bool(c1_res < tol)

    # 2. qou-w49j: s_channel_eq_zero_of_sq_eq
    a_omega = mp.mpf("3")
    cusp_mod = mp.sqrt(mp.mpf("3")) / mp.mpf("4")
    q0 = mp.mpf("11") / mp.mpf("10")
    ln_q0 = mp.log(q0)
    theta_crit = -ln_q0
    s_val = a_omega * cusp_mod * ((ln_q0 ** 2) - (theta_crit ** 2))
    c2_res = abs(s_val)
    c2_pass = bool(c2_res < tol)

    # 3. qou-xapv: weighted_integrand_nonneg
    u_p = mp.mpf("17") / mp.mpf("13")
    grad_p = mp.mpf("5") / mp.mpf("7")
    levi_p = mp.mpf("11") / mp.mpf("3")
    weighted_val = u_p * (grad_p * levi_p)
    c3_res = abs(weighted_val - (mp.mpf("935") / mp.mpf("273")))
    c3_pass = bool(c3_res < tol and weighted_val >= mp.mpf("0"))

    # 4. qou-zcjg: rossmann_cc_double_even_eq_dim_add_target
    e_deg = mp.mpf("6")
    o_deg = mp.mpf("0")
    dim_val = e_deg + o_deg
    target_val = e_deg - o_deg
    c4_res = abs(mp.mpf("2") * e_deg - (dim_val + target_val))
    c4_pass = bool(c4_res < tol)

    # 5. thb7: cube_lever_static_recovery
    f_val = mp.mpf("29") / mp.mpf("11")
    f_prime = mp.mpf("237") / mp.mpf("100")
    u_val = mp.mpf("19") / mp.mpf("7")
    u_prime = -mp.mpf("5") / mp.mpf("9")
    lever_slope = (f_prime / (u_val ** 3)) - mp.mpf("3") * (u_prime / u_val) * (f_val / (u_val ** 3))
    recovered_fp = (u_val ** 3) * lever_slope + mp.mpf("3") * (u_prime / u_val) * f_val
    c5_res = abs(recovered_fp - f_prime)
    c5_pass = bool(c5_res < tol)

    checks = [
        {"id": "qou_vdvE_cSigma_pow_four_mul_sq_abs_cot_div_two", "residual": mp.nstr(c1_res, 25), "passed": c1_pass},
        {"id": "qou_w49j_s_channel_eq_zero_of_sq_eq", "residual": mp.nstr(c2_res, 25), "passed": c2_pass},
        {"id": "qou_xapv_weighted_integrand_nonneg", "residual": mp.nstr(c3_res, 25), "passed": c3_pass},
        {"id": "qou_zcjg_rossmann_cc_double_even_eq_dim_add_target", "residual": mp.nstr(c4_res, 25), "passed": c4_pass},
        {"id": "thb7_cube_lever_static_recovery", "residual": mp.nstr(c5_res, 25), "passed": c5_pass},
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
        "probe": "computations/probes/csigma4_t5crit_massnonneg_rossmanneven_leverrec_probe.py",
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
