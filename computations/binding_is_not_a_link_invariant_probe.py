#!/usr/bin/env python3
"""
binding_is_not_a_link_invariant_probe — settles the open question by finding the
corpus already had the answer: the binding functional is NOT a link invariant and
never was, because the ONE letter that leaves the braid image is the p-n bond.
So the KMS trilemma's expensive leg does not bind.

Bean `qou-brng` (with `qou-unqc`), arc `bk-crossing-mass-binding`. Closes the
question left open by #6399.

## The question

#6399 established a trilemma: keep `tr_M` tracial and the free-energy licence
stays unreachable (KMS at beta = 0); go non-tracial and **Markov move I fails**,
so the object is not a link invariant. That second leg looked expensive because
the Jones polynomial and the braid-closure picture of nucleons rest on
conjugation invariance.

It is only expensive if the BINDING functional has to be a link invariant. It
does not -- and the corpus said so on 2026-08-25, in
`braids-and-knots/markov-disambiguation.md` (PR #5765):

    "tr_M is defined on ALL of H_n(q) ... no braid, no closure, and no topology
     are needed for the number to exist. What the closure supplies is the
     INTERPRETATION. ... for W in H_n(q) that is NOT in the image of
     rho : B_n -> H_n(q), tr_M(W) is a well-defined number WITH NO LINK BEHIND
     IT."

and names the consumer explicitly: *"the binding forms take tr_M of
`atom_braid_word_3A`, whose letters are `c sigma_g + d 1` rather than braid
generators."*

`mass_at_3A_proper.atom_braid_word_3A`'s own docstring is sharper still, and the
sharpness is the whole finding:

    "NAME IS A MISNOMER -- this does NOT return a braid word. The letters OUTSIDE
     the image of rho are exactly the AVERAGED ones, d in {-h/2, -h(1/2 -
     delta/4)} -- NOT merely the d != 0 ones. Under this module's convention
     sigma^-1 = sigma - h, a d == -h letter IS a braid generator."

## What this probe measures

Which bond letters are braid generators, and what follows.

  * `pp`: `d = 0`, the letter is `sigma_g` -- IS a braid generator.
  * `nn`: `d = -h`, the letter is `sigma_g - h = sigma_g^{-1}` -- IS one too.
  * `pn`: `d = -h(1/2 - delta/4)` -- is NOT, and it is the ONLY one that is not.

So the atom word leaves the braid image **exactly at the p-n bond**, i.e. exactly
at the colour-weighted average. Every nucleus with `Z >= 1` and `N >= 1` has at
least one, so the binding functional is not a link invariant for ANY of them.

## Two consequences, and the second is the interesting one

**(1) The trilemma's leg (2) does not bind.** Going non-tracial costs the
link-invariant property, and the binding functional never had it. There is
nothing there to lose. (What a non-tracial weight WOULD cost is `tr_M`'s
link-invariance on genuine braid images -- the Jones polynomial and everything
built on it -- so the framework would need to carry TWO functionals: `tr_M`,
tracial, for topology; and a non-tracial `phi` for thermodynamics. That is
coherent; they are different objects for different jobs. It is not free, but it
is not the same cost.)

**(2) The one quantity the framework gets RIGHT is the one built only from braid
generators.** The 3H/3He mirror splitting is `alpha (L_nn - L_pp)` -- the `L_pn`
terms cancel identically -- so it uses ONLY the `sigma` and `sigma^-1` letters
and IS a difference of genuine link invariants. It is accurate to **0.205 %**
(#6396). The absolute binding includes the averaged p-n letter, is NOT a link
invariant, and is off by **27 % to 226 %**.

That is a correlation, not a demonstrated cause, and this probe does not claim
otherwise. But it is exact and it points somewhere specific.

## Scope

Scope **(a)**. Nothing is wired, no binding energy is computed, and no
non-tracial weight is proposed. The finding is a corpus fact plus its
consequence for #6399's trilemma.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50


def fmt(x, n=10):
    return mp.nstr(x, n)


def main() -> int:
    q0 = Q_MP
    h = q0 - 1 / q0
    delta = flavor_split_leading(q0)

    print("binding_is_not_a_link_invariant_probe")
    print("=" * 78)
    print(f"q0 = {fmt(q0, 20)}   h = q0 - 1/q0 = {fmt(h, 14)}")
    print(f"delta = flavor_split_leading(q0) = {fmt(delta, 12)}")
    print()
    print("THE CRITERION (mass_at_3A_proper.atom_braid_word_3A's own docstring):")
    print("  each letter is the HECKE ELEMENT c*sigma_g + d*1, and under this")
    print("  module's convention sigma^-1 = sigma - h.  So a letter is a BRAID")
    print("  GENERATOR iff d = 0 (it is sigma) or d = -h (it is sigma^-1).")
    print("  Everything else is outside the image of rho : B_n -> H_n(q).")
    print()

    d = {"pp": mp.mpf(0),
         "pn": -h * (mp.mpf(1) / 2 - delta / 4),
         "nn": -h}
    print(f"{'bond':>6} {'d':>20} {'= 0 ?':>8} {'= -h ?':>8} "
          f"{'braid generator?':>18} {'which':>12}")
    in_image = {}
    for k in ("pp", "pn", "nn"):
        is0 = abs(d[k]) < mp.mpf(10) ** -40
        ish = abs(d[k] + h) < mp.mpf(10) ** -40
        ok = is0 or ish
        in_image[k] = ok
        which = "sigma" if is0 else ("sigma^-1" if ish else "--")
        print(f"{k:>6} {fmt(d[k], 14):>20} {str(is0):>8} {str(ish):>8} "
              f"{str(ok):>18} {which:>12}")
    print()
    assert in_image["pp"] and in_image["nn"], "pp and nn must be braid generators"
    assert not in_image["pn"], "pn must be OUTSIDE the braid image"
    print("  => pp and nn ARE braid generators; the p-n letter is the ONLY one")
    print("     that is not -- and it is exactly the COLOUR-WEIGHTED AVERAGE.")
    print()
    # How far outside? Distance to the two braid values, in units of h.
    print(f"  distance from the nearest braid value: "
          f"|d_pn - 0| = {fmt(abs(d['pn']), 8)} = {fmt(abs(d['pn']) / h, 8)} h")
    print(f"                                        "
          f"|d_pn + h| = {fmt(abs(d['pn'] + h), 8)} = "
          f"{fmt(abs(d['pn'] + h) / h, 8)} h")
    print("  -- it sits essentially midway between sigma and sigma^-1, which is")
    print("     what 'averaged' means.  Not a near miss; a genuine interior point.")
    print()

    print("WHICH NUCLEI ARE AFFECTED")
    print("-" * 78)
    print(f"{'iso':>6} {'Z':>3} {'N':>3} {'pn bonds in the chain':>22} "
          f"{'word is a braid?':>18} {'B is a link invariant?':>24}")
    for nm, Z, N in (("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
                     ("6Li", 3, 3), ("7Li", 3, 4)):
        npn = 1 if (Z >= 1 and N >= 1) else 0
        braid = npn == 0
        print(f"{nm:>6} {Z:>3} {N:>3} {npn:>22} {str(braid):>18} "
              f"{str(braid):>24}")
    print()
    print("  Every nucleus with Z >= 1 AND N >= 1 carries a p-n bond, so its word")
    print("  is not a braid image and its binding is NOT a link invariant.  That")
    print("  is every bound nucleus in the low table.")
    print()

    print("CONSEQUENCE 1 — the trilemma's expensive leg does NOT bind")
    print("-" * 78)
    print("  #6399: going non-tracial costs Markov move I, hence the link")
    print("  invariant.  But the BINDING functional never had it.  There is")
    print("  nothing there to lose, so leg (2) is not a cost against binding.")
    print()
    print("  What a non-tracial weight WOULD cost is tr_M's link-invariance on")
    print("  GENUINE braid images -- the Jones polynomial and everything built on")
    print("  it.  So the framework would carry TWO functionals: tr_M, tracial,")
    print("  for topology; and a non-tracial phi for thermodynamics.  Coherent --")
    print("  different objects for different jobs.  Not free, but not the same")
    print("  cost, and it no longer contradicts the framework's foundation.")
    print()

    print("CONSEQUENCE 2 — the accurate quantity is the braid-only one")
    print("-" * 78)
    print("  The 3H/3He mirror splitting is alpha(L_nn - L_pp): the L_pn terms")
    print("  cancel IDENTICALLY, so it uses only the sigma and sigma^-1 letters")
    print("  and IS a difference of genuine link invariants.")
    print()
    print(f"{'quantity':>34} {'uses the p-n letter?':>22} {'accuracy':>22}")
    print(f"{'3H/3He mirror splitting':>34} {'NO (cancels)':>22} "
          f"{'0.205 % (#6396)':>22}")
    print(f"{'absolute binding B_sym':>34} {'YES':>22} "
          f"{'27 % to 226 % off':>22}")
    print()
    print("  The one quantity the framework gets right is exactly the one built")
    print("  only from braid generators; the ones it gets wrong all pass through")
    print("  the averaged letter that leaves the braid image.")
    print()
    print("  THIS IS A CORRELATION, NOT A DEMONSTRATED CAUSE, and nothing here")
    print("  shows the averaged letter is WHY the absolute binding is off.  Two")
    print("  data classes is not a mechanism.  But the split is exact and it")
    print("  points somewhere specific, which is more than the arc had before.")
    print()

    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * NOT that the averaging is wrong.  bring_color_weighted is the")
    print("    canonical, derived p/n convention (owner ruling R3) and the")
    print("    alternative strict_averaged differs by ~1e-4 relative -- three to")
    print("    four orders too small to explain a 27-226 % deficit.  What the")
    print("    averaging does is leave the braid image, not misestimate a number.")
    print("  * NOT that a non-tracial weight will work.  #6399's rank obstruction")
    print("    is untouched: it still needs z off the isolated TL point, and")
    print("    non-traciality does not supply that.")
    print("  * NOT a proposal.  No weight, no z, no binding energy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
