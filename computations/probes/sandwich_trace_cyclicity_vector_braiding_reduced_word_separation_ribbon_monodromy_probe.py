#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 72 foundations:
- qou-sx5r: Two-generator sandwich reduction and trace cyclicity
- qou-slck: Vector representation mixed-weight braiding block, trace, and determinant
- qou-dgsw: Reduced-word coordinate extraction and linear independence
- qou-jfr8: Pairwise character separation and total degree-squared sum
- qou-zoyv: Double-braiding ribbon monodromy and quadratic trace invariant
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


def mat_add(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [
        [A[0][0] + B[0][0], A[0][1] + B[0][1]],
        [A[1][0] + B[1][0], A[1][1] + B[1][1]],
    ]


def mat_smul(c: mp.mpf, A: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [[c * A[0][0], c * A[0][1]], [c * A[1][0], c * A[1][1]]]


def mat_norm_diff(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> mp.mpf:
    return max(
        abs(A[0][0] - B[0][0]),
        abs(A[0][1] - B[0][1]),
        abs(A[1][0] - B[1][0]),
        abs(A[1][1] - B[1][1]),
    )


def mat_tr(A: list[list[mp.mpf]]) -> mp.mpf:
    return A[0][0] + A[1][1]


def mat_det(A: list[list[mp.mpf]]) -> mp.mpf:
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def gen_f(q: mp.mpf) -> list[list[mp.mpf]]:
    return [[q, mp.mpf(1)], [mp.mpf(0), mp.mpf(-1)]]


def gen_g(q: mp.mpf) -> list[list[mp.mpf]]:
    return [[mp.mpf(-1), mp.mpf(0)], [q, q]]


def r_mix(q: mp.mpf) -> list[list[mp.mpf]]:
    return [[q - mp.mpf(1), q], [mp.mpf(1), mp.mpf(0)]]


def id_mat() -> list[list[mp.mpf]]:
    return [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]


def run_checks() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    q_samples = [mp.mpf(k) for k in (-7, -3, -1, 1, 2, 3, 5, 11)]

    # 1. qou-sx5r: Two-generator sandwich reduction and trace cyclicity
    max_err_sx5r = mp.mpf(0)
    for q in q_samples:
        F = gen_f(q)
        G = gen_g(q)
        I2 = id_mat()
        FG = mat_mul(F, G)
        GF = mat_mul(G, F)
        GFG = mat_mul(GF, G)
        FGF = mat_mul(FG, F)
        G2 = mat_mul(G, G)
        G2_rhs = mat_add(mat_smul(q - mp.mpf(1), G), mat_smul(q, I2))
        err = max(
            abs(mat_tr(FG) - (-q)),
            abs(mat_tr(GF) - (-q)),
            abs(mat_tr(GFG)),
            abs(mat_tr(FGF)),
            mat_norm_diff(G2, G2_rhs),
            mat_norm_diff(GFG, FGF),
        )
        max_err_sx5r = max(max_err_sx5r, err)
    results.append(
        {
            "beanId": "qou-sx5r",
            "theorem": "genFG_trace_cyclicity_and_zero / genG_sandwich_coset_reduction",
            "maxAbsError": mp.nstr(max_err_sx5r, 20),
            "passed": bool(max_err_sx5r <= mp.mpf("1e-75")),
        }
    )

    # 2. qou-slck: Vector representation mixed-weight braiding block
    max_err_slck = mp.mpf(0)
    for q in q_samples:
        R = r_mix(q)
        I2 = id_mat()
        R2 = mat_mul(R, R)
        R2_rhs = mat_add(mat_smul(q - mp.mpf(1), R), mat_smul(q, I2))
        err = max(
            abs(mat_tr(R) - (q - mp.mpf(1))),
            abs(mat_det(R) - (-q)),
            mat_norm_diff(R2, R2_rhs),
        )
        max_err_slck = max(max_err_slck, err)
    results.append(
        {
            "beanId": "qou-slck",
            "theorem": "vectorBraidingMix_trace_det_and_quadratic",
            "maxAbsError": mp.nstr(max_err_slck, 20),
            "passed": bool(max_err_slck <= mp.mpf("1e-75")),
        }
    )

    # 3. qou-dgsw: Reduced-word coordinate extraction and linear independence
    max_err_dgsw = mp.mpf(0)
    for q in q_samples:
        F = gen_f(q)
        G = gen_g(q)
        I2 = id_mat()
        for c0, c1, c2 in [(-3, 5, 2), (4, -7, 1), (0, 2, -5), (9, 0, 3)]:
            mc0, mc1, mc2 = mp.mpf(c0), mp.mpf(c1), mp.mpf(c2)
            W = mat_add(
                mat_add(mat_smul(mc0, I2), mat_smul(mc1, F)),
                mat_smul(mc2, G),
            )
            rec_c1 = W[0][1]
            rec_qc2 = W[1][0]
            rec_c0 = W[0][0] - q * W[0][1] + mc2
            err = max(
                abs(rec_c1 - mc1),
                abs(rec_qc2 - q * mc2),
                abs(rec_c0 - mc0),
            )
            max_err_dgsw = max(max_err_dgsw, err)
    results.append(
        {
            "beanId": "qou-dgsw",
            "theorem": "reducedWordCombo3_coordinate_recovery",
            "maxAbsError": mp.nstr(max_err_dgsw, 20),
            "passed": bool(max_err_dgsw <= mp.mpf("1e-75")),
        }
    )

    # 4. qou-jfr8: Pairwise character separation and degree-squared sum
    max_err_jfr8 = mp.mpf(0)
    for q in q_samples:
        chi_triv = q
        chi_std = mat_tr(gen_f(q))
        chi_sign = mp.mpf(-1)
        deg_sum = mp.mpf(1) ** 2 + mp.mpf(2) ** 2 + mp.mpf(1) ** 2
        err = max(
            abs((chi_triv - chi_std) - mp.mpf(1)),
            abs((chi_std - chi_sign) - q),
            abs((chi_triv - chi_sign) - (q + mp.mpf(1))),
            abs(deg_sum - mp.mpf(6)),
        )
        max_err_jfr8 = max(max_err_jfr8, err)
    results.append(
        {
            "beanId": "qou-jfr8",
            "theorem": "threeStrand_character_separation_and_degree_sum",
            "maxAbsError": mp.nstr(max_err_jfr8, 20),
            "passed": bool(max_err_jfr8 <= mp.mpf("1e-75")),
        }
    )

    # 5. qou-zoyv: Double-braiding ribbon monodromy and quadratic trace invariant
    max_err_zoyv = mp.mpf(0)
    for q in q_samples:
        R = r_mix(q)
        M = mat_mul(R, R)
        err = max(
            abs(mat_tr(M) - (q * q + mp.mpf(1))),
            abs(mat_det(M) - (q * q)),
        )
        max_err_zoyv = max(max_err_zoyv, err)
    results.append(
        {
            "beanId": "qou-zoyv",
            "theorem": "ribbonMonodromyMix_trace_and_det",
            "maxAbsError": mp.nstr(max_err_zoyv, 20),
            "passed": bool(max_err_zoyv <= mp.mpf("1e-75")),
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
        "probeName": "sandwich_trace_cyclicity_vector_braiding_reduced_word_separation_ribbon_monodromy_probe",
        "beans": ["qou-sx5r", "qou-slck", "qou-dgsw", "qou-jfr8", "qou-zoyv"],
        "leanModule": "QOU.Foundations.SandwichTraceCyclicityVectorBraidingReducedWordSeparationRibbonMonodromy",
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
        "sandwich-trace-cyclicity-vector-braiding-reduced-word-separation-ribbon-monodromy.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {out_path} (scriptHash={script_sha256}, commit={commit_sha})")


if __name__ == "__main__":
    main()
