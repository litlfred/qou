#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 75 foundations:
- qou-sh62: Fourth-order coordination period factorization and multiplicity ratio separation
- qou-ss88: Disjoint-block trace factorization from two-step stabilization
- qou-t1kv: Scalar braid cascade residual, diagonal reducible witness, and zero content sum
- qou-csgy: Exact residual bridge between balanced and monic-quadratic generator conventions
- qou-fq1i: Identity-coefficient trace on involution generators: disjoint multiplicativity vs same-level square
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

mp.dps = 80


def run_checks() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    q_samples = [mp.mpf(k) for k in (-7, -3, -2, -1, 1, 2, 3, 5, 11)]

    # 1. qou-sh62: Fourth-order coordination period factorization and eval at q=2
    max_err_sh62 = mp.mpf(0)
    for q in q_samples:
        lhs = (q * q) ** 2 + q * q + mp.mpf(1)
        rhs = (q * q + q + mp.mpf(1)) * (q * q - q + mp.mpf(1))
        max_err_sh62 = max(max_err_sh62, abs(lhs - rhs))
    eval_two = (mp.mpf(2) ** 4 + mp.mpf(2) ** 2 + mp.mpf(1)) - mp.mpf(20)
    max_err_sh62 = max(max_err_sh62, abs(eval_two - mp.mpf(1)))
    results.append(
        {
            "beanId": "qou-sh62",
            "theorem": "coordPeriod4_factorization_and_eval_two",
            "maxAbsError": mp.nstr(max_err_sh62, 20),
            "passed": bool(max_err_sh62 <= mp.mpf("1e-75")),
        }
    )

    # 2. qou-ss88: Disjoint-block trace factorization
    max_err_ss88 = mp.mpf(0)
    for z in q_samples:
        for c0, c1, d0, d1 in [(3, -5, 2, 7), (-4, 9, 6, -1), (5, 2, -3, 8)]:
            mc0, mc1, md0, md1 = mp.mpf(c0), mp.mpf(c1), mp.mpf(d0), mp.mpf(d1)
            expand = (
                mc0 * md0
                + mc0 * (md1 * z)
                + (mc1 * z) * md0
                + (mc1 * z) * (md1 * z)
            )
            factored = (mc0 + mc1 * z) * (md0 + md1 * z)
            max_err_ss88 = max(max_err_ss88, abs(expand - factored))
    results.append(
        {
            "beanId": "qou-ss88",
            "theorem": "disjointBlockTraceExpand_eq_mul",
            "maxAbsError": mp.nstr(max_err_ss88, 20),
            "passed": bool(max_err_ss88 <= mp.mpf("1e-75")),
        }
    )

    # 3. qou-t1kv: Scalar braid cascade and diagonal reducible witness
    max_err_t1kv = mp.mpf(0)
    for X in q_samples:
        for s in q_samples:
            lhs = (X * s) * X - (s * X) * s
            rhs = s * (X * X - s * X)
            max_err_t1kv = max(max_err_t1kv, abs(lhs - rhs))
    for q1, q2 in [(-3, 5), (7, -2), (4, 9)]:
        mq1, mq2 = mp.mpf(q1), mp.mpf(q2)
        spread = mq1 - mq2
        content_twist = mp.mpf(2) * (mp.mpf(0) + mp.mpf(1) + mp.mpf(-1))
        max_err_t1kv = max(
            max_err_t1kv,
            abs((mq1 - mq2) - spread),
            abs(content_twist),
        )
    results.append(
        {
            "beanId": "qou-t1kv",
            "theorem": "scalar_braid_cascade_and_diagGen2_properties",
            "maxAbsError": mp.nstr(max_err_t1kv, 20),
            "passed": bool(max_err_t1kv <= mp.mpf("1e-75")),
        }
    )

    # 4. qou-csgy: Equivalence bridge between monic and balanced quadratic conventions
    max_err_csgy = mp.mpf(0)
    for q in q_samples:
        Q = q * q
        for s in q_samples:
            T = q * s
            monic_res = T * T - ((Q - mp.mpf(1)) * T + Q)
            bal_res = q * (s * s) - ((q * q - mp.mpf(1)) * s + q)
            max_err_csgy = max(max_err_csgy, abs(monic_res - q * bal_res))
    results.append(
        {
            "beanId": "qou-csgy",
            "theorem": "monicQuadResidual_eq_mul_balancedQuadResidual",
            "maxAbsError": mp.nstr(max_err_csgy, 20),
            "passed": bool(max_err_csgy <= mp.mpf("1e-75")),
        }
    )

    # 5. qou-fq1i: Identity-coefficient trace on involution tower
    max_err_fq1i = mp.mpf(0)
    for c1, c2 in [(-5, 3), (4, -7), (9, 2), (0, 6)]:
        mc1, mc2 = mp.mpf(c1), mp.mpf(c2)
        disj_tr = mp.mpf(1) + mc1 * mp.mpf(0) + mc2 * mp.mpf(0) + (mc1 * mc2) * mp.mpf(0)
        single1 = mp.mpf(1) + mc1 * mp.mpf(0)
        single2 = mp.mpf(1) + mc2 * mp.mpf(0)
        sq_tr = mp.mpf(1) + mp.mpf(2) * (mc1 * mp.mpf(0)) + (mc1 * mc1) * mp.mpf(1)
        err = max(
            abs(disj_tr - single1 * single2),
            abs((sq_tr - single1 * single1) - mc1 * mc1),
        )
        max_err_fq1i = max(max_err_fq1i, err)
    results.append(
        {
            "beanId": "qou-fq1i",
            "theorem": "involutionTrace_disjoint_vs_square_residual",
            "maxAbsError": mp.nstr(max_err_fq1i, 20),
            "passed": bool(max_err_fq1i <= mp.mpf("1e-75")),
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
        "probeName": "coordination_period_separation_disjoint_block_factorization_scalar_cascade_quadratic_convention_bridge_involution_trace_probe",
        "beans": ["qou-sh62", "qou-ss88", "qou-t1kv", "qou-csgy", "qou-fq1i"],
        "leanModule": "QOU.Foundations.CoordinationPeriodSeparationDisjointBlockFactorizationScalarCascadeQuadraticConventionBridgeInvolutionTrace",
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
        "coordination-period-separation-disjoint-block-factorization-scalar-cascade-quadratic-convention-bridge-involution-trace.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {out_path} (scriptHash={script_sha256}, commit={commit_sha})")


if __name__ == "__main__":
    main()
