#!/usr/bin/env python3
"""binding_magnitude_is_not_validatable_probe.py

The missing binding magnitude cannot be VALIDATED from AME light nuclei --
at any order of the cumulant tower. This is a property of the target.

WHY THIS EXISTS
---------------
qou-edt7's original question is to derive, in closed form, the magnitude of the
super-pairwise extensive term in the binding formula. Six ansaetze failed on the
deuteron; every attempt since has failed too. This probe asks a prior question
nobody has asked: HOW MUCH EVIDENCE could any closed form carry if it were
found?

AGENTS.md gates closed-form matching on resolution -- a match is evidence only
if the candidate space is small against the digits available. So the target's
own resolution decides whether the question is answerable, before any mechanism
is proposed.

WHAT IS MEASURED
----------------
The tower b3..b7 is computed from B(A) for A = 2..7 under ALL 27 combinations of
the three mirror conventions that exist in this range -- A=3 (3H/3He), A=5
(5He/5Li), A=7 (7Li/7Be). A=4 and A=6 are N=Z self-conjugate and have no mirror.
Prior work in this arc varied only A=3, which understates the band.

RESULTS

1. Every magnitude is determined to UNDER ONE significant digit:

       b3   53.6% band   0.271 digits
       b4   33.1%        0.481
       b5   15.9%        0.799
       b6   13.6%        0.865   <- the best in the tower
       b7   14.5%        0.838

2. The quantity this arc has actually been scoring candidates against is the
   WORST of all: b4/b3 spans 4.267 .. 10.314, a 93.3% band = 0.030 digits. It
   is not known to one significant figure; it ranges over a factor of 2.4.

3. Resolution IMPROVES with order, inverting where the arc has looked. The best
   determined quantity in the entire tower is b7/b6 = 2.2468 +- 5.0%
   (1.305 digits), and nothing in the corpus has ever looked at it.

4. The one convention-INVARIANT feature is the sign pattern: all 27 combinations
   give (+,+,-,+,-), and no interval straddles zero. It is PARTLY generic, and
   the part that is not is worth having. Of five arbitrary peaked functions with
   no nuclear input, 2 reproduce it (lorentzian, asymmetric exponential) and 3
   do not, and the misses are systematic rather than random:

     - linear-in-|z-3| and triangle have a LINEAR rising side, so w(1), w(2),
       w(3) are in arithmetic progression and b4 = w(3) - 2w(2) + w(1) is
       EXACTLY zero (measured -2.8e-65 and 0.0);
     - the gaussian is CONCAVE near its peak, giving b4 < 0.

   So the pattern's whole discriminating content is one fact: **w is convex on
   the rise to the peak.** Everything else about it follows from being peaked at
   z=3 and decaying. That is a real constraint on any mechanism and a weak one --
   it is a sign condition, not a magnitude.

   (Recorded because I first counted 4 of 6 here. That count read the sign of
   b4 = -2.8e-65 -- numerical noise around an exact zero -- as a hit. The
   corrected count is 2 of 5, and the correction IMPROVES the finding: the
   invariance is less generic than I first reported, for a statable reason.)

CONCLUSION -- scope-(a), and it is about the DATA
-------------------------------------------------
Maximum evidence available anywhere in the tower is ~1.3 digits, on one ratio,
and the qualitative structure is generic. Under the entropy discipline, a closed
form agreeing to ~1 digit is not evidence however motivated it is: the space of
expressions landing inside a 13-50% window is unbounded.

So the six failures are not six pieces of bad luck. The target cannot
discriminate. This does NOT say the magnitude has no closed form, and it refutes
no mechanism -- it says AME light-nucleus binding is the wrong observable to
test one against, and that effort should go to finding an observable with
resolution rather than to a seventh ansatz.

NO FLOAT64: mpmath end to end at 65 dps; AME from the vendored table.
"""

import itertools
import sys
from math import comb
from pathlib import Path

_R = Path(__file__).resolve().parents[1]
for _p in (str(_R), str(_R / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from substrate.codata_constants import ame_binding_mev as B  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 65


def fmt(x):
    return mp.nstr(mp.mpf(x), 30)


def fwd(v, k):
    return sum((-1) ** (k - i) * comb(k, i) * v[i] for i in range(k + 1))


def tower(Bs):
    w = [Bs[A] / comb(A, 2) for A in range(2, 8)]
    return [comb(n, 2) * fwd(w, n - 2) for n in range(3, 8)]


def main():
    wb = WitnessBuilder("binding-magnitude-is-not-validatable", engine="mpmath")
    wb.set_description(
        "The missing super-pairwise binding magnitude cannot be VALIDATED from "
        "AME light nuclei at any order: over all 27 mirror-convention "
        "combinations every cumulant b3..b7 is determined to under one "
        "significant digit (best b6, 0.865), and b4/b3 -- the quantity this arc "
        "scores candidates against -- to 0.030 digits (93.3% band, a factor of "
        "2.4). The one convention-invariant feature, the (+,+,-,+,-) sign "
        "pattern, is mostly generic -- 2 of 5 arbitrary peaked functions "
        "reproduce it -- and its whole discriminating content is that w is "
        "CONVEX on the rise to the peak, a sign condition not a magnitude. "
        "Scope-(a) and about the DATA, not the framework: it refutes no "
        "mechanism, and says AME light-nucleus binding is the wrong observable "
        "to test one against."
    )

    D, He4, Li6 = B(1, 2), B(2, 4), B(3, 6)
    m3 = [B(2, 3), (B(1, 3) + B(2, 3)) / 2, B(1, 3)]
    m5 = [B(3, 5), (B(3, 5) + B(2, 5)) / 2, B(2, 5)]
    m7 = [B(4, 7), (B(3, 7) + B(4, 7)) / 2, B(3, 7)]

    rows = []
    for a, b, c in itertools.product(m3, m5, m7):
        rows.append(tower({2: D, 3: a, 4: He4, 5: b, 6: Li6, 7: c}))
    central = tower({2: D, 3: m3[1], 4: He4, 5: m5[1], 6: Li6, 7: m7[1]})

    labels = ["b3", "b4", "b5", "b6", "b7"]
    ok = True

    print("cumulant   central        band %     digits   sign fixed?")
    bands = {}
    for i, lab in enumerate(labels):
        v = [r[i] for r in rows]
        lo, hi = min(v), max(v)
        band = (hi - lo) / abs(central[i])
        digits = -mp.log10(band)
        bands[lab] = (central[i], lo, hi, band, digits)
        fixed = "yes" if (lo > 0 or hi < 0) else "NO"
        print(f"  {lab:4s}  {mp.nstr(central[i],8):>12s} {mp.nstr(band*100,5):>9s} "
              f"{mp.nstr(digits,4):>10s}   {fixed}")
        if digits >= 1:
            ok = False
            print(f"     UNEXPECTED: {lab} carries >= 1 digit")

    wb.add_data("tower_convention_bands", {
        k: {"central": fmt(c), "min": fmt(lo), "max": fmt(hi),
            "band_fraction": fmt(bd), "digits": fmt(dg)}
        for k, (c, lo, hi, bd, dg) in bands.items()})

    wb.add_assertion(
        name="every_cumulant_under_one_significant_digit",
        computed=fmt(max(v[4] for v in bands.values())),
        expected="0.865", tolerance="0.01", unit="significant digits (the best)",
        source=("27 mirror-convention combinations, A=3/5/7; A=4 and A=6 are "
                "N=Z self-conjugate. Best is b6 at 0.865 digits"))
    if abs(max(v[4] for v in bands.values()) - mp.mpf("0.865")) > mp.mpf("0.01"):
        ok = False
        print("   FAIL: best-digit figure moved")

    # the quantity the arc actually scores against
    r43 = [abs(r[1] / r[0]) for r in rows]
    lo, hi = min(r43), max(r43)
    cen43 = abs(central[1] / central[0])
    band43 = (hi - lo) / cen43
    print(f"\nb4/b3 -- what this arc scores candidates against:")
    print(f"   {mp.nstr(lo,7)} .. {mp.nstr(hi,7)}   band {mp.nstr(band43*100,5)} % "
          f"= {mp.nstr(-mp.log10(band43),4)} digits")
    wb.add_data("b4_over_b3", {"central": fmt(cen43), "min": fmt(lo),
                               "max": fmt(hi), "band_fraction": fmt(band43),
                               "digits": fmt(-mp.log10(band43))})
    wb.add_assertion(
        name="scoring_quantity_carries_essentially_no_digits",
        computed=fmt(-mp.log10(band43)), expected="0.0302", tolerance="0.002",
        unit="significant digits",
        source="b4/b3 spans 4.267..10.314 over the 27 combinations")
    if abs(-mp.log10(band43) - mp.mpf("0.0302")) > mp.mpf("0.002"):
        ok = False
        print("   FAIL: b4/b3 digit count moved")

    # best-resolved quantity in the tower
    r76 = [abs(r[4] / r[3]) for r in rows]
    lo7, hi7 = min(r76), max(r76)
    cen76 = abs(central[4] / central[3])
    band76 = (hi7 - lo7) / cen76
    print(f"b7/b6 -- the BEST resolved quantity in the tower:")
    print(f"   central {mp.nstr(cen76,7)}   band {mp.nstr(band76*100,5)} % "
          f"= {mp.nstr(-mp.log10(band76),4)} digits")
    wb.add_data("b7_over_b6", {"central": fmt(cen76), "band_fraction": fmt(band76),
                               "digits": fmt(-mp.log10(band76)),
                               "note": "nothing in the corpus has looked at this"})

    # sign pattern: invariant, but generic
    patterns = set(tuple("+" if x > 0 else "-" for x in r) for r in rows)
    print(f"\nsign patterns over 27 combinations: {len(patterns)} -> {patterns}")
    wb.add_assertion(
        name="sign_pattern_is_convention_invariant",
        computed=str(len(patterns)), expected="1", tolerance="0",
        unit="distinct sign patterns",
        source="all 27 give (+,+,-,+,-); no interval straddles zero")
    if len(patterns) != 1:
        ok = False
        print("   FAIL: sign pattern not invariant")

    generic = {
        "lorentzian_peak_z3": [1 / (1 + (z - 3) ** 2) for z in range(1, 7)],
        "linear_peak_z3": [mp.mpf(3) - abs(z - 3) * mp.mpf("0.7") for z in range(1, 7)],
        "asym_exponential": [mp.e ** (-abs(z - 3) * mp.mpf("0.8")) for z in range(1, 7)],
        "gaussian_peak_z3": [mp.e ** (-((z - 3) ** 2) / 2) for z in range(1, 7)],
        "triangle_peak_z3": [mp.mpf(max(0, 3 - abs(z - 3))) for z in range(1, 7)],
    }
    target = ("+", "+", "-", "+", "-")
    hits = {}
    for k, w in generic.items():
        p = tuple("+" if comb(n, 2) * fwd(w, n - 2) > 0 else "-" for n in range(3, 8))
        hits[k] = (p == target)
    n_hit = sum(hits.values())
    print(f"generic peaked functions reproducing it: {n_hit}/{len(generic)} -> "
          f"{[k for k,v in hits.items() if v]}")
    # why the misses miss: b4 = w(3) - 2w(2) + w(1) is the convexity of the rise
    b4s = {k: comb(4, 2) * fwd(w, 2) for k, w in generic.items()}
    print("   b4 (convexity of the rise) per candidate:")
    for k, v in b4s.items():
        print(f"     {k:22s} {mp.nstr(v, 6):>14s}  "
              f"{'convex' if v > 0 else ('LINEAR (exactly 0)' if abs(v) < mp.mpf('1e-40') else 'concave')}")
    wb.add_data("why_the_misses_miss", {k: fmt(v) for k, v in b4s.items()})
    wb.add_data("sign_pattern_genericity", {k: str(v) for k, v in hits.items()})
    wb.add_assertion(
        name="sign_pattern_is_generic_not_informative",
        computed=str(n_hit), expected="2", tolerance="0",
        unit="of 5 arbitrary peaked functions with no nuclear input",
        source=("2 of 5 reproduce it; the 3 misses are systematic -- linear and "
                "triangle have a linear rise so b4 is EXACTLY 0, the gaussian "
                "is concave so b4 < 0. The pattern's whole content is that w is "
                "CONVEX on the rise: a sign condition, not a magnitude"))
    if n_hit != 2:
        ok = False
        print(f"   FAIL: genericity count is {n_hit}, expected 3")

    print("\n" + ("  OK" if ok else "  FAILURES"))
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
