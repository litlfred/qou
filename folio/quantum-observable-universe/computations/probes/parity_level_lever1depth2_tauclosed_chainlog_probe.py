#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 94 theorems (qou-3x8x, qou-4h26, qou-4kc0, qou-4r5y, qou-4un2).

Verifies:
1. dim_3_add_dim_21 (qou-3x8x):
   hookDim(3, [3,2,1]) + hookDim(3, [3,1,1]) = 1 + 2 = 3.
2. linear_selection_bound_at_threshold (qou-4h26):
   At k0 = 3 with c * r^k0 <= w(k0) <= M * k0, c * r^k0 <= M * k0.
3. depth2_no_zero_tau (qou-4kc0):
   At tau = 0, lwCl(3) = 5/2 != 0*lwCl(2) - lwCl(1) = -1, and residual for constant-tau is -7/240 != 0.
4. tau_kernel_closed_form_sub_eq_zero (qou-4r5y):
   (1 + (3q^2 + 4 + 3/q^2)/4) / ((q+1)^2 / (3q)) - 3(3q^4 + 8q^2 + 3)/(4q(q+1)^2) = 0 at 80 dps.
5. log_chainRatio_succ_neutron_sub_eq_zero (qou-4un2):
   log(chainRatio(Z, N+1)) - (log(chainRatio(Z, N)) + log(fnn)) = 0 at 80 dps.
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

    # 1. dim_3_add_dim_21 (qou-3x8x)
    fact3 = mp.factorial(3)
    dim_3 = fact3 / (mpf("3") * mpf("2") * mpf("1"))
    dim_21 = fact3 / (mpf("3") * mpf("1") * mpf("1"))
    sum_dims = dim_3 + dim_21
    diff_dims = abs(sum_dims - mpf("3"))
    c1_pass = bool(diff_dims == mpf("0"))
    checks.append({
        "id": "dim_3_add_dim_21_qou_3x8x",
        "bean": "qou-3x8x",
        "theorem": "QOU.Mass.ParitySplit.dim_3_add_dim_21",
        "dim_3": mp.nstr(dim_3, 80),
        "dim_21": mp.nstr(dim_21, 80),
        "sum_dims": mp.nstr(sum_dims, 80),
        "passed": c1_pass,
    })

    # 2. linear_selection_bound_at_threshold (qou-4h26)
    k0 = mpf("3")
    c_val = mp.pi / mpf("11")
    r_val = mpf("1") + mp.e / mpf("7")
    geom_k0 = c_val * (r_val ** k0)
    w_k0 = geom_k0 + mp.catalan
    M_val = (w_k0 + mp.ln2) / k0
    ext_k0 = M_val * k0
    gap_k0 = ext_k0 - geom_k0
    c2_pass = bool((geom_k0 <= w_k0) and (w_k0 <= ext_k0) and (geom_k0 <= ext_k0) and (gap_k0 > mpf("0")))
    checks.append({
        "id": "linear_selection_bound_at_threshold_qou_4h26",
        "bean": "qou-4h26",
        "theorem": "QOU.Mass.LevelSelection.linear_selection_bound_at_threshold",
        "geom_k0": mp.nstr(geom_k0, 80),
        "ext_k0": mp.nstr(ext_k0, 80),
        "gap_k0": mp.nstr(gap_k0, 80),
        "passed": c2_pass,
    })

    # 3. depth2_no_zero_tau (qou-4kc0)
    lw1 = mpf("2") / mpf("2")
    lw2 = mpf("4") / mpf("3")
    lw3 = mpf("10") / mpf("4")
    lw4 = mpf("26") / mpf("5")
    zero_tau_gap3 = abs(lw3 - (mpf("0") * lw2 - lw1))
    tau_seed = (lw3 + lw1) / lw2
    residual_c4 = lw4 - (tau_seed * lw3 - lw2)
    expected_res = -mpf("7") / mpf("240")
    c3_pass = bool((zero_tau_gap3 > mpf("3")) and (abs(residual_c4 - expected_res) < tol))
    checks.append({
        "id": "depth2_no_zero_tau_qou_4kc0",
        "bean": "qou-4kc0",
        "theorem": "QOU.Mass.Lever1Depth2.depth2_no_zero_tau",
        "zero_tau_gap3": mp.nstr(zero_tau_gap3, 80),
        "seed_residual_c4": mp.nstr(residual_c4, 80),
        "passed": c3_pass,
    })

    # 4. tau_kernel_closed_form_sub_eq_zero (qou-4r5y)
    q = mpf("1") + mp.pi / mpf("29")
    aD2 = mpf("1")
    aD3 = ((q + mpf("1")) ** 2) / (mpf("3") * q)
    aD4 = (mpf("3") * (q ** 2) + mpf("4") + mpf("3") / (q ** 2)) / mpf("4")
    lhs_tau = (aD2 + aD4) / aD3
    rhs_tau = mpf("3") * (mpf("3") * (q ** 4) + mpf("8") * (q ** 2) + mpf("3")) / (mpf("4") * q * ((q + mpf("1")) ** 2))
    diff_tau = abs(lhs_tau - rhs_tau)
    c4_pass = bool(diff_tau < tol)
    checks.append({
        "id": "tau_kernel_closed_form_sub_eq_zero_qou_4r5y",
        "bean": "qou-4r5y",
        "theorem": "QOU.Mass.Lever1Tau.tau_kernel_closed_form_sub_eq_zero",
        "lhs_tau": mp.nstr(lhs_tau, 80),
        "rhs_tau": mp.nstr(rhs_tau, 80),
        "abs_diff": mp.nstr(diff_tau, 80),
        "passed": c4_pass,
    })

    # 5. log_chainRatio_succ_neutron_sub_eq_zero (qou-4un2)
    Z_val = 3
    N_val = 4
    fpp = mpf("1") + mp.pi / mpf("13")
    fpn = mpf("1") + mp.e / mpf("11")
    fnn = mpf("1") + mp.sqrt(mpf("5")) / mpf("9")
    ratio_N = (fpp ** (Z_val - 1)) * fpn * (fnn ** (N_val - 1))
    ratio_N1 = (fpp ** (Z_val - 1)) * fpn * (fnn ** N_val)
    diff_log = abs(mp.log(ratio_N1) - (mp.log(ratio_N) + mp.log(fnn)))
    c5_pass = bool(diff_log < tol)
    checks.append({
        "id": "log_chainRatio_succ_neutron_sub_eq_zero_qou_4un2",
        "bean": "qou-4un2",
        "theorem": "QOU.Mass.LinearChainBond.log_chainRatio_succ_neutron_sub_eq_zero",
        "log_ratio_N1": mp.nstr(mp.log(ratio_N1), 80),
        "abs_diff": mp.nstr(diff_log, 80),
        "passed": c5_pass,
    })

    all_passed = all(c["passed"] for c in checks)
    return {
        "probe": "parity-level-lever1depth2-tauclosed-chainlog-probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/parity_level_lever1depth2_tauclosed_chainlog_probe.py",
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
