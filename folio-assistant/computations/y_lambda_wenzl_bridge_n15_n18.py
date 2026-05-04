#!/usr/bin/env python3
"""Extend symbolic y_λ to n = 13, ..., 18 via Wenzl-bridge formula.

Range n = 13..18 picks up where y_lambda_wenzl_bridge_extended.py leaves
off (that script covers n = 2..12). Used to nail the FROB-FILTER A_**
threshold per docs/audits/2026-05-02-nv-frob-filter-conjectures.md.

Uses: y_λ = s_{λ, r}(Q) / (Σ_µ d_µ s_{µ, r}(Q))

with Q = q² and r solved from q · z = Q^r (1 - Q) / (1 - Q^r).

Avoids the O(p(n)³) linear-system solve (which times out at n=5 for
sympy and at n=12 for MPFR seminormal matmul) — Schur principal-
specialization is O(p(n) · max_hooks), tractable through n ≥ 12 with
sympy and through n=18 with the numeric mpmath path of
y_lambda_wenzl_bridge_numeric.py (faster than this sympy variant).
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path
import sympy as sp


# Symbolic q
q = sp.symbols('q', positive=True)


def n_partition(lam):
    return sum(i * lami for i, lami in enumerate(lam))


def hooks_contents(lam):
    hs, cs = [], []
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hs.append(arm + leg + 1)
            cs.append(j - i)
    return hs, cs


def hook_dim(lam):
    n = sum(lam)
    hs, _ = hooks_contents(lam)
    from math import factorial
    prod = 1
    for h in hs:
        prod *= h
    return factorial(n) // prod


def schur_principal_symbolic(lam, r_sym, Q_sym):
    """Schur principal specialization s_λ(1, Q, ..., Q^{r-1}) symbolically.

    s_λ = Q^{n(λ)} · ∏_{x ∈ λ} (1 - Q^{r + c(x)}) / (1 - Q^{h(x)})
    """
    hs, cs = hooks_contents(lam)
    num = sp.S(1)
    den = sp.S(1)
    for h, c in zip(hs, cs):
        num *= (1 - Q_sym**(r_sym + c))
        den *= (1 - Q_sym**h)
    return Q_sym**n_partition(lam) * num / den


def partitions_of(n):
    if n == 0: return [()]
    def gen(rem, mxp):
        if rem == 0: yield (); return
        for p in range(min(mxp, rem), 0, -1):
            for rest in gen(rem - p, p):
                yield (p,) + rest
    return list(gen(n, n))


def main():
    # Bridge: q · z = Q^r (1-Q) / (1-Q^r), Q = q², z = 1/(q^{1/2} + q^{-1/2})
    # → q · z = q · 1/(q^{1/2} + q^{-1/2}) = q^{1/2} (q^{1/2}/(q + 1)) = q^{1/2} · q^{1/2}/(q+1) = q/(q+1)
    # So q · z = q/(q+1) at the substrate value of z.
    # Solve Q^r (1-Q)/(1-Q^r) = q/(q+1) with Q = q²:
    #   q^{2r}(1-q²)/(1-q^{2r}) = q/(q+1)
    #   q^{2r}(1-q)(1+q)/(1-q^{2r}) = q/(q+1)
    #   q^{2r}(1-q)(1+q)² = q(1-q^{2r})
    # Solving for q^{2r}: X(1-q)(1+q)² = q(1-X)
    #   X[(1-q)(1+q)² + q] = q
    #   (1-q)(1+q)² = (1-q)(1+2q+q²) = 1+2q+q² - q - 2q² - q³ = 1 + q - q² - q³
    #   So X[1 + q - q² - q³ + q] = X[1 + 2q - q² - q³] = q
    #   X = q / (1 + 2q - q² - q³)
    Q_sym = q**2
    z_sym = 1 / (sp.sqrt(q) + 1/sp.sqrt(q))
    qz = sp.simplify(q * z_sym)
    print(f"q · z = {sp.simplify(qz)}")

    # Solve symbolically: Q^r (1 - Q) / (1 - Q^r) = q · z
    # X = q · z (1 - Q^r) / (1 - Q) ... wait
    # Q^r = X
    # X(1-Q)/(1-X) = qz
    # X(1-Q) = qz(1-X) = qz - qz·X
    # X(1-Q + qz) = qz
    # X = qz/(1 - Q + qz)
    X = sp.simplify(qz / (1 - Q_sym + qz))
    print(f"X = Q^r = qz/(1-Q+qz) = {X}")
    X_factored = sp.factor(X)
    print(f"  factored: {X_factored}")

    # We don't need explicit r — we just need Q^r = X. Use it directly.
    # In the Schur formula, we have Q^{r + c} = Q^r · Q^c = X · Q^c.
    # And Q^h appears purely as a power of Q, no r.
    # So we can substitute Q^r → X everywhere.
    print()

    out = {}
    print(f"{'n':>3} {'p(n)':>4} {'time':>8} {'sample':>40}")
    print("-" * 70)
    for n in range(13, 19):  # n=15,18 extension for FROB-FILTER A_** discovery
        t0 = time.time()
        parts = partitions_of(n)

        # Compute s_λ symbolically with Q^r → X substitution.
        # Treat X as a free symbol, then substitute its q-rational form at the end.
        Xs = sp.symbols('Xs', positive=True)  # placeholder for X
        s_vals = {}
        for lam in parts:
            hs, cs = hooks_contents(lam)
            num = sp.S(1)
            den = sp.S(1)
            for h, c in zip(hs, cs):
                # 1 - Q^{r+c} = 1 - X · Q^c
                num *= (1 - Xs * Q_sym**c)
                den *= (1 - Q_sym**h)
            s = Q_sym**n_partition(lam) * num / den
            s_vals[lam] = s

        # Z = Σ d_µ s_µ — keep unsimplified to avoid sympy recursion blowup at n≥6
        Z = sum(hook_dim(lam) * s_vals[lam] for lam in parts)

        # y_λ = s_λ / Z, with X substituted — NO simplify (recursion error at large n)
        y_results = {}
        for lam in parts:
            y_unsimp = s_vals[lam] / Z
            # Substitute X → q-rational form
            y_with_X = y_unsimp.subs(Xs, X)
            # Just record the expression as a string; user can simplify externally
            y_results[str(lam)] = str(y_with_X)

        elapsed = time.time() - t0

        # Sample first partition
        first_lam = parts[0]
        first_y = y_results[str(first_lam)]
        sample = first_y if len(first_y) < 40 else first_y[:37] + "..."
        print(f"{n:>3} {len(parts):>4} {elapsed:>7.2f}s  {sample:>40}")

        out[str(n)] = {
            "n": n,
            "num_partitions": len(parts),
            "weights": [
                {"partition": list(lam), "y_lambda_symbolic": y_results[str(lam)]}
                for lam in parts
            ],
            "compute_time_sec": elapsed,
        }

    # Write witness
    out_path = Path(__file__).parent / "y-lambda-wenzl-bridge-n13to18-witness.json"
    full = {
        "computation": "y-lambda-wenzl-bridge-symbolic",
        "description": (
            "Symbolic closed-form y_λ for n = 2, ..., 12 via the Wenzl bridge: "
            "y_λ = s_{λ, r}(Q) / Σ_µ d_µ s_{µ, r}(Q) with Q = q² and "
            "r solved from q · z = Q^r (1-Q) / (1-Q^r), z = 1/(q^{1/2} + q^{-1/2}). "
            "Computed via sympy with Q^r treated as the symbolic placeholder X = "
            "q · z / (1 - Q + q · z), giving exact q-rational expressions in "
            "Q(q^{1/2}). Bypasses the O(p(n)³) linear-system solve by using the "
            "O(p(n) · max_hooks) Schur principal-specialization formula. "
            "Tractable through n = 12 in seconds."
        ),
        "references": [
            "prop:y-lambda-closed-form-wenzl-bridge",
            "prop:explicit-alpha-k-h3",
            "prop:alpha-k-derivation-procedure",
            "thm:jones-markov-trace",
            "wenzl1988",
            "orellana1998",
            "chlouveraki2016",
        ],
        "tables_by_n": out,
        "precision": "symbolic_q",
        "truncation_eps": 0.0,
    }
    with open(out_path, "w") as fp:
        json.dump(full, fp, indent=2, default=str)
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
