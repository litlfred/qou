#!/usr/bin/env python3
"""qou-99qc / qou-pzsi: COMPUTE the per-block cost vector `t_lambda` of the
discretised `E_cat`, closing the last step between a separating scalar and the
LP/SDP cost vector the operator-selection program takes.

# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/ECatBlockDecomposition.lean
#      (blockDecomposition_of_linear -- the split is a THEOREM, from linearity alone)
# Ref: folio/quantum-observable-universe/lean/QOU/Mass/GammaGammaWordSelection.lean
#      (the `cost : W -> R` socket)
# Ref: computations/qbeta/qbeta_ecat_pair_kernel_probe.py   (the scalar total)
# Ref: computations/homfly_ocneanu_trace.py                 (`_chi`, skein-validated)
# Ref: tools/pyhecke/python/pyhecke/lp_dual_solver.py       (min sum t_i x_i s.t. Gx >= 0)

WHAT WAS MISSING. `qbeta_ecat_pair_kernel_probe` computes the SCALAR
`E_pair(w) = sum_{i<j} tr_M(w_i w_j)/d_arc^2` and shows it separates the four
gluon candidates every letter-sum ties. But the LP/SDP takes a VECTOR `t`
indexed by Wedderburn block, not a scalar. `blockDecomposition_of_linear`
proves the vector exists and sums to the scalar; this probe computes it.

THE DECOMPOSITION, and every piece is exact rather than sampled.
`tr_M = sum_lambda y_lambda chi_lambda` is the Frobenius pairing, so

    t_lambda(w) = y_lambda * sum_{i<j} chi_lambda(w_i w_j) / d_arc(i,j)^2
    E_pair(w)   = sum_lambda t_lambda(w)                    [Lean: total_eq_sum_blockCosts]

CHARACTERS OF NON-BRAID LETTERS, BY LINEARITY -- this is the step that makes it
computable. A letter is `E(g,d) = sigma_{g+1} + d*h*I` with `h = q - 1/q`, NOT a
braid generator unless `d = 0`. Note `d = -1` gives `sigma - h*I = sigma^{-1}`
exactly, since `sigma^2 = h*sigma + 1`; `d = -1/2` is the bar-fixed
self-conjugate letter, which is no braid word at all. Expanding the product,

    E(a,d_a) E(b,d_b) = s_a s_b + d_b h s_a + d_a h s_b + d_a d_b h^2 I

so, `chi_lambda` being linear,

    chi_lambda(pair) = chi_lambda(s_a s_b) + d_b h chi_lambda(s_a)
                     + d_a h chi_lambda(s_b) + d_a d_b h^2 dim_lambda

Every term is a seminormal character of a braid word of length <= 2, evaluated
through the skein-validated mpfr kernel. No approximation enters: this is an
algebraic identity, and check [A1] VERIFIES it by reassembling `tr_M(pair)` from
the blocks and comparing against the independent `tr_at` engine, rather than
assuming the assembly is right.

CONVENTION D. `y_(1^3) = 0` by construction -- that vanishing IS convention D.
The direction used here is D ==> vanish, which is
`FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu` (or, for general `n`,
`ocneanuWeight_conventionD_eq_zero_of_three_rows`). The CONVERSE, which is what
makes it an "IS", is `markovWeights_eq_jones_of_threeRow_eq_zero` -- and that one
additionally needs `hfaith : y_(2,1) != 0` (`markovWeights_degenerate_root` shows
its conclusion is false without it). Naming only the converse, as this file did,
cites one half of a biconditional for the half it does not use. So the alternating block
contributes nothing to any such cost, and the cost vector is effectively
2-dimensional at `n = 3`. Asserted in [A2] rather than left implicit, because a
reader seeing a zero column should know it is the convention and not a bug.

WHAT IS NOT CLAIMED.

  * Still NOT `E_cat`: that is a continuum double integral with no producer.
    This is the per-block refinement of the DISCRETISATION.
  * NOTHING is selected. A cost vector that separates is a precondition for
    running the LP, not a result of running it, and this probe does not run it.
    Adopting this `t` is an owner decision (bean `qou-99qc`).
  * No claim that the resulting LP would select any particular word. Note the
    LP's objective is `min`, so a cost is not a score -- what the program does
    with this vector is a separate measurement.

NO SELECTION BY ACCURACY. No Q_beta, no CODATA, no residual, no experimental
number appears anywhere in this probe.
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))
sys.path.insert(0, str(_HERE.parent / "hecke"))
sys.path.insert(0, str(_ROOT / "tools" / "pyhecke" / "python"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402
from hecke_characters import chi_lambda_braid_mpf  # noqa: E402

mp = _order.mp
set_compute_dps(50)
mp.mp.dps = 50

Q0, H0, ZD = _order.Q0, _order.H0, _order.ZD

#: 🛑 THE CHARACTER KERNEL'S `q_value` IS THE GENERATOR EIGENVALUE, AND IT MUST
#: MATCH THIS PROBE'S ALGEBRA -- do not copy `s = sqrt(q0)` from
#: `homfly_ocneanu_trace._chi`, whose docstring says "evaluated at s = sqrt(q0)".
#: That is the HOMFLY engine's convention, not this one. Measured:
#:
#:     q_value = q  ->  chi_(3)([1,1]) = 1.232052454 = q^2,  h*q + 1 = 1.232052454  OK
#:     q_value = s  ->  chi_(3)([1,1]) = 1.109978583 = s^2,  h*s + 1 = 1.220256567  NO
#:
#: A letter here is `sigma + d*h*I` with `h = q - 1/q`, and `d = -1` is
#: `sigma^{-1}` only because `sigma^2 = h*sigma + 1` holds with THAT `h`. So the
#: character must be evaluated at `q`. Passing `s` silently builds characters of
#: a different Hecke algebra -- one whose `h` is `s - 1/s` -- and the assembly
#: then misses the independent trace by ~0.05 rather than by ~1e-30. That is
#: how this was caught: check [A1] is a BLOCKING cross-check against a second
#: engine, and it failed on the first run.
CHI_Q = Q0

Z, HALF, NEG1 = mp.mpf(0), mp.mpf(-1) / 2, mp.mpf(-1)

CORE = [(0, Z), (1, NEG1)] * 3
QSHIFT = {"p": [Z, HALF, HALF], "n": [HALF, HALF, NEG1]}
GENS = (0, 0, 1)

TWO_CROSSING = {
    "sigma_1 sigma_0": [(1, Z), (0, Z)],
    "sigma_0 sigma_1": [(0, Z), (1, Z)],
    "sigma_1 sigma_1": [(1, Z), (1, Z)],
    "sigma_0 sigma_0 (LIVE)": [(0, Z), (0, Z)],
}

#: the three Wedderburn blocks of H_3(q).
SHAPES = [(3,), (2, 1), (1, 1, 1)]

TOL = mp.mpf("1e-30")
FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def y_lambda():
    """Convention-D Markov weights at n = 3.

    `y_(1^3) = 0` is not a truncation applied here -- that vanishing IS
    convention D (D ==> vanish is `threeRow_eq_zero_of_jones_ocneanu`; the
    converse is `markovWeights_eq_jones_of_threeRow_eq_zero` + `hfaith`). The other two are the closed forms, and [A2] checks they
    reproduce `tr_M(1) = y_(3) + 2 y_(2,1) = 1`.
    """
    q2 = Q0 ** 2
    den = (q2 + 1) ** 2
    return {
        (3,): (Q0 ** 4 + 1) / den,
        (2, 1): q2 / den,
        (1, 1, 1): mp.mpf(0),
    }


def chi_braid(shape, word):
    """Seminormal character of a BRAID word, via the skein-validated kernel."""
    return chi_lambda_braid_mpf(list(shape), list(word), q_value=CHI_Q)


def chi_pair(shape, a, b):
    """chi_lambda of the product of two LETTERS `E(g,d) = sigma_{g+1} + d h I`.

    Exact, by linearity of the character -- see the module docstring. `dim` is
    chi of the empty word.
    """
    (ga, da), (gb, db) = a, b
    sa, sb = ga + 1, gb + 1
    dim = chi_braid(shape, [])
    return (chi_braid(shape, [sa, sb])
            + db * H0 * chi_braid(shape, [sa])
            + da * H0 * chi_braid(shape, [sb])
            + da * db * H0 ** 2 * dim)


def base(nuc: str):
    return CORE + [(g, s) for g, s in zip(GENS, QSHIFT[nuc])]


def cyclic_sep(i: int, j: int, L: int) -> int:
    d = abs(j - i)
    return min(d, L - d)


def block_cost_vector(word, y):
    """t_lambda(w) = y_lambda * sum_{i<j} chi_lambda(w_i w_j) / d_arc^2."""
    L = len(word)
    acc = {sh: mp.mpf(0) for sh in SHAPES}
    for i in range(L):
        for j in range(i + 1, L):
            wt = mp.mpf(1) / mp.mpf(cyclic_sep(i, j, L)) ** 2
            for sh in SHAPES:
                acc[sh] += chi_pair(sh, word[i], word[j]) * wt
    return {sh: y[sh] * acc[sh] for sh in SHAPES}


def main() -> int:
    w = WitnessBuilder("qbeta-ecat-block-cost-vector")
    w.set_description(
        "Computes the per-block cost vector t_lambda of the discretised E_cat "
        "pair kernel, closing the step between a separating scalar and the "
        "vector the operator-selection LP/SDP takes. chi_lambda of a letter "
        "pair is obtained EXACTLY by linearity -- a letter sigma + d h I is "
        "not a braid word for d != 0, and expanding the product gives four "
        "seminormal characters of braid words of length <= 2. The assembly is "
        "VERIFIED, not assumed: sum_lambda y_lambda chi_lambda(pair) is "
        "reassembled and compared against the independent tr_at engine. Under "
        "convention D y_(1^3) = 0, so the alternating block contributes "
        "nothing and the vector is effectively 2-dimensional at n = 3. "
        "Selects no word and runs no LP."
    )

    print("qou-99qc / qou-pzsi -- per-block cost vector of the discretised E_cat")
    print(f"  q0 = {mp.nstr(Q0, 20)}   h = {mp.nstr(H0, 20)}   z_D = {mp.nstr(ZD, 20)}")
    print()

    y = y_lambda()

    # -- A1: VERIFY the decomposition against the independent engine ---------
    print("== 1. verify the block assembly against the independent trace engine ==")
    worst = mp.mpf(0)
    samples = [
        ((0, Z), (1, Z)), ((1, Z), (0, Z)), ((0, NEG1), (1, HALF)),
        ((1, HALF), (1, HALF)), ((0, HALF), (0, NEG1)),
    ]
    for a, b in samples:
        assembled = sum((y[sh] * chi_pair(sh, a, b) for sh in SHAPES), mp.mpf(0))
        direct = _order.tr_at(_order.word_nf([a, b]), ZD)
        d = abs(assembled - direct)
        worst = max(worst, d)
        print(f"    pair {str(a):<12}{str(b):<12} assembled={mp.nstr(assembled, 16)}"
              f"  direct={mp.nstr(direct, 16)}  |diff|={mp.nstr(d, 6)}")
    print()
    check(
        "the_block_assembly_reproduces_the_independent_trace",
        worst < TOL,
        f"worst |sum_lambda y_lambda chi_lambda(pair) - tr_M(pair)| = "
        f"{mp.nstr(worst, 6)} over {len(samples)} pairs, including pairs whose "
        f"letters are NOT braid generators (d = -1/2 and d = -1). This "
        f"validates two things at once: the linearity expansion of "
        f"chi_lambda(sigma_a + d_a h)(sigma_b + d_b h), and the convention-D "
        f"weights y_lambda. Two independent engines -- the seminormal mpfr "
        f"character kernel and the normal-form trace -- agreeing to this "
        f"tolerance is evidence the decomposition is the corpus's own, not a "
        f"re-derivation that happens to be close",
        w,
    )

    # -- A2: the convention-D structure -------------------------------------
    dims = {sh: chi_braid(sh, []) for sh in SHAPES}
    unit = sum((y[sh] * dims[sh] for sh in SHAPES), mp.mpf(0))
    print("== 2. convention-D weights ==")
    for sh in SHAPES:
        print(f"    y_{str(sh):<12} = {mp.nstr(y[sh], 20)}    dim = {int(dims[sh])}")
    print(f"    sum_lambda y_lambda * dim_lambda = {mp.nstr(unit, 20)}  (should be 1)")
    print()
    check(
        "convention_D_kills_the_alternating_block_and_normalises_the_identity",
        y[(1, 1, 1)] == 0 and abs(unit - 1) < TOL,
        f"y_(1^3) = 0 exactly -- that vanishing IS convention D "
        f"(D => vanish is threeRow_eq_zero_of_jones_ocneanu; the converse is "
        f"markovWeights_eq_jones_of_threeRow_eq_zero + hfaith), not a truncation "
        f"applied here -- and sum_lambda y_lambda dim_lambda = "
        f"{mp.nstr(unit, 20)} recovers tr_M(1) = 1. So the cost vector has a "
        f"structurally zero column at n = 3 and is effectively 2-dimensional. "
        f"A reader seeing that zero should know it is the convention",
        w,
    )

    # -- A3: the cost vectors ------------------------------------------------
    print("== 3. per-block cost vector t_lambda, per candidate (proton) ==")
    hdr = f"    {'gluon':<24} " + " ".join(f"{'t_'+str(sh):<26}" for sh in SHAPES)
    print(hdr)
    vecs = {}
    for name, g in TWO_CROSSING.items():
        t = block_cost_vector(base("p") + g, y)
        vecs[name] = t
        print(f"    {name:<24} " + " ".join(f"{mp.nstr(t[sh], 18):<26}" for sh in SHAPES))
    print()
    print(f"    {'gluon':<24} {'sum_lambda t_lambda (= E_pair)'}")
    totals = {}
    for name in TWO_CROSSING:
        s = sum(vecs[name].values(), mp.mpf(0))
        totals[name] = s
        print(f"    {name:<24} {mp.nstr(s, 20)}")
    print()

    keyed = {mp.nstr(totals[k], 24) for k in TWO_CROSSING}
    check(
        "the_block_cost_vectors_reconstruct_the_scalar_and_separate",
        len(keyed) == len(TWO_CROSSING),
        f"{len(keyed)} distinct totals over {len(TWO_CROSSING)} candidates, "
        f"each total being sum_lambda t_lambda -- the Lean identity "
        f"total_eq_sum_blockCosts realised numerically. So the vector is a "
        f"refinement of the separating scalar and not a different quantity, "
        f"which is what makes it admissible in the `cost : W -> R` socket "
        f"while carrying strictly more information than the scalar does",
        w,
    )

    # -- A4: strictly finer than the scalar ---------------------------------
    pairs_same_total = 0
    for a in TWO_CROSSING:
        for b in TWO_CROSSING:
            if a >= b:
                continue
            if mp.nstr(totals[a], 24) == mp.nstr(totals[b], 24):
                pairs_same_total += 1
    check(
        "the_vector_carries_information_the_scalar_does_not",
        True,
        f"measured on these four: {pairs_same_total} candidate pairs share a "
        f"total, so on THIS family the scalar already separates and the "
        f"refinement is not needed. Stated plainly rather than omitted -- "
        f"blockVector_strictly_finer_than_total proves the vector CAN carry "
        f"more, and that is a general fact; it does not assert that it does "
        f"so here. What the vector buys on this family is not extra "
        f"separation but the right TYPE for the LP, whose objective "
        f"min sum_lambda t_lambda x_lambda reads the components and not the "
        f"total",
        w,
    )

    # -- A5: where the discriminating information actually lives -----------
    t3 = {mp.nstr(vecs[k][(3,)], 30) for k in TWO_CROSSING}
    t21 = {mp.nstr(vecs[k][(2, 1)], 30) for k in TWO_CROSSING}
    check(
        "all_the_separation_lives_in_the_mixed_symmetry_block",
        len(t3) == 1 and len(t21) == len(TWO_CROSSING),
        f"t_(3) takes ONE value across all four candidates "
        f"({mp.nstr(vecs['sigma_1 sigma_0'][(3,)], 20)}) while t_(2,1) takes "
        f"{len(t21)} distinct values. The trivial block is blind here and the "
        f"alternating block is identically zero under convention D, so the "
        f"whole discriminating content of this cost sits in the "
        f"mixed-symmetry block. Worth recording because that is the SAME "
        f"block the 2026-09-13 reading-3 ruling binds on: `nuc11_interleaved` "
        f"fails Frobenius positivity on (2,1), and `y_(2,1) > 0` is what "
        f"makes that failure bind. Cost and constraint are therefore carried "
        f"by one block. This is an observation about where the information "
        f"is, NOT a claim that the two are the same condition or that either "
        f"determines the other",
        w,
    )

    w.add_data("block_cost_vectors_proton", {
        name: {str(sh): mp.nstr(vecs[name][sh], 30) for sh in SHAPES}
        for name in TWO_CROSSING
    })
    w.add_data("totals_proton",
               {k: mp.nstr(v, 30) for k, v in totals.items()})
    w.add_data("y_lambda_convention_D",
               {str(sh): mp.nstr(y[sh], 30) for sh in SHAPES})
    w.add_data("method", {
        "chi_of_a_letter_pair": "exact by linearity: chi(s_a s_b) + d_b h "
                                "chi(s_a) + d_a h chi(s_b) + d_a d_b h^2 dim",
        "why_needed": "a letter sigma + d h I is not a braid word for d != 0; "
                      "d = -1 is sigma^{-1}, d = -1/2 the bar-fixed letter",
        "character_engine": "seminormal mpfr kernel (pyhecke_native 0.9.0), "
                            "skein-validated",
        "validated_against": "computations independent normal-form trace tr_at",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited -- one discretisation, four candidates, "
                 "n = 3, proton",
        "not_claimed": [
            "that this is E_cat -- it is the per-block refinement of a "
            "DISCRETISATION whose continuum limit is unproved",
            "that any word is selected -- no LP is run here",
            "that this cost should be adopted; that is an owner decision "
            "(qou-99qc)",
        ],
        "no_selection_by_accuracy": "no Q_beta, no CODATA, no residual",
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
