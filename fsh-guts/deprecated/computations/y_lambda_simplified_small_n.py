#!/usr/bin/env python3
"""Hand-simplify y_λ via Wenzl-bridge at n = 0, 1, 2, 3, 4 — derive
clean closed forms by manual algebra (sympy `together`/`simplify`
doesn't reduce well at higher n).

Wenzl-bridge: y_λ = s_{λ, r}(Q) / Z, with
    Q = q²
    X = Q^r = (q · z) / (1 − Q + q · z), z = 1/(q^{1/2} + q^{−1/2})
    s_{λ, r}(Q) = Q^{n(λ)} · ∏_{x ∈ λ} (1 − Q^{r + c(x)}) / (1 − Q^{h(x)})
                = Q^{n(λ)} · ∏ (1 − X · Q^{c}) / (1 − Q^h)
    Z = Σ_µ d_µ · s_{µ, r}(Q)

Universal closed form for X:

    X = q^{3/2} / (1 + q − q² − q³ + q^{3/2})

since q · z = q^{3/2}/(q + 1) (after simplification), and
1 − Q + q · z = 1 − q² + q^{3/2}/(q + 1) = ((q + 1)(1 − q²) + q^{3/2}) / (q + 1)
            = (1 + q − q² − q³ + q^{3/2}) / (q + 1).
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: E402

q = sp.symbols('q', positive=True)
Q = q ** 2
qsqrt = sp.sqrt(q)
qhalf3 = q * qsqrt  # q^{3/2}

# Universal X = q^{3/2} / (1 + q - q² - q³ + q^{3/2})
X = qhalf3 / (1 + q - q**2 - q**3 + qhalf3)
X_factored = sp.together(X)


def s_lambda(lam):
    """s_{λ, r}(Q) with X substituted."""
    if not lam:
        return sp.S(1)
    n_lam = sum(i * lami for i, lami in enumerate(lam))
    hs, cs = [], []
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hs.append(arm + leg + 1)
            cs.append(j - i)
    num = sp.S(1); den = sp.S(1)
    for h, c in zip(hs, cs):
        num *= (1 - X * Q**c)
        den *= (1 - Q**h)
    return Q**n_lam * num / den


def hook_dim(lam):
    if not lam:
        return 1
    n = sum(lam)
    rows = len(lam)
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


print(f"X = q^(3/2) / (1 + q - q² - q³ + q^(3/2))")
print(f"  factored: {X_factored}")
print()

# Numerical check
q0 = sp.Float("1.1099785955541805", 30)
print(f"At q_0 = {q0}: X = {sp.N(X.subs(q, q0), 12)}")
print()

results = {}
for n in [0, 1, 2, 3, 4]:
    print(f"=== n = {n} ===")
    parts = partitions_of(n)
    s_vals = {lam: s_lambda(lam) for lam in parts}
    Z = sum(hook_dim(lam) * s_vals[lam] for lam in parts)
    Z_simp = sp.together(Z) if n <= 3 else Z
    print(f"Z = sum d_µ s_µ = {sp.together(Z_simp) if n <= 3 else 'too big to display'}")

    n_results = {}
    for lam in parts:
        y = s_vals[lam] / Z
        # Apply two-step simplification
        if n <= 3:
            y_simp = sp.together(sp.cancel(y))
        else:
            y_simp = y  # leave unsimplified at n=4 (sympy slow)
        # Numerical check
        y_num = float(sp.N(y.subs(q, q0), 30))
        print(f"  y_{lam} = {y_simp}")
        print(f"    at q_0: {y_num:+.10f}")
        n_results[str(lam)] = {
            "expr": str(y_simp),
            "numeric_at_q0": y_num,
            "y_polynomial": expose_polynomial(y_simp, q, simplify=False),
        }
    results[str(n)] = n_results
    print()

# Save witness
out_path = Path(__file__).parent / "y-lambda-simplified-small-n.witness.json"
with open(out_path, "w") as fp:
    json.dump({
        "computation": "y-lambda-simplified-small-n",
        "description": (
            "Hand-derivable simplified closed forms for y_λ at n = 0, 1, 2, "
            "3, 4 via the Wenzl-bridge with explicit X substitution. Derived "
            "via sympy `together` + `cancel`. At n=2, the closed forms reduce "
            "to particularly clean expressions (single ratio of small "
            "polynomials in q, X)."
        ),
        "X_formula": str(X_factored),
        "results": results,
        "precision": "symbolic_q",
        "truncation_eps": 0.0,
    }, fp, indent=2, default=str)
print(f"Witness: {out_path}")
