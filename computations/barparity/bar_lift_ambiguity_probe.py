#!/usr/bin/env python3
"""Two lifts of the bar to sqrt(q), and they give the SAME object opposite parity.

Beans `qou-ndt5` (is the negative branch s = -sqrt(q) observable?) and
`qou-fi93`.  Lean:
`content/quantum-observable-universe/lean/QOU/BringsSurface/BarLiftAmbiguity.lean`.

WHY THIS EXISTS.  Two corpus arcs define the SAME expression and do not cite
each other:

    QOU/Braiding/SkeinNormalisation.lean:74        sJ  (u) := u - u^-1
    QOU/BringsSurface/ColourCurveBarVsBranch.lean:45  zOf (s) := s - s^-1

`sJ` is the bar-ODD generator of the half-power skein normalisation; `zOf` is
the colour curve's spacetime modulus.  Byte-identical definitions.

The two arcs then lift the substrate bar q -> q^-1 to the square root
DIFFERENTLY, and both lifts are legitimate -- each squares to q^-1:

    SkeinNormalisation (sJ_bar_antiinvariant)   u ->  u^-1
    ColourCurveBarVsBranch (barLift)            u -> -u^-1

They differ by exactly the branch swap u -> -u, which is the map qou-ndt5 asks
about.  And the same object has OPPOSITE bar parity under the two.

THE CONSEQUENCE IS NOT COSMETIC.  It decides whether the colour curve can
carry a matter/antimatter asymmetry at all, and the corpus currently answers
both ways in two places.  Two claims already recorded are CONDITIONAL on the
lift and were stated unconditionally -- one of them written on 2026-09-13 by
the same session that is writing this file:

  1. "the name bar_defect is a misnomer; it is a BRANCH defect" (qou-ndt5)
  2. "the colour curve is the wrong parity to carry a matter/antimatter
     asymmetry -- structurally" (qou-ndt5 consequence 3, a second route to
     qou-fi93's exclusion)

Both hold under the ColourCurveBarVsBranch lift.  Under the SkeinNormalisation
lift the bar itself negates z, the original name bar_defect was right, and the
colour curve DOES have bar-odd content.

THIS PROBE DOES NOT CHOOSE A LIFT.  It makes the choice visible and prices it.

Exact `sympy` throughout; one `mpmath.mpf` evaluation at 60 dps.  No float64.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402

mp.mp.dps = 60

u = sp.Symbol("u", positive=True)          # u = sqrt(q); qou-ndt5 calls it s
zsym = sp.Symbol("z")


def simp(e):
    return sp.simplify(sp.expand(e))


def inv_lift(e):                            # SkeinNormalisation:  u -> u^-1
    return simp(e.subs(u, 1 / u))


def ndt5_lift(e):                           # ColourCurveBarVsBranch: u -> -u^-1
    return simp(e.subs(u, -1 / u))


def branch(e):                              # branchSwap: u -> -u
    return simp(e.subs(u, -u))


def hdr(s: str) -> None:
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


z = u - 1 / u
q = u ** 2
r27 = 5 * (4 * zsym ** 3 + 3 * zsym ** 2 + 3 * zsym + 4)      # 27 * r(z)

# ---------------------------------------------------------------- section 1
hdr("[1] The two arcs define the SAME expression")

print("  SkeinNormalisation.lean:74        sJ  (u) := u - u^-1")
print("  ColourCurveBarVsBranch.lean:45    zOf (s) := s - s^-1")
print(f"  sJ(u) - zOf(u) = {simp((u - u ** -1) - z)}")
assert simp((u - u ** -1) - z) == 0
print()
print("  One is the half-power skein normalisation's bar-ODD generator; the")
print("  other is the colour curve's spacetime modulus.  Neither arc cites the")
print("  other.")

# ---------------------------------------------------------------- section 2
hdr("[2] BOTH lifts are lifts of the bar, and they differ by the BRANCH")

print(f"  inv_lift  on q = u^2 :  q -> {inv_lift(q)}    is 1/q? "
      f"{simp(inv_lift(q) - 1 / q) == 0}")
print(f"  ndt5_lift on q = u^2 :  q -> {ndt5_lift(q)}    is 1/q? "
      f"{simp(ndt5_lift(q) - 1 / q) == 0}")
assert simp(inv_lift(q) - 1 / q) == 0
assert simp(ndt5_lift(q) - 1 / q) == 0
print()
print(f"  ndt5_lift = branch o inv_lift ?  "
      f"{simp(ndt5_lift(z) - branch(inv_lift(z))) == 0}")
assert simp(ndt5_lift(z) - branch(inv_lift(z))) == 0
print()
print("  So the ambiguity in WHICH LIFT is exactly the branch ambiguity")
print("  qou-ndt5 asks about.  They are one question, not two.")

# ---------------------------------------------------------------- section 3
hdr("[3] The SAME object, OPPOSITE parity")

zi, zn = inv_lift(z), ndt5_lift(z)
print(f"  under inv_lift  (u ->  u^-1):  z -> {zi}     bar-ODD?  "
      f"{simp(zi + z) == 0}")
print(f"  under ndt5_lift (u -> -u^-1):  z -> {zn}      bar-EVEN? "
      f"{simp(zn - z) == 0}")
assert simp(zi + z) == 0 and simp(zn - z) == 0
print()
print("  This is NOT a disagreement between two objects.  It is one object")
print("  whose bar parity is UNDETERMINED by the bar on q -- fixing it")
print("  requires choosing a lift, and the corpus chooses differently in two")
print("  places.  (Lean: z_parity_not_determined.)")

# ---------------------------------------------------------------- section 4
hdr("[4] The colour curve inherits it, and the defect is the FAMILIAR formula")

r_of_z = r27.subs(zsym, z)
d_ndt5 = simp(ndt5_lift(r_of_z) - r_of_z)
d_inv = simp(r_of_z - inv_lift(r_of_z))

print(f"  27r(bar z) - 27r(z)  under ndt5_lift = {d_ndt5}     <- EXACTLY zero")
assert d_ndt5 == 0

claimed = 10 * zsym * (4 * zsym ** 2 + 3)
print(f"  27r(z) - 27r(bar z)  under inv_lift  = "
      f"{sp.factor(simp(d_inv - claimed.subs(zsym, z)))} + 10z(4z^2+3)")
assert simp(d_inv - claimed.subs(zsym, z)) == 0
print()
print(f"  and r(z) - r(-z) as a polynomial  = {sp.factor(simp(r27 - r27.subs(zsym, -zsym)))}")
assert simp((r27 - r27.subs(zsym, -zsym)) - claimed) == 0
print()
print("  10 z (4z^2 + 3)  IS the formula qou-fi93 and qou-ndt5 both record as")
print("  the 'bar defect' (7.878 % at q0).  Under ndt5_lift it is a BRANCH")
print("  defect and the bar sees nothing; under inv_lift it is a BAR defect and")
print("  the name was right all along.  Same number, opposite reading.")

# ---------------------------------------------------------------- section 5
hdr("[5] The number, at the proton pin (mpmath, 60 dps -- no float64)")

from qou_substrate.constants import q_at  # noqa: E402

q0 = q_at(dps=60)
u0 = mp.sqrt(q0)
z0 = u0 - 1 / u0


def r_num(x):
    return mp.mpf(5) / 27 * (4 * x ** 3 + 3 * x ** 2 + 3 * x + 4)


rp, rm = r_num(z0), r_num(-z0)
rel_sum = abs(rp - rm) / abs(rp + rm)
rel_mean = abs(rp - rm) / (abs(rp + rm) / 2)

print(f"  q0                = {mp.nstr(q0, 30)}")
print(f"  u0 = sqrt(q0)     = {mp.nstr(u0, 30)}")
print(f"  z0 = u0 - 1/u0    = {mp.nstr(z0, 30)}")
print(f"  r(z0)             = {mp.nstr(rp, 30)}")
print(f"  r(-z0)            = {mp.nstr(rm, 30)}")
print()
print(f"  |r(z)-r(-z)| / |r(z)+r(-z)|        = {mp.nstr(rel_sum * 100, 12)} %"
      f"   <- qou-fi93's normalisation")
print(f"  |r(z)-r(-z)| / (|r(z)+r(-z)|/2)    = {mp.nstr(rel_mean * 100, 12)} %"
      f"   <- the MEAN normalisation")
print(f"  ratio of the two                  = {mp.nstr(rel_mean / rel_sum, 20)}"
      f"   (exactly 2, by construction)")
assert abs(rel_mean / rel_sum - 2) < mp.mpf("1e-50")
print()
print("  Both printed, labelled, per the trap recorded in qou-ndt5: reporting")
print("  one against the other reads as a discrepancy when it is a")
print("  normalisation.")

# ---------------------------------------------------------------- verdict
hdr("VERDICT")

print("""
  PROVED (Lean sorry-free, QOU/BringsSurface/BarLiftAmbiguity.lean; verified
  symbolically here):

    * SkeinNormalisation.sJ and ColourCurveBarVsBranch.zOf are the SAME
      expression, u - u^-1, in two arcs that do not cite each other.
    * The two arcs lift the bar q -> q^-1 to the square root differently, and
      BOTH lifts are valid: each squares to q^-1.
    * The two lifts differ by EXACTLY the branch swap u -> -u.  So "which
      lift" and qou-ndt5's "is the negative branch observable" are ONE
      question.
    * Under those lifts the same object is bar-ODD and bar-EVEN respectively,
      so THE BAR PARITY OF z IS NOT DETERMINED BY THE BAR ON q.
    * The colour curve's defect is 0 under one lift and 10 z (4z^2+3) under
      the other -- the same formula both beans call the "bar defect", 7.878 %
      at q0 in qou-fi93's normalisation (15.757 % in the mean normalisation;
      both printed above).

  WHAT THIS CORRECTS, and one of the two is from the same session:

    1. qou-ndt5, 2026-09-13: "the name bar_defect is a MISNOMER; it is a
       branch defect."  Stated unconditionally.  It is CONDITIONAL on the
       lift -- true under ColourCurveBarVsBranch's, false under
       SkeinNormalisation's, where the bar itself negates z and the original
       name was right.
    2. qou-ndt5 consequence 3, offered as "a second, independent route to
       qou-fi93's exclusion": "the colour curve has no bar-odd part to couple
       TO."  Also conditional.  Under the skein lift it HAS one.

  qou-fi93's PRIMARY route to its exclusion -- the survey showing every
  counting measure is bar-even -- is UNAFFECTED.  That argument never passes
  through the square root.  What is weakened is the second route only.

  WHY ndt5Lift WAS CHOSEN, and what that choice actually buys.  qou-ndt5
  selects s -> -s^-1 as "the UNIQUE lift of q -> 1/q preserving the
  degeneration locus s^2 + s - 1", and that uniqueness is CORRECT -- but it is
  uniqueness SUBJECT TO PRESERVING THAT POLYNOMIAL, not uniqueness among lifts
  of the bar.  The skein lift is an equally valid lift preserving something
  else (its own parity grading).  Two defensible conventions, no ruling.

  THIS PROBE DOES NOT CHOOSE.  Choosing is an owner call, it is qou-ndt5's own
  open question, and the owner's standing ruling on it is "not sure. don't
  exclude but maybe not observable."  What is added here is that the choice
  is NOT free: it decides whether the colour curve has bar-odd content, and
  therefore whether qou-ndt5's second route to qou-fi93's exclusion exists.

  Scope (a) throughout: nothing is excluded here, and no lift is refuted.
""")

print("PROBE OK -- all symbolic and numerical assertions passed.")
