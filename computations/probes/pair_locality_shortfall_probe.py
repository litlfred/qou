#!/usr/bin/env python3
"""How much of the light-nucleus binding no pairwise assembly can reach.

CONTEXT.  Two results landed on main 2026-08-30 from different sessions:

  QOU.Mass.SelfMutualPartition.binding_eq_neg_mutualEnergy  (qou-brng, #6145)
      binding = -(mutual energy) = -(sum over INTER-COMPONENT crossings).
  QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_of_isPairwise  (qou-bhzt, #6101)
      a pairwise-additive binding has b3 == 0 identically.

Every crossing joins exactly two components, so the first sum groups by unordered
pair with no extra hypothesis.  That is one hypothesis away from the second --
namely whether a pair's weight is the SAME in every assembly containing it
("pair-locality").

QOU/Mass/CrossingModelPairLocality.lean (sorry-free, this PR) closes the gap:

  isPairwise_of_pairLocal      pair-local  =>  pairwise-additive
  b3_eq_zero_of_pairLocal      hence b3 == 0
  not_pairLocal_of_b3_ne_zero  hence a nonzero measured b3 REFUTES pair-locality
  brunnian_not_pairLocal       a Brunnian carrier is exactly that violation
  b3_eq_neg_tripleMutual_of_brunnian
                               with the pair terms gone, b3 IS the triple channel
  tripleMutual_neg_of_b3_pos   so b3 > 0 forces an attractive triple channel

WHAT THIS PROBE MEASURES.  The Lean says the measured cumulants refute
pair-locality.  It does not say by HOW MUCH, which is a question about numbers.
This quantifies it: the binding a pair-local (pairwise) assembly can reach at
all, against AME2020, with nothing fitted.

  pair-local prediction:  B_pl(A) = C(A,2) * b2        (b3 = b4 = 0 forced)
  actual:                 B(A)    = C(A,2)*b2 + C(A,3)*b3 + C(A,4)*b4

NO FREE PARAMETERS.  Everything is AME2020 plus the Ursell inversion.  No q0, no
convention, no model -- so neither the convention-C/D question nor the pin can
move any number here.

CROSS-CHECK.  The ratios b3/b2 and b4/b2 are already recorded in the corpus at
computations/deltalambda/deltalambda-kappa-interface-residual-simplex.witness.json
(field derived_rho_F_crosschecks/full_binding_mayer, from the 2026-06-23 audit) as
0.64 and 4.16.  This probe recomputes them independently; agreement is a check,
not a new result.

PRECISION.  mpmath end to end at the repo compute dps; no float arithmetic.
"""
import datetime
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

try:  # P30 provenance stamp; optional so a bare container still runs
    from qou_substrate.witness import WitnessBuilder as _WitnessBuilder
except ImportError:  # pragma: no cover
    from witness_base import WitnessBuilder as _WitnessBuilder

set_compute_dps()

# AME2020 total nuclear binding, MeV -- the same literals as
# probes/he4_body_order_shortfall_location_probe.py and
# probes/mayer_threebody_sign_threshold_probe.py.
AME = {
    "D": AME_B_DEUTERON_MEV_VALIDATION,
    "3H": AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

# Corpus cross-check values (2026-06-23 audit, via the residual-simplex witness).
CORPUS_B3_OVER_B2 = mpf("0.64")
CORPUS_B4_OVER_B2 = mpf("4.16")


def choose(n, k):
    if k > n:
        return 0
    num = 1
    for i in range(k):
        num = num * (n - i) // (i + 1)
    return num


def main():
    b2 = AME["D"]
    bbar3 = (AME["3H"] + AME["3He"]) / 2
    b3 = bbar3 - 3 * b2
    b4 = AME["4He"] - 6 * b2 - 4 * b3

    actual = {2: b2, 3: bbar3, 4: AME["4He"]}

    print("Per-body-order channel strengths (AME2020 Ursell inversion, no fit)\n")
    print(f"  b2 (per pair)   = {mp.nstr(b2, 12):>14} MeV")
    print(f"  b3 (per triple) = {mp.nstr(b3, 12):>14} MeV")
    print(f"  b4 (the quad)   = {mp.nstr(b4, 12):>14} MeV")

    print("\n  What a PAIR-LOCAL assembly can reach (b3 = b4 = 0 is FORCED):\n")
    print(f"    {'A':>2} {'B_pairlocal':>14} {'B_AME':>14} {'shortfall':>13}"
          f" {'irreducible':>12}")
    rows = []
    for A in (2, 3, 4):
        bpl = choose(A, 2) * b2
        act = actual[A]
        short = act - bpl
        frac = short / act
        rows.append({"A": A, "bonds": choose(A, 2),
                     "B_pairlocal_MeV": mp.nstr(bpl, 14),
                     "B_AME_MeV": mp.nstr(act, 14),
                     "shortfall_MeV": mp.nstr(short, 14),
                     "irreducible_fraction": mp.nstr(frac, 10)})
        print(f"    {A:>2} {mp.nstr(bpl, 10):>14} {mp.nstr(act, 10):>14}"
              f" {mp.nstr(short, 10):>13} {mp.nstr(frac * 100, 6):>11}%")

    he4_frac = (AME["4He"] - 6 * b2) / AME["4He"]
    ratio = AME["4He"] / (6 * b2)

    print(f"\n  So {mp.nstr(he4_frac * 100, 6)}% of 4He's binding is IRREDUCIBLY "
          f"many-body:")
    print(f"  no pairwise assembly reaches it, whatever bond functional is used.")
    print(f"  Pair-local ceiling {mp.nstr(6 * b2, 10)} MeV vs AME "
          f"{mp.nstr(AME['4He'], 10)} -- a factor {mp.nstr(ratio, 8)}.")

    # Decomposition of 4He by body order.
    parts = {"pairs (6 x b2)": 6 * b2, "triples (4 x b3)": 4 * b3,
             "quad (1 x b4)": b4}
    print("\n  4He binding by body order:")
    decomp = []
    for k, v in parts.items():
        decomp.append({"channel": k, "MeV": mp.nstr(v, 14),
                       "percent": mp.nstr(v / AME["4He"] * 100, 8)})
        print(f"    {k:<18} {mp.nstr(v, 12):>14} MeV   "
              f"{mp.nstr(v / AME['4He'] * 100, 6):>8}%")

    recon = 6 * b2 + 4 * b3 + b4
    recon_ok = abs(recon - AME["4He"]) < mpf(10) ** (-(mp.dps - 10))

    # Corpus cross-check.
    r32 = b3 / b2
    r42 = b4 / b2
    x32 = abs(r32 - CORPUS_B3_OVER_B2) / CORPUS_B3_OVER_B2
    x42 = abs(r42 - CORPUS_B4_OVER_B2) / CORPUS_B4_OVER_B2
    print(f"\n  corpus cross-check (2026-06-23 audit):")
    print(f"    b3/b2 = {mp.nstr(r32, 10)} vs recorded {mp.nstr(CORPUS_B3_OVER_B2, 4)}"
          f"   rel {mp.nstr(x32, 4)}")
    print(f"    b4/b2 = {mp.nstr(r42, 10)} vs recorded {mp.nstr(CORPUS_B4_OVER_B2, 4)}"
          f"   rel {mp.nstr(x42, 4)}")

    assertions = [
        {"name": "b3 > 0, so the Lean refutation of pair-locality applies "
                 "(not_pairLocal_of_b3_ne_zero)",
         "passed": bool(b3 > 0)},
        {"name": "CONDITIONAL, and its hypothesis is NOT satisfied here: IF a "
                 "carrier had w2 = 0 (CrossingModel.Brunnian) then b3 would be the "
                 "triple channel and b3 > 0 would force an ATTRACTIVE triple mutual "
                 "energy of |b3| per triple (tripleMutual_neg_of_b3_pos). L6a4 is "
                 "Brunnian TOPOLOGICALLY (linking number 0), which does NOT give "
                 "w2 = 0: brunnian_binding_survives proves 0 < countChannel for a "
                 "crossing pair at q > 1, and the b2 != 0 measured right here "
                 "refutes it a second way. What is asserted below is only b3 > 0. "
                 "See QOU.Mass.BrunnianHypothesisNotSatisfied (corrected 2026-09-07)",
         "passed": bool(b3 > 0)},
        {"name": "more than half of 4He's binding is irreducibly many-body",
         "passed": bool(he4_frac > mpf("0.5"))},
        {"name": "the body-order decomposition reconstructs B(4He) exactly",
         "passed": bool(recon_ok)},
        {"name": "b3/b2 and b4/b2 reproduce the corpus values (0.64, 4.16) "
                 "within 1%",
         "passed": bool(x32 < mpf("0.01") and x42 < mpf("0.01"))},
        {"name": "the shortfall GROWS with A (2H exactly 0, then 3-body, then "
                 "4-body) -- consistent with a Brunnian hierarchy rather than a "
                 "single missing constant",
         "passed": bool(mpf(rows[0]["irreducible_fraction"]) == 0
                        and mpf(rows[1]["irreducible_fraction"])
                        < mpf(rows[2]["irreducible_fraction"]))},
    ]

    ok = all(a["passed"] for a in assertions)
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness = {
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no q0. The shortfall is a difference of AME2020 binding "
            "energies against a pairwise-additive model built from the same "
            "data; no substrate quantity enters. Established by import-cone "
            "trace (cone=1, no q0 import) and by "
            "computations/audits/producer_baked_pin_audit.py, which finds "
            "no q0-valued literal in the source. The witness carries no q0 "
            "field."),
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "Quantifies the pair-locality refutation proved in "
            "QOU.Mass.CrossingModelPairLocality. A pair-local crossing model has "
            "b3 = b4 = 0 forced, so its binding ceiling is C(A,2)*b2. Against "
            "AME2020 that ceiling misses 4He by a factor 2.12 -- 52.8% of the "
            "binding is irreducibly many-body and no pairwise assembly reaches "
            "it, whatever bond functional is applied. "
            "CORRECTED 2026-09-07: this description previously continued 'With a "
            "Brunnian carrier the pair terms vanish and b3 is exactly the triple "
            "channel, so the measured b3 > 0 pins that channel to an attractive "
            "1.4262225 MeV per triple.' That reads CrossingModel.Brunnian "
            "(w2 = 0, pairs carry no mutual energy) as satisfied by L6a4, which "
            "is topologically Brunnian (linking number 0). The corpus proves the "
            "first does not follow from the second: BrunnianBindingChannel."
            "brunnian_binding_survives gives 0 < countChannel m m q for a "
            "crossing pair at q > 1, so w2 != 0. This witness refutes it a "
            "second way from its own data -- b2 != 0 -- by the same "
            "contrapositive the corpus uses for b3. So b3_eq_neg_tripleMutual_"
            "of_brunnian does NOT apply here and b3 does NOT cleanly pin the "
            "triple channel; the discarded pair contamination is nonzero. Both "
            "refutations are sorry-free in QOU.Mass."
            "BrunnianHypothesisNotSatisfied. The shortfall numbers above are "
            "unaffected: they use no Brunnian hypothesis."),
        "q0_pin": "not applicable -- consumes no framework quantity",
        "free_parameters": 0,
        "cumulants_MeV": {"b2": mp.nstr(b2, 14), "b3": mp.nstr(b3, 14),
                          "b4": mp.nstr(b4, 14)},
        "pair_local_ceiling": rows,
        "he4_irreducible_fraction": mp.nstr(he4_frac, 12),
        "he4_pairlocal_deficit_factor": mp.nstr(ratio, 12),
        "he4_body_order_decomposition": decomp,
        "corpus_crosscheck": {
            "source": ("computations/deltalambda/"
                       "deltalambda-kappa-interface-residual-simplex.witness.json"
                       " -> derived_rho_F_crosschecks/full_binding_mayer"),
            "b3_over_b2": mp.nstr(r32, 12), "recorded": "0.64",
            "b4_over_b2": mp.nstr(r42, 12), "recorded_b4": "4.16"},
        "assertions": assertions,
        "scope": (
            "(b) for pair-local crossing models -- the invariant is "
            "b3_eq_zero_of_pairLocal, proved in the Lean, not cited. It excludes "
            "NOTHING about which carrier is right, does not identify the triple "
            "channel, and does not touch the hbar_q^2 saturation question "
            "(qou-brng R3, separately measured numerology-suspect)."),
        "caveats": [
            "The cumulants themselves are NOT new -- b3/b2 = 0.64 and b4/b2 = "
            "4.16 are already in the corpus from the 2026-06-23 audit. What is "
            "new is the bridge making them a REFUTATION of pair-locality in the "
            "crossing model, rather than an observation about a fit.",
            "'Irreducibly many-body' means 'not reachable by summing a function "
            "over pairs'. It does NOT mean the physics is not two-body in "
            "origin: a genuine two-body force can produce non-pairwise BINDING "
            "through the assembly, which is exactly what a Brunnian carrier "
            "does. The claim is about the assembly, not about the force.",
            "b2 is read off the deuteron, whose carrier is a clasp (Hopf / "
            "trefoil, Vol = 0) per the 2026-08-29 owner ruling and is therefore "
            "NOT Brunnian. So the hierarchy is mixed: pairs contribute through "
            "clasps, triples and quads through Brunnian channels. The Lean's "
            "Brunnian theorems apply to the higher orders, not to b2.",
            "Three body orders is three data points. The growth of the "
            "irreducible fraction with A is consistent with a Brunnian "
            "hierarchy; it does not establish one, and A > 4 is untested here.",
        ],
        "lean": ("QOU/Mass/CrossingModelPairLocality.lean "
                 "(8 declarations, sorry-free, lean-direct exit 0)"),
        "related": [
            "probes/aggregator-convexity-divided-difference.witness.json",
            "probes/aggregator-family-exclusion.witness.json",
            "probes/mayer-threebody-sign-threshold.witness.json",
        ],
        "source": "AME2020 total nuclear binding energies",
    }
    out = _HERE / "pair-locality-shortfall.witness.json"
    # NOTE (#6537 x #6519): the `resolve_q0_anchor` override that #6519's sweep
    # placed here has been removed for THIS producer, deliberately.
    #
    # That helper resolves the manifest pin -- muon, proton, or ambiguous -- and
    # defaults to proton for any stem not under `ideal_muon`. It has no way to
    # return `independent`, so on a producer that provably never reads q0 it
    # manufactures a proton claim, and it did so by ASSIGNING OVER the literal
    # below, leaving the `q0AnchorReason` ("Reads no q0 ...") next to a `proton`
    # stamp that contradicts it.
    #
    # `independent` here is measured, not asserted, by three checks:
    #   - import-cone trace: no q_parameter / qou_substrate.constants edge;
    #   - producer_baked_pin_audit.py: no q0-VALUED literal in the source;
    #   - q0_pin_flip_test.py: forcing the muon anchor does not move the
    #     payload (subjects 0/7, on a harness where controls moved 2/2).
    # The sweep's pattern is right for a producer that READS q0; this one
    # does not.
    # P30: add the staleness provenance (scriptHash / commitSha /
    # engine) that a hand-rolled dump cannot get from build().
    # The q0Anchor lines just below own the anchor decision and run
    # after this, so their value stands.
    _WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
