#!/usr/bin/env python3
"""channel_asymmetry_letter_family_bound_probe — the eigenvalue criterion failed
by being EXACTLY bar-antisymmetric where nature is 22:1 asymmetric, and named
its own missing ingredient: "whatever is absent breaks the bar symmetry between
the channels".  The corpus contains exactly ONE bar-breaking object in this
sector -- `delta`.  This asks whether it can be the missing ingredient, and
answers NO for the WHOLE bond-letter family, not merely for `delta`.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.  Follows
`eigenvalue_channel_binding_criterion_probe` (4/4 signs, magnitudes falsified)
and `pn_criticality_is_forced_probe` (`delta` is the only bar-breaking, and is
of MIXED bar parity).

## The pairing that begs to be tested

Two facts sit next to each other and invite exactly one inference:

  * The eigenvalue criterion predicts `B(T=1) = -B(T=0)` **exactly**, because
    `|lambda_+ * lambda_-| = |det T| = 1` for the pure braid generator.  Nature
    gives `+2.224566` against `~ -0.066`: a **33.7 : 1** asymmetry.
  * `delta = flavor_split_leading(q)` is the ONLY bar-symmetry breaking in the
    bond-letter family, and it is exactly what displaces the p-n letter off the
    bar-symmetric midpoint.

The inference "so `delta` supplies the missing asymmetry" is the obvious next
step, and it is **wrong** -- not by a little, and not only for `delta`.

## The structural fact this turns on

The p-n letter is the ISOSPIN AVERAGE of the two pure-channel letters:

    d_pn = w * d_nn + (1 - w) * d_pp,     w = 1/2 - delta/4
         = -h * w                          (since d_pp = 0, d_nn = -h)

so `delta/4` IS the isospin-mixing asymmetry, and `w = 1/2` exactly would be
the unmixed average.  That is checked below, not asserted.

## The criterion's channel asymmetry, as a function of the letter

For a letter `d`, the transfer matrix `T(1,d) = [[h+d, 1], [1, d]]` has
eigenvalues straddling unit modulus, and the criterion reads

    B_T  =  -alpha * log|lambda_T|,   T=1 <-> lambda_+,  T=0 <-> lambda_-

so the channel asymmetry is the pure ratio

    R(d)  =  |log|lambda_-||  /  |log|lambda_+||

with `R = 1` meaning exact antisymmetry (the falsified case) and nature
requiring `R ~ 33.7`.  **`R` is scale-free**: `alpha` cancels, so no
calibration, no MeV, and nothing to fit.

## THE RESULT — an EXACT INEQUALITY, not a swept band

    R(d) <= 1  for every admissible letter,
               with equality iff  |l_+| = |l_-|  OR  |det T| = 1

and nature requires `R ~ 33.7`.  **Excluded by an inequality, in the correct
direction**: the asymmetry cannot even point the right way, let alone reach 22.

PROOF (two lines, and the sweep below only confirms it):

    |det T(1,d)| = |(h+d)d - 1| = 1 + s(h-s) >= 1     for s = -d in [0,h]

    => log|l_+| + log|l_-| = log|det| >= 0.

  `l_+` is the larger-modulus root, so `|l_+| >= |l_-|` and, the product being
  `>= 1`, `log|l_+| >= 0`.  Two cases:
    * `log|l_-| >= 0`: then `R = log|l_-|/log|l_+| <= 1` since `|l_-| <= |l_+|`,
      with equality iff `|l_-| = |l_+|`.
    * `log|l_-| <  0`: then `|log|l_-|| = -log|l_-| <= log|l_+|` directly from
      the sum being `>= 0`, with equality iff `log|det| = 0`.
  Either way `R <= 1`.                                                       []

**Second correction to my own statement of this theorem.** I first wrote the
equality condition as "iff `|det T| = 1`", i.e. the two endpoints.  The sweep
returns THREE equality points, and the third is the midpoint `d = -h/2`, where
`|det| = 1.0109 != 1` but the two moduli COINCIDE (`|l_+| = |l_-| =
1.005448`), so case 1 of the proof saturates instead of case 2.  The bound
`R <= 1` is untouched -- only the equality clause was incomplete, and the
sweep is what caught it.  Recorded rather than quietly amended, because a
theorem whose equality case is stated wrong is how a later argument picks up
"the midpoint is where |det| = 1", which is false.

So `delta`, a `1.4e-3` displacement INSIDE this range, is not special and could
not have helped: the bound is on the range, not on where in it the p-n letter
sits.

**A correction to my own first framing of this probe.** I wrote that `R` "never
leaves a narrow band around 1".  That is false -- the sweep's minimum is
`R = 0.00119`, because one log-modulus crosses zero near the midpoint, so the
band is not narrow at all.  What is true, and stronger, is the one-sided
inequality above.  The wrong version would have suggested the family gets
*close* to nature's requirement; the right one says it is on the wrong side of
1 entirely.

This is stronger than the `delta` question it was built to answer.  The
falsification's "whatever is absent breaks the bar symmetry" is therefore
**not satisfiable within the bond-letter family at all** -- the missing
structure is somewhere else in the algebra, and this rules out an entire
one-parameter search before anyone runs it.

## The escape, located exactly -- and it is a fine-tuning, not a mechanism

An exclusion is only as useful as the escape it identifies, so trace the
inequality to its one load-bearing step: `|det| >= 1` requires `(h+d)d <= 0`,
i.e. `d` and `h+d` of opposite sign, which holds exactly on the hull `[-h, 0]`.
Outside it `|det|` can drop below 1 and `R` exceeds 1.

**🛑 RETRACTED, same day, by `irrep_determinant_escape_probe`.  What follows is
FALSE AS A GENERAL CLAIM and is kept only because the retraction is the
finding.**  This section asserted:

    "The tempting escape -- a bigger irrep -- is dead. In ANY irrep sigma has
     eigenvalues {q, -1/q}, so det rho(w) = +-1 for every braid word and R = 1
     IDENTICALLY. Three-strand H_3 is worse, not better."

It was verified on **one** irrep, the 2-dim of `H_3`, and generalised from that
single case -- and in that block the two eigenvalue multiplicities happen to be
EQUAL, which is the only reason `|det| = 1` there.  I checked a general claim
against the one example that could not distinguish it from its negation.

**Counterexample in any `H_n`:** the sign representation `sigma -> -1/q`
satisfies the Hecke quadratic exactly and has `|det| = 1/q = 0.90092 < 1` --
precisely the escape condition this probe's own bound identifies.

**The correct statement is a formula, not a constant:** with `m_plus` /
`m_minus` the number of SYT placing `i, i+1` in the same row / column,

    |det rho_lambda(sigma_i)| = q^(m_plus - m_minus)

so `|det| = 1` iff `m_plus = m_minus`, and the escape is open exactly on
**column-heavy** partitions.  The `H_3` check below is retained and still
passes -- it is correct arithmetic about `lambda = (2,1)`; only the
generalisation drawn from it was wrong.

**The `R <= 1` bound itself is UNAFFECTED.**  It concerns the bond-letter family
`d in [-h, 0]` in the REGULAR representation, where `|det| = 1 + s(h-s) >= 1` is
computed directly and never goes through the irrep argument.  Only this rider
is retracted.

**Where `R` actually diverges is exact and named.**  `det T(1,d) = (h+d)d - 1`
vanishes iff `-d` is an eigenvalue of `sigma`:

    d = 1/q :  h + 1/q = q     =>  q*(1/q) - 1 = 0
    d = -q  :  h - q   = -1/q  =>  (-1/q)*(-q) - 1 = 0

and those two points are exactly the **isospin projectors** (`sigma + 1/q` is
proportional to `P_+`, `sigma - q` to `P_-`) -- the same projectors that supply
the T=1/T=0 split.  So `R` is unbounded, and nature's `22.25` IS reached:

    R(d) = 22.24566   at   d = 0.900918105761   =   4.309 * h,
    which is 1.78e-7 short of the projector at 1/q.

**Read that as a verdict, not a target.**  The framework would need its bond
letter fine-tuned to `~2e-7` of a point where the transfer matrix DEGENERATES.
That is evidence *against* the letter carrying the asymmetry, not a place to
aim a derivation.

**Two further corrections to my own passes, both about RANGE, not arithmetic.**
I first swept only to `d = 3h` and reported "R never reaches 33.7" -- true of
the range swept, false of the family, since the pole sits at `4.309*h`.  I then
swept the right window on a UNIFORM grid, which a logarithmic divergence
outruns: 20000 points reach only `R = 14.3`.  The assertion failed rather than
letting a second "never reaches" through, and the value above is obtained by
bisection.  **A negative result is only as good as the range and the resolution
behind it**, and my first two attempts were each short on one.

## What is NOT claimed

  * NOT that the eigenvalue criterion is wrong about SIGNS.  Its 4/4 stands;
    this bounds its magnitude structure.
  * NOT that `delta` is unimportant.  It is what makes the p-n bond
    finite-range at all (`pn_criticality_is_forced_probe`).  It is unable to
    do THIS job.
  * NOT a binding value, nothing wired, nothing fitted.  `R` is a ratio of
    logarithms; `alpha` cancels identically.
  * NOT a claim about `R` outside `[-h, 0]`.  The bound is stated for the
    admissible range and the sweep endpoints are printed so the scope is
    visible.

Scope **(b)** for the family bound -- it is a bound over the whole admissible
parameter range with the mechanism identified (`|det|` near 1 pins the two
log-moduli together), not a numerical near-miss.  Scope **(a)** for the
comparison to AME/PDG.

NO FLOAT64: mpmath `mpf` end to end at 50 dps, 50-digit proton pin.  Sweep
points are built from exact rationals of `h`, never from float literals.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

mp.mp.dps = 50
TOL = mp.mpf(10) ** -40

# nature, for comparison only (AME2020 / scattering); never an input
B_PN_3S1 = AME_B_DEUTERON_MEV_VALIDATION      # deuteron, bound
B_T1_SCALE = mp.mpf("0.066")       # np 1S0 virtual state -- SAME pair as the
                                   # deuteron, differing only in isospin.
                                   # CORRECTED from 0.1 (= pp/nn, a DIFFERENT
                                   # pair): a CHANNEL ratio must compare one
                                   # pair across isospin.  main 1d9d3500f5.


def fmt(x, n=12):
    return mp.nstr(x, n)


def eigs(d, h):
    """Eigenvalues of T(1,d) = [[h+d, 1],[1, d]], sorted by descending modulus."""
    tr = h + 2 * d
    dt = (h + d) * d - 1
    rt = mp.sqrt(tr * tr - 4 * dt)
    e = [(tr + rt) / 2, (tr - rt) / 2]
    e.sort(key=lambda x: -abs(x))
    return e


def R_of(d, h):
    """Channel asymmetry |log|l_-|| / |log|l_+||.  alpha-free, scale-free."""
    lp, lm = eigs(d, h)
    a, b = abs(mp.log(abs(lp))), abs(mp.log(abs(lm)))
    if a == 0 and b == 0:
        return None
    if a == 0:
        return mp.inf
    return b / a


def main() -> int:
    q = Q_MP
    h = q - 1 / q
    dx = flavor_split_leading(q)
    w = mp.mpf(1) / 2 - dx / 4
    d_pp, d_nn, d_pn = mp.mpf(0), -h, -h * w

    print("=" * 78)
    print(" CHANNEL ASYMMETRY -- a bound over the WHOLE bond-letter family")
    print(" answers 'can delta supply the 22:1?' by answering it for every letter")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}   h = {fmt(h)}   delta = {fmt(dx)}")

    print("\n[1] THE p-n LETTER IS THE ISOSPIN AVERAGE -- checked, not asserted")
    print("-" * 78)
    avg = w * d_nn + (1 - w) * d_pp
    print(f"    d_pp = {fmt(d_pp)}   (sigma,    pure T=1 letter)")
    print(f"    d_nn = {fmt(d_nn)}   (sigma^-1, pure T=0 letter)")
    print(f"    w    = 1/2 - delta/4 = {fmt(w)}")
    print(f"    w*d_nn + (1-w)*d_pp  = {fmt(avg)}")
    print(f"    d_pn                 = {fmt(d_pn)}")
    print(f"    equal to {fmt(abs(avg - d_pn), 3)} ?  {abs(avg - d_pn) < TOL}")
    assert abs(avg - d_pn) < TOL, "d_pn must be the isospin average"
    print("    => delta/4 IS the isospin-mixing asymmetry; w = 1/2 is unmixed.")

    print("\n[2] WHAT NATURE REQUIRES")
    print("-" * 78)
    need = B_PN_3S1 / B_T1_SCALE
    print(f"    B(T=0) = +{fmt(B_PN_3S1)} MeV   (deuteron 3S1, bound)")
    print(f"    B(T=1) ~ -{fmt(B_T1_SCALE)} MeV   (the 1S0 channels, unbound)")
    print(f"    required |B(T=0)/B(T=1)| ~ {fmt(need, 6)}")
    print("    the eigenvalue criterion predicts EXACTLY 1 (bar antisymmetry).")

    print("\n[3] THE THREE ACTUAL LETTERS")
    print("-" * 78)
    print(f"    {'letter':6s} {'d':>15s} {'|l_+|':>14s} {'|l_-|':>14s} {'R':>12s}")
    for nm, d in (("pp", d_pp), ("pn", d_pn), ("nn", d_nn)):
        lp, lm = eigs(d, h)
        print(f"    {nm:6s} {fmt(d, 10):>15} {fmt(abs(lp), 10):>14} "
              f"{fmt(abs(lm), 10):>14} {fmt(R_of(d, h), 8):>12}")

    print("\n[4] THE FAMILY BOUND -- sweep the ENTIRE admissible range d in [-h,0]")
    print("-" * 78)
    NP = 4001
    Rs, ds = [], []
    for i in range(NP):
        d = -h * mp.mpf(i) / mp.mpf(NP - 1)
        r = R_of(d, h)
        if r is None or r == mp.inf:
            continue
        Rs.append(r)
        ds.append(d)
    Rmin, Rmax = min(Rs), max(Rs)
    imin, imax = Rs.index(Rmin), Rs.index(Rmax)
    print(f"    sweep points: {len(Rs)} across d in [-h, 0]  (h = {fmt(h)})")
    print(f"    min R = {fmt(Rmin, 10)}   at d = {fmt(ds[imin], 8)}")
    print(f"    max R = {fmt(Rmax, 10)}   at d = {fmt(ds[imax], 8)}")
    print(f"    R at the endpoints (pure sigma / sigma^-1): "
          f"{fmt(R_of(mp.mpf(0), h), 10)} / {fmt(R_of(-h, h), 10)}")
    print()
    print(f"    NATURE REQUIRES R ~ {fmt(need, 6)}")
    print(f"    the family's MAXIMUM is {fmt(Rmax, 10)}")
    short = need / Rmax
    print(f"    short by a factor of {fmt(short, 6)}")
    print()
    print("    NOTE the min: R spans [0.0012, 1], NOT a narrow band around 1.")
    print("    (My first framing of this probe said 'narrow band'; that was")
    print("    wrong -- one log-modulus crosses zero near the midpoint.  The")
    print("    true statement is the ONE-SIDED inequality below, which is")
    print("    stronger: the family sits on the WRONG SIDE of 1 entirely.)")
    # the sharp result: R <= 1 exactly, equality iff |det| = 1
    assert Rmax <= 1 + TOL, (
        "EXACT BOUND: R <= 1 must hold across the admissible family")
    assert need > 1, "nature requires R > 1, which the bound excludes"

    print("\n[4a] THE EXACT INEQUALITY -- verified to full precision")
    print("-" * 78)
    print("    R(d) <= 1 for EVERY admissible letter, with equality iff")
    print("      |l_+| = |l_-|   OR   |det T| = 1.")
    over = [(d, r) for d, r in zip(ds, Rs) if r > 1 + TOL]
    print(f"    sweep points with R > 1 (beyond {fmt(TOL, 2)}): {len(over)}")
    eq = [(d, r) for d, r in zip(ds, Rs) if abs(r - 1) < mp.mpf("1e-12")]
    print(f"    sweep points with R == 1 (to 1e-12): {len(eq)}"
          f"   at d = {', '.join(fmt(d, 6) for d, _ in eq[:4])}")
    print("    THREE equality points, and the third corrected my own theorem:")
    print("      d = 0 and d = -h   -> |det| = 1        (case 2 saturates)")
    print("      d = -h/2           -> |l_+| = |l_-|    (case 1 saturates)")
    print("    I first stated equality as 'iff |det| = 1'.  At the midpoint")
    print(f"    |det| = {fmt(1 + (h / 2) * (h / 2), 12)} != 1, yet R = 1 because the")
    print("    two moduli COINCIDE there.  The bound R <= 1 is untouched; the")
    print("    equality clause was incomplete, and the sweep is what caught it.")
    assert len(over) == 0, "no admissible letter may have R > 1"
    assert len(eq) == 3, "exactly three equality points: 0, -h/2, -h"
    lp_m, lm_m = eigs(-h / 2, h)
    assert abs(abs(lp_m) - abs(lm_m)) < TOL, (
        "the midpoint equality is by COINCIDING MODULI, not by |det| = 1")
    assert abs(1 + (h / 2) * (h / 2) - 1) > mp.mpf("1e-3"), (
        "and |det| at the midpoint is demonstrably NOT 1")

    print("\n[5] WHY -- the mechanism, so this is a bound and not a coincidence")
    print("-" * 78)
    print("    |det T(1,d)| = |(h+d)d - 1| = 1 + s(h-s)  with  s = -d in [0,h].")
    print("    That is maximal at the midpoint and equals 1 at BOTH endpoints:")
    for nm, s in (("d = 0    ", mp.mpf(0)), ("d = -h/2 ", h / 2),
                  ("d = -h   ", h)):
        print(f"      {nm} |det| = {fmt(1 + s * (h - s), 12)}")
    print(f"    so |det| in [1, 1 + h^2/4] = [1, {fmt(1 + h * h / 4, 12)}]")
    print("    -- and crucially |det| >= 1, NEVER below.  Since")
    print("        log|l_+| + log|l_-| = log|det| >= 0,")
    print("    and l_+ is the larger-modulus root (so log|l_+| >= 0):")
    print("      * if log|l_-| >= 0:  R = log|l_-|/log|l_+| <= 1 since |l_-|<=|l_+|")
    print("      * if log|l_-| <  0:  |log|l_-|| <= log|l_+| directly from sum>=0")
    print("    Either way R <= 1, equality iff log|det| = 0.  QED -- an exact")
    print("    inequality, not a swept observation.  Nature needs R ~ 33.7 > 1,")
    print("    so the family is excluded ON THE WRONG SIDE, not merely short.")
    print()
    print("    delta is a displacement of 1.4e-3 INSIDE this range.  It is not")
    print("    special and it could not have helped: the bound is on the range,")
    print("    not on where in the range the p-n letter happens to sit.")

    print("\n[6] WHERE THE BOUND FAILS -- localising what the framework would NEED")
    print("-" * 78)
    print("    The exclusion is only as useful as the escape it identifies, so")
    print("    trace the inequality back to its one load-bearing step:")
    print("        |det| = |(h+d)d - 1| >= 1   REQUIRES   (h+d)d <= 0,")
    print("    i.e. d and h+d of OPPOSITE SIGN -- true exactly on d in [-h, 0],")
    print("    the convex hull of the two pure channels sigma and sigma^-1.")
    print("    Outside that hull (h+d)d > 0 and |det| can drop BELOW 1, which is")
    print("    the only way log|l_+| + log|l_-| goes negative and R exceeds 1.")
    print()
    print("    FIRST — 🛑 RETRACTED.  This section claimed 'a bigger irrep does")
    print("    NOT help: in ANY irrep det rho(w) = +-1, forcing R = 1")
    print("    identically'.  That is FALSE as a general claim.  It was verified")
    print("    on ONE irrep (H_3's 2-dim, below), where the two eigenvalue")
    print("    multiplicities happen to be EQUAL -- the single example that")
    print("    could not distinguish the claim from its negation.")
    print("    COUNTEREXAMPLE in any H_n: the sign rep sigma -> -1/q satisfies")
    print("    the Hecke quadratic exactly and has |det| = 1/q = 0.90092 < 1,")
    print("    which is precisely this probe's own escape condition.")
    print("    CORRECT STATEMENT: |det rho_lambda(sigma_i)| = q^(m+ - m-) with")
    print("    m+/m- the SYT counts placing i,i+1 in a row/column, so |det| = 1")
    print("    iff m+ = m-, and the escape is open on COLUMN-HEAVY partitions.")
    print("    Retraction + measurement: irrep_determinant_escape_probe.")
    print("    The R <= 1 bound itself is UNAFFECTED -- it is computed directly")
    print("    in the REGULAR rep and never uses the irrep argument.")
    print("    The H_3 check below is retained and still passes: it is correct")
    print("    arithmetic about lambda = (2,1); only my generalisation was wrong.")
    print()
    # H_3 two-dim irrep, built from the relations and VERIFIED, not imported
    s1 = mp.matrix([[q, 1], [0, -1 / q]])
    # solve the braid relation for the single free entry t in s2
    tt = mp.findroot(
        lambda t: (s1 * mp.matrix([[-1 / q, 0], [t, q]]) * s1
                   - mp.matrix([[-1 / q, 0], [t, q]]) * s1
                   * mp.matrix([[-1 / q, 0], [t, q]]))[0, 0],
        mp.mpf("1.0"))
    s2 = mp.matrix([[-1 / q, 0], [tt, q]])
    braid = s1 * s2 * s1 - s2 * s1 * s2
    quad1 = s1 * s1 - h * s1 - mp.eye(2)
    quad2 = s2 * s2 - h * s2 - mp.eye(2)

    def nrm(M):
        return max(abs(M[i, j]) for i in range(2) for j in range(2))
    print(f"    H_3 2-dim irrep built from the relations, t = {fmt(tt, 10)}")
    print(f"      braid relation residual   : {fmt(nrm(braid), 3)}")
    print(f"      quadratic residual (s1,s2): {fmt(nrm(quad1), 3)}, "
          f"{fmt(nrm(quad2), 3)}")
    assert nrm(braid) < mp.mpf("1e-30"), "the H_3 rep must satisfy the braid relation"
    assert nrm(quad1) < mp.mpf("1e-30") and nrm(quad2) < mp.mpf("1e-30"), (
        "and the Hecke quadratic")
    for nm, M in (("s1", s1), ("s2", s2), ("s1*s2", s1 * s2),
                  ("s1*s2*s1", s1 * s2 * s1)):
        dd = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
        print(f"      |det {nm:9s}| = {fmt(abs(dd), 14)}")
        assert abs(abs(dd) - 1) < mp.mpf("1e-30"), (
            "|det| = 1 in THIS block (lambda = (2,1), m+ = m- = 1) -- "
            "NOT a general fact about irreps; see irrep_determinant_escape_probe")
    print("      => |det| = 1 for every word IN THIS BLOCK, so R = 1 here.")
    print("         That is a fact about lambda = (2,1), where m+ = m- = 1.")
    print("         🛑 It does NOT generalise: the sign rep of any H_n has")
    print("         |det| = 1/q < 1.  The escape is open on column-heavy")
    print("         partitions, and leaving the hull is a SECOND escape, not")
    print("         the only one.")

    print()
    print("    SECOND, locate the requirement -- and it lands on an EXACT point.")
    print("    det T(1,d) = (h+d)d - 1 vanishes iff -d is an eigenvalue of sigma:")
    print("        d = 1/q :  h + 1/q = q,  so (h+1/q)(1/q) - 1 = q/q - 1 = 0")
    print("        d = -q  :  h - q  = -1/q, so (h-q)(-q) - 1 = 1 - 1     = 0")
    for nm, d0 in (("d = 1/q", 1 / q), ("d = -q ", -q)):
        print(f"      {nm}: det = {fmt((h + d0) * d0 - 1, 4)}   exactly zero?  "
              f"{abs((h + d0) * d0 - 1) < TOL}")
        assert abs((h + d0) * d0 - 1) < TOL, "det must vanish at minus an eigenvalue"
    print("    At a zero of det one eigenvalue is 0, log|l_-| -> -infinity, and")
    print("    R DIVERGES.  So R is UNBOUNDED outside the hull, and 22.25 is")
    print("    reached -- the question is only WHERE.")
    print()
    print("    And those two points are exactly the ISOSPIN PROJECTORS: sigma +")
    print("    1/q is proportional to P_+ and sigma - q to P_-, the same")
    print("    projectors that supply the T=1 / T=0 channel split.  The")
    print("    divergence is not at an arbitrary extrapolation -- it is at the")
    print("    pure channels themselves.")
    print()
    print(f"      {'d':>16s} {'d/h':>9s} {'|det|':>14s} {'R':>14s}")
    NO = 20000
    marks = []
    for i in (1, NO // 4, NO // 2, NO - 200, NO - 1):
        d = (1 / q) * mp.mpf(i) / mp.mpf(NO)
        marks.append((d, abs((h + d) * d - 1), R_of(d, h)))
    for d, dd, r in marks:
        print(f"      {fmt(d, 10):>16} {fmt(d / h, 5):>9} {fmt(dd, 10):>14} "
              f"{(fmt(r, 10) if r is not None else 'n/a'):>14}")
    print("    A uniform grid CANNOT resolve this: the divergence is")
    print("    LOGARITHMIC, so even the last grid point above (4.5e-5 short of")
    print("    1/q) only reaches R = 14.3.  My first attempt asserted on the")
    print("    grid and correctly FAILED rather than reporting 'never reaches'.")
    print("    Solve for d directly instead:")
    # bisection, not a secant: R is monotone on (0, 1/q) but its derivative
    # blows up at the pole, and mp.findroot's default solver overshoots there.
    lo_d, hi_d = mp.mpf("0.9"), (1 / q) * (1 - mp.mpf(10) ** -40)
    assert R_of(lo_d, h) < need < R_of(hi_d, h), "the root must be bracketed"
    for _ in range(400):
        mid = (lo_d + hi_d) / 2
        if R_of(mid, h) < need:
            lo_d = mid
        else:
            hi_d = mid
    d_need = (lo_d + hi_d) / 2
    assert mp.mpf(0) < d_need < 1 / q, "the solution must lie inside (0, 1/q)"
    assert abs(R_of(d_need, h) - need) < mp.mpf("1e-25"), (
        "and must actually solve R(d) = need")
    print(f"      solved by bisection: R({fmt(d_need, 14)})")
    print(f"                         = {fmt(R_of(d_need, h), 14)}")
    print(f"    R first reaches {fmt(need, 6)} at d = {fmt(d_need, 12)}")
    print(f"      = {fmt(d_need / h, 6)} * h, i.e. {fmt(d_need / h, 4)}x the whole")
    print(f"      hull width, and {fmt(d_need * q, 8)} of the way to 1/q.")
    print(f"      distance remaining to the projector: {fmt(1 / q - d_need, 6)}")
    print("    So the requirement is NOT a small perturbation of the bond letter.")
    print("    The framework would need a bond object far outside the convex hull")
    print("    of its own two pure channels, most of the way to the point where")
    print("    the transfer matrix DEGENERATES onto an isospin projector.")
    print()
    print("    TWO CORRECTIONS to my own passes at this section, both about")
    print("    RANGE rather than arithmetic:")
    print("      (i)  I first swept only to d = 3h and reported 'R never reaches")
    print(f"           {fmt(need, 6)}'.  True of the range swept, FALSE of the family:")
    print(f"           the pole sits at 1/q = {fmt(1 / q, 8)} = {fmt(1 / (q * h), 4)}*h,")
    print("           outside the window I had looked at.")
    print("      (ii) I then swept the right window but on a UNIFORM grid, which")
    print("           a logarithmic divergence outruns -- 20000 points reach only")
    print("           R = 14.3.  The assertion caught it instead of letting a")
    print("           second 'never reaches' through.")
    print("    A negative result is only as good as the range and the resolution")
    print("    behind it, and my first two attempts were short on one each.")
    print("    REPORTED AS A REQUIREMENT, NOT WIRED AND NOT FITTED: no value of")
    print("    d is adopted anywhere, and nothing downstream reads this.")

    print("\n[7] WHAT THIS SETTLES")
    print("-" * 78)
    print("  SETTLED, scope-(b): R <= 1 for every letter in the admissible hull")
    print("    d in [-h, 0], so no such letter gives an asymmetry even POINTING")
    print("    the right way.  The eigenvalue criterion's falsification --")
    print("    'whatever is absent breaks the bar symmetry' -- is NOT satisfiable")
    print("    inside the bond-letter family.  A one-parameter search is ruled")
    print("    out before it is run.")
    print("  🛑 RETRACTED (was: 'a bigger irrep does NOT escape it'): FALSE as a")
    print("    general claim.  |det rho_lambda(sigma_i)| = q^(m+ - m-), so the")
    print("    escape IS open on column-heavy partitions -- the sign rep of any")
    print("    H_n has |det| = 1/q < 1.  Verified on one block and generalised;")
    print("    see irrep_determinant_escape_probe.  The R <= 1 bound is")
    print("    unaffected (regular rep, computed directly).")
    print("  SETTLED, scope-(a): delta IS the isospin-mixing asymmetry (checked")
    print("    exactly in [1]) and is 1.4e-3 -- it could not have helped even")
    print("    without the bound.")
    print("  LOCALISED, and this is the useful part: R is unbounded OUTSIDE the")
    print("    hull, diverging exactly at d = 1/q and d = -q -- the two ISOSPIN")
    print("    PROJECTORS, where the transfer matrix degenerates.  Nature's")
    print(f"    R = {fmt(need, 6)} is reached at d = {fmt(d_need, 12)},")
    print(f"    which is {fmt(1 / q - d_need, 6)} from the projector.")
    print("  THE VERDICT THAT READS OFF THAT NUMBER: the framework would need")
    print("    its bond letter fine-tuned to ~2e-7 of a DEGENERATE point.  That")
    print("    is not a mechanism, it is a fine-tuning -- so this localisation")
    print("    should be read as evidence AGAINST the letter carrying the")
    print("    asymmetry at all, not as a target to aim a derivation at.")
    print("  NOT SETTLED: where the missing structure IS.  Not the letter, not")
    print("    the irrep dimension, and not a decayed pair sum")
    print("    (allpairs_decay_turnover_exclusion_probe).")
    print("  NOT CLAIMED: nothing wired, nothing fitted.  R is alpha-free, and")
    print("    d_need is REPORTED as a requirement, never adopted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
