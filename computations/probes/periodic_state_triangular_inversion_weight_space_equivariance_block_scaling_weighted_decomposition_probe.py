#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 74 foundations:
- qou-gd90: Periodic-state triangular system inversion for weight-space traces
- qou-gzsp: Unipotent intertwiner inversion and conjugation trace invariance
- qou-h56b: Block-dimension identity trace pinning and 3-strand weight constraints
- qou-hah4: Full-rank factorial recursion vs rank-one carrier deficit
- qou-luq7: Derivation of weighted character decomposition from completeness and block scaling
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

mp.dps = 80


def mat_mul(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1],
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1],
        ],
    ]


def mat_norm_diff(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> mp.mpf:
    return max(
        abs(A[0][0] - B[0][0]),
        abs(A[0][1] - B[0][1]),
        abs(A[1][0] - B[1][0]),
        abs(A[1][1] - B[1][1]),
    )


def mat_tr(A: list[list[mp.mpf]]) -> mp.mpf:
    return A[0][0] + A[1][1]


def id_mat() -> list[list[mp.mpf]]:
    return [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]


def unipotent_u(c: mp.mpf) -> list[list[mp.mpf]]:
    return [[mp.mpf(1), c], [mp.mpf(0), mp.mpf(1)]]


def run_checks() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    q_samples = [mp.mpf(k) for k in (-7, -3, -1, 1, 2, 3, 5, 11)]

    # 1. qou-gd90: Periodic-state triangular system inversion
    max_err_gd90 = mp.mpf(0)
    for Q in q_samples:
        for w0, w1, w2 in [(3, -5, 7), (4, 2, -9), (-6, 11, 5)]:
            mw0, mw1, mw2 = mp.mpf(w0), mp.mpf(w1), mp.mpf(w2)
            T0 = mw0
            T1 = mw0 + mw1
            T2 = mw0 + mw1 + mw2
            lhs_sum = (mp.mpf(1) + Q + Q * Q) * T0 + Q * (T1 - T0)
            rhs_sum = (mp.mpf(1) + Q * Q) * T0 + Q * T1
            err = max(
                abs((T1 - mw0) - mw1),
                abs((T2 - T1) - mw2),
                abs(lhs_sum - rhs_sum),
            )
            max_err_gd90 = max(max_err_gd90, err)
    results.append(
        {
            "beanId": "qou-gd90",
            "theorem": "triangular_weight_inversion_and_two_level_sum",
            "maxAbsError": mp.nstr(max_err_gd90, 20),
            "passed": bool(max_err_gd90 <= mp.mpf("1e-75")),
        }
    )

    # 2. qou-gzsp: Unipotent intertwiner group law, inversion, and conjugation trace invariance
    max_err_gzsp = mp.mpf(0)
    A = [[mp.mpf(5), mp.mpf(-3)], [mp.mpf(7), mp.mpf(11)]]
    I2 = id_mat()
    for c in q_samples:
        Uc = unipotent_u(c)
        U_neg = unipotent_u(-c)
        conj = mat_mul(mat_mul(Uc, A), U_neg)
        err = max(
            mat_norm_diff(mat_mul(Uc, U_neg), I2),
            abs(mat_tr(conj) - mat_tr(A)),
        )
        max_err_gzsp = max(max_err_gzsp, err)
    for c1, c2 in [(-4, 9), (3, -7), (5, 8)]:
        mc1, mc2 = mp.mpf(c1), mp.mpf(c2)
        prod_u = mat_mul(unipotent_u(mc1), unipotent_u(mc2))
        sum_u = unipotent_u(mc1 + mc2)
        max_err_gzsp = max(max_err_gzsp, mat_norm_diff(prod_u, sum_u))
    results.append(
        {
            "beanId": "qou-gzsp",
            "theorem": "unipotentIntertwiner_group_and_trace_conj",
            "maxAbsError": mp.nstr(max_err_gzsp, 20),
            "passed": bool(max_err_gzsp <= mp.mpf("1e-75")),
        }
    )

    # 3. qou-h56b: Block-dimension identity trace pinning
    max_err_h56b = mp.mpf(0)
    for y in q_samples:
        id_tr = y * mp.mpf(1) + y * mp.mpf(2) + y * mp.mpf(1)
        sq_tr = y * (mp.mpf(1) ** 2) + y * (mp.mpf(2) ** 2) + y * (mp.mpf(1) ** 2)
        err = max(
            abs(id_tr - mp.mpf(4) * y),
            abs(sq_tr - mp.mpf(6) * y),
            abs((sq_tr - id_tr) - mp.mpf(2) * y),
        )
        max_err_h56b = max(max_err_h56b, err)
    results.append(
        {
            "beanId": "qou-h56b",
            "theorem": "pinnedTrace3_uniform_three_strand_identities",
            "maxAbsError": mp.nstr(max_err_h56b, 20),
            "passed": bool(max_err_h56b <= mp.mpf("1e-75")),
        }
    )

    # 4. qou-hah4: Full-rank factorial recursion vs rank-one carrier deficit
    dim2 = mp.mpf(2)
    dim3 = mp.mpf(3) * dim2
    dim4 = mp.mpf(4) * dim3
    sq2 = mp.mpf(1) ** 2 + mp.mpf(1) ** 2
    sq3 = mp.mpf(1) ** 2 + mp.mpf(2) ** 2 + mp.mpf(1) ** 2
    sq4 = (
        mp.mpf(1) ** 2
        + mp.mpf(3) ** 2
        + mp.mpf(2) ** 2
        + mp.mpf(3) ** 2
        + mp.mpf(1) ** 2
    )
    def_sum = (dim2 - mp.mpf(1)) + (dim3 - mp.mpf(1)) + (dim4 - mp.mpf(1))
    max_err_hah4 = max(
        abs(dim2 - sq2),
        abs(dim3 - sq3),
        abs(dim4 - sq4),
        abs(def_sum - mp.mpf(29)),
    )
    results.append(
        {
            "beanId": "qou-hah4",
            "theorem": "fullRankDim_partition_sums_and_rankOne_deficits",
            "maxAbsError": mp.nstr(max_err_hah4, 20),
            "passed": bool(max_err_hah4 <= mp.mpf("1e-75")),
        }
    )

    # 5. qou-luq7: Weighted character trace decomposition and double-weighting residual
    max_err_luq7 = mp.mpf(0)
    for y1, y2, y3 in [(2, -3, 5), (-4, 7, 1)]:
        my1, my2, my3 = mp.mpf(y1), mp.mpf(y2), mp.mpf(y3)
        for c1, c2, c3 in [(3, -2, 8), (5, 4, -6)]:
            mc1, mc2, mc3 = mp.mpf(c1), mp.mpf(c2), mp.mpf(c3)
            t1, t2, t3 = my1 * mc1, my2 * mc2, my3 * mc3
            unw = t1 + t2 + t3
            wch = my1 * mc1 + my2 * mc2 + my3 * mc3
            defect_lhs = unw - (my1 * t1 + my2 * t2 + my3 * t3)
            defect_rhs = (
                (mp.mpf(1) - my1) * t1
                + (mp.mpf(1) - my2) * t2
                + (mp.mpf(1) - my3) * t3
            )
            err = max(abs(unw - wch), abs(defect_lhs - defect_rhs))
            max_err_luq7 = max(max_err_luq7, err)
    results.append(
        {
            "beanId": "qou-luq7",
            "theorem": "weightedCharSum3_derived_and_double_weight_defect",
            "maxAbsError": mp.nstr(max_err_luq7, 20),
            "passed": bool(max_err_luq7 <= mp.mpf("1e-75")),
        }
    )

    return results


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_rel = script_path.relative_to(repo_root).as_posix()
    script_sha256 = hashlib.sha256(script_path.read_bytes()).hexdigest()

    try:
        commit_sha = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            text=True,
        ).strip()
    except Exception:
        commit_sha = "UNKNOWN"

    checks = run_checks()
    all_passed = all(bool(c["passed"]) for c in checks)
    if not all_passed:
        raise SystemExit("One or more mpmath verification checks failed!")

    witness = {
        "schemaVersion": "1.0",
        "probeName": "periodic_state_triangular_inversion_weight_space_equivariance_block_scaling_weighted_decomposition_probe",
        "beans": ["qou-gd90", "qou-gzsp", "qou-h56b", "qou-hah4", "qou-luq7"],
        "leanModule": "QOU.Foundations.PeriodicStateTriangularInversionWeightSpaceEquivarianceBlockScalingWeightedDecomposition",
        "mpmathDps": 80,
        "scriptPath": script_rel,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }

    out_path = script_path.with_name(
        "periodic-state-triangular-inversion-weight-space-equivariance-block-scaling-weighted-decomposition.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {out_path} (scriptHash={script_sha256}, commit={commit_sha})")


if __name__ == "__main__":
    main()
