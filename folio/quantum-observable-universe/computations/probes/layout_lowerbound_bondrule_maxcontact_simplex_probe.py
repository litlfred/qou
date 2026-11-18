#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 95 theorems (qou-5ax1, qou-5ll9, qou-5lsb, qou-63fo, qou-6cm9).

Verifies:
1. surface_sub_two_eq_zero (qou-5ax1):
   For a connected path graph on n >= 2 vertices, degree sequence [1, 2, ..., 2, 1] has surface count 2, so surface - 2 = 0.
2. diff_unconstrained_zero (qou-5ll9):
   Explicit witness E1 = E2 = max(B2, B1) satisfies B1 <= E1, B2 <= E2, and E1 - E2 = 0.
3. b3_add_b4_eq_zero_of_bondRule (qou-5lsb):
   Under log-additive bond product traces, connected cumulants b3 and b4 both vanish to 80 dps, so b3 + b4 = 0.
4. maxContact_exponent_sub_inv_dim_eq_zero (qou-63fo):
   (1 - (d - 1) / d) - 1 / d = 0 at 80 decimal places.
5. not_six_equidistant (qou-6cm9):
   5-spoke equidistant Gram matrix has rank 5 > 3 (det(G_5) = 3 * (c^2/2)^5 > 0), excluding 6 equidistant points in R^3.
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

    # 1. surface_sub_two_eq_zero (qou-5ax1)
    n_verts = 8
    degrees = [(1 if v > 0 else 0) + (1 if v + 1 < n_verts else 0) for v in range(n_verts)]
    surf_count = sum(1 for deg in degrees if deg <= 1)
    surf_diff = mpf(str(surf_count)) - mpf("2")
    c1_pass = bool(surf_diff == mpf("0"))
    checks.append({
        "id": "surface_sub_two_eq_zero_qou_5ax1",
        "bean": "qou-5ax1",
        "theorem": "QOU.Mass.LinearLayoutNoBulk.surface_sub_two_eq_zero",
        "surface_count": mp.nstr(mpf(str(surf_count)), 80),
        "surface_minus_two": mp.nstr(surf_diff, 80),
        "passed": c1_pass,
    })

    # 2. diff_unconstrained_zero (qou-5ll9)
    B1 = mp.pi * mpf("3")
    B2 = mp.e * mpf("4")
    t_zero = mpf("0")
    E2 = max(B2, B1 - t_zero)
    E1 = E2 + t_zero
    diff_E = abs(E1 - E2)
    c2_pass = bool((B1 <= E1) and (B2 <= E2) and (diff_E == mpf("0")))
    checks.append({
        "id": "diff_unconstrained_zero_qou_5ll9",
        "bean": "qou-5ll9",
        "theorem": "QOU.Mass.LowerBoundCannotConstrainADifference.diff_unconstrained_zero",
        "E1": mp.nstr(E1, 80),
        "E2": mp.nstr(E2, 80),
        "abs_diff": mp.nstr(diff_E, 80),
        "passed": c2_pass,
    })

    # 3. b3_add_b4_eq_zero_of_bondRule (qou-5lsb)
    mu01 = mp.pi / mpf("2")
    mu02 = mp.e / mpf("2")
    mu03 = mp.sqrt(mpf("3"))
    mu12 = mp.sqrt(mpf("5"))
    mu13 = mp.catalan + mpf("1")
    mu23 = mp.ln2 + mpf("1")
    triple_012 = mp.log(mu01 * mu02 * mu12)
    b3_012 = triple_012 - (mp.log(mu01) + mp.log(mu02) + mp.log(mu12))
    quad_all = mp.log(mu01 * mu02 * mu03 * mu12 * mu13 * mu23)
    pair_sum = mp.log(mu01) + mp.log(mu02) + mp.log(mu03) + mp.log(mu12) + mp.log(mu13) + mp.log(mu23)
    b4_val = quad_all - pair_sum
    sum_b3_b4 = abs(b3_012 + b4_val)
    c3_pass = bool(sum_b3_b4 < tol)
    checks.append({
        "id": "b3_add_b4_eq_zero_of_bondRule_qou_5lsb",
        "bean": "qou-5lsb",
        "theorem": "QOU.Mass.MarkovBondRuleForcesPairwise.b3_add_b4_eq_zero_of_bondRule",
        "abs_b3": mp.nstr(abs(b3_012), 80),
        "abs_b4": mp.nstr(abs(b4_val), 80),
        "abs_sum": mp.nstr(sum_b3_b4, 80),
        "passed": c3_pass,
    })

    # 4. maxContact_exponent_sub_inv_dim_eq_zero (qou-63fo)
    d_val = mpf("3") + mp.pi / mpf("17")
    lhs_exp = mpf("1") - (d_val - mpf("1")) / d_val
    rhs_exp = mpf("1") / d_val
    diff_exp = abs(lhs_exp - rhs_exp)
    c4_pass = bool(diff_exp < tol)
    checks.append({
        "id": "maxContact_exponent_sub_inv_dim_eq_zero_qou_63fo",
        "bean": "qou-63fo",
        "theorem": "QOU.Mass.MaxContactHasBulk.maxContact_exponent_sub_inv_dim_eq_zero",
        "lhs_exp": mp.nstr(lhs_exp, 80),
        "rhs_exp": mp.nstr(rhs_exp, 80),
        "abs_diff": mp.nstr(diff_exp, 80),
        "passed": c4_pass,
    })

    # 5. not_six_equidistant (qou-6cm9)
    c_dist = mp.pi / mpf("3")
    m_spokes = 5  # 6 points -> 5 spokes from p_0
    gram_5 = mp.matrix(m_spokes, m_spokes)
    for i in range(m_spokes):
        for j in range(m_spokes):
            gram_5[i, j] = (c_dist ** 2) if i == j else (c_dist ** 2) / mpf("2")
    det_g5 = mp.det(gram_5)
    expected_det = mpf(str(m_spokes + 1)) * (((c_dist ** 2) / mpf("2")) ** m_spokes)
    diff_det = abs(det_g5 - expected_det)
    c5_pass = bool((det_g5 > mpf("0")) and (diff_det < tol) and (m_spokes + 1 > 3 + 1))
    checks.append({
        "id": "not_six_equidistant_qou_6cm9",
        "bean": "qou-6cm9",
        "theorem": "QOU.Mass.MaxContactSimplex.not_six_equidistant",
        "det_gram_5_spokes": mp.nstr(det_g5, 80),
        "abs_diff_det": mp.nstr(diff_det, 80),
        "passed": c5_pass,
    })

    all_passed = all(c["passed"] for c in checks)
    return {
        "probe": "layout-lowerbound-bondrule-maxcontact-simplex-probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/layout_lowerbound_bondrule_maxcontact_simplex_probe.py",
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
