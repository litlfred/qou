#!/usr/bin/env python3
"""Are the double-coset terms `T_d · x_mu · T_e` linearly independent?  (bean qou-phir)

NO — and this probe exists because I proposed proving that they are.

`CompositionDoubleCoset.mul_xComp_mul_mem` proves the SPAN statement: every
`X · x_mu · Y` lies in the span of `{T_d · x_mu · T_e : d in D_mu, e^{-1} in D_mu}`.
The natural-looking follow-up — that those terms are a BASIS of `H x_mu H` —
is false, and the counting is decisive before any Lean is attempted.

The extreme case settles it.  Take `mu = (1,1,...,1)`, all blocks singletons:

  * `S_mu` is the TRIVIAL subgroup, so `x_mu = T_1 = 1`;
  * every `d` is distinguished (the condition quantifies over pairs in a common
    block, and no two distinct positions share one), so `D_mu = S_n`;
  * the family is therefore `{T_d · T_e : d, e in S_n}` — `(n!)^2` members in a
    space of dimension `n!`.

For `n >= 2` that is more members than dimensions, so they cannot be independent.
No numerics are needed for that; the probe below exhibits the collapse concretely
and measures how far from independent the family is across small `n` and several
compositions, which is the part worth having on record.

WHAT THE CORRECT STATEMENT LOOKS LIKE.  Murphy's basis is indexed by pairs of
STANDARD tableaux OF A COMMON SHAPE, summed over shapes — not by pairs drawn from
one `D_mu`.  The corpus already carries the matching count:
`HeckeMurphyYoung.murphyIndex_card_eq_finrank` shows that index set has exactly
`dim H_n(q)` elements, via the RSK/Burnside identity.  So the span statement plus
that cardinality is the route to a basis; independence of the pair-indexed family
is not, and is false.

NO FLOAT64: every coefficient is a sympy rational function in `q`.
"""

from itertools import permutations
import sympy as sp

q = sp.Symbol("q")


def length(w):
    n = len(w)
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])


def right_mul_s(w, i):
    v = list(w)
    v[i], v[i + 1] = v[i + 1], v[i]
    return tuple(v)


def reduced_word(w):
    """A reduced word for `w`; the sorting word reversed (see tw_inverse_support_probe)."""
    v = list(w)
    n = len(v)
    sorting = []
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
                sorting.append(i)
                changed = True
    return list(reversed(sorting))


def sigma_mul(elt, i):
    """sigma_i · x, in the corpus's flipped convention (see QOU/Hecke/TwMul.lean)."""
    out = {}
    for w, c in elt.items():
        ws = right_mul_s(w, i)
        if length(ws) > length(w):
            out[ws] = out.get(ws, 0) + c
        else:
            out[ws] = out.get(ws, 0) + q * c
            out[w] = out.get(w, 0) + (q - 1) * c
    return {w: sp.cancel(c) for w, c in out.items() if sp.cancel(c) != 0}


def tw(w, n):
    elt = {tuple(range(n)): sp.Integer(1)}
    for i in reduced_word(w):
        elt = sigma_mul(elt, i)
    return elt


def mul(x, y, n):
    total = {}
    for v, cv in x.items():
        acc = dict(y)
        for i in reduced_word(v):
            acc = sigma_mul(acc, i)
        for w, cw in acc.items():
            total[w] = total.get(w, 0) + cv * cw
    return {w: sp.cancel(c) for w, c in total.items() if sp.cancel(c) != 0}


def blocks_of(comp, n):
    """index[x] = which block position x lies in."""
    idx, b, seen = [], 0, 0
    for size in comp:
        for _ in range(size):
            idx.append(b)
            seen += 1
        b += 1
    assert seen == n, (comp, n)
    return idx


def young(comp, n):
    idx = blocks_of(comp, n)
    return [w for w in permutations(range(n)) if all(idx[w[x]] == idx[x] for x in range(n))]


def is_distinguished(comp, d, n):
    idx = blocks_of(comp, n)
    return all(
        not (idx[d[a]] == idx[d[b]] and a < b and d[a] > d[b])
        for a in range(n) for b in range(n)
    )


def x_comp(comp, n):
    total = {}
    for v in young(comp, n):
        for w, c in tw(v, n).items():
            total[w] = total.get(w, 0) + c
    return {w: sp.cancel(c) for w, c in total.items() if sp.cancel(c) != 0}


def rank_of(vectors, n):
    """Rank over Q(q) of a list of elements, each a dict perm -> coefficient."""
    basis = sorted(permutations(range(n)))
    rows = [[v.get(w, sp.Integer(0)) for w in basis] for v in vectors]
    if not rows:
        return 0
    return sp.Matrix(rows).rank()


def main():
    print("Double-coset terms T_d · x_mu · T_e — independent?  (exact over Q(q))\n")
    comps = {2: [[2], [1, 1]], 3: [[3], [2, 1], [1, 1, 1]], 4: [[2, 2], [1, 1, 1, 1]]}
    print(f"  {'n':>2} {'mu':<12} {'|D_mu|':>7} {'#pairs':>7} {'rank':>5} {'dim H':>6}  verdict")
    for n, cs in comps.items():
        dim = int(sp.factorial(n))
        for comp in cs:
            D = [d for d in permutations(range(n)) if is_distinguished(comp, d, n)]
            # left-distinguished = inverse is distinguished
            DL = [e for e in permutations(range(n))
                  if is_distinguished(comp, tuple(sorted(range(n), key=lambda i: e[i])), n)]
            x = x_comp(comp, n)
            terms = [mul(mul(tw(d, n), x, n), tw(e, n), n) for d in D for e in DL]
            r = int(rank_of(terms, n))
            npairs = len(D) * len(DL)
            verdict = "independent" if r == npairs else f"DEPENDENT ({npairs - r} excess)"
            print(f"  {n:>2} {str(tuple(comp)):<12} {len(D):>7} {npairs:>7} {r:>5} {dim:>6}  {verdict}")

    print("\n  The (1,...,1) rows are the decisive ones: x_mu = 1 and D_mu = S_n,")
    print("  so the family is {T_d T_e} — (n!)^2 members in an n!-dimensional space.")
    print("  No measurement is needed to see that cannot be independent for n >= 2;")
    print("  the ranks above only show how far off it is.")


if __name__ == "__main__":
    main()
