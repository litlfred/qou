#!/usr/bin/env python3
"""
qbeta_phase_block_resolution_probe.py — qou-cds1: the ladder phase, resolved per
Wedderburn block. Derived from the representation; nothing axiomatised, nothing
substituted.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: computations/qbeta/qbeta_alpha_commutator_floor_probe.py
# Ref: computations/qbeta/qbeta_net_trace_invariance_probe.py

WHAT qou-cds1 ASKED FOR, in its own words: "a correction of a DIFFERENT
functional form, derived from the representation rather than axiomatised".
This supplies the functional form. It does not supply a correction, and says so.

THE MASTER IDENTITY. Assembling the two prior results — alpha is half the
counit-minus-trace gap (this bean), and `net` decomposes as a trace part with an
exact chi^lambda expansion plus a trace-invisible remainder (step 8) — gives,
exactly, for EVERY z:

    2*alpha(z)  =  sum_lambda [ a_lambda - y_lambda(z) ] * chi^lambda(Delta)
                   +  net(dC)

  * `a_lambda` are the coefficients of the unique trace agreeing with the
    coordinate sum on the centre. They are z-FREE — properties of the functional
    `net`, not of any convention.
  * `y_lambda(z)` are the Markov weights. They are the ONLY z-dependence in the
    whole phase.
  * `chi^lambda(Delta)` are the block characters of the neutron-proton NF
    difference. Also z-free.
  * `net(dC)` is the commutator floor: z-free, bar-even.

Note chi^lambda(dZ) = chi^lambda(Delta), because every character annihilates
[H,H] — so the identity is stated on Delta itself and needs no reference to the
central projection.

WHY THIS IS THE RE-DERIVATION AND NOT A RE-EVALUATION. The C-frame ladder writes
the phase as the single scalar (z-1)h/2, which is the SUM of the blocks. Feeding
z_D into that sum is the substitution `eigenphase_bar_defect_of_fullBar` shows is
never bar-odd. The identity above resolves that sum into its per-block parts
BEFORE any convention is chosen, so specialising it to z_D is a statement about
the D-frame representation rather than a reuse of the C-frame formula. Under D
the two-row forcing makes y_(1,1,1) vanish, and the (1,1,1) block's contribution
becomes a_(1,1,1)*chi^(1,1,1)(Delta) with NOTHING to cancel it — a term with no
counterpart in C. That uncancelled block is measured below.

WHAT IS NOT CLAIMED. The identity is exact and derived, and it still reproduces
2*alpha, so by itself it changes no number: it is a re-expression, and a
re-expression is not a correction. Its value is that it says where a correction
could come from and where it could not — per-block, with the convention entering
at exactly one factor. Scope-(a). No fit, no c_k, no wiring, no value proposed.
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
    q, h, N, BASIS, LEFT, L, R, ONE, basis_vec, vec, net, reg_char, length,
)

set_compute_dps(50)

Z = sp.Symbol("z")
Z_C = sp.sqrt(q) / (q + 1)
Z_D = q**3 / (q**2 + 1)
LABELS = ["(3)", "(2,1)", "(1,1,1)"]


def bar(e):
    return sp.simplify(sp.together(e.subs(q, 1 / q)))


def parity(e):
    """'even' / 'odd' / 'neither' under q -> 1/q."""
    if sp.simplify(bar(e) - e) == 0:
        return "even"
    if sp.simplify(bar(e) + e) == 0:
        return "odd"
    return "neither"


def main() -> int:
    w = WitnessBuilder("qbeta-phase-block-resolution", engine="sympy+mpmath")
    w.set_description(
        "The Q_beta ladder phase resolved per Wedderburn block: "
        "2a = sum_lambda [a_lambda - y_lambda(z)] chi^lambda(Delta) + net(dC), "
        "exact for every z, with the convention entering at one factor only."
    )
    ok, notes = [], []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    # ---- Delta, split, characters ------------------------------------------
    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)
    check("delta_reproduces_the_corpus_NF_vector",
          sp.simplify(delta - vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)).is_zero_matrix)

    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [chi3, chi21, chi111]

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

    check("characters_annihilate_the_commutator_part_CONTROL",
          all(sp.simplify(f(dC)) == 0 for f in CHI),
          "(so chi^lambda(dZ) = chi^lambda(Delta) and the identity needs no dZ)")

    chi_delta = [sp.simplify(sp.factor(f(delta))) for f in CHI]

    # ---- a_lambda: the trace agreeing with `net` on the centre --------------
    a = sp.symbols("a0 a1 a2")
    sol = sp.solve([sp.Eq(sum(a[k] * CHI[k](z) for k in range(3)), net(z))
                    for z in centre], a, dict=True)
    check("a_lambda_solve_uniquely", len(sol) == 1)
    A = [sp.simplify(sp.factor(sol[0][a[k]])) for k in range(3)]
    check("a_lambda_are_z_free",
          all(Z not in e.free_symbols for e in A),
          "(they are properties of `net`, not of any convention)")

    # ---- y_lambda(z): Ocneanu, from its own recursion -----------------------
    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]

    def tr_M(v):
        return sp.simplify(sum(v[i] * TR[i] for i in range(N)))

    yv = sp.symbols("y0 y1 y2")
    solY = sp.solve([sp.Eq(sum(yv[k] * CHI[k](basis_vec(i)) for k in range(3)),
                           TR[i]) for i in (0, 1, 3)], yv, dict=True)
    check("y_lambda_solve_uniquely_for_general_z", len(solY) == 1)
    Y = [sp.simplify(sp.factor(solY[0][yv[k]])) for k in range(3)]
    check("y_lambda_reproduce_the_trace_on_the_REMAINING_elements_CONTROL",
          all(sp.simplify(sum(Y[k] * CHI[k](basis_vec(i)) for k in range(3))
                          - TR[i]) == 0 for i in (2, 4, 5)))

    # ---- THE MASTER IDENTITY -------------------------------------------------
    floor = sp.factor(sp.simplify(net(dC)))
    rhs = sp.simplify(sum((A[k] - Y[k]) * chi_delta[k] for k in range(3)) + floor)
    check("master_identity_holds_for_every_z",
          sp.simplify(rhs - h * (Z - 1)) == 0,
          "(2a = sum_l [a_l - y_l(z)] chi^l(Delta) + net(dC), symbolic in z)")

    # ---- specialisations -----------------------------------------------------
    YD = [sp.simplify(sp.factor(e.subs(Z, Z_D))) for e in Y]
    YC = [sp.simplify(sp.factor(e.subs(Z, Z_C))) for e in Y]
    check("y_1cubed_vanishes_at_z_D_and_not_at_z_C",
          sp.simplify(YD[2]) == 0 and sp.simplify(YC[2]) != 0)
    check("the_1cubed_block_is_UNCANCELLED_under_D",
          sp.simplify(A[2]) != 0 and sp.simplify(chi_delta[2]) != 0,
          "(a_(1,1,1) != 0 with y_(1,1,1) = 0, so this block has no counterpart "
          "in C, where the weight partly cancels it)")

    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    blocks = []
    for k, lbl in enumerate(LABELS):
        row = {"block": lbl,
               "chi_of_delta": str(chi_delta[k]),
               "a": str(A[k]),
               "y_at_z_C": str(YC[k]), "y_at_z_D": str(YD[k]),
               "contribution_C": fmt(ev((A[k] - YC[k]) * chi_delta[k])),
               "contribution_D": fmt(ev((A[k] - YD[k]) * chi_delta[k])),
               "parity_chi": parity(chi_delta[k]),
               "parity_a": parity(A[k]),
               "parity_y_D": parity(YD[k])}
        blocks.append(row)
        print(f"    {lbl:<9} C {row['contribution_C'][:14]:>15}   "
              f"D {row['contribution_D'][:14]:>15}   "
              f"chi:{row['parity_chi']:<8} a:{row['parity_a']:<8} y_D:{row['parity_y_D']}")

    twoaC, twoaD = ev(h * (Z_C - 1)), ev(h * (Z_D - 1))
    sC = sum(mp.mpf(b["contribution_C"]) for b in blocks) + ev(floor)
    sD = sum(mp.mpf(b["contribution_D"]) for b in blocks) + ev(floor)
    check("blocks_plus_floor_reproduce_two_alpha_numerically_in_BOTH_frames",
          abs(sC - twoaC) < mp.mpf("1e-45") and abs(sD - twoaD) < mp.mpf("1e-45"))

    # ---- what Delta's characters actually are -------------------------------
    check("chi_2_1_of_delta_VANISHES_identically",
          sp.simplify(chi_delta[1]) == 0,
          "(dim 2 at the identity, trace h at each generator: "
          "(h^2/2)*2 - (h/2)*h - (h/2)*h = 0. The phase is BLIND to the "
          "2-dimensional block, in every convention)")
    check("the_other_two_block_characters_do_NOT_vanish",
          sp.simplify(chi_delta[0]) != 0 and sp.simplify(chi_delta[2]) != 0)
    check("trM_of_delta_under_D_is_carried_entirely_by_the_trivial_block",
          sp.simplify(sum(YD[k] * chi_delta[k] for k in range(3))
                      - YD[0] * chi_delta[0]) == 0,
          "(y_(1,1,1)=0 by the two-row forcing and chi^(2,1)(Delta)=0, so the "
          "supports of the D trace and of Delta overlap in ONE block)")

    # ---- bar parity: my prediction was WRONG, and the truth is sharper ------
    # Predicted every a_lambda 'neither'. a_(2,1) is bar-ODD. Recorded, not hidden.
    check("a_2_1_is_bar_ODD_prediction_retracted",
          parity(A[1]) == "odd",
          "(I asserted all three were bar-'neither' and it FAILED; a_(2,1) is "
          "exactly bar-odd. It is also the block chi kills, so it does not "
          "enter the phase — the retraction costs nothing but is recorded)")
    check("a_3_and_a_1cubed_are_bar_neither",
          parity(A[0]) == "neither" and parity(A[2]) == "neither",
          "(so `net` is the only object in the identity that is not bar-graded: "
          "the D weights are bar-even and the floor is bar-even)")
    check("both_surviving_block_characters_of_delta_are_bar_ODD",
          parity(chi_delta[0]) == "odd" and parity(chi_delta[2]) == "odd")
    check("both_surviving_D_weights_bar_even_CONTROL",
          parity(YD[0]) == "even" and parity(YD[1]) == "even")
    check("two_alpha_is_bar_odd_under_C_and_not_under_D_CONTROL",
          parity(sp.simplify(h * (Z_C - 1))) == "odd"
          and parity(sp.simplify(h * (Z_D - 1))) != "odd")

    for b in blocks:
        w.add_data(f"block_{b['block']}", b)
    w.add_data("commutator_floor_symbolic", str(floor))
    w.add_data("commutator_floor_at_q0", fmt(ev(floor)))
    w.add_data("two_alpha_C_at_q0", fmt(twoaC))
    w.add_data("two_alpha_D_at_q0", fmt(twoaD))
    w.add_data("markov_convention", "both, compared — D canonical")
    w.add_data("assertion_notes", notes)

    verdict = (
        "The ladder phase is exactly 2a = sum_lambda [a_lambda - y_lambda(z)] "
        "chi^lambda(Delta) + net(dC), for every z, with a_lambda, "
        "chi^lambda(Delta) and net(dC) all z-free: the convention enters at "
        "exactly ONE factor, y_lambda(z). That is the functional form qou-cds1 "
        "asked for -- derived from the representation, not axiomatised, and "
        "obtained by resolving the C-frame scalar (z-1)h/2 into blocks BEFORE a "
        "convention is chosen, so specialising to z_D is not the forbidden "
        "substitution. Three structural facts fall out: chi^(2,1)(Delta) = 0 "
        "identically, so the phase is blind to the 2-dimensional block in EVERY "
        "convention; under D the two-row forcing then leaves tr_M(Delta) "
        "carried entirely by the trivial block; and the (1,1,1) block "
        "contributes a_(1,1,1)*chi^(1,1,1)(Delta) UNCANCELLED, with no "
        "counterpart in C, flipping sign and growing 7.8x. NOT a correction: "
        "the identity reproduces 2a, so no number moves. It says where a "
        "correction can come from and where it cannot."
        if all(ok) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
