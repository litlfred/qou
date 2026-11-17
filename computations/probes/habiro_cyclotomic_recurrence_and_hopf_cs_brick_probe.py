#!/usr/bin/env python3
"""
80-dps mpmath witness probe for:
  folio/quantum-observable-universe/lean/QOU/QBeta/HabiroCyclotomicRecurrenceAndHopfCSBrick.lean

Beans:
  - qou-2w6j: habiro_cyclotomic_one_step_inhomogeneous_recurrence
  - qou-c9fh: hopf_link_chern_simons_pairing_nonzero_criterion
  - qou-dku0: figure_eight_habiro_tail_geometric_majorant_identity
  - qou-n5vg: twist_knot_distinguished_trace_field_quadratic_lock
  - qou-pwgw: figure_eight_branch_discriminant_and_norm_one_phase_lock
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPT_PATH = pathlib.Path(__file__).resolve()
WITNESS_PATH = SCRIPT_PATH.with_name(
    "habiro-cyclotomic-recurrence-and-hopf-cs-brick.witness.json"
)


def git_head_sha() -> str:
    return (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT)
        .decode("utf-8")
        .strip()
    )


def check_qou_2w6j() -> dict:
    # Habiro cyclotomic 1-step inhomogeneous recurrence under Chebyshev step
    q_val = mp.exp(mp.mpf("0.1041"))
    t_val = q_val + 1 / q_val
    c1 = mp.mpf("1")
    n_idx = 5
    u_prev = (q_val ** (n_idx - 1)) + (q_val ** -(n_idx - 1))
    u_curr = (q_val**n_idx) + (q_val**-n_idx)
    u_next = (q_val ** (n_idx + 1)) + (q_val ** -(n_idx + 1))

    cheb_residual = abs((u_next + u_prev) - t_val * u_curr)

    def j1(u_val: mp.mpf) -> mp.mpf:
        return 1 + c1 * (2 - u_val)

    lhs = j1(u_next) - t_val * j1(u_curr) + j1(u_prev)
    rhs = (2 - t_val) * (1 + 2 * c1)
    rec_residual = abs(lhs - rhs)

    passed = bool(
        cheb_residual < mp.mpf("1e-75")
        and rec_residual < mp.mpf("1e-75")
        and abs(rhs) > mp.mpf("1e-3")
    )
    return {
        "bean": "qou-2w6j",
        "theorem": "habiro_cyclotomic_one_step_inhomogeneous_recurrence",
        "passed": passed,
        "cheb_residual": mp.nstr(cheb_residual, 80),
        "rec_residual": mp.nstr(rec_residual, 80),
        "inhomogeneous_rhs": mp.nstr(rhs, 80),
    }


def check_qou_c9fh() -> dict:
    # Hopf link Chern-Simons pairing polarization, symmetry, and non-vanishing
    u1 = mp.pi / 5
    u2 = mp.pi / 7
    cs_12 = 2 * u1 * u2
    cs_21 = 2 * u2 * u1
    pol_rhs = ((u1 + u2) ** 2 - (u1 - u2) ** 2) / 2
    pol_residual = abs(cs_12 - pol_rhs)
    sym_residual = abs(cs_12 - cs_21)

    passed = bool(
        pol_residual < mp.mpf("1e-75")
        and sym_residual < mp.mpf("1e-75")
        and abs(cs_12) > mp.mpf("0.5")
    )
    return {
        "bean": "qou-c9fh",
        "theorem": "hopf_link_chern_simons_pairing_nonzero_criterion",
        "passed": passed,
        "pol_residual": mp.nstr(pol_residual, 80),
        "sym_residual": mp.nstr(sym_residual, 80),
        "cs_hopf_value": mp.nstr(cs_12, 80),
    }


def check_qou_dku0() -> dict:
    # Figure-eight Habiro geometric tail majorant telescoping identity
    t0 = mp.mpf("1.375")
    r = mp.mpf("0.3125")
    s3 = t0 + r * t0 + (r**2) * t0
    rem3 = (r**3) * t0
    tel_residual = abs(((1 - r) * s3 + rem3) - t0)

    passed = bool(
        tel_residual < mp.mpf("1e-75")
        and rem3 > mp.mpf("0.04")
    )
    return {
        "bean": "qou-dku0",
        "theorem": "figure_eight_habiro_tail_geometric_majorant_identity",
        "passed": passed,
        "tel_residual": mp.nstr(tel_residual, 80),
        "cubic_tail_remainder": mp.nstr(rem3, 80),
    }


def check_qou_n5vg() -> dict:
    # Distinguished twist-knot trace specialization at s = sqrt(3)
    s_val = mp.sqrt(3)
    l1 = 2 + s_val
    l2 = 2 - s_val
    sum_residual = abs((l1 + l2) - 4)
    prod_residual = abs(l1 * l2 - 1)
    disc_val = mp.mpf(-4) ** 2 - 4 * 1 * 1

    passed = bool(
        sum_residual < mp.mpf("1e-75")
        and prod_residual < mp.mpf("1e-75")
        and disc_val == 12
    )
    return {
        "bean": "qou-n5vg",
        "theorem": "twist_knot_distinguished_trace_field_quadratic_lock",
        "passed": passed,
        "sum_residual": mp.nstr(sum_residual, 80),
        "prod_residual": mp.nstr(prod_residual, 80),
        "root_l1": mp.nstr(l1, 80),
        "discriminant": mp.nstr(disc_val, 20),
    }


def check_qou_pwgw() -> dict:
    # Figure-eight A-polynomial norm-one branch discriminant and power sum
    theta = mp.pi / 3
    b_val = 2 * mp.cos(theta)  # b = 1, so b^2 = 1 < 4
    # In R-algebraic relations: L1 + L2 = b, L1 * L2 = 1 => L1^2 + L2^2 = b^2 - 2, (L1 - L2)^2 = b^2 - 4
    l1 = mp.exp(1j * theta)
    l2 = mp.exp(-1j * theta)
    diff_sq = mp.re((l1 - l2) ** 2)
    sum_sq = mp.re(l1**2 + l2**2)
    diff_sq_residual = abs(diff_sq - (b_val**2 - 4))
    sum_sq_residual = abs(sum_sq - (b_val**2 - 2))
    disc_val = b_val**2 - 4

    passed = bool(
        diff_sq_residual < mp.mpf("1e-75")
        and sum_sq_residual < mp.mpf("1e-75")
        and disc_val < mp.mpf("-2")
    )
    return {
        "bean": "qou-pwgw",
        "theorem": "figure_eight_branch_discriminant_and_norm_one_phase_lock",
        "passed": passed,
        "diff_sq_residual": mp.nstr(diff_sq_residual, 80),
        "sum_sq_residual": mp.nstr(sum_sq_residual, 80),
        "elliptic_discriminant": mp.nstr(disc_val, 80),
    }


def main() -> None:
    checks = [
        check_qou_2w6j(),
        check_qou_c9fh(),
        check_qou_dku0(),
        check_qou_n5vg(),
        check_qou_pwgw(),
    ]
    all_passed = all(c["passed"] for c in checks)
    script_bytes = SCRIPT_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()

    payload = {
        "probe": "computations/probes/habiro_cyclotomic_recurrence_and_hopf_cs_brick_probe.py",
        "beans": ["qou-2w6j", "qou-c9fh", "qou-dku0", "qou-n5vg", "qou-pwgw"],
        "precisionDps": 80,
        "scriptHash": script_hash,
        "scriptCommitSha": git_head_sha(),
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if not all_passed:
        raise SystemExit("One or more witness checks failed")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed})")


if __name__ == "__main__":
    main()
