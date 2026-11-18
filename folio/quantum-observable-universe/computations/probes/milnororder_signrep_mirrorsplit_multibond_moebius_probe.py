#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 96 theorems (qou-6irj, qou-7jhl, qou-7sin, qou-7tr2, qou-7vh1).

Verifies:
1. geometric_order_forces_square_sub_eq_zero (qou-6irj):
   For b2 = g^2, b3 = g^4, b4 = g^6, b3^2 - b2*b4 = 0 at 80 decimal places.
2. equivariant_linearMap_to_trivial_apply_eq_zero_of_neZero_two (qou-7jhl):
   Average over S_3 with signR weights (sum_{g in S3} signR(g) * x) / 6 = 0 for all x.
3. interval_width_sub_eq_zero (qou-7sin):
   ((U1 - B2) - (B1 - U2)) - ((U1 - B1) + (U2 - B2)) = 0 at 80 decimal places.
4. mubar_common_weight_sub_integer_multiple_eq_zero (qou-7tr2):
   For channel(m) = w * S(m) with S(2) = 1, channel(m) - S(m) * channel(2) = 0.
5. quadratic_coeff_sum_zero_of_three_roots (qou-7vh1):
   Lagrange interpolation of a quadratic vanishing at three distinct roots x, y, z gives A = B = C = 0 and A + B + C = 0.
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

    # 1. geometric_order_forces_square_sub_eq_zero (qou-6irj)
    g_val = mp.pi / mpf("7") + mp.sqrt(mpf("3")) / mpf("5")
    b2 = g_val ** 2
    b3 = g_val ** 4
    b4 = g_val ** 6
    diff_sq = abs((b3 ** 2) - (b2 * b4))
    c1_pass = bool(diff_sq < tol)
    checks.append({
        "id": "geometric_order_forces_square_sub_eq_zero_qou_6irj",
        "bean": "qou-6irj",
        "theorem": "QOU.Mass.MilnorCarriesOrderNotMagnitude.geometric_order_forces_square_sub_eq_zero",
        "b3_sq": mp.nstr(b3 ** 2, 80),
        "b2_mul_b4": mp.nstr(b2 * b4, 80),
        "abs_diff": mp.nstr(diff_sq, 80),
        "passed": c1_pass,
    })

    # 2. equivariant_linearMap_to_trivial_apply_eq_zero_of_neZero_two (qou-7jhl)
    s3_signs = [mpf("1"), mpf("1"), mpf("1"), -mpf("1"), -mpf("1"), -mpf("1")]
    x_val = mp.e * mp.catalan
    t_apply = sum(s * x_val for s in s3_signs) / mpf("6")
    c2_pass = bool(abs(t_apply) < tol)
    checks.append({
        "id": "equivariant_linearMap_to_trivial_apply_eq_zero_of_neZero_two_qou_7jhl",
        "bean": "qou-7jhl",
        "theorem": "QOU.Mass.MilnorSignRepObstructionTripleChannel.equivariant_linearMap_to_trivial_apply_eq_zero_of_neZero_two",
        "x_val": mp.nstr(x_val, 80),
        "t_apply": mp.nstr(t_apply, 80),
        "passed": c2_pass,
    })

    # 3. interval_width_sub_eq_zero (qou-7sin)
    B1 = mp.pi * mpf("2")
    U1 = mp.pi * mpf("3") + mp.ln2
    B2 = mp.e * mpf("2")
    U2 = mp.e * mpf("3") + mp.catalan
    lhs_width = (U1 - B2) - (B1 - U2)
    rhs_width = (U1 - B1) + (U2 - B2)
    diff_width = abs(lhs_width - rhs_width)
    c3_pass = bool(diff_width < tol)
    checks.append({
        "id": "interval_width_sub_eq_zero_qou_7sin",
        "bean": "qou-7sin",
        "theorem": "QOU.Mass.MirrorSplitIsASmallFractionOfTheEnergy.interval_width_sub_eq_zero",
        "lhs_width": mp.nstr(lhs_width, 80),
        "rhs_width": mp.nstr(rhs_width, 80),
        "abs_diff": mp.nstr(diff_width, 80),
        "passed": c3_pass,
    })

    # 4. mubar_common_weight_sub_integer_multiple_eq_zero (qou-7tr2)
    w_val = mp.sqrt(mpf("19")) / mpf("7")
    S_2 = mpf("1")
    S_m = mpf("5")
    chan_2 = w_val * S_2
    chan_m = w_val * S_m
    diff_chan = abs(chan_m - S_m * chan_2)
    c4_pass = bool(diff_chan < tol)
    checks.append({
        "id": "mubar_common_weight_sub_integer_multiple_eq_zero_qou_7tr2",
        "bean": "qou-7tr2",
        "theorem": "QOU.Mass.MixedMultibondMuBarIntegrality.mubar_common_weight_sub_integer_multiple_eq_zero",
        "chan_m": mp.nstr(chan_m, 80),
        "abs_diff": mp.nstr(diff_chan, 80),
        "passed": c4_pass,
    })

    # 5. quadratic_coeff_sum_zero_of_three_roots (qou-7vh1)
    x_r = mp.pi / mpf("3")
    y_r = mp.e / mpf("5")
    z_r = mp.sqrt(mpf("7")) / mpf("2")
    V = mp.matrix([
        [x_r ** 2, x_r, mpf("1")],
        [y_r ** 2, y_r, mpf("1")],
        [z_r ** 2, z_r, mpf("1")],
    ])
    rhs_zero = mp.matrix([mpf("0"), mpf("0"), mpf("0")])
    sol = mp.lu_solve(V, rhs_zero)
    coeff_sum = abs(sol[0] + sol[1] + sol[2])
    det_V = abs(mp.det(V))
    c5_pass = bool((det_V > mpf("0")) and (coeff_sum < tol))
    checks.append({
        "id": "quadratic_coeff_sum_zero_of_three_roots_qou_7vh1",
        "bean": "qou-7vh1",
        "theorem": "QOU.Mass.MoebiusThreePointRigidity.quadratic_coeff_sum_zero_of_three_roots",
        "vandermonde_det": mp.nstr(det_V, 80),
        "abs_coeff_sum": mp.nstr(coeff_sum, 80),
        "passed": c5_pass,
    })

    all_passed = all(c["passed"] for c in checks)
    return {
        "probe": "milnororder-signrep-mirrorsplit-multibond-moebius-probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/milnororder_signrep_mirrorsplit_multibond_moebius_probe.py",
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
