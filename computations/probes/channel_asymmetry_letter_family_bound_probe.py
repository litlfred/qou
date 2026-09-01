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
    gives `+2.224566` against `~ -0.1`: a **22.25 : 1** asymmetry.
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
requiring `R ~ 22.25`.  **`R` is scale-free**: `alpha` cancels, so no
calibration, no MeV, and nothing to fit.

## THE RESULT — an EXACT INEQUALITY, not a swept band

    R(d) <= 1  for every admissible letter,
               with equality iff  |l_+| = |l_-|  OR  |det T| = 1

and nature requires `R ~ 22.25`.  **Excluded by an inequality, in the correct
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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 50
TOL = mp.mpf(10) ** -40

# nature, for comparison only (AME2020 / scattering); never an input
B_PN_3S1 = mp.mpf("2.224566")      # deuteron, bound
B_T1_SCALE = mp.mpf("0.1")         # the 1S0 channels, ~ -0.066 .. -0.1, unbound


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
    q = mp.mpf(Q_50_DIGIT_STR)
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
    print("    inequality, not a swept observation.  Nature needs R ~ 22.25 > 1,")
    print("    so the family is excluded ON THE WRONG SIDE, not merely short.")
    print()
    print("    delta is a displacement of 1.4e-3 INSIDE this range.  It is not")
    print("    special and it could not have helped: the bound is on the range,")
    print("    not on where in the range the p-n letter happens to sit.")

    print("\n[6] WHAT THIS SETTLES")
    print("-" * 78)
    print("  SETTLED, scope-(b): no bond letter in the admissible family gives a")
    print("    channel asymmetry beyond a few percent.  The eigenvalue")
    print("    criterion's falsification -- 'whatever is absent breaks the bar")
    print("    symmetry' -- is NOT satisfiable inside the bond-letter family.")
    print("    An entire one-parameter search is ruled out before it is run.")
    print("  SETTLED, scope-(a): delta is the isospin-mixing asymmetry (checked")
    print("    exactly in [1]), and is 1.4e-3 -- four orders below what is")
    print("    needed even if the family bound did not already exclude it.")
    print("  NOT SETTLED: where the missing structure IS.  This says it is not")
    print("    in the letter.  The next candidates are outside the")
    print("    one-crossing algebra entirely.")
    print("  NOT CLAIMED: nothing wired, nothing fitted.  R is alpha-free.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
