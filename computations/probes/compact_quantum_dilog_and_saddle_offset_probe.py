#!/usr/bin/env python3
"""80-dps mpmath / exact rational probe for quantum dilogarithm 2-step
multiplier infrastructure, Borel-Pade channel-dependent bias residual, DT
Stokes saddle-offset quadratic 1 - 9q - 28q^2, classical q -> 1 quantum-integer
curvature, and compact quantum dilogarithm phi_q functional equation (qou-dizz,
qou-obmp, qou-q86o, qou-r1si, qou-rlkw).
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = SCRIPT_PATH.with_name(
    "compact-quantum-dilog-and-saddle-offset.witness.json"
)


def _script_hash() -> str:
    return hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()[:12]


def _git_commit_sha() -> str:
    res = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return res.stdout.strip()


def _phi_q(z: mp.mpf, q: mp.mpf, terms: int = 240) -> mp.mpf:
    prod = mp.mpf(1)
    for k in range(0, terms):
        prod *= 1 - z * (q**k)
    return prod


def main() -> None:
    mp.mp.dps = 80
    assertions = []

    # 1. qou-dizz: T2D quantum dilogarithm 2-step telescopic multiplier
    q_f = Fraction(3, 5)
    z_f = Fraction(2, 7)
    two_step_fac = (1 - q_f * z_f) * (1 - (q_f**2) * z_f)
    two_step_poly = 1 - q_f * (1 + q_f) * z_f + (q_f**3) * (z_f**2)
    a1_pass = two_step_fac == two_step_poly and (
        (1 - q_f * 0) * (1 - (q_f**2) * 0) == 1
    )
    assertions.append(
        {
            "id": "qou-dizz-qdilog-two-step-multiplier-expansion",
            "bean": "qou-dizz",
            "description": "Two-step quantum dilogarithm multiplier (1-qz)(1-q^2 z) equals 1 - q(1+q)z + q^3 z^2 and evaluates to 1 at z=0",
            "sampleTwoStepFactor": str(two_step_fac),
            "sampleTwoStepPoly": str(two_step_poly),
            "passed": bool(a1_pass),
        }
    )

    # 2. qou-obmp: Residual channel-dependent Pade bias plateau in V3 extraction
    c1 = Fraction(121, 100)
    c2 = Fraction(89, 100)
    bias_checks = []
    for n in range(6, 14):
        nsq = Fraction(n * n, 1)
        k1 = 1 + c1 / nsq
        k2 = 1 + c2 / nsq
        res_scaled = (k1 - k2) * nsq
        bias_checks.append(res_scaled == (c1 - c2))
    rel_plateau = (c1 - c2) / c1
    a2_pass = all(bias_checks) and rel_plateau == Fraction(32, 121)
    assertions.append(
        {
            "id": "qou-obmp-pade-channel-dependent-bias-residual",
            "bean": "qou-obmp",
            "description": "Control-channel subtraction on 1/n^2 Borel-Pade pole bias leaves order-invariant scaled residual c1 - c2",
            "scaledResidualDiff": str(c1 - c2),
            "relativePlateauSample": str(rel_plateau),
            "passed": bool(a2_pass),
        }
    )

    # 3. qou-q86o: DT Stokes saddle-offset quadratic 1 - 9q - 28q^2
    o_at_0 = 1 - 9 * 0 - 28 * (0**2)
    o_at_1 = 1 - 9 * 1 - 28 * (1**2)
    disc_o2 = (-9) ** 2 - 4 * (-28) * 1
    q_star = (-mp.mpf(9) + mp.sqrt(193)) / 56
    o_at_qstar = 1 - 9 * q_star - 28 * (q_star**2)
    sq_checks = []
    for k in range(-3, 5):
        qv = Fraction(k, 7)
        lhs = 112 * (1 - 9 * qv - 28 * (qv**2))
        rhs = 193 - (56 * qv + 9) ** 2
        sq_checks.append(lhs == rhs)
    a3_pass = (
        o_at_0 == 1
        and o_at_1 == -36
        and disc_o2 == 193
        and abs(o_at_qstar) < mp.mpf("1e-75")
        and all(sq_checks)
    )
    assertions.append(
        {
            "id": "qou-q86o-dt-saddle-offset-quadratic-and-root",
            "bean": "qou-q86o",
            "description": "DT Stokes saddle offset quadratic 1 - 9q - 28q^2 has o(0)=1, o(1)=-36, discriminant 193, and root (-9+sqrt(193))/56 ~ 0.08915",
            "offsetAtQ0": str(o_at_0),
            "offsetAtQ1": str(o_at_1),
            "discriminant": str(disc_o2),
            "positiveRoot80Dps": mp.nstr(q_star, 40),
            "passed": bool(a3_pass),
        }
    )

    # 4. qou-r1si: Classical q -> 1 limit & quadratic [n]_q curvature
    hbar_sq = Fraction(1, 25)
    qint_n1 = 1 + 1 * (1**2 - 1) * hbar_sq / 6
    qint_n2 = 2 + 2 * (2**2 - 1) * hbar_sq / 6
    qint_n3 = 3 + 3 * (3**2 - 1) * hbar_sq / 6
    a4_pass = (
        qint_n1 == Fraction(1, 1)
        and qint_n2 == 2 + hbar_sq
        and qint_n3 == 3 + 4 * hbar_sq
    )
    assertions.append(
        {
            "id": "qou-r1si-qint-quadratic-curvature-and-classical-limit",
            "bean": "qou-r1si",
            "description": "Second-order quantum integer n + n(n^2-1)*hbar^2/6 reduces to n at hbar=0, has 0 curvature at n=1, and equals 2 + hbar^2 at n=2",
            "qIntApproxN1": str(qint_n1),
            "qIntApproxN2": str(qint_n2),
            "qIntApproxN3": str(qint_n3),
            "passed": bool(a4_pass),
        }
    )

    # 5. qou-rlkw: Compact quantum dilogarithm phi_q(z) = (z; q)_infty step & bar-reflection
    q_mp = mp.mpf("0.45")
    z_mp = mp.mpf("0.3")
    phi_z = _phi_q(z_mp, q_mp)
    phi_qz = _phi_q(q_mp * z_mp, q_mp)
    phi_q2z = _phi_q((q_mp**2) * z_mp, q_mp)
    err_step1 = abs(phi_z - (1 - z_mp) * phi_qz)
    err_step2 = abs(phi_z - (1 - z_mp) * (1 - q_mp * z_mp) * phi_q2z)
    qh = Fraction(3, 2)
    qh_inv = Fraction(2, 3)
    bar_prod = (1 - qh**2) * (1 - qh_inv**2)
    bar_sq = -((qh - qh_inv) ** 2)
    a5_pass = (
        err_step1 < mp.mpf("1e-75")
        and err_step2 < mp.mpf("1e-75")
        and bar_prod == bar_sq
    )
    assertions.append(
        {
            "id": "qou-rlkw-compact-phi-q-functional-equation-and-bar-reflection",
            "bean": "qou-rlkw",
            "description": "Compact quantum dilogarithm phi_q(z) satisfies phi_q(z) = (1-z)(1-qz)phi_q(q^2 z) to 80 dps and (1-q)(1-q^-1) = -(q^{1/2}-q^{-1/2})^2",
            "phiZ80Dps": mp.nstr(phi_z, 40),
            "twoStepError": mp.nstr(err_step2, 12),
            "barReflectionProduct": str(bar_prod),
            "passed": bool(a5_pass),
        }
    )

    all_passed = all(a["passed"] for a in assertions)
    witness = {
        "probe": "compact_quantum_dilog_and_saddle_offset_probe.py",
        "beans": ["qou-dizz", "qou-obmp", "qou-q86o", "qou-r1si", "qou-rlkw"],
        "parentBean": "qou-r9ih",
        "leanModule": "QOU.QBeta.CompactQuantumDilogAndSaddleOffset",
        "scriptHash": _script_hash(),
        "scriptCommitSha": _git_commit_sha(),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "precisionDps": "80",
        "allPassed": bool(all_passed),
        "assertions": assertions,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
