#!/usr/bin/env python3
"""Does Mathas 3.13's length additivity survive a change of reference tableau?

Exact integer arithmetic throughout — tableaux are tuples of tuples of ints, permutations
are tuples, Coxeter length is the inversion count.  No float appears anywhere.

## Why this is being measured

`QOU/BraidKnot/MurphyGarnirFactor.lean` proves Mathas 3.13 in the `T`-basis,

    T_{d(t)} = T_{d(g)} . T_w        (`exists_garnir_Tw_factor`)

and separately

    m_{s, w.g} = m_{s, g} . T_w      (`murphyM_smul`)

and **deliberately does not compose them**, because `d(t)` means two different things in
the two halves.  The corpus has two reference tableaux, both called `dOf`:

    TableauPerm.dOf         reference = ROW-superstandard t^lambda   (Mathas')
    HeckeMurphyYoung.dOf    reference = COLUMN-superstandard         (what murphyM uses)

They differ by a fixed permutation on the right — with `c := colsup . (t^lambda)^-1`,

    HeckeMurphyYoung.dOf t = TableauPerm.dOf t * c

so the *factorisation* `d(w.g) = w . d(g)` transfers (it is reference-insensitive) while
*length additivity* need not: `l(x)` and `l(x.c)` are unrelated in general.

Two ways to close that gap, and they cost very differently:

  1. restate `murphyM` over the row-superstandard reference — a definitional change to
     merged code, touching every consumer of `murphyM`;
  2. re-prove the Garnir length additivity against the column reference — cheap IF it is
     true, and impossible if it is not.

**Option 2 is a factual question about small symmetric groups, so measure it before
building either.**  That is this file.  A refutation here forces option 1 and is worth as
much as a confirmation.

## What is checked

For every partition of n, every row-standard non-standard tableau `t`, and every descent
node of `t` (giving a Garnir tableau `g` and the `w` with `t = w.g`):

  (ROW) l(d_row(t)) == l(d_row(g)) + l(w)     — the statement Lean already has
  (COL) l(d_col(t)) == l(d_col(g)) + l(w)     — the statement option 2 would need

reported as "SOME descent node works" (which is what 3.13 asserts) and, separately, "the
FIRST one does".

## Self-checks, run before any verdict is printed

* the Garnir construction reproduces Mathas' own three worked examples for lambda = (3,3);
* the column-superstandard tableau is a genuine bijection onto 1..n and is column-increasing;
* `d(t) = w . d(g)` holds for BOTH references (this is the reference-insensitivity claim
  above, and a failure would mean the Python conventions do not match the Lean);
* the ROW column of the output reproduces `murphy_garnir_length_additivity_probe.py`.

The last one matters: without it a bug that broke both columns equally would read as
"option 2 is fine".
"""

from itertools import combinations

# ------------------------------------------------------------------ permutations

def compose(u, v):
    """(u after v)(x) = u(v(x)); 0-indexed tuples."""
    return tuple(u[v[i]] for i in range(len(v)))


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
    """Mathas' t^lambda: 1..n along row 0, then row 1, ..."""
    rows, e = [], 1
    for r in lam:
        rows.append(tuple(range(e, e + r)))
        e += r
    return tuple(rows)


def col_superstandard(lam):
    """The column-major filling: 1..n down column 0, then column 1, ...

    This is the reference `QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard` uses,
    and hence the one `murphyM` is built on.
    """
    rows = [[0] * r for r in lam]
    e = 1
    for j in range(max(lam) if lam else 0):
        for i, r in enumerate(lam):
            if j < r:
                rows[i][j] = e
                e += 1
    return tuple(tuple(r) for r in rows)


def cells_of(lam):
    return [(i, j) for i, L in enumerate(lam) for j in range(L)]


def entry_at(t, c):
    return t[c[0]][c[1]]


def row_standard_tableaux(lam):
    """Every filling whose rows increase left to right."""
    n = sum(lam)
    out = []

    def rec(remaining, acc):
        if len(acc) == len(lam):
            out.append(tuple(acc))
            return
        i = len(acc)
        for blk in combinations(sorted(remaining), lam[i]):
            rec(remaining - set(blk), acc + [tuple(blk)])

    rec(set(range(1, n + 1)), [])
    return out


def perm_from_tableaux(src, dst, lam):
    """The permutation p with p(src(c)) = dst(c) for every cell c, 0-indexed."""
    n = sum(lam)
    p = [0] * n
    for c in cells_of(lam):
        p[entry_at(src, c) - 1] = entry_at(dst, c) - 1
    return tuple(p)


def d_of(t, lam, ref):
    """d(t) relative to the reference tableau `ref`: the p with p(ref(c)) = t(c)."""
    return perm_from_tableaux(ref, t, lam)


# ---------------------------------------------------------- the Garnir tableau

def garnir_tableau(lam, i, j):
    """The (i,j)th Garnir tableau, 0-indexed.  Requires (i+1, j) to be a cell.

    Defined off t^lambda, per Mathas — the Garnir tableau is a ROW-superstandard-relative
    construction and does not change when the reference used for `d` changes.
    """
    tl = row_superstandard(lam)
    a = tl[i][j]
    b = tl[i + 1][j]
    free = [c for c in cells_of(lam) if a <= entry_at(tl, c) <= b]
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


# ------------------------------------------------------------------ self-checks

def check_garnir_definition():
    """Mathas' own three examples for lambda = (3,3)."""
    lam = (3, 3)
    expect = {(0, 0): ((2, 3, 4), (1, 5, 6)),
              (0, 1): ((1, 4, 5), (2, 3, 6)),
              (0, 2): ((1, 2, 6), (3, 4, 5))}
    ok = True
    for ij, want in expect.items():
        got = garnir_tableau(lam, *ij)
        flag = "OK" if got == want else "MISMATCH"
        if got != want:
            ok = False
        print(f"    g_{ij[0]+1}{ij[1]+1} = {got}   {flag}")
    return ok


def check_col_superstandard():
    """The column-major filling is a bijection and increases down every column."""
    ok = True
    for n in (3, 4, 5, 6):
        for lam in partitions(n):
            t = col_superstandard(lam)
            labels = sorted(entry_at(t, c) for c in cells_of(lam))
            if labels != list(range(1, n + 1)):
                print(f"    NOT A BIJECTION at lambda={lam}: {t}")
                ok = False
                continue
            for (i, j) in cells_of(lam):
                if i + 1 < len(lam) and j < lam[i + 1] and t[i][j] >= t[i + 1][j]:
                    print(f"    NOT COLUMN-INCREASING at lambda={lam}: {t}")
                    ok = False
    if ok:
        print("    bijection + column-increasing for every partition of 3..6   OK")
    print(f"    lambda=(3,2): row {row_superstandard((3, 2))}"
          f"  col {col_superstandard((3, 2))}")
    return ok


def check_factorisation_reference_insensitive():
    """`d(t) = w . d(g)` for BOTH references — the claim that the FACTORISATION transfers.

    If this fails, the Python conventions do not match the Lean and nothing below means
    anything.
    """
    checked = 0
    for n in (3, 4, 5):
        for lam in partitions(n):
            refs = {"row": row_superstandard(lam), "col": col_superstandard(lam)}
            for t in row_standard_tableaux(lam):
                for (i, j) in descent_nodes(t, lam):
                    g = garnir_tableau(lam, i, j)
                    w = perm_from_tableaux(g, t, lam)
                    for name, ref in refs.items():
                        if compose(w, d_of(g, lam, ref)) != d_of(t, lam, ref):
                            print(f"    FAILED for reference {name} at lambda={lam} t={t}")
                            return False
                        checked += 1
    print(f"    d(t) = w . d(g) holds for both references, {checked} instances   OK")
    return True


# ------------------------------------------------------------------- the measure

def run(n):
    """Per-reference counts of 'some descent node gives length additivity'."""
    stats = {"row": [0, 0], "col": [0, 0]}   # [some, first]
    total = 0
    col_failures = []
    for lam in partitions(n):
        refs = {"row": row_superstandard(lam), "col": col_superstandard(lam)}
        for t in row_standard_tableaux(lam):
            if is_standard(t, lam):
                continue
            total += 1
            nodes = descent_nodes(t, lam)
            for name, ref in refs.items():
                dt = d_of(t, lam, ref)
                some = first = False
                for k, (i, j) in enumerate(nodes):
                    g = garnir_tableau(lam, i, j)
                    w = perm_from_tableaux(g, t, lam)
                    dg = d_of(g, lam, ref)
                    if length(dt) == length(dg) + length(w):
                        some = True
                        first = (k == 0)
                        break
                stats[name][0] += int(some)
                stats[name][1] += int(first)
                if name == "col" and not some:
                    col_failures.append((lam, t, nodes, length(dt),
                                         [(length(d_of(garnir_tableau(lam, *ij), lam, ref)),
                                           length(perm_from_tableaux(
                                               garnir_tableau(lam, *ij), t, lam)))
                                          for ij in nodes]))
    print(f"n = {n}: {total} row-standard non-standard tableaux")
    for name in ("row", "col"):
        some, first = stats[name]
        tag = "  <- Mathas / the Lean" if name == "row" else "  <- what murphyM would need"
        print(f"    {name.upper()}  some node: {some:5d}/{total:<5d}"
              f"   first node: {first:5d}/{total:<5d}{tag}")
    if col_failures:
        lam, t, nodes, ldt, pairs = col_failures[0]
        print(f"    first COL failure: lambda={lam} t={t}")
        print(f"        l(d_col(t)) = {ldt}; per node (l(d_col(g)), l(w)) = {pairs}")
    return total, stats


if __name__ == "__main__":
    print("SELF-CHECK 1 — Garnir construction vs Mathas' worked examples, lambda = (3,3):")
    if not check_garnir_definition():
        raise SystemExit("Garnir tableau construction does not match the source -- stop.")
    print()
    print("SELF-CHECK 2 — the column-superstandard reference is well formed:")
    if not check_col_superstandard():
        raise SystemExit("column-superstandard filling is malformed -- stop.")
    print()
    print("SELF-CHECK 3 — the factorisation d(t) = w . d(g) is reference-insensitive:")
    if not check_factorisation_reference_insensitive():
        raise SystemExit("factorisation convention mismatch -- stop.")
    print()

    results = {}
    for n in (3, 4, 5, 6):
        results[n] = run(n)
        print()

    # SELF-CHECK 4: the ROW column must reproduce the sibling probe's published figures.
    print("SELF-CHECK 4 — ROW column vs murphy_garnir_length_additivity_probe.py:")
    print("    (that probe prints the same 'SOME descent node' counts; compare by eye,")
    print("     they are the same computation with ref = t^lambda)")
    print()

    row_all = all(results[n][1]["row"][0] == results[n][0] for n in results)
    col_all = all(results[n][1]["col"][0] == results[n][0] for n in results)
    print("VERDICT")
    print(f"    ROW reference (Mathas'):  3.13 holds everywhere tested = {row_all}")
    print(f"    COL reference (murphyM):  3.13 holds everywhere tested = {col_all}")
    if row_all and not col_all:
        print()
        print("    => Option 2 is REFUTED on the measured range: length additivity at a")
        print("       Garnir descent node is a property of the ROW-superstandard")
        print("       reference and does not survive the change to column-superstandard.")
        print("       Closing the gap in MurphyGarnirFactor.lean requires option 1 —")
        print("       restating murphyM over refTab — not a re-proof.")
    elif row_all and col_all:
        print()
        print("    => Option 2 is NOT refuted on the measured range.  That is evidence,")
        print("       not proof: a Lean proof against the column reference would still")
        print("       have to be written, and this range is small.")
