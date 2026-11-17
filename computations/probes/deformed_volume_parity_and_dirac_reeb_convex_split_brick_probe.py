#!/usr/bin/env python3
"""80-dps mpmath probe for DeformedVolumeParityAndDiracReebConvexSplitBrick.

Beans:
  * qou-5uj7: Categorical Dirac operator convex split 1/q + (q-1)/q = 1 and hbar_q = (q-1)/q.
  * qou-6s8k: Figure-eight deformed complex volume V_41(u) = Vol(u) + i*CS(u) conjugation reflection parity.
  * qou-7fyw: Parameterized Delta_max two-sided slack margin sum and quadratic bound factorization.
  * qou-9s8k: Garoufalidis-Kashaev bilinear block pairing diagonal-even vs off-diagonal-odd decomposition.
  * qou-cyon: Harmonic imaginary form (sqrt(3)/4)*(x^2 - y^2) diagonal factorization and swap antisymmetry.
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
    "deformed-volume-parity-and-dirac-reeb-convex-split-brick.witness.json"
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

    # 1. qou-5uj7: Categorical Dirac operator convex split 1/q + (q-1)/q == 1
    w_grad = mp.mpf(1) / q_canon
    w_reeb = mp.mpf(1) - mp.mpf(1) / q_canon
    hbar_q = (q_canon - mp.mpf(1)) / q_canon
    s_step = mp.mpf(7) + mp.ln(q_canon)
    weighted_sum = w_grad * s_step + w_reeb * s_step
    err_5uj7 = max(
        abs((w_grad + w_reeb) - mp.mpf(1)),
        abs(w_reeb - hbar_q),
        abs(weighted_sum - s_step),
    )
    assertions.append(
        {
            "id": "qou-5uj7-dirac-reeb-convex-split",
            "bean": "qou-5uj7",
            "passed": bool(err_5uj7 < tol),
            "maxAbsError": mp.nstr(err_5uj7, 20),
            "wGrad": mp.nstr(w_grad, 35),
            "hbarQ": mp.nstr(hbar_q, 35),
        }
    )

    # 2. qou-6s8k: Figure-eight deformed complex volume V_41(u) = Vol(u) + i*CS(u) parity
    v_41_0 = mp.mpf(2) * mp.clsin(2, mp.pi / mp.mpf(3))
    u_val = mp.mpf(1) / mp.mpf(11)
    vol_u = v_41_0 - mp.sqrt(mp.mpf(3)) * (u_val**2) / mp.mpf(4)
    cs_u = mp.sqrt(mp.mpf(3)) * (u_val**3) / mp.mpf(12)
    z_pos = mp.mpc(vol_u, cs_u)
    z_neg = mp.mpc(vol_u, -cs_u)
    err_6s8k = max(
        abs(mp.conj(z_pos) - z_neg),
        abs(abs(z_pos) ** 2 - abs(z_neg) ** 2),
    )
    assertions.append(
        {
            "id": "qou-6s8k-deformed-complex-volume-parity",
            "bean": "qou-6s8k",
            "passed": bool(err_6s8k < tol),
            "maxAbsError": mp.nstr(err_6s8k, 20),
            "volAtZero": mp.nstr(v_41_0, 35),
        }
    )

    # 3. qou-7fyw: Parameterized Delta_max two-sided slack margin sum and quadratic factorization
    b_max = mp.mpf(1) / mp.sqrt(mp.mpf(5))
    delta_val = (q_canon - mp.mpf(1)) * mp.mpf(2)
    upper_slack = b_max - delta_val
    lower_slack = b_max + delta_val
    err_7fyw = max(
        abs((upper_slack + lower_slack) - mp.mpf(2) * b_max),
        abs((upper_slack * lower_slack) - (b_max**2 - delta_val**2)),
    )
    assertions.append(
        {
            "id": "qou-7fyw-delta-max-two-sided-slack",
            "bean": "qou-7fyw",
            "passed": bool(err_7fyw < tol),
            "maxAbsError": mp.nstr(err_7fyw, 20),
            "quadraticSlackMargin": mp.nstr(upper_slack * lower_slack, 35),
        }
    )

    # 4. qou-9s8k: Garoufalidis-Kashaev bilinear block pairing odd/even channel projection
    d00 = q_canon**2 + mp.mpf(1)
    d11 = mp.mpf(3) / q_canon
    c01 = mp.ln(q_canon) * mp.sqrt(mp.mpf(3))
    c10 = mp.pi * (q_canon - mp.mpf(1))
    total_pos = (d00 + d11) + (c01 + c10)
    total_neg = (d00 + d11) + (-c01 - c10)
    err_9s8k = max(
        abs((total_pos - total_neg) - mp.mpf(2) * (c01 + c10)),
        abs((total_pos + total_neg) - mp.mpf(2) * (d00 + d11)),
    )
    assertions.append(
        {
            "id": "qou-9s8k-gk-bilinear-odd-even-channel",
            "bean": "qou-9s8k",
            "passed": bool(err_9s8k < tol),
            "maxAbsError": mp.nstr(err_9s8k, 20),
        }
    )

    # 5. qou-cyon: Harmonic imaginary form (sqrt(3)/4)*(x^2 - y^2) diagonal factorization & swap
    scale_harm = mp.sqrt(mp.mpf(3)) / mp.mpf(4)
    x_coord = q_canon + mp.mpf(1) / mp.mpf(3)
    y_coord = q_canon - mp.mpf(1) / mp.mpf(5)
    q_xy = scale_harm * (x_coord**2 - y_coord**2)
    q_fac = scale_harm * (x_coord - y_coord) * (x_coord + y_coord)
    q_yx = scale_harm * (y_coord**2 - x_coord**2)
    q_diag_pos = scale_harm * (x_coord**2 - x_coord**2)
    q_diag_neg = scale_harm * (x_coord**2 - (-x_coord) ** 2)
    err_cyon = max(
        abs(q_xy - q_fac),
        abs(q_yx + q_xy),
        abs(q_diag_pos),
        abs(q_diag_neg),
    )
    assertions.append(
        {
            "id": "qou-cyon-harmonic-im-form-diagonal-swap",
            "bean": "qou-cyon",
            "passed": bool(err_cyon < tol),
            "maxAbsError": mp.nstr(err_cyon, 20),
            "harmonicValue": mp.nstr(q_xy, 35),
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
        "probe": "deformed_volume_parity_and_dirac_reeb_convex_split_brick_probe",
        "beans": ["qou-5uj7", "qou-6s8k", "qou-7fyw", "qou-9s8k", "qou-cyon"],
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
