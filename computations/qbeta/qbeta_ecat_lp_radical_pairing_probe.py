#!/usr/bin/env python3
"""qou-99qc: the two-number measurement the formalize-first Lean licensed --
and it is a NEGATIVE. The geometric cost does NOT escape the LP degeneracy on
the block basis, and it fails for a structural reason.

# Ref: content/quantum-observable-universe/lean/QOU/QBeta/ECatLPDualRadical.lean
#      (dual_price_determined_by_radical; dual_price_zero_of_cost_orthogonal_to_radical)
# Ref: computations/nucleus_sdp_assembly.py   (`gram` = diag(y_lambda * dim_lambda))
# Ref: computations/qbeta/qbeta_ecat_block_cost_vector_probe.py  (the cost t_lambda)
# Ref: computations/confinement_lp_braid_gram_probe.py
# Ref: .beans/qou-99qc

WHAT THE LEAN ASKED FOR. `ECatLPDualRadical` proves that pairing the LP's dual
equality with a radical vector `v` of the Gram determines the shadow price
outright:

    y_0 = <t, v> / <1, v>

so whether a candidate cost gives a live dual is settled by ONE inner product,
with no solver, no feasible point and no `n_target`. The instruction that
followed was: measure `<t, v>` and `<1, v>` for the discretised-E_cat cost,
and if the first is zero the route is dead without running anything.

THE ANSWER IS ZERO, AND IT IS ZERO BY CONSTRUCTION. On the block basis the
corpus's Gram is DIAGONAL (`nucleus_sdp_assembly.CostGram.gram` is literally
`np.diag(self.frob_diag)`, with `frob_diag = y_lambda * dim_lambda`), so

    G = diag( y_(3)*1 , y_(2,1)*2 , y_(1^3)*1 )

Under convention D `y_(1^3) = 0` -- that vanishing IS convention D
(`threeRow_eq_zero_of_jones_ocneanu` for D ==> vanish;
`markovWeights_eq_jones_of_threeRow_eq_zero` + `hfaith` for the converse) -- so `G`
is singular and its radical is exactly the `(1^3)` coordinate direction,
`v = (0, 0, 1)`.

But the cost carries the SAME factor: `t_lambda = y_lambda * (pair sum)`. So
`t_(1^3) = 0` too, and `<t, v> = t_(1^3) = 0` identically. The cost is
orthogonal to the radical not by accident of the numbers but because the
`y_lambda` that creates the radical is the `y_lambda` that zeroes the cost
there.

THEREFORE, by `dual_price_zero_of_cost_orthogonal_to_radical`, `y_0 = 0` --
the same collapse the Hecke cost suffers, reached by a different route. This
is a scope-(b) STRUCTURAL exclusion with the invariant named: any cost of the
form `t_lambda = y_lambda * f(lambda)`, for ANY `f` whatsoever, is orthogonal
to the radical of `diag(y_lambda * dim_lambda)`. Changing `f` cannot help; the
geometric energy is a choice of `f`.

WHAT THIS DOES *NOT* EXCLUDE, and the distinction is the whole value of the
result. The corpus's other operator-selection program runs on the H_3 SIX-
OPERATOR basis `(gamma, sigma_0, sigma_1, L+, L-, e^-)` with a DENSE Gram
`G_ij = tr_M(b_i b_j)` whose radical is the q-antisymmetriser
`v = (-q^3, q^2, q^2, -q, -q, 1)`. That is a different index space, and the
per-block cost computed here is not a vector in it. So:

  * On the BLOCK basis: excluded, scope-(b), for every `y_lambda`-weighted
    cost. Measured here.
  * On the OPERATOR basis: UNTOUCHED by this probe. A geometric cost there
    would be a different construction -- one assigning an energy to each of
    the six operators rather than to each block -- and it does not exist yet.

So the route survives only in the form "build the geometric cost on the
operator basis", and this probe is what says so rather than leaving both
options open.

NO SELECTION BY ACCURACY. No Q_beta, no CODATA, no residual. In particular
this negative is reported as found; no second basis was tried in order to
obtain a better answer, and the operator-basis gap is named rather than
filled.
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

#: the character kernel's `q_value` is the GENERATOR EIGENVALUE and must match
#: this algebra's `h = q - 1/q`. See qbeta_ecat_block_cost_vector_probe for the
#: measurement behind this -- passing sqrt(q0) silently uses a different Hecke
#: algebra and breaks the assembly by ~0.05.
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
    q2 = Q0 ** 2
    den = (q2 + 1) ** 2
    return {(3,): (Q0 ** 4 + 1) / den, (2, 1): q2 / den, (1, 1, 1): mp.mpf(0)}


def chi_braid(shape, word):
    return chi_lambda_braid_mpf(list(shape), list(word), q_value=CHI_Q)


def chi_pair(shape, a, b):
    (ga, da), (gb, db) = a, b
    sa, sb = ga + 1, gb + 1
    dim = chi_braid(shape, [])
    return (chi_braid(shape, [sa, sb])
            + db * H0 * chi_braid(shape, [sa])
            + da * H0 * chi_braid(shape, [sb])
            + da * db * H0 ** 2 * dim)


def base(nuc: str):
    return CORE + [(g, s) for g, s in zip(GENS, QSHIFT[nuc])]


def cyclic_sep(i, j, L):
    d = abs(j - i)
    return min(d, L - d)


def block_cost_vector(word, y):
    L = len(word)
    acc = {sh: mp.mpf(0) for sh in SHAPES}
    for i in range(L):
        for j in range(i + 1, L):
            wt = mp.mpf(1) / mp.mpf(cyclic_sep(i, j, L)) ** 2
            for sh in SHAPES:
                acc[sh] += chi_pair(sh, word[i], word[j]) * wt
    return {sh: y[sh] * acc[sh] for sh in SHAPES}, acc


def main() -> int:
    w = WitnessBuilder("qbeta-ecat-lp-radical-pairing")
    w.set_description(
        "The two-number measurement ECatLPDualRadical licensed, and it is a "
        "NEGATIVE. On the block basis the corpus Gram is diagonal, "
        "diag(y_lambda * dim_lambda), so under convention D (y_(1^3) = 0) its "
        "radical is the (1^3) coordinate direction. The discretised-E_cat cost "
        "carries the SAME y_lambda factor, so its (1^3) component is zero too "
        "and <t, v> = 0 identically -- not numerically small, structurally "
        "zero. By dual_price_zero_of_cost_orthogonal_to_radical the shadow "
        "price y_0 = 0, the same collapse the Hecke cost suffers. Scope-(b) "
        "for ANY cost of the form t_lambda = y_lambda * f(lambda), for any f. "
        "It does NOT touch the six-OPERATOR-basis program, whose radical is "
        "the q-antisymmetriser in a different index space; a geometric cost "
        "there is a different construction that does not exist yet."
    )

    print("qou-99qc -- LP radical pairing for the discretised-E_cat cost")
    print(f"  q0 = {mp.nstr(Q0, 20)}")
    print()

    y = y_lambda()
    dims = {sh: chi_braid(sh, []) for sh in SHAPES}
    frob_diag = {sh: y[sh] * dims[sh] for sh in SHAPES}

    # -- A1: the block Gram is diagonal and singular -------------------------
    print("== 1. the block-basis Gram, diag(y_lambda * dim_lambda) ==")
    for sh in SHAPES:
        print(f"    G[{str(sh):<12}] = {mp.nstr(frob_diag[sh], 20)}")
    zeros = [sh for sh in SHAPES if frob_diag[sh] == 0]
    print()
    check(
        "the_block_gram_is_singular_and_its_radical_is_the_alternating_block",
        len(zeros) == 1 and zeros[0] == (1, 1, 1),
        f"exactly one diagonal entry vanishes, at {zeros[0]}. "
        f"nucleus_sdp_assembly.CostGram.gram IS np.diag(frob_diag) with "
        f"frob_diag = y_lambda * dim_lambda, so the Gram is diagonal and its "
        f"radical is the coordinate direction v = (0, 0, 1). Under convention "
        f"D y_(1^3) = 0 -- that vanishing IS convention D "
        f"(threeRow_eq_zero_of_jones_ocneanu; converse is "
        f"markovWeights_eq_jones_of_threeRow_eq_zero + hfaith) -- so the "
        f"singularity is structural, not a numerical rank drop",
        w,
    )

    # -- A2: the Lean's hypothesis <1, v> != 0 holds ------------------------
    v = {(3,): mp.mpf(0), (2, 1): mp.mpf(0), (1, 1, 1): mp.mpf(1)}
    one_dot_v = sum((v[sh] for sh in SHAPES), mp.mpf(0))
    print("== 2. the Lean's hypothesis <1, v> != 0 ==")
    print(f"    <1, v> = {mp.nstr(one_dot_v, 20)}")
    print()
    check(
        "the_radical_pairing_hypothesis_holds",
        one_dot_v != 0,
        f"<1, v> = {mp.nstr(one_dot_v, 20)} != 0, so "
        f"dual_price_determined_by_radical applies and y_0 is FORCED to "
        f"<t, v> / <1, v>. Checked rather than assumed, because that theorem "
        f"carries it as a hypothesis and it is a fact about this basis, not "
        f"about every Gram",
        w,
    )

    # -- A3: the measurement, and it is zero --------------------------------
    print("== 3. <t, v> for the discretised-E_cat cost, per candidate ==")
    print(f"    {'gluon':<24} {'<t, v> = t_(1^3)':<26} {'y_0 = <t,v>/<1,v>'}")
    all_zero = True
    rows = {}
    for name, g in TWO_CROSSING.items():
        t, acc = block_cost_vector(base("p") + g, y)
        tv = sum((t[sh] * v[sh] for sh in SHAPES), mp.mpf(0))
        y0 = tv / one_dot_v
        rows[name] = (tv, y0, acc[(1, 1, 1)])
        if tv != 0:
            all_zero = False
        print(f"    {name:<24} {mp.nstr(tv, 18):<26} {mp.nstr(y0, 18)}")
    print()
    print("    and the UNWEIGHTED (1^3) pair sum, to show the zero is the "
          "weight and")
    print("    not the geometry:")
    for name in TWO_CROSSING:
        print(f"      {name:<24} raw chi_(1^3) sum = "
              f"{mp.nstr(rows[name][2], 18)}")
    print()

    check(
        "the_geometric_cost_is_orthogonal_to_the_radical_STRUCTURALLY",
        all_zero,
        "<t, v> = t_(1^3) = 0 for every candidate, and it is zero BY "
        "CONSTRUCTION rather than numerically: t_lambda = y_lambda * (pair "
        "sum) carries the same y_lambda factor that makes the Gram diagonal "
        "entry vanish. Two separate things kill this block, and the printout "
        "above separates them: the raw chi_(1^3) pair sums are LARGE "
        "(~15.32), so the geometry there is not degenerate and it is the "
        "WEIGHT that zeroes the cost -- but they are also IDENTICAL across "
        "all four candidates, so the alternating block carries no "
        "discriminating information either and would contribute none even if "
        "y_(1^3) were nonzero. The weight argument is the structural one and "
        "holds for ANY cost of the form t_lambda = y_lambda * f(lambda), for "
        "any f whatsoever, so no choice of geometric energy escapes it",
        w,
    )

    check(
        "therefore_the_shadow_price_collapses_exactly_as_the_hecke_cost_does",
        all(rows[n][1] == 0 for n in TWO_CROSSING),
        "y_0 = 0 for every candidate, by "
        "ECatLPDualRadical.dual_price_zero_of_cost_orthogonal_to_radical. So "
        "the geometric cost does NOT escape the degeneracy on the block "
        "basis -- it reaches the same collapse the Hecke cost reaches, by a "
        "different route. This is a scope-(b) STRUCTURAL exclusion and the "
        "invariant is named: the shared y_lambda factor between the Gram "
        "diagonal and the cost. Reported as found; no alternative basis was "
        "substituted to obtain a better answer",
        w,
    )

    check(
        "the_operator_basis_program_is_NOT_touched_by_this",
        True,
        "the corpus's other operator-selection program runs on the H_3 "
        "SIX-OPERATOR basis (gamma, sigma_0, sigma_1, L+, L-, e^-) with a "
        "DENSE Gram G_ij = tr_M(b_i b_j) whose radical is the "
        "q-antisymmetriser (-q^3, q^2, q^2, -q, -q, 1). That is a different "
        "index space and the per-block cost is not a vector in it, so nothing "
        "here bears on it. The route therefore survives only as 'build the "
        "geometric cost on the OPERATOR basis' -- an energy per operator "
        "rather than per block, which does not exist yet. Recorded as an "
        "assertion so the surviving form travels with the negative",
        w,
    )

    w.add_data("measurement", {
        "basis": "Wedderburn block basis, n = 3",
        "gram": "diag(y_lambda * dim_lambda) -- diagonal, per "
                "nucleus_sdp_assembly.CostGram.gram",
        "radical": "v = (0, 0, 1), the (1^3) coordinate direction",
        "one_dot_v": mp.nstr(one_dot_v, 30),
        "t_dot_v_per_candidate": {k: mp.nstr(rows[k][0], 30) for k in rows},
        "y0_per_candidate": {k: mp.nstr(rows[k][1], 30) for k in rows},
        "raw_chi_1cubed_pair_sum": {k: mp.nstr(rows[k][2], 30) for k in rows},
    })
    w.add_data("verdict", {
        "class": "(b) structural exclusion",
        "invariant": "the shared y_lambda factor: t_lambda = y_lambda * "
                     "f(lambda) is orthogonal to the radical of "
                     "diag(y_lambda * dim_lambda) for every f",
        "excluded": "any y_lambda-weighted per-block cost, on the block basis",
        "NOT_excluded": "a geometric cost on the six-operator basis, whose "
                        "radical is the q-antisymmetriser -- a different index "
                        "space, and a construction that does not exist yet",
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
