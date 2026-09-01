#!/usr/bin/env python3
"""row_cap_is_one_boundary_probe — the eightfold chapter's N=3 blocker and the
tower's trace-blindness are THE SAME BOUNDARY, stated in two chapters that do
not cite each other.  Both of the framework's largest open problems -- the
Standard-Model flavour sector and the nuclear binding gap -- sit on the same
side of it.

Bean `qou-brng` (binding side) / the eightfold N=3 problem (SM side).  Written
at the owner's direction to ask whether the last day's tower work can chip away
at the Standard-Model derivation, and whether the SM results can help close the
binding gap, keeping the FULL TOWER in view rather than only the observables.

## THE TWO STATEMENTS

**Chapter `eightfold-way`, conditionality ledger** (`eightfold-open-problems.md`):

    dim V = N = 3 for the flavour fundamental | OPEN: framework supplies
    dim V = 2; no q raises the ROW CAP.  The obstruction is proved; the
    construction is missing.

and, sorry-free, `Sym2GateMultiplicity.lean`: no object of the **single-fibre**
category reaches `dim W = 3` through the `Sym^2` gate.  `N = 3` gates every
flavour statement in the chapter.

**`main`'s `qou-cds1` Step 27** (`bfc8da8dd9`, landed 2026-09-01):

    convention D is the SU(2)/Temperley-Lieb trace, so omega_lambda vanishes on
    every partition with MORE THAN TWO ROWS ... 588 of 720 dimensions are
    invisible to the observable, and the binding character is LARGEST in an
    invisible block (chi_(3,2,1) = -9.598 against +0.009 in the visible
    1-dim block).

**Same cap.  `ell(lambda) <= 2` on both sides.**  One chapter reads it as *the
algebra does not supply* a 3-dimensional flavour fundamental; the other
measures it as *the trace cannot see* anything above two rows.  Neither cites
the other.

## THE ARITHMETIC, verified here

The visible dimension is not merely "some of it" -- it is exactly a Catalan
number, and the identity holds at every `n` tested:

    SUM over lambda with ell(lambda) <= 2 of (dim lambda)^2  =  Catalan(n)

    n=4:   14 / 24     41.7 % blind
    n=5:   42 / 120    65.0 %
    n=6:  132 / 720    81.7 %      <- Step 27's 132 and 720, from Wedderburn
    n=7:  429 / 5040   91.5 %
    n=8: 1430 / 40320  96.5 %

Step 27 reached `132 = dim TL_6` from the Temperley-Lieb side; this reaches the
same number from the Wedderburn side by summing squared SYT counts.  Two
independent routes to one boundary.  **The blind fraction grows to 96.5 % by
n = 8**, so the observable is a vanishing corner of the algebra, not most of it.

## WHY THIS MATTERS FOR THE SM DERIVATION

`sm-gauge-truncation` already says, from a proved theorem, exactly where to
look and does not look there:

    By the SU(2)-emergence theorem, the gauge group of tensor automorphisms of a
    SINGLE quantum observable universe fibre is exactly SU(2) ... any
    realisation of the SU(3) and U(1) factors must come from symmetry visible
    only at the GROUPOID level -- multi-strand structure, framing data, and the
    interaction of distinct fibres.

and, of the one derived U(1) datum:

    the Coulomb charge Q = w/2 ... evaluated at THE TOWER'S LOWEST LEVEL.

So the SM derivation is (i) told by its own proved theorem that SU(3) and U(1)
cannot come from one fibre, and (ii) conducted at the tower's lowest level,
where only one fibre is visible.  **The blind sector is the multi-strand
structure that theorem points at, and it is measurably non-empty.**

## WHY IT MATTERS FOR BINDING — the two gaps are in the same place

Step 27 measured the binding character as LARGEST in a blind block
(`chi_(3,2,1) = -9.598` against `+0.009` visible).  And this PR's sibling
probes established that every trace-visible construction has channel asymmetry
exactly 1: single crossing in any representation, any pair exchange at any
separation (band generators are conjugates), any power `sigma_i^k`, and any
far-commuting product.  Nature needs `22.25`.

**So the SM's missing `N = 3` and binding's missing channel asymmetry are on the
same side of the same cap.**  That is a structural statement about where to
look, reached from two directions that share no machinery.

## THE CONVERGENCE THE CORPUS ALREADY HALF-CONTAINS

The corpus-grep turned up work that must be cited before any of the above is
read as new, and it makes the picture *stronger*, not weaker.

`docs/audits/2026-08-02-hypercharge-second-invariant-milnor.md`, with
`QOU/StandardModel/SecondCrossingInvariant.lean` (sorry-free), already
identifies the second crossing invariant and does so by a **degree** argument:

    the canonical baryon is the Borromean link B_3, on which EVERY DEGREE-1
    CROSSING INVARIANT VANISHES (writhe = 0, all pairwise linkings = 0), so Y
    cannot be any degree-1 object; mu-bar_123 = +-1 is the first non-vanishing
    finite-type invariant and equals B.

So on the **SM side** the pairwise/degree-1 layer is *proved exhausted*, and the
answer is the degree-2 Milnor triple linking.

This session's binding-side probes reached the same shape in a different
language.  Every trace-visible construction has channel asymmetry exactly 1 --
single crossing in any representation, **any pair exchange at any separation**
(band generators are conjugates of a crossing), `sigma_i^k` at any power, and
**any far-commuting product** -- while nature needs `22.25`.  The measured
minimum for any spread at all is **three or more crossings on two
non-commuting generators**.

    SM side      (2026-08-02):  degree-1 exhausted; need degree >= 2 (triple linking)
    binding side (today):       pairwise exhausted; need >= 3 crossings, non-commuting

**Two independent routes, sharing no machinery, both concluding that the
pairwise / degree-1 layer is used up.**  That is the substantive answer to
"can the Standard-Model results help close the binding gap": they supply a
*named, derived, sorry-free* degree-2 object -- the Milnor triple linking
`mu-bar_123`, equal to baryon number on the confined triple -- where the binding
side has only established that something of that degree is required.

`AGENTS.md` records the binding arc's open positive target as *"the
linking-vs-self-energy amplitude assignment -- why the binding multiplier is the
mutual (coordination) linking count while the mass multiplier is the self-linking
weight"*.  That is a **linking** question, and the SM side's answer to its own
gap is a **triple-linking** invariant.  Whether the binding asymmetry is carried
by the same `mu-bar_123` is a concrete, testable question grounded in an existing
derived result rather than an invented one.  It is **not** tested here.

## 🛑 WHAT THIS DOES **NOT** ESTABLISH

This is a research direction, not a result, and the distinctions below are the
whole of its honesty:

  * **NOT that an SU(3) action exists on the blind blocks.**  Present is not
    "carries the right action".  Nothing here constructs one.
  * **NOT that `dim V = 3` follows.**  The Schur-Weyl row cap is about which
    `lambda` appear in `V^(x)n` for `dim V = N` -- the `gl_N` partner vanishes
    above `N` rows.  Which `lambda` EXIST in `H_n` is a different statement, and
    it is the one verified here.  The blind blocks are `H_n`-side structure;
    whether they can supply a 3-dimensional `V` is untouched.
  * **The `Sym^2` gate proof stands.**  It is sorry-free and it is about the
    SINGLE fibre.  Nothing here contradicts it -- it is exactly why the search
    has to be multi-strand.
  * **NOT an unblocking of hypercharge.**  Bean `qou-tnho` settled that the `Y`
    programme is blocked upstream on `N = 3`; this relocates where to look and
    does not supply the construction.  The existing candidate second datum
    (`strand-twist-datum`) is honest that it is a FREE LABEL -- "an addition to
    the structure, not a reading of it" -- and this does not change that.
  * **NOT a binding value.**  Nothing wired, nothing fitted.

Scope **(a)**: the arithmetic identity is exact; the connection between the two
chapters is an observation about the corpus, offered for the author to accept
or reject, not a derivation.

NO FLOAT64: the whole computation is exact integer arithmetic over partitions
and standard Young tableaux.
"""

from __future__ import annotations

import sys as _sys
from math import comb, factorial
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

# Self-contained by design: the only sibling with these helpers
# (irrep_determinant_escape_probe) is on an unmerged branch, and a probe should
# not carry a cross-branch import.  Both are ~15 lines of exact integer
# combinatorics.


def partitions(n, maxpart=None):
    """All partitions of n, as weakly decreasing tuples."""
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def syt(shape):
    """All standard Young tableaux of `shape`; len() is dim of the irrep."""
    n = sum(shape)
    out = []

    def rec(pos, rows):
        if pos > n:
            out.append(1)
            return
        for r in range(len(shape)):
            c = rows[r]
            if c >= shape[r]:
                continue
            if r > 0 and rows[r - 1] <= c:
                continue          # column-strict: the cell above must be filled
            rows[r] += 1
            rec(pos + 1, rows)
            rows[r] -= 1

    rec(1, [0] * len(shape))
    return out


def main() -> int:
    print("=" * 78)
    print(" THE ROW CAP IS ONE BOUNDARY — eightfold's N=3 and the tower's")
    print(" trace-blindness are the same cap, in two chapters that do not")
    print(" cite each other")
    print("=" * 78)

    print("\n[1] THE TWO STATEMENTS")
    print("-" * 78)
    print("  eightfold-open-problems.md, conditionality ledger:")
    print("    'dim V = N = 3 for the flavour fundamental | OPEN: framework")
    print("     supplies dim V = 2; no q raises the ROW CAP.'")
    print("    + Sym2GateMultiplicity.lean (sorry-free): no SINGLE-FIBRE object")
    print("      reaches dim W = 3 through the Sym^2 gate.")
    print()
    print("  main's qou-cds1 Step 27 (bfc8da8dd9, landed today):")
    print("    'convention D is the SU(2)/Temperley-Lieb trace, so omega_lambda")
    print("     vanishes on every partition with MORE THAN TWO ROWS ... 588 of")
    print("     720 dimensions are invisible to the observable.'")
    print()
    print("  SAME CAP: ell(lambda) <= 2.  One reads it as the algebra not")
    print("  SUPPLYING a 3-dim flavour fundamental; the other measures it as")
    print("  the trace not SEEING above two rows.  Neither cites the other.")

    print("\n[2] THE ARITHMETIC — visible dimension is EXACTLY Catalan(n)")
    print("-" * 78)
    print(f"    {'n':>2} {'sum dim^2':>10} {'n!':>10} {'<=2 rows':>10} "
          f"{'Catalan':>9} {'match':>6} {'blind':>8} {'blind %':>8}")
    for n in range(3, 10):
        tot = vis = 0
        for lam in partitions(n):
            d = len(syt(lam))
            tot += d * d
            if len(lam) <= 2:
                vis += d * d
        cat = comb(2 * n, n) // (n + 1)
        blind = tot - vis
        print(f"    {n:>2} {tot:>10} {factorial(n):>10} {vis:>10} {cat:>9} "
              f"{str(vis == cat):>6} {blind:>8} {100 * blind / tot:>7.1f}%")
        assert tot == factorial(n), "Wedderburn: sum of squared dims must be n!"
        assert vis == cat, (
            "the <=2-row dimension must be exactly the Catalan number")
    print()
    print("    Step 27 reached 132 = dim TL_6 from the Temperley-Lieb side;")
    print("    this reaches it from the WEDDERBURN side by summing squared SYT")
    print("    counts.  Two independent routes to one boundary.")
    print("    The blind fraction grows to 96.5 % by n = 8 -- the observable is")
    print("    a VANISHING CORNER of the algebra, not most of it.")

    print("\n[3] WHY IT MATTERS FOR THE SM DERIVATION")
    print("-" * 78)
    print("  sm-gauge-truncation already says where to look, from a PROVED")
    print("  theorem, and does not look there:")
    print("    'By the SU(2)-emergence theorem, the gauge group of tensor")
    print("     automorphisms of a SINGLE fibre is exactly SU(2) ... any")
    print("     realisation of the SU(3) and U(1) factors must come from")
    print("     symmetry visible only at the GROUPOID level -- multi-strand")
    print("     structure, framing data, and the interaction of distinct fibres.'")
    print("  and of its one derived U(1) datum:")
    print("    'the Coulomb charge Q = w/2 ... evaluated at THE TOWER'S LOWEST")
    print("     LEVEL.'")
    print()
    print("  So the SM derivation is (i) told by its own proved theorem that")
    print("  SU(3) and U(1) cannot come from one fibre, and (ii) conducted at")
    print("  the tower's lowest level, where only one fibre is visible.")
    print("  The blind sector IS that multi-strand structure, and section [2]")
    print("  shows it is measurably non-empty and dominant.")

    print("\n[4] WHY IT MATTERS FOR BINDING — the two gaps are in one place")
    print("-" * 78)
    print("  Step 27 measured the binding character LARGEST in a blind block:")
    print("    chi_(3,2,1) = -9.598   against   +0.009 in the visible 1-dim block")
    print("  and this session's sibling probes established that EVERY")
    print("  trace-visible construction has channel asymmetry exactly 1:")
    print("    single crossing, any representation, any dimension")
    print("    any pair exchange at any separation (band gens are conjugates)")
    print("    sigma_i^k at any power")
    print("    any far-commuting product sigma_i sigma_j")
    print("  against nature's 22.2457.")
    print()
    print("  => the SM's missing N = 3 and binding's missing channel asymmetry")
    print("     are on the SAME SIDE of the SAME CAP, reached from two")
    print("     directions that share no machinery.")

    print("\n[5] THE CONVERGENCE THE CORPUS ALREADY HALF-CONTAINS")
    print("-" * 78)
    print("  Cited before any of the above is read as new -- and it makes the")
    print("  picture stronger, not weaker.")
    print()
    print("  docs/audits/2026-08-02-hypercharge-second-invariant-milnor.md, with")
    print("  QOU/StandardModel/SecondCrossingInvariant.lean (sorry-free), already")
    print("  identifies the second crossing invariant, by a DEGREE argument:")
    print("    'the canonical baryon is the Borromean link B_3, on which EVERY")
    print("     DEGREE-1 CROSSING INVARIANT VANISHES (writhe = 0, all pairwise")
    print("     linkings = 0), so Y cannot be any degree-1 object; mu-bar_123")
    print("     = +-1 is the first non-vanishing finite-type invariant and")
    print("     equals B.'")
    print()
    print("  This session's binding probes reached the same shape in another")
    print("  language:")
    print()
    print("    SM side      (2026-08-02): degree-1 exhausted;")
    print("                               need degree >= 2 (triple linking)")
    print("    binding side (today):      pairwise exhausted;")
    print("                               need >= 3 crossings, non-commuting")
    print()
    print("  Two independent routes, sharing no machinery, both concluding the")
    print("  pairwise / degree-1 layer is USED UP.  That is the substantive")
    print("  answer to 'can the SM results help close the binding gap': they")
    print("  supply a NAMED, DERIVED, SORRY-FREE degree-2 object -- the Milnor")
    print("  triple linking mu-bar_123, equal to baryon number on the confined")
    print("  triple -- where the binding side has only established that")
    print("  something of that degree is required.")
    print()
    print("  AGENTS.md records the binding arc's open positive target as 'the")
    print("  linking-vs-self-energy amplitude assignment'.  That is a LINKING")
    print("  question, and the SM side's answer to its own gap is a")
    print("  TRIPLE-LINKING invariant.  Whether the binding asymmetry is carried")
    print("  by the same mu-bar_123 is concrete and testable, grounded in an")
    print("  existing derived result rather than an invented one.")
    print("  IT IS NOT TESTED HERE.")

    print("\n[6] 🛑 WHAT THIS DOES NOT ESTABLISH")
    print("-" * 78)
    print("  This is a research DIRECTION, not a result.")
    print("  * NOT that an SU(3) action exists on the blind blocks.  Present is")
    print("    not 'carries the right action'.  Nothing here constructs one.")
    print("  * NOT that dim V = 3 follows.  The Schur-Weyl row cap is about")
    print("    which lambda appear in V^(x)n for dim V = N -- the gl_N partner")
    print("    vanishes above N rows.  Which lambda EXIST in H_n is a different")
    print("    statement, and it is the one verified here.  The blind blocks are")
    print("    H_n-side structure; whether they supply a 3-dim V is untouched.")
    print("  * The Sym^2 gate proof STANDS.  Sorry-free, about the SINGLE fibre,")
    print("    and exactly why the search must be multi-strand.")
    print("  * NOT an unblocking of hypercharge.  Bean qou-tnho settled that the")
    print("    Y programme is blocked upstream on N = 3.  This relocates where")
    print("    to look; it does not supply the construction.  The existing")
    print("    candidate (strand-twist-datum) is honest that it is a FREE LABEL")
    print("    -- 'an addition to the structure, not a reading of it' -- and")
    print("    nothing here changes that.")
    print("  * NOT a binding value.  Nothing wired, nothing fitted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
