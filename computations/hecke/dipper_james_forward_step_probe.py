#!/usr/bin/env python3
"""Mathas 3.7 forward half: does the source's INDUCTIVE STEP hold in this encoding?

Exact integer arithmetic throughout -- tableaux are tuples of tuples of ints, permutations
are tuples, lengths are inversion counts, dominance is a count comparison.  No float appears
anywhere in this file or in the module it imports.

## Why this exists, given that the STATEMENT is already measured

`dipper_james_dominance_is_bruhat_probe.py` measured Dipper-James 3.7 itself and found it
holds on every ordered pair of row-standard tableaux of every partition of `n <= 6`
(708062/708062, under both definitions of the Bruhat order).  That is a measurement of the
THEOREM.  A Lean proof follows the PROOF, and the two can come apart -- which is exactly
what this probe finds.

Mathas' argument for `s |>= t  ==>  d(s) <= d(t)`, transcribed from the source
(`library/hecke-alg/sections/sec-000-document.md`, the paragraph after 3.7):

    First suppose that s |> t and choose r minimal such that row r of s and row r of t are
    different.  Let a be the smallest number which is in row r of s but not in row r of t;
    similarly, let b be the smallest number which is in row r of t but not in row r of s.
    Then a < b since s |> t.  Therefore, if v = t(a,b) then v |> t and d(v) |> d(t).
    Further, if a is in row t of t and b is in row s of s then t > r and t >= s; so, either
    v = s or s |> v.  Therefore, by induction, d(s) |>= d(v); so d(s) |>= d(t) as required.

Every clause of that becomes an assertion about this repo's encoding the moment it is
transcribed, and a clause that is false costs a Lean session to discover.

## What is measured, and what the answer is

For every partition `lambda |- n` and every ordered pair `(s, t)` of row-standard
`lambda`-tableaux with `s |> t` strictly, take Mathas' `r`, `a`, `b` and set
`v := t(a,b)` -- read as a TABLOID, i.e. re-sorted within rows, because dominance is a
relation on tabloids and `d` is a bijection from row-standard tableaux onto `S_n`.

    a_lt_b         a < b
    v_dom_t        v |> t, strictly
    bruhat_dv_dt   d(v) <= d(t) in the subword Bruhat order
    raw_rowstd     the RAW swap `t(a,b)` is already row standard, so that
                   `d(v) = (a,b) . d(t)` -- the step this arc recorded as FREE via
                   `TableauPerm.dOf_smul` -- is about the same `v`
    one_step       `d(t) . d(v)^-1` is a single transposition and `l(d v) < l(d t)`,
                   i.e. `v` is one LEFT reflection step below `t`
    s_dom_v        s |>= v   <-- THE CLAUSE THAT FAILS

`s_dom_v` is the clause Mathas justifies with "t > r and t >= s; so, either v = s or
s |> v".  It is false on about a fifth of the pairs, and the reason is visible in the
inequality: `t >= s` says `a`'s row in `t` is at or below `b`'s row in `s`, so swapping
sends `b` to a row at or below where `s` puts it -- which is the overshoot, not a bar to it.

`raw_rowstd` / `one_step` fail together and less often: when the raw swap leaves a row
unsorted, `v` as a tabloid is still correct but is no longer `(a,b) . t` as a tableau, so
the single-transposition route to `d(v) |> d(t)` is unavailable for those pairs.  The
relation `d(v) <= d(t)` itself still holds throughout.

## What this does NOT say

It does **not** refute 3.7 -- the statement is measured true, in both directions, on the
same range.  It does not refute Mathas either: the source is OCR, the sentence carrying the
failing clause is exactly the one whose two row indices are printed as `s` and `t`, the same
glyphs as the two tableaux, so a transcription error in either direction is entirely
possible.  What it establishes is that **the argument as this corpus can read it does not
close**, so a Lean proof must not be written against it.

## The positive half, which is what makes this actionable

`step_exists` measures whether SOME transposition does what Mathas' `(a,b)` was supposed
to: `v = t(a,b)` row standard (raw), `s |>= v |> t`, `d(v) = (a,b) . d(t)`, `l` down.  One
always exists -- 142314/142314 at `n = 6`.  So the STRATEGY is sound and only the SELECTION
RULE is wrong; what a Lean proof needs is a correct rule (or an existence lemma), not a
different induction.

Five candidate rules are measured against the brute-force valid set so the next attempt
does not re-try them.  At `n = 6`, out of 142314 pairs:

    Mathas     102404   71.9%
    lowrow      95044   66.8%   worse
    deep        98448   69.2%   worse
    a_bmin     111474   78.3%   better
    bmax_a     119640   84.1%   best measured, still not a rule

The two `b`-side repairs beat the two `a`-side ones, which is the one structural hint the
search produced: Mathas' `b` -- least in row `r` of `t` but NOT in row `r` of `s` -- is the
wrong constraint.  The brute-force valid set repeatedly wants a `b` that IS in row `r` of
`s`, which Mathas' definition can never return.  No rule tried reaches 100%, and a
per-element "do not overshoot" condition is provably not the criterion: dominance is a
global count comparison, and the valid set contains steps that send a label BELOW the row
`s` puts it in.
"""

import pathlib
import sys
from itertools import combinations

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from dipper_james_dominance_is_bruhat_probe import (   # noqa: E402
    bruhat_sub_set,
    compose,
    d_of,
    dominates,
    length,
    partitions,
    row_standard_tableaux,
)


# ------------------------------------------------------------------ small helpers

def swap_perm(n, i, j):
    """The transposition `(i j)` of `{0..n-1}`, as a permutation tuple."""
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return tuple(p)


def swap_labels(t, a, b):
    """Exchange the LABELS `a` and `b` wherever they sit in `t`.  Rows are NOT re-sorted --
    whether they stay sorted is `raw_rowstd`, one of the things measured."""
    def f(x):
        return b if x == a else (a if x == b else x)
    return tuple(tuple(f(x) for x in row) for row in t)


def rowsort(t):
    """The row-standard representative of a tableau's tabloid."""
    return tuple(tuple(sorted(row)) for row in t)


def is_row_standard(t):
    return all(list(row) == sorted(row) for row in t)


def tabloid(t):
    """Rows as an ORDERED tuple of sets.  Ordered: two tableaux differing by a permutation
    of their rows are different tabloids, and comparing unordered sets here silently
    identifies them (an error this probe made before it was fixed)."""
    return tuple(frozenset(row) for row in t)


def row_of(t, x):
    for i, row in enumerate(t):
        if x in row:
            return i
    raise KeyError(x)


def first_diff_row(s, t):
    """Least `r` whose row SET differs; `None` when `s` and `t` are equal as tabloids."""
    for r in range(len(s)):
        if set(s[r]) != set(t[r]):
            return r
    return None


def inverse(p):
    q = [0] * len(p)
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)


def is_transposition(p):
    return len([i for i, x in enumerate(p) if x != i]) == 2


def mathas_ab(s, t):
    """`a` least in row `r` of `s` but not of `t`; `b` least in row `r` of `t` but not of
    `s`, at the least differing row `r`.  Both sets are nonempty: the rows have equal size
    and differ."""
    r = first_diff_row(s, t)
    return r, min(set(s[r]) - set(t[r])), min(set(t[r]) - set(s[r]))


# ------------------------------------------------- the brute-force "a good step exists"

def valid_pairs(s, t, lam):
    """Every transposition that does what Mathas' `(a,b)` was supposed to do."""
    n = sum(lam)
    out = []
    for a, b in combinations(range(1, n + 1), 2):
        raw = swap_labels(t, a, b)
        if tabloid(raw) == tabloid(t) or not is_row_standard(raw):
            continue
        if not (dominates(raw, t, lam) and dominates(s, raw, lam)):
            continue
        if d_of(raw, lam) != compose(swap_perm(n, a - 1, b - 1), d_of(t, lam)):
            continue
        if not length(d_of(raw, lam)) < length(d_of(t, lam)):
            continue
        out.append((a, b))
    return out


# --------------------------------------------------------------- candidate rules

def rule_mathas(s, t, lam):
    _, a, b = mathas_ab(s, t)
    return a, b


def rule_lowrow(s, t, lam):
    """`a` as Mathas; `b` the entry of row `r` of `t` sitting DEEPEST in `s`, among those
    greater than `a`.  A natural repair: send down whatever `s` puts furthest down."""
    r, a, _ = mathas_ab(s, t)
    cand = [x for x in t[r] if x > a]
    if not cand:
        return a, a
    return a, max(cand, key=lambda x: (row_of(s, x), x))


def rule_deep(s, t, lam):
    """`a` as Mathas; `b` the least entry of row `r` of `t` greater than `a` whose row in
    `s` is at least `a`'s row in `t` -- i.e. an explicit attempt to forbid the overshoot."""
    r, a, _ = mathas_ab(s, t)
    p = row_of(t, a)
    cand = [x for x in t[r] if x > a and row_of(s, x) >= p]
    if cand:
        return a, min(cand)
    cand = [x for x in t[r] if x > a]
    if not cand:
        return a, a
    return a, max(cand, key=lambda x: (row_of(s, x), x))


def rule_bmax_a(s, t, lam):
    """`b` as Mathas; `a` the LARGEST label below `b` sitting in a deeper row of `t`.
    The best of the five measured -- and still not right (84.1% at n = 6)."""
    r, _, b = mathas_ab(s, t)
    cand = [x for x in range(1, b) if row_of(t, x) > r]
    return (max(cand), b) if cand else (b, b)


def rule_a_bmin(s, t, lam):
    """`a` as Mathas; `b` the LEAST label in row `r` of `t` greater than `a` -- note this
    allows `b` to lie in row `r` of `s` as well, which Mathas' `b` never does, and the
    brute-force valid set shows that is sometimes exactly what is required."""
    r, a, _ = mathas_ab(s, t)
    cand = [x for x in t[r] if x > a]
    return (a, min(cand)) if cand else (a, a)


RULES = {"Mathas": rule_mathas, "lowrow": rule_lowrow, "deep": rule_deep,
         "bmax_a": rule_bmax_a, "a_bmin": rule_a_bmin}

CLAUSES = ("a_lt_b", "v_dom_t", "bruhat_dv_dt", "raw_rowstd", "one_step", "s_dom_v")


def run(n, examples=0):
    below = bruhat_sub_set(n)
    tally = {k: [0, 0] for k in CLAUSES}
    tally["step_exists"] = [0, 0]
    rule_hits = {k: 0 for k in RULES}
    shown = 0

    for lam in partitions(n):
        rst = row_standard_tableaux(lam)
        for s in rst:
            for t in rst:
                if s == t or not dominates(s, t, lam):
                    continue
                r, a, b = mathas_ab(s, t)
                raw = swap_labels(t, a, b)
                v = rowsort(raw)
                dv, dt = d_of(v, lam), d_of(t, lam)

                checks = {
                    "a_lt_b": a < b,
                    "v_dom_t": dominates(v, t, lam) and tabloid(v) != tabloid(t),
                    "bruhat_dv_dt": dv in below[dt],
                    "raw_rowstd": raw == v,
                    "one_step": (is_transposition(compose(dt, inverse(dv)))
                                 and length(dv) < length(dt)),
                    "s_dom_v": dominates(s, v, lam),
                }
                for k, ok in checks.items():
                    tally[k][1] += 1
                    tally[k][0] += ok

                vp = valid_pairs(s, t, lam)
                tally["step_exists"][1] += 1
                tally["step_exists"][0] += bool(vp)
                vps = set(vp)
                for k, f in RULES.items():
                    aa, bb = f(s, t, lam)
                    rule_hits[k] += (aa != bb and (aa, bb) in vps)

                if examples and shown < examples and not checks["s_dom_v"]:
                    print(f"    s_dom_v FAILS  lambda={lam}  s={s}  t={t}")
                    print(f"        r={r} a={a} b={b}  v={v}   "
                          f"row_t(a)={row_of(t, a)} row_s(b)={row_of(s, b)}   "
                          f"valid pairs: {sorted(vps)}")
                    shown += 1

    print(f"n = {n}")
    for k in CLAUSES + ("step_exists",):
        good, tot = tally[k]
        pct = f"{100.0 * good / tot:.1f}%" if tot else "-"
        print(f"    {k:14s} {good:7d}/{tot:<7d} {pct:>6s}  "
              f"{'ok' if good == tot else '**FAILS**'}")
    print("    selection rules vs the brute-force valid set:")
    for k in RULES:
        print(f"        {k:8s} {rule_hits[k]:7d}/{tally['step_exists'][1]:<7d}")
    return tally


if __name__ == "__main__":
    print("Mathas 3.7 forward half -- does the SOURCE'S INDUCTIVE STEP hold here?")
    print()
    tallies = {}
    for n in (3, 4, 5, 6):
        tallies[n] = run(n, examples=3 if n == 6 else 0)
        print()

    bad = sorted({k for t in tallies.values() for k, (g, tot) in t.items() if g != tot})
    print("VERDICT")
    if not bad:
        print("    every clause holds on the measured range; the Lean forward proof can")
        print("    follow the source argument as written.")
    else:
        print("    clauses that FAIL: " + ", ".join(bad))
        print()
        print("    `s_dom_v` is the substantive one: Mathas' (a,b) sends `b` PAST the row")
        print("    `s` puts it in, so the step overshoots and the induction hypothesis")
        print("    `s |>= v` is unavailable.  `raw_rowstd` / `one_step` fail together and")
        print("    only cost the single-transposition route to `d(v) |> d(t)`; the relation")
        print("    `d(v) <= d(t)` holds throughout.")
        print()
        print("    `step_exists` is the reason this is a repair and not a refutation: a")
        print("    transposition meeting every one of Mathas' conditions ALWAYS exists.")
        print("    The strategy is sound; the selection rule is not.  The five rules")
        print("    measured above are the ones already tried.  The two b-side repairs")
        print("    beat Mathas' own; the two a-side ones are worse.  None reaches 100%.")
        print()
        print("    3.7 itself is NOT in doubt: the sibling probe measures the statement")
        print("    true in both directions, 708062/708062, on this same range.")
