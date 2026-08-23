#!/usr/bin/env python3
"""Probe: y-lambda-cyclotomic-factorization
(`prop:y-lambda-cyclotomic-factorization`).

Verifies the cyclotomic-factorization structure of the Jones-Markov central
coefficients y_λ(r), r = √q, for EVERY partition at n = 2, 3, 4.  Per the
proposition:

    y_λ(r)  =  P_λ(r) / D_n(r),       D_n(r) = ∏_d Φ_d(r)^{e_{n,d}}

**Convention D** throughout (`z = q³/(q²+1)`, i.e. `r⁶/(r⁴+1)`), which is what
`markov_weights_symbolic.y_lambda_symbolic` computes.

## What this probe asserts, and what it used to

It used to compare against a hardcoded `EXPECTED` table of three hand-picked
cases carrying **convention-C** polynomials — `r³ + r − 1`, `r³ + r² + 1`,
`D_2 = Φ_4·Φ_8`, `D_3 = Φ_4²·Φ_8·Φ_3·Φ_6·Φ_12`.  The block was corrected to
convention D on 2026-08-10; this table was not, so all three cases mismatched
and the witness sat red.  Its own description meanwhile read "All three cases
pass structurally + numerically", asserted independently of the result.

A frozen table is the wrong instrument for this claim anyway.  The proposition
does not say the denominator equals one particular list of Φ_d — it says the
denominator **is a pure product of cyclotomic polynomials**.  That is a
structural property, it is what survives a convention change, and it is what is
asserted here.  The actual Φ_d exponents are recorded as `data`, so the numbers
stay visible without a frozen copy of them being able to rot.

Three assertions:

  1. every denominator factors ENTIRELY into cyclotomic polynomials — the
     recogniser now reports unrecognised factors rather than silently dropping
     them, which is what let a partial match look like a near miss;
  2. Σ_λ y_λ · dim(λ) = 1, the Markov normalisation — a derivable invariant, so
     unlike a table it cannot go stale;
  3. numerical evaluation via r agrees with direct substitution in q.

Under convention D every λ with ℓ(λ) ≥ 3 has y_λ = 0 exactly (numerator 0,
denominator 1).  Those are the empty cyclotomic product, which is a product;
they are recorded explicitly rather than skipped.

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

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from markov_weights_symbolic import y_lambda_symbolic  # noqa: E402


def _cyclotomic_decomposition(expr_denom: sp.Expr, r: sp.Symbol):
    """Decompose a denominator into cyclotomic factors.

    Returns `(d_values, unrecognised)`:
      * `d_values`      — sorted d for each Φ_d factor, with multiplicity
      * `unrecognised`  — string forms of factors that are NOT any Φ_d

    The previous version returned only `d_values` and silently dropped anything
    it could not identify, so a denominator with a genuinely non-cyclotomic
    factor was indistinguishable from one with the wrong exponents. The
    proposition's claim is precisely that `unrecognised` is empty.

    `denom == 1` (the convention-D zero weights) is the EMPTY product, which is
    a cyclotomic product — `([], [])`, not a failure.
    """
    if expr_denom == 1:
        return [], []
    p = sp.Poly(expr_denom, r)
    factors = sp.factor_list(p.as_expr())[1]
    d_values: list[int] = []
    unrecognised: list[str] = []
    for f, mult in factors:
        matched = False
        for d in range(1, 49):
            phi_d = sp.cyclotomic_poly(d, r)
            try:
                if sp.simplify(sp.Poly(f, r).as_expr() - phi_d) == 0:
                    d_values.extend([d] * mult)
                    matched = True
                    break
                ratio = sp.simplify(f / phi_d)
                if ratio.is_constant() and ratio != 0:
                    d_values.extend([d] * mult)
                    matched = True
                    break
            except Exception:
                continue
        if not matched:
            # a bare monomial r^k is a unit times r^k; r itself is not a Φ_d,
            # so say so rather than dropping it
            unrecognised.extend([sp.sstr(f)] * mult)
    return sorted(d_values), unrecognised


def _dim_partition(shape: tuple[int, ...]) -> int:
    """dim of the S_n irrep for `shape`, by the hook-length formula."""
    n = sum(shape)
    conj = [sum(1 for row in shape if row > j) for j in range(shape[0])]
    prod = 1
    for i, row in enumerate(shape):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return sp.factorial(n) // prod


def main() -> int:
    builder = WitnessBuilder(
        "y-lambda-cyclotomic-factorization-probe",
        engine="sympy+mpmath",
    )
    set_compute_dps()   # canonical dps; was a sub-canonical mp.dps = 50

    r = sp.symbols("r", positive=True)
    q_sym = sp.symbols("q", positive=True)

    results = []
    max_evaluation_residue = mpf(0)
    non_cyclotomic_denominators = 0
    max_normalisation_residue = mpf(0)
    q0 = mpf(Q_50_DIGIT_STR)
    r0_mp = sqrt(q0)

    for n in (2, 3, 4):
        y_dict = y_lambda_symbolic(n)
        norm_sum = mpf(0)
        for shape in sorted(y_dict, key=lambda t: (-len(t), t), reverse=True):
            y_expr = y_dict[shape]
            y_in_r = sp.together(sp.simplify(y_expr.subs(q_sym, r**2)))
            num, denom = sp.fraction(y_in_r)
            num, denom = sp.expand(num), sp.expand(denom)

            # (1) is the denominator a PURE cyclotomic product?
            d_list, unrecognised = _cyclotomic_decomposition(denom, r)
            if unrecognised:
                non_cyclotomic_denominators += 1

            # (2) numerical: via r, and directly in q
            symbolic_eval = sp.N(y_in_r.subs(r, sp.Float(str(r0_mp), 50)), 30)
            direct = sp.N(y_expr.subs(q_sym, sp.Float(Q_50_DIGIT_STR, 50)), 30)
            symbolic_eval_mp = mpf(str(symbolic_eval))
            direct_mp = mpf(str(direct))
            eval_residue = abs(symbolic_eval_mp - direct_mp)
            if eval_residue > max_evaluation_residue:
                max_evaluation_residue = eval_residue

            dim = int(_dim_partition(shape))
            norm_sum += direct_mp * dim

            results.append({
                "n": n,
                "shape": str(shape),
                "dim": dim,
                "numerator_factored": sp.sstr(sp.factor(num)),
                "denominator_factored": sp.sstr(sp.factor(denom)),
                "cyclotomic_d_values": d_list,
                "non_cyclotomic_factors": unrecognised,
                "is_pure_cyclotomic_product": not unrecognised,
                "vanishes_identically": num == 0,
                "y_lambda_at_q0_via_r": str(symbolic_eval_mp),
                "y_lambda_at_q0_direct": str(direct_mp),
                "evaluation_residue": str(eval_residue),
            })

        # (3) Markov normalisation at this n
        residue = abs(norm_sum - 1)
        if residue > max_normalisation_residue:
            max_normalisation_residue = residue

    (
        builder
        .set_description(
            "I1 probe for prop:y-lambda-cyclotomic-factorization, convention D. "
            "For EVERY partition at n = 2, 3, 4 it checks that the y_lambda "
            "denominator factors entirely into cyclotomic polynomials Phi_d "
            "(the proposition's structural claim), that sum_lambda y_lambda "
            "dim(lambda) = 1, and that evaluating via r = sqrt(q) agrees with "
            "direct substitution in q. The Phi_d exponents are recorded as data "
            "rather than matched against a frozen list: this probe previously "
            "compared against a hardcoded convention-C table and sat red from "
            "the 2026-08-10 convention-D correction until 2026-08-23."
        )
        .set_content_block(
            "prop:y-lambda-cyclotomic-factorization")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("convention", "D")
        .add_parameter("num_cases", len(results))
        .add_data("per_case_results", results)
        .add_assertion(
            name="denominator_factors_as_cyclotomic_product",
            computed=str(non_cyclotomic_denominators),
            expected="0",
            tolerance="0.5",
            unit=(
                "count of (n, lambda) pairs whose y_lambda denominator carries "
                "a factor that is not any Phi_d"
            ),
            source=(
                "Exact cyclotomic recognition in sympy, reporting unrecognised "
                "factors rather than dropping them. denom == 1 (the "
                "convention-D zero weights) is the empty product and passes."
            ),
        )
        .add_assertion(
            name="markov_normalisation_sum_y_dim_eq_one",
            computed=str(max_normalisation_residue),
            expected="0",
            tolerance="1e-25",
            unit="max over n of |sum_lambda y_lambda dim(lambda) - 1|",
            source=(
                "The Markov trace normalisation tr_M(1) = 1. A derivable "
                "invariant, so unlike a hardcoded table it cannot go stale on "
                "a convention change."
            ),
        )
        .add_assertion(
            name="numerical_evaluation_r_versus_q_agrees",
            computed=str(max_evaluation_residue),
            expected="0",
            tolerance="1e-20",
            unit=(
                "max over all (n, lambda) of |y_lambda(r=sqrt(q_0)) "
                "- y_lambda(q_0)| (sympy N(30) precision)"
            ),
            source=(
                "Consistency of the r <-> sqrt(q) substitution under "
                "symbolic evaluation."
            ),
        )
    )

    out = builder.save()
    print()
    for d in results:
        flag = "  (vanishes)" if d["vanishes_identically"] else ""
        bad = "" if d["is_pure_cyclotomic_product"] else f"  NON-CYCLOTOMIC: {d['non_cyclotomic_factors']}"
        print(f"  n={d['n']} lambda={d['shape']:<10} dim={d['dim']:<3} "
              f"Phi_d={d['cyclotomic_d_values']}{flag}{bad}")
    print()
    print(f"  non-cyclotomic denominators : {non_cyclotomic_denominators}")
    print(f"  max |sum y_lambda dim - 1|  : {mp.nstr(max_normalisation_residue, 6)}")
    print(f"  max evaluation residue      : {mp.nstr(max_evaluation_residue, 6)}")
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
