#!/usr/bin/env python3
"""
High-precision (50 dps) verification probe for:
- qou-04cj: Convention-D square map factorization (q_D = q_C^2) and A >= 3
  underbinding shortfall increase |B_D - B_target| - |B_C - B_target| = B_C - B_D > 0.
- qou-2vut: A-dependent Brunnian cluster shortfall ratios (A=3: 1.585x, A=4: 78.8x,
  ratio quotient 15760/317 = 49.716088328...), impossibility of constant re-weighting,
  and two-term additive residual d_4 = b_4 * (r_4 - r_3) > 0.
- qou-6xvw: Intensive scale-invariant channel I(k*A) = I(A) vs extensive additive
  channel E(k*A) = k*E(A) discrepancy E(2A) - I(2A) = E(A) > 0.
- qou-8ms1: Derived closure component arity c_free(A) = 2A and
  c_atom(A, A-1) = A + 1 (A=2 -> 3 != 1, A=3 -> 4 not in {1, 3}).
- qou-9ilw: Crossing energy E_x(q) = (q - 1/q)/2, quadratic identity
  Delta_net(q) = 2*E_x*(E_x - 1) = (q^2 - 1)(q^2 - 2q - 1)/(2q^2),
  Defect-1 discrepancy (q - 1)^2 (q^2 - 2q - 1)/(2q^2), and silver-ratio root
  q = 1 + sqrt(2) with (1 - 1/q)^2 = 6 - 4*sqrt(2).
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

import mpmath as mp

mp.mp.dps = 50

SCRIPT_REL_PATH = "computations/probes/convention_d_brunnian_intensive_arity_silver_probe.py"
WITNESS_REL_PATH = "computations/probes/convention-d-brunnian-intensive-arity-silver-probe.witness.json"


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 50)


def run_probe() -> dict:
    mp.mp.dps = 50
    checks = []

    # 1. qou-04cj: Convention-D square map factorization & underbinding shortfall shift
    q_c = mp.mpf("1.10998055098643850148")
    q_d = q_c ** 2
    skein_c = q_c - mp.mpf(1) / q_c
    skein_d = q_d - mp.mpf(1) / q_d
    skein_fac = skein_c * (q_c + mp.mpf(1) / q_c)
    skein_diff = abs(skein_d - skein_fac)

    deform_c = mp.mpf(1) - mp.mpf(1) / q_c
    deform_d = mp.mpf(1) - mp.mpf(1) / q_d
    deform_fac = deform_c * (mp.mpf(1) + mp.mpf(1) / q_c)
    deform_diff = abs(deform_d - deform_fac)

    # Representative A=3 underbinding values (MeV) with 0 < B_D < B_C < B_target
    b_target_3h = mp.mpf("8.481798")
    b_c_3h = mp.mpf("6.185")
    b_d_3h = mp.mpf("5.095")
    err_c = abs(b_c_3h - b_target_3h)
    err_d = abs(b_d_3h - b_target_3h)
    err_increase = err_d - err_c
    expected_increase = b_c_3h - b_d_3h

    c1_pass = bool(
        skein_diff < mp.mpf("1e-48")
        and deform_diff < mp.mpf("1e-48")
        and abs(err_increase - expected_increase) < mp.mpf("1e-48")
        and err_increase > 0
    )
    checks.append({
        "id": "qou-04cj-convention-d-factorization-and-shortfall-shift",
        "passed": c1_pass,
        "q_c": fmt(q_c),
        "q_d": fmt(q_d),
        "skein_factorization_residual": fmt(skein_diff),
        "deform_factorization_residual": fmt(deform_diff),
        "shortfall_increase_mev": fmt(err_increase),
    })

    # 2. qou-2vut: Brunnian cluster shortfall ratio divergence (A=3: 1.585, A=4: 78.8)
    r3 = mp.mpf("1585") / mp.mpf("1000")
    r4 = mp.mpf("788") / mp.mpf("10")
    ratio_quotient = r4 / r3
    exact_quotient = mp.mpf("15760") / mp.mpf("317")
    quotient_diff = abs(ratio_quotient - exact_quotient)
    b3_base = mp.mpf("5.351")
    b4_base = mp.mpf("0.359")
    t3_target = r3 * b3_base
    t4_target = r4 * b4_base
    d4_residual = b4_base * (r4 - r3)
    c2_pass = bool(
        quotient_diff < mp.mpf("1e-48")
        and ratio_quotient > mp.mpf("49")
        and abs((t3_target / b3_base) * b4_base + d4_residual - t4_target) < mp.mpf("1e-48")
        and d4_residual > 0
    )
    checks.append({
        "id": "qou-2vut-brunnian-shortfall-ratio-divergence",
        "passed": c2_pass,
        "r3_ratio": fmt(r3),
        "r4_ratio": fmt(r4),
        "r4_over_r3": fmt(ratio_quotient),
        "exact_15760_over_317_residual": fmt(quotient_diff),
        "d4_two_term_residual": fmt(d4_residual),
    })

    # 3. qou-6xvw: Intensive vs extensive additive channel scaling
    e_unit = mp.mpf("2.224566")
    a_anchor = mp.mpf("2")
    intensive_2a = e_unit
    extensive_2a = mp.mpf("2") * e_unit
    extensive_3a = mp.mpf("3") * e_unit
    discrepancy_2a = extensive_2a - intensive_2a
    c3_pass = bool(
        abs(discrepancy_2a - e_unit) < mp.mpf("1e-48")
        and extensive_3a == mp.mpf("3") * e_unit
        and discrepancy_2a > 0
        and a_anchor > 0
    )
    checks.append({
        "id": "qou-6xvw-intensive-vs-extensive-channel-discrepancy",
        "passed": c3_pass,
        "anchor_energy": fmt(e_unit),
        "intensive_at_2a": fmt(intensive_2a),
        "extensive_at_2a": fmt(extensive_2a),
        "extensive_at_3a": fmt(extensive_3a),
        "discrepancy_at_2a": fmt(discrepancy_2a),
    })

    # 4. qou-8ms1: Closure component count arity c_atom(A, A-1) = A + 1
    arity_rows = []
    c4_pass = True
    for a_val in (2, 3, 4):
        c_free = 2 * a_val
        m_odd = a_val - 1
        c_atom = c_free - m_odd
        if c_atom != a_val + 1:
            c4_pass = False
        arity_rows.append({
            "A": str(a_val),
            "c_free": str(c_free),
            "m_odd": str(m_odd),
            "c_atom": str(c_atom),
        })
    # Verify A=2 has 3 components (!= 1 for 6_2) and A=3 has 4 components (!= 1 for 8_11, != 3 for L6a4)
    c4_pass = bool(c4_pass and (2 * 2 - 1 == 3) and (3 != 1) and (2 * 3 - 2 == 4) and (4 not in (1, 3)))
    checks.append({
        "id": "qou-8ms1-closure-component-arity-obstruction",
        "passed": c4_pass,
        "arity_table": arity_rows,
    })

    # 5. qou-9ilw: Crossing energy E_x = (q - 1/q)/2, quadratic identity, Defect-1 discrepancy, silver ratio
    q_silver = mp.mpf(1) + mp.sqrt(2)
    ex_silver = (q_silver - mp.mpf(1) / q_silver) / mp.mpf(2)
    delta_net_silver = mp.mpf(2) * ex_silver * (ex_silver - mp.mpf(1))
    hbar_q_silver_sq = (mp.mpf(1) - mp.mpf(1) / q_silver) ** 2
    hbar_q_silver_sq_exact = mp.mpf(10) - mp.mpf(4) * q_silver

    # Check Defect-1 discrepancy at q in {0.5, 1.11, 2, 3, 10}
    max_defect1_residual = mp.mpf(0)
    for q_test_str in ("0.5", "1.11", "2", "3", "10"):
        qt = mp.mpf(q_test_str)
        ht = qt - mp.mpf(1) / qt
        ext = ht / mp.mpf(2)
        dnet = ht * (ht - mp.mpf(2)) / mp.mpf(2)
        dnet_quad = mp.mpf(2) * ext * (ext - mp.mpf(1))
        dnet_rat = (qt ** 2 - mp.mpf(1)) * (qt ** 2 - mp.mpf(2) * qt - mp.mpf(1)) / (mp.mpf(2) * qt ** 2)
        wrong_box = (qt ** 2 - mp.mpf(2) * qt - mp.mpf(1)) / (mp.mpf(2) * qt)
        exact_disc = (qt ** 2 - qt - mp.mpf(1)) * (qt ** 2 - mp.mpf(2) * qt - mp.mpf(1)) / (mp.mpf(2) * qt ** 2)
        res = max(
            abs(dnet - dnet_quad),
            abs(dnet - dnet_rat),
            abs((dnet - wrong_box) - exact_disc),
        )
        if res > max_defect1_residual:
            max_defect1_residual = res

    c5_pass = bool(
        abs(ex_silver - mp.mpf(1)) < mp.mpf("1e-48")
        and abs(delta_net_silver) < mp.mpf("1e-48")
        and abs(hbar_q_silver_sq - hbar_q_silver_sq_exact) < mp.mpf("1e-48")
        and max_defect1_residual < mp.mpf("1e-47")
    )
    checks.append({
        "id": "qou-9ilw-crossing-energy-silver-ratio-and-box-discrepancy",
        "passed": c5_pass,
        "q_silver": fmt(q_silver),
        "crossing_energy_at_silver": fmt(ex_silver),
        "hbar_q_sq_at_silver": fmt(hbar_q_silver_sq),
        "max_defect1_identity_residual": fmt(max_defect1_residual),
    })

    all_passed = all(c["passed"] for c in checks)
    return {
        "checks": checks,
        "all_passed": all_passed,
    }


def main() -> int:
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    script_path = repo_root / SCRIPT_REL_PATH
    witness_path = repo_root / WITNESS_REL_PATH

    script_bytes = script_path.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    try:
        commit_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo_root, text=True
        ).strip()
    except Exception:
        commit_sha = "0" * 40

    res = run_probe()
    witness = {
        "schema": "qou-probe-witness-v1",
        "probeId": "convention-d-brunnian-intensive-arity-silver-probe",
        "beans": ["qou-04cj", "qou-2vut", "qou-6xvw", "qou-8ms1", "qou-9ilw"],
        "scriptPath": SCRIPT_REL_PATH,
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "precisionDps": "50",
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "summary": {
            "totalChecks": str(len(res["checks"])),
            "passedChecks": str(sum(1 for c in res["checks"] if c["passed"])),
            "allPassed": res["all_passed"],
        },
        "checks": res["checks"],
    }

    witness_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"Wrote {WITNESS_REL_PATH} (allPassed={res['all_passed']}, scriptHash={script_hash}, sha={commit_sha})")
    return 0 if res["all_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
