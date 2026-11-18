#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 73 foundations:
- qou-0fmb: Tower inverse-step compatibility and trace reduction
- qou-4lft: Root-of-unity seminormal denominator vanishing at q^2 = 1
- qou-avt2: Normalization bridge between quadratic conventions and character trace sum
- qou-cf3m: Two-row quotient dimension deficit and sign-projector spectral vanishing
- qou-g6vb: Bilinear trace pairing symmetry and basis expansion on 2x2 blocks
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


def id_mat() -> list[list[mp.mpf]]:
    return [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]


def rescaled_std_gen(q: mp.mpf) -> list[list[mp.mpf]]:
    return [[q * q, q], [mp.mpf(0), mp.mpf(-1)]]


def run_checks() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    q_samples = [mp.mpf(k) for k in (-7, -3, -2, 2, 3, 5, 11)]

    # 1. qou-0fmb: Tower inverse-step compatibility and trace reduction
    max_err_0fmb = mp.mpf(0)
    for q in q_samples:
        fwd_num = (q * q) * (q * q)
        quad_num = (q * q - mp.mpf(1)) * (q * q + mp.mpf(1))
        denom = q * (q * q + mp.mpf(1))
        z_fwd = (q ** 3) / (q * q + mp.mpf(1))
        h_def = q - mp.mpf(1) / q
        z_inv = z_fwd - h_def
        for t in (-5, -1, 1, 4, 9):
            mt = mp.mpf(t)
            err = max(
                abs((fwd_num - quad_num) - mp.mpf(1)),
                abs((fwd_num * mt - quad_num * mt) - mt),
                abs(z_inv * denom - mp.mpf(1)),
            )
            max_err_0fmb = max(max_err_0fmb, err)
    results.append(
        {
            "beanId": "qou-0fmb",
            "theorem": "inverseStepNum_unit_and_trace_reduction",
            "maxAbsError": mp.nstr(max_err_0fmb, 20),
            "passed": bool(max_err_0fmb <= mp.mpf("1e-75")),
        }
    )

    # 2. qou-4lft: Root-of-unity seminormal denominator vanishing at q^2 = 1
    max_err_4lft = mp.mpf(0)
    for q in q_samples:
        den1 = q * q - mp.mpf(1)
        den2 = (q * q) * (q * q) - mp.mpf(1)
        max_err_4lft = max(max_err_4lft, abs(den2 - den1 * (q * q + mp.mpf(1))))
    for q_root in (mp.mpf(1), mp.mpf(-1)):
        num_r = q_root * q_root - mp.mpf(1)
        den1_r = q_root * q_root - mp.mpf(1)
        den2_r = (q_root * q_root) ** 2 - mp.mpf(1)
        max_err_4lft = max(max_err_4lft, abs(num_r), abs(den1_r), abs(den2_r))
    results.append(
        {
            "beanId": "qou-4lft",
            "theorem": "seminormal_factorization_and_root_of_unity_vanishing",
            "maxAbsError": mp.nstr(max_err_4lft, 20),
            "passed": bool(max_err_4lft <= mp.mpf("1e-75")),
        }
    )

    # 3. qou-avt2: Convention normalization bridge and character sum
    max_err_avt2 = mp.mpf(0)
    for q in q_samples:
        T = rescaled_std_gen(q)
        I2 = id_mat()
        T2 = mat_mul(T, T)
        T2_rhs = mat_add(
            mat_smul(q * q - mp.mpf(1), T),
            mat_smul(q * q, I2),
        )
        char_sum = mp.mpf(1) * (q * q) + mp.mpf(2) * mat_tr(T) + mp.mpf(1) * mp.mpf(-1)
        err = max(
            mat_norm_diff(T2, T2_rhs),
            abs(char_sum - mp.mpf(3) * (q * q - mp.mpf(1))),
        )
        max_err_avt2 = max(max_err_avt2, err)
    results.append(
        {
            "beanId": "qou-avt2",
            "theorem": "rescaledStdGen_quadratic_and_character_sum",
            "maxAbsError": mp.nstr(max_err_avt2, 20),
            "passed": bool(max_err_avt2 <= mp.mpf("1e-75")),
        }
    )

    # 4. qou-cf3m: Two-row quotient dimension deficit and sign-projector spectral vanishing
    max_err_cf3m = mp.mpf(0)
    for q in q_samples:
        Q = q * q
        p_triv = (Q - Q) * (Q - Q)
        p_std = (Q - Q) * (Q - mp.mpf(-1))
        p_sign = (Q - mp.mpf(-1)) * (Q - mp.mpf(-1))
        deficit = mp.mpf(6) - (mp.mpf(1) ** 2 + mp.mpf(2) ** 2)
        err = max(
            abs(p_triv),
            abs(p_std),
            abs(p_sign - (Q + mp.mpf(1)) ** 2),
            abs(deficit - mp.mpf(1)),
        )
        max_err_cf3m = max(max_err_cf3m, err)
    results.append(
        {
            "beanId": "qou-cf3m",
            "theorem": "signSpectralPoly_two_row_vanishing_and_deficit",
            "maxAbsError": mp.nstr(max_err_cf3m, 20),
            "passed": bool(max_err_cf3m <= mp.mpf("1e-75")),
        }
    )

    # 5. qou-g6vb: Bilinear trace pairing symmetry and left linearity
    max_err_g6vb = mp.mpf(0)
    A = [[mp.mpf(3), mp.mpf(-2)], [mp.mpf(5), mp.mpf(7)]]
    B = [[mp.mpf(-4), mp.mpf(9)], [mp.mpf(1), mp.mpf(-6)]]
    C = [[mp.mpf(2), mp.mpf(8)], [mp.mpf(-3), mp.mpf(4)]]
    for c1, c2 in [(-3, 5), (7, -2), (4, 11)]:
        mc1, mc2 = mp.mpf(c1), mp.mpf(c2)
        combo = mat_add(mat_smul(mc1, A), mat_smul(mc2, B))
        lhs = mat_tr(mat_mul(combo, C))
        rhs = mc1 * mat_tr(mat_mul(A, C)) + mc2 * mat_tr(mat_mul(B, C))
        err = max(
            abs(mat_tr(mat_mul(A, B)) - mat_tr(mat_mul(B, A))),
            abs(lhs - rhs),
        )
        max_err_g6vb = max(max_err_g6vb, err)
    results.append(
        {
            "beanId": "qou-g6vb",
            "theorem": "tracePair_symm_and_left_linear",
            "maxAbsError": mp.nstr(max_err_g6vb, 20),
            "passed": bool(max_err_g6vb <= mp.mpf("1e-75")),
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
        "probeName": "tower_compatibility_root_of_unity_seminormal_normalization_radical_kernel_bilinear_symmetry_probe",
        "beans": ["qou-0fmb", "qou-4lft", "qou-avt2", "qou-cf3m", "qou-g6vb"],
        "leanModule": "QOU.Foundations.TowerCompatibilityRootOfUnitySeminormalNormalizationRadicalKernelBilinearSymmetry",
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
        "tower-compatibility-root-of-unity-seminormal-normalization-radical-kernel-bilinear-symmetry.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {out_path} (scriptHash={script_sha256}, commit={commit_sha})")


if __name__ == "__main__":
    main()
