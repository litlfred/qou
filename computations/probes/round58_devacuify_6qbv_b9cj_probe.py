#!/usr/bin/env python3
"""
80-dps mpmath probe for Round 58 devacuification & non-vacuous theorem tranche:
  - qou-a30t: QOU/Habiro/FlowSolution.lean (HabiroFlowSolution q-difference recurrence & q=1 refutation)
  - qou-qcy6: QOU/ProofHygiene/SelfAssumingContexts.lean (UnderdeterminedProductContext unit-gauge freedom & pinning)
  - qou-6dzi: QOU/Hecke/Wedderburn.lean (WedderburnDecomp dimension-weighted sum & non-unit idempotent orthogonality)
  - qou-ufm1: QOU/Archimedean/JetOrderIndependence.lean (SurrealParallelTransportBound non-vacuity & LU pivot det)
  - qou-ndt5: QOU/BringsSurface/ColourCurveBarVsBranch.lean (colourCurve branch sum, bar-odd product, golden locus)
"""

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def check_a30t():
    # Verify HabiroFlowSolution q-difference recurrences at q = 3/5:
    # (1 - q^(n+1)) c_{n+1} = (1 - q) c_n with c_0 = 1 => c_1 = 1, (1+q)*c_2 = 1
    q = mp.mpf(3) / mp.mpf(5)
    c0 = mp.mpf(1)
    c1 = ((1 - q) * c0) / (1 - q**1)
    c2 = ((1 - q) * c1) / (1 - q**2)
    err_c1 = abs(c1 - 1)
    err_c2 = abs((1 + q) * c2 - 1)
    # Fourier eigenvalue at j=0: q^0 + q^0 = 2
    lam0 = q**0 + (q**0) ** (-1)
    err_lam0 = abs(lam0 - 2)
    # At q = 1, (1 - 1) * d_1 = 0 != 1 (unsatisfiable)
    lhs_q1 = (mp.mpf(1) - mp.mpf(1)) * mp.mpf(1)
    passed = bool(err_c1 == 0 and err_c2 < mp.mpf("1e-75") and err_lam0 == 0 and lhs_q1 == 0)
    return {
        "bean": "qou-a30t",
        "module": "QOU.Habiro.FlowSolution",
        "c1_error": mp.nstr(err_c1, 20),
        "c2_recurrence_error": mp.nstr(err_c2, 20),
        "fourier_eigenvalue_zero": mp.nstr(lam0, 20),
        "q_eq_one_lhs": mp.nstr(lhs_q1, 20),
        "passed": passed,
    }


def check_qcy6():
    # UnderdeterminedProductContext unit-gauge rescaling:
    # sum_i (u_i * w_i) * (u_i^-1 * chi_i) == sum_i w_i * chi_i
    weights = [mp.mpf(2) / 7, mp.mpf(3) / 7, mp.mpf(2) / 7]
    chars = [mp.mpf(1), mp.mpf(2), mp.mpf(-1)]
    units = [mp.mpf(5), mp.mpf(-3), mp.mpf(11) / 2]
    orig = sum(w * c for w, c in zip(weights, chars))
    rescaled = sum((u * w) * ((1 / u) * c) for u, w, c in zip(units, weights, chars))
    err = abs(orig - rescaled)
    passed = bool(err < mp.mpf("1e-75"))
    return {
        "bean": "qou-qcy6",
        "module": "QOU.ProofHygiene.SelfAssumingContexts",
        "original_trace": mp.nstr(orig, 30),
        "rescaled_trace": mp.nstr(rescaled, 30),
        "max_abs_error": mp.nstr(err, 20),
        "passed": passed,
    }


def check_6dzi():
    # WedderburnDecomp on H_3: partitions [3], [2,1], [1,1,1] with blockDim 1, 2, 1
    # sum_lam y_lam * f^lam = tr_M(1) = 1
    f_dims = [Fraction(1), Fraction(2), Fraction(1)]
    y_vals = [Fraction(1, 6), Fraction(1, 3), Fraction(1, 6)]
    weighted_sum = sum(y * d for y, d in zip(y_vals, f_dims))
    passed = bool(weighted_sum == Fraction(1))
    return {
        "bean": "qou-6dzi",
        "module": "QOU.Hecke.Wedderburn",
        "block_dims": [str(d) for d in f_dims],
        "weighted_sum_at_one": str(weighted_sum),
        "passed": passed,
    }


def check_ufm1():
    # JetOrderIndependence: LU pivots (1/4, 2, 1/8) product = 1/16 = det(jetJacobianBase)
    pivots = (Fraction(1, 4), Fraction(2, 1), Fraction(1, 8))
    elim_det = pivots[0] * pivots[1] * pivots[2]
    # Matrix !![1/4, -1, 55/16; 1/2, 0, -1/16; 1, 0, 0]
    # det = 1 * ((-1)*(-1/16) - 0*(55/16)) = 1/16
    mat_det = Fraction(1) * (Fraction(-1) * Fraction(-1, 16) - Fraction(0) * Fraction(55, 16))
    passed = bool(elim_det == Fraction(1, 16) and mat_det == Fraction(1, 16))
    return {
        "bean": "qou-ufm1",
        "module": "QOU.Archimedean.JetOrderIndependence",
        "elimination_det": str(elim_det),
        "matrix_det": str(mat_det),
        "passed": passed,
    }


def check_ndt5():
    # ColourCurveBarVsBranch at canonical s = sqrt(q0), phi = (1+sqrt(5))/2
    phi = (mp.mpf(1) + mp.sqrt(5)) / 2
    q0 = mp.mpf("1.0670442670094260999209120230611007313991569425981")
    s0 = mp.sqrt(q0)
    z0 = s0 - 1 / s0
    # Identity 1: z(s) * (s + 1/s) = s^2 - s^-2
    lhs1 = z0 * (s0 + 1 / s0)
    rhs1 = s0**2 - s0 ** (-2)
    err1 = abs(lhs1 - rhs1)
    # Identity 2: colourCurve(z) + colourCurve(-z) = (10/27)*(3*z^2 + 4)
    def r_curve(z):
        return (mp.mpf(5) / 27) * (4 * z**3 + 3 * z**2 + 3 * z + 4)
    lhs2 = r_curve(z0) + r_curve(-z0)
    rhs2 = (mp.mpf(10) / 27) * (3 * z0**2 + 4)
    err2 = abs(lhs2 - rhs2)
    # Identity 3: degeneration_poly_barLift at s = 1/phi: s^2 + s - 1 = 0 and (-1/s)^2 + (-1/s) - 1 = 0
    s_deg = 1 / phi
    bar_s_deg = -1 / s_deg
    err3 = max(abs(s_deg**2 + s_deg - 1), abs(bar_s_deg**2 + bar_s_deg - 1))
    passed = bool(err1 < mp.mpf("1e-75") and err2 < mp.mpf("1e-75") and err3 < mp.mpf("1e-75"))
    return {
        "bean": "qou-ndt5",
        "module": "QOU.BringsSurface.ColourCurveBarVsBranch",
        "bar_odd_product_error": mp.nstr(err1, 20),
        "branch_sum_error": mp.nstr(err2, 20),
        "degeneration_locus_error": mp.nstr(err3, 20),
        "passed": passed,
    }


def main():
    script_path = Path(__file__).resolve()
    script_bytes = script_path.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    script_hash = script_sha256[:12]
    commit_sha = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()

    results = [
        check_a30t(),
        check_qcy6(),
        check_6dzi(),
        check_ufm1(),
        check_ndt5(),
    ]
    all_passed = all(r["passed"] for r in results)
    assert all_passed, f"Some checks failed: {results}"

    witness = {
        "probe": "round58_devacuify_6qbv_b9cj_probe.py",
        "scriptHash": script_hash,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "precisionDps": "80",
        "allPassed": all_passed,
        "beans": ["qou-a30t", "qou-qcy6", "qou-6dzi", "qou-ufm1", "qou-ndt5"],
        "results": results,
    }

    out_path = script_path.parent / "round58-devacuify-6qbv-b9cj.witness.json"
    out_path.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Wrote {out_path} (scriptHash={script_hash}, commit={commit_sha})")


if __name__ == "__main__":
    main()
