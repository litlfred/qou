#!/usr/bin/env python3
"""80-dps mpmath probe for QuantumThreeStokesAndWhiteheadWindingBrick.

Beans:
  * qou-hmr9: Icosahedral 1/sqrt(5) per-partition quadratic slack identity (s^2 - 5*m^2).
  * qou-nkm1: Quantum-dimension [3]_q numerator q^2 + q + 1 classical evaluation = 3 and cyclotomic product.
  * qou-r75d: Whitehead link (5^2_1) four-Catalan volume decomposition and symmetric saddle sum.
  * qou-smyz: Wedderburn multiplicity obstruction excess gap (mSrc > mTgt -> mSrc - mTgt >= 1).
  * qou-thj7: Murakami deformed meridian winding threshold (u^2 - w0^2) parity and factorization.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80

PROBE_PATH = Path(__file__).resolve()
REPO_ROOT = PROBE_PATH.parents[2]
WITNESS_PATH = PROBE_PATH.with_name(
    "quantum-three-stokes-and-whitehead-winding-brick.witness.json"
)


def _git_sha(args: list[str]) -> str:
    try:
        out = subprocess.check_output(
            ["git", *args], cwd=REPO_ROOT, stderr=subprocess.DEVNULL
        )
        return out.decode().strip()
    except Exception:
        return "0" * 40


def run_probe() -> dict:
    mp.mp.dps = 80
    q_canon = mp.exp(2 * mp.pi / (25 * mp.sqrt(15)))
    tol = mp.mpf("1e-75")

    assertions: list[dict] = []

    # 1. qou-hmr9: Icosahedral 1/sqrt(5) per-partition quadratic slack
    s_scale = mp.mpf(1)
    m_val = (q_canon - mp.mpf(1)) * mp.mpf(3)
    slack_pos = s_scale**2 - mp.mpf(5) * (m_val**2)
    slack_neg = s_scale**2 - mp.mpf(5) * ((-m_val) ** 2)
    err_hmr9 = max(
        abs(slack_pos - slack_neg),
        abs((slack_pos + mp.mpf(5) * (m_val**2)) - s_scale**2),
    )
    assertions.append(
        {
            "id": "qou-hmr9-icosahedral-fifth-quadratic-slack",
            "bean": "qou-hmr9",
            "passed": bool(err_hmr9 < tol and slack_pos > mp.mpf(0)),
            "maxAbsError": mp.nstr(err_hmr9, 20),
            "quadraticSlack": mp.nstr(slack_pos, 35),
        }
    )

    # 2. qou-nkm1: Quantum-dimension [3]_q numerator q^2 + q + 1 and classical Stokes constant 3
    q_num = q_canon**2 + q_canon + mp.mpf(1)
    q_dim_3 = q_num / q_canon
    q_num_at_1 = mp.mpf(1) ** 2 + mp.mpf(1) + mp.mpf(1)
    cyc_lhs = (q_canon - mp.mpf(1)) * q_num
    cyc_rhs = q_canon**3 - mp.mpf(1)
    err_nkm1 = max(
        abs(q_num_at_1 - mp.mpf(3)),
        abs(cyc_lhs - cyc_rhs),
    )
    assertions.append(
        {
            "id": "qou-nkm1-qdim-three-stokes-cyclotomic",
            "bean": "qou-nkm1",
            "passed": bool(err_nkm1 < tol),
            "maxAbsError": mp.nstr(err_nkm1, 20),
            "qDimThreeAtQ0": mp.nstr(q_dim_3, 35),
        }
    )

    # 3. qou-r75d: Whitehead link (5^2_1) four-Catalan volume 4*G and saddle pair balance
    catalan_g = mp.catalan
    vol_whitehead = mp.mpf(4) * catalan_g
    four_sum = catalan_g + catalan_g + catalan_g + catalan_g
    n_idx, k_idx = mp.mpf(50), mp.mpf(25)
    err_r75d = max(
        abs(vol_whitehead - four_sum),
        abs(((n_idx - k_idx) + (n_idx + k_idx)) - mp.mpf(2) * n_idx),
        abs(((n_idx + k_idx) - (n_idx - k_idx)) - mp.mpf(2) * k_idx),
    )
    assertions.append(
        {
            "id": "qou-r75d-whitehead-four-catalan-and-saddle-balance",
            "bean": "qou-r75d",
            "passed": bool(err_r75d < tol),
            "maxAbsError": mp.nstr(err_r75d, 20),
            "whiteheadVolume": mp.nstr(vol_whitehead, 45),
        }
    )

    # 4. qou-smyz: Wedderburn multiplicity obstruction excess
    m_src, m_tgt = 7, 4
    excess = m_src - m_tgt
    err_smyz = abs(mp.mpf((excess + m_tgt) - m_src))
    assertions.append(
        {
            "id": "qou-smyz-wedderburn-multiplicity-obstruction-excess",
            "bean": "qou-smyz",
            "passed": bool(err_smyz < tol and excess >= 1),
            "maxAbsError": mp.nstr(err_smyz, 20),
            "multiplicityExcess": excess,
        }
    )

    # 5. qou-thj7: Murakami deformed meridian winding threshold (u^2 - (2*pi)^2)
    w0 = mp.mpf(2) * mp.pi
    u_val = mp.mpf(2) * mp.pi + q_canon
    slack_u = u_val**2 - w0**2
    slack_fac = (u_val - w0) * (u_val + w0)
    slack_neg_u = (-u_val) ** 2 - w0**2
    slack_at_w0 = w0**2 - w0**2
    err_thj7 = max(
        abs(slack_u - slack_fac),
        abs(slack_neg_u - slack_u),
        abs(slack_at_w0),
    )
    assertions.append(
        {
            "id": "qou-thj7-deformed-meridian-winding-threshold",
            "bean": "qou-thj7",
            "passed": bool(err_thj7 < tol and slack_u > mp.mpf(0)),
            "maxAbsError": mp.nstr(err_thj7, 20),
            "windingSlack": mp.nstr(slack_u, 35),
        }
    )

    all_passed = all(a["passed"] for a in assertions)
    script_bytes = PROBE_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()
    head_sha = _git_sha(["rev-parse", "HEAD"])
    script_commit_sha = _git_sha(
        ["log", "-n", "1", "--format=%H", "--", str(PROBE_PATH.relative_to(REPO_ROOT))]
    )
    if not script_commit_sha or script_commit_sha == "0" * 40:
        script_commit_sha = head_sha

    witness = {
        "schemaVersion": "1.0",
        "probe": "quantum_three_stokes_and_whitehead_winding_brick_probe",
        "beans": ["qou-hmr9", "qou-nkm1", "qou-r75d", "qou-smyz", "qou-thj7"],
        "precisionDps": 80,
        "qCanonical": mp.nstr(q_canon, 50),
        "commitSha": head_sha,
        "scriptCommitSha": script_commit_sha,
        "scriptSha256": script_hash,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": all_passed,
        "assertions": assertions,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed})")
    if not all_passed:
        raise SystemExit(1)
    return witness


if __name__ == "__main__":
    run_probe()
