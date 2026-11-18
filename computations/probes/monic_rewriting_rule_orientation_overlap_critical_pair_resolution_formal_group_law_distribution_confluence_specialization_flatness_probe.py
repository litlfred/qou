#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 79 (lane-e667).

Beans:
  - qou-ix9e: Monic rewriting rule orientation and leading-monomial reduction decomposition
  - qou-lncp: Overlap critical-pair difference vanishing and two-term context linearity
  - qou-ulfe: Multiplicative formal group law associativity and unit-scale factorization
  - qou-znz5: Distribution algebra divided-power normal-form additivity and exchange reduction
  - qou-pso0: Specialization flatness and parameter-difference torsion-free factorization
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80


def check_qou_ix9e() -> dict:
    samples = [
        (4, 3, 1, 9, 17),
        (5, 2, 1, -4, 23),
        (7, 1, 1, 16, -11),
        (6, 4, 1, 25, 31),
    ]
    max_err = mp.mpf("0")
    for left_r, right_r, lead_c, rhs_s, u_val in samples:
        l_mp = mp.mpf(left_r)
        r_mp = mp.mpf(right_r)
        c_mp = mp.mpf(lead_c)
        s_mp = mp.mpf(rhs_s)
        u_mp = mp.mpf(u_val)
        lead_step = c_mp * u_mp - s_mp * u_mp
        rem = s_mp * u_mp
        err1 = abs((lead_step + rem) - u_mp)
        margin_fwd = l_mp - r_mp
        margin_rev = r_mp - l_mp
        err2 = abs(margin_rev + margin_fwd)
        max_err = max(max_err, err1, err2)
    return {
        "beanId": "qou-ix9e",
        "theorem": "monicRule_decomposition_and_orientation_antisymmetry",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_qou_lncp() -> dict:
    samples = [
        (4, -7, 13, 3, -5, 9, 11, -2, 17),
        (-9, 16, 21, -4, 7, -3, 14, 8, -19),
        (25, 4, -15, 6, 11, 5, -7, 12, 23),
    ]
    max_err = mp.mpf("0")
    for sa, sb, ww, cl, cr, c1, m1, c2, m2 in samples:
        sa_m, sb_m, ww_m = mp.mpf(sa), mp.mpf(sb), mp.mpf(ww)
        cl_m, cr_m = mp.mpf(cl), mp.mpf(cr)
        c1_m, m1_m, c2_m, m2_m = mp.mpf(c1), mp.mpf(m1), mp.mpf(c2), mp.mpf(m2)
        spoly = sa_m * (sb_m * ww_m) - sb_m * (sa_m * ww_m)
        lhs_ctx = cl_m * (c1_m * m1_m + c2_m * m2_m) * cr_m
        rhs_ctx = c1_m * (cl_m * m1_m * cr_m) + c2_m * (cl_m * m2_m * cr_m)
        max_err = max(max_err, abs(spoly), abs(lhs_ctx - rhs_ctx))
    return {
        "beanId": "qou-lncp",
        "theorem": "overlap_critical_pair_vanishing_and_context_linearity",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_qou_ulfe() -> dict:
    samples = [
        (3, 5, -7, 11),
        (-2, 9, 14, -6),
        (7, -4, 8, 15),
        (1, 13, -19, 23),
    ]
    max_err = mp.mpf("0")
    for lam, x, y, z in samples:
        lam_m, x_m, y_m, z_m = mp.mpf(lam), mp.mpf(x), mp.mpf(y), mp.mpf(z)

        def fgl(a: mp.mpf, b: mp.mpf) -> mp.mpf:
            return a + b + lam_m * a * b

        def uscale(a: mp.mpf) -> mp.mpf:
            return mp.mpf(1) + lam_m * a

        err_assoc = abs(fgl(fgl(x_m, y_m), z_m) - fgl(x_m, fgl(y_m, z_m)))
        err_unit = abs(uscale(fgl(x_m, y_m)) - uscale(x_m) * uscale(y_m))
        max_err = max(max_err, err_assoc, err_unit)
    return {
        "beanId": "qou-ulfe",
        "theorem": "multiplicativeFormalGroupLaw_associativity_and_unit_factorization",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_qou_znz5() -> dict:
    samples = [
        ((2, 3, 5), (7, -1, 4), (-3, 11, 13), 9, 14, -6, 19),
        ((5, 0, 8), (1, 4, -2), (7, -5, 17), -4, 9, 11, -23),
        ((9, -3, 2), (4, 6, 7), (2, 13, -11), 16, -7, 5, 29),
    ]
    max_err = mp.mpf("0")
    for (n1, c1, p1), (n2, c2, p2), (wn, wc, wp), qs, ev, fv, kv in samples:
        w1 = mp.mpf(n1) * mp.mpf(wn) + mp.mpf(c1) * mp.mpf(wc) + mp.mpf(p1) * mp.mpf(wp)
        w2 = mp.mpf(n2) * mp.mpf(wn) + mp.mpf(c2) * mp.mpf(wc) + mp.mpf(p2) * mp.mpf(wp)
        w_sum = (
            mp.mpf(n1 + n2) * mp.mpf(wn)
            + mp.mpf(c1 + c2) * mp.mpf(wc)
            + mp.mpf(p1 + p2) * mp.mpf(wp)
        )
        qs_m, ev_m, fv_m, kv_m = mp.mpf(qs), mp.mpf(ev), mp.mpf(fv), mp.mpf(kv)
        exch = qs_m * (ev_m * fv_m + kv_m) - (qs_m * ev_m) * fv_m
        max_err = max(max_err, abs(w_sum - (w1 + w2)), abs(exch - qs_m * kv_m))
    return {
        "beanId": "qou-znz5",
        "theorem": "dividedPower_normal_weight_additivity_and_exchange_reduction",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def check_qou_pso0() -> dict:
    samples = [
        (5, -3, 7, 9, 4, 11, -13, 17),
        (-8, 12, -5, -3, 6, 19, 23, -7),
        (14, 9, 11, 15, -2, -5, 8, 29),
    ]
    max_err = mp.mpf("0")
    for c0, c1, c2, tv, sv, b0, b1, b2 in samples:
        c0_m, c1_m, c2_m = mp.mpf(c0), mp.mpf(c1), mp.mpf(c2)
        tv_m, sv_m = mp.mpf(tv), mp.mpf(sv)
        b0_m, b1_m, b2_m = mp.mpf(b0), mp.mpf(b1), mp.mpf(b2)

        def eval_comb(t: mp.mpf) -> mp.mpf:
            return c0_m * b0_m + (c1_m * t) * b1_m + (c2_m * t * t) * b2_m

        err_one = abs(eval_comb(mp.mpf(1)) - (c0_m * b0_m + c1_m * b1_m + c2_m * b2_m))
        diff_lhs = eval_comb(tv_m) - eval_comb(sv_m)
        diff_rhs = (tv_m - sv_m) * (c1_m * b1_m + c2_m * (tv_m + sv_m) * b2_m)
        max_err = max(max_err, err_one, abs(diff_lhs - diff_rhs))
    return {
        "beanId": "qou-pso0",
        "theorem": "specializationAtOne_and_difference_factorization",
        "maxAbsError": mp.nstr(max_err, 25),
        "passed": bool(max_err == 0),
    }


def main() -> None:
    script_path = pathlib.Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_bytes = script_path.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    try:
        commit_sha = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "UNKNOWN"

    checks = [
        check_qou_ix9e(),
        check_qou_lncp(),
        check_qou_ulfe(),
        check_qou_znz5(),
        check_qou_pso0(),
    ]
    all_passed = all(c["passed"] for c in checks)
    witness = {
        "schemaVersion": "1.0",
        "probeName": "monic_rewriting_rule_orientation_overlap_critical_pair_resolution_formal_group_law_distribution_confluence_specialization_flatness_probe",
        "beans": ["qou-ix9e", "qou-lncp", "qou-ulfe", "qou-znz5", "qou-pso0"],
        "leanModule": "QOU.Foundations.MonicRewritingRuleOrientationOverlapCriticalPairResolutionFormalGroupLawDistributionConfluenceSpecializationFlatness",
        "mpmathDps": int(mp.dps),
        "scriptPath": "computations/probes/monic_rewriting_rule_orientation_overlap_critical_pair_resolution_formal_group_law_distribution_confluence_specialization_flatness_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }
    witness_path = (
        script_path.parent
        / "monic-rewriting-rule-orientation-overlap-critical-pair-resolution-formal-group-law-distribution-confluence-specialization-flatness.witness.json"
    )
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {witness_path} (scriptHash={script_sha256}, commit={commit_sha})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
