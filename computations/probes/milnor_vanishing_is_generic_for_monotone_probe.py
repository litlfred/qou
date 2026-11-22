#!/usr/bin/env python3
# polynomial_q_not_applicable: permutation cycles, integer linking numbers and
# degree-2 Magnus coefficients over random braid words; no q enters anywhere.
"""The mubar vanishing is GENERIC FOR MONOTONE closures -- not special to the carrier.

Bean qou-2g9j. This is the genericity check on MY OWN MERGED RESULT (#6634,
046296ff06), and it materially weakens what that result means.

WHAT #6634 CLAIMED, and it stands as measured: `mubar` vanishes on all 606 triples
of the derived carrier -- the closure of the canonical atom braid word -- across 7
isotopes, both crossing-resolution branches, all three indeterminacy classes.

THE QUESTION A REFEREE ASKS NEXT, which AGENTS.md names explicitly: is that special
to THIS carrier, or generic? The corpus's own rule -- "precisely the kind of
coincidence this corpus has repeatedly found to be generic; do NOT read it as
evidence without a genericity check of the kind qou-22vu ran" -- applies to a
vanishing exactly as it applies to a near-match.

MEASURED, and the answer is GENERIC:

    MONOTONE random words       238 words   1879 triples   0 nonzero mubar
    NON-MONOTONE random words   220 words   1456 triples  27 nonzero mubar

(Figures are the PROBE's, at seed 20260904. An exploratory run before this file
existed reported 251/2080 for the monotone arm; it consumed the RNG in a different
order. The witness is authoritative -- do not quote 251/2080.)

So the vanishing is a structural consequence of MONOTONICITY, and says nothing
about the framework's carrier CHOICE. Any monotone word would have given it. The
honest reading of #6634 is therefore:

    NOT  "the derived carrier has vanishing Milnor triples, which is a fact
          about the carrier"
    BUT  "the framework's word is monotone, and monotone closures have vanishing
          Milnor triples"

That is weaker, and it is what the measurement supports. #6634's own conclusion --
that route 3's Delta = 2 residual is closed -- is UNAFFECTED: the residual is
closed either way. What changes is that the closure carries no information about
whether the carrier is the right object.

THE NON-MONOTONE ARM IS A SECOND POSITIVE CONTROL, and that is why it is here
rather than as a separate probe. 27 nonzero out of 1456 triples proves the scan
detects nonzero mubar in the RANDOM regime, not merely on the hand-picked Borromean
example. A monotone zero next to a non-monotone zero would have been evidence the
scanner was broken; a monotone zero next to a non-monotone nonzero is a dichotomy.

CORROBORATES THE MONOTONICITY ROOT independently. Sibling #6561 proved from the
ALGEBRA that a monotone word's Markov trace factorises over generators; #6560's
route 3 argued from the TOPOLOGY that a monotone closure's Delta = 0 triples are
split. This is the same root reached a third way, on random words rather than on
the canonical one, and it now carries a RATE: non-monotone words produce nonzero
mubar at roughly 1.9% of triples in this sampling regime.

SCOPE (a). A sampling result over a specific random-word regime (`n` in 4..9,
run exponents 1..4 monotone / lengths 6..20 non-monotone, seed 20260904), not a
theorem. It does NOT prove every monotone closure has vanishing triples -- for
that see the structural argument in
QOU/Mass/MilnorTriplesAreDefinedExactlyWhereTheyVanish.lean, which covers the
Delta = 0 case and is sorry-free. And the non-monotone RATE is a property of this
sampler, not of any physically meaningful family.

EXPLORATORY; nothing wired.
"""

from __future__ import annotations

import importlib.util
import pathlib
import random
import sys
from itertools import combinations

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402

# Reuse the calibrated machinery from #6634 rather than reimplementing it. Stated
# because a probe depending on a probe is worth noticing: the alternative is a
# second copy of the longitude/Magnus logic, and two copies drifting apart is the
# more expensive failure. That module's Borromean and Hopf controls are what make
# this one's numbers interpretable at all.
_spec = importlib.util.spec_from_file_location(
    "_mubar", HERE / "milnor_mubar_vanishes_on_every_triple_probe.py")
_mubar_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mubar_mod)
analyse = _mubar_mod.analyse
mubar = _mubar_mod.mubar

SEED = 20260904
TRIALS = 300
STRANDS = (4, 9)
MONOTONE_RUN = (1, 4)
NONMONOTONE_LEN = (6, 20)


def scan(word, n):
    """`(mu, triples, nonzero)` for one closure, or None if it has < 3 components."""
    comp, lam, lk, mu = analyse(word, n)
    if mu < 3:
        return None
    triples = nonzero = 0
    for (a, b, c) in combinations(range(mu), 3):
        _d, v = mubar(lam, comp, lk, a, b, c)
        triples += 1
        if v != 0:
            nonzero += 1
    return mu, triples, nonzero


def sweep(monotone: bool, rnd: random.Random) -> dict:
    words = triples = nonzero = 0
    for _ in range(TRIALS):
        n = rnd.randint(*STRANDS)
        if monotone:
            # one contiguous run per generator, ascending -- the shape the canonical
            # atom word has, and the shape that makes the closure a connected sum
            word = []
            for g in range(n - 1):
                word += [(g, rnd.choice([1, -1]))] * rnd.randint(*MONOTONE_RUN)
        else:
            word = [(rnd.randrange(n - 1), rnd.choice([1, -1]))
                    for _ in range(rnd.randint(*NONMONOTONE_LEN))]
        r = scan(word, n)
        if r is None:
            continue
        _mu, t, nz = r
        words += 1
        triples += t
        nonzero += nz
    return {"words": words, "triples": triples, "nonzero_mubar": nonzero}


def main() -> int:
    rnd = random.Random(SEED)
    mono = sweep(True, rnd)
    nonmono = sweep(False, rnd)

    b = WitnessBuilder(
        name="milnor-vanishing-is-generic-for-monotone",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md")
    b.set_description(
        "EXPLORATORY. Genericity check on my own merged result (#6634): mubar vanishes on "
        "all 606 triples of the derived carrier -- but is that special to the carrier? "
        "MEASURED: no. Random MONOTONE braid closures give 0 nonzero mubar over 1879 "
        "triples; random NON-MONOTONE ones give 27 over 1456. So the vanishing is a "
        "structural consequence of MONOTONICITY and says nothing about the framework's "
        "carrier CHOICE -- any monotone word would have given it. #6634's conclusion "
        "(route 3's Delta = 2 residual is closed) is UNAFFECTED; what changes is that "
        "the closure carries no information about whether the carrier is the right "
        "object. The non-monotone arm doubles as a second positive control: it proves "
        "the scan detects nonzero mubar in the RANDOM regime, not only on the "
        "hand-picked Borromean example. Independently corroborates the monotonicity root "
        "that #6561 reached from the algebra and #6560 from the topology. Scope (a): a "
        "sampling result over one random-word regime, not a theorem. Nothing wired."
    )

    b.add_data("what_is_being_checked", {
        "the_merged_claim": ("#6634 / 046296ff06: mubar = 0 on all 606 triples of the "
                             "derived carrier, 7 isotopes, both branches, all Delta classes"),
        "the_referee_question": ("special to THIS carrier, or generic? AGENTS.md names "
                                 "this explicitly -- a coincidence is not evidence without "
                                 "a genericity check of the kind qou-22vu ran, and that "
                                 "applies to a VANISHING as much as to a near-match"),
        "why_it_matters": ("if generic, the vanishing says nothing about the carrier "
                           "CHOICE, which is what the carrier-derivation arc is about"),
    })
    b.add_data("measured", {"monotone": mono, "non_monotone": nonmono})
    b.add_data("the_honest_reading_of_6634", {
        "not": ("'the derived carrier has vanishing Milnor triples, which is a fact about "
                "the carrier'"),
        "but": ("'the framework's word is monotone, and monotone closures have vanishing "
                "Milnor triples'"),
        "unaffected": ("route 3's Delta = 2 residual is closed either way -- the residual "
                       "does not care WHY mubar vanishes"),
        "what_changes": ("the closure carries no information about whether the carrier is "
                         "the right object"),
    })
    b.add_data("second_positive_control", {
        "why_the_non_monotone_arm_is_here": ("a monotone zero beside a non-monotone zero "
                                             "would be evidence the scanner is broken; a "
                                             "monotone zero beside a non-monotone NONZERO "
                                             "is a dichotomy"),
        "detects_nonzero_in_the_random_regime": nonmono["nonzero_mubar"] > 0,
        "note": ("the first controls -- Borromean and Hopf -- live in the reused module "
                 "milnor_mubar_vanishes_on_every_triple_probe.py and are what make these "
                 "numbers interpretable"),
    })
    b.add_data("corroborates_the_monotonicity_root", {
        "6561_algebra": "a monotone word's Markov trace factorises over generators",
        "6560_topology": "a monotone closure's Delta = 0 triples are split",
        "this_probe": ("the same root a third way, on RANDOM words rather than the "
                       "canonical one, and now with a rate"),
    })
    b.add_data("sampling_regime", {
        "seed": SEED, "trials_per_arm": TRIALS, "strands": list(STRANDS),
        "monotone_run_exponent": list(MONOTONE_RUN),
        "non_monotone_length": list(NONMONOTONE_LEN),
        "caveat": ("the non-monotone RATE is a property of this sampler, not of any "
                   "physically meaningful family"),
    })

    b.add_assertion(
        name="monotone_closures_give_NO_nonzero_mubar",
        computed=str(mono["nonzero_mubar"]), expected="0", tolerance="0", unit="triples",
        source=(f"over {mono['triples']} triples from {mono['words']} random monotone "
                "words. This is what makes the carrier's vanishing GENERIC rather than "
                "special."),
    )
    b.add_assertion(
        name="CONTROL_non_monotone_closures_DO_give_nonzero_mubar",
        computed="1" if nonmono["nonzero_mubar"] > 0 else "0", expected="1",
        tolerance="0", unit="bool",
        source=(f"{nonmono['nonzero_mubar']} nonzero over {nonmono['triples']} triples. "
                "The second positive control: without it, the monotone zero would be "
                "indistinguishable from a scanner that never reports nonzero."),
    )
    b.add_assertion(
        name="monotone_triples_scanned",
        computed="1" if mono["triples"] > 0 else "0", expected="1", tolerance="0",
        unit="bool",
        source=("the size of the null result, recorded so it is visible in the witness "
                f"({mono['triples']} triples): a vanishing over few triples would establish nothing."),
    )

    out = b.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "reads no q0. Inputs are randomly generated braid words and their closures' "
            "permutation cycles, integer linking numbers and degree-2 Magnus "
            "coefficients. No substrate pin is evaluated on any path."
        ),
    })
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
