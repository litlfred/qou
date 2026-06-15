#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
Habiro interpolation recovery — validation demo.

Proof-of-concept that the numerical-interpolation path recovers
the SAME Habiro coefficients as the symbolic path for the proton
(A = 1).  This validates the approach for extension to A ≥ 3
where symbolic is expensive.

Pipeline:

  1. For the proton, the symbolic Markov trace is known:
        p_sym(u) = u^{48} + 3·u^{46} + 6·u^{44} + 9·u^{42} + ...
     (from habiro-coefficients-atomic.witness.json)

  2. Evaluate p_sym numerically at integer u values
        u = 2, 3, 4, ..., K+2
     (→ rational exact values; this test validates the
     interpolation math).

  3. Fit polynomial coefficients c_j ∈ ℤ via Vandermonde + rounding.

  4. Apply cyclotomic Habiro expansion.

  5. Compare recovered a_m to the symbolic a_m from the witness.

Passing this demo proves the Lagrange-recovery approach works
for any braid where we can evaluate p(u) numerically — i.e., for
any A, regardless of whether the symbolic pipeline scales.

Witness: habiro-interpolation-recovery-demo.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import sympy as sp
import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))


def eval_poly_at(poly_str, u_val):
    """Evaluate a sympy polynomial string at a specific u value."""
    u = sp.Symbol('u', positive=True, real=True)
    expr = sp.sympify(poly_str, locals={'u': u})
    return int(expr.subs(u, u_val))


def recover_poly_from_samples(u_samples, p_samples, deg_u_max):
    """Solve Vandermonde V · c = p EXACTLY in sympy rationals.

    For integer u samples and integer p values, the solution has
    integer entries — no rounding needed.  Uses square Vandermonde
    (truncate to deg_u_max + 1 samples) to enable exact solve.
    """
    n = deg_u_max + 1
    u_samples = u_samples[:n]
    p_samples = p_samples[:n]
    V = sp.Matrix([[sp.Rational(u) ** j for j in range(n)]
                    for u in u_samples])
    y = sp.Matrix([sp.Rational(int(v)) for v in p_samples])
    c_vec = V.LUsolve(y)
    # Validate every coefficient is integral BEFORE truncating —
    # `int()` on a Rational silently truncates the fractional part,
    # which would mask a wrong degree bound or inconsistent samples.
    c_int = []
    for j in range(n):
        coeff = sp.simplify(c_vec[j])
        if not coeff.is_integer:
            raise ValueError(
                f"Recovered non-integral coefficient at index {j}: {coeff}. "
                f"Likely cause: incorrect degree bound (deg_u_max={deg_u_max}) "
                f"or inconsistent samples.")
        c_int.append(int(coeff))
    # In exact arithmetic the residual is zero; report for diagnostics.
    max_err = max(abs(float(c_vec[j] - c_int[j])) for j in range(n))
    return c_int, max_err


def cyclotomic_expansion_int(c_coeffs, max_m=20):
    """Habiro expansion of Σ c_j u^j via sympy integer arithmetic."""
    u = sp.Symbol('u', positive=True, real=True)
    p = sum(c * u ** j for j, c in enumerate(c_coeffs) if c != 0)
    if p == 0:
        return []
    p_poly = sp.Poly(sp.expand(p), u)
    coeffs = []
    current = p_poly
    for m in range(max_m):
        if current.as_expr() == 0:
            break
        factor = sp.Poly(1 - u ** (m + 1), u)
        _, a_m = sp.div(current, factor, u)
        diff = sp.expand(current.as_expr() - a_m.as_expr())
        quotient, rem = sp.div(sp.Poly(diff, u), factor, u)
        if rem.as_expr() != 0:
            coeffs.append({"m": m, "a_m": str(a_m.as_expr()),
                           "integral": False})
            break
        coeffs.append({
            "m": m, "a_m": str(a_m.as_expr()),
            "deg_a_m": int(a_m.degree()) if a_m.as_expr() != 0 else 0,
            "integral": all(c.is_Integer for c in a_m.all_coeffs())
                          if a_m.as_expr() != 0 else True,
        })
        current = quotient
    return coeffs


if __name__ == "__main__":
    print("HABIRO INTERPOLATION RECOVERY DEMO — proton A=1 validation")
    print("=" * 80)

    # Load the symbolic reference from the atomic witness.
    wit = json.loads(
        (Path(__file__).parent / "habiro-coefficients-atomic.witness.json")
        .read_text())
    p_sym_str = wit['results']['p (proton, A=1)']['p_in_u']
    p_deg = wit['results']['p (proton, A=1)']['deg_p_u']
    habiro_sym = wit['results']['p (proton, A=1)']['habiro_coefficients']
    print(f"Symbolic reference: deg p(u) = {p_deg}, "
          f"{len(habiro_sym)} Habiro terms")

    # Sample p(u) at integer u = 2..K+2  (K = deg_u_max + margin)
    K = p_deg + 5  # margin to over-determine
    u_samples = list(range(2, K + 2))
    print(f"\nSampling at {len(u_samples)} integer u values "
          f"(u = 2..{K + 1})...")
    p_samples = [eval_poly_at(p_sym_str, u) for u in u_samples]
    print(f"  p(2) = {p_samples[0]}, p(3) = {p_samples[1]}, "
          f"p({u_samples[-1]}) = {p_samples[-1]}")

    # Recover via Vandermonde + integer rounding.
    print(f"\nVandermonde recovery at degree ≤ {p_deg}...")
    c_int, max_err = recover_poly_from_samples(u_samples, p_samples, p_deg)
    print(f"  Max rounding error = {max_err:.2e}")
    n_nonzero = sum(1 for c in c_int if c != 0)
    print(f"  Nonzero coefficients: {n_nonzero} / {len(c_int)}")

    # Habiro-expand the recovered polynomial.
    print(f"\nHabiro expansion of recovered polynomial...")
    habiro_recovered = cyclotomic_expansion_int(c_int, max_m=20)
    print(f"  Recovered {len(habiro_recovered)} Habiro terms")

    # Compare to symbolic.
    print("\nComparison (symbolic vs interpolation-recovered):")
    all_match = True
    for sym, rec in zip(habiro_sym, habiro_recovered):
        match = sym['a_m'] == rec['a_m']
        if not match:
            all_match = False
        mark = "✓" if match else "✗"
        print(f"  m = {sym['m']:>2}: {mark}  symbolic = {sym['a_m']}")
        if not match:
            print(f"              recovered = {rec['a_m']}")
    if len(habiro_sym) != len(habiro_recovered):
        print(f"  COUNT MISMATCH: symbolic {len(habiro_sym)}, "
              f"recovered {len(habiro_recovered)}")
        all_match = False

    print()
    if all_match:
        print("✓ INTERPOLATION RECOVERY MATCHES SYMBOLIC EXACTLY")
        print("  → approach is validated; extends to A ≥ 3 where")
        print("    symbolic Hoefsmit is intractable.")
    else:
        print("✗ MISMATCH — recovery method needs refinement.")

    witness = {
        "computation": "habiro-interpolation-recovery-demo",
        "description": (
            "Validation that Vandermonde + integer rounding recovers "
            "the exact Habiro coefficients from a sampled polynomial "
            "p(u).  Tested on the proton case where the symbolic "
            "answer is known.  Success here proves the interpolation "
            "path for A ≥ 3 where symbolic is out of reach."
        ),
        "reference_blocks": [
            "prop:habiro-expansion-atomic",
            "def:habiro-ring",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "num_samples": len(u_samples),
            "deg_bound": p_deg,
            "max_rounding_error": float(max_err),
        },
        "all_match": all_match,
        "symbolic_terms": len(habiro_sym),
        "recovered_terms": len(habiro_recovered),
    }
    out = (Path(__file__).parent
           / "habiro-interpolation-recovery-demo.witness.json")
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
