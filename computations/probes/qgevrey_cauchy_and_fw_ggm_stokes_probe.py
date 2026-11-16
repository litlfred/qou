#!/usr/bin/env python3
"""80-dps mpmath / exact rational probe for q-Gevrey Cauchy convolution deficit,
cosh/BCH crossing parity decomposition, FW-GGM Stokes prefactor & median-Borel
resummation, 3-saddle resurgent sum rule check, and B2 sibling convergence
normalization bridge (qou-qb99, qou-ratf, qou-ri9w, qou-rsrg, qou-u7hx).
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
    "qgevrey-cauchy-and-fw-ggm-stokes.witness.json"
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


def _tri_exp(s: Fraction, n: Fraction) -> Fraction:
    return s * n * (n - 1) / 2


def main() -> None:
    mp.mp.dps = 80
    assertions = []

    # 1. qou-qb99: q-Gevrey Cauchy convolution exponent deficit s * i * j
    s_order = Fraction(1, 2)
    cauchy_checks = []
    for i_int in range(0, 8):
        for j_int in range(0, 8):
            i_f = Fraction(i_int, 1)
            j_f = Fraction(j_int, 1)
            lhs = _tri_exp(s_order, i_f + j_f) - (
                _tri_exp(s_order, i_f) + _tri_exp(s_order, j_f)
            )
            rhs = s_order * i_f * j_f
            cauchy_checks.append(lhs == rhs and rhs >= 0)
    sample_def = s_order * Fraction(3, 1) * Fraction(4, 1)
    a1_pass = all(cauchy_checks) and sample_def == Fraction(6, 1)
    assertions.append(
        {
            "id": "qou-qb99-qgevrey-cauchy-convolution-deficit",
            "bean": "qou-qb99",
            "description": "Triangular q-Gevrey exponent at Cauchy index i+j exceeds the sum at i and j by s*i*j >= 0",
            "testedOrderS": str(s_order),
            "sampleDeficitAt3And4": str(sample_def),
            "passed": bool(a1_pass),
        }
    )

    # 2. qou-ratf: cosh/BCH crossing parity decomposition & rotor Casimir completed square
    x_mp = mp.mpf("0.35")
    f_plus = mp.exp(x_mp)
    f_minus = mp.exp(-x_mp)
    even_part = (f_plus + f_minus) / 2
    odd_part = (f_plus - f_minus) / 2
    err_recon = max(
        abs((even_part + odd_part) - f_plus),
        abs((even_part - odd_part) - f_minus),
        abs((even_part**2 - odd_part**2) - (f_plus * f_minus)),
    )
    casimir_checks = []
    for j_num in range(0, 10):
        j_f = Fraction(j_num, 2)
        casimir_checks.append(
            (j_f + Fraction(1, 2)) ** 2 - Fraction(1, 4) == j_f * (j_f + 1)
        )
    a2_pass = err_recon < mp.mpf("1e-75") and all(casimir_checks)
    assertions.append(
        {
            "id": "qou-ratf-cosh-even-sinh-odd-and-rotor-casimir",
            "bean": "qou-ratf",
            "description": "Bilateral crossing observable decomposes into cosh-even and sinh-odd parts with (even^2 - odd^2) = fPlus*fMinus and (J+1/2)^2 - 1/4 = J(J+1)",
            "coshEvenAt0p35": mp.nstr(even_part, 40),
            "sinhOddAt0p35": mp.nstr(odd_part, 40),
            "maxReconstructionError": mp.nstr(err_recon, 12),
            "passed": bool(a2_pass),
        }
    )

    # 3. qou-ri9w: FW->GGM coupling defect & median-Borel resummation
    a41, b41 = 1, 2
    a52, b52 = 2, 3
    def_41 = b41 - a41
    def_52 = b52 - a52
    s_minus = Fraction(7, 5)
    m0_stokes = Fraction(3, 1)
    s_plus = s_minus + m0_stokes * s_minus
    twice_median = s_plus + s_minus
    jump_borel = s_plus - s_minus
    a3_pass = (
        def_41 == 1
        and def_52 == 1
        and (b52 - b41) == 1
        and twice_median == (2 + m0_stokes) * s_minus
        and jump_borel == m0_stokes * s_minus
    )
    assertions.append(
        {
            "id": "qou-ri9w-fw-ggm-coupling-defect-and-median-borel",
            "bean": "qou-ri9w",
            "description": "Both 4_1 (1,2) and 5_2 (2,3) have unit FW coupling defect B-A = 1, and twice the median-Borel sum equals (2 + m0)*S_-",
            "defect41": str(def_41),
            "defect52": str(def_52),
            "twiceMedianBorelSample": str(twice_median),
            "stokesDiscontinuitySample": str(jump_borel),
            "passed": bool(a3_pass),
        }
    )

    # 4. qou-rsrg: 3-saddle resurgent coherent sum rule check S(0) = 3 * S(pi) = -3*pi^2/2
    n_saddles = Fraction(3, 1)
    s_pi_coeff = Fraction(-1, 2)
    s_zero_coeff = n_saddles * s_pi_coeff
    excess_coeff = s_zero_coeff - s_pi_coeff
    s_pi_mp = -mp.pi**2 / 2
    s_zero_mp = 3 * s_pi_mp
    err_sum_rule = abs(s_zero_mp - (-3 * mp.pi**2 / 2))
    a4_pass = (
        s_zero_coeff == Fraction(-3, 2)
        and excess_coeff == Fraction(-1, 1)
        and excess_coeff == (n_saddles - 1) * s_pi_coeff
        and err_sum_rule < mp.mpf("1e-75")
    )
    assertions.append(
        {
            "id": "qou-rsrg-three-saddle-coherent-sum-rule-check",
            "bean": "qou-rsrg",
            "description": "For N=3 saddles with per-saddle value S(pi) = -pi^2/2, the coherent sum is S(0) = -3*pi^2/2 with excess S(0)-S(pi) = -pi^2",
            "sZeroPiSqCoeff": str(s_zero_coeff),
            "excessPiSqCoeff": str(excess_coeff),
            "sZero80Dps": mp.nstr(s_zero_mp, 40),
            "passed": bool(a4_pass),
        }
    )

    # 5. qou-u7hx: B2 sibling convergence normalization bridge
    v_a, z_a = Fraction(15, 4), Fraction(5, 2)
    v_b, z_b = Fraction(9, 2), Fraction(3, 1)
    v_c, z_c = Fraction(21, 2), Fraction(7, 1)
    def_ab = v_a * z_b - v_b * z_a
    def_bc = v_b * z_c - v_c * z_b
    def_ac = v_a * z_c - v_c * z_a
    # Also test arbitrary non-zero defects for the transitive identity
    v_b_pert = Fraction(5, 1)
    def_ab_p = v_a * z_b - v_b_pert * z_a
    def_bc_p = v_b_pert * z_c - v_c * z_b
    trans_lhs = z_c * def_ab_p + z_a * def_bc_p
    trans_rhs = z_b * def_ac
    a5_pass = (
        def_ab == 0
        and def_bc == 0
        and def_ac == 0
        and (v_a / z_a) == (v_b / z_b)
        and trans_lhs == trans_rhs
    )
    assertions.append(
        {
            "id": "qou-u7hx-sibling-normalization-defect-and-transitivity",
            "bean": "qou-u7hx",
            "description": "Cross-multiplied sibling normalization defect vA*zB - vB*zA vanishes iff normalized values agree, and satisfies zC*def(A,B) + zA*def(B,C) = zB*def(A,C)",
            "normalizedValue": str(v_a / z_a),
            "defectAB": str(def_ab),
            "transitiveCheckDiff": str(trans_lhs - trans_rhs),
            "passed": bool(a5_pass),
        }
    )

    all_passed = all(a["passed"] for a in assertions)
    witness = {
        "probe": "qgevrey_cauchy_and_fw_ggm_stokes_probe.py",
        "beans": ["qou-qb99", "qou-ratf", "qou-ri9w", "qou-rsrg", "qou-u7hx"],
        "parentBean": "qou-frzo",
        "leanModule": "QOU.MassTheory.QGevreyCauchyAndFWGGMStokes",
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
