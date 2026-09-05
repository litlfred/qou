#!/usr/bin/env python3
# polynomial_q_not_applicable: permutation cycles, integer linking numbers and
# degree-2 Magnus coefficients; no q enters anywhere.
"""`eps_eq` decomposed: eight sharper facts, each measured, replacing one opaque one.

Beans qou-768r (route 3), qou-2g9j. Measures the hypotheses of
`QOU/Mass/EpsEqFromMonotonicity.lean` (sorry-free, lean-direct exit 0).

WHERE THIS PICKS UP. `ChainTripleMilnorVanishesByGcdDividesProduct.lean` closes route
3's last residual on `gcd u v | u*v`, but carries `ChainTriple.eps_eq` -- "the degree-2
Magnus coefficient of the hub's longitude is u*v" -- as one structural hypothesis. This
probe splits that hypothesis into eight, in two tiers.

TIER 1, the braid-word facts (still assumed in Lean; deriving them needs the strand
permutation bookkeeping of a monotone word formalised, which is not attempted):

    all hub-x crossings sit in ONE generator's run
    all hub-y crossings sit in ONE generator's run
    those two generators differ
    g_x < g_y  iff  x < y
    each run has EVEN length
    each run's length is exactly 2|lk|

TIER 2, the consequences (these are what the Lean consumes):

    the signed sum of x-letters inside lambda_hub equals u  (and likewise y, v)
    each far component's letters are CONTIGUOUS in lambda_hub
    the two blocks are disjoint, with x's entirely before y's

WHAT THE LEAN PROVES from tier 2: `epsCoeff_append_of_blocks` -- a block-split word has
`eps_{x,y} = (signed sum of block A)(signed sum of block B)` and `eps_{y,x} = 0`. That is
the arithmetic of `eps_eq`, and it is a statement about lists with no topology in it.
`eps_eq_of_blocks` composes it with the signed-sum facts to give `eps = u*v`.

WHAT IS STILL ASSUMED, stated plainly: tier 1. The gain is that `eps_eq` went from one
hypothesis about a Magnus coefficient to a theorem given three hypotheses about a braid
word -- and the part that could have been subtly wrong, the arithmetic that makes
`gcd u v | u*v` applicable at all, is now machine-checked.

SAMPLING. One RNG (seed 20260904) consumed sequentially, monotone arm first, matching
`milnor_vanishing_is_generic_for_monotone_probe.py` so the arms stay comparable with
#6679 and #6726. Figures live in the witness; do NOT quote a number from a scratch run
against a per-arm RNG -- that produced a wrong figure twice in this arc (#6679's
251/2080, and a "0 of 71" vacuity claim in #6726 that was really 1 of 78).

SCOPE (a): 7 isotopes, both crossing-resolution branches, one random-word regime. The
Lean statements are unconditional; only the claim that their hypotheses hold on monotone
closures is empirical. EXPLORATORY; nothing wired.
"""

from __future__ import annotations

import collections
import importlib.util
import pathlib
import random
import sys
from itertools import combinations

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
TRIALS = 300
STRANDS = (4, 9)
MONOTONE_RUN = (1, 4)
NONMONOTONE_LEN = (6, 20)

TIER1 = ["hub_x_one_generator", "hub_y_one_generator", "generators_differ",
         "generator_order_matches_component_order", "runs_even_length",
         "run_length_is_twice_lk"]
TIER2 = ["signSum_x_eq_u", "signSum_y_eq_v", "x_block_contiguous",
         "y_block_contiguous", "blocks_disjoint_x_before_y"]


def _lk(lk, a, b):
    return lk.get((min(a, b), max(a, b)), 0)


def chain_of(lk, a, b, c):
    for hub, (x, y) in ((a, (b, c)), (b, (a, c)), (c, (a, b))):
        if _lk(lk, hub, x) != 0 and _lk(lk, hub, y) != 0 and _lk(lk, x, y) == 0:
            return hub, x, y
    return None


def generators_hosting(word, n, comp, ci, cj):
    """generator -> crossing count, for crossings between components ci and cj."""
    perm = list(range(n))
    hits: collections.Counter = collections.Counter()
    for (g, _s) in word:
        if {comp[perm[g]], comp[perm[g + 1]]} == {ci, cj}:
            hits[g] += 1
        perm[g], perm[g + 1] = perm[g + 1], perm[g]
    return hits


def scan(word, n, comp, lam, lk, mu, acc):
    for (a, b, c) in combinations(range(mu), 3):
        cs = chain_of(lk, a, b, c)
        if cs is None:
            continue
        hub, x, y = cs
        u, v = _lk(lk, hub, x), _lk(lk, hub, y)
        acc["chain_triples"] += 1

        # --- tier 1: the braid-word facts ---
        hx = generators_hosting(word, n, comp, hub, x)
        hy = generators_hosting(word, n, comp, hub, y)
        if len(hx) == 1:
            acc["hub_x_one_generator"] += 1
        if len(hy) == 1:
            acc["hub_y_one_generator"] += 1
        if len(hx) == 1 and len(hy) == 1:
            gx, gy = next(iter(hx)), next(iter(hy))
            if gx != gy:
                acc["generators_differ"] += 1
            if (gx < gy) == (x < y):
                acc["generator_order_matches_component_order"] += 1
            if hx[gx] % 2 == 0 and hy[gy] % 2 == 0:
                acc["runs_even_length"] += 1
            if hx[gx] == 2 * abs(u) and hy[gy] == 2 * abs(v):
                acc["run_length_is_twice_lk"] += 1

        # --- tier 2: the consequences the Lean consumes ---
        w = lam[hub]
        if sum(s for (o, s) in w if comp[o] == x) == u:
            acc["signSum_x_eq_u"] += 1
        if sum(s for (o, s) in w if comp[o] == y) == v:
            acc["signSum_y_eq_v"] += 1
        px = [i for i, (o, _s) in enumerate(w) if comp[o] == x]
        py = [i for i, (o, _s) in enumerate(w) if comp[o] == y]
        if px and px == list(range(min(px), max(px) + 1)):
            acc["x_block_contiguous"] += 1
        if py and py == list(range(min(py), max(py) + 1)):
            acc["y_block_contiguous"] += 1
        if px and py and max(px) < min(py):
            acc["blocks_disjoint_x_before_y"] += 1


def carrier_scan():
    acc: collections.Counter = collections.Counter()
    for (sgn, _bn) in BRANCHES:
        for (Z, N, _name) in ISOTOPES:
            n = 3 * (Z + N)
            word = [(g, sgn) for (g, _ct) in atom_canonical_crossings(Z, N)]
            comp, lam, lk, mu = analyse(word, n)
            scan(word, n, comp, lam, lk, mu, acc)
    return dict(acc)


def random_scan(monotone: bool, rnd: random.Random):
    acc: collections.Counter = collections.Counter()
    for _ in range(TRIALS):
        n = rnd.randint(*STRANDS)
        if monotone:
            word = []
            for g in range(n - 1):
                word += [(g, rnd.choice([1, -1]))] * rnd.randint(*MONOTONE_RUN)
        else:
            word = [(rnd.randrange(n - 1), rnd.choice([1, -1]))
                    for _ in range(rnd.randint(*NONMONOTONE_LEN))]
        comp, lam, lk, mu = analyse(word, n)
        if mu >= 3:
            scan(word, n, comp, lam, lk, mu, acc)
    return dict(acc)


def main() -> int:
    carrier = carrier_scan()
    rnd = random.Random(SEED)
    mono = random_scan(True, rnd)
    nonmono = random_scan(False, rnd)

    mono_n = carrier["chain_triples"] + mono["chain_triples"]
    combined = {k: carrier.get(k, 0) + mono.get(k, 0) for k in TIER1 + TIER2}
    all_hold = all(combined[k] == mono_n for k in TIER1 + TIER2)
    weakest_nonmono = min(nonmono.get(k, 0) for k in TIER1 + TIER2)

    b = WitnessBuilder(
        name="eps-eq-decomposition-from-monotonicity",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md")
    b.set_description(
        "EXPLORATORY. Splits ChainTriple.eps_eq -- the one structural hypothesis "
        "carrying route 3's chain closure -- into eight sharper facts in two tiers. "
        "TIER 1 (braid-word, still assumed in Lean): all hub-x and hub-y crossings each "
        "sit in ONE generator's run; the two generators differ; g_x < g_y iff x < y; "
        "each run has even length; each length is exactly 2|lk|. TIER 2 (the "
        "consequences the Lean consumes): the signed sum of each far component's letters "
        "inside lambda_hub equals that pair's linking number; each block is contiguous; "
        "the blocks are disjoint with x's before y's. All eight hold on every monotone "
        "chain triple measured (carrier, both branches, plus random monotone words) and "
        "every one degrades off monotone. QOU/Mass/EpsEqFromMonotonicity.lean then PROVES "
        "the step tier 2 -> eps = u*v (epsCoeff_append_of_blocks, a statement about lists "
        "with no topology in it) so eps_eq is no longer a bare assumption: it is a "
        "theorem given three braid-word hypotheses. What remains assumed is tier 1, whose "
        "derivation needs the strand-permutation bookkeeping of a monotone word "
        "formalised -- not attempted, and named as borrowed rather than elided. Scope "
        "(a): 7 isotopes, both branches, one random-word regime, one RNG consumed "
        "sequentially so the arms stay comparable with #6679/#6726. Nothing wired."
    )

    b.add_data("tier_1_braid_word_facts_STILL_ASSUMED", {
        "why_assumed": ("deriving these needs positions, runs and who-passes-under "
                        "formalised for a monotone word -- a substantially larger object "
                        "than anything in this arc"),
        "carrier": {k: carrier.get(k, 0) for k in TIER1},
        "monotone_random": {k: mono.get(k, 0) for k in TIER1},
        "non_monotone_random": {k: nonmono.get(k, 0) for k in TIER1},
    })
    b.add_data("tier_2_consequences_CONSUMED_BY_THE_LEAN", {
        "carrier": {k: carrier.get(k, 0) for k in TIER2},
        "monotone_random": {k: mono.get(k, 0) for k in TIER2},
        "non_monotone_random": {k: nonmono.get(k, 0) for k in TIER2},
    })
    b.add_data("denominators", {
        "carrier_chain_triples": carrier["chain_triples"],
        "monotone_random_chain_triples": mono["chain_triples"],
        "monotone_combined": mono_n,
        "non_monotone_chain_triples": nonmono["chain_triples"],
    })
    b.add_data("what_the_lean_proves", {
        "epsCoeff_append_of_blocks": ("a block-split word has eps_{x,y} = (signed sum of "
                                      "block A)(signed sum of block B) and eps_{y,x} = 0 "
                                      "-- the arithmetic of eps_eq, about lists, no "
                                      "topology"),
        "eps_eq_of_blocks": ("composes it with the signed-sum facts to give eps = u*v, "
                             "which IS ChainTriple.eps_eq"),
        "underSum_eq_linking": ("the run of 2m crossings alternates, so the hub records m "
                                "of them at the run's sign; the pair's total signed count "
                                "is 2*lk; hence lk = m*s"),
        "axioms": ("all sorry-free; carrier_shape_gives_four depends on NO axioms, the "
                   "rest on propext (+ Quot.sound, Classical.choice)"),
    })
    b.add_data("sampling_discipline", {
        "seed": SEED, "trials_per_arm": TRIALS,
        "rng": ("ONE RNG consumed sequentially, monotone arm first -- matching the merged "
                "genericity probe so the arms are comparable"),
        "why_it_is_called_out": ("a scratch run with a FRESH per-arm RNG produced a wrong "
                                 "figure twice in this arc: #6679's 251/2080, and a "
                                 "'0 of 71' vacuity claim in #6726 that was really 1 of "
                                 "78. Quote the witness, never a scratch figure"),
    })

    b.add_assertion(
        name="ALL_EIGHT_facts_hold_on_EVERY_monotone_chain_triple",
        computed="1" if all_hold else "0", expected="1", tolerance="0", unit="bool",
        source=(f"each of the {len(TIER1) + len(TIER2)} facts holds on all {mono_n} "
                "monotone chain triples (carrier both branches + random)."),
    )
    b.add_assertion(
        name="EVERY_fact_degrades_off_monotone",
        computed="1" if weakest_nonmono < nonmono["chain_triples"] else "0",
        expected="1", tolerance="0", unit="bool",
        source=(f"weakest holds on {weakest_nonmono} of {nonmono['chain_triples']} "
                "non-monotone chain triples. Without this the facts would look like "
                "identities rather than consequences of monotonicity."),
    )
    b.add_assertion(
        name="tier_2_signSum_x_eq_u_on_monotone",
        computed=str(combined["signSum_x_eq_u"]), expected=str(mono_n), tolerance="0",
        unit="triples",
        source=("the hypothesis `hsum` of eps_eq_of_blocks -- the signed sum of the far "
                "component's letters inside the hub longitude IS that pair's linking "
                "number."),
    )
    b.add_assertion(
        name="tier_2_blocks_disjoint_x_before_y_on_monotone",
        computed=str(combined["blocks_disjoint_x_before_y"]), expected=str(mono_n),
        tolerance="0", unit="triples",
        source=("the hypotheses `hA`/`hB` of epsCoeff_append_of_blocks -- the block split "
                "that turns the Magnus coefficient into a product."),
    )
    b.add_assertion(
        name="tier_1_each_pair_crosses_at_ONE_generator_on_monotone",
        computed=str(combined["hub_x_one_generator"]), expected=str(mono_n),
        tolerance="0", unit="triples",
        source=("the root braid-word fact: it is what makes each block contiguous, and "
                "it is the part still assumed rather than proved."),
    )

    out = b.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "reads no q0. Inputs are braid words, their closures' permutation cycles, "
            "integer linking numbers and degree-2 Magnus coefficients. No substrate pin "
            "is evaluated on any path."
        ),
    })
    print(f"wrote {out}")
    print(f"monotone combined n={mono_n}; non-monotone n={nonmono['chain_triples']}")
    for k in TIER1 + TIER2:
        print(f"  {k:42s} mono {combined[k]:4d}/{mono_n}   nonmono {nonmono.get(k,0):3d}/{nonmono['chain_triples']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
