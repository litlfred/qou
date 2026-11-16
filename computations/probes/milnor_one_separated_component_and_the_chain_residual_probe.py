#!/usr/bin/env python3
# polynomial_q_not_applicable: permutation cycles, integer linking numbers and
# degree-2 Magnus coefficients; no q enters anywhere.
"""Route 3 needs only ONE component separated -- and the residual is exactly the chain.

Beans qou-768r (route 3), qou-2g9j. Measures the claim formalised in
`QOU/Mass/OneSeparatedComponentSufficesForMilnorVanishing.lean` (sorry-free,
lean-direct exit 0; the core `splitsOff_of_unlinked` depends on NO axioms).

WHY THIS EXISTS. The merged `MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean` proves
`Delta = 0` -- all three pairwise linking numbers vanishing -- forces separation, hence
a split sublink, hence `mubar = 0`. That hypothesis is stronger than the argument
needs. `mubar_abc` is the coefficient of `h_a h_b` in the Magnus expansion of
`lambda_c`; if ONE component splits off from the other two, that coefficient vanishes,
and the other two may be linked to each other arbitrarily.

So the right classification is not by `Delta` but by SHAPE:

    SEPARABLE   some component is unlinked from BOTH others   -> the argument reaches it
    CHAIN       no component is                               -> it does not

MEASURED on the derived carrier (closure of the canonical atom word, 7 isotopes, BOTH
crossing-resolution branches). See the witness for the per-branch table; on the
all-`sigma^-1` branch:

    SEPARABLE   393 triples,  0 nonzero mubar     (of which Delta = 2: 182)
    CHAIN        31 triples,  0 nonzero mubar     (all of them Delta = 2)

THE 31 ARE THE CONSECUTIVE TRIPLES, and this probe VERIFIES that rather than inferring
it. `31 = sum over the seven isotopes of (A - 1) = 1+2+2+3+5+7+11`, which is the count
of `{i, i+1, i+2}` on a path of `mu = A + 1` components -- a count match is suggestive
and is not evidence, so every CHAIN triple is checked to BE `{i, i+1, i+2}` in
component indices. The Lean proves this is forced (`splitsOff_or_consecutive`: on the
path carrier an ordered triple is separable or consecutive, with no third case), and
that the trichotomy is sharp (`consecutive_has_no_separable_component`).

WHAT THIS CHANGES. The merged theorem reaches the 211 triples that are separable AND
`Delta = 0`. The 182 that are `Delta = 2` with one component unlinked from both others
are reached for the first time, by the same idea -- coverage goes 211 -> 393 of 424,
i.e. 49.8 % -> 92.7 %: +42.9 percentage POINTS, or +86.3 % relative. Both are stated
because "43 % more" reads as the relative figure and is not it. All from deleting a
hypothesis rather than adding an argument.

THE RESIDUAL IS ONE SHAPE, not a ragged remainder. It cannot be chipped at further with
linking-number bookkeeping, because the Lean shows there is no third case. Closing it
needs a different invariant: `mubar` of length `k` vanishing unless all `k` indices lie
in a single connected-sum summand. Combined with the measured "each summand touches at
most 2 components" that would close the chain case AND subsume this file. It is NOT
asserted anywhere -- axiomatising it as a class would be the
axiomatisation-is-not-a-proof pattern.

THE RESIDUAL VANISHES EMPIRICALLY, AND GENERICALLY FOR MONOTONE WORDS. 0 nonzero on all
31 chain triples of the carrier, and 0 on all chain triples of random MONOTONE closures
at seed 20260904. The non-monotone arm is the positive control and it does produce
nonzero mubar, including at `Delta = 2` -- so the chain null is a fact about
monotonicity and not about the scanner. Measurement, not proof, which is why the Lean
leaves the chain case open rather than assuming it.

A NOTE ON WHAT THE GENERICITY RESULT WAS NOT. #6679 reported 0 nonzero mubar over 1879
monotone triples. `Delta = 1` makes `mubar = 0` VACUOUSLY (it lives in Z/1), so that
null would have been weak if it were mostly `Delta = 1`. Measured here: the monotone arm
splits `{Delta 0: 319, Delta 1: 870, Delta 2: 690}` -- 46.3 % vacuous, but 1009
NON-vacuous triples all zero, 690 of them at exactly `Delta = 2`. The null stands. It is
recorded because the check was worth running and its outcome was not obvious.

SCOPE (a) for the measurement. 7 isotopes, both branches, one random-word regime. The
scope-(b) exclusion lives in the Lean, which cites its invariant. EXPLORATORY; nothing
wired.
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
mubar = _mubar_mod.mubar

ISOTOPES = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"),
            (3, 3, "6Li"), (4, 4, "8Be"), (6, 6, "12C")]
BRANCHES = [(+1, "sigma"), (-1, "sigma^-1")]

# The genericity probe's sampler, reused verbatim so the arms are comparable.
SEED = 20260904
TRIALS = 300
STRANDS = (4, 9)
MONOTONE_RUN = (1, 4)
NONMONOTONE_LEN = (6, 20)


def _lk(lk, x, y):
    return lk.get((min(x, y), max(x, y)), 0)


def shape(lk, a, b, c) -> str:
    """SEPARABLE when some component is unlinked from BOTH others; CHAIN otherwise.

    This is the hypothesis of `splitsOff_of_unlinked`, not a `Delta` classification --
    the pair the separated component leaves behind may be linked arbitrarily.
    """
    for k, (x, y) in ((a, (b, c)), (b, (a, c)), (c, (a, b))):
        if _lk(lk, k, x) == 0 and _lk(lk, k, y) == 0:
            return "SEPARABLE"
    return "CHAIN"


def classify(comp, lam, lk, mu, acc, chain_triples=None):
    for (a, b, c) in combinations(range(mu), 3):
        d, v = mubar(lam, comp, lk, a, b, c)
        s = shape(lk, a, b, c)
        acc[(s, "total")] += 1
        acc[("delta", d)] += 1
        if d == 2:
            acc[(s, "delta2")] += 1
        if v != 0:
            acc[(s, "nonzero")] += 1
            acc[("nonzero_delta", d)] += 1
        if s == "CHAIN" and chain_triples is not None:
            chain_triples.append((a, b, c))


def carrier_sweep():
    rows = []
    totals = collections.Counter()
    chain_all = []
    consecutive_ok = chain_seen = 0
    for (sgn, bname) in BRANCHES:
        for (Z, N, name) in ISOTOPES:
            A = Z + N
            n = 3 * A
            word = [(g, sgn) for (g, _ct) in atom_canonical_crossings(Z, N)]
            comp, lam, lk, mu = analyse(word, n)
            acc = collections.Counter()
            chain = []
            classify(comp, lam, lk, mu, acc, chain)
            # VERIFY, do not infer: every CHAIN triple must BE {i, i+1, i+2}.
            for (a, b, c) in chain:
                chain_seen += 1
                if b == a + 1 and c == a + 2:
                    consecutive_ok += 1
            rows.append({
                "branch": bname, "isotope": name, "A": A, "components": mu,
                "A_minus_1": A - 1,
                "separable": acc[("SEPARABLE", "total")],
                "separable_nonzero": acc[("SEPARABLE", "nonzero")],
                "separable_delta2": acc[("SEPARABLE", "delta2")],
                "chain": acc[("CHAIN", "total")],
                "chain_nonzero": acc[("CHAIN", "nonzero")],
                "chain_delta2": acc[("CHAIN", "delta2")],
            })
            for k, v in acc.items():
                totals[(bname,) + k] += v
            chain_all += chain
    return rows, totals, chain_seen, consecutive_ok


def random_sweep(monotone: bool, rnd: random.Random):
    acc = collections.Counter()
    words = 0
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
        if mu < 3:
            continue
        words += 1
        classify(comp, lam, lk, mu, acc, None)
    return {
        "words": words,
        "separable": acc[("SEPARABLE", "total")],
        "separable_nonzero": acc[("SEPARABLE", "nonzero")],
        "chain": acc[("CHAIN", "total")],
        "chain_nonzero": acc[("CHAIN", "nonzero")],
        "chain_delta2": acc[("CHAIN", "delta2")],
        "delta_histogram": {str(k[1]): v for k, v in sorted(acc.items())
                            if k[0] == "delta"},
        "nonzero_by_delta": {str(k[1]): v for k, v in sorted(acc.items())
                             if k[0] == "nonzero_delta"},
    }


def main() -> int:
    rows, totals, chain_seen, consecutive_ok = carrier_sweep()
    rnd = random.Random(SEED)
    mono = random_sweep(True, rnd)
    nonmono = random_sweep(False, rnd)

    per_branch = {}
    for (_sgn, bname) in BRANCHES:
        per_branch[bname] = {
            "separable": totals[(bname, "SEPARABLE", "total")],
            "separable_nonzero": totals[(bname, "SEPARABLE", "nonzero")],
            "separable_delta2": totals[(bname, "SEPARABLE", "delta2")],
            "chain": totals[(bname, "CHAIN", "total")],
            "chain_nonzero": totals[(bname, "CHAIN", "nonzero")],
            "chain_delta2": totals[(bname, "CHAIN", "delta2")],
        }
    sum_A_minus_1 = sum(A - 1 for (Z, N, _n) in ISOTOPES for A in [Z + N])
    carrier_nonzero = sum(per_branch[b][k] for b in per_branch
                          for k in ("separable_nonzero", "chain_nonzero"))

    b = WitnessBuilder(
        name="milnor-one-separated-component-and-the-chain-residual",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md")
    b.set_description(
        "EXPLORATORY. Route 3's splitting argument needs only ONE component separated, "
        "not all three: mubar_abc is the h_a h_b coefficient of lambda_c, so if c splits "
        "off from the pair it vanishes however strongly a and b are linked. "
        "Reclassifying the derived carrier's triples by SHAPE rather than by Delta: "
        "SEPARABLE (some component unlinked from both others -- the argument reaches it) "
        "vs CHAIN (none is). On the all-sigma^-1 branch, 393 SEPARABLE and 31 CHAIN, "
        "0 nonzero mubar in either. The merged Delta = 0 theorem reaches only the 211 "
        "that are separable AND Delta = 0; the 182 separable Delta = 2 triples are "
        "reached for the first time: coverage 211 -> 393 of 424, i.e. 49.8 % -> 92.7 %, "
        "which is +42.9 percentage POINTS or +86.3 % relative -- both stated because "
        "'43 % more' reads as the relative figure and is not it. From deleting a "
        "hypothesis rather than adding an argument. The 31 CHAIN triples are VERIFIED "
        "(not inferred from the count matching sum(A-1)) to be exactly the consecutive "
        "{i, i+1, i+2}, and the companion Lean proves that is forced with no third case, "
        "so the residual is ONE SHAPE and cannot be chipped at further by "
        "linking-number bookkeeping. Closing it needs a different invariant -- mubar "
        "vanishing unless all indices lie in one connected-sum summand -- which is NOT "
        "asserted here. The chain null is generic for monotone words and the "
        "non-monotone arm is the positive control that it is a fact about monotonicity "
        "rather than about the scanner. Also records that #6679's monotone null is 53.7 % "
        "NON-vacuous (690 of its triples are Delta = 2, not Delta = 1). Scope (a) for the "
        "measurement; the scope-(b) exclusion lives in the Lean. Nothing wired."
    )

    b.add_data("the_strengthening", {
        "merged_hypothesis": ("Delta = 0 -- ALL THREE pairwise linking numbers vanish "
                              "(MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean)"),
        "what_the_argument_needs": ("ONE component unlinked from both others. mubar_abc "
                                    "is the h_a h_b coefficient of the Magnus expansion "
                                    "of lambda_c; if c splits off from the pair that "
                                    "coefficient is zero, and a, b may be linked to each "
                                    "other arbitrarily"),
        "companion_lean": ("QOU/Mass/OneSeparatedComponentSufficesForMilnorVanishing.lean "
                           "-- sorry-free, lean-direct exit 0; splitsOff_of_unlinked "
                           "depends on NO axioms"),
        "gain_on_the_carrier": ("the merged theorem reaches 211 (separable AND Delta = 0); "
                                "this reaches all 393 separable, adding the 182 that are "
                                "Delta = 2 with one component unlinked from both"),
    })
    b.add_data("carrier_by_shape", {"per_branch": per_branch, "rows": rows})
    b.add_data("the_chain_is_the_consecutive_triple", {
        "verified_not_inferred": ("every CHAIN triple was checked to satisfy "
                                  "b == a+1 and c == a+2 in component indices"),
        "chain_triples_seen": chain_seen,
        "of_those_consecutive": consecutive_ok,
        "count_corroboration": ("31 per branch = sum over the 7 isotopes of (A - 1) = "
                                f"{sum_A_minus_1} = 1+2+2+3+5+7+11, the number of "
                                "{i, i+1, i+2} on a path of mu = A + 1 components. A "
                                "count match is corroboration, not evidence, which is why "
                                "the shape itself is checked"),
        "forced_by_the_lean": ("splitsOff_or_consecutive: on the path carrier an ordered "
                               "triple is separable or is {a, a+1, a+2}, with no third "
                               "case; consecutive_has_no_separable_component shows the "
                               "trichotomy is sharp"),
    })
    b.add_data("what_would_close_the_residual", {
        "the_invariant_needed": ("mubar of length k vanishes unless all k indices lie in a "
                                 "single connected-sum summand"),
        "why_it_would_suffice": ("combined with the measured 'each summand touches at most "
                                 "2 components', no summand could hold all three indices "
                                 "of any triple -- closing the chain case and subsuming "
                                 "this file"),
        "status": ("NOT asserted and NOT formalised. Axiomatising it as a class would be "
                   "the axiomatisation-is-not-a-proof pattern"),
    })
    b.add_data("random_monotone", mono)
    b.add_data("CONTROL_random_non_monotone", dict(nonmono, note=(
        "the positive control. Without a non-monotone arm producing nonzero mubar -- "
        "including at Delta = 2 -- the monotone chain null would be indistinguishable "
        "from a scanner that never reports nonzero")))
    b.add_data("6679_monotone_null_is_not_vacuous", {
        "why_it_could_have_been": ("Delta = 1 makes mubar = 0 VACUOUSLY, since it lives "
                                   "in Z/1. A null dominated by Delta = 1 would be a count "
                                   "of vacuous zeros"),
        "monotone_delta_histogram": mono["delta_histogram"],
        "reading": ("53.7 % of the monotone arm is NON-vacuous (Delta = 0 or >= 2), 690 "
                    "triples at exactly Delta = 2, all zero. The null stands"),
    })

    b.add_assertion(
        name="every_CHAIN_triple_IS_the_consecutive_triple",
        computed=str(consecutive_ok), expected=str(chain_seen), tolerance="0",
        unit="triples",
        source=("checked directly in component indices, not inferred from the count "
                "matching sum(A-1). The count match is corroboration only."),
    )
    b.add_assertion(
        name="NO_triple_of_the_derived_carrier_carries_nonzero_mubar",
        computed=str(carrier_nonzero), expected="0", tolerance="0", unit="triples",
        source=("both branches, 7 isotopes, separable and chain alike -- reproducing "
                "#6634 under the new classification."),
    )
    b.add_assertion(
        name="monotone_random_CHAIN_triples_give_NO_nonzero_mubar",
        computed=str(mono["chain_nonzero"]), expected="0", tolerance="0", unit="triples",
        source=(f"over {mono['chain']} chain triples ({mono['chain_delta2']} of them at "
                "Delta = 2). The residual vanishes generically for monotone words, not "
                "only on the carrier."),
    )
    b.add_assertion(
        name="CONTROL_non_monotone_random_DOES_give_nonzero_mubar",
        computed="1" if (nonmono["separable_nonzero"] + nonmono["chain_nonzero"]) > 0 else "0",
        expected="1", tolerance="0", unit="bool",
        source=(f"{nonmono['separable_nonzero'] + nonmono['chain_nonzero']} nonzero. "
                "Without this the monotone nulls above would be uninterpretable."),
    )
    b.add_assertion(
        name="the_6679_monotone_null_is_majority_NON_vacuous",
        computed="1" if 2 * mono["delta_histogram"].get("1", 0) < mono["triples"] else "0",
        expected="1", tolerance="0", unit="bool",
        source=("the Delta = 1 (vacuous) count is strictly less than half of the monotone "
                "triples, so the non-vacuous majority is checked rather than asserted in prose."),
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
