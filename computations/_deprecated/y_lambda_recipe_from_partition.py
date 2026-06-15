#!/usr/bin/env python3
"""Recipe: λ ↦ y_λ(q) — explicit q-rational construction in √q.

Implements the 5-step recipe from prop:y-lambda-recipe-from-partition:

  Step 1: Compute partition data (contents c, hooks h, n(λ)).
  Step 2: X = q^(3/2)/(1 + q - q² - q³ + q^(3/2)) (universal substitution).
  Step 3: s_{λ,r}(Q) = Q^{n(λ)} · ∏ (1 - X·Q^c)/(1 - Q^h), Q = q².
  Step 4: y_λ(q) = s_λ / Σ_µ d_µ s_µ.
  Step 5: Factor over Q in √q to expose cyclotomic structure.

Usage:
    from y_lambda_recipe_from_partition import y_lambda
    y = y_lambda([3, 1])  # returns sympy expression in q
"""
from __future__ import annotations
import json
import sys
from math import factorial
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: E402


# --- Step 1: Partition data ------------------------------------------------

def cells(lam):
    """List of (i, j) cells (1-indexed) of partition lam."""
    return [(i + 1, j + 1) for i, li in enumerate(lam) for j in range(li)]


def content(lam, i, j):
    """c(i, j) = j - i."""
    return j - i


def hook(lam, i, j):
    """h(i, j) = arm + leg + 1, with i, j 1-indexed."""
    arm = lam[i - 1] - j  # cells right of (i, j) in row i
    leg = sum(1 for r in range(i, len(lam)) if lam[r] > j - 1)
    return arm + leg


def hook_alt(lam, i_idx, j_idx):
    """Alternate (0-indexed) hook: row i_idx, col j_idx."""
    arm = lam[i_idx] - j_idx - 1
    leg = sum(1 for r in range(i_idx + 1, len(lam)) if lam[r] > j_idx)
    return arm + leg + 1


def n_partition(lam):
    """n(λ) := Σ (i-1) λ_i, i 1-indexed."""
    return sum(i * li for i, li in enumerate(lam))


def hook_dim(lam):
    """f^λ via hook formula = n! / ∏ h(i,j)."""
    n = sum(lam)
    prod = 1
    for i_idx in range(len(lam)):
        for j_idx in range(lam[i_idx]):
            prod *= hook_alt(lam, i_idx, j_idx)
    return factorial(n) // prod


# --- Step 2: Universal X substitution -------------------------------------

def make_q_X():
    """Return (q symbol, X expression in terms of q)."""
    q = sp.symbols('q', positive=True)
    sqrt_q = sp.sqrt(q)
    X = q * sqrt_q / (1 + q - q**2 - q**3 + q * sqrt_q)
    return q, X


# --- Step 3: Schur principal-specialisation -------------------------------

def schur_principal(lam, q, X):
    """s_{λ, r}(Q) = Q^{n(λ)} · ∏ (1 - X·Q^c) / (1 - Q^h), Q = q²."""
    Q = q ** 2
    n_lam = n_partition(lam)
    num = sp.S(1)
    den = sp.S(1)
    for i_idx in range(len(lam)):
        for j_idx in range(lam[i_idx]):
            c = j_idx - i_idx  # 0-indexed: same as (j_idx+1) - (i_idx+1)
            h = hook_alt(lam, i_idx, j_idx)
            num *= (1 - X * Q**c)
            den *= (1 - Q**h)
    return Q**n_lam * num / den


def partitions_of(n):
    """All partitions of n in non-increasing order."""
    if n == 0:
        return [()]
    def gen(rem, mxp):
        if rem == 0:
            yield ()
            return
        for p in range(min(mxp, rem), 0, -1):
            for rest in gen(rem - p, p):
                yield (p,) + rest
    return list(gen(n, n))


# --- Step 4 & 5: Normalise + factor ---------------------------------------

def y_lambda(lam):
    """Return y_λ(q) as a sympy expression in √q (after factor over ℚ)."""
    q, X = make_q_X()
    n = sum(lam)
    parts = partitions_of(n)
    s_vals = {tuple(mu): schur_principal(list(mu), q, X) for mu in parts}
    Z = sum(hook_dim(list(mu)) * s_vals[tuple(mu)] for mu in parts)
    y = s_vals[tuple(lam)] / Z
    # Cancel and factor over ℚ in t = √q
    t = sp.symbols('t', positive=True)
    y_in_t = y.subs(q, t**2)
    y_factored = sp.cancel(y_in_t)
    num, den = sp.fraction(y_factored)
    num_f = sp.factor(num)
    den_f = sp.factor(den)
    # Convert back to q for display: t = √q
    num_q = num_f.subs(t, sp.sqrt(q))
    den_q = den_f.subs(t, sp.sqrt(q))
    return {
        "lam": list(lam),
        "n": n,
        "y_in_q": str(y),
        "y_in_t_factored_num": str(num_f),
        "y_in_t_factored_den": str(den_f),
        "y_in_q_num": str(num_q),
        "y_in_q_den": str(den_q),
        "y_polynomial": expose_polynomial(y, q, simplify=False),
    }


def main():
    """Demo: run the recipe on all partitions of n = 2, 3, 4."""
    print("Recipe demo: y_λ(q) via Wenzl-bridge in √q form")
    print("=" * 70)
    print()

    out = {}
    for n in [2, 3, 4]:
        print(f"--- n = {n} ---")
        n_results = []
        for lam in partitions_of(n):
            r = y_lambda(list(lam))
            print(f"\n  λ = {list(lam)}  (dim = {hook_dim(list(lam))})")
            print(f"    factored num (in t = √q): {r['y_in_t_factored_num']}")
            print(f"    factored den (in t = √q): {r['y_in_t_factored_den']}")
            n_results.append(r)
        out[str(n)] = n_results
        print()

    out_path = Path(__file__).parent / "y-lambda-recipe-from-partition.witness.json"
    with open(out_path, "w") as fp:
        json.dump({
            "computation": "y-lambda-recipe-from-partition",
            "description": (
                "Complete recipe λ ↦ y_λ(q) via the Wenzl-bridge with X "
                "substitution, factored over Q in √q. Implements the 5-step "
                "algorithm in prop:y-lambda-recipe-from-partition."
            ),
            "X_in_q": "q^(3/2) / (1 + q - q² - q³ + q^(3/2))",
            "results": out,
            "precision": "symbolic_q",
            "truncation_eps": 0.0,
        }, fp, indent=2, default=str)
    print(f"Witness: {out_path}")


if __name__ == "__main__":
    main()
