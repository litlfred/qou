#!/usr/bin/env python3
"""The confinement SDP, both halves, selects EXACTLY ONE gamma-gamma word on
four strands: (v0 v1)^2 -- four vertices, eight letters, zero free parameters.

## Why this probe exists

`qou-ales` (owner ruling 2026-09-08) says every canonical braid word is selected
through gamma-gamma pair production AND the confinement SDP at q_0.
`qbeta_gamma_gamma_sdp_feasibility_probe` did the FEASIBILITY half: of 8190
gamma-gamma words on four strands, 5 are PSD-feasible, and on three strands
none is. It explicitly did not compute the other half, and said so:

    "no cost / minimality is computed. SDPSelected also requires minimal cost
     among feasible candidates, so this NARROWS the candidate set without
     selecting a word"

This is that half.

## The cost is the corpus's, not one chosen here

`mba-step10-confinement-sdp.md` states the program verbatim:

    minimize   Sum_i t_i x_i
    subject to net(x) = n_target,  G x >= 0,  x >= 0

with `t_i = tr_M(b_i)` the Markov-trace vector. So the objective on a WORD
candidate is its Markov trace, and `QOU.Mass.GammaGammaWordSelection.SDPSelected`
-- `mem`, `psd`, and `minimal : forall w' in cands, PSDFeasible w' -> cost w <=
cost w'` -- is evaluated with `cost = tr_M`. Nothing here is free to choose.

The trace is the general-n Ocneanu recursion from
`qbeta_ocneanu_trace_general_n_probe`, which reproduces `pyhecke.gram`'s
hand-coded H_3 vector symbolically in both `h` and `z` and satisfies the trace
and Markov properties at `n = 4` -- neither of which is an input to it.

## The result

Costs at `z_D = q^3/(q^2+1)`, proton pin, over the five PSD-feasible words:

    (0,1,0,1)                      = (v0 v1)^2    1.032897755524660383   <- MIN
    (0,0,1,1,0,1,1,0,0,1)          sporadic       1.073238807935729209
    (0,1,1,0,0,1,0,0,1,1)          sporadic       1.073238807935729209
    (0,1,0,1,0,1,0,1)              = (v0 v1)^4    1.137405209118677445
    (0,1,0,1,0,1,0,1,0,1,0,1)      = (v0 v1)^6    1.331992492573499969

**The minimum is attained, not merely least-in-a-truncation** (CHECK 3): the
cost on the even alternating family is STRICTLY INCREASING in `m` --
1.0329, 1.1374, 1.3320, 1.6511, 2.1510, 2.9201 for `m = 2..12` -- so extending
the enumeration cannot produce a cheaper member of that family. The two
sporadic words are dearer than the minimum, and are the only other feasible
words found to 12 vertices.

**So `SDPSelected` has a unique solution among the words tested, and it is
`(v0 v1)^2`.** Four vertices, eight letters, on four strands. Derived: no
continuous parameter is tuned, no discrete choice is made against a measured
value, and no observable enters the selection at any point.

## 🛑 Two honest gaps, neither of which the result may be quoted without

1. **The LP's `net(x) = n_target` constraint is NOT imposed.** It belongs to
   the mixture formulation (`x` a non-negative vector over the NF basis), and
   `SDPSelected` as stated in Lean carries no analogue for a single-word
   candidate. This probe reports `net` for each feasible word (CHECK 5) so the
   constraint can be applied later, and applies it to nothing.
2. **"Unique" means unique among gamma-gamma words of at most 12 vertices on
   four strands.** The feasible set is not characterised -- the two sporadic
   words show it is not merely the even alternating family -- so a cheaper
   feasible word at 13+ vertices is not excluded by anything here. What IS
   excluded is a cheaper member of the alternating family, by the monotonicity
   above.

## 🛑 And what must NOT be done with it

No `Q_beta` comparison is made or implied. `Q_beta = |eps(Delta)| * E_0` is an
`H_3` construction -- `E_0` and the element-to-observable map are three-strand
objects and the corpus does not define their `n = 4` analogue. Reporting a
residual for this word would also re-introduce exactly the selection-against-
the-target that the sibling probes measured and rejected. The word is derived;
what it predicts is a separate question and is not answered here.

Scope-(a). Selects a word *within the corpus's own stated predicate*; wires
nothing, and moves no number in the corpus.
"""

from __future__ import annotations

import importlib.util
import os
import sys
import warnings

import sympy as sp

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "computations/qbeta",
           "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

_OC = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_ocneanu_trace_general_n_probe.py")
_spec = importlib.util.spec_from_file_location("_oc", _OC)
_oc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_oc)

_FE = os.path.join(ROOT, "computations", "qbeta",
                   "qbeta_gamma_gamma_sdp_feasibility_probe.py")
_spec2 = importlib.util.spec_from_file_location("_fe", _FE)
_fe = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(_fe)

set_compute_dps(60)
mp.mp.dps = 40

h = _oc.h
H0 = _oc.H0
ZD = _oc.ZD
Q0 = _oc.Q0
word_to_vec = _oc.word_to_vec
tr = _oc.tr

HR = sp.Rational(str(H0))
ZR = sp.Rational(str(ZD))

#: the five PSD-feasible words, from the sibling probe's measurement.
FEASIBLE = [
    ((0, 1, 0, 1), "(v0 v1)^2"),
    ((0, 1, 0, 1, 0, 1, 0, 1), "(v0 v1)^4"),
    ((0, 0, 1, 1, 0, 1, 1, 0, 0, 1), "sporadic A (10 vertices)"),
    ((0, 1, 1, 0, 0, 1, 0, 0, 1, 1), "sporadic B (10 vertices)"),
    ((0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1), "(v0 v1)^6"),
]

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def gg_vec(combo, n: int = 4):
    """The gamma-gamma word's normal form, `h` already specialised."""
    lets = []
    for i in combo:
        lets += [(i, sp.Integer(0)), (i + 1, -HR)]
    return word_to_vec(lets, n, {}, HR)


def cost(combo, n: int = 4):
    """The LP objective on a word candidate: its Markov trace at `z_D`."""
    return mp.mpf(str(sp.N(tr(gg_vec(combo, n), n, HR, ZR), 35)))


def net(combo, n: int = 4):
    """`net(x)` = the coordinate sum, for the constraint this probe does NOT
    impose. Reported so it can be imposed later."""
    v = gg_vec(combo, n)
    return mp.mpf(str(sp.N(sum(v.values()), 35)))


def main() -> int:
    w = WitnessBuilder("qbeta-sdp-selects-a-unique-word")
    w.set_description(
        "The minimality half of GammaGammaWordSelection.SDPSelected, with the "
        "cost the corpus states (t_i = tr_M(b_i), mba-step10-confinement-sdp). "
        "Over the five PSD-feasible gamma-gamma words on four strands the "
        "unique minimiser is (v0 v1)^2 -- four vertices, eight letters -- and "
        "the minimum is ATTAINED, since the cost on the even alternating "
        "family is strictly increasing in m. Derived: nothing is tuned and no "
        "observable enters. Two gaps stated: the LP's net(x) = n_target "
        "constraint is not imposed (net is reported so it can be), and "
        "'unique' means among words of at most 12 vertices. NO Q_beta "
        "comparison is made -- E_0 is an H_3 construction. Scope-(a)."
    )

    print("Assertions:")

    # ---------------------------------------------------------------- CHECK 1
    # Calibration: the trace machinery still reproduces the corpus H_3 vector.
    # Imported rather than re-derived, but re-verified here so this file does
    # not inherit a silent breakage.
    B3 = [(), (0,), (1,), (1, 0), (0, 1), (0, 1, 0)]
    z = sp.Symbol("z")
    ref = [sp.Integer(1), z, z, z ** 2, z ** 2, z * (h * z + 1)]
    bad = []
    for slot, wrd in enumerate(B3):
        p = _oc.perm_of_word(wrd, 3)
        if sp.simplify(tr({p: sp.Integer(1)}, 3) - ref[slot]) != 0:
            bad.append(wrd)
    check("trace_still_reproduces_the_corpus_h3_vector", not bad,
          f"all six slots of pyhecke.gram's TR_M, symbolic in (h, z); "
          f"mismatches: {bad or 'none'} -- re-verified here so this file "
          f"cannot inherit a silent breakage of the imported recursion", w)

    # ---------------------------------------------------------------- CHECK 2
    # The costs.
    rows = [(c, label, cost(c), net(c)) for c, label in FEASIBLE]
    rows_sorted = sorted(rows, key=lambda r: r[2])
    best = rows_sorted[0]
    check("the_unique_minimiser_is_the_two_fold_alternating_word",
          best[0] == (0, 1, 0, 1)
          and all(r[2] > best[2] for r in rows_sorted[1:]),
          f"costs over the 5 PSD-feasible words: "
          f"{[(r[1], mp.nstr(r[2], 16)) for r in rows_sorted]} -- the minimum "
          f"is {best[1]} at {mp.nstr(best[2], 20)}, and it is STRICT (every "
          f"other feasible word costs more)", w)

    # ---------------------------------------------------------------- CHECK 3
    # The minimum is ATTAINED, not merely least in a truncation.
    fam = [(m, cost(tuple((0, 1) * m))) for m in range(2, 15, 2)]
    increasing = all(fam[i][1] < fam[i + 1][1] for i in range(len(fam) - 1))
    check("cost_is_strictly_increasing_on_the_even_alternating_family",
          increasing and fam[0][1] == best[2],
          f"(v0 v1)^m for m = {[m for m, _ in fam]}: "
          f"{[mp.nstr(v, 12) for _, v in fam]} -- strictly increasing, so "
          f"extending the enumeration cannot produce a cheaper member of this "
          f"family and the minimum at m = 2 is ATTAINED rather than merely "
          f"least-so-far", w)

    # ---------------------------------------------------------------- CHECK 4
    # The two sporadic words cost exactly the same -- an observation, flagged.
    spor = [r for r in rows if r[1].startswith("sporadic")]
    same = abs(spor[0][2] - spor[1][2]) < mp.mpf("1e-30")
    check("the_two_sporadic_words_have_equal_cost", same,
          f"sporadic A and B both cost {mp.nstr(spor[0][2], 20)} (agreeing to "
          f"< 1e-30). Recorded as an OBSERVATION -- nothing here explains it, "
          f"and two data points are not a pattern", w)

    # ---------------------------------------------------------------- CHECK 5
    # The constraint this probe does NOT impose, reported so it can be.
    nets = [(r[1], mp.nstr(r[3], 20)) for r in rows_sorted]
    check("net_is_reported_for_every_feasible_word", len(nets) == len(FEASIBLE),
          f"net(x) = coordinate sum per feasible word: {nets}. The LP's "
          f"net(x) = n_target constraint is NOT imposed here -- it belongs to "
          f"the mixture formulation and SDPSelected carries no single-word "
          f"analogue -- so these are reported for a later pass, and applied to "
          f"nothing", w)

    # ------------------------------------------------------------------ data
    w.add_data("cost_definition",
               "t_i = tr_M(b_i), the Markov-trace vector of "
               "mba-step10-confinement-sdp's LP `minimize Sum_i t_i x_i`; "
               "evaluated at z_D = q^3/(q^2+1), proton pin")
    w.add_data("feasible_words_by_cost", [
        {"word": list(r[0]), "label": r[1],
         "cost_tr_M": mp.nstr(r[2], 25), "net": mp.nstr(r[3], 25)}
        for r in rows_sorted])
    w.add_data("selected", {
        "word": list(best[0]), "label": best[1],
        "cost_tr_M": mp.nstr(best[2], 25),
        "vertices": len(best[0]), "letters": 2 * len(best[0]),
        "strands": 4,
        "derivation": "SDPSelected = mem + psd + minimal, with cost the "
                      "corpus's LP objective; no continuous parameter tuned, "
                      "no discrete choice made against a measured value, no "
                      "observable entering at any point"})
    w.add_data("alternating_family_costs",
               [{"m": m, "cost": mp.nstr(v, 25)} for m, v in fam])
    w.add_data("scope", "a")
    w.add_data("gaps_stated", [
        "the LP's net(x) = n_target constraint is NOT imposed; net is "
        "reported per word so it can be applied later",
        "'unique' means unique among gamma-gamma words of at most 12 vertices "
        "on four strands; the feasible set is not characterised, so a cheaper "
        "feasible word at 13+ vertices is not excluded -- what IS excluded is "
        "a cheaper member of the alternating family, by monotonicity",
        "NO Q_beta comparison is made or implied: E_0 and the "
        "element-to-observable map are H_3 constructions with no corpus-"
        "defined n = 4 analogue, and reporting a residual would re-introduce "
        "the selection-against-the-target the sibling probes rejected"])
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.add_data("z_convention", "D, z_D = q^3/(q^2+1)")

    print()
    print("  PSD-feasible words by cost (tr_M at z_D):")
    for r in rows_sorted:
        mark = "   <- SELECTED" if r[0] == best[0] else ""
        print(f"    {str(r[0]):38s} {r[1]:26s} {mp.nstr(r[2], 20)}{mark}")
    print(f"\n  SDPSelected -> {best[1]} = {best[0]}: "
          f"{len(best[0])} vertices, {2 * len(best[0])} letters, 4 strands")

    w.save()
    print()
    if FAILED:
        print(f"FAILED ({len(FAILED)}): {', '.join(FAILED)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
