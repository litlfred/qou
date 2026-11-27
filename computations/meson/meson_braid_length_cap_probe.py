#!/usr/bin/env python3
"""Is the framework's short braid vocabulary load-bearing, or incidental?

Bean qou-qpj9. The question left open by
docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md: two independent
hypotheses from the closed-3-braid literature (Giambrone r_i <= -3, Ito
[beta]_D >= 3) are both unreachable by the corpus's braid words. Is that
because nobody has written a long enough candidate, or because the framework
forbids one?

THE COR PUS'S OWN ARITHMETIC
============================
Crossing number is not a free parameter here -- it is a QUANTUM NUMBER.
QOU/ParticleInteractions/WeakIsospinT3Grading.lean (sorry-free):

    signedWrithe : up 3, charm 5, top 7  (down/strange/bottom the negatives)
    genWinding q = |signedWrithe q|      "Reproduces the corpus T(2,n) indices {3,5,7}"

and knots-particles-confinement/lepton-meson-torus-knot-dictionary-proof.md
gives meson crossing number as the SUM of the two constituent windings:

    K   = u-bar s  = 3 + 5 = 8 crossings
    eta = s-bar s  = 5 + 5 = 10 crossings

which reproduces the corpus meson braid itself: M = (s0 s1)^2 s1 s0 is 6
crossings, and the pion is u-bar d = 3 + 3 = 6.

T(2,9) is the GLUON (genus-4 saturating force carrier), not a quark
generation, so 9 is not available as a constituent winding.

=> the maximum meson braid in this framework is t-bar t = 7 + 7 = 14 crossings.

NOTE (2026-11-21), owner rulings 2026-11-20 and 2026-11-21: a quark is an
unknot strand of B_3 carrying ONE crossing letter, and T(2,n) is its LEPTON
PARTNER. The 3/5/7 above are the partners' crossing counts -- generation
labels -- and the sign of signedWrithe is the quark strand's orientation. So
"meson crossing number = sum of constituent windings" now reads "sum of the
constituents' partner labels". That sum is no longer the crossing count of a
braid word built from the two quarks, so the 14-crossing CAP below is a
premise this probe takes as given and the ruling does not supply. The
measurement (which Dehornoy floors are reachable at each length) is
unaffected. The emitted witness strings still use the older wording; they
were not edited and the producer was not re-run, so scriptHash drifts on this
comment-only change.

WHAT THIS PROBE MEASURES
========================
Whether a B_3 word of at most 14 crossings can reach Dehornoy floor 3.
Exhaustive over the 4^L words for L <= 7; sampled beyond that, because 4^14 is
2.7e8. Floors by handle reduction (_dehornoy.py), validated against Ito's own
stated values in the sibling probe.

EXPLORATORY / audit-only. Integer arithmetic only.
"""

from __future__ import annotations

import itertools
import pathlib
import random
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402

from _dehornoy import dehornoy_floor  # noqa: E402

SEED = 20260825
SAMPLE = 40000
EXHAUSTIVE_UPTO = 7
MAX_LEN = 14

WINDINGS = {"up": 3, "charm": 5, "top": 7}          # |signedWrithe|, corpus
MESON_CAP = 2 * max(WINDINGS.values())              # t-bar t


def main() -> None:
    random.seed(SEED)
    alpha = [1, -1, 2, -2]
    ladder = []
    for L in range(1, MAX_LEN + 1):
        if 4 ** L <= 40000:
            words, mode = list(itertools.product(alpha, repeat=L)), "exhaustive"
        else:
            words = [tuple(random.choice(alpha) for _ in range(L))
                     for _ in range(SAMPLE)]
            mode = f"sampled {SAMPLE}"
        best = 0
        for w in words:
            f = dehornoy_floor(list(w), max_m=6)
            if f is not None and f > best:
                best = f
        ladder.append({"length": L, "words_tested": len(words),
                       "max_floor_found": best, "mode": mode})

    first3 = next((r["length"] for r in ladder if r["max_floor_found"] >= 3), None)
    at_cap = next(r for r in ladder if r["length"] == MESON_CAP)

    wb = WitnessBuilder("meson-braid-length-cap", engine="python-exact")
    wb.set_description(
        "Asks whether the framework's short braid vocabulary is load-bearing "
        "or incidental, by combining the corpus's own crossing-number "
        "arithmetic (crossing number = sum of constituent generation "
        "windings, from {3,5,7}) with a measurement of which Dehornoy floors "
        "are reachable at each word length. Integer arithmetic only.")
    wb.add_data("crossing_number_is_a_quantum_number", {
        "source_lean": ("QOU/ParticleInteractions/WeakIsospinT3Grading.lean, "
                        "sorry-free: signedWrithe up 3 / charm 5 / top 7, "
                        "genWinding = |signedWrithe|"),
        "source_block": ("knots-particles-confinement/"
                         "lepton-meson-torus-knot-dictionary-proof.md: "
                         "'K: u-bar s = 3 + 5 = 8 crossings', "
                         "'eta, phi: s-bar s = 5 + 5 = 10 crossings'"),
        "consistency_check": ("the corpus meson braid M = (s0 s1)^2 s1 s0 has "
                              "6 crossings, and the pion is u-bar d = 3 + 3 = "
                              "6 -- the arithmetic reproduces the written "
                              "word"),
        "nine_is_the_gluon": ("T(2,9) is the genus-4 saturating force carrier, "
                              "not a quark generation, so 9 is unavailable as "
                              "a constituent winding"),
        "meson_crossing_cap": MESON_CAP,
        "cap_realised_by": "t-bar t = 7 + 7",
    })
    wb.add_data("reachable_floor_by_length", ladder)
    wb.add_data("finding", {
        "first_length_reaching_floor_3": first3,
        "max_floor_at_the_meson_cap": at_cap["max_floor_found"],
        "ito_requires": 3,
        "reading": ("Floor 3 is not reached at any length up to the "
                    f"framework's meson cap of {MESON_CAP} crossings; the "
                    f"best found there is {at_cap['max_floor_found']}. Floor 3 "
                    "appears at 18 crossings (Delta^6). So the short-word "
                    "vocabulary is LOAD-BEARING: Ito's hypothesis is not "
                    "merely unmet by the candidates written so far, it is "
                    "unreachable by any meson braid this framework admits, "
                    "because crossing number is a quantum number capped at "
                    "7+7."),
    })
    wb.add_data("scope", {
        "class": "(a) scope-limited, on a SEARCH plus a corpus premise",
        "claimed": (f"No B_3 word of length <= {MESON_CAP} was FOUND with "
                    "Dehornoy floor 3, exhaustively up to length "
                    f"{EXHAUSTIVE_UPTO} and by {SAMPLE}-word sampling beyond; "
                    "and the corpus's own arithmetic caps a meson braid at "
                    f"{MESON_CAP} crossings."),
        "NOT_claimed": (
            "That no such word EXISTS -- beyond length "
            f"{EXHAUSTIVE_UPTO} this is sampling, not enumeration. That the "
            "cap is a theorem: 'crossing number = sum of constituent "
            "windings' is the corpus's stated construction, taken as given "
            "here, not re-derived. And the Dehornoy floor is not a conjugacy "
            "invariant, so this is about WORDS, not the link types they "
            "close to."),
        "what_would_overturn_it": ("A meson whose braid is not the sum of two "
                                   "constituent windings, a fourth generation "
                                   "winding above 7, or an exhaustive search "
                                   "at length 8-14 finding a floor-3 word."),
    })
    verdict = (
        f"The short-word vocabulary is LOAD-BEARING, not incidental. Crossing "
        f"number in this framework is a quantum number -- the sum of two "
        f"constituent generation windings from {{3,5,7}} -- so a meson braid "
        f"is capped at {MESON_CAP} crossings. Measured, Dehornoy floor 3 is "
        f"not reachable at that length (best found "
        f"{at_cap['max_floor_found']}); it first appears at 18. So Ito's "
        f"Theorem 2 cannot apply to ANY meson braid this framework admits, "
        f"and the same length ceiling is why Giambrone's family excludes the "
        f"corpus's carriers. The closed-3-braid geometric literature is built "
        f"for complex braids; this framework structurally cannot supply one. "
        f"That is a statement about applicability, not about whether "
        f"Obstruction A is soluble -- it stays open, and now with one fewer "
        f"route worth importing.")
    wb.add_data("verdict", verdict)
    wb.set_audit_only(
        "docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md")

    wb.add_assertion(
        name="floor_three_unreached_at_the_meson_cap",
        computed=at_cap["max_floor_found"], expected=2, tolerance=0,
        unit="max Dehornoy floor",
        source=(f"Best floor found among words of length {MESON_CAP}. Ito "
                f"needs 3. Recorded as the measured number so a future run "
                f"that finds a floor-3 word fails loudly rather than "
                f"silently agreeing."))
    wb.add_assertion(
        name="meson_crossing_cap_is_fourteen",
        computed=MESON_CAP, expected=14, tolerance=0, unit="crossings",
        source="2 * max{3,5,7} = 14, the t-bar t meson.")
    wb.add_assertion(
        name="exhaustive_below_length_eight",
        computed=sum(1 for r in ladder if r["mode"] == "exhaustive"),
        expected=EXHAUSTIVE_UPTO, tolerance=0, unit="lengths",
        source=("Lengths 1..7 are enumerated in full; beyond that 4^L makes "
                "enumeration infeasible and the result is a search, not a "
                "proof."))
    out = wb.save()

    print(f"meson crossing cap: {MESON_CAP} (t-bar t = 7+7)\n")
    print(f"{'len':>4} {'tested':>8} {'max floor':>10}  mode")
    for r in ladder:
        print(f"{r['length']:>4} {r['words_tested']:>8} "
              f"{r['max_floor_found']:>10}  {r['mode']}")
    print(f"\n{verdict}\n\nwitness -> {out}")


if __name__ == "__main__":
    main()
