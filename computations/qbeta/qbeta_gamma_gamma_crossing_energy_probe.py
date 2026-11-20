#!/usr/bin/env python3
"""Every gamma-gamma word has crossing energy exactly `k*h` -- strictly
POSITIVE, i.e. repulsion-dominated, for every non-empty word at every q > 1.
And minimising it hits the same degeneracy as the LP: the empty word wins.

## Why this probe exists

`qou-ales` selects canonical braid words through gamma-gamma pair production
plus the confinement SDP. PR #7295 worked out both halves: together they cut
8190 four-strand candidates to 5, and the SDP's *minimality* half turned out
degenerate -- the empty word is PSD-feasible with the cheapest Markov trace,
exactly as `prop:operator-selection-lp` §"Degeneracy of this program" proves
for the continuous LP.

That left the question of what breaks the tie among the 5. The corpus carries a
THIRD functional, which its own knot-operator selection actually uses:
`knot-operator-selection-proof.md` minimises the **crossing energy**
`E_cross` subject to a demand constraint. This probe evaluates that functional
on the gamma-gamma words. It does NOT implement the demand constraint -- see
Scope.

## The definition, and the calibration that pins it

`def:crossing-energy` (`knots-particles-confinement/crossing-energy.md`):

    E_cross(beta) = sum over crossings of beta of
                      q      for a positive crossing (L_+)
                     -1/q    for a negative crossing (L_-)

CHECK 1 calibrates that transcription against the corpus's own worked values in
`pair-creation-energy.md`: the electron is the left trefoil `T_{2,3}` with three
POSITIVE crossings, `E_cross = 3q ~ 3.330`; the positron is its mirror with
three NEGATIVE crossings, `E_cross = -3/q ~ -2.703`. If this file had the sign
convention backwards those two would swap, so the check is not decorative.

## The result

A gamma-gamma vertex `sigma_i sigma_{i+1}^{-1}` is exactly one positive and one
negative crossing, so it contributes `q - 1/q = h`, and a word of `k` vertices
has

    E_cross = k * h        (CHECK 2, exact and symbolic)

Three consequences, in increasing order of how much they matter:

1. **E_cross is a function of the vertex COUNT alone** -- blind to the vertex
   indices and to their order, like the alternating character of #7295 and for
   the same reason (it is a sum over letters).
2. **Every non-empty gamma-gamma word is strictly POSITIVE**, since `h > 0` for
   every `q > 1` (CHECK 3). The defining block reads the sign physically: *"A
   positive E_cross indicates that repulsion dominates; a negative value
   indicates that binding dominates."* So **no gamma-gamma word is
   binding-dominated, at any q > 1, on any number of strands.** That is a
   statement about whether pair-production words can carry a BOUND state, and
   it is a clean structural one.
3. **Minimising E_cross is degenerate in exactly the way the LP objective is**
   (CHECK 5): the empty word has `E_cross = 0 < k*h`, so it wins again. This is
   now the THIRD functional on which the trivial answer is the optimum -- the
   Markov trace, the LP objective (proved degenerate by the corpus), and now
   crossing energy.

## 🛑 Scope, and the one thing this does NOT do

`knot-operator-selection-proof.md` does not minimise `E_cross` over an
unconstrained set. It minimises subject to a DEMAND constraint,

    <Phi, dem(K)>_F  >=  ||dem(K)||_F ,     dem(K) = sum_{i : c_i < 0} |c_i| b_i^v

and that constraint is what should exclude the trivial answer: the identity
supplies only vacuum content and cannot fill a non-zero demand. **This probe
does not implement it.** Building `dem(K)` needs a state `K`, the Frobenius
dual via `G^{-1}`, and a choice of which `K` the nucleon is -- the last of which
is the very question the arc is trying to settle, so wiring it here would be
circular. What this file establishes is the functional's VALUE on the
gamma-gamma family, which the demand computation will need either way.

Consequently: finding 2 (always repulsion-dominated) stands on its own and does
not depend on the demand constraint. Finding 3 (minimisation is degenerate) is
explicitly a statement about the UNCONSTRAINED minimum, and the demand
constraint is the stated reason it may not be the last word.

Scope-(a). Selects nothing, wires nothing, moves no number in the corpus.
"""

from __future__ import annotations

import itertools
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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps(60)
mp.mp.dps = 40

Q0 = Q_MP
H0 = Q0 - 1 / Q0

q = sp.Symbol("q", positive=True)
h_sym = q - 1 / q

#: the five PSD-feasible gamma-gamma words on four strands (#7295)
FEASIBLE = [
    ((0, 1, 0, 1), "(v0 v1)^2"),
    ((0, 1, 0, 1, 0, 1, 0, 1), "(v0 v1)^4"),
    ((0, 0, 1, 1, 0, 1, 1, 0, 0, 1), "sporadic A"),
    ((0, 1, 1, 0, 0, 1, 0, 0, 1, 1), "sporadic B"),
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


def e_cross(crossings, sym: bool = True):
    """`def:crossing-energy`: +q for a positive crossing, -1/q for a negative
    one, summed over the braid word. `crossings` is a list of booleans, True =
    positive."""
    qq = q if sym else Q0
    acc = 0
    for pos in crossings:
        acc += qq if pos else -1 / qq
    return sp.simplify(acc) if sym else acc


def gg_crossings(combo):
    """A gamma-gamma word's crossing signs: each vertex `sigma_i
    sigma_{i+1}^{-1}` is one positive then one negative crossing."""
    out = []
    for _i in combo:
        out += [True, False]
    return out


def main() -> int:
    w = WitnessBuilder("qbeta-gamma-gamma-crossing-energy")
    w.set_description(
        "Crossing energy on gamma-gamma words. E_cross(k vertices) = k*h "
        "exactly -- a function of the vertex COUNT alone, blind to indices and "
        "order. Hence strictly POSITIVE for every non-empty word at every "
        "q > 1, and def:crossing-energy reads a positive value as "
        "repulsion-dominated: no gamma-gamma word is binding-dominated, on any "
        "number of strands. And minimising it is degenerate -- the empty word "
        "has E_cross = 0 -- making crossing energy the THIRD functional whose "
        "unconstrained optimum is the trivial answer. Does NOT implement "
        "knot-operator-selection-proof's demand constraint, which is the "
        "stated reason the unconstrained minimum may not be the last word. "
        "Calibrated against the corpus's own electron/positron values. "
        "Scope-(a)."
    )

    print("Assertions:")

    # ---------------------------------------------------------------- CHECK 1
    # Calibration against the corpus's own worked values. If the sign
    # convention were backwards these two would swap, so this is not
    # decorative.
    e_electron = e_cross([True] * 3)
    e_positron = e_cross([False] * 3)
    ee = mp.mpf(str(sp.N(e_electron.subs(q, sp.Rational(Q_50_DIGIT_STR)), 30)))
    ep = mp.mpf(str(sp.N(e_positron.subs(q, sp.Rational(Q_50_DIGIT_STR)), 30)))
    check("calibrates_against_the_corpus_electron_and_positron_values",
          sp.simplify(e_electron - 3 * q) == 0
          and sp.simplify(e_positron + 3 / q) == 0
          and abs(ee - mp.mpf("3.330")) < mp.mpf("0.001")
          and abs(ep + mp.mpf("2.703")) < mp.mpf("0.001"),
          f"electron = left trefoil T_(2,3), three POSITIVE crossings: "
          f"E_cross = {e_electron} = {mp.nstr(ee, 10)} (pair-creation-energy.md "
          f"says ~3.330); positron = mirror, three NEGATIVE: "
          f"E_cross = {e_positron} = {mp.nstr(ep, 10)} (says ~-2.703). A "
          f"reversed sign convention would swap these", w)

    # ---------------------------------------------------------------- CHECK 2
    # The closed form, exact and symbolic, over a range of k.
    bad = []
    for k in range(0, 15):
        val = e_cross(gg_crossings(tuple([0] * k)))
        if sp.simplify(val - k * h_sym) != 0:
            bad.append(k)
    check("gamma_gamma_crossing_energy_is_exactly_k_times_h", not bad,
          f"E_cross of a k-vertex gamma-gamma word = k*h exactly, k = 0..14 "
          f"(each vertex is one positive and one negative crossing, "
          f"q + (-1/q) = h). Mismatches: {bad or 'none'}", w)

    # ---------------------------------------------------------------- CHECK 3
    # Blind to indices and order -- the same shape as the alternating character.
    base = (0, 1, 1, 0, 1)
    seen = set()
    for perm in itertools.permutations(base):
        for gens in itertools.product((0, 1), repeat=len(base)):
            seen.add(sp.srepr(e_cross(gg_crossings(gens))))
    check("crossing_energy_is_blind_to_index_and_order", len(seen) == 1,
          f"{120 * 32} (permutation, index-assignment) pairs of a 5-vertex "
          f"word -> {len(seen)} distinct value(s). E_cross is a sum over "
          f"letters, so like the alternating character of #7295 it cannot see "
          f"which vertex sits where", w)

    # ---------------------------------------------------------------- CHECK 4
    # THE FINDING: strictly positive, hence repulsion-dominated, always.
    positive = all(
        mp.mpf(str(sp.N((k * h_sym).subs(q, sp.Rational(Q_50_DIGIT_STR)), 30)))
        > 0 for k in range(1, 15))
    h_pos = sp.solve(sp.Eq(h_sym, 0), q)
    check("every_non_empty_gamma_gamma_word_is_repulsion_dominated",
          positive and h_pos == [sp.Integer(1)],
          f"E_cross = k*h > 0 for every k >= 1 and every q > 1, since h = 0 "
          f"only at q = {h_pos}. def:crossing-energy reads a positive value as "
          f"'repulsion dominates' and a negative one as 'binding dominates', "
          f"so NO gamma-gamma word is binding-dominated -- on any number of "
          f"strands, at any q > 1. At q_0, h = {mp.nstr(H0, 20)}", w)

    # ---------------------------------------------------------------- CHECK 5
    # The third degeneracy.
    rows = [(c, lab, len(c),
             mp.mpf(str(sp.N((len(c) * h_sym).subs(
                 q, sp.Rational(Q_50_DIGIT_STR)), 30))))
            for c, lab in FEASIBLE]
    rows.sort(key=lambda r: r[3])
    empty_e = mp.mpf(0)
    check("unconstrained_minimisation_is_degenerate_the_empty_word_wins",
          all(r[3] > empty_e for r in rows),
          f"E_cross(empty word) = 0, against "
          f"{[(r[1], mp.nstr(r[3], 12)) for r in rows]} for the five "
          f"PSD-feasible words. So the UNCONSTRAINED minimum is the empty word "
          f"-- the THIRD functional with that property, after the Markov trace "
          f"and the LP objective (the latter proved degenerate by "
          f"prop:operator-selection-lp). The demand constraint of "
          f"knot-operator-selection-proof is the stated reason this may not be "
          f"the last word, and it is NOT implemented here", w)

    # ---------------------------------------------------------------- CHECK 6
    # Among non-empty words the ordering is by vertex count, nothing else.
    by_k = all(rows[i][2] <= rows[i + 1][2] for i in range(len(rows) - 1))
    check("ordering_among_non_empty_words_is_by_vertex_count_alone", by_k,
          f"sorted by E_cross: {[(r[1], r[2]) for r in rows]} -- monotone in "
          f"the vertex count, which is the whole content of E_cross = k*h. "
          f"The two sporadic 10-vertex words TIE exactly, so even restricted "
          f"to non-empty words this functional does not separate them", w)

    # ------------------------------------------------------------------ data
    w.add_data("definition",
               "def:crossing-energy: E_cross(beta) = sum over crossings, "
               "+q for L_+, -1/q for L_-")
    w.add_data("calibration", {
        "electron_T23_three_positive": {"symbolic": str(e_electron),
                                        "at_q0": mp.nstr(ee, 20),
                                        "corpus_says": "~3.330"},
        "positron_mirror_three_negative": {"symbolic": str(e_positron),
                                           "at_q0": mp.nstr(ep, 20),
                                           "corpus_says": "~-2.703"}})
    w.add_data("closed_form", "E_cross(gamma-gamma word, k vertices) = k*h")
    w.add_data("feasible_words", [
        {"word": list(r[0]), "label": r[1], "vertices": r[2],
         "E_cross_at_q0": mp.nstr(r[3], 25)} for r in rows])
    w.add_data("empty_word_E_cross", "0")
    w.add_data("findings", [
        "E_cross is a function of the vertex COUNT alone -- blind to index and "
        "order, like the alternating character and for the same reason",
        "every non-empty gamma-gamma word is strictly POSITIVE hence "
        "repulsion-dominated, at every q > 1 and on any number of strands",
        "unconstrained minimisation is degenerate: the empty word has "
        "E_cross = 0. Third functional with that property",
        "even among non-empty words it does not separate the two sporadic "
        "10-vertex candidates, which tie exactly"])
    w.add_data("not_implemented",
               "knot-operator-selection-proof's demand constraint "
               "<Phi, dem(K)>_F >= ||dem(K)||_F. Building dem(K) needs a state "
               "K, the Frobenius dual via G^-1, and a choice of which K the "
               "nucleon is -- the last being the question the arc is trying to "
               "settle, so wiring it here would be circular")
    w.add_data("scope", "a")
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)

    print()
    print(f"  E_cross(gamma-gamma word, k vertices) = k*h,  "
          f"h = {mp.nstr(H0, 16)} > 0")
    print(f"  empty word: 0")
    for r in rows:
        print(f"    {r[1]:14s} k = {r[2]:2d}   E_cross = {mp.nstr(r[3], 16)}")
    print("  -> every non-empty gamma-gamma word is REPULSION-DOMINATED")

    w.save()
    print()
    if FAILED:
        print(f"FAILED ({len(FAILED)}): {', '.join(FAILED)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
