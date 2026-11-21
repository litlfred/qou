#!/usr/bin/env python3
# polynomial_q_not_applicable: integer linking numbers and gcds of the atom
# word's closure. No q, no float, nothing evaluated at q0.
"""
atom_closure_milnor_indeterminacy_probe.py — the Milnor triple-linking route
is obstructed, because the atom closure's PAIRWISE linking does not vanish.

## The route being tested

Route 3 of bean `qou-768r`: the arc's missing binding term is **extensive and
super-pairwise** (`qou-brng`), and Milnor's higher linking numbers are
super-pairwise by construction. The corpus already leans on one instance --
`3He`'s binding link `L6a4` IS the Borromean rings, which is **Brunnian**:
every pairwise linking number vanishes and the triple invariant carries the
whole content. So: does the canonical atom closure behave the same way?

## UPDATE 2026-09-03 — the components are KNOTTED. See
## `total_curvature_is_the_computable_half_probe.py` (bean `qou-m3sh`)

Everything below treats the components as carriers of *linking* only, which
is the Brunnian frame the Borromean comparison invites. They are not unknots.
Deleting all other strands and taking the Jones polynomial of each component
by an exact-integer Kauffman bracket, on BOTH classical branches of the
averaged letters, every multi-strand component is a `(2, odd)`-torus knot:
`T(2,7)` throughout on the `sigma` branch, a mix of `T(2,5)` and `T(2,3)` on
the `sigma^-1` branch, for every isotope tried (`A = 2, 3, 4, 6`). Only the
single 1-strand component is the unknot. So each component carries its own
knot-level content -- non-trivial Jones, bridge number 2 -- before any
linking is counted, and `b(L) >= 2A + 1`. That is a second, independent
reason the Borromean/Brunnian model does not describe this closure, on top
of the non-vanishing pairwise linking measured below. Nothing measured
below changes; `mu`, the path structure and the `Delta` table are all
component-type-blind.

## Measured: no. The closure is not Brunnian, and its linking graph is a PATH

Components are the cycles of the word's permutation; `mu = A + 1` (proved
parity consequence in `QOU/Mass/SLq2LabelParity.lean`). Linking numbers are
half the signed crossings between distinct components.

    nonzero lk pairs = mu - 1 = A,  always the CONSECUTIVE pairs (i, i+1)

so the linking graph is the path `P_mu` -- bounded degree 2, never the
complete graph. Same shape front A found for the inter-nucleon crossing set
(`QOU/MassTheory/BraidPathNotCoordination.lean`), now at the level of linking
rather than of crossings.

**Branch dependence, stated because it matters.** An `averaged` letter is
`sigma_g - (h/2)*1`, the MIDPOINT between `sigma_g` (d=0) and `sigma_g^-1`
(d=-h) -- so its two resolutions are the two crossing SIGNS. Both swap, so
`mu` is branch-independent; `lk` is not. Resolving every averaged letter to
`sigma^-1` gives the uniform `lk(i,i+1) = -2`; resolving to `sigma` gives a
mix of `-1` and `-2`.

## Consequence: SOME triple invariants survive, and their count is the problem

Milnor's `mubar(ijk)` is well defined only modulo

    Delta(ijk) = gcd( lk(ij), lk(jk), lk(ki) ).

`Delta = 0` (Brunnian) makes `mubar` a genuine integer -- which is why the
Borromean case carries information. Measured here, per triple:

  * **triples of MUTUALLY NON-ADJACENT components have `Delta = 0`** -- all
    three pairwise linking numbers vanish, so `mubar` IS a genuine integer.
    On a path these exist as soon as `mu >= 5`, i.e. **`A >= 4`**;
  * triples touching a linked pair have `Delta = 2` (uniform branch, one bit
    of `mubar` survives) or `Delta = 1` (mixed branch, no information).

So the Milnor route looked **not obstructed** -- partially available, starting
exactly at `A = 4`.

**SUPERSEDED 2026-08-31 by `milnor_defined_triples_are_split_probe.py`.** The
`Delta = 0` triples are exactly the mutually non-adjacent ones, and between
non-adjacent components this closure has **zero crossings** -- their strand
blocks are pairwise disjoint intervals with no interacting letter, so each such
triple is a **split** 3-component sublink and its `mubar` is **identically
zero**. Definedness and triviality coincide. Read the "partially available"
conclusion below as refuted: the route is closed, and the Magnus expansion
would return zero on exactly the triples where it is meaningful. What follows
is retained because the indeterminacy split is still correct and is what makes
the collapse legible. For `A <= 3` (`mu <= 4`) a path has no
mutually non-adjacent triple at all, so **no genuine integer `mubar` exists**;
the A=3 mirror pair and the deuteron are outside its reach.

**The problem is the COUNT, not the definition.** Non-adjacent triples on a
path `P_mu` number `C(mu - 2, 3) = C(A - 1, 3)`, growing like `A^3`. Summing a
per-triple contribution over them reproduces exactly the supra-linear scaling
that **C4** of `docs/audits/2026-07-13-atom-knot-rule-a5plus-constraints.md`
already excludes arithmetically, and that `QOU.Mass.CoordinationSaturation`
refutes structurally. So a Milnor-triple extensive term must be supported on a
**bounded-degree** subfamily, not on all defined triples -- and naming that
subfamily without fitting it is the open problem, not computing the invariants.

Scope **(a)**: this closure, this assignment.

## What DOES survive, and is worth the next look

The path structure gives `sum |lk| = 2A` in the uniform branch: **linear in A
with bounded per-component degree**, which is precisely the shape
`QOU.Mass.CoordinationSaturation` demands (saturation forces bounded degree;
the complete graph's `z = A-1` is refuted). So the mutual-linking total has the
right scaling for an extensive term. It supplies no magnitude on its own -- a
scale would have to come from somewhere that is not a fit -- but it is a
derived, non-volume, correctly-scaling candidate, which the volume route is
not.

## An error caught by an impossible number

A first pass resolved `averaged` to the IDENTITY (no crossing) and produced
**half-integer linking numbers** (`-3/2`, totals `7/2`, `11/2`, `21/2`).
Linking numbers of a genuine link are integers -- two closed curves cross an
even number of times -- so the output was impossible and the model was wrong.
Reading `canonical_braid_crossings.py` settled it: `averaged` is
`sigma_g - (h/2)*1`, a mixture of the two crossing SIGNS, not of crossing and
no-crossing. With that fixed every value is integral, which is the check that
the fix was right rather than merely different.
"""
from __future__ import annotations

import sys
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

ISOTOPES = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"),
            (3, 3, "6Li"), (4, 4, "8Be"), (6, 6, "12C")]


def linking(Z: int, N: int, avg_sign: int) -> tuple[int, dict]:
    """Component count and the pairwise linking matrix of the closure, with
    every `averaged` letter resolved to the given crossing sign."""
    A, n = Z + N, 3 * (Z + N)
    word = atom_canonical_crossings(Z, N)
    perm = list(range(n))
    for g, _ in word:
        perm[g], perm[g + 1] = perm[g + 1], perm[g]
    comp: dict[int, int] = {}
    c = 0
    for i in range(n):
        if i not in comp:
            j = i
            while j not in comp:
                comp[j] = c
                j = perm[j]
            c += 1
    twice_lk: dict[tuple[int, int], int] = {}
    pos = list(range(n))
    for g, kind in word:
        a, b = comp[pos[g]], comp[pos[g + 1]]
        sign = 1 if kind == "sigma" else (-1 if kind == "sigma_inv" else avg_sign)
        if a != b:
            k = (min(a, b), max(a, b))
            twice_lk[k] = twice_lk.get(k, 0) + sign
        pos[g], pos[g + 1] = pos[g + 1], pos[g]
    assert all(v % 2 == 0 for v in twice_lk.values()), \
        "signed crossings between two components must be even — model is wrong"
    return c, {k: v // 2 for k, v in twice_lk.items()}


def main() -> int:
    checks: list[tuple[bool, str]] = []
    print("=" * 78)
    print("ATOM CLOSURE — pairwise linking, and Milnor triple indeterminacy")
    print("=" * 78)

    for tag, s in (("averaged -> sigma", 1), ("averaged -> sigma^-1", -1)):
        print(f"\n[{tag}]\n")
        print(f"{'iso':>5} {'A':>3} {'mu':>3} {'nonzero':>8} {'C(mu,2)':>8} "
              f"{'path?':>6} {'sum|lk|':>8} {'Delta set':>12}")
        for Z, N, name in ISOTOPES:
            A = Z + N
            mu, lk = linking(Z, N, s)
            nz = {k: v for k, v in lk.items() if v != 0}
            is_path = (len(nz) == mu - 1
                       and all(j == i + 1 for (i, j) in nz))
            total = sum(abs(v) for v in nz.values())
            # Milnor indeterminacy Delta(ijk) = gcd(lk ij, lk jk, lk ki)
            deltas = set()
            for i in range(mu):
                for j in range(i + 1, mu):
                    for k in range(j + 1, mu):
                        g = 0
                        for p in ((i, j), (j, k), (i, k)):
                            g = gcd(g, abs(lk.get(p, 0)))
                        deltas.add(g)
            print(f"{name:>5} {A:>3} {mu:>3} {len(nz):>8} {mu*(mu-1)//2:>8} "
                  f"{str(is_path):>6} {total:>8} {sorted(deltas)!s:>12}")
            checks.append((mu == A + 1, f"{name}/{tag}: mu = A+1"))
            checks.append((is_path,
                           f"{name}/{tag}: linking graph is the path P_mu"))
            # Delta = 0 <=> a mutually non-adjacent triple exists <=> mu >= 5.
            # A first pass asserted `0 not in deltas` outright; the probe
            # refuted it at A >= 4 and the assertion was wrong, not the datum.
            checks.append(((0 in deltas) == (mu >= 5),
                           f"{name}/{tag}: a genuine-integer mubar exists "
                           f"iff mu >= 5 (i.e. A >= 4)"))
            from math import comb
            checks.append((sum(1 for i in range(mu) for j in range(i+2, mu)
                               for k in range(j+2, mu)) == comb(mu - 2, 3),
                           f"{name}/{tag}: non-adjacent triples number "
                           f"C(mu-2,3) = C(A-1,3), i.e. ~A^3"))
            if s == -1:
                checks.append((total == 2 * A,
                               f"{name}: sum|lk| = 2A in the uniform branch"))
                checks.append((all(v == -2 for v in nz.values()),
                               f"{name}: every bond carries lk = -2"))

    print("\n" + "=" * 78)
    print("Delta = gcd(lk ij, lk jk, lk ki) is the Milnor indeterminacy:")
    print("  Delta = 0  ->  mubar is a genuine integer   (Brunnian; L6a4)")
    print("  Delta = 2  ->  mubar survives as ONE BIT")
    print("  Delta = 1  ->  mubar is defined mod 1: NO information")
    print("Delta = 0 occurs exactly on MUTUALLY NON-ADJACENT triples, which a")
    print("path admits iff mu >= 5 (A >= 4).  They number C(mu-2,3) = C(A-1,3),")
    print("so summing over all of them re-creates the ~A^3 scaling C4 excludes.")
    print("=" * 78)

    failed = [m for ok, m in checks if not ok]
    for ok, m in checks:
        if not ok:
            print(f"  FAIL  {m}")
    print(f"{len(checks) - len(failed)}/{len(checks)} checks passed")
    print("=" * 78)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
