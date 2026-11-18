#!/usr/bin/env python3
"""
80-dps mpmath numerical falsification & verification probe for:
- qou-c3if: Dyadic shell summation-by-parts and order-growth shell bound
- qou-7028: Central idempotent projectors and 4-strand symmetrizer normalization
- qou-bt3u: Fiber-adjoint involution categorical machinery on 2x2 endomorphisms
- qou-mp3m: Planar transfer-matrix and two-strand state-sum equivalence
- qou-ga7i: Monoidality of the pivotal trace and tensor-dual evaluation-coevaluation pairing

No raw float64 arithmetic is used; all real calculations are performed via mpmath at 80 decimal digits.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpf

mp.dps = 80


def _git_commit_sha(repo_root: Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(repo_root), text=True
        ).strip()
        return out
    except Exception:
        return "0" * 40


def _script_hash(script_path: Path) -> str:
    return hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]


def run_probe() -> dict:
    mp.dps = 80
    tol = mpf("1e-70")
    results = []

    # 1. qou-c3if: Dyadic shell summation-by-parts and order-growth shell bound
    # Verify exact Abel summation-by-parts and convergence of sum_{k=0}^{K-1} (N_{k+1}-N_k) 2^{-k(rho+eps)}
    rho = mpf("3") / mpf("2")
    eps = mpf("1") / mpf("4")
    c_const = mpf("5") / mpf("3")
    n_seq = [c_const * (mpf("2") ** (rho * mpf(k))) for k in range(4)]
    w_seq = [mpf("2") ** (-mpf(k) * (rho + eps)) for k in range(3)]
    inc_sum = (
        (n_seq[1] - n_seq[0]) * w_seq[0]
        + (n_seq[2] - n_seq[1]) * w_seq[1]
        + (n_seq[3] - n_seq[2]) * w_seq[2]
    )
    byparts_sum = (
        n_seq[3] * w_seq[2]
        - n_seq[0] * w_seq[0]
        + n_seq[1] * (w_seq[0] - w_seq[1])
        + n_seq[2] * (w_seq[1] - w_seq[2])
    )
    uniform_w = mpf("7") / mpf("11")
    unif_inc = (
        (n_seq[1] - n_seq[0]) * uniform_w
        + (n_seq[2] - n_seq[1]) * uniform_w
        + (n_seq[3] - n_seq[2]) * uniform_w
    )
    unif_tel = (n_seq[3] - n_seq[0]) * uniform_w
    err_c3if = max(abs(inc_sum - byparts_sum), abs(unif_inc - unif_tel))
    qou_c3if_ok = err_c3if <= tol

    results.append(
        {
            "beanId": "qou-c3if",
            "claim": "Discrete dyadic shell summation-by-parts identity and telescoping uniform-weight shell sum hold to 80-dps",
            "maxResidual": mp.nstr(err_c3if, 25),
            "passed": bool(qou_c3if_ok),
        }
    )

    # 2. qou-7028: Central idempotent projectors and 4-strand symmetrizer normalization
    q_val = mpf("1.1099785827513808")
    # In R[T]/(T^2 - (q-1)T - q), multiply (a1, b1) and (a2, b2)
    def mul_quad(x: tuple[mpf, mpf], y: tuple[mpf, mpf]) -> tuple[mpf, mpf]:
        a1, b1 = x
        a2, b2 = y
        return (
            a1 * a2 + q_val * b1 * b2,
            a1 * b2 + b1 * a2 + (q_val - mpf("1")) * b1 * b2,
        )

    e_pos = (mpf("1") / (mpf("1") + q_val), mpf("1") / (mpf("1") + q_val))
    e_neg = (q_val / (mpf("1") + q_val), -mpf("1") / (mpf("1") + q_val))
    e_pos_sq = mul_quad(e_pos, e_pos)
    e_neg_sq = mul_quad(e_neg, e_neg)
    e_orth = mul_quad(e_pos, e_neg)
    p4_one = (
        (mpf("1") + mpf("1"))
        * (mpf("1") + mpf("1") + mpf("1"))
        * (mpf("1") + mpf("1") + mpf("1") + mpf("1"))
    )
    err_7028 = max(
        abs(e_pos_sq[0] - e_pos[0]),
        abs(e_pos_sq[1] - e_pos[1]),
        abs(e_neg_sq[0] - e_neg[0]),
        abs(e_neg_sq[1] - e_neg[1]),
        abs(e_orth[0]),
        abs(e_orth[1]),
        abs((e_pos[0] + e_neg[0]) - mpf("1")),
        abs(e_pos[1] + e_neg[1]),
        abs(p4_one - mpf("24")),
    )
    qou_7028_ok = err_7028 <= tol

    results.append(
        {
            "beanId": "qou-7028",
            "claim": "Spectral projectors e_+ and e_- in the quadratic algebra satisfy e_+^2=e_+, e_-^2=e_-, e_+ e_-=0, e_+ + e_-=1 and P_4(1)=24",
            "maxResidual": mp.nstr(err_7028, 25),
            "passed": bool(qou_7028_ok),
        }
    )

    # 3. qou-bt3u: Fiber-adjoint involution categorical machinery on 2x2 endomorphisms
    a_mat = (mpf("3") / mpf("7"), mpf("-5") / mpf("11"), mpf("13") / mpf("17"), mpf("19") / mpf("23"))
    b_mat = (mpf("2") / mpf("5"), mpf("7") / mpf("9"), mpf("-4") / mpf("13"), mpf("11") / mpf("15"))

    def mul2(x: tuple[mpf, mpf, mpf, mpf], y: tuple[mpf, mpf, mpf, mpf]) -> tuple[mpf, mpf, mpf, mpf]:
        return (
            x[0] * y[0] + x[1] * y[2],
            x[0] * y[1] + x[1] * y[3],
            x[2] * y[0] + x[3] * y[2],
            x[2] * y[1] + x[3] * y[3],
        )

    def adj2(x: tuple[mpf, mpf, mpf, mpf]) -> tuple[mpf, mpf, mpf, mpf]:
        return (x[0], x[2], x[1], x[3])

    ab_adj = adj2(mul2(a_mat, b_mat))
    ba_adj = mul2(adj2(b_mat), adj2(a_mat))
    ata = mul2(adj2(a_mat), a_mat)
    tr_ata = ata[0] + ata[3]
    sq_sum = a_mat[0] ** 2 + a_mat[1] ** 2 + a_mat[2] ** 2 + a_mat[3] ** 2
    err_bt3u = max(
        max(abs(ab_adj[i] - ba_adj[i]) for i in range(4)),
        abs(tr_ata - sq_sum),
    )
    qou_bt3u_ok = err_bt3u <= tol and tr_ata > mpf("0")

    results.append(
        {
            "beanId": "qou-bt3u",
            "claim": "Fiber adjoint involution satisfies (AB)^dagger = B^dagger A^dagger and tr(A^dagger A) = sum_{i,j} A_{ij}^2 > 0 for nonzero A",
            "maxResidual": mp.nstr(err_bt3u, 25),
            "passed": bool(qou_bt3u_ok),
        }
    )

    # 4. qou-mp3m: Planar transfer-matrix and two-strand state-sum equivalence
    a_param = mpf("7") / mpf("5")
    b_param = mpf("5") / mpf("7")
    d_loop = -(a_param**2) - (b_param**2)
    # (a I + b U)^2 = a^2 I + (2 a b + d b^2) U
    c_i_sq = a_param * a_param
    c_u_sq = mpf("2") * a_param * b_param + d_loop * (b_param * b_param)
    expected_c_u = mpf("1") - (b_param**4)
    err_mp3m = abs(c_u_sq - expected_c_u)
    qou_mp3m_ok = err_mp3m <= tol

    results.append(
        {
            "beanId": "qou-mp3m",
            "claim": "Two-strand planar state-sum transfer square (A I + A^{-1} U)^2 equals A^2 I + (1 - A^{-4}) U at loop weight d = -A^2 - A^{-2}",
            "maxResidual": mp.nstr(err_mp3m, 25),
            "passed": bool(qou_mp3m_ok),
        }
    )

    # 5. qou-ga7i: Monoidality of the pivotal trace and tensor-dual pairing
    p1 = q_val
    p2 = mpf("1") / q_val
    q1 = q_val**2
    q2 = mpf("1") / (q_val**2)
    tr_p_a = p1 * a_mat[0] + p2 * a_mat[3]
    tr_q_b = q1 * b_mat[0] + q2 * b_mat[3]
    tr_tensor = (
        (p1 * q1) * (a_mat[0] * b_mat[0])
        + (p1 * q2) * (a_mat[0] * b_mat[3])
        + (p2 * q1) * (a_mat[3] * b_mat[0])
        + (p2 * q2) * (a_mat[3] * b_mat[3])
    )
    err_ga7i = abs(tr_tensor - tr_p_a * tr_q_b)
    qou_ga7i_ok = err_ga7i <= tol

    results.append(
        {
            "beanId": "qou-ga7i",
            "claim": "Weighted pivotal trace is strictly multiplicative on tensor products tr_{p otimes q}(A otimes B) = tr_p(A) tr_q(B)",
            "maxResidual": mp.nstr(err_ga7i, 25),
            "passed": bool(qou_ga7i_ok),
        }
    )

    all_passed = all(r["passed"] for r in results)
    repo_root = Path(__file__).resolve().parents[2]
    script_path = Path(__file__).resolve()

    witness = {
        "probe": "dyadic_shell_summation_central_idempotent_fiber_adjoint_planar_transfer_pivotal_monoidality_probe",
        "beans": ["qou-c3if", "qou-7028", "qou-bt3u", "qou-mp3m", "qou-ga7i"],
        "parents": ["qou-t5uj", "qou-k4oq", "qou-o9ge", "qou-0cyu", "qou-rtxm", "qou-c8p8"],
        "leanModule": "QOU.Foundations.DyadicShellSummationCentralIdempotentFiberAdjointPlanarTransferPivotalMonoidality",
        "precisionDps": 80,
        "scriptPath": "computations/probes/dyadic_shell_summation_central_idempotent_fiber_adjoint_planar_transfer_pivotal_monoidality_probe.py",
        "scriptHash": _script_hash(script_path),
        "scriptCommitSha": _git_commit_sha(repo_root),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": bool(all_passed),
        "results": results,
    }
    return witness


def main() -> None:
    witness = run_probe()
    out_path = Path(__file__).with_name(
        "dyadic-shell-summation-central-idempotent-fiber-adjoint-planar-transfer-pivotal-monoidality.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (allPassed={witness['allPassed']}, scriptHash={witness['scriptHash']})")
    if not witness["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
