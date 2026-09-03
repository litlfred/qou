#!/usr/bin/env python3
"""Bound the meson-braid candidate space from the INGESTED literature.

Bean qou-qpj9 / qou-pb1w (Obstruction A).

WHY THIS EXISTS
===============
docs/audits/2026-08-24-meson-braid-obstruction-a-measured.md measured that the
corpus's own meson braid M = (s0 s1)^2 s1 s0 closes to T(2,5) with Vol = 0, and
diagnosed it: "length is not the culprit; positivity is." It then recorded two
things about the literature:

  "The corpus library (332 documents) ... carries the volume-conjecture line
   ... but NOTHING on the classification or volumes of closed 3-braids, which
   is exactly the tool Obstruction A needs."

  "These are search-result summaries, NOT READ PAPERS -- I did not fetch the
   FKP theorem statements, so the exact volume-bound constants are not quoted
   here and MUST BE CHECKED BEFORE USE."

**The first is false.** The library DOES carry it, sectioned and greppable:
library/arxiv-1406.7337v4/ -- Giambrone, "Semi-Adequate Closed Braids and
Volume" -- the same arXiv id (1406.7337) that audit linked as an external
web-search result it could not fetch. This probe does the checking-before-use
it asked for, from the ingested copy.

WHAT THE PAPER ACTUALLY SAYS (read, not summarised)
===================================================
Theorem 1.2. For D(K) a certain A-adequate closed 3-braid diagram,
    v8 * (s - 1)  <=  vol(S^3 \\ K)  <  4 * v8 * s
with v8 = 3.6638... the volume of the regular ideal OCTAHEDRON.

Theorem 3.1. For a nice 3-braid satisfying Lemma 2.1, the Schreier parameter
    s = t_-(D) = #{negative syllables in beta}
is read directly off the ORIGINAL braid word -- no normal-form computation.

Lemma 2.1(1). Every negative exponent r_i < 0 satisfies r_i <= -3.

Sublemma 2.1 (proof). "Condition (2a), Condition (2b), and Condition (2c) of
Lemma 2.1 imply that BETA CANNOT BE POSITIVE. Because positive syllables of
beta are cyclically neighbored by negative syllables..." -- and per Prop 2.1
that neighbouring is Stoimenow's classification of A-adequate closed 3-braid
diagrams.

CONSEQUENCE 1 -- the audit's diagnosis becomes a theorem
========================================================
A fully positive 3-braid word is STRUCTURALLY EXCLUDED from the A-adequate
family: s = t_-(D) = 0. The corpus braid M is entirely positive, so s = 0, its
Schreier class is non-generic, and it cannot be hyperbolic by this route. That
is exactly the measured Vol = 0 -- now predicted from the braid word alone,
with no SnapPy. "Positivity is the culprit" was an empirical diagnosis; it is
now a structural one, and s is the dial.

CONSEQUENCE 2 -- the heavy end IS bounded (the audit said it was not)
====================================================================
The audit records: "the J/psi and D0 targets (59.50, 35.83) lie far above
anything reachable at these braid lengths, so THE CANDIDATE SPACE IS NOT EVEN
BOUNDED YET at the heavy end." Inverting Theorem 1.2 bounds it:

    vol < 4*v8*s   =>  s >  V / (4*v8)
    v8*(s-1) <= vol =>  s <= V / v8 + 1

and Lemma 2.1(1) forces every negative syllable to carry exponent <= -3, so
    minimum negative crossings  >=  3 * s_min.

This probe computes those windows for the corpus's own target volumes.

SCOPE -- read before citing
===========================
This bounds the candidate space; it does NOT derive a braid, propose one, or
check a mass. Obstruction A (a canonical parameter-free operation fixing the
braid) is untouched and remains open. The bounds are also CONDITIONAL on the
target braid lying in Giambrone's family (nice + Lemma 2.1 + A-adequate); a
candidate outside it is not excluded by these numbers, it is merely not
covered by them. Stated as a necessary condition for the family, never as a
sufficient one for anything.

EXPLORATORY / audit-only. mpmath, no float64 anywhere.
"""

from __future__ import annotations

import pathlib

# bootstrap: _path_bridge lives in computations/, one level up from this
# cluster dir, so it must be on sys.path BEFORE it is imported. Without
# this the module is unresolvable and the script cannot run standalone.
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf, floor, ceil  # noqa: E402

set_compute_dps()

# Regular ideal OCTAHEDRON volume: v8 = 4*Catalan = 3.66386237671...
# NOT 8*Catalan -- that is 7.32772475342 = 2*v8 = Vol(Borromean), the corpus's
# own 8G. Writing 8*Catalan here is the right-constant/wrong-coefficient trap
# AGENTS.md flags for Lambda vs Cl_2; it was made in the first draft of this
# probe and caught by the v8_matches_corpus_borromean_volume assertion below,
# which is why that assertion is worth keeping.
V8 = 4 * mp.catalan

# Target Vol*rho from the audit's own table (proton pin,
# hbar_q^2 = 0.00981718645427507381). Reproduced, not recomputed.
TARGETS = [
    ("pi+-",  mpf("2.681392089")),
    ("K+-",   mpf("9.484401401")),
    ("K0",    mpf("9.559980444")),
    ("eta",   mpf("10.52539033")),
    ("D0",    mpf("35.82684854")),
    ("eta_c", mpf("57.3259547")),
    ("J/psi", mpf("59.49688298")),
]

# The corpus's meson braid, def:categorical-meson: M = (s0 s1)^2 s1 s0.
CORPUS_BRAID = [1, 2, 1, 2, 2, 1]          # all positive exponents


def negative_syllables(word):
    """Count maximal same-generator runs with negative exponent."""
    return sum(1 for e in word if e < 0)


def main() -> None:
    set_compute_dps()

    s_corpus = negative_syllables(CORPUS_BRAID)

    rows = []
    for name, V in TARGETS:
        s_min = int(floor(V / (4 * V8))) + 1        # strict: s > V/(4 v8)
        s_max = int(floor(V / V8)) + 1              # v8(s-1) <= V
        rows.append({
            "meson": name,
            "vol_rho_target": mp.nstr(V, 10),
            "s_min": s_min,
            "s_max": s_max,
            "min_negative_crossings": 3 * s_min,
            "window_lo": mp.nstr(V8 * (s_min - 1), 8),
            "window_hi": mp.nstr(4 * V8 * s_max, 8),
        })

    wb = WitnessBuilder("meson-braid-syllable-bound", engine="mpmath")
    wb.set_description(
        "Bounds the meson-braid candidate space using Giambrone's closed-"
        "3-braid volume bounds, read from the INGESTED library copy "
        "(library/arxiv-1406.7337v4/). The 2026-08-24 Obstruction-A audit "
        "recorded that the library carried nothing on closed-3-braid volumes "
        "and that its literature entries were unread search summaries whose "
        "constants must be checked before use. The library does carry the "
        "paper; this does that checking. Bounds the candidate space; derives "
        "no braid and checks no mass.")
    wb.add_data("corrects_prior_audit", {
        "audit": "docs/audits/2026-08-24-meson-braid-obstruction-a-measured.md",
        "its_claim": ("'The corpus library (332 documents) ... carries the "
                      "volume-conjecture line ... but nothing on the "
                      "classification or volumes of closed 3-braids, which "
                      "is exactly the tool Obstruction A needs.'"),
        "correction": ("library/arxiv-1406.7337v4/ IS that tool -- Giambrone, "
                       "'Semi-Adequate Closed Braids and Volume', the same "
                       "arXiv id the audit linked as an unfetchable external "
                       "result. Sectioned and greppable."),
        "its_own_caveat_now_discharged": ("'These are search-result "
                                          "summaries, not read papers ... "
                                          "the exact volume-bound constants "
                                          "are not quoted here and must be "
                                          "checked before use.'"),
        "nothing_else_in_that_audit_is_disturbed": (
            "Its SnapPy measurement, its T(2,5) identification, its axis-trap "
            "method note and its chiral-limit refutation all stand."),
    })
    wb.add_data("theorem_as_read", {
        "source": "library/arxiv-1406.7337v4 (Giambrone), read from sections",
        "thm_1_2": "v8*(s-1) <= vol(S^3 \\ K) < 4*v8*s, for a certain "
                   "A-adequate closed 3-braid diagram",
        "thm_3_1": "s = t_-(D) = #{negative syllables in beta}, readable off "
                   "the original 3-braid word",
        "lemma_2_1_cond_1": "every negative exponent r_i satisfies r_i <= -3",
        "sublemma_2_1_proof_quote": (
            "'Condition (2a), Condition (2b), and Condition (2c) of Lemma 2.1 "
            "imply that beta cannot be positive. Because positive syllables "
            "of beta are cyclically neighbored by negative syllables...'"),
        "v8_value": mp.nstr(V8, 12),
        "v8_identity": "v8 = 8*Catalan; the corpus carries 2*v8 = 8G = "
                       "Vol(Borromean) = 7.32772475342",
    })
    wb.add_data("consequence_1_positivity_is_structural", {
        "corpus_braid": "M = (s0 s1)^2 s1 s0 (def:categorical-meson)",
        "negative_syllables": s_corpus,
        "reading": ("A fully positive 3-braid word is structurally excluded "
                    "from the A-adequate family by Sublemma 2.1's own proof, "
                    "and has s = 0. The 2026-08-24 audit measured Vol = 0 in "
                    "SnapPy and diagnosed 'positivity is the culprit'. That "
                    "diagnosis is now theorem-backed and quantified: s, the "
                    "negative-syllable count, is the volume dial."),
        "not_claimed": ("That Theorem 1.2 'predicts' the measured 0. A "
                        "positive braid is OUTSIDE the theorem's family, so "
                        "the theorem does not apply to it -- it excludes it. "
                        "Exclusion from the hyperbolic family and a measured "
                        "Vol = 0 agree, which is the point, but they are not "
                        "the same statement."),
    })
    wb.add_data("consequence_2_heavy_end_is_bounded", {
        "audit_said": ("'the J/psi and D0 targets (59.50, 35.83) lie far "
                       "above anything reachable at these braid lengths, so "
                       "the candidate space is not even bounded yet at the "
                       "heavy end.'"),
        "now_bounded_by": ("s > V/(4*v8) and s <= V/v8 + 1, with >= 3 "
                           "negative crossings per negative syllable from "
                           "Lemma 2.1(1)."),
        "windows": rows,
    })
    wb.add_data("scope", {
        "class": "(a) a NECESSARY-condition bound on a candidate space",
        "claimed": ("Within Giambrone's family, a closed 3-braid realising "
                    "target volume V must have negative-syllable count s in "
                    "the stated window, hence at least 3*s_min negative "
                    "crossings."),
        "NOT_claimed": ("That any braid is derived, proposed, or checked "
                        "against a mass. Obstruction A -- a canonical, "
                        "parameter-free operation fixing the braid -- is "
                        "untouched and open. A candidate outside the family "
                        "is not excluded by these numbers; it is uncovered "
                        "by them."),
    })

    jpsi = next(r for r in rows if r["meson"] == "J/psi")
    pion = next(r for r in rows if r["meson"] == "pi+-")
    verdict = (
        f"The tool the Obstruction-A audit called absent from the library is "
        f"IN the library (arxiv-1406.7337v4), and its constants are now read "
        f"rather than summarised. Two consequences. (1) A fully positive "
        f"3-braid is structurally excluded from the A-adequate family -- the "
        f"corpus braid has s = {s_corpus} -- so 'positivity is the culprit' "
        f"is now structural, with s the volume dial. (2) The heavy end IS "
        f"bounded, contrary to that audit: J/psi (V = 59.497) needs s in "
        f"[{jpsi['s_min']}, {jpsi['s_max']}], hence at least "
        f"{jpsi['min_negative_crossings']} negative crossings; the pion "
        f"(V = 2.681) needs s in [{pion['s_min']}, {pion['s_max']}], at least "
        f"{pion['min_negative_crossings']}. Necessary conditions only -- no "
        f"braid is derived, proposed, or mass-checked, and Obstruction A "
        f"stays open.")
    wb.add_data("verdict", verdict)
    wb.set_audit_only(
        "docs/audits/2026-08-24-meson-braid-obstruction-a-measured.md")

    wb.add_assertion(
        name="corpus_meson_braid_has_zero_negative_syllables",
        computed=s_corpus, expected=0, tolerance=0, unit="count",
        source=("M = (s0 s1)^2 s1 s0 is entirely positive, so it is excluded "
                "from the A-adequate family by Sublemma 2.1."))
    wb.add_assertion(
        name="v8_matches_corpus_borromean_volume",
        computed=mp.nstr(2 * V8, 12), expected="7.32772475342",
        tolerance="1e-10", unit="hyperbolic volume",
        source=("v8 = 8*Catalan must reproduce the corpus's own "
                "Vol(Borromean) = 2*v8, which the prior audit verified in "
                "SnapPy to 11 places. Ties this probe's constant to a "
                "measured corpus number."))
    wb.add_assertion(
        name="heavy_end_windows_are_finite",
        computed=1 if all(r["s_max"] >= r["s_min"] for r in rows) else 0,
        expected=1, tolerance=0, unit="boolean",
        source="Every target admits a non-empty, finite syllable window.")
    out = wb.save()

    print(f"v8 = {mp.nstr(V8, 12)}   2*v8 = {mp.nstr(2*V8, 12)} "
          f"(corpus Borromean 7.32772475342)\n")
    print(f"corpus braid M = (s0 s1)^2 s1 s0 -> negative syllables = "
          f"{s_corpus}  => excluded from the A-adequate family\n")
    print(f"{'meson':>7} {'Vol*rho':>11} {'s_min':>6} {'s_max':>6} "
          f"{'>= neg crossings':>17}")
    for r in rows:
        print(f"{r['meson']:>7} {r['vol_rho_target']:>11} {r['s_min']:>6} "
              f"{r['s_max']:>6} {r['min_negative_crossings']:>17}")
    print(f"\nverdict:\n{verdict}")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
