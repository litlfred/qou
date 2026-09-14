#!/usr/bin/env python3
"""qou-99qc / qou-pzsi: IMPLEMENT the discretised `E_cat` double integral as a
separation-weighted pair kernel over the word, and measure whether it separates
the four gluon candidates that every letter-sum provably ties.

# Ref: content/quantum-observable-universe/lean/QOU/MobiusEnergy.lean  (prop:mobius-energy)
# Ref: content/quantum-observable-universe/lean/QOU/QBeta/ECatBlockDecomposition.lean
# Ref: content/quantum-observable-universe/lean/QOU/QBeta/LetterSumBlindness.lean
# Ref: content/quantum-observable-universe/lean/QOU/Mass/GammaGammaWordSelection.lean  (the cost socket)
# Ref: computations/confinement_lp_braid_gram_probe.py  ("change the objective, not the Gram")
# Ref: computations/qbeta/qbeta_embedding_energy_can_discriminate_probe.py

WHERE THIS SITS. `QOU/Mass/GammaGammaWordSelection.lean` defines the selection
principle with `cost : W -> R` as a FREE PARAMETER, and every instantiation in
the corpus fills it with `fun w => (w.length : R)` -- the crossing count. That
is the letter-sum class `LetterSumBlindness.lean` excludes scope-(b): a sum
over letters is permutation-invariant, the closure is not, so the crossing
count cannot separate `sigma_1 sigma_0` from `sigma_0 sigma_1`. Independently,
`confinement_lp_braid_gram_probe.py` shows the LP's Hecke objective is
degenerate (`t_j = G_{0j}` makes `t.x = u_0` constant on the feasible set) and
concludes in its own words that "a surviving formulation has to break (a):
change the OBJECTIVE, not the Gram". This probe computes a candidate objective.

THE DISCRETISATION, and every step is read off the spec rather than chosen.
`prop:mobius-energy` gives

    E_cat(g) = lambda . tr_A  int int  (D(g(s)) (x) D(g(t))) *_q ||dg/ds ^_q dg/dt|| ds dt

On the closed braid the curve is the closure, so `s, t` run over the word's
positions and the diagonal is excluded exactly as in the continuum:

    D(g(s)) (x) D(g(t))   ->   the letter pair (w_i, w_j)
    lambda . tr_A          ->   tr_M(w_i w_j)  -- the Frobenius form composed
                                with the algebra trace IS the Markov trace, and
                                this is the corpus's own Gram entry G_ij
    *_q ||...|| ds dt      ->   the separation weight 1 / d_arc(i,j)^2

    E_pair(w) = sum_{i<j} tr_M(w_i w_j) / d_arc(i,j)^2

with `d_arc(i,j) = min(j-i, L-(j-i))` the CYCLIC separation, because the
closure of a braid is a circle -- the same `min(u, L-u)` the flat-torus bridge
uses. No constant is fitted and no branch is chosen: the only inputs are the
spec's three factors.

WHY THE SEPARATION WEIGHT IS THE WHOLE POINT. Permuting the letters does not
change the multiset, but it DOES change which pairs sit at which separation.
`ECatBlockDecomposition.pairSum_not_perm_invariant` proves that a
separation-dependent pair kernel escapes the permutation-invariance exclusion,
and that a kernel ignoring `d` and symmetric in its two letters would be
permutation-invariant again and buy nothing. Check [A3] measures exactly that
contrast on the live candidates: the `d`-weighted sum against the same sum with
the weight removed.

WHAT IS NOT CLAIMED, and the list is longer than the list of what is.

  * This is NOT `E_cat`. `E_cat` is a continuum double integral over
    `S^1 x S^1` and has no producer in the corpus; `energy : R` in
    `CategoricalMobiusEnergy` is a bare structure field. This is a
    DISCRETISATION whose factors are read off the spec, and whether its
    continuum limit is `E_cat` is unproved.
  * NOTHING here selects a word. A cost that separates candidates is a
    precondition for selection, not a selection: minimising it would be a
    choice this probe does not make, and choosing it BECAUSE it lands a target
    would be selection against the target under the anti-fit directive.
  * The per-block split `t_lambda` is PROVED to be a refinement
    (`ECatBlockDecomposition.blockDecomposition_of_linear`, from linearity
    alone) but is NOT computed here -- that needs `chi_lambda` of each letter
    pair, which is a separate wiring step. The totals below are
    `sum_lambda t_lambda`, per `total_eq_sum_blockCosts`.
  * The classical-limit leg of `MobiusEnergy.lean` is assumed, not proved, and
    its own header records an incident where it made `E_cat` blind
    (`E_cat = 1 + const` for every knot) with no `sorry`. Unretired; bean
    `qou-pzsi`.

NO SELECTION BY ACCURACY. No Q_beta, no CODATA, no residual, no experimental
number appears anywhere in this probe.
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

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402

mp = _order.mp
set_compute_dps(60)
mp.mp.dps = 60

Q0, H0, ZD = _order.Q0, _order.H0, _order.ZD

Z, HALF, NEG1 = mp.mpf(0), mp.mpf(-1) / 2, mp.mpf(-1)

#: the 6-letter gamma-gamma core (sigma_0 sigma_1^-1)^3.
CORE = [(0, Z), (1, NEG1)] * 3
#: the 3-letter quark block's shifts, by flavour.
QSHIFT = {"p": [Z, HALF, HALF], "n": [HALF, HALF, NEG1]}
GENS = (0, 0, 1)

#: the four two-crossing gluon dressings every letter-sum ties at 2q.
TWO_CROSSING = {
    "sigma_1 sigma_0": [(1, Z), (0, Z)],
    "sigma_0 sigma_1": [(0, Z), (1, Z)],
    "sigma_1 sigma_1": [(1, Z), (1, Z)],
    "sigma_0 sigma_0 (LIVE)": [(0, Z), (0, Z)],
}

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def tr(letters):
    """Markov trace at the convention-D admissible root z_D = q^3/(q^2+1).

    This is `lambda . tr_A` of the spec: the Frobenius form composed with the
    algebra trace. Carried as mpf end to end.
    """
    return _order.tr_at(_order.word_nf(letters), ZD)


def base(nuc: str):
    return CORE + [(g, s) for g, s in zip(GENS, QSHIFT[nuc])]


def cyclic_sep(i: int, j: int, L: int) -> int:
    """Arc separation on the CLOSED braid: the closure is a circle, so the two
    ways round compete, exactly as `min(u, L-u)` in the flat-torus bridge."""
    d = abs(j - i)
    return min(d, L - d)


def pair_energy(word, weighted: bool = True):
    """The discretised E_cat: sum over ordered pairs of `tr_M(w_i w_j)`,
    weighted by `1/d_arc^2`.

    `weighted=False` removes the separation factor, leaving a kernel that is
    symmetric in the two letters and blind to where they sit -- the control
    that shows the weight is what does the work (check [A3]).
    """
    L = len(word)
    total = mp.mpf(0)
    for i in range(L):
        for j in range(i + 1, L):
            g = tr([word[i], word[j]])
            if weighted:
                d = cyclic_sep(i, j, L)
                total += g / mp.mpf(d) ** 2
            else:
                total += g
    return total


def main() -> int:
    w = WitnessBuilder("qbeta-ecat-pair-kernel")
    w.set_description(
        "Implements the discretised E_cat double integral as a "
        "separation-weighted pair kernel over the braid word -- each factor "
        "read off prop:mobius-energy rather than chosen: the letter pair for "
        "D(g(s)) (x) D(g(t)), the Markov trace tr_M(w_i w_j) for lambda . "
        "tr_A, and 1/d_arc^2 for the measure factor, with d_arc the CYCLIC "
        "separation since a braid closure is a circle. Measures whether this "
        "cost separates the four two-crossing gluon candidates that every "
        "letter-sum provably ties, and contrasts it against the same sum with "
        "the separation weight removed -- the control for "
        "ECatBlockDecomposition.pairSum_not_perm_invariant. It is NOT E_cat "
        "(that is a continuum integral with no producer), it selects no word, "
        "and the per-block split is proved a refinement in Lean but not "
        "computed here."
    )

    print("qou-99qc / qou-pzsi -- discretised E_cat as a pair kernel")
    print(f"  q0 = {mp.nstr(Q0, 20)}   z_D = {mp.nstr(ZD, 20)}")
    print()

    # -- A1: the letter-sum tie, restated so the contrast is on one page -----
    print("== 1. every letter-sum ties these four (the thing being escaped) ==")
    writhes = {}
    for name, g in TWO_CROSSING.items():
        wr = sum(1 if d == Z else -1 for _, d in g)
        writhes[name] = wr
        print(f"    {name:<24} writhe = {wr:+d}   length = {len(g)}")
    print()
    check(
        "all_four_candidates_are_tied_by_every_letter_sum",
        len(set(writhes.values())) == 1
        and len({len(g) for g in TWO_CROSSING.values()}) == 1,
        "all four have writhe +2 and length 2, so the crossing COUNT (the "
        "corpus's live cost in GammaGammaWordSelection) and the crossing "
        "ENERGY E_cross (a sum over letters) take one value across all four. "
        "LetterSumBlindness.letterSum_perm_invariant makes this structural "
        "rather than coincidental: no letter-sum, for any q and any "
        "coefficients, can do better",
        w,
    )

    # -- A2: the pair kernel ------------------------------------------------
    print("== 2. the discretised E_cat pair kernel, per candidate ==")
    print(f"    {'gluon':<24} {'E_pair(proton)':<26} {'E_pair(neutron)'}")
    energies = {}
    for name, g in TWO_CROSSING.items():
        ep = pair_energy(base("p") + g)
        en = pair_energy(base("n") + g)
        energies[name] = (ep, en)
        print(f"    {name:<24} {mp.nstr(ep, 18):<26} {mp.nstr(en, 18)}")
    print()

    vals_p = [energies[k][0] for k in TWO_CROSSING]
    distinct_p = len({mp.nstr(v, 24) for v in vals_p})
    check(
        "the_pair_kernel_separates_the_candidates_a_letter_sum_ties",
        distinct_p == len(TWO_CROSSING),
        f"{distinct_p} distinct proton values over {len(TWO_CROSSING)} "
        f"candidates, against ONE value for every letter-sum. So a "
        f"separation-weighted pair kernel is a cost that can distinguish what "
        f"the crossing count cannot -- which is the precondition the "
        f"GammaGammaWordSelection cost socket needs and the crossing count "
        f"fails. It does NOT follow that this cost should be adopted or "
        f"minimised; that is a choice this probe does not make",
        w,
    )

    # -- A3: the control — the separation weight is what does the work ------
    print("== 3. control: the same sum with the separation weight REMOVED ==")
    print(f"    {'gluon':<24} {'unweighted (proton)'}")
    unw = {}
    for name, g in TWO_CROSSING.items():
        u = pair_energy(base("p") + g, weighted=False)
        unw[name] = u
        print(f"    {name:<24} {mp.nstr(u, 18)}")
    print()
    sharp = ("sigma_1 sigma_0", "sigma_0 sigma_1")
    d_w = abs(energies[sharp[0]][0] - energies[sharp[1]][0])
    d_u = abs(unw[sharp[0]] - unw[sharp[1]])
    check(
        "the_separation_weight_is_what_breaks_the_tie_not_the_pairing",
        d_w > d_u,
        f"on the SHARP pair -- same letter multiset, same writhe, differing "
        f"only in ORDER -- the weighted kernel separates by "
        f"{mp.nstr(d_w, 8)} against {mp.nstr(d_u, 8)} unweighted. This is the "
        f"measured form of ECatBlockDecomposition.pairSum_not_perm_invariant: "
        f"pairing alone is not enough, because a kernel symmetric in its two "
        f"letters and blind to their separation is permutation-invariant "
        f"again. The 1/d_arc^2 factor of the O'Hara integrand is doing the "
        f"work, and it is the factor the spec supplies rather than one chosen "
        f"here",
        w,
    )

    # -- A4: the honest boundary -------------------------------------------
    check(
        "this_is_a_discretisation_and_not_E_cat",
        True,
        "E_cat is a continuum double integral over S^1 x S^1 and has no "
        "producer in the corpus -- `energy : R` in CategoricalMobiusEnergy is "
        "a bare structure field. What is computed here is a discretisation "
        "whose three factors are read off prop:mobius-energy; whether its "
        "continuum limit is E_cat is UNPROVED, and the classical-limit leg it "
        "would need is assumed rather than derived and carries an unretired "
        "blindness incident (E_cat = 1 + const for every knot, no sorry). "
        "Recorded as an assertion so the boundary travels with the numbers",
        w,
    )

    w.add_data("pair_energies", {
        k: {"proton": mp.nstr(v[0], 30), "neutron": mp.nstr(v[1], 30)}
        for k, v in energies.items()
    })
    w.add_data("unweighted_control_proton",
               {k: mp.nstr(v, 30) for k, v in unw.items()})
    w.add_data("kernel", {
        "form": "E_pair(w) = sum_{i<j} tr_M(w_i w_j) / d_arc(i,j)^2",
        "d_arc": "min(j-i, L-(j-i)) -- cyclic, because a braid closure is a circle",
        "markov_parameter": "z_D = q^3/(q^2+1) (convention D)",
        "provenance": "each factor read off prop:mobius-energy; no fitted "
                      "constant, no chosen branch",
    })
    w.add_data("socket", {
        "target": "QOU/Mass/GammaGammaWordSelection.SDPSelected, field "
                  "`cost : W -> R`",
        "currently": "fun w => (w.length : R) -- the crossing count, a "
                     "letter-sum, excluded scope-(b)",
        "status": "this probe supplies a cost that SEPARATES; it does not "
                  "instantiate the selection, and adopting it is an owner "
                  "decision (bean qou-99qc)",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited -- one discretisation, four candidates, "
                 "one nucleus pair",
        "not_claimed": [
            "that this is E_cat, or that its continuum limit is",
            "that any word should be selected by minimising it",
            "that the per-block split t_lambda is computed -- it is PROVED a "
            "refinement in Lean (blockDecomposition_of_linear, from linearity "
            "alone) and left uncomputed here",
            "that the MobiusEnergy classical-limit leg is sound -- it is "
            "assumed and carries an unretired blindness incident",
        ],
        "no_selection_by_accuracy": "no Q_beta, no CODATA, no residual, no "
                                    "experimental number in this probe",
    })
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)

    ok = not FAILED
    w.save()
    print()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
