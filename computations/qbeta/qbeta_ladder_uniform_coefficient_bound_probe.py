#!/usr/bin/env python3
"""The Q_beta ladder exclusion, made INDEPENDENT OF THE SIGN of the rungs.

WHAT THIS ADDS TO WHAT THE CORPUS ALREADY HAS.
`QOU.QBeta.LadderFactorBound.ladder_lt_of_rungs` (PR #7355, sorry-free) proves
the ladder cannot reach a requirement F >= 1 -- but ONLY under the hypothesis
that every rung lies in (0, 1], i.e. that every c_k is NEGATIVE. Its own file
says so: "P is a *hypothesis*, not a claim about the rungs, and the numeric
fact that this corpus's rungs satisfy it is measured in the probe rather than
asserted here."

That hypothesis is measured of today's coefficients. It is not proved of the
family, and bean `qou-cds1` is the open task of RE-DERIVING the whole ladder
under convention D. A re-derivation producing a single POSITIVE coefficient
voids `ladder_lt_of_rungs` outright -- the theorem's hypothesis simply fails
and it says nothing. An agent reading only that file could conclude the
exclusion had lifted and go hunting the Q_beta residual in the rungs.

THE REPLACEMENT INPUT IS UNIFORM BOUNDEDNESS, WHICH IS SIGN-BLIND.
`QOU.QBeta.LadderUniformBound` (this PR, sorry-free, 6 declarations, axioms
[propext, Classical.choice, Quot.sound] only) proves the Weierstrass bound

    sum |c_k u^k| <= S < 1   ==>   prod (1 + c_k u^k) * (1 - S) <= 1

with NO sign hypothesis and no division anywhere, then composes it with the
cos <= 1 cap as `ladder_lt_of_sum_bound`. `sum_abs_le_of_scaled` reduces the
hypothesis to a single scalar: if |c_k| <= C and the weights u^k total at most
G, then sum |c_k u^k| <= C*G.

THIS PROBE SUPPLIES THE NUMBERS THE LEAN DELIBERATELY DOES NOT ASSERT: G, the
required factor F on each admissible cell, and the smallest uniform bound
C_min = (1 - 1/F)/G that could possibly reach F.

THE ANSWER, and it is not close. At the proton pin u = 0.0085172345..., the
geometric total is G = u^2/(1-u) = 7.3166e-5, so on the LIVE SCORED cell the
ladder would need C_min ~ 2279 against a corpus whose largest live |c_k| is
|c_3| = 2.0693 -- a factor of ~1102 -- and whose largest EVER-RECORDED
coefficient, the SUPERSEDED c_5 = +12.8676, still leaves a factor of ~177. So
the exclusion survives not only a sign flip but an order-of-magnitude
coefficient blow-up.

QUOTE THE WITNESS, NOT THIS DOCSTRING, for any of those figures: they are
`required_factor_and_C_min_per_cell` and `corpus_coefficients` in
qbeta-ladder-uniform-coefficient-bound.witness.json. The cells are READ from
the sibling probe's witness rather than hardcoded here, so they move when it
does -- which is not hypothetical: the first draft of this probe hardcoded
four cells and the sibling carries FIVE (the bar-odd parity-forced survivor,
F = 2.2136, C_min = 7493, was missing), and its F for the live cell differed
from AGENTS.md's prose at the 8th digit.

THE CONCLUSION IS NOT NEW; THE REASON IS. That the Q_beta L2 residual is a
BASE/ASSEMBLY problem rather than a rung problem is ALREADY the corpus's stated
position, in at least five places -- the merged adjudication
docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md ("the live
open question is not 'what is alpha' but 'what object supplies a factor above 1
at all' -- a question about the base or the assembly, not the phase"), beans
qou-pdix and qou-cds1, qbeta_eigenphase_rationality_quantization_probe.py, and
that probe's witness. Nothing here establishes it for the first time, and it
must not be reported as a new finding.

What every one of those rests on is (i) the cos <= 1 cap and (ii) the MEASURED
SIGN of today's recorded c_k. None argues from magnitude. So this probe adds no
conclusion -- it replaces a fragile premise with a robust one, so that the
corpus's existing conclusion stays standing under the qou-cds1 re-derivation
instead of being voided by one positive rung.

WHAT IS *NOT* CLAIMED.
  * NOT that the re-derived convention-D coefficients ARE bounded by any
    particular C. C is a hypothesis; its corpus value is a measurement, and
    `qou-cds1` has not run.
  * NOT that the missing factor is exhibited. Nothing is selected, nothing is
    re-scored, no base is proposed.
  * NOT anything about the cosh route, which Part 4 of
    qbeta_eigenphase_rationality_quantization_probe re-opened on the ruled base
    (the 2026-08-22 exclusion was computed on the RETIRED z = 1 cell and is
    void). This rules out one lever; it does not survey the others.

PRECISION. Every quantity is mpmath mpf at 60 dps, carried end to end; float()
appears nowhere, not even in display (mp.nstr throughout). NO-FLOAT64 satisfied
by construction.

Beans `qou-cds1` (the re-derivation this is robust to), `qou-pdix` (the phase,
which PART 3 of the sibling probe already showed is not the blocker).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import mp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" /
                       "qou-substrate" / "python"))

from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_proton_extracted, substrate_ladder_quantities  # noqa: E402

mp.dps = 60


def fmt(x):
    return mp.nstr(x, 30)


#: The required factor F = Q_codata / Q_base per cell is READ FROM THE SIBLING
#: WITNESS, never hardcoded: the sibling records each cell as a percentage
#: against CODATA, and F = 1/(1 + pct/100). Two reasons. AGENTS.md's standing
#: instruction on these rows is "quote the witness, not this paragraph" -- the
#: figures have gone stale three times in this arc. And the sibling's own prose
#: and witness DISAGREED at the 8th digit when this probe was written
#: (1.20016236389 in AGENTS.md against 1.20016322219 computed), which is
#: exactly what a literal cannot survive and a read does.
SIBLING = (Path(__file__).resolve().parent /
           "qbeta-eigenphase-rationality-quantization.witness.json")

#: NO hand-kept list of which cells the 2026-09-08 ruling selects. The first
#: draft carried one and its keys had ALREADY drifted from the sibling's
#: (`augmentation_z_eq_q` against the witness's own longer key, and the bar-odd
#: parity-forced survivor missing entirely), so two cells would have been
#: recorded with a null ruling status while the probe "knew" the answer. The
#: sibling's own key names carry the ruling and are reproduced verbatim below
#: rather than re-encoded here.


#: The ladder coefficients the corpus actually records. c_2 is structural; c_3
#: is the proton-pin extraction (recomputed by the canonical qbeta_ck_cache
#: extraction, not typed); c_5 is the CURRENT value, and the superseded
#: c_5 is carried deliberately as the worst case the corpus has ever held.
CORPUS_CK = {
    "c_2 (structural)":            mp.mpf("-1"),
    "c_3 (proton extraction)":     c3_proton_extracted(60),
    "c_5 (current, -(b^2+1/2))":   mp.mpf("-1.2527"),
}
CK_SUPERSEDED = {"c_5 (SUPERSEDED, 3c_3^2+b)": mp.mpf("12.8676")}


def main() -> int:
    failures = []

    def check(name, ok, detail=""):
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        if detail:
            print(f"      {detail}")
        if not ok:
            failures.append(name)

    print("\nPART 1 - the geometric total G, which is a property of u alone\n")

    geo = {}
    for q, label in ((q_at(), "proton"), (q_muon_at(), "muon")):
        u = substrate_ladder_quantities(q)["u"]
        # sum_{k>=2} u^k = u^2/(1-u), exact for |u| < 1
        G = u ** 2 / (1 - u)
        # partial-sum cross-check: the closed form must agree with the sum
        partial = mp.fsum([u ** k for k in range(2, 400)])
        geo[label] = {"q": fmt(q), "u": fmt(u), "G": fmt(G),
                      "G_partial_k_to_400": fmt(partial)}
        print(f"  {label:7s}  u = {mp.nstr(u, 20)}   G = {mp.nstr(G, 12)}")

    u_p = substrate_ladder_quantities(q_at())["u"]
    G_p = u_p ** 2 / (1 - u_p)

    check("1. G = u^2/(1-u) agrees with the truncated geometric sum to 40 "
          "digits at BOTH pins",
          all(abs(mp.mpf(g["G"]) - mp.mpf(g["G_partial_k_to_400"]))
              < mp.mpf(10) ** (-40) for g in geo.values()),
          f"proton G = {mp.nstr(G_p, 14)}; the closed form is what the Lean's "
          f"`sum_abs_le_of_scaled` consumes as the weight total.")

    check("2. u < 1 at both pins, so the Weierstrass hypothesis S < 1 is "
          "reachable at all",
          all(mp.mpf(g["u"]) < 1 for g in geo.values()),
          f"u_proton = {mp.nstr(u_p, 14)}")

    print("\nPART 2 - C_min: the smallest uniform coefficient bound that "
          "could reach each cell\n")

    with open(SIBLING) as fh:
        sib = json.load(fh)
    part3 = sib["data"]["part3_base_not_phase"]
    pcts = part3["cells_pct_vs_codata"]
    # F = Q_codata / Q_base = 1 / (1 + pct/100)
    cells = {k: 1 / (1 + mp.mpf(str(v)) / 100) for k, v in pcts.items()}
    # cross-check the one figure the sibling states outright
    F_live_sib = mp.mpf(str(part3["required_ladder_factor_live_cell"]))
    check("3. F derived from the sibling's percentage table reproduces the "
          "factor it states outright, to 8 digits",
          abs(cells["nuc11_interleaved_tower_E0_LIVE"] - F_live_sib)
          / F_live_sib < mp.mpf("1e-8"),
          f"derived {mp.nstr(cells['nuc11_interleaved_tower_E0_LIVE'], 14)} vs "
          f"stated {mp.nstr(F_live_sib, 14)} -- so the pct table and the "
          f"factor field are the same measurement, not two")

    cmins = {}
    for label, F in cells.items():
        if F <= 1:
            cmins[label] = {"F": fmt(F),
                            "C_min": "n/a - F <= 1, the cap already exceeds it"}
            print(f"  {label:34s}  F = {mp.nstr(F, 12)}   (F <= 1: no rung "
                  f"needed)")
            continue
        S_need = 1 - 1 / F
        C_min = S_need / G_p
        cmins[label] = {"F": fmt(F),
                        "S_required": fmt(S_need), "C_min": fmt(C_min),
                        "C_min_exp_route": fmt(mp.log(F) / G_p)}
        print(f"  {label:34s}  F = {mp.nstr(F, 12)}   C_min = "
              f"{mp.nstr(C_min, 12)}  (exp route "
              f"{mp.nstr(mp.log(F) / G_p, 12)})")

    live = cmins["nuc11_interleaved_tower_E0_LIVE"]
    C_live = mp.mpf(live["C_min"])

    # Keyed on the PROPERTY (F > 1), never on a hand-kept list of cells: the
    # first draft of this probe hardcoded four cells and the sibling witness
    # turned out to carry five, so a curated list would have narrowed the claim
    # silently. Every cell that needs a correction at all is covered.
    needing = {k: v for k, v in cmins.items() if "S_required" in v}
    check("4. EVERY cell that needs a correction at all -- all "
          f"{len(needing)} of them -- needs a uniform coefficient bound above "
          "2000",
          len(needing) > 0 and all(mp.mpf(v["C_min"]) > 2000
                                   for v in needing.values()),
          "live cell C_min = " + mp.nstr(C_live, 12) + "; the cells excluded "
          "are exactly those with F <= 1, where no rung is needed. "
          "min over the cells needing one = " +
          mp.nstr(min(mp.mpf(v["C_min"]) for v in needing.values()), 12))

    print("\nPART 3 - what the corpus actually records\n")

    ck_max = max(abs(v) for v in CORPUS_CK.values())
    ck_max_name = [k for k, v in CORPUS_CK.items() if abs(v) == ck_max][0]
    sup_max = max(abs(v) for v in CK_SUPERSEDED.values())
    print(f"  largest live       |c_k| = {mp.nstr(ck_max, 12)}  ({ck_max_name})")
    print(f"  largest ever held  |c_k| = {mp.nstr(sup_max, 12)}  "
          f"(SUPERSEDED c_5)")

    ratio_live = C_live / ck_max
    ratio_sup = C_live / sup_max
    print(f"  C_min / largest live       = {mp.nstr(ratio_live, 10)}")
    print(f"  C_min / largest ever held  = {mp.nstr(ratio_sup, 10)}")

    check("5. the live ladder is short by a factor above 1000",
          ratio_live > 1000,
          f"{mp.nstr(ratio_live, 10)}x -- the coefficient would have to be "
          f"three orders of magnitude larger than anything the corpus holds")

    check("6. the exclusion survives the worst coefficient the corpus has "
          "EVER held, superseded c_5 = +12.8676 included",
          ratio_sup > 100,
          f"{mp.nstr(ratio_sup, 10)}x -- so this is robust to an "
          f"order-of-magnitude blow-up, not only to a sign flip")

    print("\nPART 4 - the Lean's bound, evaluated at generous C\n")

    bounds = {}
    for C in ("1", "3", "12.8676", "100"):
        Cm = mp.mpf(C)
        S = Cm * G_p
        # the Lean gives prod * (1 - S) <= 1, i.e. prod <= 1/(1 - S)
        cap = 1 / (1 - S)
        bounds[C] = {"S": fmt(S), "ladder_cap": fmt(cap)}
        print(f"  C = {C:>8s}   S = {mp.nstr(S, 10)}   ladder cap = "
              f"{mp.nstr(cap, 16)}")

    cap100 = mp.mpf(bounds["100"]["ladder_cap"])
    F_live = cells["nuc11_interleaved_tower_E0_LIVE"]

    check("7. even at C = 100 -- 48x the corpus's largest live coefficient -- "
          "the ladder cap is still far below the live cell's requirement",
          cap100 < F_live,
          f"cap {mp.nstr(cap100, 14)} vs required {mp.nstr(F_live, 12)}; "
          f"shortfall {mp.nstr((F_live - 1) / (cap100 - 1), 8)}x in the "
          f"correction itself")

    check("8. the Lean hypothesis S < 1 holds at every C tested, so "
          "`ladder_lt_of_sum_bound` applies rather than being vacuous",
          all(mp.mpf(v["S"]) < 1 for v in bounds.values()),
          "largest S tested = " + mp.nstr(mp.mpf(bounds["100"]["S"]), 10))

    exp_live = mp.log(F_live) / G_p
    check("9. the two independent Lean routes BRACKET the requirement: the "
          "Weierstrass C_min is the smaller, so it is the one quoted",
          C_live < exp_live,
          f"Weierstrass {mp.nstr(C_live, 12)} < exp route "
          f"{mp.nstr(exp_live, 12)} -- 1/(1-S) >= exp(S) on [0,1), so the "
          f"weaker product bound yields the more conservative exclusion. "
          f"`ladder_lt_of_sum_bound` and `ladder_lt_of_sum_bound_exp` are "
          f"independent proofs of the same statement.")

    print("\nCONSEQUENCE\n")
    print("""  That the Q_beta L2 residual is a BASE/ASSEMBLY problem rather than a
  rung problem is ALREADY the corpus's position -- merged audit
  2026-09-13-formb-probe-adjudication-and-cds1-state.md, beans qou-pdix and
  qou-cds1, the sibling probe and its witness. NOTHING HERE ESTABLISHES IT.

  What is new is that the statement no longer depends on the SIGNS of the
  coefficients, which is what made the existing exclusion fragile to the open
  qou-cds1 re-derivation: one positive rung voids
  LadderFactorBound.ladder_lt_of_rungs outright. A re-derived convention-D
  ladder now overturns the conclusion only by producing a coefficient above
  ~2279 in absolute value, three orders of magnitude past anything the corpus
  has held -- a single scalar a future agent can check.

  NOT claimed: that the re-derived coefficients are bounded (C is a
  hypothesis), that the missing factor is exhibited, or anything about the
  cosh route, which stays open on the ruled base. Nothing re-scored.""")

    wb = WitnessBuilder("qbeta-ladder-uniform-coefficient-bound")
    wb.set_description(
        "The Q_beta ladder cannot reach the required correction factor on any "
        "ruled base, for rungs of EITHER SIGN -- the existing exclusion "
        "(LadderFactorBound.ladder_lt_of_rungs) assumes every c_k < 0 and is "
        "voided by a single positive coefficient, which the open qou-cds1 "
        "re-derivation could produce. The sign-blind replacement input is "
        "uniform boundedness: the smallest |c_k| bound that could reach the "
        "LIVE SCORED cell is C_min = 2279.45, against a corpus whose largest "
        "live coefficient is 2.0693 (factor 1101.5) and whose largest "
        "ever-recorded one, the superseded c_5 = +12.8676, still leaves a "
        "factor of 177.1. Lean twin: QOU.QBeta.LadderUniformBound, sorry-free."
    )
    wb.add_data("geometric_totals", geo)
    wb.add_data("required_factor_and_C_min_per_cell", cmins)
    wb.add_data("corpus_coefficients", {
        "live": {k: fmt(v) for k, v in CORPUS_CK.items()},
        "superseded_worst_case": {k: fmt(v) for k, v in CK_SUPERSEDED.items()},
        "largest_live_abs": fmt(ck_max),
        "C_min_over_largest_live": fmt(ratio_live),
        "C_min_over_largest_ever_held": fmt(ratio_sup),
    })
    wb.add_data("ladder_cap_at_generous_C", bounds)
    wb.add_data("lean_twin", {
        "module": "QOU.QBeta.LadderUniformBound",
        "theorems": ["sum_abs_nonneg", "prod_one_add_pos",
                     "prod_one_add_mul_le_one", "sum_abs_le_of_scaled",
                     "ladder_lt_of_sum_bound", "sum_bound_of_ladder_ge"],
        "status": "sorry-free; lean-direct exit 0 with -DautoImplicit=false "
                  "-s 65536; axioms [propext, Classical.choice, Quot.sound]",
        "what_it_supersedes": "NOTHING -- LadderFactorBound stays valid and is "
                              "TIGHTER where its sign hypothesis holds. This "
                              "removes the hypothesis, it does not replace the "
                              "file.",
    })
    wb.add_data("scope", {
        "proved": "the IMPLICATION: bounded coefficients => ladder below the "
                  "requirement, either sign",
        "measured": "C_min, G, and the corpus's coefficient magnitudes",
        "NOT_established": [
            "that a re-derived convention-D ladder's coefficients are bounded "
            "by any particular C -- qou-cds1 has not run",
            "any candidate for the missing factor",
            "anything about the cosh route, re-opened on the ruled base",
        ],
    })
    for i, nm in enumerate([
        "G = u^2/(1-u) matches the truncated geometric sum at both pins",
        "u < 1 at both pins so the Weierstrass hypothesis is reachable",
        "F derived from the sibling pct table matches its stated factor",
        "every ruled cell needs a uniform coefficient bound above 2000",
        "the live ladder is short by a factor above 1000",
        "the exclusion survives the worst coefficient ever held",
        "even C = 100 leaves the cap far below the live requirement",
        "the Lean hypothesis S < 1 holds, so the theorem is not vacuous",
        "the two independent Lean routes bracket the requirement",
    ], 1):
        wb.add_assertion(f"{i}. {nm}", "FAIL" if nm in failures else "PASS",
                         "PASS")
    out = wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": (
        "u and the geometric total G are evaluated at BOTH the proton pin (q_at) and the live CODATA-2022 muon pin (q_muon_at) and both are recorded; the bound's headline is at proton, the muon arm checks the hypothesis holds at both pins")})
    print(f"\nWitness: {out}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
