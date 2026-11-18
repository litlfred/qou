#!/usr/bin/env python3
"""80-dps mpmath numerical probe for Round 76 beans:
qou-gmfz, qou-img9, qou-phir, qou-siin, qou-l25z.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80


def check_gmfz() -> dict:
    """Verify triBar_involutive_and_classical_limit at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (2, 3, -5, 7, 11),
        (-4, 5, 2, -9, 13),
        (7, -11, 17, 23, -19),
    ]
    for d, s0, s1, x0, x1 in samples:
        d_m, s0_m, s1_m, x0_m, x1_m = map(mp.mpf, (d, s0, s1, x0, x1))
        # triBar d (x0, x1) = (x0 + d * x1, x1)
        b1_0 = x0_m + d_m * x1_m
        b1_1 = x1_m
        # triBar (-d) (triBar d v)
        b2_0 = b1_0 + (-d_m) * b1_1
        b2_1 = b1_1
        err_inv = abs(b2_0 - x0_m) + abs(b2_1 - x1_m)
        # obsLinear shift
        obs_bar = s0_m * b1_0 + s1_m * b1_1
        obs_orig = s0_m * x0_m + s1_m * x1_m
        err_shift = abs((obs_bar - obs_orig) - (s0_m * d_m) * x1_m)
        max_err = max(max_err, err_inv, err_shift)
    return {
        "beanId": "qou-gmfz",
        "theorem": "triBar_involutive_and_classical_limit",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_img9() -> dict:
    """Verify simple_refl_quad_zero_vs_wordLen2_residual at 80-dps."""
    max_err = mp.mpf(0)
    for q in (-3, -2, 0, 1, 2, 3, 5, 11):
        qm = mp.mpf(q)
        # reflGen1 = (q, -1), reflGen2 = (-1, q), wordLen2 = (-q, -q)
        r1_0 = qm * qm - (qm - 1) * qm - qm
        r1_1 = (-1) * (-1) - (qm - 1) * (-1) - qm
        w_0 = (-qm) * (-qm) - (qm - 1) * (-qm) - qm
        expected_w = 2 * (qm * qm) - 2 * qm
        err = abs(r1_0) + abs(r1_1) + abs(w_0 - expected_w)
        max_err = max(max_err, err)
    return {
        "beanId": "qou-img9",
        "theorem": "simple_refl_quad_zero_vs_wordLen2_residual",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_phir() -> dict:
    """Verify rightDichotomyOp_basis_and_quadratic_identity at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (2, 3, -5),
        (-3, 7, 11),
        (5, -13, 17),
    ]
    for q, x0, x1 in samples:
        qm, x0m, x1m = map(mp.mpf, (q, x0, x1))
        r1_0 = qm * x1m
        r1_1 = x0m + (qm - 1) * x1m
        r2_0 = qm * r1_1
        r2_1 = r1_0 + (qm - 1) * r1_1
        rhs_0 = (qm - 1) * r1_0 + qm * x0m
        rhs_1 = (qm - 1) * r1_1 + qm * x1m
        err = abs(r2_0 - rhs_0) + abs(r2_1 - rhs_1)
        max_err = max(max_err, err)
    return {
        "beanId": "qou-phir",
        "theorem": "rightDichotomyOp_basis_and_quadratic_identity",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_siin() -> dict:
    """Verify rescaledQuadPoly_eq_mul_rootQuadPoly_and_euler_invariance at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (2, 1, 3, 5, 7, 11, 13, 17),
        (-3, 2, -5, 8, 4, 9, -2, 6),
        (5, -4, 7, 12, 19, 23, -7, 11),
    ]
    for u, v, n, b0, b1, b2, d1, d2 in samples:
        um, vm, nm, b0m, b1m, b2m, d1m, d2m = map(
            mp.mpf, (u, v, n, b0, b1, b2, d1, d2)
        )
        root_poly = nm * nm - (um - vm) * nm - um * vm
        tm = um * nm
        rescaled = tm * tm - (um * um - um * vm) * tm - (um * um) * (um * vm)
        err_poly = abs(rescaled - (um * um) * root_poly)
        euler_shifted = (b0m + d1m) - (b1m + d1m + d2m) + (b2m + d2m)
        euler_orig = b0m - b1m + b2m
        err_euler = abs(euler_shifted - euler_orig)
        max_err = max(max_err, err_poly, err_euler)
    return {
        "beanId": "qou-siin",
        "theorem": "rescaledQuadPoly_eq_mul_rootQuadPoly_and_euler_invariance",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def check_l25z() -> dict:
    """Verify writhe_relators_and_uniform_generator_vanishing at 80-dps."""
    max_err = mp.mpf(0)
    samples = [
        (3, -5, 1, 7, -11, 13),
        (-4, 9, 2, -6, 15, -8),
    ]
    for ei, ej, w, w1, w2, w3 in samples:
        eim, ejm, wm, w1m, w2m, w3m = map(mp.mpf, (ei, ej, w, w1, w2, w3))
        far_comm = eim + ejm - eim - ejm
        braid_rel = (eim + ejm + eim) - (ejm + eim + ejm)
        braid_unif = (wm + wm + wm) - (wm + wm + wm)
        assoc_err = abs(((w1m + w2m) + w3m) - (w1m + (w2m + w3m)))
        err = abs(far_comm) + abs(braid_rel - (eim - ejm)) + abs(braid_unif) + assoc_err
        max_err = max(max_err, err)
    return {
        "beanId": "qou-l25z",
        "theorem": "writhe_relators_and_uniform_generator_vanishing",
        "maxAbsError": mp.nstr(max_err, 20),
        "passed": bool(max_err == 0),
    }


def main() -> None:
    script_path = pathlib.Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_bytes = script_path.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    try:
        commit_sha = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "UNKNOWN"

    checks = [
        check_gmfz(),
        check_img9(),
        check_phir(),
        check_siin(),
        check_l25z(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "schemaVersion": "1.0",
        "probeName": "triangular_bar_involution_length_two_quadratic_defect_right_multiplication_dichotomy_root_parameter_rescaling_writhe_homomorphism_probe",
        "beans": ["qou-gmfz", "qou-img9", "qou-phir", "qou-siin", "qou-l25z"],
        "leanModule": "QOU.Foundations.TriangularBarInvolutionLengthTwoQuadraticDefectRightMultiplicationDichotomyRootParameterRescalingWritheHomomorphism",
        "mpmathDps": 80,
        "scriptPath": "computations/probes/triangular_bar_involution_length_two_quadratic_defect_right_multiplication_dichotomy_root_parameter_rescaling_writhe_homomorphism_probe.py",
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }

    witness_path = script_path.with_name(
        "triangular-bar-involution-length-two-quadratic-defect-right-multiplication-dichotomy-root-parameter-rescaling-writhe-homomorphism.witness.json"
    )
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {witness_path} (scriptHash={script_sha256}, commit={commit_sha})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
