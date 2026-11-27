#!/usr/bin/env python3
"""80-dps mpmath probe for Round 78 theorems (kl2o, qou-jfx8, qou-upbq, qou-v4in, qou-yb2b).

Checks:
1. nzReVolume_add_phase_neg (kl2o): nzReVolume(r, phi) + nzReVolume(r, -phi) == 0 at 80 dps.
2. bindingForm_self_eq_zero (qou-jfx8): -alpha * log(trM(a) / trM(a)) == 0 at 80 dps.
3. simplex_tetrahedron_coeff_inversion (qou-upbq): M(4) - 4*M(3) + 6*M(2) == mu_4 at 80 dps.
4. trace_three_step_from_two_step (qou-v4in): tr(M^(n+3)) == (t^2 - d)*tr(M^(n+1)) - t*d*tr(M^n) at 80 dps.
5. CuspShape.meridianShear_comp_re_add_im (qou-yb2b): ((re + s1) + s2) + im == (re + (s1 + s2)) + im at 80 dps.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from mpmath import mp

mp.dps = 80


def nz_re_volume(r: mp.mpf, phi: mp.mpf) -> mp.mpf:
    return -((mp.sqrt(mp.mpf("3")) / mp.mpf("2")) * (r ** 2) * mp.sin(mp.mpf("2") * phi))


def run_checks() -> dict:
    tol = mp.mpf("1e-75")

    # 1. kl2o: nzReVolume_add_phase_neg
    r_val = mp.mpf("7") / mp.mpf("5")
    phi_val = mp.pi / mp.mpf("7")
    c1_res = abs(nz_re_volume(r_val, phi_val) + nz_re_volume(r_val, -phi_val))
    c1_pass = bool(c1_res < tol)

    # 2. qou-jfx8: bindingForm_self_eq_zero
    alpha_val = mp.mpf("1") / mp.mpf("137")
    tr_a = mp.mpf("19") / mp.mpf("11")
    c2_res = abs(-alpha_val * mp.log(tr_a / tr_a))
    c2_pass = bool(c2_res < tol)

    # 3. qou-upbq: simplex_tetrahedron_coeff_inversion
    mu2 = mp.mpf("0")
    mu3 = mp.mpf("4708") / mp.mpf("10000")
    mu4 = -mp.mpf("4591") / mp.mpf("1000")
    s_a2 = mu2 * mp.mpf("1") + mu3 * mp.mpf("0") + mu4 * mp.mpf("0")
    s_a3 = mu2 * mp.mpf("3") + mu3 * mp.mpf("1") + mu4 * mp.mpf("0")
    s_a4 = mu2 * mp.mpf("6") + mu3 * mp.mpf("4") + mu4 * mp.mpf("1")
    inv_mu4 = s_a4 - mp.mpf("4") * s_a3 + mp.mpf("6") * s_a2
    c3_res = abs(inv_mu4 - mu4)
    c3_pass = bool(c3_res < tol)

    # 4. qou-v4in: trace_three_step_from_two_step for 2x2 matrix M
    m00 = mp.mpf("5") / mp.mpf("3")
    m01 = mp.mpf("2") / mp.mpf("7")
    m10 = -mp.mpf("3") / mp.mpf("5")
    m11 = mp.mpf("11") / mp.mpf("13")
    t_val = m00 + m11
    d_val = m00 * m11 - m01 * m10

    def mat_mul(a, b):
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
        ]

    def mat_tr(a):
        return a[0][0] + a[1][1]

    m1 = [[m00, m01], [m10, m11]]
    m2 = mat_mul(m1, m1)
    m3 = mat_mul(m2, m1)
    m4 = mat_mul(m3, m1)
    lhs_tr = mat_tr(m4)
    rhs_tr = (t_val ** 2 - d_val) * mat_tr(m2) - t_val * d_val * mat_tr(m1)
    c4_res = abs(lhs_tr - rhs_tr)
    c4_pass = bool(c4_res < tol)

    # 5. qou-yb2b: CuspShape.meridianShear_comp_re_add_im
    re_val = mp.mpf("1") / mp.mpf("2")
    im_val = mp.sqrt(mp.mpf("3")) / mp.mpf("2")
    s1_val = mp.mpf("3") / mp.mpf("11")
    s2_val = -mp.mpf("5") / mp.mpf("17")
    lhs_shear = ((re_val + s1_val) + s2_val) + im_val
    rhs_shear = (re_val + (s1_val + s2_val)) + im_val
    c5_res = abs(lhs_shear - rhs_shear)
    c5_pass = bool(c5_res < tol)

    checks = [
        {"id": "kl2o_nzReVolume_add_phase_neg", "residual": mp.nstr(c1_res, 25), "passed": c1_pass},
        {"id": "qou_jfx8_bindingForm_self_eq_zero", "residual": mp.nstr(c2_res, 25), "passed": c2_pass},
        {"id": "qou_upbq_simplex_tetrahedron_coeff_inversion", "residual": mp.nstr(c3_res, 25), "passed": c3_pass},
        {"id": "qou_v4in_trace_three_step_from_two_step", "residual": mp.nstr(c4_res, 25), "passed": c4_pass},
        {"id": "qou_yb2b_meridianShear_comp_re_add_im", "residual": mp.nstr(c5_res, 25), "passed": c5_pass},
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
        "probe": "computations/probes/nzvol_blockself_simplexinv_threestep_meridianshear_probe.py",
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
