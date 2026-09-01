#!/usr/bin/env python3
"""Is the kappa(A) unreachability verdict independent of the separation law?

Bean qou-17mq (ROAST of that bean's own finding 2, by finding 3).

THE QUESTION
============
qou-17mq's finding 2 concludes, flatly, that

  "SATURATION BEGINS PAST THE END OF THE NUCLEAR CHART ... the
   discriminating regime is unreachable in any nucleus"

and computes the required A from alpha = c * A^(1/3).  Three sections later
in the SAME bean, finding 3 calls that exponent "an unexamined Euclidean
import" fed into a hyperbolic-by-construction kernel -- "two geometries in
one quantity" -- and reports that hyperbolic self-consistency (V ~ A in H^3
gives R ~ (1/2) ln(2V/pi)) requires alpha ~ ln A instead.

So finding 3 is UPSTREAM of finding 2, and the bean's "NET OF ALL THREE"
presents them as independent and cumulative.  This probe asks whether
finding 2's verdict survives the input finding 3 questions.

WHAT IT DOES
============
Nothing is fitted and no hypothesis is scored.  For each of the four
separation laws finding 3 itself tabulates, the single scale c is anchored
so that alpha reproduces the committed value at the top of the measured
span -- the same anchoring finding 2 used -- and the A required to reach
each saturation threshold is solved for.

  law            provenance
  A^(1/3)        the Euclidean nuclear radius law, as used by finding 2
  A^(1/4)        finding 3's tabulated alternative
  ln A           the hyperbolic self-consistent law finding 3 derives
  A^(1/2)        finding 3's tabulated alternative

Inputs (alpha_max, A_max, the scale, the heaviest nuclide) are read from
the committed witness of the probe being checked, so the first row must
reproduce that probe's published 334 / 606 / 1764 or this probe is wrong.

WHAT IT IS NOT
==============
This is a robustness check on ONE claim's law-dependence.  It is not a
scoring of the laws (finding 3 already did that: 3.505 / 6.358 / 9.253 /
13.95 percent scatter, Euclidean best), not a refutation of H_coth, and not
a claim that the discrimination test can be run.  Scope (a).
"""

from __future__ import annotations

import json
import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf, acoth, log, findroot  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
UPSTREAM = HERE / "em-linking-kappa-regime-reachability.witness.json"

LAWS = {
    "A^(1/3)": ("Euclidean nuclear radius law, as used by finding 2",
                lambda A: A ** (mpf(1) / 3)),
    "A^(1/4)": ("finding 3's tabulated alternative",
                lambda A: A ** (mpf(1) / 4)),
    "ln A": ("hyperbolic self-consistent (V ~ A in H^3 => R ~ ln)",
             lambda A: log(A)),
    "A^(1/2)": ("finding 3's tabulated alternative",
                lambda A: A ** (mpf(1) / 2)),
}

TOLERANCES = {"10pct": mpf("1.10"), "5pct": mpf("1.05"), "1pct": mpf("1.01")}


def main() -> None:
    up = json.loads(UPSTREAM.read_text())
    span = up["data"]["alpha_range_spanned"]
    alpha_max = mpf(span["alpha_max"])
    A_max = mpf(span["A_max"])
    heaviest = mpf(up["data"]["saturation_onset"]["heaviest_known_nuclide_A"])

    thresholds = {k: acoth(v) for k, v in TOLERANCES.items()}

    rows = {}
    for name, (why, f) in LAWS.items():
        c = alpha_max / f(A_max)
        entry = {"scale_c": mp.nstr(c, 10), "provenance": why, "required_A": {}}
        for tol, a_req in thresholds.items():
            A = findroot(lambda A: c * f(A) - a_req, mpf(300))
            entry["required_A"][tol] = {
                "A": mp.nstr(A, 10),
                "reachable_in_the_nuclear_chart": bool(A <= heaviest),
            }
        rows[name] = entry

    euclid = rows["A^(1/3)"]["required_A"]
    published = {"10pct": 334, "5pct": 606, "1pct": 1764}
    reproduces = all(
        abs(mpf(euclid[k]["A"]) - mpf(published[k])) < mpf(1)
        for k in published)

    hyperbolic_still_unreachable = not rows["ln A"]["required_A"]["10pct"][
        "reachable_in_the_nuclear_chart"]
    any_law_reachable = [
        name for name, e in rows.items()
        if e["required_A"]["10pct"]["reachable_in_the_nuclear_chart"]]

    verdict = (
        "Finding 2's verdict is NOT law-independent, and the bean states it "
        "flatly. It holds under the law the data prefers (A^(1/3), required "
        f"A = {euclid['10pct']['A']}) and is STRENGTHENED under the law the "
        "hyperbolic geometry requires (ln A, required A = "
        f"{rows['ln A']['required_A']['10pct']['A']}), but FAILS under "
        f"A^(1/2) (required A = "
        f"{rows['A^(1/2)']['required_A']['10pct']['A']} <= {mp.nstr(heaviest,4)}), "
        "which is one of the four laws finding 3 itself tabulates. A^(1/2) "
        "scores worst on scatter (13.95% vs 3.505%), so this is not a live "
        "threat -- but that defence is a FIT argument, and finding 3's point "
        "is that the fit and the geometry disagree about which law is right. "
        "Scope (a): a conditionality the bean does not flag, not a refutation.")

    wb = WitnessBuilder("em-linking-reachability-law-sensitivity",
                        engine="mpmath")
    wb.set_description(
        "Roast of qou-17mq finding 2 by qou-17mq finding 3: the "
        "'saturation is unreachable' verdict is recomputed under each of "
        "the four separation laws finding 3 tabulates, anchoring the "
        "single scale at the committed alpha_max. Reproduces the published "
        "334/606/1764 for the Euclidean law before departing from it. "
        "Nothing fitted, nothing scored; scope (a) on a conditionality the "
        "bean does not flag.")
    wb.add_data("alpha_thresholds",
                {k: mp.nstr(v, 10) for k, v in thresholds.items()})
    wb.add_data("required_A_by_separation_law", rows)
    wb.add_data("heaviest_known_nuclide_A", int(heaviest))
    wb.add_data("upstream_witness", UPSTREAM.name)
    wb.add_data("verdict", verdict)

    wb.add_assertion(
        name="reproduces_the_published_euclidean_figures",
        computed=1 if reproduces else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"A^(1/3) requires A = {euclid['10pct']['A']} / "
                f"{euclid['5pct']['A']} / {euclid['1pct']['A']} against the "
                "published 334 / 606 / 1764. A probe that did not reproduce "
                "them would be measuring its own method."))
    wb.add_assertion(
        name="hyperbolic_law_strengthens_the_unreachability",
        computed=1 if hyperbolic_still_unreachable else 0, expected=1,
        tolerance=0, unit="boolean",
        source=(f"Under ln A the 10% regime needs A = "
                f"{rows['ln A']['required_A']['10pct']['A']}, further out "
                f"than the Euclidean {euclid['10pct']['A']}. The conclusion "
                "survives the input finding 3 questions."))
    wb.add_assertion(
        name="verdict_is_not_law_independent",
        computed=1 if any_law_reachable else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"Reachable under: {', '.join(any_law_reachable)}. The bean "
                "states unreachability without qualification."))
    out = wb.save()

    print(f"alpha_max = {mp.nstr(alpha_max, 10)} at A = {int(A_max)}  "
          f"(from {UPSTREAM.name})")
    print(f"heaviest known nuclide A = {int(heaviest)}\n")
    print(f"{'law':<10} {'scale c':<12} " +
          "  ".join(f"{t:>12}" for t in TOLERANCES))
    for name, e in rows.items():
        cells = []
        for t in TOLERANCES:
            r = e["required_A"][t]
            mark = "*" if r["reachable_in_the_nuclear_chart"] else " "
            cells.append(f"{r['A'][:10]:>11}{mark}")
        print(f"{name:<10} {e['scale_c'][:11]:<12} " + "  ".join(cells))
    print("\n* = inside the nuclear chart\n")
    print(f"verdict:\n{verdict}")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
