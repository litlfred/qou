#!/usr/bin/env python3
"""Mathas 3.7 as a RANK-MATRIX statement -- and the converse half stops needing `qou-3k66`.

Exact integer arithmetic throughout.  No float appears anywhere in this file or the module
it imports.

## Why this exists

`dipper_james_forward_step_probe.py` established that Mathas' transposition induction does
not transcribe, and -- from the seven selection rules it measures -- that no rule of the
form *"identify the offending label, move it"* can work: dominance is a global count
comparison, and there are pairs whose only valid step does not move the least misplaced
label at all.  That is an argument for abandoning the transposition induction entirely and
proving 3.7 from COUNT CRITERIA on both sides.

This probe measures that route before anyone builds it, and it turns out to do more than
re-scope the forward half: it makes the CONVERSE half reachable with machinery that already
exists, where it was previously recorded as blocked on bean `qou-3k66` (`BruhatLe ->
ReflLe`).

## The three measurements

Write `rank(u, i, m) = #{x < i : u(x) < m}` for a permutation `u` of `{0..n-1}`, and let
`N_0 < N_1 < ...` be the ROW BOUNDARIES of `lambda` (`N_i = lambda_0 + ... + lambda_i`).

    dominance == boundary_rank
        `s |>= t`  iff  rank(d(s), N_i, m) >= rank(d(t), N_i, m) for every row boundary
        N_i and every m.

        This is an IDENTITY, not a coincidence, and the algebra is worth having in front of
        you before reading the numbers.  `d(t)` sends a reference label to `t`'s label at
        the same cell, and the reference tableau is row-superstandard, so the row of a label
        `y` in `t` is the row of `d(t)^-1(y)` in `t^lambda`, which depends only on which
        block of `lambda` that index falls in.  Hence

            domCount(rowPattern(t), i, m) = #{y < m : row_t(y) <= i}
                                          = #{x < N_i : d(t)(x) < m}
                                          = rank(d(t), N_i, m).

        So the dominance order on tabloids IS a rank comparison on permutations, read only
        at the row boundaries.

    bruhat == full_rank
        `u <= w` in the SUBWORD Bruhat order iff `rank(u, i, m) >= rank(w, i, m)` for EVERY
        `i`, not merely the boundaries.  This is Ehresmann's tableau criterion (Bjorner-
        Brenti Thm 2.1.5).  Measured here rather than assumed, because it is the one
        ingredient of this route that is Mathlib-scale.

    boundary => full
        For the DISTINGUISHED (minimal-length) coset representatives that `d` produces,
        the boundary inequalities already force the full ones.  This is the bridge, and it
        is elementary: a minimal representative is increasing within each block, so its
        rank function is determined by interpolation between block boundaries.

## What the three give, and why the converse half is the news

Composing them:

    FORWARD   s |>= t  ->  boundary rank  ->  [bridge]  full rank  ->  [Ehresmann, HARD
              direction: rank criterion implies subword]  d(s) <= d(t)

    CONVERSE  d(s) <= d(t)  ->  [Ehresmann, EASY direction: a subword can only raise the
              rank function]  full rank  ->  boundary rank, by SPECIALISATION  ->  s |>= t

The converse needs no bridge and no hard direction -- only that a subword of a reduced word
has pointwise-larger rank matrix, which is an induction on deletions from the subword
definition itself.  **It does not need `BruhatLe -> ReflLe` at all.**  The corpus recorded
`bruhatLe_to_dominance` as blocked on bean `qou-3k66`; on this route it is not.

The forward half still needs the hard direction of Ehresmann, so it is re-scoped rather
than unblocked: the tableau-side selection problem is replaced by a named classical theorem
with a known proof, which is a better place to be stuck.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from dipper_james_dominance_is_bruhat_probe import (   # noqa: E402
    bruhat_sub_set,
    d_of,
    dominates,
    partitions,
    row_standard_tableaux,
)


def rank(u, i, m):
    """`#{x < i : u(x) < m}` -- the rank matrix of a 0-indexed permutation tuple."""
    return sum(1 for x in range(i) if u[x] < m)


def row_boundaries(lam):
    """`N_i = lambda_0 + ... + lambda_i`, the cumulative row sizes."""
    out, c = [], 0
    for L in lam:
        c += L
        out.append(c)
    return out


def run(n):
    below = bruhat_sub_set(n)
    tal = {k: [0, 0] for k in ("dominance_eq_boundary", "bruhat_eq_full", "boundary_to_full",
                               "full_to_boundary")}
    for lam in partitions(n):
        rst = row_standard_tableaux(lam)
        N = row_boundaries(lam)
        ds = {t: d_of(t, lam) for t in rst}
        for s in rst:
            for t in rst:
                u, w = ds[s], ds[t]
                dom = dominates(s, t, lam)
                bdry = all(rank(u, i, m) >= rank(w, i, m)
                           for i in N for m in range(n + 1))
                full = all(rank(u, i, m) >= rank(w, i, m)
                           for i in range(n + 1) for m in range(n + 1))
                bru = u in below[w]

                tal["dominance_eq_boundary"][1] += 1
                tal["dominance_eq_boundary"][0] += (dom == bdry)
                tal["bruhat_eq_full"][1] += 1
                tal["bruhat_eq_full"][0] += (bru == full)
                if bdry:
                    tal["boundary_to_full"][1] += 1
                    tal["boundary_to_full"][0] += full
                if full:
                    tal["full_to_boundary"][1] += 1
                    tal["full_to_boundary"][0] += bdry

    print(f"n = {n}")
    for k, (g, tt) in tal.items():
        print(f"    {k:22s} {g:7d}/{tt:<7d} {'ok' if g == tt else '**FAILS**'}")
    return tal


if __name__ == "__main__":
    print("Mathas 3.7 as a rank-matrix statement")
    print()
    tallies = {}
    for n in (3, 4, 5, 6):
        tallies[n] = run(n)
        print()

    bad = sorted({k for t in tallies.values() for k, (g, tot) in t.items() if g != tot})
    print("VERDICT")
    if bad:
        print("    FAILS: " + ", ".join(bad))
        print("    Do not build this route until the failing row is understood.")
    else:
        print("    All four hold on the measured range.  Consequences, in order of value:")
        print()
        print("    1. The CONVERSE half of 3.7 does NOT need bean `qou-3k66`.")
        print("       d(s) <= d(t)  ->  full rank (EASY Ehresmann: a subword can only")
        print("       raise the rank matrix, an induction on deletions)  ->  boundary rank")
        print("       BY SPECIALISATION  ->  s |>= t.  No reflection order anywhere.")
        print()
        print("    2. The FORWARD half is re-scoped, not unblocked: it still needs the")
        print("       HARD direction of Ehresmann (rank criterion implies subword).  But")
        print("       that is a named classical theorem with a known proof, in place of a")
        print("       tableau selection rule that seven attempts failed to find.")
        print()
        print("    3. `dominance == boundary_rank` removes the tableaux from the statement")
        print("       entirely.  Both sides of 3.7 are rank comparisons of the SAME two")
        print("       permutations; the whole content is `read at the row boundaries` vs")
        print("       `read at every index`, reconciled by `d` being a minimal coset")
        print("       representative.  That is the sentence to formalise.")
