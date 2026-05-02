#!/usr/bin/env python3
"""
Symbolic y_λ computation: exact q-rational forms via sympy.

For the Iwahori–Hecke algebra H_n(R, q) with Markov parameter
z = 1/(√q + 1/√q), the Markov-trace block weights y_λ are the
unique solution of the linear system

    Σ_λ χ_λ(w_μ) · y_λ  =  z^{n-len(μ)},   μ ⊢ n.

Solving this with q kept symbolic (sympy.Symbol) gives y_λ as exact
q-rational functions — no numerical interpolation, no Padé
ambiguity, no condition-number issue.

Pure-Python sympy is feasible for n ≤ 4: n = 2, 3 finish in well
under 10 s; n = 4 takes roughly a minute on commodity hardware
(~60 s observed).  n = 5 is beyond pure sympy by both paths tested:
  - `simplify_each=True`  (default): timed out after 20 min on the
    7×7 character matrix with length-4 generator products.
  - `simplify_each=False` (skip): sympy's HeuristicGCDFailed in the
    later `Matrix.solve` simplification step.
For n ≥ 5 the sibling Rust kernel
(phase-b-heavy-rust-character-kernel) is preferred.

References:
- prop:alpha-k-derivation-procedure §"Symbolic linear-system solve"
- prop:explicit-alpha-k-h3 (the H_3 closed form is the n=3 case of this)
- [geck-pfeiffer] "Characters of Finite Coxeter Groups and Iwahori–Hecke Algebras"
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401

sys.path.insert(0, str(Path(__file__).parent))
from hecke_characters import partitions_of, standard_young_tableaux


def symbolic_seminormal_matrices(shape, q):
    """Build seminormal matrices for partition `shape` with q kept
    symbolic.  Returns (sigmas, dim, syts) where each sigma is a
    sympy Matrix of size dim × dim with entries in Q(q^{1/2})."""
    n = sum(shape)
    syts, _cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], dim, syts
    h = q - 1 / q
    sigmas = []
    for k in range(1, n):
        M = sp.zeros(dim, dim)
        processed: set = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (1 - q ** (-2 * rho))
            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break
            if j is None:
                M[i, i] = a
                processed.add(i)
            else:
                a_prime = h / (1 - q ** (2 * rho))
                b_sq = a * a_prime + 1
                # b is a square root; keep sympy symbolic
                b = sp.sqrt(sp.simplify(b_sq))
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)
        sigmas.append(M)
    return sigmas, dim, syts


def cycle_type_word(mu):
    """Reduced word realising cycle type μ on n = sum(μ) strands."""
    word = []
    s = 0
    for m in mu:
        for j in range(m - 1):
            word.append(s + j + 1)
        s += m
    return word


def chi_lambda_symbolic(sigmas, dim, word, simplify_each=True):
    """χ_λ(σ_w) symbolic: trace of Π σ_{w_i}.

    Default `simplify_each=True` calls `sp.simplify` per character.
    Setting it to False skips the per-character simplify, which
    might in principle be faster, but at n=5 the unsimplified
    polynomial expansion triggers sympy's HeuristicGCDFailed in
    later linear-solve simplification.  Pure sympy for n ≥ 5 is
    therefore not feasible by either path; use the sibling Rust
    kernel.
    """
    if dim == 0:
        return sp.Integer(0)
    M = sp.eye(dim)
    for idx in word:
        M = M * sigmas[idx - 1]
    tr = sp.trace(M)
    return sp.simplify(tr) if simplify_each else tr


def solve_y_symbolic(n: int, q):
    """Solve y_λ symbolically at H_n with q kept symbolic.  Returns
    list of (partition, y_λ_symbolic) pairs."""
    parts = list(partitions_of(n))
    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))

    # Cache symbolic seminormal matrices per partition
    cache: dict = {}
    for lam in parts:
        sigmas, dim, _ = symbolic_seminormal_matrices(lam, q)
        cache[lam] = (sigmas, dim)

    p_n = len(parts)
    A = sp.zeros(p_n, p_n)
    b = sp.zeros(p_n, 1)
    for i, mu in enumerate(parts):
        word = cycle_type_word(mu)
        b[i, 0] = z ** (n - len(mu))
        for j, lam in enumerate(parts):
            sigmas, dim = cache[lam]
            A[i, j] = chi_lambda_symbolic(sigmas, dim, word)

    y_solution = A.solve(b)
    return [
        (list(lam), sp.simplify(y_solution[j, 0]))
        for j, lam in enumerate(parts)
    ]


def main(ns: list[int]) -> None:
    q = sp.Symbol("q", positive=True)
    out_path = Path(__file__).parent / "y-lambda-symbolic-witness.json"
    # Merge-aware: load existing witness so running with a subset of
    # n's preserves entries for the others.  Running `y_lambda_symbolic.py 5`
    # will keep n=2,3,4 entries intact rather than overwriting them.
    if out_path.exists():
        out: dict = json.loads(out_path.read_text())
    else:
        out = {"tables_by_n": {}}
    out["description"] = (
        "Exact q-rational y_λ via symbolic linear-system solve "
        "(sympy).  No interpolation, no Padé ambiguity — exact "
        "Markov-trace block weights as elements of Q(q^{1/2})."
    )
    out["references"] = [
        "prop:alpha-k-derivation-procedure",
        "prop:explicit-alpha-k-h3",
    ]
    out["computedAt"] = datetime.now(timezone.utc).isoformat()
    out.setdefault("tables_by_n", {})

    preserved = sorted(
        (k for k in out["tables_by_n"] if int(k) not in ns),
        key=int,
    )
    if preserved:
        print(f"Preserving existing entries for n in {preserved}\n")
    for n in ns:
        print(f"Solving y_λ symbolically at H_{n}(R, q) (n={n})...")
        ys = solve_y_symbolic(n, q)
        out["tables_by_n"][str(n)] = {
            "n": n,
            "weights": [
                {
                    "partition": lam,
                    "y_lambda_symbolic": sp.sstr(y_sym),
                    "y_lambda_simplified_factored": sp.sstr(sp.factor(y_sym)),
                }
                for lam, y_sym in ys
            ],
        }
        for lam, y_sym in ys:
            print(f"  λ = {lam}: y_λ = {sp.sstr(sp.factor(y_sym))}")
        print()

    out_path.write_text(json.dumps(out, indent=2))
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    # Default: small n where pure-Python sympy completes within a
    # minute (n = 2, 3 in seconds; n = 4 ~60 s).  n = 5 is beyond the
    # 20-min budget here and triggers HeuristicGCDFailed when the
    # per-character simplify is skipped; use the sibling Rust kernel.
    ns = [int(a) for a in sys.argv[1:]] or [2, 3, 4]
    main(ns)
