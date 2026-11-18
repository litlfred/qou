#!/usr/bin/env python3
"""80-dps mpmath probe for Round 87 theorems (qou-ontj, qou-rx2u, qou-sa60, qou-zrbv, qou-v2om)."""
import hashlib
import json
import os
import sys
from mpmath import mp, mpf

mp.dps = 80


def verify_all():
    results = {}
    tol = mpf("1e-75")

    # 1. qou-ontj: isoformalDim_two_slope_ne_zero
    # For r0, r1 > 0 and mu0 < mu1, rszIsoformalDim = r0*r1*(mu1 - mu0) != 0
    r0, r1 = mpf("3"), mpf("5")
    mu0, mu1 = mpf("-2"), mpf("7")
    iso_dim = r0 * r1 * (mu1 - mu0)
    results["isoformalDim_two_slope_ne_zero"] = {
        "r0": mp.nstr(r0, 80),
        "r1": mp.nstr(r1, 80),
        "mu0": mp.nstr(mu0, 80),
        "mu1": mp.nstr(mu1, 80),
        "isoformalDim": mp.nstr(iso_dim, 80),
        "passed": bool(iso_dim > mpf("0") and iso_dim != mpf("0")),
    }

    # 2. qou-rx2u: mubar_common_weight_diff
    # channel(m) = w * S(m) with S(2) = 1 => channel(m) - channel(k) = (S(m) - S(k)) * channel(2)
    w = mp.pi / mpf("7")
    S_map = {2: mpf("1"), 5: mpf("11"), 8: mpf("29")}
    ch2 = w * S_map[2]
    ch5 = w * S_map[5]
    ch8 = w * S_map[8]
    lhs_diff = ch8 - ch5
    rhs_diff = (S_map[8] - S_map[5]) * ch2
    res_diff = abs(lhs_diff - rhs_diff)
    results["mubar_common_weight_diff"] = {
        "lhs": mp.nstr(lhs_diff, 80),
        "rhs": mp.nstr(rhs_diff, 80),
        "residual": mp.nstr(res_diff, 80),
        "passed": bool(res_diff < tol),
    }

    # 3. qou-sa60: abs_sum_le_zero_of_le_zero
    # For all i in s, |a_i| <= 0 => |sum a_i| <= 0
    terms = [mpf("0"), mpf("0"), mpf("0"), mpf("0")]
    abs_sum = abs(sum(terms, mpf("0")))
    results["abs_sum_le_zero_of_le_zero"] = {
        "abs_sum": mp.nstr(abs_sum, 80),
        "passed": bool(abs_sum <= mpf("0") and abs_sum == mpf("0")),
    }

    # 4. qou-zrbv: chargeIndependent_eq_pairs
    # Under OneBody f: f(x,y) = (f(x,x) + f(y,y))/2 and f(p,p) = f(n,n) = v0
    v0 = mp.sqrt(mpf("19")) / mpf("3")
    diag = {"p": v0, "n": v0}
    pairs = [("p", "p"), ("p", "n"), ("n", "p"), ("n", "n")]
    evals = [(diag[a] + diag[b]) / mpf("2") for (a, b) in pairs]
    max_spread = max(abs(x - y) for x in evals for y in evals)
    results["chargeIndependent_eq_pairs"] = {
        "v0": mp.nstr(v0, 80),
        "max_pair_spread": mp.nstr(max_spread, 80),
        "passed": bool(max_spread < tol),
    }

    # 5. qou-v2om: qbeta_proxy_mul_two_eq_E0_h_two_sub_h
    # 2 * QbetaProxy(q) = E0(q) * hOf(q) * (2 - hOf(q))
    q = mpf("17") / mpf("11")
    E0_q = (q - mpf("1")) ** 2 / q
    h_q = (q - mpf("1")) / q
    qbeta_q = ((q - mpf("1")) ** 3 * (q + mpf("1"))) / (mpf("2") * (q ** 3))
    lhs_qbeta = mpf("2") * qbeta_q
    rhs_qbeta = E0_q * h_q * (mpf("2") - h_q)
    res_qbeta = abs(lhs_qbeta - rhs_qbeta)
    results["qbeta_proxy_mul_two_eq_E0_h_two_sub_h"] = {
        "q": mp.nstr(q, 80),
        "lhs": mp.nstr(lhs_qbeta, 80),
        "rhs": mp.nstr(rhs_qbeta, 80),
        "residual": mp.nstr(res_qbeta, 80),
        "passed": bool(res_qbeta < tol),
    }

    all_passed = all(v["passed"] for v in results.values())
    script_bytes = open(os.path.abspath(__file__), "rb").read()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    commit_sha = os.environ.get("SCRIPT_COMMIT_SHA", "0" * 40)
    payload = {
        "probe": "noalien_mubardiff_multzero_onebodyeq_qbetamul2_probe",
        "beans": ["qou-ontj", "qou-rx2u", "qou-sa60", "qou-zrbv", "qou-v2om"],
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
