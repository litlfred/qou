#!/usr/bin/env python3
"""pairing_parity_b3_sign_probe.py

The odd-even pairing term DERIVES the b3 sign and NOT the magnitude.

THE POINTER THAT LED HERE
-------------------------
fingerprint_screen_zero_parameter left a specific residue: smooth growth laws get
b4 nearly right ([n]_q! to 1.66%) and b3 badly wrong (low by 16-18%). Whatever
supplies b3 is NOT a smooth growth law -- so look for something non-smooth at
A = 3. The parities are:

    A=2  2H  Z=1,N=1  ODD-ODD
    A=3  3H/3He       ODD-A
    A=4  4He Z=2,N=2  EVEN-EVEN

and the semi-empirical pairing term is parity-dependent by construction:
+delta(A) even-even, 0 odd-A, -delta(A) odd-odd, delta > 0.

RESULT 1 -- THE SIGN IS DERIVED, NOT FITTED
--------------------------------------------
    b3-contribution = p(3) - 3 p(2) = 0 - 3(-delta) = +3 delta > 0

for EVERY delta > 0. The signs come from which nuclei are odd and which are even;
the magnitude does not enter the sign at all. Formalised sorry-free in
QOU/Mass/PairingParityForcesPositiveB3.lean.

**This is the first mechanism in the whole arc that produces the measured sign
for a principled reason** rather than by choice of coefficient. Every earlier
candidate either could not contribute (Delta^3 = 0: pair counts, all SU(N)
antisymmetric Casimirs), carried no magnitude (mu-bar = +-1), or got the sign
wrong (b4/b3 <= 0 for dim[1^n], the cubic Casimir, p(A), A^3).

It also has a textbook physical reading: the deuteron is ODD-ODD, so pairing
PENALISES it -- which is the standard reason 2H is so weakly bound, and a weak
B(2) is exactly what makes b3 = B(3) - 3B(2) positive.

RESULT 2 -- THE MAGNITUDE IS NOT DERIVED, AND THE GOOD NUMBER WAS CONVENTION LUCK
----------------------------------------------------------------------------------
Fit a smooth term plus the pairing term to b3 and b4, then PREDICT b2. Best
smooth partner is the central binomial C(2n,n):

    raw AME, isospin-averaged A=3        b2 pred 2.196193    1.28%
    raw AME, 3H                          b2 pred 1.887753   15.14%
    Coulomb-corrected (3H, 4He + 0.70)   b2 pred 2.044540    8.09%

**The 1.28% does not survive the Coulomb correction, and that correction is the
physically required one.** A model carrying no Coulomb term must be compared
against Coulomb-corrected data; Coulomb ~ Z(Z-1)/A^(1/3) touches 3He and 4He but
NOT 2H or 3H, so 3H is the Coulomb-free A=3 point and 4He needs its own shift.
The 1.28% was the best of nine trials on the one dataset that flatters it.

**Reported as convention luck, not a result.** The honest verdict is that the
pairing route derives the SIGN and not the SIZE -- a genuine advance on "no
candidate", and not a closure.

SCOPE
-----
Derives no magnitude. Does not refute the pairing route -- it is the strongest
candidate the arc has produced and the first with a derived sign. What is
recorded is exactly how far it gets, and that its apparent quantitative success
is an artifact of choosing the flattering dataset.

Bean qou-edt7.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb, factorial  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from q_parameter import Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)

# SEMF pairing, delta = 1: 2H odd-odd (-), A=3 odd-A (0), 4He even-even (+)
P = {2: -mp.mpf(1) / mp.mpf(2) ** mp.mpf(1.5), 3: mp.mpf(0), 4: mp.mpf(1) / 8}
EC4 = mp.mpf("0.70")   # Coulomb shift on 4He; corpus Tjon block gives B ~ 29.0


def main() -> int:
    wb = WitnessBuilder("pairing-parity-b3-sign", engine="mpmath")
    wb.set_description(
        "The odd-even pairing term DERIVES the b3 sign: 2H is odd-odd so pairing "
        "enters as -delta, A=3 is odd-A so it vanishes, giving a contribution "
        "+3delta > 0 for EVERY delta -- the first mechanism in the arc with the "
        "right sign for a principled reason. The MAGNITUDE is not derived: the "
        "1.28% b2 prediction does not survive the physically required Coulomb "
        "correction (8.09%), so it is convention luck, not a result."
    )
    ok = True

    D = ame_binding_mev(1, 2)
    T3, He3, He4 = ame_binding_mev(1, 3), ame_binding_mev(2, 3), ame_binding_mev(2, 4)
    q = mp.mpf(str(Q))

    # ---- Result 1: the sign, and its independence of delta ---------------
    print("RESULT 1 -- the sign is forced by the parities\n")
    print("  2H ODD-ODD -> p(2) = -delta;  A=3 ODD-A -> p(3) = 0")
    print("  b3-contribution = p(3) - 3p(2) = +3 delta > 0  for EVERY delta > 0\n")
    contribs = []
    for dlt in ("0.01", "0.1", "1", "10", "1000"):
        d = mp.mpf(dlt)
        c = mp.mpf(0) - 3 * (-d)
        contribs.append({"delta": fmt(d), "b3_contrib": fmt(c), "positive": c > 0})
        print(f"    delta = {dlt:>6}   b3-contribution = {mp.nstr(c,8):>10}   "
              f"{'POSITIVE' if c > 0 else 'NEG'}")
    wb.add_data("sign_independent_of_delta", contribs)
    wb.add_assertion(
        name="pairing_forces_positive_b3_for_every_delta",
        computed=str(sum(1 for c in contribs if c["positive"])),
        expected=str(len(contribs)), tolerance="0",
        unit="delta values giving a positive b3 contribution",
        source=("p(3) - 3p(2) = 3delta; the sign comes from the parities, not the "
                "coefficient. Lean: PairingParityForcesPositiveB3"),
    )
    ok &= all(c["positive"] for c in contribs)

    # ---- Result 2: the magnitude, across datasets -------------------------
    def qint(n):
        return sum(q ** (n - 1 - 2 * k) for k in range(n)) if n > 0 else mp.mpf(0)

    def qfact(n):
        r = mp.mpf(1)
        for k in range(1, n + 1):
            r *= qint(k)
        return r

    SMOOTH = {"q_factorial": qfact, "n_factorial": lambda n: mp.mpf(factorial(n)),
              "central_binomial": lambda n: mp.mpf(comb(2 * n, n))}
    SETS = {"raw_isospin_average": (D, (T3 + He3) / 2, He4),
            "raw_3H": (D, T3, He4),
            "coulomb_corrected": (D, T3, He4 + EC4)}

    print("\nRESULT 2 -- the magnitude: fit to b3,b4 then PREDICT b2\n")
    print(f"  {'dataset':<22} {'smooth':<18} {'b2 pred':>11} {'err':>9}")
    rows = {}
    for sn, (b2t, B3, B4) in SETS.items():
        b3, b4 = B3 - 3 * b2t, B4 - 4 * B3 + 6 * b2t
        for nm, fs in SMOOTH.items():
            s3, p3 = fs(3) - 3 * fs(2), P[3] - 3 * P[2]
            s4, p4 = fs(4) - 4 * fs(3) + 6 * fs(2), P[4] - 4 * P[3] + 6 * P[2]
            det = s3 * p4 - p3 * s4
            g, d = (b3 * p4 - p3 * b4) / det, (s3 * b4 - b3 * s4) / det
            b2p = g * fs(2) + d * P[2]
            err = abs(b2p - b2t) / b2t
            rows[f"{sn}|{nm}"] = {"b2_pred": fmt(b2p), "err": fmt(err)}
            print(f"  {sn:<22} {nm:<18} {mp.nstr(b2p,8):>11} {mp.nstr(err*100,5):>8}%")
    wb.add_data("magnitude_by_dataset", rows)

    best_raw = mp.mpf(rows["raw_isospin_average|central_binomial"]["err"])
    best_cc = mp.mpf(rows["coulomb_corrected|central_binomial"]["err"])
    print(f"\n  the flattering dataset gives {mp.nstr(best_raw*100,4)}%; the physically")
    print(f"  required Coulomb-corrected one gives {mp.nstr(best_cc*100,4)}%.")
    print("  Coulomb ~ Z(Z-1)/A^(1/3) touches 3He and 4He but NOT 2H or 3H, so 3H is")
    print("  the Coulomb-free A=3 point and 4He needs its own shift. A model with no")
    print("  Coulomb term must be compared against corrected data.")
    wb.add_assertion(
        name="magnitude_does_not_survive_the_coulomb_correction",
        computed=fmt(best_cc), expected="0.0809", tolerance="0.02",
        unit="relative b2 error on the Coulomb-corrected dataset",
        source=("1.28% on raw isospin-averaged vs 8.09% Coulomb-corrected; the "
                "good number is the best of nine trials on the one dataset that "
                "flatters it -- convention luck, not a result"),
    )
    ok &= best_cc > mp.mpf("0.05")

    wb.add_data("verdict", {
        "sign_derived": True,
        "sign_why": "p(3) - 3p(2) = 3delta > 0 from the parities alone; 2H is "
                    "odd-odd (penalised, the textbook reason it is weakly bound) "
                    "and A=3 is odd-A",
        "first_mechanism_with_a_derived_sign": True,
        "magnitude_derived": False,
        "magnitude_why_not": "the 1.28% b2 prediction is dataset-dependent and "
                             "degrades to 8.09% under the physically required "
                             "Coulomb correction",
        "pairing_route_refuted": False,
        "status": "strongest candidate the arc has produced; sign derived, size open",
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
