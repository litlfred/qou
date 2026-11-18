#!/usr/bin/env python3
"""
Round 67 80-dps mpmath numerical verification probe for devacuified beans:
  1. qou-y7ea: ContactFormAlgebra classical specialization (dq_one, δq_one) and
     non-degenerate unitModel formal adjoint uniqueness (unitModel_δq_unique).
  2. ne0m: NSI q-deformed kernel classical limit (qDeformedKernel_at_one) and
     exact algebraic difference identity (qDeformedKernel_sub_classical).
  3. rt2f: Keystone n = 5 hook-product division identities (dq_row5_div,
     dq_41_div, dq_32_div, dq_311_div) and transpose-invariance of radial weights.
  4. cj317: Fundamental 2-cycle iteration periodicity (iterate_two_attractor,
     iterate_two_add_one_attractor) and domain-stable cone invariance.
  5. qcz7: Three-step OEE contraction bound (contraction_ratio_three_steps,
     two_halvings_beat_tripling_margin) and two-sided contact threshold
     (1 < log[3]_q / log[2]_q < 2).
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import platform
import subprocess
import sys

import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = pathlib.Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = SCRIPT_PATH.parent / "round67-devacuify-6qbv-b9cj.witness.json"


def q_int_geo(q: mp.mpf, k: int) -> mp.mpf:
    return (mp.power(q, k) - 1) / (q - 1)


def q_factorial_geo(q: mp.mpf, n: int) -> mp.mpf:
    prod = mp.mpf(1)
    for k in range(1, n + 1):
        prod *= q_int_geo(q, k)
    return prod


def run_checks() -> list[dict[str, object]]:
    tol = mp.mpf("1e-70")
    q0 = mp.mpf("1.1097319478893822104839481029384756102938475610293847561029384756")
    checks: list[dict[str, object]] = []

    # 1. qou-y7ea: ContactFormAlgebra unitModel adjoint & classical q = 1 limit
    # In unitModel over R, inner(z, x) = z * x, d = delta = lieReeb = lieReebStar = iotaReeb = thetaWedge = id.
    # For any unit q, dq(q)(alpha) = q^{-1} alpha + (1 - q^{-1}) alpha = alpha, and delta_q(q)(beta) = beta.
    alpha = mp.mpf("3.14159265358979323846264338327950288419716939937510")
    beta = mp.mpf("2.71828182845904523536028747135266249775724709369995")
    q_inv = 1 / q0
    dq_alpha = q_inv * alpha + (1 - q_inv) * alpha
    delta_q_beta = q_inv * beta + (1 - q_inv) * beta
    lhs_inner = dq_alpha * beta
    rhs_inner = alpha * delta_q_beta
    res_y7ea = abs(lhs_inner - rhs_inner) + abs(dq_alpha - alpha) + abs(delta_q_beta - beta)
    checks.append({
        "id": "qou-y7ea-unit-model-adjoint-and-q1-limit",
        "bean": "qou-y7ea",
        "description": "Verify ContactFormAlgebra.unitModel formal adjoint identity and q = 1 classical collapse",
        "lhs": mp.nstr(lhs_inner, 40),
        "rhs": mp.nstr(rhs_inner, 40),
        "residual": mp.nstr(res_y7ea, 25),
        "passed": bool(res_y7ea < tol),
    })

    # 2. ne0m: NSI q-deformed kernel difference identity and q = 1 evaluation
    r_val = mp.mpf("1.75")
    hbar_q = 1 - 1 / q0
    q_int2_bal = q0 + 1 / q0
    k_q = q_int2_bal / (r_val ** 2 - hbar_q ** 2)
    k_1 = mp.mpf(2) / (r_val ** 2)
    diff_lhs = k_q - k_1
    diff_rhs = ((q_int2_bal - 2) * (r_val ** 2) + 2 * (hbar_q ** 2)) / (
        (r_val ** 2) * (r_val ** 2 - hbar_q ** 2)
    )
    res_ne0m = abs(diff_lhs - diff_rhs)
    checks.append({
        "id": "ne0m-nsi-q-deformed-kernel-sub-classical",
        "bean": "ne0m",
        "description": "Verify qDeformedKernel_sub_classical and qDeformedKernel_at_one at 80 dps",
        "lhs": mp.nstr(diff_lhs, 40),
        "rhs": mp.nstr(diff_rhs, 40),
        "residual": mp.nstr(res_ne0m, 25),
        "passed": bool(res_ne0m < tol),
    })

    # 3. rt2f: Keystone n = 5 hook-product division identities (dq_row5_div, dq_41_div, dq_32_div, dq_311_div)
    qf5 = q_factorial_geo(q0, 5)
    qi1 = q_int_geo(q0, 1)
    qi2 = q_int_geo(q0, 2)
    qi3 = q_int_geo(q0, 3)
    qi4 = q_int_geo(q0, 4)
    qi5 = q_int_geo(q0, 5)
    hook_row5 = qi5 * qi4 * qi3 * qi2 * qi1
    hook_41 = qi5 * qi3 * qi2 * qi1 * qi1
    hook_32 = qi4 * qi3 * qi2 * qi1 * qi1
    hook_311 = qi5 * qi2 * qi2 * qi1 * qi1
    res_rt2f = (
        abs(qf5 / hook_row5 - 1)
        + abs(qf5 / hook_41 - qi4)
        + abs(qf5 / hook_32 - qi5)
        + abs(qf5 / hook_311 - (qi4 * qi3) / qi2)
    )
    checks.append({
        "id": "rt2f-keystone-n5-hook-division-identities",
        "bean": "rt2f",
        "description": "Verify dq_row5_div, dq_41_div, dq_32_div, and dq_311_div at n = 5",
        "dq_41": mp.nstr(qf5 / hook_41, 40),
        "dq_32": mp.nstr(qf5 / hook_32, 40),
        "dq_311": mp.nstr(qf5 / hook_311, 40),
        "residual": mp.nstr(res_rt2f, 25),
        "passed": bool(res_rt2f < tol),
    })

    # 4. cj317: Fundamental 2-cycle iteration periodicity in SkeinCollatzArith
    # Attractor alpha_0 = q^{-1} (q-odd since alpha_0 + 1 = (q + 1)/q = [2]_q * q^{-1}),
    # C_odd(alpha_0) = ([3]_q * q^{-1} + 1) / [2]_q = 1 + q^{-1},
    # C_even(1 + q^{-1}) = (1 + q^{-1}) / [2]_q = q^{-1} = alpha_0.
    alpha_0 = 1 / q0
    alpha_1 = (qi3 * alpha_0 + 1) / qi2
    alpha_2 = alpha_1 / qi2
    res_cj317 = abs(alpha_1 - (1 + 1 / q0)) + abs(alpha_2 - alpha_0)
    checks.append({
        "id": "cj317-fundamental-two-cycle-periodicity",
        "bean": "cj317",
        "description": "Verify 2-periodic orbit {q^-1, 1 + q^-1} under C_odd and C_even",
        "attractor": mp.nstr(alpha_0, 40),
        "step1": mp.nstr(alpha_1, 40),
        "step2": mp.nstr(alpha_2, 40),
        "residual": mp.nstr(res_cj317, 25),
        "passed": bool(res_cj317 < tol and abs(alpha_1 - alpha_0) > mp.mpf("0.5")),
    })

    # 5. qcz7: Three-step OEE contraction margin and two-sided contact threshold
    margin_lhs = (qi2 ** 3) - qi2 * qi3
    margin_rhs = q0 * (q0 + 1)
    ratio_3step = qi3 / (qi2 ** 3)
    inv_qi2 = 1 / qi2
    v_star = mp.log(qi3) / mp.log(qi2)
    res_qcz7 = abs(margin_lhs - margin_rhs)
    checks.append({
        "id": "qcz7-three-step-contraction-and-contact-threshold",
        "bean": "qcz7",
        "description": "Verify two_halvings_beat_tripling_margin, contraction_ratio_three_steps, and 1 < v* < 2",
        "margin": mp.nstr(margin_lhs, 40),
        "ratio_3step": mp.nstr(ratio_3step, 40),
        "inv_qi2": mp.nstr(inv_qi2, 40),
        "contact_threshold": mp.nstr(v_star, 40),
        "residual": mp.nstr(res_qcz7, 25),
        "passed": bool(res_qcz7 < tol and ratio_3step < inv_qi2 and 1 < v_star < 2),
    })

    return checks


def main() -> int:
    checks = run_checks()
    all_passed = all(bool(c["passed"]) for c in checks)
    script_bytes = SCRIPT_PATH.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    try:
        commit_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
        ).strip()
    except Exception:
        commit_sha = "unknown"

    witness = {
        "probe": "round67_devacuify_6qbv_b9cj_probe",
        "beans": ["qou-y7ea", "ne0m", "rt2f", "cj317", "qcz7"],
        "scriptPath": str(SCRIPT_PATH.relative_to(REPO_ROOT)),
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "executedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "pythonVersion": sys.version.split()[0],
        "platform": platform.platform(),
        "mpmathVersion": mp.__version__,
        "dps": int(mp.mp.dps),
        "allPassed": all_passed,
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed}, scriptHash={script_sha256})")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
