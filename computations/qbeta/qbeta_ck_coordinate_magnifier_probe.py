#!/usr/bin/env python3
"""The c_k coordinates magnify F-errors by 1/u^k — so they overstate D's failure.

BEAN `qou-cds1`. That bean established that the PHASE is a bad coordinate: it
has a square-root branch point 0.062 % above q0, manufactured by writing a
smooth multiplicative correction as cos(alpha - u/2). Its recommendation was to
work in

    F(q) := Q_beta(q) / Q_A(q).

This probe shows the SAME pathology afflicts the c_k coordinate, and quantifies
it as an exact identity rather than an impression.

THE IDENTITY (exact, verified to ~1e-47 at 50 dps, both anchors):

    c_2 + 1  =  (F_required - F_N2) / (F_N1 * u^2)

with  F_N1 = cos(alpha - u/2),  F_N2 = F_N1 * (1 - u^2),  F_required = Q_cod/Q_A.

So the deviation of c_2 from its canonical -1 is the F-residual divided by u^2.
The magnifier 1/u^2 = 13785 is FIXED — it carries no information about the
model, exactly as the bean found the 1/u^3 magnifier does for c_3.

WHY THIS MATTERS FOR THE D RE-DERIVATION. The bean's own table reports the
forced bar-odd projection (a_odd = a - h^2/4, derived with NO free parameter)
as `implied c2 = -1.733`, next to C's -1.018. In c_2 units that reads as a
catastrophic 73 % miss. In F it is:

    C                    -0.076 %   of the required correction
    D z-swap             -35.9  %
    D bar-odd (forced)   - 3.17 %

The forced projection buys a factor ~11 over the naive z-swap. The c_2
coordinate concealed that, because 1/u^2 turns a 3 % F-error into a 0.73
absolute c_2 shift.

WHAT THIS DOES *NOT* SAY. -3.17 % is NOT a closure and must not be read as
one. L2 for Q_beta needs ~7.8 ppb; 3 % is five orders away. The bar-odd
projection remains, in the bean's own words, "NECESSARY and derived, but NOT
sufficient" — and its standing instruction holds: do not search for further
corrections until one lands near -1, because that is a fit. Nothing here
derives F, proposes a c_k value, or wires anything.

Scope-(a) throughout.
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


def substrate(q: mp.mpf) -> dict:
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h**2 + 3) / (h**2 + 4))
    return {
        "h": h,
        "hbar": hbar,
        "b": b,
        "u": b * hbar**2,
        "z_C": mp.sqrt(q) / (q + 1),
        "z_D": q**3 / (q**2 + 1),
        "Q_A": M_E * abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3),
    }


def main() -> int:
    ok = True
    for name, q in ANCHORS.items():
        s = substrate(q)
        u, h, b, hbar = s["u"], s["h"], s["b"], s["hbar"]
        Freq = Q_CODATA / s["Q_A"]

        cases = [
            ("C  alpha=(z_C-1)h/2", (s["z_C"] - 1) * h / 2),
            ("D  z-swap", (s["z_D"] - 1) * h / 2),
            ("D  bar-odd (forced)", (s["z_D"] - 1) * h / 2 - h**2 / 4),
        ]
        print(f"=== anchor {name}   u = {mp.nstr(u, 12)}   1/u^2 = {mp.nstr(1/u**2, 10)}")
        print(f"    target 1 - F_required = {mp.nstr(1 - Freq, 12)}")
        print("    %-22s %-14s %-14s %s" % ("object", "1-F_N2", "rel.dev(F)", "c_2 implied"))
        for nm, a in cases:
            FN1 = mp.cos(a - b * hbar**2 / 2)
            FN2 = FN1 * (1 - u**2)
            c2 = (Freq / FN1 - 1) / u**2
            reldev = (1 - FN2) / (1 - Freq) - 1
            print("    %-22s %-14s %-14s %s"
                  % (nm, mp.nstr(1 - FN2, 10), mp.nstr(reldev, 6), mp.nstr(c2, 8)))
            # the exact identity
            ok &= abs((c2 + 1) - (Freq - FN2) / (FN1 * u**2)) < mp.mpf("1e-40")
        print()

        # the forced projection must beat the z-swap by an order in F
        def dev(a):
            FN2 = mp.cos(a - b * hbar**2 / 2) * (1 - u**2)
            return abs((1 - FN2) / (1 - Freq) - 1)

        d_swap = dev((s["z_D"] - 1) * h / 2)
        d_odd = dev((s["z_D"] - 1) * h / 2 - h**2 / 4)
        ok &= d_odd < d_swap / 10
        ok &= d_odd > mp.mpf("0.01")      # and it is still ~3 %, NOT a closure

    print("IDENTITY: c_2 + 1 = (F_required - F_N2) / (F_N1 * u^2)   [exact]")
    print("  => the c_k coordinates magnify F-errors by 1/u^k, a FIXED factor")
    print("     carrying no information about the model. Judging the D frame in")
    print("     c_k units overstates its failure by ~1e4.")
    print("  The forced bar-odd projection buys ~11x over the z-swap in F")
    print("  (-35.9 % -> -3.17 %), which the c_2 coordinate concealed.")
    print("  It is NOT a closure: L2 needs ~7.8 ppb and this is 3 %.")
    print()
    print("ASSERTIONS PASS" if ok else "ASSERTIONS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
