#!/usr/bin/env python3
"""Is the canonical symmetrizing trace's Schur element Wenzl's, and at which X?

`qou-kwoa`, option 3 step (i).  `QOU/Hecke/TauSchurElement.lean` defines the
ABSTRACT Schur element `s_lambda = 1 / c_lambda`, where `c_lambda` is the weight
of the canonical trace `tau` (`tau(T_w) = delta_{w,1}`) on the lambda-block.
`QOU/MathlibExt/WenzlSchurElement.lean` carries a DIFFERENT object, Wenzl's
two-parameter

    schurElement Q X lam = Q^{n(lam)} * prod_x (1 - X Q^{c(x)}) / (1 - Q^{h(x)}),

and `SchurElementCriterion` is stated with THAT one.  Identifying them is what
option 3 needs, and the statement is not even well posed until `X` is pinned.

CONVENTION CLASH, measured rather than assumed.  In this corpus `schurElement`
feeds `jonesMarkovCoeff Q X lam = schurElement / wenzlNormalisation`, documented
as the Jones-Markov coefficient `y_lambda` -- i.e. a WEIGHT of the Markov trace.
Geck-Pfeiffer's Schur element is a RECIPROCAL weight (`tau = sum (1/s) chi`).
So the two names denote reciprocal-flavoured objects of two DIFFERENT traces,
and "tau's weights are 1/s_lambda" cannot be read off the names.

THE CLAIM UNDER TEST.  The content factors `(1 - X Q^{c(x)})` are exactly what
distinguishes the Markov trace from `tau`; they disappear at `X = 0`.  So the
candidate is

    c_lambda  ==  (1 - Q)^n * schurElement(Q, X=0, lambda)                 (*)

with `n = |lambda|`.  Everything is exact symbolic in `Q` -- sympy Rational and
polynomial arithmetic only, no float anywhere (NO-FLOAT64 applies to probes).

WHAT IS TESTED, and the two tiers are NOT the same strength:

  TIER 1 (consistency, all n): sum_lambda f_lambda c_lambda == 1, i.e. tau(1)=1.
     This is implied by the Macdonald hook telescope the corpus ALREADY has, so
     passing it corroborates the normalisation but is NOT independent evidence
     for the per-block claim.

  TIER 2 (per-block, n = 2 and 3): build the regular representation of H_n(q)
     in the T_w basis from the corpus's own structure constants (`sigma_mul_Tw`),
     read the character table off it, solve `sum_lambda c_lambda chi_lambda(T_w)
     = delta_{w,1}` for the weights, and compare each one to (*).  THIS is the
     evidence.  It works only up to n = 3, because for n <= 3 the non-linear
     characters are recoverable from chi_reg, chi_triv and chi_sign alone.
"""

from __future__ import annotations

import itertools
import sympy as sp

Q = sp.Symbol("Q")

# ---------------------------------------------------------------- combinatorics


def partitions(n: int) -> list[tuple[int, ...]]:
    """Partitions of n, weakly decreasing."""
    if n == 0:
        return [()]
    out = []

    def rec(rest: int, cap: int, acc: tuple[int, ...]) -> None:
        if rest == 0:
            out.append(acc)
            return
        for part in range(min(rest, cap), 0, -1):
            rec(rest - part, part, acc + (part,))

    rec(n, n, ())
    return out


def hook_length(lam: tuple[int, ...], i: int, j: int) -> int:
    arm = lam[i] - j - 1
    leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
    return arm + leg + 1


def n_lambda(lam: tuple[int, ...]) -> int:
    """n(lambda) = sum_i i * lambda_i -- the prefactor WenzlSchurElement uses."""
    return sum(i * part for i, part in enumerate(lam))


def f_lambda(lam: tuple[int, ...]) -> int:
    """Number of standard Young tableaux, by the hook-length formula."""
    n = sum(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= hook_length(lam, i, j)
    return sp.factorial(n) // prod


def wenzl_schur(lam: tuple[int, ...], X) -> sp.Expr:
    """Q^{n(lam)} * prod_x (1 - X Q^{c(x)}) / (1 - Q^{h(x)}) -- the Lean def."""
    val = Q ** n_lambda(lam)
    for i, row in enumerate(lam):
        for j in range(row):
            val *= (1 - X * Q ** (j - i)) / (1 - Q ** hook_length(lam, i, j))
    return sp.together(sp.simplify(val))


def candidate_weight(lam: tuple[int, ...]) -> sp.Expr:
    """(*)  c_lambda = (1 - Q)^n * schurElement(Q, 0, lambda)."""
    n = sum(lam)
    return sp.cancel(sp.simplify((1 - Q) ** n * wenzl_schur(lam, sp.Integer(0))))


# ------------------------------------------------- the algebra, from the corpus


def perms(n: int) -> list[tuple[int, ...]]:
    """S_n as tuples; v[k] is the image of k."""
    return [tuple(p) for p in itertools.permutations(range(n))]


def length(v: tuple[int, ...]) -> int:
    return sum(1 for a in range(len(v)) for b in range(a + 1, len(v)) if v[a] > v[b])


def right_mul_s(v: tuple[int, ...], i: int) -> tuple[int, ...]:
    """v * s_i, with s_i the transposition (i, i+1) -- swaps POSITIONS i, i+1."""
    w = list(v)
    w[i], w[i + 1] = w[i + 1], w[i]
    return tuple(w)


def sigma_matrix(n: int, i: int, order: list[tuple[int, ...]]) -> sp.Matrix:
    """Left multiplication by sigma_i in the T_w basis.

    The rule is `QOU.Hecke.TwBasis.sigma_mul_Tw`, verbatim:

        sigma_i * T_v = T_{v s_i}                     if v(i) < v(i+1)
                      = (q-1) T_v + q T_{v s_i}       otherwise

    Column v holds the image of T_v.
    """
    idx = {w: k for k, w in enumerate(order)}
    M = sp.zeros(len(order), len(order))
    for v in order:
        col = idx[v]
        vs = right_mul_s(v, i)
        if v[i] < v[i + 1]:
            M[idx[vs], col] += 1
        else:
            M[col, col] += Q - 1
            M[idx[vs], col] += Q
    return M


def tw_matrices(n: int) -> tuple[list[tuple[int, ...]], dict]:
    """L_{T_w} for every w, built by walking a reduced word."""
    order = sorted(perms(n), key=lambda v: (length(v), v))
    sig = [sigma_matrix(n, i, order) for i in range(n - 1)]
    ident = sp.eye(len(order))
    mats = {order[0] if length(order[0]) == 0 else tuple(range(n)): ident}
    mats[tuple(range(n))] = ident
    # breadth-first over lengths: T_{v s_i} = sigma_i * T_v when the length rises
    frontier = [tuple(range(n))]
    while frontier:
        nxt = []
        for v in frontier:
            for i in range(n - 1):
                vs = right_mul_s(v, i)
                if length(vs) == length(v) + 1 and vs not in mats:
                    mats[vs] = sig[i] * mats[v]
                    nxt.append(vs)
        frontier = nxt
    return order, mats


def character_table(n: int, order, mats) -> dict:
    """chi_lambda(T_w) for every partition of n. Only valid for n <= 3."""
    lams = partitions(n)
    chi = {}
    chi[(n,)] = {w: Q ** length(w) for w in order}                       # trivial
    chi[tuple([1] * n)] = {w: sp.Integer(-1) ** length(w) for w in order}  # sign
    if n == 3:
        reg = {w: sp.expand(mats[w].trace()) for w in order}
        chi[(2, 1)] = {
            w: sp.cancel((reg[w] - chi[(3,)][w] - chi[(1, 1, 1)][w]) / 2)
            for w in order
        }
    if set(chi) != set(lams):
        raise RuntimeError(f"character table incomplete for n={n}")
    return chi


def solve_tau_weights(n: int, order, chi) -> dict:
    """Solve sum_lambda c_lambda chi_lambda(T_w) = delta_{w,1} for the weights."""
    lams = partitions(n)
    syms = {lam: sp.Symbol(f"c_{'_'.join(map(str, lam))}") for lam in lams}
    eqs = []
    for w in order:
        lhs = sum(syms[lam] * chi[lam][w] for lam in lams)
        rhs = sp.Integer(1) if length(w) == 0 else sp.Integer(0)
        eqs.append(sp.Eq(sp.expand(lhs), rhs))
    sol = sp.solve(eqs, list(syms.values()), dict=True)
    if len(sol) != 1:
        raise RuntimeError(f"tau weights not uniquely determined at n={n}: {sol}")
    return {lam: sp.cancel(sp.simplify(sol[0][syms[lam]])) for lam in lams}


# --------------------------------------------------------------------- the runs


def tier1(max_n: int) -> list[tuple[int, bool]]:
    print("TIER 1 -- consistency: sum_lambda f_lambda * c_lambda == 1 ?")
    print("  (implied by the Macdonald telescope at X=0; corroboration, not")
    print("   independent evidence for the per-block claim)")
    rows = []
    for n in range(1, max_n + 1):
        total = sum(f_lambda(lam) * candidate_weight(lam) for lam in partitions(n))
        ok = sp.simplify(sp.cancel(total) - 1) == 0
        rows.append((n, bool(ok)))
        print(f"  n={n}: {'PASS' if ok else 'FAIL  -> ' + str(sp.cancel(total))}")
    return rows


def tier2(n: int) -> bool:
    print(f"\nTIER 2 -- per-block at n={n}: solve for tau's weights, compare to (*)")
    order, mats = tw_matrices(n)
    chi = character_table(n, order, mats)
    weights = solve_tau_weights(n, order, chi)
    all_ok = True
    for lam in partitions(n):
        got = weights[lam]
        want = candidate_weight(lam)
        ok = sp.simplify(sp.cancel(got - want)) == 0
        all_ok = all_ok and bool(ok)
        print(f"  lambda={lam}: tau weight = {got}")
        print(f"             (1-Q)^n * s^Wenzl(X=0) = {want}   {'MATCH' if ok else 'DIFFER'}")
    return all_ok


def main() -> int:
    print(__doc__.split("\n\n")[0])
    print()
    rows = tier1(8)
    ok2 = tier2(2)
    ok3 = tier2(3)
    print()
    t1 = all(ok for _, ok in rows)
    print(f"TIER 1 (n=1..8, consistency) : {'PASS' if t1 else 'FAIL'}")
    print(f"TIER 2 (n=2, per-block)      : {'PASS' if ok2 else 'FAIL'}")
    print(f"TIER 2 (n=3, per-block)      : {'PASS' if ok3 else 'FAIL'}")
    print()
    if t1 and ok2 and ok3:
        print("VERDICT: X = 0 is the pure-Hecke specialisation, and the")
        print("         normalisation is (1-Q)^n. Per-block exact at n=2,3.")
        print("         Scope: n <= 3 only -- the character table is recoverable")
        print("         from chi_reg alone only up to n=3, so this is NOT a")
        print("         proof for general n. It pins the STATEMENT option 3")
        print("         must prove; it does not prove it.")
        return 0
    print("VERDICT: the candidate identification FAILS -- see the rows above.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
