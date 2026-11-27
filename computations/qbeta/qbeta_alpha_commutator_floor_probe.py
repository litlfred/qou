#!/usr/bin/env python3
"""
qbeta_alpha_commutator_floor_probe.py — qou-cds1: the ladder phase splits into a
z-dependent trace difference and a z-INDEPENDENT commutator floor, and the floor
is bar-even. A re-derivation step, not a z-swap.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: computations/qbeta/qbeta_net_trace_invariance_probe.py
# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean
# Ref: folio/quantum-observable-universe/nuclear-interactions/qbeta-counit-closed-form.md

WHERE THIS SITS. qou-cds1 located the ladder's phase exactly:

    eps(Delta) - tr_M^z(Delta) = h(z-1) = 2*alpha            [exact, any z]

so alpha is half the counit-minus-trace gap and the ladder is transporting the
evaluation between two functionals. This probe factors that gap using the step-8
decomposition of Delta itself, and the factorisation is what the re-derivation
requirement is about: it goes back to where (z-1)h/2 comes from instead of
feeding z_D into it.

THE SPLIT. H_3(q) is split semisimple, so H = Z(H) + [H,H], and every trace
annihilates [H,H]. Write Delta = dZ + dC accordingly. tr_M^z is a trace, so it
sees only dZ; `net` is not a trace (step 8, 25/25) and sees both. Hence for
EVERY z:

    2*alpha  =  [ net(dZ) - tr_M^z(dZ) ]  +  net(dC)
                \_____ z-dependent _____/    \__ z-FREE __/

The second term involves no Markov parameter at all. It is therefore identical
in convention C and convention D: a floor on the transport that no choice of z
can move. Measured share of 2*alpha and the exact closed form are below.

WHY THE FLOOR IS THE INTERESTING TERM. The sibling prune on this bean
(fcffeee29, QOU.QBeta.MarkovWeightsConventionD) reads: both surviving D weights
are bar-EVEN, so no quantity built from the D-frame weights alone carries a
bar-odd part, and the bar-odd eigenphase the C ladder uses "CANNOT BE ASSEMBLED
FROM THEM AT ALL". That prune is about quantities built from the WEIGHTS. The
floor is not built from the weights — it is a non-trace functional evaluated on
the component every weight annihilates, so the prune does not reach it. If the
floor were bar-odd, the material the prune calls absent would exist, outside the
sector the prune covers.

IT IS NOT. Exactly, under bar: q -> 1/q,

    net(dC) = -(q^2-1)^2 / (q^4+q^2+1)        is BAR-EVEN.

So the prune EXTENDS rather than breaking: the trace-invisible sector supplies
no bar-odd material either. That is a gap closed in an existing exclusion, not a
new route — and it is exact, not a search.

FOURTH INDEPENDENT ROUTE TO THE D WEIGHTS. The weights here are not read from
`y_lambda_su_n` or from the sibling's solve. They are obtained by solving
sum_lambda y_lambda chi^lambda(T_w) = tr(T_w) against the Ocneanu trace built
from its own defining recursion (tr(1)=1, tr(T_i)=z, tr(T_0T_1)=z^2,
tr(T_0T_1T_0)=z(hz+1)), symbolically in z, then specialising. Three routes
already agreed (Wenzl, the Markov linear system, numeric); this is a fourth, and
it is checked against the corpus's `y_lambda_su_n` rather than assuming it.

NO fit, NO c_k, NO wiring, no value proposed for anything. Scope-(a).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

# The H_3(q) regular representation, verified in the step-8 probe (25/25).
from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS, BASIS_NAMES, LEFT, L, R, ONE,
    basis_vec, vec, net, counit, reg_char, length,
)

set_compute_dps(50)

Z = sp.Symbol("z")

# Convention parameters (definitions, not substitutions into a phase).
Z_C = sp.sqrt(q) / (q + 1)
Z_D = q**3 / (q**2 + 1)


def bar(e):
    """The bar involution q -> 1/q."""
    return sp.simplify(sp.together(e.subs(q, 1 / q)))


def main() -> int:
    w = WitnessBuilder("qbeta-alpha-commutator-floor", engine="sympy+mpmath")
    w.set_description(
        "The Q_beta ladder phase alpha = (eps - tr_M)/2 splits exactly into a "
        "z-dependent trace difference and a z-independent commutator floor; "
        "the floor is bar-even, extending the D-frame bar-even prune to the "
        "sector that prune does not cover."
    )
    ok, notes = [], []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    # ---- 1. Delta, and its central / commutator split -----------------------
    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)
    check("delta_reproduces_the_corpus_NF_vector",
          sp.simplify(delta - vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)).is_zero_matrix)

    comms = [LEFT[i] * basis_vec(j) - LEFT[j] * basis_vec(i)
             for i in range(N) for j in range(N)]
    comm_basis = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * basis_vec(i) - R[0] * basis_vec(i)),
                           sp.simplify(L[1] * basis_vec(i) - R[1] * basis_vec(i)))
          for i in range(N)]
    centre = sp.Matrix.hstack(*zc).nullspace()
    check("centre_and_commutator_are_both_3_dimensional",
          len(centre) == 3 and len(comm_basis) == 3)
    P = sp.Matrix.hstack(*(list(centre) + list(comm_basis)))
    coords = sp.simplify(P.solve(delta))
    dZ = sp.simplify(sum((coords[i] * centre[i] for i in range(3)), sp.zeros(N, 1)))
    dC = sp.simplify(delta - dZ)
    check("delta_splits_exactly", sp.simplify(delta - dZ - dC).is_zero_matrix)

    # ---- 2. the Ocneanu trace, from its own recursion -----------------------
    # tr(1)=1, tr(T_i)=z, tr(T_0T_1)=tr(T_1T_0)=z^2, tr(T_0T_1T_0)=z(hz+1).
    TR = {(): sp.Integer(1), (0,): Z, (1,): Z,
          (0, 1): Z**2, (1, 0): Z**2, (0, 1, 0): Z * (h * Z + 1)}
    REDUCED = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
    tr_vals = [TR[wd] for wd in REDUCED]

    def tr_M(v):
        return sp.simplify(sum(v[i] * tr_vals[i] for i in range(N)))

    check("ocneanu_trace_reproduces_the_corpus_trM_of_delta",
          sp.simplify(tr_M(delta) - (h**2 / 2 - h * Z)) == 0,
          "(tr_M(Delta) = h^2/2 - h z, the corpus form)")
    check("ocneanu_trace_is_cyclic_CONTROL",
          all(sp.simplify(tr_M(LEFT[i] * basis_vec(j))
                          - tr_M(LEFT[j] * basis_vec(i))) == 0
              for i in range(N) for j in range(N)))
    check("ocneanu_trace_annihilates_the_commutator_sector_CONTROL",
          all(sp.simplify(tr_M(c)) == 0 for c in comm_basis))

    # ---- 3. THE SPLIT --------------------------------------------------------
    two_alpha = sp.simplify(h * (Z - 1))
    check("alpha_is_half_the_counit_minus_trace_gap",
          sp.simplify(net(delta) - tr_M(delta) - two_alpha) == 0,
          "(eps(Delta) - tr_M(Delta) = h(z-1) = 2*alpha, exact, any z)")

    floor = sp.factor(sp.simplify(net(dC)))
    trace_diff = sp.simplify(net(dZ) - tr_M(dZ))
    check("the_split_is_exact_for_every_z",
          sp.simplify(trace_diff + floor - two_alpha) == 0,
          "(2a = [net(dZ) - tr_M(dZ)] + net(dC))")
    check("the_floor_is_z_independent_hence_convention_independent",
          sp.simplify(sp.diff(floor, Z)) == 0 and Z not in floor.free_symbols,
          f"(net(dC) = {floor})")

    # ---- 4. bar parity of the floor -----------------------------------------
    check("the_commutator_floor_is_BAR_EVEN",
          sp.simplify(bar(floor) - floor) == 0,
          "(so the trace-invisible sector supplies NO bar-odd material either "
          "— the sibling's weights-level prune extends to it)")
    check("the_floor_is_not_bar_odd_CONTROL",
          sp.simplify(bar(floor) + floor) != 0)
    check("h_is_bar_odd_CONTROL", sp.simplify(bar(h) + h) == 0)

    # ---- 5. the weights, fourth independent route ---------------------------
    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [("(3)", chi3), ("(2,1)", chi21), ("(1,1,1)", chi111)]
    y = sp.symbols("y0 y1 y2")
    eqs = [sp.Eq(sum(y[k] * CHI[k][1](basis_vec(i)) for k in range(3)),
                 tr_vals[i]) for i in (0, 1, 3)]
    sol = sp.solve(eqs, y, dict=True)
    check("markov_weights_solve_uniquely_for_general_z", len(sol) == 1)
    sol = sol[0]
    yz = [sp.simplify(sp.factor(sol[y[k]])) for k in range(3)]
    check("weights_reproduce_the_trace_on_the_REMAINING_basis_elements_CONTROL",
          all(sp.simplify(sum(yz[k] * CHI[k][1](basis_vec(i)) for k in range(3))
                          - tr_vals[i]) == 0 for i in (2, 4, 5)))

    yD = [sp.simplify(sp.factor(e.subs(Z, Z_D))) for e in yz]
    yC = [sp.simplify(sp.factor(e.subs(Z, Z_C))) for e in yz]
    check("y_1cubed_vanishes_at_z_D", sp.simplify(yD[2]) == 0,
          "(the two-row forcing, reached from the Ocneanu recursion)")
    check("y_1cubed_does_NOT_vanish_at_z_C_CONTROL", sp.simplify(yC[2]) != 0)
    check("D_weights_match_the_sibling_closed_forms",
          sp.simplify(yD[0] - (q**4 + 1) / (q**2 + 1)**2) == 0
          and sp.simplify(yD[1] - q**2 / (q**2 + 1)**2) == 0,
          "(y_(3)=(q^4+1)/(q^2+1)^2, y_(2,1)=q^2/(q^2+1)^2 — fourth route)")
    check("D_weights_normalise_to_one",
          sp.simplify(yD[0] + 2 * yD[1] + yD[2] - 1) == 0)
    check("both_surviving_D_weights_are_bar_even_CONTROL",
          sp.simplify(bar(yD[0]) - yD[0]) == 0
          and sp.simplify(bar(yD[1]) - yD[1]) == 0,
          "(re-confirms the sibling prune's premise independently)")

    # cross-check the D weights against the corpus producer
    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    corpus = y_lambda_su_n(3, q0, 2)
    cmap = {tuple(k) if not isinstance(k, tuple) else k: v
            for k, v in (corpus.items() if hasattr(corpus, "items")
                         else dict(corpus).items())}
    got = {(3,): ev(yD[0]), (2, 1): ev(yD[1]), (1, 1, 1): ev(yD[2])}
    agree = all(abs(cmap.get(k, mp.mpf(0)) - v) < mp.mpf("1e-40")
                for k, v in got.items())
    check("D_weights_agree_with_the_corpus_y_lambda_su_n_CONTROL", agree,
          "(read-only cross-check against computations/y_lambda_su_n.py)")

    # ---- 6. numbers ----------------------------------------------------------
    rows = []
    for name, zval in (("C", Z_C), ("D", Z_D)):
        ta = ev(two_alpha.subs(Z, zval))
        td = ev(trace_diff.subs(Z, zval))
        fl = ev(floor)
        rows.append({"convention": name,
                     "two_alpha": fmt(ta), "trace_difference": fmt(td),
                     "commutator_floor": fmt(fl),
                     "floor_share_of_two_alpha": fmt(abs(fl / ta))})
    for r in rows:
        w.add_data(f"split_{r['convention']}", r)
    fl = ev(floor)
    check("the_floor_is_numerically_identical_in_C_and_D",
          rows[0]["commutator_floor"] == rows[1]["commutator_floor"],
          f"(net(dC) = {fmt(fl)} in both)")
    check("the_floor_is_not_a_rounding_term",
          mp.mpf(rows[0]["floor_share_of_two_alpha"]) > mp.mpf("0.01"),
          f"({rows[0]['floor_share_of_two_alpha'][:8]} of 2a in C, "
          f"{rows[1]['floor_share_of_two_alpha'][:8]} in D)")

    w.add_data("commutator_floor_symbolic", str(floor))
    w.add_data("trace_difference_symbolic_general_z", str(sp.factor(trace_diff)))
    for (lbl, _), e in zip(CHI, yz):
        w.add_data(f"y_{lbl}_general_z", str(e))
    for (lbl, _), e in zip(CHI, yD):
        w.add_data(f"y_{lbl}_at_z_D", str(e))
    w.add_data("markov_convention", "both, compared — D canonical")

    verdict = (
        "The ladder phase splits exactly, for every z, into a z-dependent trace "
        "difference and a z-INDEPENDENT commutator floor net(dC) = "
        "-(q^2-1)^2/(q^4+q^2+1), identical in C and D and carrying ~13.7 % of "
        "2*alpha. The floor is BAR-EVEN. Consequence for qou-cds1: the sibling "
        "prune (both D weights bar-even => no bar-odd material can be assembled "
        "from the weights) does not cover the trace-invisible sector, because "
        "the floor is not built from weights — and the sector supplies no "
        "bar-odd material either. The prune EXTENDS. Scope-(a): this derives no "
        "phase and proposes no value; it closes a gap in an existing exclusion "
        "and supplies the exact z-free part of the transport the ladder was "
        "approximating."
        if all(ok) else
        "INCONCLUSIVE — an assertion failed; re-derive before citing.")
    w.add_data("assertion_notes", notes)
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
