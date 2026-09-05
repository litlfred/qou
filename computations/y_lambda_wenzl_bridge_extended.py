#!/usr/bin/env python3
"""Extend symbolic y_λ to n = 2, ..., 12 via Wenzl-bridge formula.

Uses: y_λ = s_{λ, r}(Q) / (Σ_µ d_µ s_{µ, r}(Q))

with Q = q² and r solved from q · z = Q^r (1 - Q) / (1 - Q^r).

Avoids the O(p(n)³) linear-system solve (which times out at n=5 for
sympy and at n=12 for MPFR seminormal matmul) — Schur principal-
specialization is O(p(n) · max_hooks), tractable through n=12.

CONVENTION D (migrated 2026-08-10, bean qou-8x1l). z = q³/(q²+1), which
forces r = 2 — see the derivation in main(). Consequence: y_λ = 0 for every
partition with ℓ(λ) ≥ 3, automatically, because a Schur polynomial in two
variables vanishes there.

Un-deprecated for this migration. It had been filed under `_deprecated/` as
an exploration, but its witness never moved with it and six live producers
read that witness — `delta_lambda_empirical_tabulation`,
`per_irrep_pole_atom_crystal`, `phase5/phase1c_proton_h3_symbolic_decomposition`,
`rho_k_co_casimir_extended`, `rho_k_h3a_refinement`,
`sigma_shell_from_beta_chain`. Per `_deprecated/README.md`, reviving an
exploration is just running the producer to re-emit its witness.

The old note here claimed verification against y-lambda-symbolic-witness.json
at n = 3, 4. That file is convention C too (20 sqrt-bearing expressions), so
the agreement confirmed only that both were built the same way. The check
that now stands in its place is downstream and falsifiable: the Schur-Weyl
identity Σ_λ y_λ χ^λ(β_D) = tr_M(β_D) in `rho_k_h3a_refinement`, which failed
at 4.75e-8 against the convention-C weights.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path
import sys
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: E402
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


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
    # Bridge: q · z = Q^r (1-Q) / (1-Q^r), Q = q².
    #
    # CONVENTION D.  z = q³/(q² + 1), and the bridge then forces r = 2 exactly:
    #
    #   r = 2:  Q²(1-Q)/(1-Q²) = Q²(1-Q)/((1-Q)(1+Q)) = Q²/(1+Q) = q⁴/(1+q²)
    #           so  q · z = q⁴/(1+q²)  ⟺  z = q³/(q²+1).
    #
    # That is the *whole* content of the convention change here, and it is not
    # a re-parameterisation: r is the number of variables in the Schur
    # principal specialisation, so r = 2 says the fibre is two-dimensional.
    # A Schur polynomial in two variables vanishes identically once the
    # partition has a third row — concretely, the cell at (i, j) = (2, 0) has
    # content c = -2, so the factor (1 - X·Q^c) below is (1 - Q⁰) = 0 and
    # kills the numerator.
    #
    # So convention D's "y_λ = 0 for ℓ(λ) ≥ 3" is not an extra rule bolted on
    # top of this formula. It falls out of r = 2, which is Schur-Weyl on a
    # two-dimensional fibre. Of the 270 partitions emitted for n = 2..12, the
    # 223 with three or more rows are now exactly zero.
    #
    # The previous convention-C line was
    #     z_sym = 1 / (sp.sqrt(q) + 1/sp.sqrt(q))     # = √q/(q+1)
    # which solves to a NON-integer r, so nothing vanished and every dead
    # block carried a live weight. The sqrt is also the detector signature:
    # D is rational in q and never calls sqrt (cf. `markov_z` in gram.rs),
    # so a half-integer power of q in a weight expression is C on sight.
    Q_sym = q**2
    z_sym = q**3 / (q**2 + 1)
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
    for n in range(2, 13):
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
        y_exprs = {}
        for lam in parts:
            y_unsimp = s_vals[lam] / Z
            # Substitute X → q-rational form
            y_with_X = y_unsimp.subs(Xs, X)
            y_exprs[str(lam)] = y_with_X
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
                {
                    "partition": list(lam),
                    "y_lambda_symbolic": y_results[str(lam)],
                    "y_lambda_polynomial": expose_polynomial(
                        y_exprs[str(lam)], q, simplify=False
                    ),
                }
                for lam in parts
            ],
            "compute_time_sec": elapsed,
        }

    # Write witness
    out_path = Path(__file__).parent / "y-lambda-wenzl-bridge-symbolic-witness.json"
    full = {
        "computation": "y-lambda-wenzl-bridge-symbolic",
        "description": (
            "Symbolic closed-form y_λ for n = 2, ..., 12 via the Wenzl bridge: "
            "y_λ = s_{λ, r}(Q) / Σ_µ d_µ s_{µ, r}(Q) with Q = q² and "
            "r solved from q · z = Q^r (1-Q) / (1-Q^r), z = q³/(q²+1) "
            "(CONVENTION D), which forces r = 2 exactly. Since r is the number "
            "of variables in the Schur principal specialisation, r = 2 is a "
            "two-dimensional fibre and y_λ = 0 identically for ℓ(λ) ≥ 3 — of the "
            "270 partitions here, the 223 with three or more rows are exact "
            "zeros. Convention C (z = 1/(q^{1/2} + q^{-1/2})) solved to a "
            "non-integer r, so no weight vanished. "
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
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out_path
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as fp:
        json.dump(full, fp, indent=2, default=str)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
