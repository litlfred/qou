#!/usr/bin/env python3
"""
qbeta_net_as_trace_plus_longest_probe.py — qou-cds1: `net` IS the Ocneanu trace
at z = 1, corrected on the longest element alone; and the whole z-free floor is
that correction, equal to -h * a_(2,1).

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: computations/qbeta/qbeta_phase_block_resolution_probe.py
# Ref: computations/qbeta/qbeta_alpha_commutator_floor_probe.py
# Ref: folio/quantum-observable-universe/nuclear-interactions/qbeta-counit-closed-form.md

WHAT THE CORPUS SAYS, AND WHAT IT LEAVES VAGUE. qbeta-counit-closed-form.md
states eps(Delta) = h^2/2 - h and tr_M(Delta) = h^2/2 - h*z, then: "The two agree
precisely when z = 1. The trivial-loop value is never attained on the substrate.
THE COUNIT AND THE MARKOV TRACE ARE GENUINELY DISTINCT FUNCTIONALS ON THE
SUBSTRATE." True, and left as a bare assertion of distinctness. This measures
exactly HOW they differ, and the answer is a single rank-one term.

    net  =  tr_M^{z=1}  -  h * (coefficient of the longest element)

🛑 SCOPE, added 2026-08-26 — an n = 3 FACT, not a characterisation of the two
functionals. At n = 4 it FAILS: `net - tr^{z=1}` is nonzero on 11 of 24 basis
elements with four distinct values, and the trace at z = 1 is not constant off
w_0 either (five values). See `qbeta_rank_one_identity_is_n3_only_probe.py`
(6/6). Every conclusion below stands — each is evaluated on Delta, and Delta
lives in H_3(q) — but the unscoped sentence did not, and PR #5337 had warned
about generalising an n = 3 coincidence ON THIS VERY BEAN before I did it.

verified on all six basis elements. The Ocneanu trace at z = 1 sends every basis
element to 1 EXCEPT the longest, where tr(T_0T_1T_0) = z(hz+1) evaluates to
1 + h; `net` sends every basis element to 1 by definition. So the two functionals
differ by exactly h on w_0 and nowhere else.

THREE CONSEQUENCES, all exact.

 1. Delta has zero coordinate on w_0, so eps(Delta) = tr_M^{z=1}(Delta) is not a
    coincidence of values but a consequence of Delta's SUPPORT. The corpus's
    "they agree precisely when z = 1" is therefore a statement about Delta, not
    about the functionals: on T_{w_0} they differ by h at every z, z = 1
    included.

 2. The ladder phase is a transport WITHIN one family, not between two unrelated
    functionals:  2*alpha(z) = tr_M^{1}(Delta) - tr_M^{z}(Delta).  The
    counit-minus-trace framing is correct but understates it — the endpoint is
    the same Ocneanu trace at the trivial loop value. That is what the ladder
    exponentiates.

 3. THE 2-DIMENSIONAL BLOCK CARRIES THE ENTIRE FLOOR. Since tr_M^{z=1} is a
    trace it annihilates [H,H], so the whole z-free floor is the rank-one term:
    net(dC) = -h * (dC)_{w_0}. And symbolically

        (dC)_{w_0}  =  a_(2,1)  =  q(q^2-1) / (q^4+q^2+1)        [exact]
        net(dC)     =  -h * a_(2,1)

    where a_(2,1) is the (2,1) coefficient of the trace agreeing with `net` on
    the centre. Read alongside the block resolution, which showed
    chi^(2,1)(Delta) = 0 identically: the 2-dimensional block contributes
    NOTHING to the trace-visible part of the phase and EVERYTHING to the
    trace-invisible part. Its contribution was not absent — it was in the
    sector no trace can see.

NO fit, NO c_k, NO wiring, no value proposed. Scope-(a).
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

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS, BASIS_NAMES, LEFT, L, R, ONE,
    basis_vec, vec, net, reg_char, length,
)

set_compute_dps(50)

Z = sp.Symbol("z")
W0 = 5  # index of e⁻ = σ₀σ₁σ₀, the longest element


def main() -> int:
    w = WitnessBuilder("qbeta-net-as-trace-plus-longest", engine="sympy+mpmath")
    w.set_description(
        "`net` equals the Ocneanu trace at z=1 corrected by -h on the longest "
        "element alone; Delta's support explains their agreement; and the "
        "z-free commutator floor is exactly -h*a_(2,1)."
    )
    ok, notes = [], []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]

    def tr_M(v, zval=None):
        e = sum(v[i] * TR[i] for i in range(N))
        return sp.simplify(e if zval is None else e.subs(Z, zval))

    # ---- 1. the exact difference of the two functionals ---------------------
    check("net_sends_every_basis_element_to_one",
          all(sp.simplify(net(basis_vec(i)) - 1) == 0 for i in range(N)))
    check("trM_at_z_one_is_one_except_on_the_longest_element",
          all(sp.simplify(tr_M(basis_vec(i), 1) - 1) == 0
              for i in range(N) if i != W0)
          and sp.simplify(tr_M(basis_vec(W0), 1) - (1 + h)) == 0,
          "(tr(T_0T_1T_0) = z(hz+1) -> 1+h at z=1)")

    def delta_w0(v):
        """The rank-one functional v -> coefficient of the longest element."""
        return sp.simplify(v[W0])

    check("net_equals_trM_at_z_one_minus_h_times_the_longest_coefficient",
          all(sp.simplify(net(basis_vec(i))
                          - (tr_M(basis_vec(i), 1) - h * delta_w0(basis_vec(i))))
              == 0 for i in range(N)),
          "(exact on all six basis elements, hence as functionals)")
    check("the_two_functionals_DO_differ_exhibited_on_the_longest_element",
          sp.simplify(net(basis_vec(W0)) - tr_M(basis_vec(W0), 1)) == -h,
          "(so 'they agree precisely when z=1' is about Delta, not the "
          "functionals — on T_{w_0} they differ by h at every z)")
    check("the_longest_coefficient_functional_is_NOT_a_trace",
          any(sp.simplify(delta_w0(LEFT[i] * basis_vec(j))
                          - delta_w0(LEFT[j] * basis_vec(i))) != 0
              for i in range(N) for j in range(N)),
          "(which is exactly why `net` fails cyclicity)")

    # ---- 2. Delta's support ---------------------------------------------------
    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)
    check("delta_reproduces_the_corpus_NF_vector",
          sp.simplify(delta - vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)).is_zero_matrix)
    check("delta_has_ZERO_coordinate_on_the_longest_element",
          sp.simplify(delta_w0(delta)) == 0,
          "(so eps(Delta) = tr_M^{z=1}(Delta) follows from SUPPORT, not "
          "from a numerical coincidence)")
    check("epsNPq_equals_the_trace_at_the_trivial_loop_value",
          sp.simplify(net(delta) - tr_M(delta, 1)) == 0
          and sp.simplify(net(delta) - (h**2 / 2 - h)) == 0)
    check("the_phase_is_a_transport_WITHIN_the_markov_family",
          sp.simplify(tr_M(delta, 1) - tr_M(delta) - h * (Z - 1)) == 0,
          "(2*alpha(z) = tr_M^1(Delta) - tr_M^z(Delta), symbolic in z)")

    # ---- 3. the floor is the rank-one term, and it is the (2,1) block --------
    comms = [LEFT[i] * basis_vec(j) - LEFT[j] * basis_vec(i)
             for i in range(N) for j in range(N)]
    comm_basis = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * basis_vec(i) - R[0] * basis_vec(i)),
                           sp.simplify(L[1] * basis_vec(i) - R[1] * basis_vec(i)))
          for i in range(N)]
    centre = sp.Matrix.hstack(*zc).nullspace()
    P = sp.Matrix.hstack(*(list(centre) + list(comm_basis)))
    coords = sp.simplify(P.solve(delta))
    dZ = sp.simplify(sum((coords[i] * centre[i] for i in range(3)), sp.zeros(N, 1)))
    dC = sp.simplify(delta - dZ)
    floor = sp.factor(sp.simplify(net(dC)))

    check("the_floor_is_MINUS_h_times_the_longest_coefficient_of_dC",
          sp.simplify(floor + h * delta_w0(dC)) == 0,
          "(tr_M^{z=1} kills [H,H], so the rank-one term is all that survives)")

    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [chi3, chi21, chi111]
    a = sp.symbols("a0 a1 a2")
    sol = sp.solve([sp.Eq(sum(a[k] * CHI[k](c) for k in range(3)), net(c))
                    for c in centre], a, dict=True)
    A = [sp.simplify(sp.factor(sol[0][a[k]])) for k in range(3)]

    check("the_longest_coefficient_of_dC_EQUALS_a_two_one",
          sp.simplify(delta_w0(dC) - A[1]) == 0,
          f"(both = {sp.factor(A[1])})")
    check("hence_the_floor_is_minus_h_times_a_two_one",
          sp.simplify(floor + h * A[1]) == 0)
    check("and_chi_two_one_of_delta_vanishes_CROSS_REFERENCE",
          sp.simplify(chi21(delta)) == 0,
          "(so the 2-dim block contributes NOTHING to the trace-visible part "
          "of the phase and EVERYTHING to the trace-invisible part)")

    # ---- 4. the a_lambda are DERIVED, not merely solved for -----------------
    # Everything else in the block-resolved identity is built from the Ocneanu
    # trace. The a_lambda were obtained by solving three linear equations, which
    # makes them determined but not explained. Since net = tr_M^{z=1} - h*d_w0,
    # and both sides restrict to the centre where every functional is a trace:
    #
    #     a_lambda  =  y_lambda(1)  -  h * b_lambda
    #
    # with y_lambda(1) the Markov weights at the trivial loop value and
    # b_lambda the chi-expansion of the longest-coefficient functional on the
    # centre. That closes the identity: every object in it now comes from the
    # Ocneanu trace plus one rank-one term.
    b = sp.symbols("b0 b1 b2")
    solB = sp.solve([sp.Eq(sum(b[k] * CHI[k](c) for k in range(3)), delta_w0(c))
                     for c in centre], b, dict=True)
    check("the_longest_coefficient_functional_has_a_chi_expansion_on_the_centre",
          len(solB) == 1)
    B = [sp.simplify(sp.factor(solB[0][b[k]])) for k in range(3)]

    yv = sp.symbols("yy0 yy1 yy2")
    solY = sp.solve([sp.Eq(sum(yv[k] * CHI[k](basis_vec(i)) for k in range(3)),
                           TR[i].subs(Z, 1)) for i in (0, 1, 3)], yv, dict=True)
    Y1 = [sp.simplify(sp.factor(solY[0][yv[k]])) for k in range(3)]
    check("markov_weights_at_the_trivial_loop_value_solve_uniquely",
          len(solY) == 1)
    check("a_lambda_EQUALS_y_lambda_at_one_minus_h_times_b_lambda",
          all(sp.simplify(A[k] - (Y1[k] - h * B[k])) == 0 for k in range(3)),
          "(so every object in the block-resolved identity is now built from "
          "the Ocneanu trace plus the single rank-one term)")
    check("b_two_one_is_what_makes_the_floor",
          sp.simplify(floor + h * (Y1[1] - h * B[1])) == 0,
          f"(floor = -h*(y_(2,1)(1) - h*b_(2,1)); b_(2,1) = {sp.factor(B[1])})")
    # b_(2,1) came out ZERO, which collapses the previous line to something
    # stated entirely inside the Ocneanu family, with no `net`-specific object
    # left in it at all.
    check("b_two_one_VANISHES",
          sp.simplify(B[1]) == 0,
          "(the longest-coefficient functional has no (2,1) component on the "
          "centre — so a_(2,1) is not merely equal to a Markov weight by "
          "arithmetic, it IS one)")
    check("a_two_one_IS_the_markov_weight_at_the_trivial_loop_value",
          sp.simplify(A[1] - Y1[1]) == 0)
    check("THE_FLOOR_IS_MINUS_h_TIMES_y_two_one_AT_z_EQUALS_ONE",
          sp.simplify(floor + h * Y1[1]) == 0,
          "(net(dC) = -h * y_(2,1)(1): the z-free part of the ladder phase, "
          "in the Ocneanu family alone)")

    # ---- numbers --------------------------------------------------------------
    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    w.add_data("floor_symbolic", str(floor))
    w.add_data("a_2_1_symbolic", str(A[1]))
    w.add_data("longest_coefficient_of_dC_symbolic", str(sp.factor(delta_w0(dC))))
    w.add_data("floor_at_q0", fmt(ev(floor)))
    w.add_data("a_2_1_at_q0", fmt(ev(A[1])))
    w.add_data("h_at_q0", fmt(ev(h)))
    w.add_data("minus_h_times_a_2_1_at_q0", fmt(-ev(h) * ev(A[1])))
    w.add_data("net_minus_trM_z1_on_the_longest_element", str(sp.simplify(-h)))
    for k, lbl in enumerate(["(3)", "(2,1)", "(1,1,1)"]):
        w.add_data(f"y_{lbl}_at_z_equals_one", str(Y1[k]))
        w.add_data(f"b_{lbl}_longest_functional_on_centre", str(B[k]))
    w.add_data("markov_convention",
               "convention-free — the results hold for every z, and the floor "
               "contains no Markov parameter at all")
    w.add_data("assertion_notes", notes)

    verdict = (
        "`net` = tr_M^{z=1} - h*(coefficient of the longest element), exactly, "
        "ON H_3(q) -- it FAILS at n = 4 (11 of 24; see "
        "qbeta_rank_one_identity_is_n3_only_probe), so it is an n=3 fact and "
        "not a characterisation of the functionals; the conclusions below are "
        "unaffected because each is evaluated on Delta in H_3(q). Measured "
        "on all six basis elements. That sharpens the corpus's 'genuinely "
        "distinct functionals' to a single rank-one difference supported on "
        "w_0, and turns its companion 'they agree precisely when z=1' into a "
        "statement about Delta's SUPPORT -- Delta has zero w_0 coordinate -- "
        "rather than about the functionals, which differ by h on T_{w_0} at "
        "EVERY z. Consequences: the ladder phase is a transport WITHIN one "
        "family, 2*alpha(z) = tr_M^1(Delta) - tr_M^z(Delta); and since "
        "tr_M^{z=1} annihilates [H,H], the whole z-free floor is the rank-one "
        "term. Chasing that through gives the closed form the identity was "
        "missing: b_(2,1) = 0, so a_(2,1) IS the Markov weight y_(2,1)(1), and "
        "    net(dC) = -h * y_(2,1)(1)  -- exact, and stated entirely inside "
        "the Ocneanu family with no `net`-specific object left in it. Read "
        "with chi^(2,1)(Delta) = 0 from the block resolution: the "
        "2-dimensional block contributes nothing to the trace-visible part of "
        "the phase and everything to the trace-invisible part. Its "
        "contribution was never absent -- it was in the sector no trace can "
        "see. Scope-(a): derives no correction, proposes no value, wires "
        "nothing."
        if all(ok) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
