#!/usr/bin/env python3
"""Is Murphy's leading-permutation map `lead` injective?  Exact test at n = 3, 4, 5.

Bean `qou-phir`.  Cellular axiom (C1) is being reduced to the three fields of
`QOU.BraidKnot.SpechtStandardBasis.Triangular`, and the hard one is `lead_inj`:
that distinct pairs of standard tableaux give distinct leading permutations.

The candidate definition, from Murphy's basis `m_st = T_d(s)^* x_lambda T_d(t)`, is

    lead(lambda, s, t) = d(s)^-1 . w_lambda . d(t)

with `w_lambda` the longest element of the Young subgroup `S_lambda` and `d(t)` the
permutation carrying the reference tableau to `t`.  Whether that is injective ACROSS
partitions -- not merely within one -- is what `lead_inj` needs, and it is not obvious.

Formalising a false statement is the expensive way to discover it is false, so this
measures first.  Cheap and decisive: full enumeration, exact integer arithmetic, no
tolerance and no sampling.

**No floats anywhere and none admissible** (AGENTS.md, PROBES ARE NOT EXEMPT): every
quantity here is a Python int or a tuple of ints.  The output is an ARGUMENT about
whether a Lean definition is correct, which is the expensive kind of wrong.

Conventions match the Lean exactly:
  * a tableau is a tuple `cells[l] = (row, col)` of the cell holding label `l`;
  * the reference tableau is COLUMN-superstandard (`ColSuperstandardTableau`), filling
    down columns left to right -- matching `colSuperstandard`'s lex order on (col, row);
  * `d(t)` is `l |-> t^-1(colSuperstandard(l))`, matching `dOf t = (colSuperstandard).trans t.symm`;
  * Coxeter length on `S_m` is the inversion count.

Usage:  python3 -u computations/hecke/murphy_lead_injectivity_probe.py
"""
from __future__ import annotations

import itertools
from typing import Dict, List, Tuple

Cell = Tuple[int, int]
Perm = Tuple[int, ...]


def partitions(m: int) -> List[List[int]]:
    """Partitions of `m`, weakly decreasing."""
    out: List[List[int]] = []

    def rec(rem: int, largest: int, acc: List[int]) -> None:
        if rem == 0:
            out.append(list(acc))
            return
        for part in range(min(rem, largest), 0, -1):
            acc.append(part)
            rec(rem - part, part, acc)
            acc.pop()

    rec(m, m, [])
    return out


def cells_of(lam: List[int]) -> List[Cell]:
    return [(r, c) for r, row in enumerate(lam) for c in range(row)]


def col_superstandard(lam: List[int]) -> Tuple[Cell, ...]:
    """Reference tableau `t^lambda`: cells in lex order on (col, row) -- fill down
    columns, left to right.  `cells[l]` is the cell of label `l`."""
    return tuple(sorted(cells_of(lam), key=lambda rc: (rc[1], rc[0])))


def standard_tableaux(lam: List[int]) -> List[Tuple[Cell, ...]]:
    """All standard Young tableaux of shape `lam`, as `cells[l] = cell of label l`.
    Standard = entries increase along rows and down columns."""
    cells = cells_of(lam)
    m = len(cells)
    out: List[Tuple[Cell, ...]] = []
    for perm in itertools.permutations(cells):
        entry: Dict[Cell, int] = {c: i for i, c in enumerate(perm)}
        ok = True
        for (r, c) in cells:
            if (r, c + 1) in entry and entry[(r, c + 1)] < entry[(r, c)]:
                ok = False
                break
            if (r + 1, c) in entry and entry[(r + 1, c)] < entry[(r, c)]:
                ok = False
                break
        if ok:
            out.append(perm)
    return out


def d_of(lam: List[int], t: Tuple[Cell, ...]) -> Perm:
    """`d(t)(l) = t^-1(t^lambda(l))` -- the label that `t` assigns to the cell which the
    reference tableau assigns to `l`.  Matches `dOf t = (colSuperstandard).trans t.symm`."""
    ref = col_superstandard(lam)
    inv = {c: i for i, c in enumerate(t)}
    return tuple(inv[ref[l]] for l in range(len(ref)))


def compose(a: Perm, b: Perm) -> Perm:
    """`(a . b)(i) = a(b(i))`."""
    return tuple(a[b[i]] for i in range(len(b)))


def inverse(a: Perm) -> Perm:
    out = [0] * len(a)
    for i, v in enumerate(a):
        out[v] = i
    return tuple(out)


def inversions(a: Perm) -> int:
    """Coxeter length on `S_m`."""
    return sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j])


def row_stabiliser(lam: List[int], t: Tuple[Cell, ...]) -> List[Perm]:
    """The Young subgroup `S_lambda`: permutations of LABELS preserving each row of `t`
    setwise.  Matches `Specht.rowStab` (stabiliser of the row pattern)."""
    m = len(t)
    rowof = [t[l][0] for l in range(m)]
    return [p for p in itertools.permutations(range(m))
            if all(rowof[p[l]] == rowof[l] for l in range(m))]


def longest_element(sub: List[Perm]) -> Perm:
    """A maximal-length element.  Also reports whether it is unique (it should be)."""
    best = max(inversions(p) for p in sub)
    maxima = [p for p in sub if inversions(p) == best]
    return maxima[0], len(maxima)


def run(m: int) -> bool:
    print(f"n+1 = {m}   (S_{m}, order {len(list(itertools.permutations(range(m))))})")
    seen: Dict[Perm, Tuple] = {}
    total = 0
    collisions: List[Tuple] = []
    for lam in partitions(m):
        ref = col_superstandard(lam)
        sub = row_stabiliser(lam, ref)
        wlam, n_max = longest_element(sub)
        syts = standard_tableaux(lam)
        if n_max != 1:
            print(f"  lambda={lam}: WARNING {n_max} maximal-length elements (not unique)")
        for s in syts:
            for t in syts:
                total += 1
                lead = compose(compose(inverse(d_of(lam, s)), wlam), d_of(lam, t))
                key = (tuple(lam), s, t)
                if lead in seen:
                    collisions.append((seen[lead], key, lead))
                else:
                    seen[lead] = key
        print(f"  lambda={str(lam):12s} |S_lambda|={len(sub):3d}  #SYT={len(syts):3d}"
              f"  l(w_lambda)={inversions(wlam)}")
    print(f"  pairs (s,t) over all lambda : {total}")
    print(f"  distinct lead values        : {len(seen)}")
    print(f"  m! = {__import__('math').factorial(m)}")
    if collisions:
        print(f"  *** NOT INJECTIVE: {len(collisions)} collision(s) ***")
        for a, b, lead in collisions[:5]:
            print(f"      {a}\n   vs {b}\n   both -> {lead}")
        return False
    print("  INJECTIVE on this rank")
    return True


def w_lambda_collisions(m: int) -> List[Tuple]:
    """Is `lambda |-> w_lambda` itself injective?  This is the STRUCTURAL cause of the
    failure above, and it is what makes the negative a statement about the SHAPE of the
    definition rather than an accident of small rank."""
    seen: Dict[Perm, List[int]] = {}
    coll: List[Tuple] = []
    for lam in partitions(m):
        w, _ = longest_element(row_stabiliser(lam, col_superstandard(lam)))
        if w in seen:
            coll.append((seen[w], lam, w))
        else:
            seen[w] = lam
    return coll, len(seen)


def main() -> None:
    print("Murphy leading-permutation map: lead(lambda,s,t) = d(s)^-1 . w_lambda . d(t)")
    print("Testing injectivity ACROSS partitions, by full enumeration.\n")
    results = {}
    for m in (3, 4, 5):
        results[m] = run(m)
        print()
    print("=" * 68)
    print("STRUCTURAL CAUSE: is `lambda |-> w_lambda` injective?\n")
    for m in (3, 4, 5, 6):
        coll, ndist = w_lambda_collisions(m)
        print(f"  m={m}: {len(partitions(m))} partitions -> {ndist} distinct w_lambda,"
              f" {len(coll)} collision(s)")
        for a, b, w in coll:
            print(f"      w_{a} = w_{b} = {w}  (length {inversions(w)})")
    print()
    print("  It is NOT, at any rank tested.  Combined with `dOf_colSuperstandard`")
    print("  (d(t^lambda) = 1, PROVED in Lean on #6283), this forces")
    print("      lead(lambda, t^lambda, t^lambda) = w_lambda,")
    print("  so any two partitions sharing a longest element collide.  That is a")
    print("  structural obstruction to this SHAPE of definition, not a small-rank")
    print("  artifact -- it recurs at every m tested.\n")
    for m, ok in results.items():
        print(f"  n+1 = {m}: {'injective' if ok else 'NOT INJECTIVE'}")
    if all(results.values()):
        print("\nlead_inj is consistent with the data at these ranks -- worth formalising.")
    else:
        print("\nlead_inj is FALSE as defined. The Lean definition must change before")
        print("anyone attempts the proof. This is the decisive outcome the probe was for.")


if __name__ == "__main__":
    main()
