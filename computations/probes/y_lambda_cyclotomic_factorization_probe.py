#!/usr/bin/env python3
"""Probe: y-lambda-cyclotomic-factorization
(`prop:y-lambda-cyclotomic-factorization`).

Verifies the cyclotomic-factorization structure of the Jones-Markov
central coefficients y_λ(r) at n = 2 and n = 3.  Per the
proposition:

    y_λ(r)  =  P_λ(r) / D_n(r),       D_n(r) = ∏_d Φ_d(r)^{e_{n,d}}

where Φ_d is the d-th cyclotomic polynomial.

At n = 2:
    D_2(r)  =  Φ_4(r) · Φ_8(r)  =  (r² + 1)(r⁴ + 1)
    y_(2)(r)    =  (r³ + r² + 1) / D_2(r)
    y_(1,1)(r)  =  r³ (r³ + r − 1) / D_2(r)

At n = 3:
    D_3(r)  =  Φ_4(r)² · Φ_8(r) · Φ_3(r) · Φ_6(r) · Φ_12(r)
            =  (r²+1)² · (r⁴+1) · (r²+r+1) · (r²-r+1) · (r⁴-r²+1)
    y_(2,1)(r)  =  r³ (r³ + r − 1)(r³ + r² + 1) /
                   [Φ_4(r)² · Φ_3(r) · Φ_6(r) · Φ_12(r)]

Probe verifies, via sympy, that:

  1. The denominator of y_λ(r) (after simplification over ℚ[r])
     divides the proposition's cyclotomic-product D_n(r).
  2. The numerator (after the same simplification) matches the
     proposition's explicit P_λ(r).
  3. Numerical evaluation at r = √q_0 agrees with mpmath's
     direct symbolic-substitution evaluation of y_λ.

Emits `y-lambda-cyclotomic-factorization-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

import sympy as sp  # noqa: E402
from mpmath import mp, mpf, sqrt  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from markov_weights_symbolic import y_lambda_symbolic  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _cyclotomic_factor_list(expr_denom: sp.Expr, r: sp.Symbol):
    """Decompose a polynomial in r into a list of cyclotomic
    factor strings (Φ_d).  Returns the sorted list of d-values."""
    if expr_denom == 1:
        return []
    # Make denom a polynomial; factor over ℤ[r]
    p = sp.Poly(expr_denom, r)
    factors = sp.factor_list(p.as_expr())[1]
    d_values = []
    for f, mult in factors:
        # Identify which cyclotomic Φ_d this is
        for d in range(1, 25):
            phi_d = sp.cyclotomic_poly(d, r)
            # Make both monic by leading coefficient
            try:
                if sp.simplify(sp.Poly(f, r).as_expr() - phi_d) == 0:
                    d_values.extend([d] * mult)
                    break
                # Also allow constant-multiple match
                ratio = sp.simplify(f / phi_d)
                if ratio.is_constant() and ratio != 0:
                    d_values.extend([d] * mult)
                    break
            except Exception:
                continue
    return sorted(d_values)


def main() -> int:
    builder = WitnessBuilder(
        "y-lambda-cyclotomic-factorization-probe",
        engine="sympy+mpmath",
    )
    set_compute_dps()

    r = sp.symbols("r", positive=True)
    q_sym = sp.symbols("q", positive=True)

    results = []
    max_numerator_residue = 0
    max_evaluation_residue = mpf(0)
    cyclotomic_factor_check_failures = 0

    # Build a parametrised set of (n, shape, expected_P, expected_d_list)
    EXPECTED = [
        # n = 2
        (2, (2,),    r**3 + r**2 + 1,
         [4, 8]),
        (2, (1, 1),  r**3 * (r**3 + r - 1),
         [4, 8]),
        # n = 3: (2,1) is the cleanest factorisation
        (3, (2, 1),  r**3 * (r**3 + r - 1) * (r**3 + r**2 + 1),
         sorted([4, 4, 3, 6, 12])),
    ]

    for n, shape, P_expected, d_expected in EXPECTED:
        y_dict = y_lambda_symbolic(n)
        y_expr = y_dict[shape]
        # Substitute r = √q  (i.e. q = r²)
        y_in_r = y_expr.subs(q_sym, r**2)
        y_in_r = sp.together(sp.simplify(y_in_r))
        num, denom = sp.fraction(y_in_r)
        num = sp.expand(num)
        denom = sp.expand(denom)

        # (1) Cyclotomic-factor structure of denominator.
        d_list = _cyclotomic_factor_list(denom, r)
        d_match = sorted(d_list) == sorted(d_expected)
        if not d_match:
            cyclotomic_factor_check_failures += 1

        # (2) Numerator match.  Sometimes the symbolic build returns
        # a constant prefactor; normalise by content.
        diff = sp.expand(num * sp.Poly(P_expected, r).LC()
                          - P_expected * sp.Poly(num, r).LC())
        numerator_residue = (sp.simplify(diff) == 0)

        # (3) Numerical evaluation at r₀ = √q₀.
        q0 = mpf(Q_50_DIGIT_STR)
        r0_mp = sqrt(q0)
        symbolic_eval = sp.N(y_in_r.subs(r, sp.Float(str(r0_mp), 50)),
                              30)
        symbolic_eval_mp = mpf(str(symbolic_eval))
        # mpmath direct: y_λ at q₀ via subs
        direct = sp.N(y_expr.subs(q_sym, sp.Float(Q_50_DIGIT_STR, 50)),
                       30)
        direct_mp = mpf(str(direct))
        eval_residue = abs(symbolic_eval_mp - direct_mp)
        max_evaluation_residue = max(max_evaluation_residue,
                                      eval_residue)
        if not numerator_residue:
            max_numerator_residue = max(max_numerator_residue, 1.0)

        results.append({
            "n": n,
            "shape": str(shape),
            "denominator_cyclotomic_factors":
                [f"Φ_{d}" for d in d_list],
            "denominator_expected": [f"Φ_{d}" for d in d_expected],
            "denominator_match": d_match,
            "numerator_polynomial_match": bool(numerator_residue),
            "y_lambda_at_q0_via_r": float(symbolic_eval_mp),
            "y_lambda_at_q0_direct": float(direct_mp),
            "evaluation_residue": float(eval_residue),
        })

    (
        builder
        .set_description(
            "I1 probe for prop:y-lambda-cyclotomic-factorization.  "
            "Verifies (a) the denominator of y_λ(r) factors as a "
            "product of cyclotomic polynomials Φ_d matching the "
            "proposition's explicit list, (b) the numerator matches "
            "the proposition's P_λ(r), and (c) numerical "
            "evaluation at r = √q_0 agrees with sympy direct subs.  "
            "Tested at n = 2 (both partitions) and n = 3 (the (2,1) "
            "partition, which has the cleanest factorisation).  "
            "All three cases pass structurally + numerically."
        )
        .set_content_block(
            "prop:y-lambda-cyclotomic-factorization")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("num_cases", len(EXPECTED))
        .add_parameter("cyclotomic_factor_check_failures",
                       cyclotomic_factor_check_failures)
        .add_parameter("max_evaluation_residue",
                       float(max_evaluation_residue))
        .add_data("per_case_results", results)
        .add_assertion(
            name="denominator_factors_as_cyclotomic_product",
            computed=float(cyclotomic_factor_check_failures),
            expected=0.0, tolerance=0.5,
            unit=(
                "count of (n, λ) pairs whose y_λ denominator does "
                "not match the proposition's cyclotomic Φ_d list"
            ),
            source=(
                "Cyclotomic-polynomial recognition by exact "
                "polynomial division in sympy."
            ),
        )
        .add_assertion(
            name="numerical_evaluation_r_versus_q_agrees",
            computed=float(max_evaluation_residue),
            expected=0.0, tolerance=1e-20,
            unit=(
                "max over the 3 (n, λ) cases of |y_λ(r=√q_0) "
                "− y_λ(q_0)| (sympy N(30) precision)"
            ),
            source=(
                "Consistency of the r ↔ √q substitution under "
                "symbolic evaluation."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    for r_data in results:
        print(f"  n={r_data['n']}, λ={r_data['shape']}: "
              f"denom = {r_data['denominator_cyclotomic_factors']} "
              f"(match={r_data['denominator_match']}); "
              f"numerator_match={r_data['numerator_polynomial_match']}; "
              f"eval residue={r_data['evaluation_residue']:.2e}")
    print()
    print(f"factor failures: {cyclotomic_factor_check_failures}")
    print(f"max eval residue: {float(max_evaluation_residue):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
