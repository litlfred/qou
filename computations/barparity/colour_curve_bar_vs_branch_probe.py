#!/usr/bin/env python3
"""The colour curve's 7.878 % is a BRANCH asymmetry, not a BAR asymmetry.

Beans `qou-ndt5` (the s = +-sqrt(q) branch) and `qou-fi93` (the bar-defect /
matter-antimatter asymmetry).  Companion to
`crossing_energy_bar_split_probe.py` in the same directory.

TWO INVOLUTIONS ARE IN PLAY AND THEY ARE NOT THE SAME ONE.  `qou-ndt5` settles
the algebra: the colour-curve modulus is `z = s - 1/s` with `s^2 = q`, `r` is
the polynomial `r(z) = (5/27)(4z^3 + 3z^2 + 3z + 4)`, and `s -> -1/s` is the
UNIQUE lift of the substrate bar `q -> 1/q` that preserves the degeneration
locus `s^2 + s - 1`.  `qou-fi93` measures a 7.878 % asymmetry as
`r(z) - r(-z)` and reads it as a candidate matter/antimatter defect.

    THE BAR       q -> 1/q,  lifted as  s -> -1/s
    THE BRANCH    s -> -s    (same q; the other square root)

They act on `z` in opposite ways, and that is the whole content of this probe:

    z(-1/s) = -1/s - 1/(-1/s) = -1/s + s = z        BAR FIXES z
    z(-s)   = -s  - 1/(-s)    = -s  + 1/s = -z      BRANCH NEGATES z

So `r`, being a polynomial in `z`, is EXACTLY BAR-INVARIANT -- and
`r(z) - r(-z)` is a difference between the two SQUARE-ROOT BRANCHES over one
and the same `q`, not between `q` and `1/q`.

WHY THAT MATTERS FOR `qou-fi93`.  Matter/antimatter in this framework is the
bar (`prop:antiparticle-crossing-reversal`: the mirror sends `q <-> q^-1`).
A quantity that is exactly bar-invariant cannot distinguish matter from
antimatter AT ALL -- so the colour curve is the wrong parity to carry a
matter/antimatter asymmetry, for a structural reason, independently of
`qou-fi93`'s own counting-measure survey.  That is a SECOND and independent
route to the same exclusion.

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

s = sp.Symbol("s", nonzero=True)
z = sp.Symbol("z")


def hdr(t: str) -> None:
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# the corpus's own objects
z_of_s = s - 1 / s
r_of_z = sp.Rational(5, 27) * (4 * z**3 + 3 * z**2 + 3 * z + 4)
deg_locus = s**2 + s - 1          # z + 1 = 0  <=>  this  (qou-ndt5)

# ---------------------------------------------------------------- section 1
hdr("[1] The two involutions, and what each does to z")

bar_s = -1 / s            # the UNIQUE lift of q -> 1/q preserving the locus
branch_s = -s             # the other square root of the SAME q

z_bar = sp.simplify(z_of_s.subs(s, bar_s))
z_branch = sp.simplify(z_of_s.subs(s, branch_s))

print(f"  z(s)            = {z_of_s}")
print(f"  z(-1/s)  [BAR]  = {z_bar}")
print(f"  z(-s) [BRANCH]  = {z_branch}")
print()
print(f"  z(-1/s) - z(s)  = {sp.simplify(z_bar - z_of_s)}      -> BAR FIXES z")
print(f"  z(-s)  + z(s)   = {sp.simplify(z_branch + z_of_s)}      -> BRANCH NEGATES z")
assert sp.simplify(z_bar - z_of_s) == 0
assert sp.simplify(z_branch + z_of_s) == 0

# and confirm each really is a lift of the stated q-map
q_bar = sp.simplify((bar_s) ** 2)
q_branch = sp.simplify((branch_s) ** 2)
print()
print(f"  q under BAR     = {q_bar}    (should be 1/q = 1/s^2)   {sp.simplify(q_bar - 1/s**2) == 0}")
print(f"  q under BRANCH  = {q_branch}       (should be q  = s^2)     {sp.simplify(q_branch - s**2) == 0}")
assert sp.simplify(q_bar - 1 / s**2) == 0
assert sp.simplify(q_branch - s**2) == 0

# ---------------------------------------------------------------- section 2
hdr("[2] The bar lift is the one that preserves the degeneration locus")

for label, m in (("s -> -1/s", bar_s), ("s -> 1/s", 1 / s)):
    img = sp.simplify(sp.expand(deg_locus.subs(s, m) * s**2))
    prop = sp.simplify(sp.factor(img + deg_locus))   # 0 iff img == -locus
    same = sp.simplify(sp.factor(img - deg_locus))   # 0 iff img ==  locus
    keeps = (prop == 0) or (same == 0)
    print(f"  {label:<12} (s^2+s-1) -> {img}   preserves locus: {keeps}")

print()
print("  Only `s -> -1/s` sends the locus to a scalar multiple of itself, so it")
print("  is the bar lift qou-ndt5 identifies. `s -> 1/s` gives s^2 - s - 1, a")
print("  DIFFERENT polynomial (roots phi, -1/phi).")

# ---------------------------------------------------------------- section 3
hdr("[3] Therefore r is EXACTLY bar-invariant, and the 7.878% is the OTHER involution")

r_of_s = sp.simplify(r_of_z.subs(z, z_of_s))
r_bar = sp.simplify(r_of_s.subs(s, bar_s))
r_branch = sp.simplify(r_of_s.subs(s, branch_s))

d_bar = sp.simplify(sp.expand(r_bar - r_of_s))
d_branch = sp.simplify(sp.expand(r_of_s - r_branch))

print(f"  r(bar s) - r(s)     = {d_bar}          <- EXACTLY ZERO")
assert d_bar == 0

# the branch defect, in z, is qou-fi93's own formula
d_branch_z = sp.simplify(sp.expand(r_of_z - r_of_z.subs(z, -z)))
fi93 = sp.Rational(10, 27) * z * (4 * z**2 + 3)
print(f"  r(z) - r(-z)        = {sp.factor(d_branch_z)}")
print(f"  qou-fi93's formula  = {sp.factor(fi93)}")
print(f"  difference          = {sp.simplify(d_branch_z - fi93)}   -> the SAME object")
assert sp.simplify(d_branch_z - fi93) == 0

print("""
  So qou-fi93's bar_defect is, precisely, the BRANCH defect r(z) - r(-z):
  a difference between the two square roots of ONE q, not between q and 1/q.
  Under the actual bar, r does not move at all.""")

# ---------------------------------------------------------------- section 4
hdr("[4] Numbers at the substrate anchor")

from qou_substrate.constants import q_at  # noqa: E402

q0 = q_at(dps=60)
s0 = mp.sqrt(q0)
z0 = s0 - 1 / s0


def r_num(zv):
    return mp.mpf(5) / 27 * (4 * zv**3 + 3 * zv**2 + 3 * zv + 4)


print(f"  q0            = {mp.nstr(q0, 30)}")
print(f"  s0 = +sqrt(q0)= {mp.nstr(s0, 30)}")
print(f"  z0 = s0 - 1/s0= {mp.nstr(z0, 30)}")
print()
print(f"  r(+z0)        = {mp.nstr(r_num(z0), 25)}")
print(f"  r(-z0)        = {mp.nstr(r_num(-z0), 25)}")
# TWO NORMALISATIONS, and they differ by exactly a factor of 2.  Report both
# and name them, because AGENTS.md records this exact trap -- "a quantity
# differing only by normalisation, mistaken for a discrepancy" -- and a
# reader meeting one figure beside the bean's other one would read a
# contradiction where there is none.
num = r_num(z0) - r_num(-z0)
rel_sum = num / (r_num(z0) + r_num(-z0))          # qou-fi93's convention
rel_mean = num / ((r_num(z0) + r_num(-z0)) / 2)   # twice that
print(f"  (r+ - r-)/(r+ + r-)       = {mp.nstr(100 * rel_sum, 12)} %"
      "   <- qou-fi93's 7.878 %, sum-normalised")
print(f"  (r+ - r-)/mean(r+, r-)    = {mp.nstr(100 * rel_mean, 12)} %"
      "   <- the same defect, mean-normalised")
print(f"  ratio of the two          = {mp.nstr(rel_mean / rel_sum, 6)}"
      "   <- exactly 2, by construction; NOT a discrepancy")
assert abs(rel_mean / rel_sum - 2) < mp.mpf("1e-50")
print()
print("  And note z0 = sqrt(q0) - 1/sqrt(q0) is the bar-odd factor OF THE")
print("  SQUARE-ROOT VARIABLE -- the s-analogue of the (q - 1/q) that the")
print("  companion probe shows the crossing energy keeps undivided.")
print(f"  z0           = {mp.nstr(z0, 25)}")
print(f"  q0 - 1/q0    = {mp.nstr(q0 - 1/q0, 25)}")
print(f"  z0 * (s0 + 1/s0) = {mp.nstr(z0 * (s0 + 1/s0), 25)}  = q0 - 1/q0? "
      f"{abs(z0 * (s0 + 1/s0) - (q0 - 1/q0)) < mp.mpf('1e-50')}")

# ---------------------------------------------------------------- section 5
hdr("[5] VERDICT -- a second, independent route to qou-fi93's exclusion")

print("""
  ESTABLISHED (exact, sympy):

    1. The substrate bar q -> 1/q, lifted as s -> -1/s (the unique lift
       preserving the degeneration locus s^2 + s - 1), FIXES z = s - 1/s.

    2. r is a polynomial in z, hence EXACTLY bar-invariant: r(bar s) = r(s),
       identically, with zero defect.

    3. qou-fi93's bar_defect (10/27)z(4z^2+3) is verified here to be exactly
       r(z) - r(-z) -- the BRANCH involution s -> -s, which fixes q and
       negates z.  It is a difference between the two square roots of ONE q.

  CONSEQUENCE, and it is independent of qou-fi93's own argument.  Matter and
  antimatter are related by the BAR in this framework
  (prop:antiparticle-crossing-reversal sends q <-> q^-1).  A quantity that is
  exactly bar-invariant cannot distinguish them at all.  So the colour curve
  is the WRONG PARITY to carry a matter/antimatter asymmetry -- structurally,
  not because the available counting measures happen to be bar-even.

  qou-fi93 reached the same exclusion by surveying the counting objects and
  finding them all bar-even.  This reaches it from the other side: the
  colour curve itself has no bar-odd part to couple TO.  Two independent
  routes to one exclusion is worth more than either alone.

  WHAT IS NOT CLAIMED:

    * The 7.878 % is NOT shown to be unphysical.  It is a real difference
      between two square-root branches, and qou-ndt5 records the owner's
      standing ruling on those -- "not sure. don't exclude but maybe not
      observable".  This probe does not touch that question; it says only
      that the difference is BRANCH-parity, not BAR-parity.

    * Nothing here bears on whether the negative branch is observable, nor
      on whether the window (phi^-2, phi^2) is bounded above -- the gate
      qou-ndt5 names.  That remains the owner's open call.

  Scope (b) on the parity claim: the invariant is the exact bar-invariance
  of z, proved rather than measured.  Scope (a) on nothing -- no numerical
  near-miss is involved.
""")

print("PROBE OK -- all symbolic assertions passed.")
