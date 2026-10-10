#!/usr/bin/env python3
# polynomial_q_not_applicable: exact integer/set combinatorics on the strand
# path plus exact Fraction arithmetic on the Ursell identity; no symbolic-q
# polynomial output.
"""Route (b) on the extensive term: what does the bond-product family rest on,
and does closing the chain into a cycle escape it?

Measured answers: (1) NOT what I first claimed -- connected-sum
multiplicativity does **not** force the path; (2) closing the chain into a
triangle does **not** flip the sign of `b3`; (3) the target for route (b),
restated normalisation-free.

## What this probe got wrong on its first run, and why that matters

The first version asserted an equivalence -- *single-letter interfaces <=>
every block is an interval* -- and CHECK 4 refuted it on its own first run:
20 counterexamples.  The counterexamples are the interesting object and are
now the content of CHECK 5.  The claim is withdrawn; nothing downstream of it
was written.

## The chain being traced

`string_vs_bond_product_probe.py` established (scope-(b), invariant = bond-
product factorisation) that `Z_S = prod_e f_e` cannot produce the exactly
soluble 1D n-string binding, and left route (b) -- leaving the family --
unexplored.  This probe asks what the family RESTS on.

It rests on connected-sum multiplicativity.  `mass_at_3A_proper.py`
(2026-09-07, bean `qou-m6gp`) states the surviving grounding in one clause:

    "each interface is a single letter, so every atom branch closure is the
     connected sum of its A nucleon pieces (800/800 branches over
     2H/3H/3He/4He decompose into exactly A summands)"

-- and in the same passage records that the OTHER grounding is gone: the
alternating core `(sigma_0 sigma_1^-1)^3` is NOT monotone, so the
monotone => #T(2,k) argument no longer applies.

  REPORTED, NOT FIXED (ask-first rule): `MonotoneWordTraceFactorizes.lean`'s
  docstring still says "the production word is monotone in the sense above".
  Against `mass_at_3A_proper.py`'s measured 2026-09-07 note that the live core
  is NOT monotone, that is stale.  The RESULT survives -- connected sums do
  the work -- but the Lean file's stated reason does not.  Two files on `main`
  give different groundings for the same identity.

## What is measured

1. Contiguous layout: every interface is exactly ONE generator, at `3k+2`
   (CHECK 1-2), and distinct interface generators are three apart, so they
   FAR-COMMUTE -- no ordering of the bonds can put a cross term between them
   (CHECK 3).
2. Interleaved (residue) layout: every interface is THREE generators
   (CHECK 4).  No connected-sum decomposition, so no grounding for
   `Z_S = prod_e f_e` there.
3. **The correction.**  Single-letter interfaces do NOT imply the path
   (CHECK 5).  Exhaustively over every 3-uniform partition:

       A = 3:  3 partitions have all interfaces single-letter;
               1 is the contiguous layout,  2 carry a TRIANGLE
       A = 4: 19 partitions have all interfaces single-letter;
               1 is the contiguous layout, 16 carry a TRIANGLE

   The A = 3 pair are the WRAP-AROUND partitions -- `{0,1,8} {2,3,4} {5,6,7}`
   and `{0,7,8} {1,2,3} {4,5,6}` -- one block straddling the two ends of the
   strand line, quotient the cycle `C_3`.  So connected-sum multiplicativity
   is compatible with a CYCLIC coordination graph; only the gamma-gamma
   interval condition excludes it
   (`gamma_gamma_forces_the_layout_probe.py`, 15/15).
4. **And closing the chain does not help** (CHECK 6-7).  On a triangle all
   three bonds are present, so `g_13 != 0` and
   `phi3 = g12 g13 + g12 g23 + g13 g23 + g12 g13 g23`.  With every bond
   repulsive (`f = mu in (0,1)`, `g = -u`, `u in (0,1)`) that is
   `u12 u13 + u12 u23 + u13 u23 - u12 u13 u23 > 0`, since
   `u12 u13 u23 < u12 u13`.  So `b3 < 0` on the cycle too -- this is the
   corpus's `b3corpus_neg`, reached from the wrap-around layout rather than
   from the bond values.
5. The Ursell target for route (b), exactly, in `Z` units (CHECK 8-9).
6. The sign of the one exact cross term the corpus holds (CHECK 10).

## The target route (b) has to hit

With `phi3 = Z_123 - 1 - g_12 - g_13 - g_23` and no 1-3 bond on a chain
(`g_13 = 0`), `b3 = -phi3` is positive exactly when

    Z_123  <  f_12 + f_23 - 1          (the ADDITIVE value)

and the bond product `Z_123 = f_12 f_23` OVERSHOOTS that by exactly
`g_12 g_23 = |b3|`.  So route (b) needs a three-body correction to `Z_123`
that is NEGATIVE and at least `|b3|` in size: `0.293278112721` for 3H,
`0.190468485549` for 3He (cited from `UrsellPartitionFunctionB3` / bean
`qou-rwhv`, not recomputed here).  That is normalisation-free and in the same
units as `Z`, which the earlier framing of route (b) did not have.

Equivalently, and this is the corpus's own form: the multiplicative aggregator
`W(Z) = 1 - Z` must be replaced by one that is convex through the origin
(`AggregatorConvexity.b3Agg_nonneg_of_convexOn`, bean `qou-82mc`), which gives
`b3 >= 0` with every bond still inside `(0,1)`.  The two statements are the
same escape seen from the partition function and from the aggregator.

The corpus holds ONE exact cross term of the right sign:
`MarkovTraceInterleavedCrossTerm` gives `z(z^2 - h z - 1)` between the
interleaved `g0 g1 g0 g2 g1` and the sequential `g0^2 g1^2 g2`, negative at
both pins (CHECK 10).  NOT claimed to be the needed correction -- it lives on
three ADJACENT generators in `H_4`, and the chain's bond generators are three
apart.  It is evidence the family can be left at all, and it says where:
adjacent, non-commuting interfaces.

## Scope

Scope (b), structural, invariant named: a nucleon block that is a strand
interval meets its neighbour at exactly one edge of the strand path.

NOT claimed: that single-letter interfaces force the path (measured false);
that no correction of the needed size exists; that the cross term above is it;
any value for `b3` under a non-contiguous layout.

Read-only: writes no witness, runs no producer, reads no AME/CODATA/census.
"""
import sys
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:
    from mpmath import mp, mpf
except ImportError:  # pragma: no cover
    print("mpmath required")
    sys.exit(2)

mp.dps = 60

Q_PROTON = "1.109978582751380807592"
Q_MUON = "1.109978595642739046682"


# ---------------------------------------------------------------- layouts

def contiguous_layout(a):
    return tuple(frozenset({3 * k, 3 * k + 1, 3 * k + 2}) for k in range(a))


def residue_layout(a):
    return tuple(frozenset({k, k + a, k + 2 * a}) for k in range(a))


def is_interval(block):
    s = sorted(block)
    return all(y - x == 1 for x, y in zip(s, s[1:]))


def block_of(partition, s):
    for idx, block in enumerate(partition):
        if s in block:
            return idx
    raise KeyError(s)


def interface_generators(partition, n):
    """{(block_j, block_k): [generator indices]} per inter-block path edge.

    Path edge `(s, s+1)` is the crossing `sigma_s`, so the generator index is
    the smaller strand.
    """
    out = {}
    for s in range(n - 1):
        j, k = block_of(partition, s), block_of(partition, s + 1)
        if j != k:
            out.setdefault(frozenset({j, k}), []).append(s)
    return out


def has_triangle(edges, a):
    return any(frozenset({x, y}) in edges and frozenset({y, z}) in edges
               and frozenset({x, z}) in edges
               for x, y, z in combinations(range(a), 3))


def partitions_into_triples(elements):
    elements = tuple(sorted(elements))
    if not elements:
        yield ()
        return
    head, rest = elements[0], elements[1:]
    for pair in combinations(rest, 2):
        block = frozenset((head,) + pair)
        remaining = tuple(e for e in rest if e not in pair)
        for tail in partitions_into_triples(remaining):
            yield (block,) + tail


# ---------------------------------------------------------------- Ursell

def phi3(z123, g12, g13, g23):
    """Third Ursell function from the cluster property, as
    `UrsellPartitionFunctionB3.cluster3` states it."""
    return z123 - 1 - g12 - g13 - g23


# ---------------------------------------------------------------- main

def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    print("=" * 78)
    print("Route (b): what the bond-product family rests on, and the target")
    print("=" * 78)

    # ---- CHECK 1-3: contiguous interfaces
    print("\n[1-3] contiguous layout: one generator per interface, far-commuting")
    ok_single, ok_gens, detail = True, True, []
    for a in (2, 3, 4, 5):
        n = 3 * a
        iface = interface_generators(contiguous_layout(a), n)
        if any(len(v) != 1 for v in iface.values()):
            ok_single = False
        gens = sorted(g for v in iface.values() for g in v)
        if gens != [3 * k + 2 for k in range(a - 1)]:
            ok_gens = False
        detail.append(f"A={a}:{gens}")
    check("every contiguous interface is a SINGLE generator", ok_single, "; ".join(detail))
    check("and it sits at 3k+2", ok_gens)
    far = all(abs(i - j) >= 2
              for a in (3, 4, 5)
              for i, j in combinations([3 * k + 2 for k in range(a - 1)], 2))
    check("distinct interface generators FAR-COMMUTE (|i-j| = 3)", far,
          "so no reordering of the bonds can produce a cross term between them")

    # ---- CHECK 4: residue interfaces
    print("\n[4] interleaved (residue) layout: multi-letter interfaces")
    res_detail, all_multi = [], True
    for a in (3, 4):
        n = 3 * a
        sizes = sorted(len(v) for v in interface_generators(residue_layout(a), n).values())
        res_detail.append(f"A={a}: sizes {sizes}")
        if any(s == 1 for s in sizes):
            all_multi = False
    check("no residue interface is a single letter", all_multi, "; ".join(res_detail))

    # ---- CHECK 5: THE CORRECTION
    print("\n[5] single-letter interfaces do NOT force the path (claim withdrawn)")
    census = {}
    for a in (3, 4):
        n = 3 * a
        single = single_int = single_tri = 0
        examples = []
        for part in partitions_into_triples(range(n)):
            iface = interface_generators(part, n)
            if all(len(v) == 1 for v in iface.values()):
                single += 1
                if all(is_interval(b) for b in part):
                    single_int += 1
                if has_triangle(set(iface), a):
                    single_tri += 1
                    if a == 3:
                        examples.append([sorted(b) for b in part])
        census[a] = (single, single_int, single_tri)
        print(f"    A = {a}: all-single-letter {single}; of which all-interval "
              f"{single_int}; carrying a TRIANGLE {single_tri}")
        if a == 3:
            for e in examples:
                print(f"        wrap-around: {e}")
    check("some all-single-letter partitions are NOT all-interval",
          all(c[0] > c[1] for c in census.values()),
          f"A=3: {census[3][0]} vs {census[3][1]}; A=4: {census[4][0]} vs {census[4][1]}")
    check("and they carry TRIANGLES -- connected sums admit a CYCLIC layout",
          census[3][2] == 2 and census[4][2] == 16,
          "so the bond product's grounding does NOT exclude the 3-cell; "
          "only the gamma-gamma interval condition does")

    # ---- CHECK 6-7: closing the chain does not flip b3
    print("\n[6-7] a triangle with all bonds repulsive still has b3 < 0")
    tri_ok, chain_ok = True, True
    samples = ((1, 2, 1, 3, 2, 5), (2, 5, 7, 9, 1, 4), (9, 10, 1, 7, 5, 6))
    for n1, d1, n2, d2, n3, d3 in samples:
        f12, f23, f13 = F(n1, d1), F(n2, d2), F(n3, d3)
        g12, g23, g13 = f12 - 1, f23 - 1, f13 - 1
        # triangle: Z is the product of all three bonds
        p3 = phi3(f12 * f23 * f13, g12, g13, g23)
        if not p3 > 0:
            tri_ok = False
        # closed form check: phi3 == g12 g13 + g12 g23 + g13 g23 + g12 g13 g23
        if p3 != g12 * g13 + g12 * g23 + g13 * g23 + g12 * g13 * g23:
            tri_ok = False
        # chain: no 1-3 bond, f13 = 1
        if phi3(f12 * f23, g12, 0, g23) != g12 * g23:
            chain_ok = False
    check("triangle: phi3 > 0 hence b3 < 0, for every repulsive bond triple",
          tri_ok, "exact rationals; u12 u13 u23 < u12 u13 does it")
    check("chain: phi3 == g12*g23 exactly (the corpus's b3corpus_chain)", chain_ok)

    # ---- CHECK 8-9: the target
    print("\n[8-9] the Ursell target for route (b), in exact rationals")
    overshoot_ok = True
    for n1, d1, n2, d2 in ((1, 2, 1, 3), (2, 5, 7, 9), (9, 10, 1, 7)):
        f12, f23 = F(n1, d1), F(n2, d2)
        g12, g23 = f12 - 1, f23 - 1
        if f12 * f23 - (f12 + f23 - 1) != g12 * g23:
            overshoot_ok = False
    check("bond product overshoots the additive value by exactly g12*g23 = |b3|",
          overshoot_ok, "exact rationals, three sample bond pairs")
    sign_ok = all((F(a, b) - 1) * (F(c, d) - 1) > 0
                  for a, b, c, d in ((1, 2, 1, 3), (2, 5, 7, 9), (9, 10, 1, 7)))
    check("both bonds repulsive => phi3 > 0 => b3 < 0, always", sign_ok,
          "re-derived from the Ursell identity")

    print("\n    TARGET: Z_123 must fall BELOW the additive value f_12 + f_23 - 1")
    print("            by at least |b3| = 0.293278112721 (3H) / 0.190468485549 (3He)")
    print("            [cited from UrsellPartitionFunctionB3 / qou-rwhv, not recomputed]")
    print("            Equivalently: an aggregator convex through the origin")
    print("            (AggregatorConvexity.b3Agg_nonneg_of_convexOn, bean qou-82mc).")

    # ---- CHECK 10: the cross term's sign
    print("\n[10] the corpus's one exact cross term, at both pins")
    cross_ok = True
    for label, qs in (("proton", Q_PROTON), ("muon", Q_MUON)):
        q = mpf(qs)
        z = q ** 3 / (q ** 2 + 1)
        h = q - 1 / q
        x = z * (z * z - h * z - 1)
        print(f"    {label:7s}: z_D = {mp.nstr(z, 16)}  h^2 = {mp.nstr(h * h, 16)}  "
              f"z(z^2 - hz - 1) = {mp.nstr(x, 16)}")
        if not x < 0:
            cross_ok = False
    check("the interleaved cross term is NEGATIVE at both pins", cross_ok,
          "the direction route (b) needs -- NOT claimed to be the correction")

    print("\n" + "=" * 78)
    print(f"{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    print("=" * 78)
    print("""
VERDICT

**The claim this probe was written to make is false, and CHECK 5 is the
refutation.**  Connected-sum multiplicativity -- single-letter interfaces --
does NOT force the path.  The wrap-around partitions `{0,1,8} {2,3,4}
{5,6,7}` and `{0,7,8} {1,2,3} {4,5,6}` have every interface a single letter
and quotient the CYCLE C_3, a triangle; at A = 4, 16 of the 19 single-letter
partitions carry one.  So the bond product's own grounding is compatible with
a 3-cell.

What forces the path is the gamma-gamma interval condition alone
(`gamma_gamma_forces_the_layout_probe.py`).  One route, not two.

**And closing the chain does not escape anyway.**  On a triangle all three
bonds are present and every one is repulsive, so
`phi3 = u12 u13 + u12 u23 + u13 u23 - u12 u13 u23 > 0` and `b3 < 0` still.
That is the corpus's `b3corpus_neg`, reached here from the LAYOUT rather than
from the bond values -- which is worth having, because the wrap-around
partition is the obvious next thing to try and it is already excluded.

What route (b) actually needs is unchanged and now has a normalisation-free
target: `Z_123` below the additive value `f_12 + f_23 - 1` by at least `|b3|`,
equivalently an aggregator convex through the origin (bean `qou-82mc`).  The
one exact cross term the corpus holds has the right SIGN at both pins; nothing
here claims it has the right size, and it lives on adjacent generators in
`H_4` while the chain's bonds are three apart.
""")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
