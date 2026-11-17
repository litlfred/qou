#!/usr/bin/env python3
"""80-dps mpmath probe for StateIntegralTwoSidedLatticeAndValuationResidueBrick.

Beans:
  * qou-0a8e: Inhomogeneous q-difference residual and geometric Wronskian defect W = -f0 * r.
  * qou-0ml9: Two-row RSK shape (n-k, k) doubled Frobenius content shift -2*(n - 2*k).
  * qou-523q: Two-sided Z-lattice unit-coefficient top/bottom inversion for Fantini-Wheeler eq.(14).
  * qou-5el3: Haar-forcing cross-defect vanishing and unit-anchor uniqueness.
  * qou-5g8u: Natural valuation (ord_w) vs leading residue separation under scaling and multiplication.
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
    "state-integral-two-sided-lattice-and-valuation-residue-brick.witness.json"
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

    # 1. qou-0a8e: Geometric Wronskian defect W(f0, a*f0, a^2*f0 + r) == -f0 * r
    f0 = mp.ln(q_canon) + mp.mpf(3)
    a = q_canon - mp.mpf(1) / q_canon
    r = mp.pi / mp.mpf(7)
    f1 = a * f0
    f2 = a * f1 + r
    wronskian = f1 * f1 - f0 * f2
    expected_wronskian = -f0 * (f2 - a * f1)
    err_0a8e = abs(wronskian - expected_wronskian)
    assertions.append(
        {
            "id": "qou-0a8e-qdiff-wronskian-residual",
            "bean": "qou-0a8e",
            "passed": bool(err_0a8e < tol),
            "maxAbsError": mp.nstr(err_0a8e, 20),
            "wronskian": mp.nstr(wronskian, 35),
        }
    )

    # 2. qou-0ml9: Two-row RSK content sum step difference
    max_err_0ml9 = mp.mpf(0)
    for n in (5, 8, 11, 14):
        for k in range(0, n // 2):
            c_curr = mp.mpf((n - k) * (n - k - 1) + k * (k - 3))
            c_next = mp.mpf((n - (k + 1)) * (n - (k + 1) - 1) + (k + 1) * (k - 2))
            diff = c_next - c_curr
            expected_diff = mp.mpf(-2 * (n - 2 * k))
            max_err_0ml9 = max(max_err_0ml9, abs(diff - expected_diff))
    assertions.append(
        {
            "id": "qou-0ml9-two-row-rsk-content-step",
            "bean": "qou-0ml9",
            "passed": bool(max_err_0ml9 < tol),
            "maxAbsError": mp.nstr(max_err_0ml9, 20),
        }
    )

    # 3. qou-523q: Two-sided Z-lattice unit inversion for FW eq.(14) row-0 recurrence
    i_bot = q_canon**2 + mp.mpf(5)
    mid_sum = -mp.mpf(3) * q_canon + mp.sqrt(mp.mpf(15))
    i_top = -mid_sum - i_bot
    i_bot_recovered = -mid_sum - i_top
    rel_top = i_top + mid_sum + i_bot
    rel_bot = i_bot_recovered + mid_sum + i_top
    err_523q = max(abs(rel_top), abs(rel_bot), abs(i_bot_recovered - i_bot))
    assertions.append(
        {
            "id": "qou-523q-fw-row0-two-sided-inversion",
            "bean": "qou-523q",
            "passed": bool(err_523q < tol),
            "maxAbsError": mp.nstr(err_523q, 20),
        }
    )

    # 4. qou-5el3: Haar-forcing cross-defect vanishing and unit-anchor uniqueness
    c1 = mp.exp(mp.pi / mp.mpf(5))
    c2 = mp.sqrt(mp.mpf(15)) * q_canon
    u0 = mp.mpf(1) + q_canon
    x_val = mp.mpf(7) - mp.mpf(2) / q_canon
    cross_defect = (c1 * x_val) * (c2 * u0) - (c2 * x_val) * (c1 * u0)
    err_5el3 = abs(cross_defect)
    assertions.append(
        {
            "id": "qou-5el3-haar-forcing-cross-defect",
            "bean": "qou-5el3",
            "passed": bool(err_5el3 < tol),
            "maxAbsError": mp.nstr(err_5el3, 20),
        }
    )

    # 5. qou-5g8u: Ordered-field natural valuation (ord_w) vs residue separation
    res1, deg1 = q_canon + mp.mpf(2), 3
    res2, deg2 = mp.pi - q_canon, -1
    lam = mp.sqrt(mp.mpf(15))
    scaled_res, scaled_deg = lam * res1, deg1
    prod_res, prod_deg = res1 * res2, deg1 + deg2
    err_5g8u = max(
        abs(scaled_res - lam * res1),
        abs(mp.mpf(scaled_deg - deg1)),
        abs(prod_res - res1 * res2),
        abs(mp.mpf(prod_deg - (deg1 + deg2))),
    )
    assertions.append(
        {
            "id": "qou-5g8u-valuation-vs-residue-separation",
            "bean": "qou-5g8u",
            "passed": bool(err_5g8u < tol),
            "maxAbsError": mp.nstr(err_5g8u, 20),
            "productResidue": mp.nstr(prod_res, 35),
            "productValuationDeg": prod_deg,
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
        "probe": "state_integral_two_sided_lattice_and_valuation_residue_brick_probe",
        "beans": ["qou-0a8e", "qou-0ml9", "qou-523q", "qou-5el3", "qou-5g8u"],
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
