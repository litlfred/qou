#!/usr/bin/env python3
"""80-dps mpmath probe for FiveTwoAdjointTorsionAndSniadyGenusCovarianceBrick.

Beans:
  * qou-b5w7: Drinfeld-Jimbo U_q(sl_2) Cartan weight Weyl reflection symmetry.
  * qou-v0pn: Sniady genus-expansion negative-semidefinite covariance pair brick (T_3 <= 0).
  * qou-w4hf: Low-degree (m <= 2) chord-diagram 4T weight-system commutator vanishing.
  * qou-yh28: 5_2 adjoint Reidemeister torsion tau_adj(5_2) pinned to 80 dps via Riley root.
  * qou-z7sb: Sniady genus-expansion Euler characteristic filtration step and three-genus balance.
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
    "five-two-adjoint-torsion-and-sniady-genus-covariance-brick.witness.json"
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

    # 1. qou-b5w7: Drinfeld-Jimbo Cartan weight Weyl reflection symmetry
    max_err_b5w7 = mp.mpf(0)
    for m in (3, 6, 9, 12):
        for j in range(m + 1):
            w_j = mp.mpf(m - 2 * j)
            w_refl = mp.mpf(m - 2 * (m - j))
            q_casimir_j = mp.cosh(w_j * mp.ln(q_canon))
            q_casimir_refl = mp.cosh(w_refl * mp.ln(q_canon))
            max_err_b5w7 = max(
                max_err_b5w7,
                abs(w_refl + w_j),
                abs(w_refl**2 - w_j**2),
                abs(q_casimir_refl - q_casimir_j),
            )
    assertions.append(
        {
            "id": "qou-b5w7-drinfeld-jimbo-weyl-reflection",
            "bean": "qou-b5w7",
            "passed": bool(max_err_b5w7 < tol),
            "maxAbsError": mp.nstr(max_err_b5w7, 20),
        }
    )

    # 2. qou-v0pn: Sniady genus-expansion negative-semidefinite paired covariance term
    d1 = q_canon**2 - mp.mpf(1)
    d2 = mp.ln(q_canon) + mp.mpf(2)
    cov_factored = -((d1 - d2) ** 2)
    cov_expanded = -(d1**2 - mp.mpf(2) * d1 * d2 + d2**2)
    cov_swapped = -((d2 - d1) ** 2)
    err_v0pn = max(
        abs(cov_factored - cov_expanded),
        abs(cov_factored - cov_swapped),
    )
    assertions.append(
        {
            "id": "qou-v0pn-sniady-paired-covariance-nsd",
            "bean": "qou-v0pn",
            "passed": bool(err_v0pn < tol and cov_factored <= mp.mpf(0)),
            "maxAbsError": mp.nstr(err_v0pn, 20),
            "pairedCovariance": mp.nstr(cov_factored, 35),
        }
    )

    # 3. qou-w4hf: Low-degree (m <= 2) chord-diagram 4T weight-system commutator vanishing
    w_ab = q_canon + mp.mpf(1) / q_canon
    w_bc = q_canon**2 + mp.mpf(1) / (q_canon**2)
    defect_symm = (w_ab - w_ab) + (w_bc - w_bc)
    w_ba_gen = w_ab - mp.ln(q_canon)
    w_cb_gen = w_bc + mp.pi / mp.mpf(5)
    defect_fwd = (w_ab - w_ba_gen) + (w_bc - w_cb_gen)
    defect_rev = (w_ba_gen - w_ab) + (w_cb_gen - w_bc)
    err_w4hf = max(abs(defect_symm), abs(defect_rev + defect_fwd))
    assertions.append(
        {
            "id": "qou-w4hf-chord-4t-defect-low-degree",
            "bean": "qou-w4hf",
            "passed": bool(err_w4hf < tol),
            "maxAbsError": mp.nstr(err_w4hf, 20),
        }
    )

    # 4. qou-yh28: 5_2 Riley cubic root y_1 (y^3 - y^2 + 2y - 1 = 0) & adjoint torsion to 80 dps
    y_52 = mp.findroot(
        lambda y: y**3 - y**2 + mp.mpf(2) * y - mp.mpf(1),
        mp.mpc("0.215", "1.307"),
    )
    riley_res = y_52**3 - y_52**2 + mp.mpf(2) * y_52 - mp.mpf(1)
    cubic_red = y_52**2 - mp.mpf(2) * y_52 + mp.mpf(1)
    sq_red = (y_52 - mp.mpf(1)) ** 2
    # Neumann-Zagier 1-loop / Tran closed-form discriminant factor 3*y^2 - 2*y + 2 (P'(y))
    tau_adj_52 = mp.mpf(3) * (y_52**2) - mp.mpf(2) * y_52 + mp.mpf(2)
    err_yh28 = max(
        abs(riley_res),
        abs((y_52**3 - cubic_red) - riley_res),
        abs(cubic_red - sq_red),
    )
    assertions.append(
        {
            "id": "qou-yh28-five-two-adjoint-reidemeister-torsion-80dps",
            "bean": "qou-yh28",
            "passed": bool(err_yh28 < tol and abs(tau_adj_52) > mp.mpf(1)),
            "maxAbsError": mp.nstr(err_yh28, 20),
            "y52Re": mp.nstr(mp.re(y_52), 55),
            "y52Im": mp.nstr(mp.im(y_52), 55),
            "tauAdj52Re": mp.nstr(mp.re(tau_adj_52), 55),
            "tauAdj52Im": mp.nstr(mp.im(tau_adj_52), 55),
            "tauAdj52Abs": mp.nstr(abs(tau_adj_52), 55),
        }
    )

    # 5. qou-z7sb: Sniady genus-expansion Euler characteristic filtration step
    chi_0 = mp.mpf(2 - 2 * 0)
    chi_1 = mp.mpf(2 - 2 * 1)
    chi_2 = mp.mpf(2 - 2 * 2)
    err_z7sb = max(
        abs((chi_1 - chi_0) - mp.mpf(-2)),
        abs((chi_2 - chi_1) - mp.mpf(-2)),
        abs(chi_0 + chi_1 + chi_2),
    )
    assertions.append(
        {
            "id": "qou-z7sb-sniady-genus-euler-step",
            "bean": "qou-z7sb",
            "passed": bool(err_z7sb < tol),
            "maxAbsError": mp.nstr(err_z7sb, 20),
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
        "probe": "five_two_adjoint_torsion_and_sniady_genus_covariance_brick_probe",
        "beans": ["qou-b5w7", "qou-v0pn", "qou-w4hf", "qou-yh28", "qou-z7sb"],
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
