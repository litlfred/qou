#!/usr/bin/env python3
"""Dehornoy floors of the corpus's braids, by handle reduction.

Bean qou-qpj9. Closes the step
docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md left open:
that audit compared exponent sums as a SCALE INDICATOR and said plainly that
the floors were not computed and that handle reduction was the honest next
step. This runs it.

WHY IT MATTERS
==============
Ito's Theorem 2 (library/arxiv-0805.1447v2) makes the Nielsen-Thurston type of
a braid decide the geometry of its closure -- pseudo-Anosov <=> hyperbolic --
but ONLY under the hypothesis [beta]_D >= 3. Without a floor computation the
hypothesis cannot be checked, so the criterion cannot be applied to anything.

METHOD
======
Dehornoy handle reduction (_dehornoy.py), which decides sigma-positivity and
hence the Dehornoy ordering; the floor is then read off Definition 1 directly:
the minimal m >= 0 with Delta^{-2m-2} < beta < Delta^{2m+2}.

VALIDATED BEFORE USE against all three values Ito states himself, including the
conjugation pair he uses to show the floor is NOT a conjugacy invariant:

    (s1 s2)^4          -> 1
    Delta^2 s1 s2^-1   -> 1
    Delta^2 s2 s1^-1   -> 0     (conjugate to the previous, different floor)

A run that fails any of those asserts rather than reporting.

EXPLORATORY / audit-only. Integer arithmetic only -- no floats anywhere, so
the precision gates are vacuous here by construction rather than by exemption.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402

from _dehornoy import dehornoy_floor, DELTA2  # noqa: E402

# Ito's own stated values -- the validation gate.
ITO_CHECKS = [
    ("(s1 s2)^4", [1, 2] * 4, 1),
    ("Delta^2 s1 s2^-1", [1, 2, 1, 2, 1, 2, 1, -2], 1),
    ("Delta^2 s2 s1^-1", [1, 2, 1, 2, 1, 2, 2, -1], 0),
]

CORPUS = [
    ("meson M = (s1 s2)^2 s2 s1", "def:categorical-meson", [1, 2, 1, 2, 2, 1]),
    ("figure-eight (s1 s2^-1)^2", "muon carrier, Vol 2.0299", [1, -2, 1, -2]),
    ("Borromean (s1 s2^-1)^3", "proton carrier, Vol 7.3277", [1, -2, 1, -2, 1, -2]),
    ("trefoil s1^3", "-", [1, 1, 1]),
    ("T(2,5) s1^5", "the meson braid's closure", [1] * 5),
]

SCALE = [(f"Delta^{2*k} = (s1 s2)^{3*k}", [1, 2] * (3 * k)) for k in range(1, 5)]


def main() -> None:
    # --- validate before trusting anything -----------------------------
    validation = []
    for name, w, expect in ITO_CHECKS:
        got = dehornoy_floor(w)
        validation.append({"braid": name, "computed": got, "ito_states": expect,
                           "agrees": got == expect})
        assert got == expect, f"validation failed on {name}: {got} != {expect}"

    corpus = [{"braid": n, "role": r, "crossings": len(w),
               "dehornoy_floor": dehornoy_floor(w),
               "ito_thm2_applies": bool((dehornoy_floor(w) or 0) >= 3)}
              for n, r, w in CORPUS]
    scale = [{"braid": n, "crossings": len(w), "dehornoy_floor": dehornoy_floor(w)}
             for n, w in SCALE]

    first = next((s for s in scale if (s["dehornoy_floor"] or 0) >= 3), None)
    max_corpus = max(c["dehornoy_floor"] or 0 for c in corpus)

    wb = WitnessBuilder("meson-braid-dehornoy-floor", engine="python-exact")
    wb.set_description(
        "Dehornoy floors of the corpus's braid words, computed by handle "
        "reduction, so that Ito's Theorem 2 hypothesis [beta]_D >= 3 can "
        "actually be checked rather than estimated. Validated against all "
        "three values Ito states himself before use. Integer arithmetic "
        "throughout.")
    wb.add_data("validation_against_ito", validation)
    wb.add_data("corpus_floors", corpus)
    wb.add_data("scale_delta_powers", scale)
    wb.add_data("threshold", {
        "first_power_reaching_floor_3": None if first is None else first["braid"],
        "crossings_required": None if first is None else first["crossings"],
        "max_floor_among_corpus_braids": max_corpus,
    })
    wb.add_data("corrects_prior_estimate", {
        "where": "docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md",
        "prior_claim": ("[beta]_D >= 3 'means clearing Delta^8 = (s1 s2)^12 -- "
                        "24 crossings'."),
        "computed": ("Delta^6 = (s1 s2)^9 already HAS floor 3, so the "
                     "threshold is 18 crossings, not 24."),
        "why_the_estimate_was_wrong": ("I read Definition 1's interval bound "
                                       "Delta^{2m+2} at m = 3 as the braid "
                                       "that must be cleared. It is the "
                                       "bracketing power, not the smallest "
                                       "braid of that floor. The conclusion "
                                       "is unchanged in direction and the "
                                       "margin is still wide -- 18 against a "
                                       "corpus maximum of 6 crossings -- but "
                                       "the number was mine, not measured, "
                                       "and it was wrong."),
    })
    wb.add_data("resolves_the_contradiction", {
        "what": ("The Ito audit inferred that the corpus meson braid must "
                 "have [beta]_D < 3, because it is pseudo-Anosov (|tr| = 3 "
                 "in PSL(2,Z)) yet its closure was MEASURED as T(2,5) with "
                 "Vol = 0 -- which Theorem 2 forbids."),
        "now_computed": ("[M]_D = 1. The inference was right and is now a "
                         "computation."),
    })
    wb.add_data("scope", {
        "class": "(a) a hypothesis check, not a result about any meson",
        "claimed": ("No braid word the corpus currently uses satisfies Ito's "
                    "hypothesis; the maximum floor among them is "
                    f"{max_corpus}, against a required 3."),
        "NOT_claimed": ("That a candidate cannot exist, that longer braids "
                        "work, or anything about the mass law. Obstruction A "
                        "is untouched. The floor is also NOT a conjugacy "
                        "invariant (Ito's own example, reproduced in the "
                        "validation above), so these are statements about "
                        "these WORDS, not about the link types they close "
                        "to."),
    })
    verdict = (
        f"Computed rather than estimated. Corpus floors: meson 1, muon 0, "
        f"proton 0, trefoil 0, T(2,5) 0 -- maximum {max_corpus} against Ito's "
        f"required 3. The threshold is first reached at "
        f"{first['braid'] if first else 'n/a'}, "
        f"{first['crossings'] if first else 'n/a'} crossings, which CORRECTS "
        f"the prior audit's estimate of 24. [M]_D = 1 also turns the audit's "
        f"inferred resolution of the pseudo-Anosov/T(2,5) contradiction into "
        f"a computed one. Nothing derived; Obstruction A open.")
    wb.add_data("verdict", verdict)
    wb.set_audit_only(
        "docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md")

    wb.add_assertion(
        name="reproduces_all_three_ito_stated_floors",
        computed=sum(1 for v in validation if v["agrees"]), expected=3,
        tolerance=0, unit="count",
        source=("Includes the conjugation pair Ito uses to show the floor is "
                "not a conjugacy invariant, so the implementation is pinned "
                "on the subtle case and not only the easy one."))
    wb.add_assertion(
        name="no_corpus_braid_meets_ito_hypothesis",
        computed=sum(1 for c in corpus if c["ito_thm2_applies"]), expected=0,
        tolerance=0, unit="count",
        source=f"Maximum corpus floor is {max_corpus}; Theorem 2 needs >= 3.")
    wb.add_assertion(
        name="threshold_is_18_crossings_not_24",
        computed=first["crossings"] if first else -1, expected=18, tolerance=0,
        unit="crossings",
        source=("Delta^6 = (s1 s2)^9 has floor 3. The prior audit estimated "
                "24 by misreading the bracketing power as the required "
                "braid."))
    out = wb.save()

    print("validation against Ito's own values:")
    for v in validation:
        print(f"  {'OK ' if v['agrees'] else 'FAIL'} {v['braid']:20} "
              f"-> {v['computed']} (states {v['ito_states']})")
    print(f"\n{'braid':32} {'cross':>6} {'floor':>6}  Thm 2?")
    for c in corpus:
        print(f"{c['braid']:32} {c['crossings']:>6} "
              f"{str(c['dehornoy_floor']):>6}  "
              f"{'YES' if c['ito_thm2_applies'] else 'no'}")
    print()
    for s in scale:
        print(f"{s['braid']:32} {s['crossings']:>6} "
              f"{str(s['dehornoy_floor']):>6}")
    print(f"\n{verdict}\n\nwitness -> {out}")


if __name__ == "__main__":
    main()
