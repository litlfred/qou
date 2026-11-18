#!/usr/bin/env python3
"""80-dps mpmath numerical probe for Round 77 beans:
qou-36vh, qou-3xjy, qou-73kb, qou-anpu, qou-gjnc.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80


def check_36vh() -> dict:
    """Verify swap01_swap12_involutive_and_cubic_braid_eq_rev012 at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (3, -5, 11),
        (-7, 13, 19),
        (23, -29, 31),
    ]
    for x0, x1, x2 in samples:
        v = (mp.mpf(x0), mp.mpf(x1), mp.mpf(x2))
        s01 = lambda u: (u[1], u[0], u[2])
        s12 = lambda u: (u[0], u[2], u[1])
        rev = (v[2], v[1], v[0])
        inv01 = s01(s01(v))
        inv12 = s12(s12(v))
        lhs_braid = s01(s12(s01(v)))
        rhs_braid = s12(s01(s12(v)))
        err = (
            sum(abs(inv01[i] - v[i]) for i in range(3))
            + sum(abs(inv12[i] - v[i]) for i in range(3))
            + sum(abs(lhs_braid[i] - rhs_braid[i]) for i in range(3))
            + sum(abs(lhs_braid[i] - rev[i]) for i in range(3))
        )
        max_err = max(max_err, err)
    return {
        "beanId": "qou-36vh",
        "theorem": "swap01_swap12_involutive_and_cubic_braid_eq_rev012",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_3xjy() -> dict:
    """Verify invPoly3_and_invPoly4_expansion_and_classical_eval at 80-dps."""
    max_err = mp.mpf(0)
    for q in (-3, -1, 0, 1, 2, 3, 5, 7):
        qm = mp.mpf(q)
        p2 = 1 + qm
        p3 = p2 + (1 + qm)
        p4 = p3 + (1 + qm + qm * qm) * p2
        exp3 = 2 + 2 * qm
        exp4 = 3 + 4 * qm + 2 * (qm * qm) + qm * (qm * qm)
        err = abs(p3 - exp3) + abs(p4 - exp4)
        if q == 1:
            err += abs(p3 - 4) + abs(p4 - 10)
        max_err = max(max_err, err)
    return {
        "beanId": "qou-3xjy",
        "theorem": "invPoly3_and_invPoly4_expansion_and_classical_eval",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_73kb() -> dict:
    """Verify cosetMultipliedSum_factorization_and_transversal_zero at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (6, 5, 11, 7),
        (12, -3, 8, -13),
        (24, 17, -19, 23),
    ]
    for hcard, t0, t1, t2 in samples:
        hm, t0m, t1m, t2m = map(mp.mpf, (hcard, t0, t1, t2))
        trans = t0m - t1m + t2m
        coset_sum = hm * t0m - hm * t1m + hm * t2m
        trans_zero = t0m - (t0m + t2m) + t2m
        coset_zero = hm * t0m - hm * (t0m + t2m) + hm * t2m
        err = abs(coset_sum - hm * trans) + abs(trans_zero) + abs(coset_zero)
        max_err = max(max_err, err)
    return {
        "beanId": "qou-73kb",
        "theorem": "cosetMultipliedSum_factorization_and_transversal_zero",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_anpu() -> dict:
    """Verify majGen21_factorization_and_clearedHook_identity at 80-dps."""
    max_err = mp.mpf(0)
    for q in (-4, -2, 0, 1, 2, 3, 5, 9):
        qm = mp.mpf(q)
        maj = qm + qm * qm
        lhs = (1 + qm + qm * qm) * maj
        rhs = qm * ((1 + qm) * (1 + qm + qm * qm))
        err = abs(maj - qm * (1 + qm)) + abs(lhs - rhs)
        if q == 1:
            err += abs(maj - 2)
        max_err = max(max_err, err)
    return {
        "beanId": "qou-anpu",
        "theorem": "majGen21_factorization_and_clearedHook_identity",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_gjnc() -> dict:
    """Verify constructive_unimodular_witness_identities at 80-dps."""
    max_err = mp.mpf(0)
    for n in (-11, -5, -1, 0, 1, 2, 7, 19):
        nm = mp.mpf(n)
        w1 = nm * (-1) + (nm + 1) * 1
        w2 = (2 * nm + 1) * 1 + nm * (-2)
        w3 = (3 * nm + 1) * 1 + nm * (-3)
        err = abs(w1 - 1) + abs(w2 - 1) + abs(w3 - 1)
        max_err = max(max_err, err)
    return {
        "beanId": "qou-gjnc",
        "theorem": "constructive_unimodular_witness_identities",
        "maxAbsError": mp.nstr(max_err, 20),
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
        check_36vh(),
        check_3xjy(),
        check_73kb(),
        check_anpu(),
        check_gjnc(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "schemaVersion": "1.0",
        "probeName": "adjacent_transposition_cubic_relation_involution_dimension_sum_transversal_straightening_hook_major_sum_constructive_witness_probe",
        "beans": ["qou-36vh", "qou-3xjy", "qou-73kb", "qou-anpu", "qou-gjnc"],
        "leanModule": "QOU.Foundations.AdjacentTranspositionCubicRelationInvolutionDimensionSumTransversalStraighteningHookMajorSumConstructiveWitness",
        "mpmathDps": 80,
        "scriptPath": "computations/probes/adjacent_transposition_cubic_relation_involution_dimension_sum_transversal_straightening_hook_major_sum_constructive_witness_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }

    witness_path = script_path.with_name(
        "adjacent-transposition-cubic-relation-involution-dimension-sum-transversal-straightening-hook-major-sum-constructive-witness.witness.json"
    )
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {witness_path} (scriptHash={script_sha256}, commit={commit_sha})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
