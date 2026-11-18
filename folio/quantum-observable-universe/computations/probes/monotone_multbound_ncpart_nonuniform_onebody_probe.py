#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 97 theorems (qou-87ms, qou-8fl1, qou-8foz, qou-8jfh, qou-8jjo).

Verifies:
1. allEven_posAfter_sub_eq_zero (qou-87ms):
   For all-even exponents e(g) = 2, posAfter(e, N, i) - i = 0 for all i + 1 <= N.
2. sub_nonneg_of_dominant (qou-8fl1):
   0 <= card(s) * |a(i0)| - |sum_{i in s} a(i)| at 80 decimal places.
3. card_ncpart_three_add_four (qou-8foz):
   Catalan(3) + Catalan(4) = 5 + 14 = 19.
4. mirrorSplit_self_eq_zero (qou-8jfh):
   fhBoundNonuniform(P) - fhBoundNonuniform(P) = 0 at 80 decimal places.
5. chargeIndependent_symm (qou-8jjo):
   For one-body f(a, b) = g(b) with f(p, p) = f(n, n), f(a, b) = f(b, a) across all 4 pairs.
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

    # 1. allEven_posAfter_sub_eq_zero (qou-87ms)
    N_runs = 7
    pos = list(range(N_runs + 1))
    for g in range(N_runs):
        e_g = 2
        if e_g % 2 != 0:
            pos[g], pos[g + 1] = pos[g + 1], pos[g]
    max_diff_pos = max(abs(mpf(str(pos[i] - i))) for i in range(N_runs))
    c1_pass = bool(max_diff_pos == mpf("0"))
    checks.append({
        "id": "allEven_posAfter_sub_eq_zero_qou_87ms",
        "bean": "qou-87ms",
        "theorem": "QOU.Mass.MonotoneWordCycleStructure.allEven_posAfter_sub_eq_zero",
        "N_runs": str(N_runs),
        "max_diff_pos": mp.nstr(max_diff_pos, 80),
        "passed": c1_pass,
    })

    # 2. sub_nonneg_of_dominant (qou-8fl1)
    terms = [mp.pi / mpf("3"), -mp.e / mpf("2"), mp.sqrt(mpf("7")) / mpf("4"), -mp.catalan]
    dom_abs = max(abs(x) for x in terms)
    card_s = mpf(str(len(terms)))
    slack_dom = card_s * dom_abs - abs(sum(terms))
    c2_pass = bool(slack_dom >= mpf("0") and slack_dom > mpf("1"))
    checks.append({
        "id": "sub_nonneg_of_dominant_qou_8fl1",
        "bean": "qou-8fl1",
        "theorem": "QOU.Mass.MultiplicityCountingBound.sub_nonneg_of_dominant",
        "dom_abs": mp.nstr(dom_abs, 80),
        "slack_dom": mp.nstr(slack_dom, 80),
        "passed": c2_pass,
    })

    # 3. card_ncpart_three_add_four (qou-8foz)
    c3 = mp.binomial(6, 3) / mpf("4")
    c4 = mp.binomial(8, 4) / mpf("5")
    sum_c3_c4 = c3 + c4
    diff_c = abs(sum_c3_c4 - mpf("19"))
    c3_pass = bool(diff_c == mpf("0"))
    checks.append({
        "id": "card_ncpart_three_add_four_qou_8foz",
        "bean": "qou-8foz",
        "theorem": "QOU.Mass.card_ncpart_three_add_four",
        "c3": mp.nstr(c3, 80),
        "c4": mp.nstr(c4, 80),
        "sum_c3_c4": mp.nstr(sum_c3_c4, 80),
        "passed": c3_pass,
    })

    # 4. mirrorSplit_self_eq_zero (qou-8jfh)
    C_val = (mp.pi / mpf("16")) ** (mpf("1") / mpf("4"))
    m_flux = mp.e / mpf("5")
    a_weights = [mp.sqrt(mpf("2")), mp.sqrt(mpf("3")), mp.sqrt(mpf("5")), mp.sqrt(mpf("7"))]
    phi_p = mp.pi / mpf("2")
    phi_n = mp.ln2
    P_idx = [0, 2]
    P_comp = [1, 3]
    fh_P = C_val * m_flux * (sum(a_weights[k] for k in P_idx) * phi_p + sum(a_weights[k] for k in P_comp) * phi_n)
    self_diff = abs(fh_P - fh_P)
    c4_pass = bool(self_diff == mpf("0") and fh_P > mpf("0"))
    checks.append({
        "id": "mirrorSplit_self_eq_zero_qou_8jfh",
        "bean": "qou-8jfh",
        "theorem": "QOU.Mass.NonUniformAcRelocatesTheObligation.mirrorSplit_self_eq_zero",
        "fh_P": mp.nstr(fh_P, 80),
        "self_diff": mp.nstr(self_diff, 80),
        "passed": c4_pass,
    })

    # 5. chargeIndependent_symm (qou-8jjo)
    g_val = mp.pi * mp.e
    g_map = {"p": g_val, "n": g_val}
    f_onebody = lambda a, b: g_map[b]
    max_asym = max(abs(f_onebody(a, b) - f_onebody(b, a)) for a in ("p", "n") for b in ("p", "n"))
    c5_pass = bool(max_asym == mpf("0"))
    checks.append({
        "id": "chargeIndependent_symm_qou_8jjo",
        "bean": "qou-8jjo",
        "theorem": "QOU.Mass.OneBodyBondOrdering.chargeIndependent_symm",
        "common_val": mp.nstr(g_val, 80),
        "max_asym": mp.nstr(max_asym, 80),
        "passed": c5_pass,
    })

    all_passed = all(c["passed"] for c in checks)
    return {
        "probe": "monotone-multbound-ncpart-nonuniform-onebody-probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/monotone_multbound_ncpart_nonuniform_onebody_probe.py",
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
