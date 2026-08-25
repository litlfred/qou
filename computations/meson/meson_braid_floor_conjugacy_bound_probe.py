#!/usr/bin/env python3
"""The conjugacy bound was in the corpus: search -> PROOF.

Bean qou-qpj9. UPGRADES the result of
meson_braid_conjugacy_floor_search_probe.py from a scope-(a) search to a
scope-(b) structural exclusion, and records why that took two attempts.

WHAT I GOT WRONG
================
That probe's scope note reads: "no Malyutin bound is invoked -- that paper is
not in library/, so corpus-grep path 5 cannot support citing it." The bound IS
in library/. Ito quotes it in full, attributed to both [MN] and [Ma], in
sec-001-2-braid-ordering-and-dehornoy-floor -- the SAME section whose conjugate
pair I used as that probe's validation gate. I read the definition and the
example and stopped three lines above the theorem.

The mechanical cause is worth more than the result. I grepped for "Malyutin"
in library/INDEX.md and docs/ and found only my own audit. INDEX.md is ONE LINE
PER DOCUMENT, so a result CITED INSIDE a document I hold is invisible to it by
construction, and Malyutin has no document of his own here. AGENTS.md path 5
lists three tiers; tier 1 answering "no" is not tier 3 answering "no". A bound
you need may be quoted in a paper you already have.

THE BOUND (Ito, Proposition 2, attributed to [MN],[Ma])
=======================================================
  (1) if a word for beta has s occurrences of sigma_1 and k of sigma_1^-1,
      then [beta]_D < max{s, k}
  (2) |[beta]_D - [beta']_D| <= 1 if beta and beta' are CONJUGATE
  (3) [alpha beta]_D <= 1 + [alpha]_D + [beta]_D
  (4) if the closure admits destabilization or an exchange move, [beta]_D <= 1

Stated in Ito's convention, which is the one implemented in _dehornoy.py and
validated against all three floors Ito states. Ito's Remark 1 notes his
definition differs slightly from [Ma]'s and follows [MN]; since Proposition 2
is stated in HIS convention, it applies to these floors directly and no
convention reconciliation is needed. That check is the reason this file exists
rather than a one-line edit to the audit.

WHAT (2) DOES
=============
4_1 has floor 0, so EVERY conjugate has floor <= 1. Ito's Theorem 2 needs >= 3.
So no representative of the figure-eight's conjugacy class in B_3 can satisfy
the hypothesis -- not "none found in 118097 samples", none EXISTS. Likewise the
corpus meson at floor 1: every conjugate <= 2.

The 118097-conjugate search is now CORROBORATION rather than evidence, and it
corroborates two ways: it found no counterexample, and its raising control
SATURATES the bound (Ito's pair, 0 -> 1, exactly |delta| = 1).

EXPLORATORY / audit-only. Integer arithmetic only.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402

from _dehornoy import dehornoy_floor  # noqa: E402

ITO_THM2_REQUIRES = 3

# (name, word, is_knot_closure, geometry)
TARGETS = [
    ("4_1 figure-eight (s1 s2^-1)^2", [1, -2, 1, -2], True,
     "HYPERBOLIC, Vol 2.0299 (muon carrier)"),
    ("Borromean (s1 s2^-1)^3", [1, -2, 1, -2, 1, -2], False,
     "HYPERBOLIC, Vol 7.3277 (proton carrier) -- a LINK, Thm 2 excludes it"),
    ("meson M = (s1 s2)^2 s2 s1", [1, 2, 1, 2, 2, 1], True, "torus T(2,5), Vol 0"),
    ("trefoil s1^3", [1, 1, 1], True, "torus T(2,3), Vol 0"),
]

# Ito's own conjugate pair -- the tightness witness for (2).
ITO_PAIR = (("Delta^2 s1 s2^-1", [1, 2, 1, 2, 1, 2, 1, -2]),
            ("Delta^2 s2 s1^-1", [1, 2, 1, 2, 1, 2, 2, -1]))


def sigma1_counts(w):
    return sum(1 for x in w if x == 1), sum(1 for x in w if x == -1)


def main() -> None:
    rows = []
    for name, w, is_knot, geom in TARGETS:
        f = dehornoy_floor(w)
        s, k = sigma1_counts(w)
        rows.append({
            "braid": name, "geometry": geom, "closure_is_a_knot": is_knot,
            "floor": f,
            "sigma1_pos": s, "sigma1_neg": k,
            "prop2_1_strict_bound": max(s, k),
            "prop2_1_respected": f < max(s, k),
            "max_floor_over_ENTIRE_conjugacy_class_by_prop2_2": f + 1,
            "can_ANY_representative_meet_ito_thm2": (f + 1) >= ITO_THM2_REQUIRES,
        })

    # tightness of (2): Ito's pair differs by exactly 1
    (na, wa), (nb, wb) = ITO_PAIR
    fa, fb = dehornoy_floor(wa), dehornoy_floor(wb)
    tight = {"a": na, "floor_a": fa, "b": nb, "floor_b": fb,
             "abs_difference": abs(fa - fb),
             "prop2_2_allows_at_most": 1,
             "saturates_the_bound": abs(fa - fb) == 1}

    by = {r["braid"]: r for r in rows}
    fig8 = by["4_1 figure-eight (s1 s2^-1)^2"]
    meson = by["meson M = (s1 s2)^2 s2 s1"]

    # 1. the implementation agrees with a theorem it never saw
    assert all(r["prop2_1_respected"] for r in rows), \
        "a computed floor violates Ito Prop 2(1); the handle reduction is wrong"
    # 2. the bound is tight, so (2) is not being applied vacuously
    assert tight["saturates_the_bound"], \
        "Ito's own conjugate pair does not differ by 1 -- either the pair or " \
        "the implementation is misread, and (2) cannot be trusted here"
    # 3. THE RESULT, now by proof
    assert not fig8["can_ANY_representative_meet_ito_thm2"], \
        "the exclusion of 4_1 does not follow; re-derive before publishing"
    assert not meson["can_ANY_representative_meet_ito_thm2"], \
        "the exclusion of the corpus meson does not follow"

    wb_ = WitnessBuilder("meson-braid-floor-conjugacy-bound", engine="python-exact")
    wb_.set_description(
        "Applies Ito's Proposition 2 (attributed to Malyutin-Netsvetaev and "
        "Malyutin, quoted in the ingested library/arxiv-0805.1447v2) to upgrade "
        "the conjugacy-floor SEARCH to a structural exclusion. Prop 2(2) bounds "
        "the floor's variation over a conjugacy class by 1, so a floor-0 braid "
        "has no representative above 1 and can never meet Theorem 2's [beta]_D "
        ">= 3. Also checks the implementation against Prop 2(1), a theorem it "
        "was not built from, and confirms Prop 2(2) is tight on Ito's own pair.")
    wb_.add_data("bound_source", {
        "quoted_in": ("library/arxiv-0805.1447v2/sections/"
                      "sec-001-2-braid-ordering-and-dehornoy-floor.md"),
        "attributed_by_ito_to": [
            "[MN] A. Malyutin, N. Netsvetaev, Dehornoy's ordering on the braid "
            "group and braid moves, St. Petersburg Math. J. 15, No.3 (2004), "
            "437-448",
            "[Ma] A. Malyutin, Twist number of (closed) braids, St. Petersburg "
            "Math. J. 16, No.5 (2005), 791-813",
        ],
        "convention_check": ("Ito's Remark 1 says his floor definition differs "
                             "slightly from [Ma]'s and follows [MN]. Prop 2 is "
                             "stated in ITO's convention, which is what "
                             "_dehornoy.py implements and what was validated "
                             "against Ito's three stated floors -- so it "
                             "applies directly, with no reconciliation."),
        "neither_paper_is_ingested": ("arxiv.org is denied at CONNECT by this "
                                      "sandbox's proxy (403, policy), as are "
                                      "export.arxiv.org, link.springer.com and "
                                      "mathnet.ru. Not needed: the statement "
                                      "used is quoted in full in a document the "
                                      "corpus holds."),
    })
    wb_.add_data("exclusion_by_prop2_2", rows)
    wb_.add_data("prop2_2_is_tight", tight)
    wb_.add_data("corrects_my_own_scope_note", {
        "where": "computations/meson/meson_braid_conjugacy_floor_search_probe.py",
        "said": ("no Malyutin bound is invoked -- that paper is not in "
                 "library/, so corpus-grep path 5 cannot support citing it"),
        "actual": ("the bound is quoted in full in library/arxiv-0805.1447v2, "
                   "in the SAME section whose conjugate pair that probe uses as "
                   "its validation gate"),
        "mechanical_cause": ("I grepped 'Malyutin' in library/INDEX.md and "
                             "docs/ only. INDEX.md is ONE LINE PER DOCUMENT, so "
                             "a result CITED INSIDE a held document is "
                             "invisible to it by construction, and Malyutin has "
                             "no document of his own here. AGENTS.md path 5 has "
                             "three tiers; tier 1 answering 'no' is not tier 3 "
                             "answering 'no'."),
        "what_changes": ("scope (a) search -> scope (b) structural exclusion "
                         "with the invariant cited. The 118097-conjugate search "
                         "becomes corroboration, and it corroborates twice: no "
                         "counterexample, and its raising control saturates the "
                         "bound."),
        "what_does_NOT_change": ("the numbers, and the reading. Ito's threshold "
                                 "still sits at 18 crossings and a genuinely "
                                 "hyperbolic knot still cannot reach it. The "
                                 "finding is now proved rather than sampled."),
    })
    wb_.set_audit_only(
        "docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md")

    wb_.add_assertion(
        name="implementation_respects_prop2_1",
        computed=sum(1 for r in rows if r["prop2_1_respected"]),
        expected=len(rows), tolerance=0, unit="count",
        source=("Prop 2(1) is a theorem the handle-reduction code was not built "
                "from, so agreement is an independent check on it."))
    wb_.add_assertion(
        name="prop2_2_is_tight_on_itos_own_pair",
        computed=tight["abs_difference"], expected=1, tolerance=0, unit="floor",
        source="Conjugate braids differing by exactly the bound's maximum.")
    wb_.add_assertion(
        name="no_representative_of_4_1_can_meet_ito_thm2",
        computed=fig8["max_floor_over_ENTIRE_conjugacy_class_by_prop2_2"],
        expected=1, tolerance=0, unit="floor",
        source=("floor 0 + Prop 2(2) => class max 1 < 3. A genuinely hyperbolic "
                "knot, excluded by proof rather than by sampling."))
    wb_.add_assertion(
        name="no_representative_of_the_corpus_meson_can_meet_ito_thm2",
        computed=meson["max_floor_over_ENTIRE_conjugacy_class_by_prop2_2"],
        expected=2, tolerance=0, unit="floor",
        source="floor 1 + Prop 2(2) => class max 2 < 3.")
    out = wb_.save()

    print(f"{'braid':<32}{'floor':>6}{'P2(1)<':>8}{'class max':>11}  Thm 2 reachable?")
    for r in rows:
        print(f"{r['braid']:<32}{r['floor']:>6}"
              f"{r['prop2_1_strict_bound']:>8}"
              f"{r['max_floor_over_ENTIRE_conjugacy_class_by_prop2_2']:>11}  "
              f"{'YES' if r['can_ANY_representative_meet_ito_thm2'] else 'NO -- by proof'}")
    print(f"\nProp 2(2) tight on Ito's pair: |{fa} - {fb}| = "
          f"{tight['abs_difference']} (bound 1)")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
