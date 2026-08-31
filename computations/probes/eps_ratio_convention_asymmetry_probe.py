#!/usr/bin/env python3
"""eps_ratio_convention_asymmetry_probe.py

The two numbers qou-edt7 still calls open are NOT the same kind of object.

WHY THIS EXISTS
---------------
Bean qou-edt7's remaining question is stated as a pair:

    "Why eps(2)/eps(1) = 1.2137 (and eps(3)/eps(1) = 2.1200)."

They are quoted side by side, to comparable precision, as one open item. They
are not comparable. eps(z) ratios are w(z) ratios with

    w(1) = B(2)/1,  w(2) = B(3)/3,  w(3) = B(4)/6,

so eps(2)/eps(1) contains B(3) and eps(3)/eps(1) does not. B(3) is exactly where
this arc's convention systematic lives: there is no charge-symmetric A=3
binding, only the mirror pair 3H/3He split by 0.76375488 MeV, and which
combination represents "the" A=3 binding is a choice
(eps_ratio_target_precision_probe, 9.4% band). eps(3)/eps(1) = (B(4)/6)/B(2) is
built from A=2 and A=4 only and inherits none of it.

WHAT IS MEASURED
----------------
The same three A=3 conventions are pushed through BOTH ratios. The A=3 choice
moves one and is structurally incapable of moving the other, so the bands are
9.4% and identically 0.

WHY IT MATTERS -- the entropy consequence
-----------------------------------------
AGENTS.md gates closed-form matching on resolution: a match is evidence only if
the candidate space is small against the digits available. With a 9.4% band
eps(2)/eps(1) supplies log10(1/0.094) ~ 1.0 digits, so essentially no closed
form can be evidence for it -- an unbounded supply of expressions lands inside a
9% window. eps(3)/eps(1) is convention-free, so its resolution is set by AME
experimental uncertainty instead; the corpus states 0.8 eV on B(4He)
(ame_2020_binding_energies.py), i.e. ~2.8e-8 relative, so it supplies roughly
7 digits even before B(2)'s own uncertainty is counted.

So the two differ by ~6-7 orders of magnitude in how much evidence a match to
them could ever carry. A derivation should be aimed at eps(3)/eps(1), and a
candidate that hits eps(2)/eps(1) alone has demonstrated nearly nothing.

SCOPE
-----
Scope-(a) and deliberately small. This refutes nothing, derives nothing, and
proposes no mechanism. It re-prioritises the one axis qou-edt7 has left, and it
is a correction to how that bean states its own open question -- which I wrote.

NO FLOAT64: mpmath end to end at 65 dps; AME from the vendored table.
"""

import sys
from pathlib import Path

_R = Path(__file__).resolve().parents[1]
for _p in (str(_R), str(_R / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from substrate.codata_constants import ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 65


def fmt(x):
    return mp.nstr(mp.mpf(x), 30)


def main():
    wb = WitnessBuilder("eps-ratio-convention-asymmetry", engine="mpmath")
    wb.set_description(
        "qou-edt7 states its remaining open item as a PAIR -- eps(2)/eps(1) = "
        "1.2137 and eps(3)/eps(1) = 2.1200 -- but eps(2)/eps(1) contains B(3) "
        "and eps(3)/eps(1) does not. Pushing the three A=3 mirror conventions "
        "through both gives a 9.4% band on the first and identically 0 on the "
        "second, so they differ by ~6-7 orders of magnitude in the evidence a "
        "closed-form match could carry. Aim derivations at eps(3)/eps(1). "
        "Scope-(a): derives nothing, refutes nothing."
    )

    D = ame_binding_mev(1, 2)
    T3, He3, He4 = (ame_binding_mev(1, 3), ame_binding_mev(2, 3),
                    ame_binding_mev(2, 4))

    conventions = {
        "3He_alone": He3,
        "isospin_average": (T3 + He3) / 2,
        "3H_alone": T3,
    }

    print("AME2020 (vendored):")
    for lbl, v in (("B(2H)", D), ("B(3H)", T3), ("B(3He)", He3), ("B(4He)", He4)):
        print(f"   {lbl:8s} = {mp.nstr(v, 12)} MeV")
    print(f"\n   3H/3He mirror splitting = {mp.nstr(T3 - He3, 9)} MeV\n")

    r21, r31 = {}, {}
    for k, B3 in conventions.items():
        w1, w2, w3 = D, B3 / 3, He4 / 6
        r21[k] = w2 / w1
        r31[k] = w3 / w1

    def band(d):
        """Width normalised by the CENTRAL (isospin-average) reading.

        Normalisation matters and is easy to get wrong: dividing by the low end
        instead gives 9.8957% for the same band. eps_ratio_target_precision
        quotes 9.4292%, normalised by the central value, and this reproduces
        that rather than introducing a second figure for one quantity.
        """
        lo, hi = min(d.values()), max(d.values())
        return lo, hi, (hi - lo) / d["isospin_average"]

    lo21, hi21, wid21 = band(r21)
    lo31, hi31, wid31 = band(r31)

    print("eps(2)/eps(1)  -- contains B(3)")
    for k, v in r21.items():
        print(f"   {k:18s} {mp.nstr(v, 10)}")
    print(f"   band width = {mp.nstr(wid21 * 100, 5)} %\n")

    print("eps(3)/eps(1)  -- built from A=2 and A=4 only")
    for k, v in r31.items():
        print(f"   {k:18s} {mp.nstr(v, 12)}")
    print(f"   band width = {mp.nstr(wid31 * 100, 5)} %\n")

    wb.add_data("ame_inputs_mev", {
        "B_2H": fmt(D), "B_3H": fmt(T3), "B_3He": fmt(He3), "B_4He": fmt(He4),
        "mirror_splitting": fmt(T3 - He3),
    })
    wb.add_data("eps2_over_eps1_by_convention", {k: fmt(v) for k, v in r21.items()})
    wb.add_data("eps3_over_eps1_by_convention", {k: fmt(v) for k, v in r31.items()})

    ok = True

    # 1. the banded one
    wb.add_assertion(
        name="eps2_ratio_carries_the_A3_convention_band",
        computed=fmt(wid21), expected="0.0942916716", tolerance="1e-8",
        unit="fractional band width",
        source=("three readings of 'the' A=3 binding (3He alone / isospin "
                "average / 3H alone), width normalised by the central "
                "reading; reproduces eps_ratio_target_precision's 9.4292% "
                "exactly. Normalising by the low end instead gives 9.8957% "
                "for the SAME band -- a normalisation difference, not a "
                "discrepancy"),
    )
    if abs(wid21 - mp.mpf("0.094")) > mp.mpf("0.002"):
        ok = False
        print("   FAIL: eps2 band not ~9.4%")

    # 2. the convention-free one -- exactly zero, not merely small
    wb.add_assertion(
        name="eps3_ratio_is_exactly_convention_free",
        computed=fmt(wid31), expected="0", tolerance="0",
        unit="fractional band width",
        source=("(B(4)/6)/B(2) contains no A=3 quantity, so the mirror "
                "convention cannot enter -- structural, not numerical"),
    )
    if wid31 != 0:
        ok = False
        print("   FAIL: eps3 band is not identically zero")

    # 3. the consequence, as digits
    digits21 = -mp.log10(wid21)
    b4_rel = mp.mpf("0.8") / (He4 * mp.mpf("1e6"))   # 0.8 eV on B(4He), in MeV
    digits31 = -mp.log10(b4_rel)
    print(f"digits available:  eps(2)/eps(1) ~ {mp.nstr(digits21, 3)}"
          f"   eps(3)/eps(1) ~ {mp.nstr(digits31, 3)}")
    print(f"   ratio of evidential capacity ~ 10^{mp.nstr(digits31 - digits21, 3)}")

    wb.add_data("digits_available", {
        "eps2_over_eps1": fmt(digits21),
        "eps3_over_eps1_from_AME_uncertainty": fmt(digits31),
        "note": ("eps3 figure uses the 0.8 eV AME uncertainty on B(4He) stated "
                 "in ame_2020_binding_energies.py; B(2H)'s own uncertainty is "
                 "not counted, so it is a LOWER bound on the digits available"),
    })
    wb.add_assertion(
        name="eps2_supplies_about_one_digit",
        computed=fmt(digits21), expected="1.0255", tolerance="0.001",
        unit="significant digits",
        source=("-log10(band width); with ~1 digit no closed form can be "
                "evidence -- the candidate space is unbounded"),
    )
    if abs(digits21 - mp.mpf("1.03")) > mp.mpf("0.05"):
        ok = False
        print("   FAIL: eps2 digit count off")

    print("\n" + ("  OK" if ok else "  FAILURES"))
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
