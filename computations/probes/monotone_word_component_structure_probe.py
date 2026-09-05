#!/usr/bin/env python3
# polynomial_q_not_applicable: permutation cycles and integer linking numbers over
# monotone braid words; no q enters anywhere.
"""Tier 1 is a THEOREM, and the same argument derives the path linking graph.

Beans qou-768r (route 3), qou-2g9j. Measures the five predictions of
`QOU/Mass/MonotoneWordComponentStructure.lean` (sorry-free, lean-direct exit 0), which
closes the tier-1 gap `EpsEqFromMonotonicity.lean` left open.

THE ARGUMENT, in one paragraph. A monotone word runs its generators in ascending order,
one contiguous run each. Generator `g` moves only positions `g` and `g+1`, and every
earlier run touched only positions `< g+1` -- so when run `R_g` begins, position `g+1`
STILL HOLDS STRAND `g+1`. Every crossing of that run is therefore between one fixed pair
of strands, `(pStart g, g+1)`, and the run either restores the pair (`e_g` even) or
swaps it (`e_g` odd). The closure's permutation is thus `prod over {g : e_g odd} of
sigma_g`, whose cycles are the maximal consecutive blocks of odd-exponent generators.
Consequence: an ODD run crosses two strands of the SAME component (self-crossings,
invisible to linking); an EVEN run crosses two strands of ADJACENT components.

FIVE PREDICTIONS, measured BEFORE the Lean was written:

    P1  inter-component crossings occur ONLY at even-exponent generators
    P2  components are consecutive intervals of strand indices
    P3  the linking graph is EXACTLY the path (lk != 0 iff the components are adjacent)
    P4  mu = 1 + #{g : e_g even}
    P5  every even run's crossings are ALL inter-component

WHAT THIS BUYS. Tier 1 of `eps_eq` was five measured braid-word facts; each is now a
reading of the single Lean statement `components_differ_iff_even`. Even run length is
`even_of_components_differ`; one generator per component pair is
`distinct_even_generators_distinct_pairs`; generator order matching component order is
`compIdx_mono`.

AND IT DERIVES SOMETHING THE WHOLE ARC ASSUMED. P3 is the `P_μ` path shape.
`PathCarrier` in `OneSeparatedComponentSufficesForMilnorVanishing.lean` takes "lk
vanishes off consecutive components" as a HYPOTHESIS, and the arc has carried it as a
measurement across 7 isotopes and both crossing-resolution branches since the carrier
was derived. `linking_only_between_adjacent` proves it for every monotone word.

WHAT IS STILL NOT FORMALISED, and it is the honest remainder: that `pStart` and
`compIdx` -- the two one-line recursions the Lean reasons about -- really do describe a
monotone braid closure's strand positions and cycles. That step needs braid words,
position permutations and cycle decomposition as Lean objects. This probe is what stands
in for it: the recursions' predictions are checked against `analyse`, the same routine
every other probe in this arc uses.

SCOPE (a) for the measurement. The Lean theorems are unconditional. EXPLORATORY;
nothing wired.
"""

from __future__ import annotations

import collections
import importlib.util
import pathlib
import random
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "_mubar", HERE / "milnor_mubar_vanishes_on_every_triple_probe.py")
_mubar_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mubar_mod)
analyse = _mubar_mod.analyse

ISOTOPES = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"),
            (3, 3, "6Li"), (4, 4, "8Be"), (6, 6, "12C")]
BRANCHES = [(+1, "sigma"), (-1, "sigma^-1")]
SEED = 20260904
TRIALS = 400
STRANDS = (4, 10)
RUN_EXPONENT = (1, 4)

PREDICTIONS = ["P1_inter_crossings_only_at_even_runs",
               "P2_components_are_strand_intervals",
               "P3_linking_graph_is_exactly_the_path",
               "P4_mu_eq_one_plus_even_run_count",
               "P5_every_even_run_is_wholly_inter_component"]


def check(runs, n, acc):
    """`runs` is `[(generator, sign, exponent)]`, ascending, one entry per generator."""
    word = []
    for (g, s, ex) in runs:
        word += [(g, s)] * ex
    comp, _lam, lk, mu = analyse(word, n)
    acc["words"] += 1

    perm = list(range(n))
    inter = collections.Counter()
    for (g, _s) in word:
        if comp[perm[g]] != comp[perm[g + 1]]:
            inter[g] += 1
        perm[g], perm[g + 1] = perm[g + 1], perm[g]
    evens = {g for (g, _s, ex) in runs if ex % 2 == 0}

    if set(inter) <= evens:
        acc["P1_inter_crossings_only_at_even_runs"] += 1

    by_comp = collections.defaultdict(list)
    for strand, c in enumerate(comp):
        by_comp[c].append(strand)
    if all(v == list(range(min(v), max(v) + 1)) for v in by_comp.values()):
        acc["P2_components_are_strand_intervals"] += 1

    path = all((lk.get((i, j), 0) != 0) == (j == i + 1)
               for i in range(mu) for j in range(i + 1, mu))
    if path:
        acc["P3_linking_graph_is_exactly_the_path"] += 1

    if mu == 1 + len(evens):
        acc["P4_mu_eq_one_plus_even_run_count"] += 1

    if all(inter.get(g, 0) == ex for (g, _s, ex) in runs if ex % 2 == 0):
        acc["P5_every_even_run_is_wholly_inter_component"] += 1


def carrier_runs(Z, N, sgn):
    runs = []
    for (g, _ct) in atom_canonical_crossings(Z, N):
        if runs and runs[-1][0] == g:
            runs[-1] = (g, sgn, runs[-1][2] + 1)
        else:
            runs.append((g, sgn, 1))
    return runs


def main() -> int:
    carrier: collections.Counter = collections.Counter()
    for (sgn, _bn) in BRANCHES:
        for (Z, N, _name) in ISOTOPES:
            check(carrier_runs(Z, N, sgn), 3 * (Z + N), carrier)

    rnd = random.Random(SEED)
    rand: collections.Counter = collections.Counter()
    for _ in range(TRIALS):
        n = rnd.randint(*STRANDS)
        runs = [(g, rnd.choice([1, -1]), rnd.randint(*RUN_EXPONENT))
                for g in range(n - 1)]
        check(runs, n, rand)

    total = carrier["words"] + rand["words"]
    combined = {k: carrier[k] + rand[k] for k in PREDICTIONS}
    all_hold = all(combined[k] == total for k in PREDICTIONS)

    b = WitnessBuilder(
        name="monotone-word-component-structure",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md")
    b.set_description(
        "EXPLORATORY. Closes the tier-1 gap EpsEqFromMonotonicity.lean left open, and "
        "derives the path linking graph the carrier arc has assumed throughout. "
        "ARGUMENT: in a monotone word generator g moves only positions g, g+1, and every "
        "earlier run touched only positions < g+1 -- so when run R_g begins position g+1 "
        "still holds strand g+1, and every crossing of that run is between ONE fixed "
        "strand pair. The run restores the pair when e_g is even and swaps it when odd, "
        "so the closure permutation is the product of sigma_g over odd runs and its "
        "cycles are the maximal consecutive odd blocks. Hence an ODD run crosses two "
        "strands of the SAME component and an EVEN run crosses ADJACENT components. Five "
        "predictions follow and all hold on every monotone word measured: "
        "inter-component crossings only at even runs; components are strand intervals; "
        "the linking graph is EXACTLY the path; mu = 1 + #even runs; every even run is "
        "wholly inter-component. Tier 1's five facts are now readings of one Lean "
        "statement (components_differ_iff_even), and P3 is linking_only_between_adjacent "
        "-- the P_mu hypothesis of PathCarrier, proved. STILL NOT FORMALISED: that the "
        "two recursions pStart/compIdx really model a monotone closure; that needs braid "
        "words and cycle decomposition as Lean objects, and this probe stands in for it. "
        "Scope (a) for the measurement; the Lean theorems are unconditional. Nothing "
        "wired."
    )

    b.add_data("the_argument", {
        "why_one_pair_per_run": ("generator g moves only positions g, g+1, and runs are "
                                 "ascending, so nothing has yet touched position g+1 when "
                                 "R_g begins -- it still holds strand g+1"),
        "the_recursion": ("pStart 0 = 0; pStart (g+1) = g+1 if e_g even else pStart g. "
                          "An even run restores the pair, an odd run swaps it"),
        "the_permutation": ("product of sigma_g over {g : e_g odd}; its cycles are the "
                            "maximal consecutive blocks of odd-exponent generators"),
        "the_dichotomy": ("odd run -> both strands in ONE component (self-crossings, "
                          "invisible to linking); even run -> ADJACENT components"),
    })
    b.add_data("measured", {
        "carrier": dict(carrier), "random_monotone": dict(rand),
        "combined": combined, "words": total,
    })
    b.add_data("what_tier_1_becomes", {
        "even_run_length": "even_of_components_differ",
        "one_generator_per_component_pair": "distinct_even_generators_distinct_pairs",
        "generator_order_matches_component_order": "compIdx_mono",
        "all_from": ("the single statement components_differ_iff_even -- the two strands "
                     "of run g differ in component exactly when e_g is even, and then by "
                     "exactly one"),
    })
    b.add_data("what_it_also_derives", {
        "P3_is_the_path_hypothesis": ("PathCarrier in "
                                      "OneSeparatedComponentSufficesForMilnorVanishing"
                                      ".lean assumes lk vanishes off consecutive "
                                      "components; linking_only_between_adjacent proves "
                                      "it for every monotone word"),
        "why_that_matters": ("the P_mu shape has been carried as a MEASUREMENT since the "
                             "carrier was derived -- 7 isotopes, both branches -- and it "
                             "is a theorem"),
    })
    b.add_data("still_not_formalised", {
        "the_remainder": ("that pStart and compIdx describe a monotone braid closure's "
                          "strand positions and cycles"),
        "what_it_would_need": ("braid words, position permutations and cycle "
                               "decomposition as Lean objects"),
        "what_stands_in_for_it": ("this probe: the recursions' predictions checked "
                                  "against `analyse`, the same routine every other probe "
                                  "in this arc uses"),
    })

    for k in PREDICTIONS:
        b.add_assertion(
            name=k, computed=str(combined[k]), expected=str(total), tolerance="0",
            unit="words",
            source=(f"over {carrier['words']} carrier branch-isotope pairs and "
                    f"{rand['words']} random monotone words."),
        )
    b.add_assertion(
        name="ALL_FIVE_predictions_hold_on_EVERY_word",
        computed="1" if all_hold else "0", expected="1", tolerance="0", unit="bool",
        source=("stated as its own assertion so a partial failure cannot hide behind four "
                "passing rows."),
    )

    out = b.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "reads no q0. Inputs are monotone braid words and their closures' permutation "
            "cycles and integer linking numbers. No substrate pin is evaluated on any "
            "path."
        ),
    })
    print(f"wrote {out}")
    print(f"words={total}")
    for k in PREDICTIONS:
        print(f"  {k:46s} {combined[k]}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
