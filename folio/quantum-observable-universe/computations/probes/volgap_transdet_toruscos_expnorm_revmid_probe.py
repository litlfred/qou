#!/usr/bin/env python3
"""80-dps mpmath probe for Round 89 theorems (qou-8lxd, qou-dap4, qou-g7f6, qou-hok7, qou-i5d7)."""
import hashlib
import json
import os
import sys
from mpmath import mp, mpf, mpc

mp.dps = 80


def verify_all():
    results = {}
    tol = mpf("1e-75")

    # 1. qou-8lxd: volume_gap_pos
    aV = mpf("158") / mpf("10")
    aS = mpf("183") / mpf("10")
    aC = mpf("714") / mpf("1000")
    u = mpf("4")
    per_nuc = aV - (aS / u) - aC * (u ** 2)
    gap = aV - per_nuc
    results["volume_gap_pos"] = {
        "aV": mp.nstr(aV, 80),
        "perNucleon": mp.nstr(per_nuc, 80),
        "gap": mp.nstr(gap, 80),
        "passed": bool(gap > mpf("0")),
    }

    # 2. qou-dap4: transfer_det_neg
    t = mp.pi / mpf("3")
    det_pos = (t * mpf("0")) - (mpf("-1") * mpf("1"))
    det_neg = ((-t) * mpf("0")) - (mpf("-1") * mpf("1"))
    res_det = abs(det_neg - det_pos)
    results["transfer_det_neg"] = {
        "det_pos": mp.nstr(det_pos, 80),
        "det_neg": mp.nstr(det_neg, 80),
        "residual": mp.nstr(res_det, 80),
        "passed": bool(res_det == mpf("0") and det_pos == mpf("1")),
    }

    # 3. qou-g7f6: cos_q_mul_inflection_zero
    q = mpf("5")
    arg = q * ((mpf("2") * mpf("0") + mpf("1")) * mp.pi / q)
    val_cos = mp.cos(arg)
    res_cos = abs(val_cos - mpf("-1"))
    results["cos_q_mul_inflection_zero"] = {
        "q": mp.nstr(q, 80),
        "cos_val": mp.nstr(val_cos, 80),
        "residual": mp.nstr(res_cos, 80),
        "passed": bool(res_cos < tol),
    }

    # 4. qou-hok7: norm_exp_two_pi_I_mul_zero_im
    mu = mpc(mp.sqrt(mpf("7")) / mpf("3"), mpf("0"))
    z = mp.exp(mpf("2") * mp.pi * mpc(mpf("0"), mpf("1")) * mu)
    norm_z = abs(z)
    res_norm = abs(norm_z - mpf("1"))
    results["norm_exp_two_pi_I_mul_zero_im"] = {
        "norm_z": mp.nstr(norm_z, 80),
        "residual": mp.nstr(res_norm, 80),
        "passed": bool(res_norm < tol),
    }

    # 5. qou-i5d7: exchangeSymmetric_reverse_midpoint
    # Additively separable f(a,b) = g(a) + k(b) with f(p,n) = f(n,p) <=> g(p)-k(p) = g(n)-k(n) = c
    c_shift = mp.sqrt(mpf("3"))
    kp = mp.sqrt(mpf("5"))
    kn = mp.sqrt(mpf("11"))
    gp = kp + c_shift
    gn = kn + c_shift
    f_pp = gp + kp
    f_nn = gn + kn
    f_np = gn + kp
    lhs_mid = f_np + f_np
    rhs_mid = f_pp + f_nn
    res_mid = abs(lhs_mid - rhs_mid)
    results["exchangeSymmetric_reverse_midpoint"] = {
        "lhs": mp.nstr(lhs_mid, 80),
        "rhs": mp.nstr(rhs_mid, 80),
        "residual": mp.nstr(res_mid, 80),
        "passed": bool(res_mid < tol),
    }

    all_passed = all(v["passed"] for v in results.values())
    script_bytes = open(os.path.abspath(__file__), "rb").read()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    commit_sha = os.environ.get("SCRIPT_COMMIT_SHA", "0" * 40)
    payload = {
        "probe": "volgap_transdet_toruscos_expnorm_revmid_probe",
        "beans": ["qou-8lxd", "qou-dap4", "qou-g7f6", "qou-hok7", "qou-i5d7"],
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
