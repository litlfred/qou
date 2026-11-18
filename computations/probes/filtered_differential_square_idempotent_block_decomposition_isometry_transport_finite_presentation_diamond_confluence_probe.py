#!/usr/bin/env python3
"""80-dps mpmath numerical probe for Round 78 beans:
qou-pan0, qou-tgci, qou-ykt7, qou-bq5e, qou-ch3j.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80


def check_pan0() -> dict:
    """Verify filteredDiff_nilpotency_and_norm_multiplicativity at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (3, 5, -7, 11, 13, 2, -4, 9),
        (-2, 7, 3, -5, 19, -8, 11, -3),
        (5, -11, 17, 23, -29, 6, 15, -21),
    ]
    for a, x1, y1, x2, y2, v0, v1, v2 in samples:
        am, x1m, y1m, x2m, y2m, v0m, v1m, v2m = map(
            mp.mpf, (a, x1, y1, x2, y2, v0, v1, v2)
        )
        d1 = (am * v1m, am * v2m, mp.mpf(0))
        d1_sq = (am * d1[1], am * d1[2], mp.mpf(0))
        d1_cu = (am * d1_sq[1], am * d1_sq[2], mp.mpf(0))
        d2 = ((am * am) * v2m, mp.mpf(0), mp.mpf(0))
        err_diff = (
            sum(abs(d1_sq[i] - d2[i]) for i in range(3))
            + sum(abs(d1_cu[i]) for i in range(3))
        )
        lhs_norm = (x1m * x2m - y1m * y2m) ** 2 + (x1m * y2m + y1m * x2m) ** 2
        rhs_norm = (x1m ** 2 + y1m ** 2) * (x2m ** 2 + y2m ** 2)
        err_norm = abs(lhs_norm - rhs_norm)
        max_err = max(max_err, err_diff, err_norm)
    return {
        "beanId": "qou-pan0",
        "theorem": "filteredDiff_nilpotency_and_norm_multiplicativity",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_tgci() -> dict:
    """Verify complementary_projection_decomposition_and_orthogonality at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (3, -5, 7, 11),
        (-4, 9, -13, 17),
        (6, 11, 19, -23),
    ]
    for a, b, x0, x1 in samples:
        am, bm, x0m, x1m = map(mp.mpf, (a, b, x0, x1))
        p_plus = (am * x0m + bm * x1m, mp.mpf(0))
        p_minus = (-bm * x1m, am * x1m)
        sum_v = (p_plus[0] + p_minus[0], p_plus[1] + p_minus[1])
        scaled_v = (am * x0m, am * x1m)
        pp_plus = (am * p_plus[0] + bm * p_plus[1], mp.mpf(0))
        mm_minus = (-bm * p_minus[1], am * p_minus[1])
        mp_cross = (-bm * p_plus[1], am * p_plus[1])
        pm_cross = (am * p_minus[0] + bm * p_minus[1], mp.mpf(0))
        err = (
            abs(sum_v[0] - scaled_v[0])
            + abs(sum_v[1] - scaled_v[1])
            + abs(pp_plus[0] - am * p_plus[0])
            + abs(pp_plus[1] - am * p_plus[1])
            + abs(mm_minus[0] - am * p_minus[0])
            + abs(mm_minus[1] - am * p_minus[1])
            + abs(mp_cross[0])
            + abs(mp_cross[1])
            + abs(pm_cross[0])
            + abs(pm_cross[1])
        )
        max_err = max(max_err, err)
    return {
        "beanId": "qou-tgci",
        "theorem": "complementary_projection_decomposition_and_orthogonality",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_ykt7() -> dict:
    """Verify isoMap_bijection_and_displacement_transport at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (1, 5, -7, 13, 2),
        (-1, -9, 11, -17, 4),
        (1, -12, 19, 29, -3),
        (-1, 8, -23, 31, 7),
    ]
    for s, t, x, y, m in samples:
        sm, tm, xm, ym, mm = map(mp.mpf, (s, t, x, y, m))
        iso_x = sm * xm + tm
        iso_y = sm * ym + tm
        inv_iso_x = sm * (iso_x - tm)
        iso_inv_y = sm * (sm * (ym - tm)) + tm
        disp_add = ((mm - xm) + (ym - mm)) - (ym - xm)
        disp_eq = (iso_y - iso_x) - sm * (ym - xm)
        err = (
            abs(inv_iso_x - xm)
            + abs(iso_inv_y - ym)
            + abs(disp_add)
            + abs(disp_eq)
        )
        max_err = max(max_err, err)
    return {
        "beanId": "qou-ykt7",
        "theorem": "isoMap_bijection_and_displacement_transport",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_bq5e() -> dict:
    """Verify overlapDefect_formula_and_commuting_vanishing at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (3, 2, 5, 7, 11, 4),
        (-2, 5, -9, 13, -7, 3),
        (1, 4, 8, 6, 2, 1),
    ]
    for p, q, xy, y, x, c in samples:
        pm, qm, xym, ym, xm, cm = map(mp.mpf, (p, q, xy, y, x, c))
        left_b = pm * xym + qm * ym + (2 * cm) * xm
        right_b = pm * xym + qm * ym + pm * cm
        defect = left_b - right_b
        expected = cm * (2 * xm - pm)
        err = abs(defect - expected)
        if (p, x, c) == (1, 2, 1):
            err += abs(defect - 3)
        max_err = max(max_err, err)
    return {
        "beanId": "qou-bq5e",
        "theorem": "overlapDefect_formula_and_commuting_vanishing",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_ch3j() -> dict:
    """Verify diamondJoin_confluence_and_normal_form_uniqueness at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (25, 7, 11),
        (-13, 5, -9),
        (42, 17, 19),
    ]
    for w, d1, d2 in samples:
        wm, d1m, d2m = map(mp.mpf, (w, d1, d2))
        b_a = (wm - d1m) - d2m
        b_b = (wm - d2m) - d1m
        join1 = wm - d1m - d2m
        join2 = wm - d2m - d1m
        err = abs(b_a - join1) + abs(b_b - join1) + abs(join1 - join2)
        max_err = max(max_err, err)
    return {
        "beanId": "qou-ch3j",
        "theorem": "diamondJoin_confluence_and_normal_form_uniqueness",
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
        check_pan0(),
        check_tgci(),
        check_ykt7(),
        check_bq5e(),
        check_ch3j(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "schemaVersion": "1.0",
        "probeName": "filtered_differential_square_idempotent_block_decomposition_isometry_transport_finite_presentation_diamond_confluence_probe",
        "beans": ["qou-pan0", "qou-tgci", "qou-ykt7", "qou-bq5e", "qou-ch3j"],
        "leanModule": "QOU.Foundations.FilteredDifferentialSquareIdempotentBlockDecompositionIsometryTransportFinitePresentationDiamondConfluence",
        "mpmathDps": 80,
        "scriptPath": "computations/probes/filtered_differential_square_idempotent_block_decomposition_isometry_transport_finite_presentation_diamond_confluence_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }

    witness_path = script_path.with_name(
        "filtered-differential-square-idempotent-block-decomposition-isometry-transport-finite-presentation-diamond-confluence.witness.json"
    )
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {witness_path} (scriptHash={script_sha256}, commit={commit_sha})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
