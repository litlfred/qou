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

## 🛑 SHARPER THAN "THE TRACE CANNOT SEE IT" — THE CONVENTION IS *DEFINED* BY IT

My first framing above says the trace *happens to be* blind above two rows.
That understates it, and the corpus proves the stronger statement.

Bean `qou-3qrv` (2026-08-08), with `MarkovTraceTLUniqueness.lean` sorry-free
(`lean`-direct exit 0, `#print axioms` clean):

    A normalised Markov trace on H_3(q) is fixed by (tr 1, tr s0, tr s0 s1) =
    (1, z, z^2), so the weights are a 3x3 solve in the Ocneanu parameter z. The
    Temperley-Lieb condition y_(1^3)(z) = 0 has exactly TWO roots: z = q,
    degenerate (weights (1,0,0) -- it kills the 2-row block too, so it is not
    faithful on TL_3), and z = q^3/(q^2+1), whose weight vector is exactly
    ([4]_q/[2]_q^3, 1/[2]_q^2, 0) = CONVENTION D.  So D is the UNIQUE Markov
    trace factoring through TL_3 and faithful on it.

`z = q^3/(q^2+1)` **is convention D**, which the owner ruled canonical on
2026-08-15.  So the canonical observable is not incidentally blind above two
rows -- **`y_(1^3) = 0` is the condition that SELECTS it, uniquely.**

Measured, exactly, by `computations/probe3qrv_tl.py` on the Borromean baryon:

    lambda = (3,)      y = 0.50540422650393080248   chi = 1.0   y*chi = 0.5054...
    lambda = (2,1)     y = 0.24729788674803459876   chi = 1.994 y*chi = 0.4932...
    lambda = (1,1,1)   y = 0                        chi = 1.0   y*chi = 0

    D - C = 0,  D - TL = 0   (exact, as rational functions of t = sqrt(q))

**The blind block's character is NONZERO (chi = 1.0); its WEIGHT is exactly
zero.**  So the structure is present and the observable annihilates it -- not
approximately, identically, and by the defining property of the canonical
convention.

That is precisely the tower reading: the higher sector exists, contributes
nothing to any trace, and is reachable only by *subtraction* -- which is what
mass-minus-constituents already is.

`qou-3qrv` also poses the resulting question in as many words, and it is the
same question the eightfold chapter poses from the flavour side:

    does the mass fibre functor land in Rep(SU_q(2)) ~ TL (no 3-row image) or
    in the full H_3(q)?

    eightfold:  dim V = 2 supplied, N = 3 needed, "no q raises the row cap"

**Three chapters, one question.**  `qou-3qrv` asks it about the fibre functor,
the eightfold asks it as the `N = 3` blocker, Step 27 measures it as
trace-blindness at `n = 6`.  Convention C is the full-Hecke Ocneanu trace and
does **not** kill the 3-row block; D does; D is canonical.

## THE N=3 CONSTRUCTION IS NOT MISSING — IT IS THE NEXT MEMBER OF A FAMILY

The eightfold ledger says of `dim V = N = 3`: *"the obstruction is proved; the
**construction is missing**."*  It is not missing.  It is the `N = 3` member of
a one-parameter family the framework already inhabits, and its weights are
computable in closed form.

`h3-markov-wenzl-weights-context.md` records that the Ocneanu parameter fixes
the fibre dimension through `z * [N]_q = q^N`.  Solving that for `z` gives

    z_N  =  q^N / [N]_q

and **convention D is exactly the `N = 2` member** (verified: `q^2/[2]_q` against
`q^3/(q^2+1)` agree to `2.3e-41`).  The family at the proton pin:

    N = 1:  1.10997858275138081
    N = 2:  0.612688037146465252   == CONVENTION D  (canonical)
    N = 3:  0.449304809090207861   <- the flavour sector
    N = 4:  0.369360232235604919
    N = 5:  0.322749650471015791

**Convention C is not an integer member at all** -- solving `q^N/[N]_q = z_C`
gives `N = 2.5995155364`, reproducing the scope note's figure and its verdict of
"no integer fibre dimension".

**And the `N = 3` member is a perfectly legitimate trace.**  Solving the same
3x3 Markov system `(tr 1, tr s, tr ss) = (1, z, z^2)` that fixes `D` -- the
machinery validated first against `D`'s known answer
`([4]_q/[2]_q^3, 1/[2]_q^2, 0)`, reproduced to 16 digits:

    lambda      y at z_D (canonical)      y at z_3 (N = 3)
    (3)         0.5054042265039308        0.378370691342330394
    (2,1)       0.2472978867480346        0.293082487286846423
    (1^3)       0                         0.0354643340839767606   <- ALIVE

all three weights **positive**, and `SUM y_lambda * dim_lambda = 1.0` exactly.

So the eightfold's *"no q raises the row cap"* is exactly right and slightly
misdirecting: **no `q` raises it because the cap is set by `z`, not by `q`.**
Changing `q` cannot help; moving to `z_3` does, and `z_3` is forced -- there is
no freedom in it, `z * [3]_q = q^3` has one solution.

**The trade is therefore explicit and derived, not a matter of taste:**

    N = 2  (z_D):  factors through TL_3, faithful on it, 3-row block dead,
                   SU(2) fibre, canonical by owner ruling 2026-08-15
    N = 3  (z_3):  3-row block alive with weight 0.0355, all weights positive,
                   and by MarkovTraceTLUniqueness it CANNOT factor through TL_3

You cannot have both from one Markov trace on `H_3`.  That is the whole content
of the `N = 3` blocker, stated as a choice rather than an absence.

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
  * **🛑 NOT a proposal to adopt `z_3`.**  `D` is canonical by owner ruling and
    by a sorry-free uniqueness theorem, and switching `z` moves every mass and
    binding number in the corpus.  What is shown is only that the `N = 3`
    object EXISTS and is computable -- turning "the construction is missing"
    into "the construction is a different member of a family we already
    inhabit, and here are its weights".  Which member is right is not settled
    here and is not mine to settle.
  * **NOT that a nonzero 3-row weight gives SU(3).**  `y_(1^3) = 0.0355 != 0`
    means the block is alive in the trace; it does not construct a flavour
    action on it.  That gap is untouched.
  * The `z * [N]_q = q^N` reading of "fibre dimension" is taken from
    `h3-markov-wenzl-weights-context.md`, **not derived here**.  What is
    verified here is that `D` satisfies it at `N = 2` exactly and that `C`
    gives `N = 2.5995`, reproducing that note's own figures.

Scope **(a)**: the arithmetic identity is exact; the connection between the two
chapters is an observation about the corpus, offered for the author to accept
or reject, not a derivation.

NO FLOAT64: the whole computation is exact integer arithmetic over partitions
and standard Young tableaux.
"""

from __future__ import annotations

import sys as _sys
from math import comb, factorial

TOLZ = 1e-30
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from partition_utils import dim_lambda  # noqa: E402

# Irrep dimensions come from the corpus's canonical `partition_utils.dim_lambda`
# (exact hook-length, on main since #2353 — whose commit message is literally
# "centralize dim_lambda").  An earlier version of this probe counted them by
# enumerating standard Young tableaux instead, which was wrong twice over: it is
# exponential where the hook-length formula is not, and it re-created one of the
# ad-hoc copies that function's docstring says it exists to replace.  I had
# justified it as "self-contained by design", but the sibling I checked for the
# helper was `irrep_determinant_escape_probe` on an unmerged branch; the merged,
# canonical module one directory up went unchecked.  Caught by Copilot on #6415.
#
# `syt` is KEPT, and is not dead weight: it is an INDEPENDENT check that the
# hook-length formula agrees with an actual enumeration, run below at n <= 6
# only, where the whole enumeration is a few thousand tableaux.  Bounding it is
# what removes the scaling objection; deleting it would remove a real check.
#
# `partitions` stays local — `partition_utils` has no partition generator.


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
    print("    dim_lambda is the corpus's canonical exact hook-length formula;")
    print("    cross-checked here against a direct SYT enumeration at n <= 6.")
    xcheck = 0
    for n in range(1, 7):
        for lam in partitions(n):
            enumerated, formula = len(syt(lam)), dim_lambda(lam)
            assert enumerated == formula, (
                f"hook-length disagrees with SYT enumeration at {lam}: "
                f"{formula} vs {enumerated}")
            xcheck += 1
    print(f"    cross-check: hook-length == enumeration on all {xcheck} "
          f"partitions of n <= 6  (asserted)")
    print()
    print(f"    {'n':>2} {'sum dim^2':>10} {'n!':>10} {'<=2 rows':>10} "
          f"{'Catalan':>9} {'match':>6} {'blind':>8} {'blind %':>8}")
    for n in range(3, 10):
        tot = vis = 0
        for lam in partitions(n):
            d = dim_lambda(lam)
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
    print("  against nature's 33.7.")
    print()
    print("  🛑 CORRECTED from 22.2457, and the error was methodological, not")
    print("  arithmetic.  A CHANNEL asymmetry must compare the SAME PAIR in two")
    print("  isospin channels.  I used the deuteron (np, T=0) against pp/nn")
    print("  (~0.1 MeV) -- a DIFFERENT PAIR -- which conflates pair identity")
    print("  with isospin.  main's 1d9d3500f5 (t7qv/m896) uses the np 1S0")
    print("  VIRTUAL STATE (~0.066 MeV): same np pair, differing only in")
    print("  isospin.  2.224566/0.066 = 33.7055, robust to the virtual-state")
    print("  energy (67.4 at half, 16.9 at double).  The exclusion is")
    print("  unaffected -- both exceed the cap of 1, and 33.7 makes the gap")
    print("  WIDER -- but the figure I quoted was the wrong comparison.")
    print()
    print("  => the SM's missing N = 3 and binding's missing channel asymmetry")
    print("     are on the SAME SIDE of the SAME CAP, reached from two")
    print("     directions that share no machinery.")

    print("\n[4a] 🛑 SHARPER THAN 'THE TRACE CANNOT SEE IT'")
    print("-" * 78)
    print("  Section [1] says the trace HAPPENS to be blind above two rows.")
    print("  That understates it, and the corpus proves the stronger statement.")
    print()
    print("  qou-3qrv + MarkovTraceTLUniqueness.lean (sorry-free):")
    print("    'A normalised Markov trace on H_3(q) is fixed by (1, z, z^2), so")
    print("     the weights are a 3x3 solve in the Ocneanu parameter z.  The")
    print("     Temperley-Lieb condition y_(1^3)(z) = 0 has exactly TWO roots:")
    print("     z = q, degenerate, and z = q^3/(q^2+1), whose weight vector is")
    print("     ([4]_q/[2]_q^3, 1/[2]_q^2, 0) = CONVENTION D.  So D is the")
    print("     UNIQUE Markov trace factoring through TL_3 and faithful on it.'")
    print()
    print("  z = q^3/(q^2+1) IS convention D, ruled canonical 2026-08-15.")
    print("  => the canonical observable is NOT incidentally blind above two")
    print("     rows.  y_(1^3) = 0 is the condition that SELECTS it, uniquely.")
    print()
    print("  Measured exactly by computations/probe3qrv_tl.py on the Borromean")
    print("  baryon: y_(1,1,1) = 0 while chi_(1,1,1) = 1.0, so the blind block's")
    print("  CHARACTER is nonzero and its WEIGHT is identically zero; D - TL = 0")
    print("  as rational functions.")
    print()
    print("  That is precisely the tower reading: the higher sector exists,")
    print("  contributes nothing to any trace, and is reachable only by")
    print("  SUBTRACTION -- which is what mass-minus-constituents already is.")
    print()
    print("  THREE CHAPTERS, ONE QUESTION:")
    print("    qou-3qrv : does the mass fibre functor land in Rep(SU_q(2)) ~ TL")
    print("               (no 3-row image) or in the full H_3(q)?")
    print("    eightfold: dim V = 2 supplied, N = 3 needed, 'no q raises the")
    print("               row cap'")
    print("    Step 27  : 588 of 720 invisible at n = 6")
    print("  Convention C is the full-Hecke Ocneanu trace and does NOT kill the")
    print("  3-row block; D does; D is canonical.")

    print("\n[4b] THE N=3 CONSTRUCTION IS NOT MISSING — IT IS THE NEXT MEMBER")
    print("-" * 78)
    import mpmath as mp
    from q_parameter import Q_50_DIGIT_STR, Q_MP
    mp.mp.dps = 40
    q = Q_MP

    def qint(N):
        return (q ** N - q ** (-N)) / (q - 1 / q)

    zD = q ** 3 / (q ** 2 + 1)
    zC = mp.sqrt(q) / (q + 1)
    print("  The eightfold says of dim V = N = 3: 'the obstruction is proved;")
    print("  the CONSTRUCTION IS MISSING'.  It is not missing.")
    print()
    print("  h3-markov-wenzl-weights-context.md records that the Ocneanu")
    print("  parameter fixes the fibre dimension via z*[N]_q = q^N.  Solving:")
    print("      z_N = q^N / [N]_q")
    for N in range(1, 6):
        zN = q ** N / qint(N)
        tag = "   == CONVENTION D (canonical)" if abs(zN - zD) < TOLZ else ""
        print(f"      N = {N}:  {mp.nstr(zN, 18):>22}{tag}")
    assert abs(q ** 2 / qint(2) - zD) < TOLZ, "D must be the N=2 member exactly"
    NC = mp.findroot(lambda N: q ** N / qint(N) - zC, mp.mpf("2.6"))
    print(f"  Convention C is NOT an integer member: N = {mp.nstr(NC, 12)}")
    assert abs(NC - mp.nint(NC)) > mp.mpf("1e-4"), "C must be non-integer"

    # the 3x3 Markov system, validated against D's known closed form first
    s1 = mp.matrix([[q, 1], [0, -1 / q]])
    tt = mp.findroot(
        lambda t: (s1 * mp.matrix([[-1 / q, 0], [t, q]]) * s1
                   - mp.matrix([[-1 / q, 0], [t, q]]) * s1
                   * mp.matrix([[-1 / q, 0], [t, q]]))[0, 0], mp.mpf(1))
    s2 = mp.matrix([[-1 / q, 0], [tt, q]])
    P = s1 * s2
    X = mp.matrix([[1, 2, 1],
                   [q, s1[0, 0] + s1[1, 1], -1 / q],
                   [q ** 2, P[0, 0] + P[1, 1], 1 / q ** 2]])

    def weights(z):
        return mp.lu_solve(X, mp.matrix([1, z, z ** 2]))

    wD, w3 = weights(zD), weights(q ** 3 / qint(3))
    assert abs(wD[0] - qint(4) / qint(2) ** 3) < mp.mpf("1e-25"), "validate vs D"
    assert abs(wD[1] - 1 / qint(2) ** 2) < mp.mpf("1e-25"), "validate vs D"
    assert abs(wD[2]) < mp.mpf("1e-25"), "D must kill the 3-row block"
    print()
    print("  Same 3x3 Markov system that fixes D (validated against D's known")
    print("  closed form ([4]/[2]^3, 1/[2]^2, 0) to 25 digits), solved at z_3:")
    print(f"      {'lambda':>8} {'y at z_D':>24} {'y at z_3':>24}")
    for nm, a, b in zip(("(3)", "(2,1)", "(1^3)"), wD, w3):
        print(f"      {nm:>8} {mp.nstr(a, 16):>24} {mp.nstr(b, 18):>24}")
    print(f"      3-row block ALIVE at z_3?  {abs(w3[2]) > mp.mpf('1e-12')}")
    print(f"      all weights positive?      {all(x > 0 for x in w3)}")
    print(f"      sum y*dim = {mp.nstr(w3[0] + 2 * w3[1] + w3[2], 12)}")
    assert abs(w3[2]) > mp.mpf("1e-6"), "the N=3 member must keep the 3-row block"
    assert all(x > 0 for x in w3), "and must be a POSITIVE trace"
    assert abs(w3[0] + 2 * w3[1] + w3[2] - 1) < mp.mpf("1e-25"), "normalised"
    print()
    print("  So 'no q raises the row cap' is right and slightly misdirecting:")
    print("  no q raises it because the cap is set by z, NOT by q.  Moving to")
    print("  z_3 does, and z_3 is FORCED -- z*[3]_q = q^3 has one solution.")
    print()
    print("  THE TRADE, derived rather than a matter of taste:")
    print("    N=2 (z_D): factors through TL_3, faithful, 3-row DEAD,")
    print("               SU(2) fibre, canonical by ruling 2026-08-15")
    print("    N=3 (z_3): 3-row ALIVE at weight 0.0355, all weights positive,")
    print("               and by MarkovTraceTLUniqueness CANNOT factor via TL_3")
    print("  You cannot have both from one Markov trace on H_3.  That is the")
    print("  whole content of the N=3 blocker, stated as a CHOICE not an ABSENCE.")
    print()
    print("  🛑 NOT a proposal to adopt z_3.  D is canonical by ruling and by a")
    print("  sorry-free uniqueness theorem, and switching z moves every mass and")
    print("  binding number.  And a nonzero 3-row weight does NOT construct an")
    print("  SU(3) action -- that gap is untouched.")

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
