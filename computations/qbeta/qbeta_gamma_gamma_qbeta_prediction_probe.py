"""What the gamma-gamma ruling actually PREDICTS for Q_beta -- and why the
0.11 % near-hit inside that family is worth nothing.

# Ref: AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3" -- selection against the
#      target, and "accuracy is not evidence of correctness"
# Ref: AGENTS.md §"OWNER RULING 2026-09-08" (qou-99qc) -- eps is the Markov
#      trace at z_D = q^3/(q^2+1); (qou-ales) -- canonical braid words are
#      selected by gamma-gamma construction + the confinement SDP, never census
# Ref: computations/qbeta/qbeta_gamma_gamma_sdp_feasibility_probe.py (PR #7295)
#      -- the 5 PSD-feasible words of 8190 at n = 4
# Ref: computations/per_observable_100x_status.py::_q_beta_row -- the scoring
#      path this probe mirrors exactly

WHY THIS EXISTS.  AGENTS.md: *"If a derivation is specified but not
implemented, implement the specification, and report what it gives even when
that is worse.  A documented honest miss is a result."*  The 2026-09-08 ruling
specifies both halves -- gamma-gamma selection AND the confinement SDP -- and
nobody had scored the resulting admissible set against Q_beta.  This does.

🛑 SCOPING CORRECTION, 2026-09-13.  This probe scores each feasible word
**alone** as a Q_beta prediction.  That is NOT the scoring path: the observable
is `|eps(Delta)| * E_0` with `Delta` the **neutron element MINUS the proton
element** (`qbeta_option_e_required_level_probe.py::delta_of`).  The numbers
below are what you get if a single word is the functional's argument, and they
are correct as such -- they are not what the admissible set predicts for Q_beta.
For that, all 15 PAIRS run -100 % to +79.4 %:
`qbeta_qbeta_scores_a_difference_probe.py` (6/6).

THE ANSWER IS THAT IT MISSES BY 5.6x TO 7.2x, and the interesting part is that
the five admissible words agree with each other far more closely than any of
them agrees with the measurement: the prediction spread across the whole
admissible set is 1.29x, against a miss of 5.6-7.2x.  So the miss is a property
of the FAMILY, not of which word is picked out of it.  Picking differently
inside the admissible set cannot fix Q_beta.

🛑 AND THERE IS A TRAP IN THIS FAMILY THAT THIS PROBE EXISTS TO DISARM.  Drop
the SDP half and scan the whole gamma-gamma family, and you find a word landing
on Q_beta to **0.11 %** -- eleven `v_0` vertices and one `v_1`.  That number is
worth NOTHING, and the probe measures why rather than asserting it:

  * the family has **529 distinct** trace values over its 8190 words;
  * **50** of them lie within +-10 % of the target;
  * their median spacing gives an expected best-of-family miss, by chance
    alone, of **0.047 %**;
  * the observed best is **0.111 %** -- i.e. *worse than chance*.

Same control, and the same verdict, as the difference-grid check in the H_3
admissible-family probe (0.455 % observed against 0.322 % expected).  A grid
this dense near the target explains a 0.11 % landing with no physics in it at
all.  And the twelve words that tie at that value are one order-blind orbit
(the trace cannot see which vertex sits where), none of them PSD-feasible.

WHAT IS SCOPE-(a) HERE, AND WHAT IS NOT.  The miss is scope-(a): it measures
one functional on one family at one strand count.  It does not exclude a
gamma-gamma word at higher `n`, nor a different `E_0`, nor a tower correction.
What it does establish, and this is the reusable part, is that inside n = 4 the
choice of admissible word is not the free parameter anyone is looking for.
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys

import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python", "tools/pyhecke/python"):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
import qbeta_e0  # noqa: E402
from codata_constants import Q_BETA_MEV  # noqa: E402

_OC = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_ocneanu_trace_general_n_probe.py")
_spec = importlib.util.spec_from_file_location("_oc", _OC)
_oc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_oc)

set_compute_dps(60)
mp.mp.dps = 40

H0 = _oc.H0
ZD = _oc.ZD
HR = sp.Rational(str(H0))
ZR = sp.Rational(str(ZD))

#: the PSD-feasible words at n = 4, MEASURED by the sibling probe (PR #7295),
#: not re-derived here.  5 of 8190.
FEASIBLE = [
    ((0, 1, 0, 1), "(v0 v1)^2"),
    ((0, 1, 0, 1, 0, 1, 0, 1), "(v0 v1)^4"),
    ((0, 0, 1, 1, 0, 1, 1, 0, 0, 1), "sporadic A"),
    ((0, 1, 1, 0, 0, 1, 0, 0, 1, 1), "sporadic B"),
    ((0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1), "(v0 v1)^6"),
]

#: `tr^{z_D}` of the currently-scored census element, read from the census
#: witness the dashboard itself reads -- the calibration anchor.
CENSUS_WITNESS = os.path.join(ROOT, "computations", "qbeta",
                              "qbeta-option-e-required-level.witness.json")
SCORED_ELEMENT = "nuc11_interleaved"

MAX_VERTICES = 12

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def gg_vec(combo, n: int = 4):
    """Normal form of the gamma-gamma word `prod_i v_i`, `h` specialised."""
    lets: list = []
    for i in combo:
        lets += [(i, sp.Integer(0)), (i + 1, -HR)]
    return _oc.word_to_vec(lets, n, {}, HR)


def trace(combo, n: int = 4):
    """`tr^{z_D}` of the word -- the ruled functional `eps`."""
    return mp.mpf(str(sp.N(_oc.tr(gg_vec(combo, n), n, HR, ZR), 35)))


def main() -> int:
    w = WitnessBuilder("qbeta-gamma-gamma-qbeta-prediction")
    w.set_description(
        "Scores the gamma-gamma + confinement-SDP admissible set at n = 4 "
        "against Q_beta through the dashboard's own path, eps = tr^{z_D} times "
        "the canonical tower-summed E_0. All five admissible words overshoot, "
        "+458.1 % to +619.8 %, and they agree with EACH OTHER 1.29x while "
        "missing the measurement 5.6-7.2x -- so the miss belongs to the family, "
        "not to the choice inside it. The probe then disarms the trap: drop the "
        "SDP half and the unconstrained family contains a word at 0.11 %, which "
        "is WORSE THAN CHANCE for a family whose 529 distinct trace values put "
        "50 within +-10 % of the target (expected best 0.047 %). Scope-(a): one "
        "functional, one family, n = 4."
    )

    E0 = qbeta_e0.canonical()
    qb = mp.mpf(str(Q_BETA_MEV))
    target = qb / E0

    print(f"  E_0 (tower-summed, canonical) = {mp.nstr(E0, 20)} MeV")
    print(f"  Q_beta (CODATA)               = {mp.nstr(qb, 12)} MeV")
    print(f"  => target |tr^z_D|            = {mp.nstr(target, 15)}")
    print()

    # ---- 1. calibration: reproduce the dashboard's own scored cell ----------
    import json
    cens = json.loads(open(CENSUS_WITNESS).read())
    tr_scored = mp.mpf(cens["data"]["per_candidate"][SCORED_ELEMENT]["tr_conv_D"])
    pred_scored = abs(tr_scored) * E0
    err_scored = (pred_scored - qb) / qb * 100
    # AGENTS.md records the scored cell as -16.678 % on the canonical E_0.
    check("calibrates_against_the_dashboards_own_scored_cell",
          abs(err_scored - mp.mpf("-16.678")) < mp.mpf("0.01"),
          f"scoring the census element {SCORED_ELEMENT} through this probe's "
          f"path gives {mp.nstr(pred_scored, 12)} MeV, {mp.nstr(err_scored, 8)} "
          f"%, against the -16.678 % AGENTS.md records for the dashboard row. "
          f"The path is therefore the dashboard's, not a re-invention", w)

    # ---- 2. score the admissible set, ALL of it ----------------------------
    rows = []
    for combo, label in FEASIBLE:
        t = abs(trace(combo))
        p = t * E0
        rows.append((label, len(combo), t, p, (p - qb) / qb * 100))
    rows.sort(key=lambda r: r[1])          # by VERTEX COUNT, the derived order

    print("  the gamma-gamma + SDP admissible set, ordered by vertex count")
    print("  (NOT by residual -- ordering candidates by residual is the "
          "selection AGENTS.md forbids):")
    print(f"    {'word':12s} {'k':>3s} {'|tr^z_D|':>16s} {'Q_beta MeV':>16s} "
          f"{'err %':>12s}")
    for label, k, t, p, e in rows:
        print(f"    {label:12s} {k:3d} {mp.nstr(t, 12):>16s} "
              f"{mp.nstr(p, 12):>16s} {mp.nstr(e, 7):>12s}")
    print()

    errs = [r[4] for r in rows]
    check("every_admissible_word_overshoots_and_none_is_close",
          all(e > 400 for e in errs),
          f"all {len(rows)} PSD-feasible gamma-gamma words at n = 4 overshoot "
          f"Q_beta, from {mp.nstr(min(errs), 7)} % to {mp.nstr(max(errs), 7)} "
          f"%. This is what the ruling's two halves give when both are applied; "
          f"it is reported because a documented honest miss is a result", w)

    # ---- 3. the spread is small against the miss ---------------------------
    preds = [r[3] for r in rows]
    spread = max(preds) / min(preds)
    miss_lo = min(preds) / qb
    miss_hi = max(preds) / qb
    check("the_miss_belongs_to_the_family_not_to_the_choice",
          spread < miss_lo,
          f"the admissible words agree with each other to a factor "
          f"{mp.nstr(spread, 6)}, while missing the measurement by "
          f"{mp.nstr(miss_lo, 6)}x to {mp.nstr(miss_hi, 6)}x. The internal "
          f"spread is smaller than the smallest miss, so no re-selection "
          f"INSIDE the admissible set can reach Q_beta -- the choice of word "
          f"is not the free parameter", w)

    # ---- 4. every feasible trace is above the empty word's -----------------
    #  tr(empty) = 1 exactly (the Markov normalisation); the target is 0.185.
    check("the_target_lies_BELOW_every_PSD_feasible_trace",
          target < min(r[2] for r in rows) and target < 1,
          f"target |tr^z_D| = {mp.nstr(target, 12)} is below 1 = tr(empty "
          f"word) and below the smallest feasible trace "
          f"{mp.nstr(min(r[2] for r in rows), 12)}. PSD feasibility pushes the "
          f"trace UP, and the target sits under the whole feasible set -- so "
          f"the SDP half is what excludes the measured value, not the "
          f"gamma-gamma half", w)

    # ---- 5. the unconstrained family DOES reach the target ----------------
    print(f"  scanning the unconstrained gamma-gamma family, k = 1..{MAX_VERTICES} "
          f"(this takes ~2 min) ...")
    allv: list[tuple[mp.mpf, tuple]] = []
    for k in range(1, MAX_VERTICES + 1):
        for c in itertools.product((0, 1), repeat=k):
            allv.append((abs(trace(c)), c))
    n_words = len(allv)
    lo = min(v for v, _ in allv)
    hi = max(v for v, _ in allv)
    check("the_unconstrained_family_straddles_the_target",
          lo < target < hi,
          f"over {n_words} gamma-gamma words at n = 4, |tr^z_D| spans "
          f"[{mp.nstr(lo, 8)}, {mp.nstr(hi, 8)}] and the target "
          f"{mp.nstr(target, 10)} is strictly inside. So the gamma-gamma "
          f"construction ALONE can produce the measured value -- which is the "
          f"setup for the control below, not a result", w)

    # ---- 6. the chance control, which is the point -------------------------
    uniq = sorted({mp.nstr(v, 20) for v, _ in allv})
    U = sorted(mp.mpf(x) for x in uniq)
    win = [v for v in U if abs(v - target) <= mp.mpf("0.10") * target]
    gaps = sorted(win[i + 1] - win[i] for i in range(len(win) - 1))
    median_gap = gaps[len(gaps) // 2]
    expected = median_gap / 4 / target * 100
    # Take the best over the FULL-precision values, not over `U` -- `U` is
    # round-then-reparse, so `==` against it finds nothing.  The tie test then
    # has to be a tolerance, not equality, for the same reason.
    best = min(abs(v - target) for v, _ in allv)
    observed = best / target * 100
    tied = [c for v, c in allv if abs(abs(v - target) - best) < mp.mpf("1e-25")]

    print()
    print(f"    words                                 {n_words}")
    print(f"    DISTINCT trace values                 {len(U)}")
    print(f"    distinct values within +-10 % of target  {len(win)}")
    print(f"    median spacing there                  {mp.nstr(median_gap, 8)}")
    print(f"    => expected best-by-chance            {mp.nstr(expected, 4)} %")
    print(f"    observed best                         {mp.nstr(observed, 6)} %")
    print()

    check("the_best_gamma_gamma_match_is_WORSE_than_chance",
          observed > expected,
          f"the family has {len(U)} distinct trace values over {n_words} words, "
          f"{len(win)} of them within +-10 % of the target; their median "
          f"spacing {mp.nstr(median_gap, 6)} gives an expected best-of-family "
          f"miss of {mp.nstr(expected, 4)} % by chance alone. The observed best "
          f"is {mp.nstr(observed, 6)} % -- WORSE than chance. A 0.11 % landing "
          f"in a grid this dense is not evidence of anything, and quoting it "
          f"would be exactly the selection-against-the-target AGENTS.md bans", w)

    feasible_set = {c for c, _ in FEASIBLE}
    check("the_near_hit_is_an_order_blind_orbit_and_none_of_it_is_feasible",
          len(tied) > 1 and not (set(tied) & feasible_set),
          f"{len(tied)} words tie at the best value, all with the same multiset "
          f"of vertex indices -- the trace is order-blind, so they are one "
          f"orbit, not {len(tied)} independent near-hits. None of them is "
          f"PSD-feasible, so the SDP half of the ruling excludes the whole "
          f"orbit anyway. Representative: k = {len(tied[0])}, {tied[0]}", w)

    w.add_data("target", {
        "E0_MeV": mp.nstr(E0, 30),
        "E0_form": "tower_summed (canonical, qbeta_e0.canonical)",
        "Q_beta_CODATA_MeV": mp.nstr(qb, 12),
        "target_abs_tr_zD": mp.nstr(target, 25),
        "markov_parameter": "z_D = q^3/(q^2+1)",
    })
    w.add_data("calibration", {
        "scored_element": SCORED_ELEMENT,
        "tr_conv_D": mp.nstr(tr_scored, 25),
        "Q_beta_MeV": mp.nstr(pred_scored, 15),
        "err_pct": mp.nstr(err_scored, 8),
        "agents_md_records": "-16.678",
    })
    w.add_data("admissible_set_scored", [
        {"label": lab, "vertices": k, "abs_tr_zD": mp.nstr(t, 25),
         "Q_beta_MeV": mp.nstr(p, 15), "err_pct": mp.nstr(e, 8)}
        for lab, k, t, p, e in rows
    ])
    w.add_data("family_spread_vs_miss", {
        "internal_spread_factor": mp.nstr(spread, 10),
        "miss_factor_min": mp.nstr(miss_lo, 10),
        "miss_factor_max": mp.nstr(miss_hi, 10),
        "reading": "the admissible words agree with each other far more "
                   "closely than any agrees with the measurement, so the "
                   "choice of word is not the free parameter",
    })
    w.add_data("chance_control", {
        "words": n_words,
        "distinct_values": len(U),
        "distinct_within_10pct": len(win),
        "median_spacing": mp.nstr(median_gap, 20),
        "expected_best_pct_by_chance": mp.nstr(expected, 8),
        "observed_best_pct": mp.nstr(observed, 8),
        "tied_words": len(tied),
        "verdict": "observed is WORSE than expected-by-chance; the near-hit "
                   "carries no information",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited",
        "what_it_does_not_show": "nothing about n > 4, about a different E_0, "
                                 "or about a tower correction; it measures one "
                                 "functional on one family at one strand count",
        "what_it_does_show": "inside n = 4 the choice of admissible word "
                             "cannot reach Q_beta, and the unconstrained "
                             "family's best match is worse than chance",
    })
    w.add_data("not_implemented", {
        "demand_constraint": "knot-operator-selection-proof's <Phi, dem(K)>_F "
                             ">= ||dem(K)||_F is NOT imposed here; building "
                             "dem(K) requires choosing which K the nucleon is, "
                             "which is the open question",
    })

    ok = not FAILED
    w.save()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
