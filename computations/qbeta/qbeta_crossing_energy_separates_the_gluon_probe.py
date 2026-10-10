#!/usr/bin/env python3
"""qou-99qc: crossing ENERGY and crossing COUNT disagree on the gluon dressing —
and part 7's degeneracy verdict does NOT transfer off gamma-gamma words.

# Ref: computations/qbeta/qbeta_gamma_gamma_crossing_energy_probe.py  (part 7: E_cross = k*h on gg words, degenerate)
# Ref: computations/qbeta/qbeta_cost_minimal_budget_under_reading3_probe.py  (the cost-minimal budget)
# Ref: folio/quantum-observable-universe/lean/QOU/Mass/GammaGammaFrobeniusSelection.lean
# Ref: folio/quantum-observable-universe/lean/QOU/MobiusEnergy.lean
# Ref: .beans/qou-99qc--...md   (part 7 is on main at 645dece2790)

WHY THIS EXISTS. The sibling probe selects the gluon dressing by MINIMAL
CROSSING COUNT, because that is the cost `FrobeniusSelected` is instantiated
with in the Lean. The owner's objection (2026-09-14): crossing count is a
combinatorial proxy, not an energy — a stabiliser that ADDS a crossing may
LOWER the energy, so the two need not agree. This probe measures whether they
in fact disagree on this family. They do.

THE FUNCTIONAL, calibrated not assumed. `def:crossing-energy` assigns `+q` to a
positive crossing and `-1/q` to a negative one. Part 7 pinned the orientation
against `pair-creation-energy.md` by data: the electron (left trefoil, three
POSITIVE crossings) is `3q = 3.3299357483` against its `~3.330`, and the
positron (mirror) `-3/q = -2.7027548519` against `~-2.703`. Both are reproduced
here as checks 1-2 before anything is read off the functional.

RESULT 1 -- PART 7's VERDICT IS CORRECT AND IS SPECIFIC TO gg WORDS. A
gamma-gamma vertex `sigma_i sigma_{i+1}^{-1}` is one positive and one negative
crossing, so it contributes `q + (-1/q) = h` and a k-vertex word has
`E_cross = k*h` EXACTLY -- reproduced here. On that family energy is therefore
PROPORTIONAL to count, so swapping one cost for the other changes nothing, and
`E_cross(empty) = 0` sits below every non-empty gg word. That is the degeneracy
that retired the functional.

RESULT 2 -- THE GLUON IS NOT A gg WORD, AND THERE THEY DISAGREE. gg words are
sign-BALANCED by construction; the gluon dressing is explicitly outside the gg
construction and its letters are unbalanced. Among the reading-3-feasible
gluons, `sigma_1` and `sigma_1^-1` TIE at crossing count 1, while by energy
`sigma_1^-1 = -0.9009182840` STRICTLY BEATS `sigma_1 = +1.1099785828`. So the
selected gluon changes with the cost, which is exactly the owner's point made
concrete.

RESULT 3 -- AND THE DEGENERACY DISSOLVES HERE. `E_cross(empty) = 0`, but
`sigma_1^-1` is NEGATIVE. The empty word is NOT the energy minimum once
negative crossings are available, and the gluon family has them while gg words
never do. So the objection that killed this functional in part 7 does not
transfer, and crossing energy is USABLE on the gluon where it was not on the
core.

RESULT 4 -- IT IS STILL ORDER-BLIND, SO IT DOES NOT FINISH THE JOB. `E_cross`
is a sum over letters, so it cannot separate `sigma_1 sigma_0` from
`sigma_0 sigma_1`, and all three two-crossing feasible gluons tie EXACTLY at
`2q`. It breaks the one-crossing tie and leaves the two-crossing tie standing.

WHAT THIS POINTS AT, and it is NOT built. An embedding energy (O'Hara / Moebius
via the Bring embedding) is not a letter-sum: it depends on the geometry of the
embedded curve, so it is order-SENSITIVE and can rank a longer word below a
shorter one. The corpus has the integrator (calibrated against the proved
`E(Hopf) = 2*pi^2`, Agol-Marques-Neves) and a categorical `E_cat` in
`QOU.MobiusEnergy`, but NO map from a braid word to a curve in or on the Bring
surface -- searched for in `computations/` and `tools/`, found none, which is
an absence on those surfaces rather than a proof of absence. Moebius energy is
a property of an EMBEDDING and not a knot invariant (the invariant is the
infimum over the isotopy class), so such a bridge needs either the minimiser or
a canonical embedding. Recorded as an open target, not attempted here.

WHAT IS NOT CLAIMED. That `sigma_1^-1` should be adopted -- that would be
swapping one proxy for another, and this probe's own RESULT 4 says the energy
does not separate the remaining candidates. That crossing energy is the right
cost. No selection was made by proximity to any measured value; the Q_beta
column below is reported as a CONSEQUENCE of each candidate and is not an
input to any ordering here.

ARITHMETIC. mpmath mpf at 60 dps, proton pin, convention D. No float64.

Run: python3 -u computations/qbeta/qbeta_crossing_energy_separates_the_gluon_probe.py \
       2>&1 | tee /tmp/qbeta_crossing_energy_gluon.log
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import Q_BETA_MEV  # noqa: E402

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402
import qbeta_e0  # noqa: E402

mp = _order.mp
set_compute_dps(60)
mp.mp.dps = 60

Q0, H0, ZD = _order.Q0, _order.H0, _order.ZD
Y3 = (Q0 ** 4 + 1) / (Q0 ** 2 + 1) ** 2
Y21 = Q0 ** 2 / (Q0 ** 2 + 1) ** 2

Z, HALF, NEG1 = mp.mpf(0), mp.mpf(-1) / 2, mp.mpf(-1)
CORE = [(0, Z), (1, NEG1)] * 3
QSHIFT = {"p": [Z, HALF, HALF], "n": [HALF, HALF, NEG1]}
GENS = (0, 0, 1)

#: `pair-creation-energy.md`'s recorded values, to two decimals as published.
ELECTRON_PUB = mp.mpf("3.330")
POSITRON_PUB = mp.mpf("-2.703")

TOL = mp.mpf("1e-25")
FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def tr(letters):
    return _order.tr_at(_order.word_nf(letters), ZD)


def chi3(letters):
    v = mp.mpf(1)
    for _, d in letters:
        v *= (Q0 + d * H0)
    return v


def chi21(letters):
    return (tr(letters) - Y3 * chi3(letters)) / Y21


def reading3(letters) -> bool:
    return chi3(letters) >= 0 and chi21(letters) >= 0


def ecross(letters) -> mp.mpf:
    """`def:crossing-energy`: a positive crossing contributes `+q`, a negative
    one `-1/q`.  Defined only on PURE crossings -- the bar-fixed letter
    (`d = -h/2`) is not a crossing and raises rather than being fudged."""
    e = mp.mpf(0)
    for _, d in letters:
        if d == Z:
            e += Q0
        elif d == NEG1:
            e += -1 / Q0
        else:
            raise ValueError("E_cross undefined on the bar-fixed letter")
    return e


def base(nuc: str):
    return CORE + [(g, s) for g, s in zip(GENS, QSHIFT[nuc])]


#: the gluon candidates.  All pure crossings, so `ecross` is defined on each.
CANDIDATES = {
    "(empty)": [],
    "sigma_1": [(1, Z)],
    "sigma_1^-1": [(1, NEG1)],
    "sigma_0": [(0, Z)],
    "sigma_0^-1": [(0, NEG1)],
    "sigma_0 sigma_0 (LIVE)": [(0, Z), (0, Z)],
    "sigma_1 sigma_0": [(1, Z), (0, Z)],
    "sigma_0 sigma_1": [(0, Z), (1, Z)],
    "sigma_1 sigma_1": [(1, Z), (1, Z)],
}


def main() -> int:
    w = WitnessBuilder("qbeta-crossing-energy-separates-the-gluon")
    w.set_description(
        "Crossing COUNT is the cost FrobeniusSelected is instantiated with; the "
        "owner objected that it is a combinatorial proxy and a stabiliser that "
        "adds a crossing may lower the energy. Measured: on gamma-gamma words "
        "part 7's verdict holds exactly (E_cross = k*h, so energy is "
        "proportional to count and the empty word is the minimum), but the "
        "gluon dressing is NOT a gg word and there the two costs DISAGREE -- "
        "sigma_1 and sigma_1^-1 tie at count 1 while sigma_1^-1 = -0.9009 "
        "strictly beats sigma_1 = +1.1100 by energy. The degeneracy also "
        "dissolves: E_cross(empty) = 0 is NOT minimal once negative crossings "
        "are available, which gg words never have. But E_cross is a letter-sum "
        "and stays order-blind -- the three two-crossing feasible gluons tie "
        "exactly -- so it breaks one tie and not the other. Points at an "
        "embedding energy (O'Hara/Moebius via Bring), for which the corpus has "
        "the integrator but NO braid-word-to-curve map."
    )

    print("qou-99qc — crossing energy vs crossing count on the gluon dressing")
    print(f"  q0 = {mp.nstr(Q0, 20)}   h = {mp.nstr(H0, 20)}")
    print()

    # ---- 1. calibrate the functional against published values ------------
    print("== 1. calibration — orientation pinned by data ==")
    e_electron = ecross([(0, Z)] * 3)
    e_positron = ecross([(0, NEG1)] * 3)
    print(f"    electron (3 positive crossings) : {mp.nstr(e_electron, 12)}"
          f"   published ~{mp.nstr(ELECTRON_PUB, 6)}")
    print(f"    positron (mirror)               : {mp.nstr(e_positron, 12)}"
          f"   published ~{mp.nstr(POSITRON_PUB, 6)}")
    check("crossing_energy_orientation_matches_the_published_pair",
          abs(e_electron - ELECTRON_PUB) < mp.mpf("5e-4")
          and abs(e_positron - POSITRON_PUB) < mp.mpf("5e-4"),
          f"electron {mp.nstr(e_electron, 12)} vs ~3.330, positron "
          f"{mp.nstr(e_positron, 12)} vs ~-2.703 (pair-creation-energy.md). A "
          f"reversed sign convention would swap these, so the orientation is "
          f"pinned before any verdict is read off the functional", w)

    vertex = ecross([(0, Z), (1, NEG1)])
    check("a_gamma_gamma_vertex_contributes_exactly_h",
          abs(vertex - H0) < TOL,
          f"sigma_i sigma_{{i+1}}^-1 = q + (-1/q) = h = {mp.nstr(H0, 20)}, "
          f"reproducing part 7's closed form independently", w)

    gg5 = ecross([(0, Z), (1, NEG1)] * 5)
    check("E_cross_on_gg_words_is_k_times_h_so_energy_IS_count_there",
          abs(gg5 - 5 * H0) < TOL,
          f"a 5-vertex gg word has E_cross = {mp.nstr(gg5, 20)} = 5h exactly. On "
          f"gg words energy is PROPORTIONAL to count, so part 7 is right that "
          f"swapping the cost changes nothing there -- and E_cross(empty) = 0 "
          f"is below every non-empty gg word, which is its degeneracy", w)
    print()

    # ---- 2. the gluon family ---------------------------------------------
    print("== 2. the gluon candidates — count vs energy ==")
    E0 = qbeta_e0.canonical()
    qb = mp.mpf(str(Q_BETA_MEV))
    rows = {}
    print("   gluon G                    |G|  reading-3  E_cross(G)        "
          "Q_beta MeV     vs CODATA")
    for name, g in CANDIDATES.items():
        wp, wn = base("p") + g, base("n") + g
        feas = reading3(wp) and reading3(wn)
        e = ecross(g)
        q = abs(tr(wn) - tr(wp)) * E0
        rows[name] = {"k": len(g), "feasible": feas, "E_cross": e, "Q_beta": q}
        print(f"   {name:<26s} {len(g):<4d} {'Y' if feas else 'n':<10s} "
              f"{mp.nstr(e, 14):<17s} {mp.nstr(q, 10):<14s} "
              f"{float((q - qb) / qb * 100):+.3f} %")

    feasible = {n: r for n, r in rows.items() if r["feasible"]}
    by_count = sorted(feasible, key=lambda n: feasible[n]["k"])
    by_energy = sorted(feasible, key=lambda n: feasible[n]["E_cross"])
    min_k = min(feasible[n]["k"] for n in feasible)
    count_ties = [n for n in feasible if feasible[n]["k"] == min_k]

    print()
    print(f"    feasible gluons          : {sorted(feasible)}")
    print(f"    min by crossing COUNT    : {count_ties}  (k = {min_k})")
    print(f"    min by crossing ENERGY   : {by_energy[0]}  "
          f"(E = {mp.nstr(feasible[by_energy[0]]['E_cross'], 12)})")

    check("count_and_energy_select_DIFFERENT_gluons",
          by_energy[0] not in count_ties or len(count_ties) > 1,
          f"crossing count TIES {count_ties} at k = {min_k}; crossing energy "
          f"strictly prefers {by_energy[0]} at "
          f"{mp.nstr(feasible[by_energy[0]]['E_cross'], 12)}. The two costs do "
          f"not agree on this family, so the choice of cost is a real decision "
          f"rather than a formality -- the owner's objection, measured", w)

    check("sigma_1_inv_strictly_beats_sigma_1_by_energy_while_tying_by_count",
          rows["sigma_1^-1"]["E_cross"] < rows["sigma_1"]["E_cross"]
          and rows["sigma_1^-1"]["k"] == rows["sigma_1"]["k"],
          f"sigma_1^-1 E = {mp.nstr(rows['sigma_1^-1']['E_cross'], 12)} < "
          f"sigma_1 E = {mp.nstr(rows['sigma_1']['E_cross'], 12)}, both at k = 1 "
          f"and both reading-3-feasible. A negative crossing carries NEGATIVE "
          f"energy, which no count can see", w)
    print()

    # ---- 3. the degeneracy does not transfer ------------------------------
    print("== 3. does part 7's degeneracy transfer? ==")
    e_empty = ecross([])
    min_feas_e = min(feasible[n]["E_cross"] for n in feasible)
    print(f"    E_cross(empty)                  = {mp.nstr(e_empty, 12)}")
    print(f"    min E_cross over feasible gluons = {mp.nstr(min_feas_e, 12)}")
    check("the_empty_word_is_NOT_the_energy_minimum_on_the_gluon_family",
          min_feas_e < e_empty,
          f"{mp.nstr(min_feas_e, 12)} < {mp.nstr(e_empty, 12)}. gg words are "
          f"sign-BALANCED by construction so every non-empty one costs a "
          f"positive multiple of h; the gluon is outside that construction and "
          f"admits a bare negative crossing. So the degeneracy that retired "
          f"this functional in part 7 is specific to gg words and does NOT "
          f"transfer -- crossing energy is usable here", w)
    print()

    # ---- 4. still order-blind --------------------------------------------
    print("== 4. what it still cannot do ==")
    e_10 = rows["sigma_1 sigma_0"]["E_cross"]
    e_01 = rows["sigma_0 sigma_1"]["E_cross"]
    two_feas = {n: r for n, r in feasible.items() if r["k"] == 2}
    two_vals = {mp.nstr(r["E_cross"], 25) for r in two_feas.values()}
    print(f"    sigma_1 sigma_0 vs sigma_0 sigma_1 : "
          f"{mp.nstr(e_10, 12)} vs {mp.nstr(e_01, 12)}")
    print(f"    feasible 2-crossing gluons          : {sorted(two_feas)} "
          f"-> {len(two_vals)} distinct energy value(s)")
    check("crossing_energy_is_order_blind_and_ties_the_two_crossing_gluons",
          abs(e_10 - e_01) < TOL and len(two_vals) == 1,
          f"E_cross is a sum over letters, so reordering is invisible "
          f"({mp.nstr(abs(e_10 - e_01), 4)} apart) and all "
          f"{len(two_feas)} feasible 2-crossing gluons tie at one value. It "
          f"breaks the k = 1 tie and leaves the k = 2 tie standing -- which is "
          f"why an EMBEDDING energy, not a letter-sum, is what the question "
          f"actually needs", w)

    w.add_data("crossing_energy_convention", {
        "positive_crossing": "+q",
        "negative_crossing": "-1/q",
        "calibration": "electron 3q vs ~3.330, positron -3/q vs ~-2.703 "
                       "(pair-creation-energy.md)",
        "gamma_gamma_vertex": "q + (-1/q) = h",
        "undefined_on": "the bar-fixed letter d = -h/2 (not a crossing) -- the "
                        "implementation raises rather than fudging it",
    })
    w.add_data("candidates", {
        n: {"k": r["k"], "reading3_feasible": bool(r["feasible"]),
            "E_cross": mp.nstr(r["E_cross"], 25),
            "Q_beta_MeV": mp.nstr(r["Q_beta"], 20)}
        for n, r in rows.items()})
    w.add_data("selection", {
        "min_by_count": count_ties,
        "min_by_energy": by_energy[0],
        "they_disagree": True,
        "empty_is_energy_minimum": bool(e_empty <= min_feas_e),
        "note": "neither is adopted; both are proxies and RESULT 4 shows the "
                "energy does not separate the remaining candidates",
    })
    w.add_data("open_target_not_attempted", {
        "what": "an embedding energy -- O'Hara / Moebius via the Bring "
                "embedding -- which is order-SENSITIVE and can rank a longer "
                "word below a shorter one",
        "exists": ["mobius_cross_energy_hopf_calibration.py (calibrated "
                   "against the proved E(Hopf) = 2*pi^2)",
                   "mobius_cross_energy_borromean.py",
                   "QOU.MobiusEnergy (categorical E_cat; 2 sorries; its header "
                   "records a prior vacuity incident where classicalLimit made "
                   "E_cat blind)",
                   "Bring period matrix / mapping-torus residue machinery"],
        "missing": "any map from a braid word to a curve in or on the Bring "
                   "surface; the integrators consume hand-parametrised named "
                   "embeddings (Hopf, Borromean). Searched computations/ and "
                   "tools/ -- an absence on those surfaces, not a proof of "
                   "absence",
        "hard_part": "Moebius energy is a property of an EMBEDDING and is not "
                     "a knot invariant (the invariant is the infimum over the "
                     "isotopy class), so a bridge needs the minimiser or a "
                     "canonical embedding -- which is what the Bring surface "
                     "would be for",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited",
        "unconditional": [
            "E_cross = k*h on gamma-gamma words",
            "sigma_1 and sigma_1^-1 tie by count and differ by energy",
            "the empty word is not the energy minimum on the gluon family",
            "E_cross is order-blind and ties the 2-crossing gluons",
        ],
        "not_claimed": [
            "that sigma_1^-1 should be adopted",
            "that crossing energy is the right cost",
            "that no braid-to-Bring-embedding map exists anywhere",
        ],
        "no_selection_by_accuracy": "the Q_beta column is a reported "
                                    "consequence of each candidate and is not "
                                    "an input to any ordering here",
    })

    ok = not FAILED
    # AGENTS.md q0-anchor rule: "Say which pin you used. Any new witness
    # must record its q0 so a later reader can tell which layer it belongs
    # to without inferring it from a call site."
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.save()
    print()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
