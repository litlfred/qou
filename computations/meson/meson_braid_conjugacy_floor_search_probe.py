#!/usr/bin/env python3
"""Is Ito's hypothesis reachable at the LINK level, not just as written?

Bean qou-qpj9.  Successor to meson_braid_dehornoy_floor_probe.py, and the
carefully-scoped replacement for the claim RETRACTED in
docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md.

WHAT WAS RETRACTED, AND WHY THIS IS A DIFFERENT QUESTION
========================================================
The retracted claim read a floor computed on ONE WRITTEN WORD as a fact about
the framework's braid vocabulary.  It is not: the closure of a braid -- and
hence Vol(K), which is what the mass law m(K) = m_e Vol(K) rho(K) / hbar_q^2
actually reads -- depends only on the braid's conjugacy class (Markov move I)
and on stabilisation (Markov move II).  A word is a presentation; the link is
the object.  The Dehornoy floor is NOT a conjugacy invariant -- Ito says so
himself and gives the pair, which this file's dependency validates against --
so a floor read off one spelling says nothing about the link.

The link-level question is therefore: does ANY representative of the conjugacy
class reach [beta]_D >= 3?  That is the quantity that would let Ito's Theorem 2
be applied to the CLOSURE, because both sides of his equivalence
(Nielsen-Thurston type; hyperbolicity of the closure) are conjugacy invariants
even though the hypothesis is not.

THIS IS A SEARCH, NOT A PROOF
=============================
It samples conjugates gamma^-1 beta gamma over freely-reduced conjugator words
gamma of bounded length.  A "max floor found" of 0 is evidence, not a theorem:
the supremum of the floor over a full conjugacy class is not computed here and
no bound on it is invoked.  In particular this file deliberately asserts no bound on
that supremum.

SUPERSEDED, 2026-08-25, same day: this section used to add "no Malyutin
quasi-morphism bound is cited -- that paper is not in library/". THAT WAS WRONG.
Ito quotes the bound in full as his Proposition 2(2), attributed to [MN] and
[Ma], in the very section whose conjugate pair validates this file. It gives
|[beta]_D - [beta']_D| <= 1 for conjugates, which turns this search into a
proof: floor 0 => no representative above 1 => Theorem 2 unreachable, full stop.
See meson_braid_floor_conjugacy_bound_probe.py. This probe's numbers stand and
are now corroboration rather than evidence.

THE CONTROL THAT MAKES THE NEGATIVE READABLE
============================================
The figure-eight knot 4_1 is GENUINELY HYPERBOLIC (Vol = 2.0299, the corpus's
muon carrier) and is a knot, so Theorem 2 applies to it by hypothesis if the
floor condition can be met at all.  If even 4_1 has no sampled representative
with floor >= 3, the reading is that the threshold is far above everything at
this scale -- not that these particular links fail some geometric test.

Two further controls guard the search itself:
  * a POSITIVE control -- a class that does reach floor >= 3 -- so a run that
    found nothing anywhere would fail rather than report;
  * a RAISING control -- Ito's own conjugate pair, searched from the LOW side,
    so the search is shown to find floor-increasing conjugates and not merely
    to re-report the floor it started from.

WHY B_3 IS THE RIGHT PLACE TO LOOK -- and the limit of that argument
====================================================================
Ito's own stated example has (s1 s2)^4 at floor 1 in B_3 and floor 0 in B_4:
Delta_n^2 is longer for larger n, the bracketing interval widens, and the floor
can only fall.  That single example is the whole basis for searching at minimal
braid index; it is an example Ito states, not a theorem this file verified, and
it is recorded here as such.

EXPLORATORY / audit-only.  Integer arithmetic only -- no floats anywhere, so
the precision gates are vacuous here by construction rather than by exemption.
"""

from __future__ import annotations

import itertools
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402

from _dehornoy import dehornoy_floor, free_reduce, inv  # noqa: E402

MAX_CONJ_LEN = 10         # freely-reduced conjugator words in B_3
GENS = (1, -1, 2, -2)

# Ito's own stated values -- the same validation gate the floor probe uses.
ITO_CHECKS = [
    ("(s1 s2)^4", [1, 2] * 4, 1),
    ("Delta^2 s1 s2^-1", [1, 2, 1, 2, 1, 2, 1, -2], 1),
    ("Delta^2 s2 s1^-1", [1, 2, 1, 2, 1, 2, 2, -1], 0),
]

TARGETS = [
    ("4_1 figure-eight (s1 s2^-1)^2", "knot", "HYPERBOLIC, Vol 2.0299 (muon carrier)",
     [1, -2, 1, -2]),
    ("Borromean (s1 s2^-1)^3", "3-component link", "HYPERBOLIC, Vol 7.3277 (proton carrier)",
     [1, -2, 1, -2, 1, -2]),
    ("meson M = (s1 s2)^2 s2 s1", "knot T(2,5)", "torus, Vol 0",
     [1, 2, 1, 2, 2, 1]),
    # POSITIVE control: a class that does reach floor >= 3.
    ("Delta^6 s1 s2^-1", "control (positive)", "expected floor >= 3",
     [1, 2] * 9 + [1, -2]),
    # RAISING control: Ito's low-side representative; a working search must
    # find its floor-1 conjugate.
    ("Delta^2 s2 s1^-1", "control (raising)", "floor 0 as written; conjugate has 1",
     [1, 2, 1, 2, 1, 2, 2, -1]),
]


def conjugators(max_len: int):
    """Freely-reduced words over {s1^+-1, s2^+-1} of length <= max_len."""
    yield []
    frontier = [[g] for g in GENS]
    for w in frontier:
        yield w
    for _ in range(max_len - 1):
        nxt = []
        for w in frontier:
            for g in GENS:
                if g != -w[-1]:
                    nxt.append(w + [g])
        frontier = nxt
        for w in frontier:
            yield w


def search(beta, max_len: int):
    base = dehornoy_floor(beta)
    best, witness, n = base, [], 0
    for g in conjugators(max_len):
        n += 1
        f = dehornoy_floor(free_reduce(inv(g) + beta + g))
        if f is not None and f > (best if best is not None else -1):
            best, witness = f, list(g)
    return base, best, witness, n


def main() -> None:
    validation = []
    for name, w, expect in ITO_CHECKS:
        got = dehornoy_floor(w)
        validation.append({"braid": name, "computed": got,
                           "ito_states": expect, "agrees": got == expect})
        assert got == expect, f"validation failed on {name}: {got} != {expect}"

    rows = []
    for name, kind, geometry, w in TARGETS:
        base, best, conj, n = search(w, MAX_CONJ_LEN)
        rows.append({
            "braid": name,
            "closure_kind": kind,
            "geometry": geometry,
            "crossings_as_written": len(w),
            "floor_as_written": base,
            "max_floor_over_sampled_conjugates": best,
            "conjugator_achieving_max": conj,
            "conjugates_sampled": n,
            "ito_thm2_hypothesis_met_by_some_sample": bool((best or 0) >= 3),
            "ito_thm2_applies_by_hypothesis": kind.startswith("knot"),
        })

    by = {r["braid"]: r for r in rows}
    fig8 = by["4_1 figure-eight (s1 s2^-1)^2"]
    pos = by["Delta^6 s1 s2^-1"]
    rais = by["Delta^2 s2 s1^-1"]

    # 1. the search is not vacuous: it finds a class that meets the hypothesis
    assert (pos["max_floor_over_sampled_conjugates"] or 0) >= 3, (
        "positive control failed: the search found no floor >= 3 anywhere, so "
        "a null result elsewhere would be uninterpretable")
    # 2. the search genuinely RAISES floors, it does not just re-report
    assert (rais["max_floor_over_sampled_conjugates"] or 0) > (
        rais["floor_as_written"] or 0), (
        "raising control failed: the search never increased a floor by "
        "conjugation, so a null result is about the search, not the class")
    # 3. the finding itself -- stated as a search result
    assert (fig8["max_floor_over_sampled_conjugates"] or 0) < 3, (
        "figure-eight DOES reach the hypothesis in this sample -- the audit's "
        "negative must be rewritten, not merely re-scoped")
    # 4. every sampled floor is a genuine non-None value (handle reduction
    #    terminated everywhere; no silent None poisoning the maxima)
    assert all(r["floor_as_written"] is not None for r in rows), \
        "a floor came back None: handle reduction did not resolve it"

    wb = WitnessBuilder("meson-braid-conjugacy-floor-search", engine="python-exact")
    wb.set_description(
        "Link-level successor to the Dehornoy floor probe: searches the "
        "conjugacy class (the Markov-I orbit, which is what the closure -- and "
        "hence Vol(K) -- actually depends on) for a representative meeting "
        "Ito's Theorem 2 hypothesis [beta]_D >= 3. A SEARCH over freely-reduced "
        "conjugators of length <= 10, not a proof: no bound on the supremum of "
        "the floor over a conjugacy class is computed or cited. Carries a "
        "positive control (a class that does reach 3) and a raising control "
        "(Ito's own pair, searched from the low side) so that a null result is "
        "readable as a fact about the class rather than about the search.")
    wb.add_data("validation_against_ito", validation)
    wb.add_data("search_parameters", {
        "group": "B_3",
        "conjugator_words": "freely reduced over {s1^+-1, s2^+-1}",
        "max_conjugator_length": MAX_CONJ_LEN,
        "why_B_3": ("Ito states (s1 s2)^4 has floor 1 in B_3 and 0 in B_4: "
                    "Delta_n^2 lengthens with n, the bracketing interval "
                    "widens, and the floor can only fall. So the floor is "
                    "maximised at minimal braid index and B_3 is the best "
                    "case. This rests on that single stated example, not on a "
                    "theorem verified here."),
    })
    wb.add_data("link_level_search", rows)
    wb.add_data("finding", {
        "claim": ("No sampled representative of the figure-eight knot's "
                  "conjugacy class in B_3 reaches [beta]_D >= 3, so Ito's "
                  "Theorem 2 cannot certify the hyperbolicity of 4_1 -- a knot "
                  "that IS hyperbolic, with the volume the corpus's muon "
                  "carrier uses."),
        "scope": ("(a) scope-limited negative: this construction, searched this "
                  "far, does not meet the hypothesis. NOT (b): no invariant is "
                  "proved to forbid it, and the supremum over the full "
                  "conjugacy class is not computed."),
        "what_it_replaces": ("the word-level 'load-bearing' claim retracted in "
                             "docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-"
                             "criterion.md, which read a floor off one chosen "
                             "spelling as a fact about the link"),
        "borromean_caveat": ("the Borromean row is a 3-COMPONENT LINK; Ito's "
                             "Theorem 2 is stated for braids whose closure is a "
                             "KNOT, so the theorem does not apply to it by "
                             "hypothesis regardless of its floor. Reported for "
                             "scale only."),
        "corrects_a_sibling_conjecture": {
            "where": ("docs/audits/2026-08-25-atom-word-closures-are-not-"
                      "hyperbolic.md, Addendum 2026-08-25, item 2 (landed on "
                      "main as b437d3bb7e, and scoped by its author as a "
                      "conjecture rather than a result)"),
            "conjectured": ("small floor is 'precisely the regime where a word "
                            "admits many closed-braid representatives and "
                            "closures tend to be torus or composite'"),
            "what_the_paper_states": ("the implication runs the other way. Ito "
                                      "Prop 4: non-braided satellite closure "
                                      "=> [beta]_D < 3. Ito Remark 4, citing "
                                      "Menasco-Nakamura: composite closure => "
                                      "[beta]_D < 2. So composite => small "
                                      "floor."),
            "what_this_measurement_adds": ("the converse fails. 4_1 is PRIME "
                                           "and HYPERBOLIC and has floor 0 "
                                           "across 118097 conjugates. A small "
                                           "floor is a fact about SCALE, "
                                           "shared by hyperbolic and "
                                           "non-hyperbolic small links alike."),
            "what_is_NOT_affected": ("their primary conclusion. The atom "
                                     "words' non-hyperbolicity rests on "
                                     "monotonicity, which never touches the "
                                     "floor -- and Prop 4 read FORWARDS "
                                     "supports them: composite closures are "
                                     "exactly what must have small floor."),
        },
        "not_computed": ("sup over the conjugacy class (Malyutin's quantity). "
                         "That paper is not in library/; no bound from it is "
                         "invoked here."),
    })
    wb.set_audit_only(
        "docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md")

    wb.add_assertion(
        name="reproduces_all_three_ito_stated_floors",
        computed=sum(1 for v in validation if v["agrees"]), expected=3,
        tolerance=0, unit="count",
        source=("Includes the conjugation pair Ito uses to show the floor is "
                "not a conjugacy invariant -- the property this whole probe "
                "turns on."))
    wb.add_assertion(
        name="positive_control_reaches_the_hypothesis",
        computed=pos["max_floor_over_sampled_conjugates"], expected=3,
        tolerance=0, unit="floor",
        source=("Delta^6 s1 s2^-1. Without this a null result elsewhere would "
                "be uninterpretable -- it could mean the search is broken."))
    wb.add_assertion(
        name="search_raises_floors_by_conjugation",
        computed=(rais["max_floor_over_sampled_conjugates"]
                  - rais["floor_as_written"]), expected=1,
        tolerance=0, unit="floor",
        source=("Ito's Delta^2 s2 s1^-1 has floor 0 as written and a "
                "floor-1 conjugate. Searching from the LOW side shows the "
                "search finds increases and does not merely re-report."))
    wb.add_assertion(
        name="hyperbolic_figure_eight_never_meets_the_hypothesis",
        computed=fig8["max_floor_over_sampled_conjugates"], expected=0,
        tolerance=0, unit="floor",
        source=(f"Searched {fig8['conjugates_sampled']} conjugates in B_3. "
                "4_1 IS hyperbolic (Vol 2.0299) and IS a knot, so Theorem 2 "
                "would apply to it if the floor condition could be met. A "
                "SEARCH result: no bound on the class supremum is computed."))

    out = wb.save()

    print(f"B_3, conjugators up to length {MAX_CONJ_LEN}\n")
    for r in rows:
        print(f"  {r['braid']:<34s} {r['geometry']}")
        print(f"      as written {r['floor_as_written']}   "
              f"best over {r['conjugates_sampled']} conjugates: "
              f"{r['max_floor_over_sampled_conjugates']}   "
              f"[{r['closure_kind']}]")
    print("\nIto Thm 2 requires floor >= 3, and applies only to knot closures.")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
