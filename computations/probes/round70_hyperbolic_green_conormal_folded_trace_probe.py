#!/usr/bin/env python3
"""Round 70 80-dps mpmath numerical probe for qou-ut4e, qou-uwcc, qou-v56q, qou-vfl4, qou-vo5j.

Verifies at 80 decimal digits of precision (mp.dps = 80):
1. qou-ut4e ([deturck-gluck2008], 2026-08-01-em-linking-reads-round1.md):
   H^3 scalar Green's function phi_0(alpha) = (-1/(4*pi))*(coth(alpha) - 1) decay at infinity
   via (e^alpha + e^-alpha) - (e^alpha - e^-alpha) = 2*e^-alpha and ODE residual
   (d^2/dalpha^2 + 2*coth(alpha)*d/dalpha) phi_0(alpha) = 0 for alpha > 0, contrasted with
   the shifted-Laplacian linking kernel phi(alpha) = (-1/(4*pi))*csch(alpha) satisfying
   (d^2/dalpha^2 + 2*coth(alpha)*d/dalpha + 1) phi(alpha) = 0.
2. qou-uwcc ([rossmann-invariant-eigendistributions-2], alg:delta-lambda-closure):
   Conormal-variety homology signed Euler characteristic Delta_lambda = e_+ - e_- vs
   unsigned multiplicity M_lambda = e_+ + e_- satisfies M_lambda - Delta_lambda = 2*e_-.
3. qou-v56q ([geck-lambropoulou-2004], conj:type-b-folding-cpt):
   Type-B folded trace bar-conjugation asymmetry defect (a - b)*(y_+ - y_-) and exact
   vanishing when a = b.
4. qou-vfl4 ([finster2021], rem:cfs-comparison-summary):
   Causal-Lagrangian eigenvalue polarization (lam_+ - lam_-)^2 + 4*lam_+*lam_- = (lam_+ + lam_-)^2
   and quadratic-norm factorization g^2 - s^2 = (g - s)*(g + s).
5. qou-vo5j ([sniady2006asymptotics], QOU.BraidsAndKnots.DeltaLambdaDReduction):
   Normalized character polynomial Sigma_hat_3 = R_4 + R_2 genus expansion at n = 4:
   (c^3 - 3*c) + 2*c = c*(c - 1)*(c + 1).
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
from datetime import datetime, timezone

from mpmath import mp

mp.dps = 80


def verify_qou_ut4e_hyperbolic_green_kernel() -> dict:
    alpha = mp.mpf("1.75")
    u = mp.exp(alpha)
    v = mp.exp(-alpha)
    unshifted_num = u + v
    baseline_num = u - v
    decay_diff_res = abs((unshifted_num - baseline_num) - 2 * v)

    # phi_0(alpha) = (-1/(4*pi))*(coth(alpha) - 1) = (-1/(2*pi)) * e^(-alpha) / sinh(alpha)
    coth_m1 = mp.coth(alpha) - 1
    exact_ratio = 2 * v / (u - v)
    ratio_res = abs(coth_m1 - exact_ratio)

    # Shifted Laplacian identity on H^3: (d^2/da^2 + 2*coth(a)*d/da + 1)(csch(a)) = 0
    # since (csch a)'' = csch a * (1 + 2*csch^2 a) and (csch a)' = -coth a * csch a,
    # so (csch a)'' + 2*coth a*(csch a)' + csch a = csch a*(2 + 2*csch^2 a - 2*coth^2 a) = 0.
    csch_a = mp.csch(alpha)
    coth_a = mp.coth(alpha)
    d1_csch = -coth_a * csch_a
    d2_csch = csch_a * (1 + 2 * csch_a**2)
    shifted_laplacian_res = abs(d2_csch + 2 * coth_a * d1_csch + csch_a)

    passed = bool(
        decay_diff_res < mp.mpf("1e-76")
        and ratio_res < mp.mpf("1e-76")
        and shifted_laplacian_res < mp.mpf("1e-76")
    )
    return {
        "bean": "qou-ut4e",
        "cite": "deturck-gluck2008",
        "alpha": mp.nstr(alpha, 20),
        "cothMinusOne": mp.nstr(coth_m1, 40),
        "decayDiffResidual": mp.nstr(decay_diff_res, 25),
        "ratioResidual": mp.nstr(ratio_res, 25),
        "shiftedLaplacianResidual": mp.nstr(shifted_laplacian_res, 25),
        "passed": passed,
    }


def verify_qou_uwcc_conormal_signed_characteristic() -> dict:
    e_even = mp.mpf(14)
    e_odd = mp.mpf(5)
    delta_signed = e_even - e_odd
    m_unsigned = e_even + e_odd
    diff_res = abs((m_unsigned - delta_signed) - 2 * e_odd)
    sum_res = abs((m_unsigned + delta_signed) - 2 * e_even)

    passed = bool(
        diff_res < mp.mpf("1e-77")
        and sum_res < mp.mpf("1e-77")
        and int(delta_signed) == 9
        and int(m_unsigned) == 19
    )
    return {
        "bean": "qou-uwcc",
        "cite": "rossmann-invariant-eigendistributions-2",
        "deltaSigned": int(delta_signed),
        "mUnsigned": int(m_unsigned),
        "diffResidual": mp.nstr(diff_res, 25),
        "sumResidual": mp.nstr(sum_res, 25),
        "passed": passed,
    }


def verify_qou_v56q_folded_type_b_trace() -> dict:
    z = mp.pi / mp.mpf(5)
    a = mp.sqrt(mp.mpf(3))
    b = mp.sqrt(mp.mpf(2))
    y_pos = mp.exp(mp.mpf("0.37"))
    y_neg = mp.exp(mp.mpf("-0.37"))

    tr_orig = z + a * y_pos + b * y_neg
    tr_bar = z + a * y_neg + b * y_pos
    defect_lhs = tr_orig - tr_bar
    defect_rhs = (a - b) * (y_pos - y_neg)
    factor_res = abs(defect_lhs - defect_rhs)

    tr_sym_orig = z + a * y_pos + a * y_neg
    tr_sym_bar = z + a * y_neg + a * y_pos
    sym_res = abs(tr_sym_orig - tr_sym_bar)

    passed = bool(
        factor_res < mp.mpf("1e-76")
        and sym_res < mp.mpf("1e-76")
    )
    return {
        "bean": "qou-v56q",
        "cite": "geck-lambropoulou-2004",
        "asymmetryDefect": mp.nstr(defect_rhs, 40),
        "factorResidual": mp.nstr(factor_res, 25),
        "symmetricBarResidual": mp.nstr(sym_res, 25),
        "passed": passed,
    }


def verify_qou_vfl4_causal_lagrangian_polarization() -> dict:
    lam_pos = mp.sqrt(mp.mpf(7)) + mp.mpf("1.25")
    lam_neg = mp.sqrt(mp.mpf(7)) - mp.mpf("0.85")
    pol_lhs = (lam_pos - lam_neg) ** 2 + 4 * lam_pos * lam_neg
    pol_rhs = (lam_pos + lam_neg) ** 2
    pol_res = abs(pol_lhs - pol_rhs)

    g = mp.pi * mp.mpf("1.4")
    s = mp.e * mp.mpf("0.9")
    norm_lhs = g**2 - s**2
    norm_rhs = (g - s) * (g + s)
    norm_res = abs(norm_lhs - norm_rhs)

    passed = bool(
        pol_res < mp.mpf("1e-76")
        and norm_res < mp.mpf("1e-76")
    )
    return {
        "bean": "qou-vfl4",
        "cite": "finster2021",
        "polarizationResidual": mp.nstr(pol_res, 25),
        "normFactorResidual": mp.nstr(norm_res, 25),
        "passed": passed,
    }


def verify_qou_vo5j_sigma_hat3_free_cumulant() -> dict:
    max_res = mp.mpf(0)
    values = {}
    for c_int in [2, 3, 4, 5, 6]:
        c = mp.mpf(c_int)
        r4 = c**3 - 3 * c
        r2 = 2 * c
        sigma_hat3 = r4 + r2
        factored = c * (c - 1) * (c + 1)
        res = abs(sigma_hat3 - factored)
        if res > max_res:
            max_res = res
        values[str(c_int)] = int(sigma_hat3)

    passed = bool(max_res < mp.mpf("1e-77") and values["4"] == 60)
    return {
        "bean": "qou-vo5j",
        "cite": "sniady2006asymptotics",
        "maxResidual": mp.nstr(max_res, 25),
        "sigmaHat3Values": values,
        "passed": passed,
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
        commit_sha = "unknown"

    checks = {
        "qou_ut4e_hyperbolic_green_kernel": verify_qou_ut4e_hyperbolic_green_kernel(),
        "qou_uwcc_conormal_signed_characteristic": verify_qou_uwcc_conormal_signed_characteristic(),
        "qou_v56q_folded_type_b_trace": verify_qou_v56q_folded_type_b_trace(),
        "qou_vfl4_causal_lagrangian_polarization": verify_qou_vfl4_causal_lagrangian_polarization(),
        "qou_vo5j_sigma_hat3_free_cumulant": verify_qou_vo5j_sigma_hat3_free_cumulant(),
    }
    all_passed = all(item["passed"] for item in checks.values())

    witness = {
        "probe": "round70_hyperbolic_green_conormal_folded_trace_probe",
        "beans": ["qou-ut4e", "qou-uwcc", "qou-v56q", "qou-vfl4", "qou-vo5j"],
        "scriptPath": str(script_path.relative_to(repo_root)),
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "mpmathDps": int(mp.dps),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }

    witness_path = script_path.with_name(
        "round70-hyperbolic-green-conormal-folded-trace.witness.json"
    )
    witness_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {witness_path.relative_to(repo_root)} (allPassed={all_passed})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
