#!/usr/bin/env python3
"""🛑 RETRACTION + the correct result. The SDP's minimality half does NOT select
a word: the EMPTY word is PSD-feasible with cost exactly 1.0, strictly below
every non-empty candidate. Feasibility does all the work; minimality is
degenerate, exactly as the corpus already proves for the continuous LP.

## What this file first claimed, and why it was wrong

An earlier version of this probe was named `qbeta_sdp_selects_a_unique_word`
and concluded that `GammaGammaWordSelection.SDPSelected` has a unique solution,
`(v0 v1)^2`. **It does not.** That conclusion silently restricted the candidate
set to words with at least one vertex. The empty gamma-gamma word -- zero
vertices, the identity of `H_n` -- is PSD-feasible in every block (trivially:
the identity matrix is PSD) and its Markov trace is exactly `1.0`, against
`1.032897755524660383` for `(v0 v1)^2`. So over the gamma-gamma candidate set
as the Lean states it, `SDPSelected` selects the EMPTY WORD, which is vacuous.

I found this by reading `prop:operator-selection-lp` properly, which I had
cited for the cost function without reading its §"Degeneracy of this program".

## The corpus already proved this, one level up

That section proves two things about the continuous LP and says plainly that
*"downstream blocks have read the program as a selection principle, which it
is not"*:

  * **The optimal value is identically zero.** The NF basis begins with the
    empty word, so `b_1 = 1` and `G_1j = tr_M(1 * b_j) = t_j`: the first row of
    the Gram matrix IS the objective vector, so the Frobenius positivity
    constraint at `i = 1` reads `Sum_j t_j x_j >= 0` -- the objective, bounded
    below by zero. Holds for every `n`, every `q`, every trace convention.
  * **The minimiser set is not a point** but a positive-dimensional,
    mirror-closed face with no mirror-symmetric vertex, so which vertex a
    solver returns is a property of its pivoting rule.

**The identity being in the basis is the cause in both settings.** In the
continuous LP it makes the positivity constraint coincide with the objective;
in the discrete gamma-gamma candidate set it is itself the cheapest feasible
candidate. This probe is therefore an independent confirmation of that
proposition in a setting it does not cover -- and I became one of the
downstream readers it warns about before I became a confirmation of it.

## What actually survives

Two things, and they should be quoted separately:

1. **Feasibility does the real work, and that result is untouched.** The
   sibling probe's 5-of-8190 at `n = 4` and none-at-`n = 3` stand: PSD
   feasibility is a genuine, structural, zero-parameter filter.
2. **Among NON-EMPTY gamma-gamma words** of at most 12 vertices on four
   strands, `(v0 v1)^2` is the strict minimiser, and the minimum is ATTAINED
   rather than least-in-a-truncation -- the cost on the even alternating
   family is strictly increasing in `m` (1.0329 -> 4.0944 for `m = 2..14`).
   That is a true statement about a restricted candidate set. It is NOT
   `SDPSelected`, and calling it that requires an exclusion of the identity
   that nothing in the corpus licenses.

## Scope

Scope-(a). The cost is the corpus's (`t_i = tr_M(b_i)`, from the LP objective,
whose identification as the linear functional `tr_M` is unaffected by the
degeneracy -- what the degeneracy changes is whether minimising it selects
anything). No `Q_beta` comparison is made: `E_0` and the
element-to-observable map are `H_3` constructions with no corpus-defined
`n = 4` analogue. Selects nothing, wires nothing, moves no number.
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
    w = WitnessBuilder("qbeta-sdp-minimality-is-degenerate")
    w.set_description(
        "RETRACTION: the SDP's minimality half does NOT select a word. The "
        "EMPTY gamma-gamma word is PSD-feasible with Markov trace exactly "
        "1.0, strictly below every non-empty candidate, so SDPSelected over "
        "the candidate set as stated selects it -- vacuously. This is the "
        "discrete form of the degeneracy prop:operator-selection-lp already "
        "proves for the continuous LP (b_1 = 1 makes the first Frobenius "
        "positivity constraint coincide with the objective), and that block "
        "warns downstream readers against reading the program as a selection "
        "principle. What survives: FEASIBILITY does the work (5 of 8190 at "
        "n=4, none at n=3, sibling probe, untouched); and among NON-EMPTY "
        "words of <= 12 vertices (v0 v1)^2 is the strict minimiser with the "
        "minimum attained. Scope-(a)."
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
    # 🛑 THE RETRACTION. The empty word is a gamma-gamma word (the empty
    # product of vertices -- GammaGammaWord.nil), it is PSD-feasible in every
    # block because the identity matrix is PSD, and its Markov trace is the
    # normalisation tr_M(1) = 1. So it is the cheapest feasible candidate and
    # SDPSelected picks it. An earlier version of this file concluded
    # otherwise by silently restricting to words with >= 1 vertex.
    empty_cost = cost(())
    rows = [(c, label, cost(c), net(c)) for c, label in FEASIBLE]
    rows_sorted = sorted(rows, key=lambda r: r[2])
    best_nonempty = rows_sorted[0]
    check("empty_word_is_feasible_and_strictly_cheapest_so_minimality_is_degenerate",
          abs(empty_cost - 1) < mp.mpf("1e-30")
          and all(r[2] > empty_cost for r in rows_sorted),
          f"tr_M(empty word) = {mp.nstr(empty_cost, 20)} exactly (the trace "
          f"normalisation), against {mp.nstr(best_nonempty[2], 20)} for the "
          f"cheapest non-empty feasible word. The empty word is a gamma-gamma "
          f"word (GammaGammaWord.nil) and is PSD-feasible in every block, so "
          f"SDPSelected over the candidate set AS STATED selects it -- "
          f"vacuously. Minimality does not select", w)

    # ---------------------------------------------------------------- CHECK 2b
    # What survives, stated as the restricted claim it is.
    check("among_non_empty_words_the_minimiser_is_the_two_fold_alternating_word",
          best_nonempty[0] == (0, 1, 0, 1)
          and all(r[2] > best_nonempty[2] for r in rows_sorted[1:]),
          f"costs over the 5 PSD-feasible NON-EMPTY words: "
          f"{[(r[1], mp.nstr(r[2], 16)) for r in rows_sorted]} -- strict "
          f"minimum {best_nonempty[1]} at {mp.nstr(best_nonempty[2], 20)}. "
          f"A true statement about a RESTRICTED candidate set; it is not "
          f"SDPSelected, and calling it that needs an exclusion of the "
          f"identity that nothing in the corpus licenses", w)

    # ---------------------------------------------------------------- CHECK 3
    # The minimum is ATTAINED, not merely least in a truncation.
    fam = [(m, cost(tuple((0, 1) * m))) for m in range(2, 15, 2)]
    increasing = all(fam[i][1] < fam[i + 1][1] for i in range(len(fam) - 1))
    check("cost_is_strictly_increasing_on_the_even_alternating_family",
          increasing and fam[0][1] == best_nonempty[2],
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
    w.add_data("degeneracy", {
        "empty_word_cost": mp.nstr(empty_cost, 25),
        "empty_word_is_psd_feasible": True,
        "verdict": "SDPSelected over the gamma-gamma candidate set as stated "
                   "selects the EMPTY word; minimality does not select",
        "corpus_already_proves_this_for_the_LP":
            "prop:operator-selection-lp §'Degeneracy of this program': b_1 = 1 "
            "makes G_1j = t_j, so the first Frobenius positivity constraint IS "
            "the objective bounded below by zero; optimal value identically 0 "
            "for every n, q and trace convention, and the minimiser set is a "
            "positive-dimensional mirror-closed face. That block states "
            "downstream readers have wrongly taken the program as a selection "
            "principle",
        "what_survives": "FEASIBILITY (5 of 8190 at n=4, none at n=3) is "
                         "untouched and does the real work"})
    w.add_data("restricted_minimiser", {
        "word": list(best_nonempty[0]), "label": best_nonempty[1],
        "cost_tr_M": mp.nstr(best_nonempty[2], 25),
        "vertices": len(best_nonempty[0]), "letters": 2 * len(best_nonempty[0]),
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
    print(f"  EMPTY word (0 vertices)                tr_M = "
          f"{mp.nstr(empty_cost, 20)}   <- PSD-feasible, and CHEAPEST")
    print("  PSD-feasible NON-EMPTY words by cost (tr_M at z_D):")
    for r in rows_sorted:
        mark = "   <- min among non-empty" if r[0] == best_nonempty[0] else ""
        print(f"    {str(r[0]):38s} {r[1]:26s} {mp.nstr(r[2], 20)}{mark}")
    print()
    print("  SDPSelected over the candidate set AS STATED -> the EMPTY word.")
    print("  Minimality does NOT select; feasibility does the work.")
    print(f"  Restricted to non-empty words: {best_nonempty[1]} = "
          f"{best_nonempty[0]}, {len(best_nonempty[0])} vertices, "
          f"{2 * len(best_nonempty[0])} letters, 4 strands -- a statement "
          f"about a restricted set, NOT SDPSelected.")

    w.save()
    print()
    if FAILED:
        print(f"FAILED ({len(FAILED)}): {', '.join(FAILED)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
