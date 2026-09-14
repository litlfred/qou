#!/usr/bin/env python3
"""qou-99qc: what DOES fix the crossing budget once reading 3 is the live
criterion — the corpus's own cost function, and it does not select 11.

# Ref: computations/qbeta/qbeta_reading3_does_not_constrain_the_budget_probe.py  (reading 3 admits every k)
# Ref: content/quantum-observable-universe/lean/QOU/Mass/GammaGammaFrobeniusSelection.lean
# Ref: computations/qbeta/qbeta_gamma_gamma_sdp_feasibility_probe.py   (is_psd / blocks)
# Ref: .beans/qou-ales--...md   (OWNER RULING 2026-09-12: reading 3 selected)
# Ref: .beans/qou-99qc--...md

THE SETUP. The sibling probe establishes that reading 3 — `chi_lambda(w) >= 0`
on every block with `y_lambda > 0`, the owner-selected criterion — admits EVERY
dressing count k = 0..3 for both nucleons, so it does not fix the budget. That
leaves the question open rather than answered, and this probe asks what closes
it.

THE ANSWER IS ALREADY IN THE CORPUS, and it is not a new principle. The Lean
selection structure is `FrobeniusSelected B y cands cost w`: `w` is
reading-3-feasible AND `cost w <= cost w'` for every feasible candidate. The
cost the corpus instantiates is the **crossing count**,
`fun w => (w.length : R)` (`frobeniusSelected_borromean`, which selects
`beta_Bor` = the 6-letter core exactly this way). So the budget question has a
derived answer: **the minimal-cost reading-3-feasible dressing.**

RESULT 1 -- MINIMAL COST SELECTS k = 0, NOT k = 2. The empty dressing is
reading-3-feasible (4 of 8 generator assignments, both nucleons), so the
cost-minimal word is the **9-letter** `core + quark` with NO gluon dressing.
The live model is `nuc11_interleaved`, k = 2. **It is not cost-minimal.**

RESULT 2 -- AND IF THE EMPTY DRESSING IS EXCLUDED, THE ANSWER IS k = 1, STILL
NOT 2. `frobeniusSelected_nil` records that with the crossing-count cost the
EMPTY word is trivially selected — which is exactly why the core selection
restricts its candidates to non-zero vertex powers. Whether the same exclusion
applies to the dressing is an unstated modelling choice. It does not rescue 11:
excluding the empty dressing gives k = 1 (18 of 48 feasible), a 10-letter word.
**Under either convention the live 11-letter budget is not what the corpus's own
selection principle picks.**

RESULT 3 -- THE PRINCIPLE FIXES THE BUDGET, NOT THE WORD. At k = 0 four
generator assignments are feasible per nucleon, carrying only **two** distinct
traces each (proton 0.6121259628 / 0.6263353681; neutron 0.4830505246 /
0.4902320181). `FrobeniusSelected.cost_eq` says two selected words share a cost,
not that the word is unique — and measured, it is not. A residual 2-fold
degeneracy survives the selection and is NOT closed here.

RESULT 4 -- READING 1 IS FEASIBLE NOWHERE IN THIS FAMILY, AND THAT IS STRONGER
THAN THE PARITY ARGUMENT. Checking literal `Matrix.PosSemidef` on every
Wedderburn block: **0 feasible of 8 / 48 / 288 / 1728 at k = 0/1/2/3, for both
nucleons.** The zeros at k = 1 and k = 3 are the interesting ones — those are
EVEN total lengths, which the alternating-character parity theorem
(`alt_psd_iff_even`) permits. So reading 1 excludes them by a different and
less elegant mechanism, the `(2,1)` block's symmetry, and the parity theorem is
not the binding constraint even where it applies. **This corrects my own
framing in the sibling probe**, which reported reading 1 as annihilating *by
parity*; it is annihilating outright.

WHAT IS NOT CLAIMED. That k = 0 should be adopted — that is the owner's call,
it hangs on the unstated empty-dressing convention, and this probe deliberately
does not re-score the dashboard. That the cost function is right: extending the
H_3 core's crossing-count cost to the dressing is an extrapolation of the
corpus's principle, not a theorem about it. That the 2-fold degeneracy is
harmless. No selection was made by proximity to any measured value, and no
Q_beta residual is computed here for precisely that reason.

ARITHMETIC. mpmath mpf at 60 dps, proton pin, convention D. No float64.

Run: python3 -u computations/qbeta/qbeta_cost_minimal_budget_under_reading3_probe.py \
       2>&1 | tee /tmp/qbeta_cost_minimal_budget.log
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402

_ROOT = _HERE.parent.parent
_FE = os.path.join(_ROOT, "computations", "qbeta",
                   "qbeta_gamma_gamma_sdp_feasibility_probe.py")
_spec = importlib.util.spec_from_file_location("_fe", _FE)
_fe = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_fe)

mp = _order.mp
set_compute_dps(60)
mp.mp.dps = 60

Q0, H0, ZD = _order.Q0, _order.H0, _order.ZD
Y3 = (Q0 ** 4 + 1) / (Q0 ** 2 + 1) ** 2
Y21 = Q0 ** 2 / (Q0 ** 2 + 1) ** 2

Z, HALF, NEG1 = mp.mpf(0), mp.mpf(-1) / 2, mp.mpf(-1)
SHIFTS = (Z, HALF, NEG1)
CORE = [(0, Z), (1, NEG1)] * 3
QSHIFT = {"p": [Z, HALF, HALF], "n": [HALF, HALF, NEG1]}

#: the live model's dressing count (`nuc11_interleaved` = 6 + 3 + 2).
LIVE_K = 2

B3 = _fe.blocks(3)
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
    """`chi_lambda >= 0` on every block with `y_lambda > 0` -- under D that is
    `(3)` and `(2,1)`; `y_(1^3) = 0`."""
    return chi3(letters) >= 0 and chi21(letters) >= 0


def reading1(letters) -> bool:
    """Literal `Matrix.PosSemidef` on EVERY Wedderburn block -- the parked
    reading, checked here to measure what it would select."""
    for sig, dim in B3.values():
        M = mp.eye(dim)
        for g, d in letters:
            M = M * (sig[g] + (d * H0) * mp.eye(dim))
        if not _fe.is_psd(M, dim):
            return False
    return True


def words_at(nuc: str, k: int):
    for qg in itertools.product((0, 1), repeat=3):
        base = CORE + [(g, s) for g, s in zip(qg, QSHIFT[nuc])]
        if k == 0:
            yield qg, (), base
            continue
        for dr in itertools.product(itertools.product((0, 1), SHIFTS), repeat=k):
            yield qg, dr, base + list(dr)


def main() -> int:
    w = WitnessBuilder("qbeta-cost-minimal-budget-under-reading3")
    w.set_description(
        "Reading 3 admits every dressing count, so it does not fix the crossing "
        "budget. The corpus's own selection principle does: FrobeniusSelected "
        "takes the MINIMAL-COST reading-3-feasible candidate with cost = "
        "crossing count (the Lean's own instantiation, which selects beta_Bor "
        "for the core). Applied to the dressing that gives k = 0 -- the "
        "9-letter word, no gluon crossings -- and k = 1 if the empty dressing "
        "is excluded the way frobeniusSelected_nil forced for the core. Either "
        "way the live 11-letter nuc11_interleaved (k = 2) is NOT what the "
        "principle selects. The principle fixes the BUDGET, not the word: four "
        "assignments tie at k = 0 carrying two distinct traces per nucleon. And "
        "reading 1 is feasible NOWHERE in this family (0 of 8/48/288/1728), "
        "including at the EVEN lengths the parity theorem permits -- so it is "
        "annihilating outright, not by parity, correcting my own framing."
    )

    print("qou-99qc — the cost-minimal budget under the live reading")
    print(f"  q0 (proton pin) = {mp.nstr(Q0, 20)}")
    print(f"  z_D             = {mp.nstr(ZD, 20)}")
    print()

    # ---- 1. calibration -------------------------------------------------
    print("== 1. calibration ==")
    tot = Y3 + 2 * Y21
    check("y_1cubed_vanishes_under_convention_D",
          abs(tot - 1) < TOL,
          f"y_(3) + 2 y_(2,1) = 1 to {mp.nstr(abs(tot - 1), 4)}, so y_(1^3) = 0 "
          f"exactly and reading 3 sees only (3) and (2,1)", w)
    check("chi21_of_the_identity_is_the_block_dimension",
          abs(chi21([]) - 2) < TOL,
          f"chi_(2,1)(1) = {mp.nstr(chi21([]), 20)} = 2, the block dimension -- "
          f"the extraction is calibrated before any verdict", w)
    print()

    # ---- 2. the sweep, both readings -------------------------------------
    print("== 2. feasibility by dressing count, both readings ==")
    print("   k  len  parity   reading 3 (p)    reading 3 (n)   reading 1 p/n")
    table = {}
    for k in range(0, 4):
        row = {}
        for nuc in ("p", "n"):
            f3 = f1 = n = 0
            for _, _, word in words_at(nuc, k):
                n += 1
                if reading3(word):
                    f3 += 1
                if reading1(word):
                    f1 += 1
            row[nuc] = (f3, f1, n)
        table[k] = row
        par = "even" if (9 + k) % 2 == 0 else "odd"
        print(f"   {k}   {9 + k:2d}   {par:4s}    "
              f"{row['p'][0]:4d}/{row['p'][2]:<7d} {row['n'][0]:4d}/{row['n'][2]:<7d} "
              f"  {row['p'][1]}/{row['n'][1]}")

    r1_total = sum(table[k][n][1] for k in table for n in ("p", "n"))
    check("reading1_is_feasible_NOWHERE_in_this_family",
          r1_total == 0,
          f"{r1_total} reading-1-feasible words across all k = 0..3 and both "
          f"nucleons, out of {sum(table[k][n][2] for k in table for n in ('p','n'))} "
          f"checked. Literal Matrix.PosSemidef on every block admits nothing "
          f"here", w)

    even_k_r1 = table[1]["p"][1] + table[1]["n"][1] + table[3]["p"][1] + table[3]["n"][1]
    check("reading1_fails_even_at_the_EVEN_lengths_parity_permits",
          even_k_r1 == 0,
          "k = 1 and k = 3 are total lengths 10 and 12, which alt_psd_iff_even "
          "permits, and reading 1 still admits ZERO. So the (2,1) block excludes "
          "them independently of parity -- the parity theorem is not the binding "
          "constraint even where it applies, which CORRECTS my own sibling-probe "
          "framing of reading 1 as annihilating 'by parity'", w)
    print()

    # ---- 3. the cost-minimal selection ----------------------------------
    print("== 3. minimal crossing-count among reading-3-feasible ==")
    feasible_k = sorted(k for k in table
                        if table[k]["p"][0] > 0 and table[k]["n"][0] > 0)
    k_min = feasible_k[0]
    k_min_nonempty = min(k for k in feasible_k if k > 0)
    print(f"    cost = word length (the Lean's own instantiation)")
    print(f"    reading-3-feasible k: {feasible_k}")
    print(f"    minimal cost                      -> k = {k_min} (length {9 + k_min})")
    print(f"    minimal cost, empty dressing excluded -> k = {k_min_nonempty} "
          f"(length {9 + k_min_nonempty})")

    check("minimal_cost_selects_k_zero_not_the_live_eleven",
          k_min == 0 and k_min != LIVE_K,
          f"the empty dressing is reading-3-feasible "
          f"({table[0]['p'][0]}/{table[0]['p'][2]} proton, "
          f"{table[0]['n'][0]}/{table[0]['n'][2]} neutron), so the cost-minimal "
          f"word is the 9-letter core+quark with NO gluon dressing. The live "
          f"model is k = {LIVE_K}", w)

    check("excluding_the_empty_dressing_gives_one_still_not_two",
          k_min_nonempty == 1 and k_min_nonempty != LIVE_K,
          f"frobeniusSelected_nil records that the crossing-count cost makes the "
          f"EMPTY word trivially selected, which is why the core selection "
          f"restricts to non-zero vertex powers. Applying the same exclusion to "
          f"the dressing gives k = 1 (length 10), NOT k = {LIVE_K}. So the live "
          f"budget is unselected under both conventions", w)
    print()

    # ---- 4. the residual degeneracy -------------------------------------
    print("== 4. does the principle pin ONE word? ==")
    degeneracy = {}
    for nuc in ("p", "n"):
        feas = [(qg, word) for qg, _, word in words_at(nuc, k_min)
                if reading3(word)]
        traces = sorted({mp.nstr(tr(word), 20) for _, word in feas})
        degeneracy[nuc] = {"n_words": len(feas), "traces": traces}
        print(f"    {nuc}: {len(feas)} feasible words, {len(traces)} distinct traces")
        for t in traces:
            print(f"        tr = {t}")

    check("the_cost_minimal_set_does_NOT_pin_a_unique_trace",
          all(len(degeneracy[n]["traces"]) > 1 for n in ("p", "n")),
          f"proton {degeneracy['p']['n_words']} words / "
          f"{len(degeneracy['p']['traces'])} traces, neutron "
          f"{degeneracy['n']['n_words']} / {len(degeneracy['n']['traces'])}. "
          f"FrobeniusSelected.cost_eq gives equal COST, not a unique word, and "
          f"measured the words do not agree on the trace. A 2-fold degeneracy "
          f"survives the selection and is NOT closed here", w)

    w.add_data("cost_function", {
        "source": "QOU/Mass/GammaGammaFrobeniusSelection.lean, "
                  "frobeniusSelected_borromean",
        "cost": "fun w => (w.length : R) -- the crossing count",
        "principle": "FrobeniusSelected = reading-3-feasible AND minimal cost "
                     "among feasible candidates",
        "caveat": "extending the H_3 core's cost to the dressing is an "
                  "extrapolation of the corpus's principle, not a theorem",
    })
    w.add_data("feasibility_by_k", {
        f"k{k}": {"length": 9 + k,
                  "parity": "even" if (9 + k) % 2 == 0 else "odd",
                  "reading3_p": table[k]["p"][0], "reading3_n": table[k]["n"][0],
                  "reading1_p": table[k]["p"][1], "reading1_n": table[k]["n"][1],
                  "total_p": table[k]["p"][2], "total_n": table[k]["n"][2]}
        for k in table})
    w.add_data("selection", {
        "k_min": k_min,
        "k_min_excluding_empty": k_min_nonempty,
        "live_model_k": LIVE_K,
        "verdict": "the live 11-letter nuc11_interleaved is cost-minimal under "
                   "NEITHER convention",
        "residual_degeneracy": degeneracy,
    })
    w.add_data("scope", {
        "class": "(a) scope-limited",
        "unconditional": [
            "reading 1 admits 0 words in this family at k = 0..3",
            "the empty dressing is reading-3-feasible",
            "k = 2 is not the reading-3 cost minimum, with or without the "
            "empty dressing",
            "the cost-minimal set carries 2 distinct traces per nucleon",
        ],
        "not_claimed": [
            "that k = 0 should be adopted -- owner's call, and it hangs on the "
            "unstated empty-dressing convention",
            "that the crossing-count cost is the right cost for the dressing",
            "any re-scoring of the L2 dashboard",
        ],
        "no_selection_by_accuracy": "no Q_beta residual is computed here, "
                                    "deliberately -- the selection is by "
                                    "derived cost, never by proximity to the "
                                    "measured value",
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
