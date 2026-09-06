#!/usr/bin/env python3
"""Dipper-James 3.7: is dominance on row-standard tableaux the Bruhat order -- and WHICH one?

Exact integer arithmetic throughout: tableaux are tuples of tuples of ints, permutations are
tuples, lengths are inversion counts.  No float appears anywhere.

## Why measure a lemma the source states

Mathas 3.7 (Dipper-James) reads, in the OCR'd source:

    Let lambda be a composition of n and suppose that s and t are row standard
    lambda-tableaux.  Then  s |> t  if and only if  d(s) |> d(t).

preceded by "The partial order D on S_n is the ubiquitous Bruhat-Chevalley order.  Perhaps
surprisingly, it agrees with the dominance ordering on row standard lambda-tableaux (when
restricted to D_lambda)."

Three reasons not to state it in Lean straight off the page:

1. **The source is OCR.**  `D` and `B` (for the non-strict and strict relations) are the
   glyphs this document renders the two orders as, and the statement's direction and
   strictness are exactly what a Lean statement gets wrong silently.  A finite check is the
   cheapest way to confirm the reading.
2. **THE CORPUS IS ABOUT TO CARRY TWO BRUHAT ORDERS UNDER ONE NAME.**
   `QOU.Machinery.CoxeterBruhat.BruhatLe` is the SUBWORD definition -- `u <= w` iff some
   reduced word for `w` has a subword spelling `u`.  Mathas' is REFLECTION-GENERATED WITH
   LENGTH INCREASE -- `w = v t_1...t_k` with transpositions `t_i` and
   `l(v t_1...t_j) = l(v) + j`.  Their equivalence is a theorem, not an unfolding.  This
   probe evaluates BOTH and reports whether they agree on `S_n`, which settles empirically
   which one 3.7 should be stated against before anyone proves anything.
3. **Which `d`?**  3.7 is stated for a COMPOSITION; this corpus's `TableauPerm.dOf` is on
   partition shapes.  A partition IS a composition, so the partition case is a genuine
   special case -- and it is the one `MurphyInductionMeasure.murphyLex` needs, since that is
   indexed by `PartOf n`.  This probe runs partition shapes, which is the scope the Lean
   statement will have.

## What is checked

For every partition `lambda |- n` (n <= 6) and every ORDERED PAIR (s, t) of row-standard
`lambda`-tableaux:

    dom(s, t)         s dominates t, via the standard column-count criterion on rows
                      -- and note the ORDER REVERSAL: `t^lambda` is dominance-maximal while
                      `d(t^lambda) = 1` is Bruhat-minimal, so `s |>= t` matches
                      `d(s) <= d(t)`, not `d(t) <= d(s)`
    bruhat_sub(u, w)  u <= w in the SUBWORD order
    bruhat_refl(u, w) u <= w in the REFLECTION order (length-increasing transposition chain)

and the two implications of 3.7 are counted separately, so a one-directional failure is
visible rather than averaged away.

## Self-checks, run before any verdict prints

* `d` is a bijection from row-standard tableaux onto a set of permutations of the right size;
* `d(t^lambda) = identity` (the reference tableau maps to `1`);
* dominance is a partial order on the row-standard tableaux of each shape (refl/antisym/trans);
* both Bruhat relations are partial orders on `S_n`, and both have `1` as least element;
* the two Bruhat relations are compared to each other directly, so "they agree" is measured
  rather than assumed.
"""

from itertools import combinations, permutations

# ------------------------------------------------------------------ permutations

def compose(u, v):
    """(u after v)(x) = u(v(x)); 0-indexed tuples."""
    return tuple(u[v[i]] for i in range(len(v)))


def length(w):
    n = len(w)
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])


def transpositions(n):
    """All transpositions of {0..n-1}, as permutation tuples."""
    out = []
    for a, b in combinations(range(n), 2):
        p = list(range(n))
        p[a], p[b] = p[b], p[a]
        out.append(tuple(p))
    return out


def simple_word(w):
    """A reduced word for `w` in the simple transpositions s_i = (i, i+1), as a list of i.

    Bubble-sort: repeatedly apply the simple transposition that removes an inversion.  The
    resulting word is reduced because each step lowers the inversion count by exactly one.
    """
    n = len(w)
    cur = list(w)
    word = []
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if cur[i] > cur[i + 1]:
                cur[i], cur[i + 1] = cur[i + 1], cur[i]
                word.append(i)
                changed = True
                break
    word.reverse()          # we peeled from w down to 1; reverse to spell w from 1
    return word


def word_prod(n, word):
    """Product of the simple transpositions named by `word`, applied left to right."""
    p = tuple(range(n))
    for i in word:
        s = list(range(n))
        s[i], s[i + 1] = s[i + 1], s[i]
        p = compose(p, tuple(s))
    return p


# ---------------------------------------------------- the two Bruhat definitions

def bruhat_sub_set(n):
    """SUBWORD order: u <= w iff SOME reduced word for w has a subword spelling u.

    Computed as a closure: start from every w, and repeatedly delete one letter from a
    reduced word, keeping the product whenever the deletion drops the length by exactly one
    (a shorter product of a subword is automatically reachable, and the standard subword
    property makes "some reduced word" and "every reduced word" agree -- which is itself one
    of the things this file does not assume: see the direct cross-check below).
    """
    perms = list(permutations(range(n)))
    below = {w: {w} for w in perms}
    # order by length so shorter results are already closed when used
    for w in sorted(perms, key=length):
        word = simple_word(w)
        assert word_prod(n, word) == w, "reduced word does not multiply back"
        assert len(word) == length(w), "word is not reduced"
        for k in range(len(word)):
            sub = word[:k] + word[k + 1:]
            u = word_prod(n, sub)
            if length(u) < length(w):
                below[w] |= below[u]
    return below


def bruhat_refl_set(n):
    """REFLECTION order (Mathas'): w >= v iff w = v t_1...t_k with transpositions t_i and
    l(v t_1...t_j) = l(v) + j for every j.  Built as the transitive closure of the covering
    relation "multiply by a transposition, length goes up by at least 1"."""
    perms = list(permutations(range(n)))
    trs = transpositions(n)
    above = {v: {v} for v in perms}
    for v in sorted(perms, key=length, reverse=True):
        for t in trs:
            w = compose(v, t)
            if length(w) > length(v):
                above[v] |= above[w]
    # invert: below[w] = {v : v <= w}
    below = {w: set() for w in perms}
    for v, ws in above.items():
        for w in ws:
            below[w].add(v)
    return below


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
    n = sum(lam)
    out = []

    def rec(remaining, acc):
        if len(acc) == len(lam):
            out.append(tuple(acc))
            return
        for blk in combinations(sorted(remaining), lam[len(acc)]):
            rec(remaining - set(blk), acc + [tuple(blk)])

    rec(set(range(1, n + 1)), [])
    return out


def cells_of(lam):
    return [(i, j) for i, L in enumerate(lam) for j in range(L)]


def d_of(t, lam):
    """Mathas' d(t): the permutation p with p(t^lambda(c)) = t(c) for every cell c."""
    n = sum(lam)
    tl = row_superstandard(lam)
    p = [0] * n
    for (i, j) in cells_of(lam):
        p[tl[i][j] - 1] = t[i][j] - 1
    return tuple(p)


def dominates(s, t, lam):
    """s |>= t : for every row r and every m, |{entries <= m in rows 0..r of s}| >= same for t.

    The standard dominance criterion on row-standard tableaux (equivalently on their
    tabloids, since only the row sets matter).
    """
    n = sum(lam)
    for r in range(len(lam)):
        srows = set().union(*[set(s[i]) for i in range(r + 1)])
        trows = set().union(*[set(t[i]) for i in range(r + 1)])
        for m in range(1, n + 1):
            if sum(1 for x in srows if x <= m) < sum(1 for x in trows if x <= m):
                return False
    return True


# ------------------------------------------------------------------ self-checks

def check_d_and_dominance(n):
    ok = True
    for lam in partitions(n):
        rst = row_standard_tableaux(lam)
        ds = [d_of(t, lam) for t in rst]
        if len(set(ds)) != len(rst):
            print(f"    d NOT INJECTIVE at lambda={lam}")
            ok = False
        if d_of(row_superstandard(lam), lam) != tuple(range(n)):
            print(f"    d(t^lambda) != identity at lambda={lam}")
            ok = False
        for t in rst:
            if not dominates(t, t, lam):
                print(f"    dominance NOT REFLEXIVE at lambda={lam}, t={t}")
                ok = False
        for a in rst:
            for b in rst:
                if a != b and dominates(a, b, lam) and dominates(b, a, lam):
                    print(f"    dominance NOT ANTISYMMETRIC at lambda={lam}: {a} {b}")
                    ok = False
        for a in rst:
            for b in rst:
                if not dominates(a, b, lam):
                    continue
                for c in rst:
                    if dominates(b, c, lam) and not dominates(a, c, lam):
                        print(f"    dominance NOT TRANSITIVE at lambda={lam}")
                        ok = False
    return ok


def check_bruhat(n, below, name):
    ok = True
    perms = list(permutations(range(n)))
    one = tuple(range(n))
    for w in perms:
        if w not in below[w]:
            print(f"    {name} NOT REFLEXIVE at {w}")
            ok = False
        if one not in below[w]:
            print(f"    {name}: identity is not below {w}")
            ok = False
        for u in below[w]:
            if length(u) > length(w):
                print(f"    {name}: {u} <= {w} but is longer")
                ok = False
            if u != w and w in below[u]:
                print(f"    {name} NOT ANTISYMMETRIC: {u} {w}")
                ok = False
        for u in below[w]:
            for v in below[u]:
                if v not in below[w]:
                    print(f"    {name} NOT TRANSITIVE at {w} {u} {v}")
                    ok = False
    return ok


# ------------------------------------------------------------------- the measure

def run(n):
    sub = bruhat_sub_set(n)
    refl = bruhat_refl_set(n)

    same = sum(1 for w in sub if sub[w] == refl[w])
    total_w = len(sub)
    print(f"n = {n}: subword vs reflection Bruhat agree on "
          f"{same}/{total_w} permutations "
          f"{'-- IDENTICAL' if same == total_w else '-- THEY DIFFER'}")

    for name, below in (("subword", sub), ("reflection", refl)):
        fwd = bwd = pairs = 0
        for lam in partitions(n):
            rst = row_standard_tableaux(lam)
            for s in rst:
                for t in rst:
                    pairs += 1
                    dom = dominates(s, t, lam)
                    # ORIENTATION, and it is the whole content of this line.
                    # `t^lambda` is the MAXIMUM for dominance and `d(t^lambda) = 1` is the
                    # MINIMUM for standard Bruhat, so the bijection `d` is order-REVERSING
                    # onto standard Bruhat: `s |>= t` corresponds to `d(s) <= d(t)`.
                    # Equivalently, Mathas' `D` on S_n is standard Bruhat with the order
                    # reversed.  Coding it the other way round makes BOTH implications fail
                    # by IDENTICAL counts -- measured, 30/46, 511/773, 14201/19426,
                    # 565748/708062 -- which is the signature of a flipped relation rather
                    # than of a counterexample, and is how this was caught.
                    bru = d_of(s, lam) in below[d_of(t, lam)]   # d(s) <= d(t), Bruhat
                    fwd += (not dom) or bru          # dom => bruhat
                    bwd += (not bru) or dom          # bruhat => dom
        print(f"    {name:10s}  s |>= t  =>  d(s) <= d(t) : {fwd:6d}/{pairs:<6d}"
              f"   converse: {bwd:6d}/{pairs:<6d}"
              f"   {'BOTH HOLD' if fwd == pairs == bwd else 'FAILS'}")
    return sub, refl


if __name__ == "__main__":
    print("SELF-CHECK 1 -- d is injective, d(t^lambda) = 1, dominance is a partial order:")
    for n in (3, 4, 5):
        if not check_d_and_dominance(n):
            raise SystemExit(f"self-check 1 failed at n={n} -- stop.")
    print("    n = 3,4,5 clean")
    print()

    print("SELF-CHECK 2 -- both Bruhat relations are partial orders with least element 1:")
    for n in (3, 4):
        s_, r_ = bruhat_sub_set(n), bruhat_refl_set(n)
        if not (check_bruhat(n, s_, "subword") and check_bruhat(n, r_, "reflection")):
            raise SystemExit(f"self-check 2 failed at n={n} -- stop.")
    print("    n = 3,4 clean")
    print()

    results = {}
    for n in (3, 4, 5, 6):
        results[n] = run(n)
        print()

    print("VERDICT")
    print("    Read the two rows per n: if both say BOTH HOLD, Dipper-James 3.7 is confirmed")
    print("    on the measured range for that definition of Bruhat, in BOTH directions.")
    print("    If the agreement line says IDENTICAL, the corpus's subword `BruhatLe` and")
    print("    Mathas' reflection order are the same relation on S_n and the naming")
    print("    collision flagged in CoxeterBruhat.lean is cosmetic rather than semantic --")
    print("    which is still worth a docstring, but not a rename.")
