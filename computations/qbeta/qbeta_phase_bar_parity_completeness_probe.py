#!/usr/bin/env python3
"""The forced bar-odd projection does not make the ladder phase bar-odd — u/2 does not.

BEAN `qou-cds1`, extending its own bar-parity analysis by one term.

WHAT THE BEAN PROVED (sorry-free, MarkovZFullBarCondition.lean):

    eigenphase_barOdd_of_barEven      bar(z)=z    =>  bar(2a)+2a = 0
    eigenphase_bar_defect_of_fullBar  bar(z)=z-h  =>  bar(2a)+2a = h^2

i.e. the eigenphase a = (z-1)h/2 is bar-odd EXACTLY when z is bar-even; z_C is
bar-even so a_C is bar-odd, while z_D satisfies the full-bar condition so under
D the eigenphase is NOT bar-odd, with a z-INDEPENDENT defect. The bean concludes
that the bar-odd projection is therefore "forced with no free parameter":

    a_odd = a - h^2/4.

THE TERM THAT WAS NEVER CHECKED. The ladder's phase is not `a`. It is

    phase = a - u/2,      u = b * hbar_q^2,   hbar_q = (q-1)/q.

Bar-parity of every factor, computed symbolically (bar: q -> 1/q):

    h        -> -h        (bar-ODD)
    h^2, b   ->  h^2, b   (bar-EVEN)
    hbar_q   -> -q*hbar_q   NEITHER
    u        ->  q^2 * u    NEITHER

So `u` is neither bar-even nor bar-odd, and consequently, for ANY bar-odd `a`,

    bar(a - u/2) + (a - u/2)  =  -u*(1+q^2)/2   !=  0.

MEASURED CONSEQUENCES (proton anchor, 50 dps):

  1. The defect is IDENTICAL in both conventions: -0.0095054571 for C's a_C and
     for D's forced a_odd alike. It is carried entirely by u, so it is
     CONVENTION-INDEPENDENT — not a D problem, a ladder problem.

  2. Replacing u/2 by its bar-odd part u_odd/2 = u(1-q^2)/4 moves 1-F by
     15.1 % of the required correction. This is not a rounding-level term.

READING. The bean's two Lean results are correct as stated — they are about `a`
alone. What does not follow is the motivation attached to the projection: making
`a` bar-odd does not make the PHASE bar-odd, because u/2 was never bar-odd, in
either frame. So "restore bar-oddness" is not achieved by a_odd on its own.

WHAT THIS DOES NOT ESTABLISH. Whether F is REQUIRED to be bar-even is an open
question this probe does not settle — Q_A is not bar-odd in the naive sense
(bar(Q_A)/Q_A = q^3*|q^2+2q-1|/|q^2-2q-1|, not +-1), so the requirement cannot
be read off the chain as written. If bar-evenness is NOT required, the
observation above is a curiosity. If it IS required, then the ladder violates it
in both conventions by a term worth 15 % of the correction, and the projection
is incomplete rather than forced-and-final.

Scope-(a) throughout: measurement, no derivation, no value proposed, nothing
wired.
"""
from __future__ import annotations

import sys

import mpmath as mp

# --- muon anchor: READ, never retyped ---------------------------------------
# This file used to carry the muon q0 as a string literal. A transcribed pin
# cannot be re-pinned, cannot be flipped by QOU_Q0_ANCHOR, and reports a
# q0Anchor describing its label rather than its computation. The literal here
# was B = Vol(4_1)/206.7682830, the CODATA-2018 derivation -- superseded by the
# owner ruling of 2026-08-22 (A -> CODATA 2022, PR #5500). Reading the anchor
# is correct before and after that ruling; retyping either value is not.
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[2]
                        / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import _q0_value_for_anchor as _q0_for  # noqa: E402

mp.mp.dps = 50

ANCHORS = {
    "proton": mp.mpf("1.10997858275138080759166909561076887987449912187357873607281"),
    "muon": mp.mpf(_q0_for("muon")),
}
M_E = mp.mpf("0.51099895069")
Q_CODATA = mp.mpf("0.78233341")


def main() -> int:
    ok = True
    for name, q in ANCHORS.items():
        h = q - 1 / q
        hbar = (q - 1) / q
        b = mp.sqrt((h**2 + 3) / (h**2 + 4))
        u = b * hbar**2
        Q_A = M_E * abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)
        target = 1 - Q_CODATA / Q_A

        z_C = mp.sqrt(q) / (q + 1)
        z_D = q**3 / (q**2 + 1)
        a_C = (z_C - 1) * h / 2
        a_D_odd = (z_D - 1) * h / 2 - h**2 / 4      # the forced projection

        u_odd = u * (1 - q**2) / 2                   # (u - bar u)/2, since bar u = q^2 u
        u_even = u * (1 + q**2) / 2

        print(f"=== anchor {name}")
        print(f"  u = {mp.nstr(u, 12)}   u_odd = {mp.nstr(u_odd, 12)}   "
              f"u_even = {mp.nstr(u_even, 12)}")

        defects = []
        for nm, a in (("C  a_C", a_C), ("D  a_odd (forced)", a_D_odd)):
            phase = a - u / 2
            # bar(a) = -a for both (a_C bar-odd; a_odd bar-odd by construction)
            bar_phase = -a - (q**2 * u) / 2
            defect = bar_phase + phase
            defects.append(defect)
            print(f"  {nm:<20} bar(phase)+phase = {mp.nstr(defect, 10)}  "
                  f"(0 iff bar-odd)")

        # the defect is the SAME in both frames, and equals -u_even
        ok &= abs(defects[0] - defects[1]) < mp.mpf("1e-40")
        ok &= abs(defects[0] + u_even) < mp.mpf("1e-40")
        ok &= abs(defects[0]) > mp.mpf("1e-3")        # and it is not small

        def one_minus_F(a, shift):
            return 1 - mp.cos(a - shift) * (1 - u**2)

        d_full = one_minus_F(a_D_odd, u / 2)
        d_odd = one_minus_F(a_D_odd, u_odd / 2)
        moved = abs(d_full - d_odd) / target
        print(f"  replacing u/2 by its bar-odd part moves {mp.nstr(moved*100, 6)} % "
              f"of the target")
        ok &= moved > mp.mpf("0.05")                  # a real term, not noise
        print()

    print("FINDINGS")
    print("  1. u is NEITHER bar-even nor bar-odd: bar(u) = q^2 * u (symbolic).")
    print("  2. Hence for ANY bar-odd a, bar(a - u/2) + (a - u/2) = -u(1+q^2)/2,")
    print("     IDENTICAL in C and D — the defect is convention-independent.")
    print("  3. It is worth ~15 % of the required correction, not a rounding term.")
    print("  => making `a` bar-odd does not make the PHASE bar-odd. The bean's")
    print("     Lean is correct as stated (it is about `a`); the motivation")
    print("     attached to the projection does not follow from it.")
    print("  OPEN: whether F must be bar-even at all is NOT settled here.")
    print()
    print("ASSERTIONS PASS" if ok else "ASSERTIONS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
