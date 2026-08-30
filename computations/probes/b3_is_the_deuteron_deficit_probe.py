#!/usr/bin/env python3
"""b3_is_the_deuteron_deficit_probe.py

TWO RETRACTIONS of my own recent claims, and the reframing that survives them.

RETRACTION 1 -- "a systematic 25-100x under-shoot across four mechanisms"
-------------------------------------------------------------------------
I asserted this pattern and proposed spending a turn investigating it. **It is
false.** Measured, in the b3/b2 coordinate (measured value 0.64112282):

    SU(N) antisym Casimir   Delta^3 = 0 EXACTLY -- contribution is ZERO, not small
    Milnor mu-bar           normalised +-1 -- carries NO magnitude at all
    n!                      0.0            -> INFINITE
    [n]_q!                  0.0437062      -> 14.67x
    C(2n,n)                 0.3333333      -> **1.92x**
    pairing                 (see below)

Two of them have no magnitude at all, so "too small" is not even defined for
them. The rest span 1.92x to INFINITE. **That is not a consistent 25-100x
under-shoot** -- C(2n,n) is under by less than a factor of two, which directly
contradicts the range I quoted. What is actually there is the tautology "nothing
produces b3", restated as a pattern.

RETRACTION 2 -- "the fitted pairing delta is 25-40x too weak"
--------------------------------------------------------------
Worse, because it stood as a refutation. I compared the fitted pairing energy at
A=2 (0.208-0.338 MeV) against the SEMF a_P = 12/sqrt(A) = 8.485 MeV. **The SEMF
is fitted to heavy nuclei and has no validity at A <= 4.** Its own predictions
there, with standard coefficients:

    2H   SEMF B = -4.661 MeV   actual  2.225   <- predicts the deuteron is UNBOUND
    3H   SEMF B =  2.325 MeV   actual  8.482
    4He  SEMF B = 22.841 MeV   actual 28.296

A formula that puts the deuteron below threshold cannot supply the standard
against which an A=2 pairing strength is judged. **The refutation is withdrawn.**

Compared instead against the quantity it actually has to explain:

    deuteron deficit  = B(3)/3 - B(2) = 0.475 (isospin avg) .. 0.603 (3H) MeV
    fitted pairing at A=2             = 0.208 .. 0.338 MeV
    SEMF extrapolated to A=2          = 8.485 MeV  -- 17.8x the ENTIRE deficit

The fitted value is the SAME ORDER as the deficit, covering roughly 35-71% of it.
Pairing is **not refuted**; it is a live candidate whose sign is derived and whose
magnitude is the right size.

WHAT SURVIVES, AND IT IS SHARPER THAN THE PATTERN I INVENTED
-------------------------------------------------------------
    b3 = B(3) - 3B(2) = 3 * (B(3)/3 - B(2)) = 3 * (the deuteron deficit)

exactly. So **the b3 question IS the deuteron-weakness question.** A large b3
means a weak B(2), and the deuteron is 17.6-21.3% weaker than b3 = 0 would
require. In binding per nucleon it sits 2.54x below A=3 and 6.36x below 4He.

Every mechanism that treats B(2) as an ordinary member of a smooth family gets b3
too small, because none of them makes the deuteron anomalously weak. That is a
statement about a TWO-BODY anomaly, not a three-body one -- which is a striking
place for a connected three-body cumulant to be dominated from.

This relocates the target: derive the deuteron deficit, not b3. The deficit has
an established physical cause (the near-unitary 3S1 channel, scattering length
5.42 fm against a ~1.4 fm range; the unbound 1S0 virtual state), so whether the
framework reproduces it is a sharper and more tractable question than "produce
b3".

SCOPE
-----
Derives nothing. Retracts two claims of mine, one of which was a refutation now
withdrawn. The reframing (b3 = 3 x deficit) is an identity, not a result -- its
value is that it moves the question to a two-body quantity with known physics.

Bean qou-edt7.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb, factorial  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from q_parameter import Q_MP  # noqa: E402  (exact mpf; NEVER mpf(str(Q)) -- Q is f64)
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)


def main() -> int:
    wb = WitnessBuilder("b3-is-the-deuteron-deficit", engine="mpmath")
    wb.set_description(
        "Retracts two of my own claims: the '25-100x systematic under-shoot' "
        "(false -- factors span 1.92x to infinite, and two mechanisms have no "
        "magnitude at all) and the 'pairing delta is 25-40x too weak' refutation "
        "(invalid standard -- the SEMF predicts an UNBOUND deuteron at A=2). What "
        "survives: b3 = 3 x the deuteron deficit exactly, so the b3 question is "
        "the deuteron-weakness question, a TWO-body anomaly."
    )
    ok = True

    D = ame_binding_mev(1, 2)
    T3, He3, He4 = ame_binding_mev(1, 3), ame_binding_mev(2, 3), ame_binding_mev(2, 4)
    q = +Q_MP

    def qint(n):
        return sum(q ** (n - 1 - 2 * k) for k in range(n)) if n > 0 else mp.mpf(0)

    def qfact(n):
        r = mp.mpf(1)
        for k in range(1, n + 1):
            r *= qint(k)
        return r

    b3m = ((T3 + He3) / 2 - 3 * D) / D

    # ---- Retraction 1 -----------------------------------------------------
    print("RETRACTION 1 -- the '25-100x under-shoot' pattern is FALSE\n")
    print(f"  measured b3/b2 = {mp.nstr(b3m,8)}\n")
    facts = {
        "n_factorial": (mp.mpf(factorial(3)) - 3 * mp.mpf(factorial(2))) / mp.mpf(factorial(2)),
        "q_factorial": (qfact(3) - 3 * qfact(2)) / qfact(2),
        "central_binomial": (mp.mpf(comb(6, 3)) - 3 * mp.mpf(comb(4, 2))) / mp.mpf(comb(4, 2)),
    }
    rows = []
    for nm, v in facts.items():
        r = b3m / v if v != 0 else None
        rows.append({"mechanism": nm, "b3_over_b2": fmt(v),
                     "under_by": "infinite" if r is None else fmt(r)})
        print(f"  {nm:<20} b3/b2 = {mp.nstr(v,9):>12}   under by "
              f"{'INFINITE' if r is None else mp.nstr(r,6)}x")
    print("  SU(N) Casimir        Delta^3 = 0 EXACTLY -- zero, not small")
    print("  Milnor mu-bar        normalised +-1 -- no magnitude at all")
    cb_ratio = b3m / facts["central_binomial"]
    print(f"\n  factors span {mp.nstr(cb_ratio,4)}x to INFINITE, and two have no magnitude.")
    print("  NOT a consistent 25-100x under-shoot. The claim was mine and unmeasured.")
    wb.add_data("retraction_1_undershoot_factors", rows)
    wb.add_assertion(
        name="undershoot_is_not_consistent",
        computed=fmt(cb_ratio), expected="1.92", tolerance="0.2",
        unit="C(2n,n) under-shoot factor",
        source="under 2x, directly contradicting the 25-100x range I asserted",
    )
    ok &= cb_ratio < mp.mpf("3")

    # ---- Retraction 2 -----------------------------------------------------
    print("\nRETRACTION 2 -- the SEMF is not a valid standard at A <= 4\n")
    aV, aS, aC, aA, aP = 15.75, 17.8, 0.711, 23.7, 11.18
    semf = {}
    for nm, Z, A in (("2H", 1, 2), ("3H", 1, 3), ("4He", 2, 4)):
        N = A - Z
        pair = (mp.mpf(0) if A % 2 else
                (aP / mp.sqrt(A) if (Z % 2 == 0 and N % 2 == 0) else -aP / mp.sqrt(A)))
        b = (aV * A - aS * mp.mpf(A) ** (mp.mpf(2) / 3)
             - aC * Z * (Z - 1) / mp.mpf(A) ** (mp.mpf(1) / 3)
             - aA * (A - 2 * Z) ** 2 / mp.mpf(A) + pair)
        semf[nm] = b
        act = {"2H": D, "3H": T3, "4He": He4}[nm]
        print(f"  {nm:<4} SEMF B = {mp.nstr(b,8):>11} MeV   actual {mp.nstr(act,8):>10} MeV"
              f"{'   <- UNBOUND' if b < 0 else ''}")
    wb.add_data("semf_at_low_A", {k: fmt(v) for k, v in semf.items()})
    wb.add_assertion(
        name="semf_predicts_an_unbound_deuteron",
        computed=fmt(semf["2H"]), expected="-4.66", tolerance="0.5",
        unit="MeV, SEMF B(2H)",
        source=("a formula putting the deuteron below threshold cannot supply the "
                "standard for an A=2 pairing strength; the 25-40x refutation is "
                "WITHDRAWN"),
    )
    ok &= semf["2H"] < 0

    print("\n  compared against the quantity pairing actually has to explain:")
    defs = {}
    for nm, B3 in (("isospin_average", (T3 + He3) / 2), ("3H", T3)):
        d = B3 / 3 - D
        defs[nm] = d
        print(f"    {nm:<18} deuteron deficit = {mp.nstr(d,8)} MeV")
    print(f"    fitted pairing at A=2      0.208 - 0.338 MeV   <- SAME ORDER")
    print(f"    SEMF extrapolated to A=2   8.485 MeV           <- 17.8x the deficit")
    wb.add_data("deuteron_deficit", {k: fmt(v) for k, v in defs.items()})
    frac_lo = mp.mpf("0.208") / defs["3H"]
    frac_hi = mp.mpf("0.338") / defs["isospin_average"]
    print(f"\n  the fitted pairing covers roughly {mp.nstr(frac_lo*100,3)}-"
          f"{mp.nstr(frac_hi*100,3)}% of the deficit.")
    print("  PAIRING IS NOT REFUTED: sign derived, magnitude the right order.")
    wb.add_data("pairing_status_restored", {
        "previously": "refuted at 25-40x against the SEMF",
        "now": "live candidate -- sign derived, magnitude the right order",
        "fraction_of_deficit_covered": f"{fmt(frac_lo)}..{fmt(frac_hi)}",
    })

    # ---- what survives -----------------------------------------------------
    print("\nWHAT SURVIVES -- b3 IS the deuteron deficit\n")
    for nm, B3 in (("isospin_average", (T3 + He3) / 2), ("3H", T3)):
        b3 = B3 - 3 * D
        print(f"  {nm:<18} b3 = {mp.nstr(b3,9)}   3 x deficit = "
              f"{mp.nstr(3*defs[nm],9)}   identical")
        print(f"                     deuteron is {mp.nstr((1-D/(B3/3))*100,5)}% weaker "
              f"than b3 = 0 requires")
    print(f"\n  B/A: 2H {mp.nstr(D/2,7)}, 3H {mp.nstr(T3/3,7)}, 4He {mp.nstr(He4/4,7)}")
    print(f"  the deuteron sits {mp.nstr((T3/3)/(D/2),5)}x below A=3 and "
          f"{mp.nstr((He4/4)/(D/2),5)}x below 4He")
    wb.add_data("reframing", {
        "identity": "b3 = B(3) - 3B(2) = 3 * (B(3)/3 - B(2)) = 3 * deuteron deficit",
        "consequence": "the b3 question IS the deuteron-weakness question -- a "
                       "TWO-body anomaly dominating a connected three-body cumulant",
        "relocated_target": "derive the deuteron deficit, not b3; it has an "
                            "established cause (near-unitary 3S1, a_t = 5.42 fm "
                            "against a ~1.4 fm range; the unbound 1S0 virtual state)",
        "is_a_result": False,
        "why_not": "the identity is trivial; its value is moving the question to a "
                   "two-body quantity with known physics",
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
