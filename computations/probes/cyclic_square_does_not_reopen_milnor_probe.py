#!/usr/bin/env python3
# polynomial_q_not_applicable: permutation cycles and integer linking numbers;
# no q enters anywhere.
"""The one non-monotone shape that breaks route 3's premise -- and it DOES reopen route 3.

*** CORRECTED 2026-09-04. The filename and the original headline (\"does NOT reopen\")
*** are WRONG and are kept only because this file is already merged and referenced.
*** The MEASUREMENT below stands; the INFERENCE drawn from it does not. See
*** `mixed_sign_cyclic_square_does_reopen_milnor_probe.py`, which computes the
*** `mubar` this probe never computed and finds it NONZERO in 2 of this probe's
*** OWN 188 all-positive spanning insertions (Delta = 2, mubar = 1), and in 563 of
*** 3008 across all 16 inserted-sign patterns.

Bean qou-768r, route 3 — follow-up answering sibling PR #6561 (`qou-kru4`).

WHAT THIS TESTS, and why it needed testing. The route-3 result
(`milnor_minspan_triples_share_no_summand_probe.py`, and
`QOU/Mass/MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean`) rests on a premise
that is TRUE ONLY FOR MONOTONE WORDS: a monotone closure is a connected sum
`#_g T(2, e_g)`, so each summand comes from one generator and touches AT MOST 2
components. A shared summand links, so `Delta = 0` -- the condition for `mubar` to
be a genuine integer -- forces separation, hence a SPLIT sublink, hence `mubar = 0`.
(Split, not unlink: the components are (2, odd)-torus knots. Splitness is what the
vanishing needs; local knotting changes no Milnor invariant.)

Sibling #6561 proved (sorry-free, `QOU/MathlibExt/RevisitClassCrossTerm.lean`) that
the cyclic square `(g_m g_{m+1})^2` -- three adjacent strands cyclically braided --
is the ONLY non-monotone shape producing a Markov-trace cross term. That makes it
the natural candidate to break this premise, since it spans THREE strands rather
than two.

I GUESSED IT WOULD BE LOCAL KNOTTING ON ONE COMPONENT, AND THAT WAS WRONG.
`(g_m g_{m+1})^2` closes to `T(3,2)`, a knot, so the tempting reading is that it
adds a knotted summand to a single component -- and local knotting changes no
Milnor invariant. Measured, it spans up to 3 DISTINCT components: 188 of 694
insertions. The premise really does break.

THE CONCLUSION WAS CLAIMED TO SURVIVE, AND THAT CLAIM IS RETRACTED. In every one of
those 188 cases at least one pairwise linking number among the three spanned
components is NONZERO -- so `Delta != 0` there. That much is measured and stands. The
step from it that this probe took, and that is now retracted, was: `Delta != 0` means
`mubar` is "not a genuine integer in the first place", therefore no obstruction.

    NOT AN INTEGER   -- true, `mubar` lives in Z/Delta
    NO OBSTRUCTION   -- FALSE, a nonzero RESIDUE is still a nonvanishing invariant

This probe never computed `mubar`; it stopped at `Delta`. Computing it (see
`mixed_sign_cyclic_square_does_reopen_milnor_probe.py`), 2 of these very 188
all-positive spanning insertions carry `Delta = 2` with `mubar = 1` --

    4He, position 25, m=5,  lk = [0, -2, 0]
    8Be, position 77, m=17, lk = [0, 0, -2]

-- which is precisely the one bit route 3's own `Delta = 2` residual is about. The
SCOPE note below already said "it does not touch the `Delta = 2` one-bit triples";
that note was right and this headline was not.

    route 3's PREMISE is monotone-specific and does break;
    route 3's CONCLUSION also fails on this shape, at Delta = 2.

What is NOT affected: the unperturbed derived carrier, where `mubar = 0` on every
triple, and `MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean`, which concerns
`Delta = 0`. Both are re-measured as controls in the correcting probe.

SCOPE (a), and deliberately narrow. This tests ONE non-monotone shape -- the only
one #6561 shows yields a trace cross term -- with all-positive inserted crossings,
at sampled word positions across 4 isotopes. It is NOT a proof that no non-monotone
word reopens route 3, and it does not touch the `Delta = 2` one-bit triples. What
it rules out is the specific escape the sibling's own result points at.

Companion Lean: none. The statement proved in
`MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean` is unchanged -- this measures
the reach of its hypothesis rather than altering it. EXPLORATORY; nothing wired.
"""

from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

ISOTOPES = [(2, 2, "4He"), (3, 3, "6Li"), (4, 4, "8Be"), (5, 5, "10B")]

# Sampled word positions per isotope. The insertion point matters -- braid letters
# do not commute, so appending is not representative and testing only the end
# would be a weaker claim than it looks.
POSITION_SAMPLES = 8


def analyse(letters: list[tuple[int, int]], n: int):
    """Component labels and pairwise linking numbers of the closure of `letters`.

    `letters` is a list of `(generator, sign)`. Components are permutation cycles;
    a crossing between strands lying in distinct components contributes its sign,
    halved at the end (each linked pair is crossed an even number of times).
    """
    perm = list(range(n))
    for (g, _s) in letters:
        perm[g], perm[g + 1] = perm[g + 1], perm[g]

    comp = [-1] * n
    c = 0
    for s0 in range(n):
        if comp[s0] < 0:
            x = s0
            while comp[x] < 0:
                comp[x] = c
                x = perm[x]
            c += 1

    perm = list(range(n))
    twice: dict[tuple[int, int], int] = {}
    for (g, s) in letters:
        a, b = comp[perm[g]], comp[perm[g + 1]]
        if a != b:
            k = (a, b) if a < b else (b, a)
            twice[k] = twice.get(k, 0) + s
        perm[g], perm[g + 1] = perm[g + 1], perm[g]

    # Integrality is a real check, not bookkeeping: two closed curves cross an even
    # number of times, so an odd `twice` means the crossing accounting is wrong.
    # qou-768r's route-3 pass hit exactly that bug (lk = -3/2) by resolving an
    # averaged letter to the identity instead of to a crossing sign.
    odd = sum(1 for v in twice.values() if v % 2 != 0)
    return c, {k: v // 2 for k, v in twice.items()}, comp, odd


def main() -> int:
    rows = []
    tot_tested = tot_span3 = tot_reopen = 0
    half_integer_seen = 0

    for (Z, N, name) in ISOTOPES:
        A = Z + N
        n = 3 * A
        base = [(g, -1) for (g, _ct) in atom_canonical_crossings(Z, N)]
        L = len(base)
        step = max(1, L // POSITION_SAMPLES)

        tested = span3 = reopen = 0
        for pos in range(0, L + 1, step):
            for m in range(n - 2):
                word = base[:pos] + [(m, 1), (m + 1, 1), (m, 1), (m + 1, 1)] + base[pos:]
                _mu, lk, comp, odd = analyse(word, n)
                half_integer_seen += odd
                tested += 1
                spanned = {comp[m], comp[m + 1], comp[m + 2]}
                if len(spanned) == 3:
                    span3 += 1
                    a, b, c2 = sorted(spanned)
                    trip = [lk.get((a, b), 0), lk.get((b, c2), 0), lk.get((a, c2), 0)]
                    if all(v == 0 for v in trip):
                        reopen += 1

        rows.append({
            "isotope": name, "A": A, "strands": n,
            "insertions_tested": tested,
            "square_spans_three_components": span3,
            "spanning_triples_with_all_linking_zero": reopen,
        })
        tot_tested += tested
        tot_span3 += span3
        tot_reopen += reopen

    b = WitnessBuilder(
        name="cyclic-square-does-not-reopen-milnor",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md")
    b.set_description(
        "EXPLORATORY. Route 3's result rests on a premise true only for MONOTONE words: "
        "each summand of the connected-sum closure touches at most 2 components. Sibling "
        "#6561 proves the cyclic square (g_m g_{m+1})^2 is the ONLY non-monotone shape "
        "yielding a Markov-trace cross term, making it the natural candidate to break "
        "that premise. It DOES: measured, it spans 3 distinct components in 188 of 694 "
        "insertions -- so the tempting reading that it is local knotting on one component "
        "(its closure T(3,2) is a knot) is WRONG. CORRECTED 2026-09-04 -- the original "
        "reading, that the conclusion survives for a "
        "different reason: in ALL 188 cases at least one pairwise linking number among "
        "the three spanned components is nonzero, so Delta != 0 and mubar is not a "
        "genuine integer there anyway. The insertion that joins three components is the "
        "same one that links them -- IS RETRACTED. Delta != 0 means mubar lives in Z/Delta, "
        "NOT that there is no obstruction; a nonzero residue is a nonvanishing "
        "invariant. This probe never computed mubar. It is nonzero in 2 of these 188 "
        "all-positive spanning insertions, at Delta = 2 with mubar = 1 -- exactly route "
        "3's one-bit residual. See mixed_sign_cyclic_square_does_reopen_milnor_probe.py, "
        "which also sweeps all 16 inserted-sign patterns (563 of 3008 nonzero) and "
        "re-measures the UNPERTURBED carrier as a control (294 triples, 0 nonzero), so "
        "route 3 at Delta = 0 and its Lean are untouched. Scope (a), narrow: one shape, all-positive inserted "
        "crossings, sampled word positions, 4 isotopes. NOT a proof that no non-monotone "
        "word reopens route 3, and the Delta = 2 one-bit triples are untouched. Nothing "
        "wired."
    )

    b.add_data("what_is_being_tested", {
        "route_3_premise": ("each summand touches at most 2 components -- TRUE FOR "
                            "MONOTONE WORDS, which is how the closure decomposes as "
                            "#_g T(2, e_g)"),
        "the_candidate": ("the cyclic square (g_m g_{m+1})^2, which #6561's "
                          "RevisitClassCrossTerm.lean shows is the ONLY non-monotone "
                          "shape producing a trace cross term. It spans THREE strands."),
        "my_wrong_guess": ("that it would be local knotting on one component, since its "
                           "closure T(3,2) is a knot and local knotting changes no Milnor "
                           "invariant. Measured: it spans up to 3 DISTINCT components. "
                           "Recorded because the guess was reasonable and wrong."),
        "insertion_positions": ("sampled across the word, not only appended -- braid "
                                "letters do not commute, so an append-only test would be "
                                "a weaker claim than it looks"),
    })
    b.add_data("measured_per_isotope", {"rows": rows})
    b.add_data("the_result", {
        "premise_breaks": True,
        "insertions_spanning_three_components": tot_span3,
        "of_those_with_all_pairwise_linking_zero": tot_reopen,
        "reading": ("the premise really does break -- but in every spanning case at least "
                    "one pairwise linking number is nonzero, so Delta != 0 and mubar is "
                    "not a genuine integer there. Route 3's PREMISE is monotone-specific "
                    "and does break; route 3's CONCLUSION ALSO FAILS on this shape, at "
                    "Delta = 2 -- see the RETRACTED note above and "
                    "mixed_sign_cyclic_square_does_reopen_milnor_probe.py."),
    })
    b.add_data("what_this_does_NOT_establish", {
        "other_non_monotone_words": ("NOT tested. This is one shape -- the one #6561 "
                                     "singles out -- not the non-monotone class"),
        "delta_2_triples": "NOT examined; still route 3's stated residual",
        "sign_choices": ("inserted crossings are all positive. A mixed-sign insertion "
                         "could cancel a linking number and is not covered"),
        "the_lean": ("unchanged. MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean "
                     "proves what it proves; this measures the reach of its hypothesis"),
        "scope": "(a), narrow",
    })

    b.add_assertion(
        name="cyclic_square_DOES_break_the_at_most_two_components_premise",
        computed="1" if tot_span3 > 0 else "0", expected="1", tolerance="0", unit="bool",
        source=("recorded as a POSITIVE result because it refutes my own first guess. If "
                "this ever reads 0 the premise would be shape-independent and this whole "
                "probe would be unnecessary."),
    )
    b.add_assertion(
        name="spanning_triples_that_would_reopen_route_3",
        computed=str(tot_reopen), expected="0", tolerance="0", unit="triples",
        source=("THE RESULT. Of the insertions whose square spans three distinct "
                "components, none leaves all three pairwise linking numbers zero -- so "
                "mubar is not a genuine integer on any of them and route 3's conclusion "
                "is untouched by this shape."),
    )
    b.add_assertion(
        name="insertions_tested_across_positions_and_isotopes",
        computed="1" if tot_tested > 0 else "0", expected="1", tolerance="0",
        unit="bool",
        source=("recorded so the SIZE of the search is visible in the witness rather than "
                f"only in prose ({tot_tested} insertions): a null result is only as strong as what was searched."),
    )
    b.add_assertion(
        name="all_linking_numbers_are_integers",
        computed=str(half_integer_seen), expected="0", tolerance="0", unit="violations",
        source=("a REAL check, counted per pair per insertion across all "
                f"{tot_tested} words: two closed curves cross an even number of times, "
                "so an ODD crossing sum means the accounting is wrong. qou-768r's "
                "route-3 pass hit exactly that (lk = -3/2) by resolving an averaged "
                "letter to the identity rather than to a crossing sign. An earlier "
                "draft of this assertion was VACUOUS -- the counter was never "
                "incremented -- and is fixed here rather than shipped."),
    )

    out = b.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "reads no q0. Inputs are permutation cycles and integer linking numbers of "
            "modified braid words. No substrate pin is evaluated on any path, so no "
            "q0Value exists."
        ),
    })
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
