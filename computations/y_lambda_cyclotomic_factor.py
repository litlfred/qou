#!/usr/bin/env python3
"""Factor y_λ closed forms via cyclotomic polynomials Φ_d(q).

The Wenzl-bridge gives y_λ as q-rational expressions in
Frac(Z[r, r^{-1}]) where r = q^{1/2} (the spinor information rate;
see notation-register.md Ch 4 and notation-collisions.md).

Notation note (2026-06-04): the narrative now writes the spinor rate
as \check{q} (q-háček, "little hook" in Czech), with \check{q}² = q.
The sympy SYMBOL below stays "r" so that the emitted witness
expression strings (and this script's printed output) are unchanged;
the narrative s_{λ,\check{q}}(Q) in y-lambda-cyclotomic-factorization.md
corresponds to this script's r-form term-for-term (\check{q} ↔ r).

Sympy's
default `together`/`cancel` doesn't simplify well at n≥3, but
sympy `factor` over Q can identify cyclotomic factors directly:

  q^n - 1 = ∏_{d | n} Φ_d(q)
  Φ_1 = q-1, Φ_2 = q+1, Φ_3 = q²+q+1, Φ_4 = q²+1,
  Φ_5 = q⁴+q³+q²+q+1, Φ_6 = q²-q+1, ...

Strategy: substitute q = r² so all expressions become Laurent
polynomial in r.  Then factor over Q to identify Φ_d(r) factors.
This gives the cleanest possible compact form.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: E402


# Use r = q^{1/2} as the underlying variable so all expressions are
# Laurent polynomial in r (no sqrt's).  The Python local variable
# happens to be named `t` for legacy reasons (this script predates
# the r adoption); the sympy SYMBOL is "r" so all printed output
# uses r-notation per notation-register.md.
t = sp.symbols("r", positive=True)
q = t ** 2  # q = r²
Q = q ** 2  # Q = q² = r⁴

# Markov parameter z = 1/(q^{1/2} + q^{-1/2}) = 1/(r + 1/r) = r/(r²+1)
z = t / (t ** 2 + 1)

# X = Q^ℓ = (q · z) / (1 - Q + q · z)  (Wenzl level expressed in r)
qz = q * z  # = r² · r/(r²+1) = r³/(r²+1)
# Numerator of X = qz = r³ / (r²+1)
# Denominator of X = (1 - Q + qz) = 1 - r⁴ + r³/(r²+1)
#                  = ((1-r⁴)(r²+1) + r³)/(r²+1)
#                  = (r²+1 - r⁴(r²+1) + r³)/(r²+1)
#                  = (r²+1 - r⁶ - r⁴ + r³)/(r²+1)
#                  = (1 + r² + r³ - r⁴ - r⁶)/(r²+1)
X = sp.together(qz / (1 - Q + qz))
X_factored = sp.factor(X)


def cyclotomic_factor(expr, max_d=20):
    """Factor a Laurent polynomial in r over Q and identify cyclotomic
    factors.  Returns a string with cyclotomic notation Φ_d(r) where
    applicable."""
    expr = sp.together(expr)
    num, den = sp.fraction(expr)
    num_f = sp.factor(num)
    den_f = sp.factor(den)
    return num_f, den_f


def n_partition(lam):
    return sum(i * lami for i, lami in enumerate(lam))


def s_lambda(lam):
    """Schur principal-specialization in terms of (Q, X) — returned in t."""
    if not lam:
        return sp.S(1)
    n_lam = n_partition(lam)
    rows = len(lam)
    num = sp.S(1); den = sp.S(1)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            h = arm + leg + 1
            c = j - i
            num *= (1 - X * Q**c)
            den *= (1 - Q**h)
    return Q**n_lam * num / den


def hook_dim(lam):
    if not lam:
        return 1
    n = sum(lam); rows = len(lam)
    from math import factorial
    prod = 1
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            prod *= arm + leg + 1
    return factorial(n) // prod


def partitions_of(n):
    if n == 0: return [()]
    def gen(rem, mxp):
        if rem == 0: yield (); return
        for p in range(min(mxp, rem), 0, -1):
            for rest in gen(rem - p, p):
                yield (p,) + rest
    return list(gen(n, n))


print(f"X (in r = q^(1/2)) factored:")
print(f"  X = {X_factored}")
print()

results = {}
for n in [2, 3, 4]:
    print(f"=== n = {n} ===")
    parts = partitions_of(n)
    s_vals = {lam: s_lambda(lam) for lam in parts}
    Z = sum(hook_dim(lam) * s_vals[lam] for lam in parts)
    Z_simp = sp.together(Z)
    Z_num, Z_den = sp.fraction(Z_simp)
    Z_num_f = sp.factor(Z_num)
    Z_den_f = sp.factor(Z_den)
    print(f"Z (n={n}):")
    print(f"  num: {Z_num_f}")
    print(f"  den: {Z_den_f}")
    print()

    n_results = {}
    for lam in parts:
        y = s_vals[lam] / Z
        # Cancel and factor
        y_cancel = sp.cancel(y)
        y_num, y_den = sp.fraction(y_cancel)
        y_num_f = sp.factor(y_num)
        y_den_f = sp.factor(y_den)

        # Display with cyclotomic notation if possible
        num_str = str(y_num_f)
        den_str = str(y_den_f)
        if len(num_str) > 200:
            num_str = num_str[:197] + "..."
        if len(den_str) > 200:
            den_str = den_str[:197] + "..."
        print(f"  y_{lam}:")
        print(f"    num: {num_str}")
        print(f"    den: {den_str}")
        # Polynomial form in r = q^{1/2}; reuse the default q_0
        # for q's value but pass sqrt(q_0) for the t-substitution
        # (this script's symbolic variable is t, not q).
        from witness_polynomial import _default_q0
        t_at_q0 = sp.sqrt(_default_q0())
        n_results[str(lam)] = {
            "numerator_factored": str(y_num_f),
            "denominator_factored": str(y_den_f),
            "y_polynomial": expose_polynomial(
                y_cancel, t, q0=t_at_q0, simplify=False
            ),
        }
    results[str(n)] = n_results
    print()

# Save witness
out_path = Path(__file__).parent / "y-lambda-cyclotomic-factor.witness.json"
with open(out_path, "w") as fp:
    json.dump({
        "computation": "y-lambda-cyclotomic-factor",
        "description": (
            "Factor y_λ closed forms over Q in r = q^{1/2} to identify "
            "cyclotomic Φ_d(r) factors. Substitution Q = q² = r⁴ makes "
            "all expressions Laurent polynomial in r; sympy `factor` "
            "then exposes Schur-element-style cyclotomic structure."
        ),
        "X_in_r": str(X_factored),
        "results": results,
        "precision": "symbolic_q",
        "truncation_eps": 0.0,
    }, fp, indent=2, default=str)
print(f"Witness: {out_path}")
