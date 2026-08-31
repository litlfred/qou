#!/usr/bin/env python3
"""Mathas Lemma 3.13: does `l(d(t)) = l(d(g)) + l(w)` actually hold?

Exact integer arithmetic throughout — tableaux are tuples of tuples of ints, permutations
are tuples, and Coxeter length is the inversion count.  No float appears anywhere.

Lemma 3.13 (Mathas, *Iwahori-Hecke Algebras and Schur Algebras of the Symmetric Group*):
for a row-standard, non-standard lambda-tableau `t` there exist a Garnir tableau `g` and
`w in S_n` with `t = g . w` and `l(d(t)) = l(d(g)) + l(w)`.

This is the one ingredient of the Murphy spanning argument with NO `q = 1` antecedent in
the corpus: Sagan's Garnir straightening never tracks Coxeter lengths, so there is nothing
to transport and the statement has to be established from scratch.  Before formalising it,
measure it — twice this session a probe of a finite claim about small `n` refuted a target
that would otherwise have cost a tranche.

**The (i,j)th Garnir tableau**, per Mathas §3 (the definition is verified below against his
own three worked examples for `lambda = (3,3)`): with `a = t^lambda(i,j)` and
`b = t^lambda(i+1,j)`, all entries `< a` or `> b` keep their positions from `t^lambda`, and
`a, a+1, ..., b` are placed in increasing order left to right into the remaining cells,
**first along row i+1, then along row i**.
"""

from itertools import combinations

# ------------------------------------------------------------------ permutations

def compose(u, v):
    """(u after v)(x) = u(v(x)); 1-based dicts held as 0-indexed tuples."""
    return tuple(u[v[i]] for i in range(len(v)))

def inverse(w):
    out = [0] * len(w)
    for i, wi in enumerate(w):
        out[wi] = i
    return tuple(out)

def length(w):
    n = len(w)
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])

# --------------------------------------------------------------------- tableaux

def partitions(n):
    def rec(n, cap):
        if n == 0:
            yield ()
            return
        for k in range(min(n, cap), 0, -1):
            for rest in rec(n - k, k):
                yield (k,) + rest
    return list(rec(n, n))

def row_superstandard(lam):
    rows, e = [], 1
    for r in lam:
        rows.append(tuple(range(e, e + r)))
        e += r
    return tuple(rows)

def row_standard_tableaux(lam):
    """Every filling whose rows increase left to right: an ordered set partition of
    {1..n} into blocks of sizes lam, each block sorted."""
    n = sum(lam)
    out = []

    def rec(remaining, acc):
        if not remaining_shape(acc, lam):
            out.append(tuple(acc))
            return
        i = len(acc)
        for blk in combinations(sorted(remaining), lam[i]):
            rec(remaining - set(blk), acc + [tuple(blk)])

    def remaining_shape(acc, lam):
        return len(acc) < len(lam)

    rec(set(range(1, n + 1)), [])
    return out

def cells_of(lam):
    return [(i, j) for i, L in enumerate(lam) for j in range(L)]

def entry_at(t, c):
    return t[c[0]][c[1]]

def perm_from_tableaux(src, dst, lam):
    """The permutation p with p(src(c)) = dst(c) for every cell c, 0-indexed."""
    n = sum(lam)
    p = [0] * n
    for c in cells_of(lam):
        p[entry_at(src, c) - 1] = entry_at(dst, c) - 1
    return tuple(p)

def d_of(t, lam):
    """d(t): t = t^lambda . d(t)."""
    return perm_from_tableaux(row_superstandard(lam), t, lam)

# ---------------------------------------------------------- the Garnir tableau

def garnir_tableau(lam, i, j):
    """The (i,j)th Garnir tableau, 0-indexed (i,j).  Requires (i+1, j) to be a cell."""
    tl = row_superstandard(lam)
    a = tl[i][j]
    b = tl[i + 1][j]
    free = [c for c in cells_of(lam) if a <= entry_at(tl, c) <= b]
    # fill order: along row i+1 first (left to right), then along row i
    order = ([c for c in free if c[0] == i + 1] +
             [c for c in free if c[0] == i] +
             [c for c in free if c[0] not in (i, i + 1)])
    assert len(order) == len(free), "Garnir free set spans more than two rows"
    rows = [list(r) for r in tl]
    for val, c in zip(range(a, b + 1), order):
        rows[c[0]][c[1]] = val
    return tuple(tuple(r) for r in rows)

def descent_nodes(t, lam):
    """0-indexed (i,j) with (i+1,j) a cell and t(i,j) > t(i+1,j)."""
    return [(i, j) for i in range(len(lam) - 1) for j in range(lam[i + 1])
            if t[i][j] > t[i + 1][j]]

def is_standard(t, lam):
    return not descent_nodes(t, lam)

# ------------------------------------------------------------- the verification

def verify_definition():
    """Mathas' own three examples for lambda = (3,3)."""
    lam = (3, 3)
    expect = {(0, 0): ((2, 3, 4), (1, 5, 6)),
              (0, 1): ((1, 4, 5), (2, 3, 6)),
              (0, 2): ((1, 2, 6), (3, 4, 5))}
    ok = True
    for ij, want in expect.items():
        got = garnir_tableau(lam, *ij)
        flag = "OK " if got == want else "MISMATCH"
        if got != want:
            ok = False
        print(f"    g_{ij[0]+1}{ij[1]+1} = {got}   {flag}")
    return ok

def run(n):
    total = 0
    exists_ok = 0
    first_ok = 0
    failures = []
    for lam in partitions(n):
        for t in row_standard_tableaux(lam):
            if is_standard(t, lam):
                continue
            total += 1
            nodes = descent_nodes(t, lam)
            dt = d_of(t, lam)
            hit_any = False
            for k, (i, j) in enumerate(nodes):
                g = garnir_tableau(lam, i, j)
                # t = g . w  =>  w(g(c)) = t(c)
                w = perm_from_tableaux(g, t, lam)
                dg = d_of(g, lam)
                assert compose(w, dg) == dt, "d(t) = w . d(g) failed -- convention error"
                if length(dt) == length(dg) + length(w):
                    hit_any = True
                    if k == 0:
                        first_ok += 1
                    break
                elif k == 0:
                    pass
            if hit_any:
                exists_ok += 1
            else:
                failures.append((lam, t, nodes, length(dt),
                                 [(length(d_of(garnir_tableau(lam, *ij), lam)),
                                   length(perm_from_tableaux(garnir_tableau(lam, *ij), t, lam)))
                                  for ij in nodes]))
    print(f"n = {n}: {total} row-standard non-standard tableaux")
    print(f"    SOME descent node gives l(d(t)) = l(d(g)) + l(w):  {exists_ok}/{total}")
    print(f"    the FIRST descent node does:                       {first_ok}/{total}")
    if failures:
        lam, t, nodes, ldt, pairs = failures[0]
        print(f"    first failure: lambda={lam} t={t}")
        print(f"        l(d(t)) = {ldt}; per node (l(d(g)), l(w)) = {pairs}")
    return total, exists_ok, first_ok


if __name__ == "__main__":
    print("Garnir-tableau definition, against Mathas' worked examples for lambda = (3,3):")
    if not verify_definition():
        raise SystemExit("Garnir tableau construction does not match the source -- stop.")
    print()
    for n in (3, 4, 5, 6):
        run(n)
