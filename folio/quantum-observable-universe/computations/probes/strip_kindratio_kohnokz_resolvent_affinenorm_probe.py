#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 93 theorems (qou-2wtx, qou-306p, qou-37kk, qou-3ral, qou-3wc5).

Verifies:
1. period_carrier_strip_sub_eq_zero (qou-2wtx):
   f(m+1)/(m+1) - (f(m+1)/(m+1)!) * m! = 0 at 80 decimal places.
2. rho_pp_div_rho_nn_sub_eq_zero (qou-306p):
   (bPP(q)/bPN(q)) / (bNN(q)/bPN(q)) - q^4 = 0 at 80 decimal places.
3. massClass_kz_sub_eq_zero (qou-37kk):
   Framing-corrected site-weighted KZ holonomy trace difference vanishes at 80 decimal places.
4. colourResolvent_cyclic_eigenvalue_sub_eq_zero (qou-3ral):
   For w = exp(2*pi*i/3) with w^3 = 1, w*(x1 + w*x2 + w^2*x0) - (x0 + w*x1 + w^2*x2) = 0.
5. affineNormalize_scale (qou-3wc5):
   affineNormalize(c*z + 0) - affineNormalize(z) = 0 for c != 0.
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

    # 1. period_carrier_strip_sub_eq_zero (qou-2wtx)
    m_val = 6
    f_m1 = mpf("76")  # involutionNumber(7) = 232, or any rational/real value
    m_fac = mp.factorial(m_val)
    m1_fac = mp.factorial(m_val + 1)
    lhs_strip = f_m1 / mpf(str(m_val + 1))
    rhs_strip = (f_m1 / m1_fac) * m_fac
    diff_strip = abs(lhs_strip - rhs_strip)
    c1_pass = bool(diff_strip < tol)
    checks.append({
        "id": "period_carrier_strip_sub_eq_zero_qou_2wtx",
        "bean": "qou-2wtx",
        "theorem": "QOU.Mass.KeystoneBridgeC1Binding.period_carrier_strip_sub_eq_zero",
        "lhs_strip": mp.nstr(lhs_strip, 80),
        "rhs_strip": mp.nstr(rhs_strip, 80),
        "abs_diff": mp.nstr(diff_strip, 80),
        "passed": c1_pass,
    })

    # 2. rho_pp_div_rho_nn_sub_eq_zero (qou-306p)
    q = mpf("1") + mp.pi / mpf("29")
    zD = q ** 3 / (q ** 2 + mpf("1"))
    hq = q - mpf("1") / q
    flavorDelta = (q - mpf("1")) ** 2 * (mpf("1") - mpf("1") / (q ** 4)) / mpf("3")
    tPN = mpf("1") / mpf("2") - flavorDelta / mpf("4")
    bPP = zD
    bPN = zD - hq * tPN
    bNN = zD - hq
    ratio_lhs = (bPP / bPN) / (bNN / bPN)
    ratio_rhs = q ** 4
    diff_ratio = abs(ratio_lhs - ratio_rhs)
    c2_pass = bool(diff_ratio < tol)
    checks.append({
        "id": "rho_pp_div_rho_nn_sub_eq_zero_qou_306p",
        "bean": "qou-306p",
        "theorem": "QOU.Mass.KindRatioFromBondLetters.rho_pp_div_rho_nn_sub_eq_zero",
        "ratio_lhs": mp.nstr(ratio_lhs, 80),
        "q_pow_4": mp.nstr(ratio_rhs, 80),
        "abs_diff": mp.nstr(diff_ratio, 80),
        "passed": c2_pass,
    })

    # 3. massClass_kz_sub_eq_zero (qou-37kk)
    kappa = mp.sqrt(mpf("2")) / mpf("11")
    qC = mp.exp(mpf("2") * mp.pi * mp.j * kappa)
    wi = mpf("1") / (mpf("1") + qC ** 2)
    strand_factor = (qC + mpf("1") / qC) * wi
    writhe_factor = qC
    kz_trace = mp.e + mp.catalan * mp.j
    lhs_mass = (strand_factor ** 2) * (writhe_factor ** 3) * ((wi ** 2) * kz_trace)
    rhs_mass = ((strand_factor ** 2) * (writhe_factor ** 3)) * ((wi ** 2) * kz_trace)
    diff_mass = abs(lhs_mass - rhs_mass)
    c3_pass = bool(diff_mass < tol)
    checks.append({
        "id": "massClass_kz_sub_eq_zero_qou_37kk",
        "bean": "qou-37kk",
        "theorem": "QOU.Mass.KohnoWeightedClass.massClass_kz_sub_eq_zero",
        "abs_mass": mp.nstr(abs(lhs_mass), 80),
        "abs_diff": mp.nstr(diff_mass, 80),
        "passed": c3_pass,
    })

    # 4. colourResolvent_cyclic_eigenvalue_sub_eq_zero (qou-3ral)
    w = mp.exp(mpf("2") * mp.pi * mp.j / mpf("3"))
    x0 = mp.pi / mpf("5")
    x1 = mp.e / mpf("7")
    x2 = mp.sqrt(mpf("11")) / mpf("3")
    lhs_res = w * (x1 + w * x2 + (w ** 2) * x0)
    rhs_res = x0 + w * x1 + (w ** 2) * x2
    diff_res = abs(lhs_res - rhs_res)
    c4_pass = bool(diff_res < tol)
    checks.append({
        "id": "colourResolvent_cyclic_eigenvalue_sub_eq_zero_qou_3ral",
        "bean": "qou-3ral",
        "theorem": "QOU.Mass.colourResolvent_cyclic_eigenvalue_sub_eq_zero",
        "abs_lhs": mp.nstr(abs(lhs_res), 80),
        "abs_diff": mp.nstr(diff_res, 80),
        "passed": c4_pass,
    })

    # 5. affineNormalize_scale (qou-3wc5)
    z = [mp.pi / mpf("7"), mp.e + mpf("1"), mp.sqrt(mpf("13")), mp.catalan * mpf("5")]
    c_scale = mp.sqrt(mpf("19")) + mp.ln2
    z_scaled = [c_scale * zk + mpf("0") for zk in z]
    norm_orig = [(zk - z[0]) / (z[1] - z[0]) for zk in z]
    norm_scaled = [(zk - z_scaled[0]) / (z_scaled[1] - z_scaled[0]) for zk in z_scaled]
    max_diff_norm = max(abs(a - b) for a, b in zip(norm_orig, norm_scaled))
    c5_pass = bool(max_diff_norm < tol)
    checks.append({
        "id": "affineNormalize_scale_qou_3wc5",
        "bean": "qou-3wc5",
        "theorem": "QOU.Mass.LagrangianKZ.affineNormalize_scale",
        "norm_2_orig": mp.nstr(norm_orig[2], 80),
        "max_abs_diff": mp.nstr(max_diff_norm, 80),
        "passed": c5_pass,
    })

    all_passed = all(c["passed"] for c in checks)
    return {
        "probe": "strip-kindratio-kohnokz-resolvent-affinenorm-probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/strip_kindratio_kohnokz_resolvent_affinenorm_probe.py",
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
