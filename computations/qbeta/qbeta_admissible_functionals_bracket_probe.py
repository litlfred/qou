#!/usr/bin/env python3
"""
qbeta_admissible_functionals_bracket_probe.py — qou-cds1 / qou-99qc: exactly two
functionals survive convention D, they BRACKET the Q-value, and the one that
matches it is the one that does not survive.

# Ref: computations/qbeta/qbeta_which_algebra_the_decay_channel_lives_in_probe.py
# Ref: folio/quantum-observable-universe/observations/algebraic-gns-embedding-proof.md
# Ref: .beans/qou-99qc--...md   (which functional is epsilon meant to be)

WHY THIS IS FORCED RATHER THAN SEARCHED. The corpus places the convention-D
theory in the Temperley-Lieb quotient, and a functional descends to a quotient
exactly when it annihilates the ideal. That leaves no freedom to explore:

  * MULTIPLICATIVE functionals into a commutative ring are precisely the
    1-dimensional representations, and H_3(q) has exactly two -- sigma -> q and
    sigma -> -1/q. The second IS the block convention D quotients away, so
    exactly ONE multiplicative functional survives: the augmentation sigma -> q.
    Uniqueness, not a choice.
  * The Markov trace at z_D survives by construction (y_(1,1,1) = 0).
  * The coordinate sum `net`, which the Q_beta ansatz actually evaluates, does
    NOT survive.

So the ansatz has exactly two admissible replacements for its epsilon, each
giving one determined number. Both are computed here. Nothing is tuned and no
combination is formed -- see the trap below.

WHAT COMES OUT, and it is adverse. Against Q_codata:

    coordinate sum   (INADMISSIBLE under D)      +0.17 %
    augmentation     (admissible, unique mult.)  +12 %
    Markov trace     (admissible)                -15 %

The functional that reproduces the measured Q-value is precisely the one the
canonical convention forbids, and the two that are permitted miss by more than
an order of magnitude in OPPOSITE directions. Reported plainly: this is evidence
against the ansatz as it stands, not a step towards repairing it.

THE TRAP, STATED SO NOBODY WALKS INTO IT. Because the two admissible values
bracket the target, some convex combination reproduces it exactly. That
combination is a ONE-PARAMETER FIT with a single anchor to fit to, and finding
it would be numerology, not a derivation. This probe computes the bracket and
deliberately does NOT compute the interpolating weight. Any future work here has
to DERIVE a weight from the representation, not read one off Q_codata.

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
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS, LEFT, L, R, ONE, basis_vec, vec, net, reg_char, length,
)

set_compute_dps(50)

Z = sp.Symbol("z")
Z_D = q**3 / (q**2 + 1)


def main() -> int:
    w = WitnessBuilder("qbeta-admissible-functionals-bracket", engine="sympy+mpmath")
    w.set_description(
        "Under convention D exactly two functionals descend to the "
        "Temperley-Lieb quotient — the augmentation (unique multiplicative one) "
        "and the Markov trace. They bracket Q_codata; the coordinate sum that "
        "matches it is inadmissible."
    )
    ok, notes = [], []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    # ---- the two 1-dim characters, and which one survives -------------------
    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI, DIMS = [chi3, chi21, chi111], [1, 2, 1]

    # both 1-dim characters really are algebra maps on the generators
    for nm, f in (("chi3", chi3), ("chi111", chi111)):
        check(f"{nm}_is_multiplicative_on_the_generators_CONTROL",
              all(sp.simplify(f(LEFT[a] * basis_vec(b))
                              - f(basis_vec(a)) * f(basis_vec(b))) == 0
                  for a in (1, 2) for b in (1, 2)))
    check("the_two_dim_character_is_NOT_multiplicative_CONTROL",
          any(sp.simplify(chi21(LEFT[a] * basis_vec(b))
                          - chi21(basis_vec(a)) * chi21(basis_vec(b))) != 0
              for a in (1, 2) for b in (1, 2)),
          "(so the multiplicative functionals are exactly the two 1-dim ones)")

    # the (1,1,1) ideal
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * basis_vec(i) - R[0] * basis_vec(i)),
                           sp.simplify(L[1] * basis_vec(i) - R[1] * basis_vec(i)))
          for i in range(N)]
    centre = sp.Matrix.hstack(*zc).nullspace()
    cf = sp.symbols("c0 c1 c2")
    gen = sum((cf[i] * centre[i] for i in range(3)), sp.zeros(N, 1))
    sol = sp.solve([sp.Eq(CHI[mu](gen), DIMS[mu] if mu == 2 else 0)
                    for mu in range(3)], cf, dict=True)[0]
    e111 = sp.simplify(sum((sol[cf[i]] * centre[i] for i in range(3)),
                           sp.zeros(N, 1)))
    Le = sum((e111[i] * LEFT[i] for i in range(N)), sp.zeros(N, N))
    J = [sp.simplify(Le * basis_vec(i)) for i in range(N)]

    check("the_augmentation_descends",
          all(sp.simplify(chi3(j)) == 0 for j in J))
    check("the_OTHER_one_dim_character_does_NOT_descend",
          any(sp.simplify(chi111(j)) != 0 for j in J),
          "(chi^(1,1,1) IS the block convention D quotients away)")
    check("so_EXACTLY_ONE_multiplicative_functional_survives_under_D", True,
          "(two 1-dim reps; one is the quotiented block; the augmentation is "
          "unique — a uniqueness statement, not a choice)")

    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]

    def tr_M(v, zval):
        return sp.simplify(sum(v[i] * TR[i] for i in range(N)).subs(Z, zval))

    check("the_markov_trace_at_z_D_descends",
          all(sp.simplify(tr_M(j, Z_D)) == 0 for j in J))
    check("the_coordinate_sum_does_NOT_descend",
          any(sp.simplify(net(j)) != 0 for j in J))

    # ---- the three numbers ---------------------------------------------------
    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)
    check("delta_reproduces_the_corpus_NF_vector",
          sp.simplify(delta - vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)).is_zero_matrix)

    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
    Qexp = mp.mpf(str(Q_NEUTRON_MEV))

    rows = []
    for label, val, admissible in (
        ("coordinate sum (epsNPq)", ev(sp.simplify(net(delta))), False),
        ("augmentation  (sigma->q)", ev(sp.simplify(chi3(delta))), True),
        ("Markov trace  (z_D)", ev(sp.simplify(tr_M(delta, Z_D))), True),
    ):
        Q = abs(val) * E0
        rows.append({"functional": label, "descends_under_D": admissible,
                     "value_on_delta": fmt(val), "Q_MeV": fmt(Q),
                     "err_pct": fmt((Q / Qexp - 1) * 100)})
        print(f"    {label:<26} {'ADMISSIBLE' if admissible else 'INADMISSIBLE':<13}"
              f" Q={fmt(Q)[:12]:>14}  err={fmt((Q / Qexp - 1) * 100)[:9]:>11} %")

    check("calibrates_the_coordinate_sum_against_the_committed_closed_form",
          abs(mp.mpf(rows[0]["Q_MeV"]) - mp.mpf("0.783645827374621")) < mp.mpf("1e-12"),
          "(harness reproduces the corpus's Q_A before anything else is trusted)")
    check("calibrates_the_trace_against_the_corpus_closed_form",
          abs(ev(sp.simplify(tr_M(delta, Z_D)))
              - ev(sp.simplify((h**2 / 2 - h * Z).subs(Z, Z_D)))) < mp.mpf("1e-45"),
          "(tr_M(Delta) = h^2/2 - h z, the corpus form, at z_D)")
    # A calibration I first wrote WRONG, kept because the mistake is the point.
    # I asserted this row should reproduce qbeta-d-frame-trace-baseline's
    # -15.451 %. It FAILED, at -43.157 %, and the failure is correct: that probe
    # evaluates tr_M on the EXHIBITED NUCLEON WORDS, this one on the NF VECTOR,
    # and qou-avt5 established those are different objects. Two numbers both
    # called "tr_M(Delta)" are not comparable, and I nearly quoted them as if
    # they were.
    check("the_NF_vector_and_the_exhibited_words_give_DIFFERENT_traces",
          abs(ev(sp.simplify(tr_M(delta, Z_D))) - mp.mpf("-0.15801600434149"))
          > mp.mpf("0.01"),
          f"(NF vector {fmt(ev(sp.simplify(tr_M(delta, Z_D))))[:14]} vs the "
          "words' -0.158016004341 from qbeta-d-frame-trace-baseline; "
          "qou-avt5's finding, and the reason this probe uses ONE object for "
          "all three functionals)")

    e_ina = abs(mp.mpf(rows[0]["err_pct"]))
    e_aug = mp.mpf(rows[1]["err_pct"])
    e_tr = mp.mpf(rows[2]["err_pct"])
    check("the_two_ADMISSIBLE_functionals_BRACKET_the_measured_Q_value",
          (e_aug > 0) and (e_tr < 0),
          f"(augmentation {fmt(e_aug)[:7]} %, trace {fmt(e_tr)[:8]} % — "
          "opposite signs)")
    check("the_INADMISSIBLE_one_is_the_one_that_matches",
          e_ina < abs(e_aug) / 10 and e_ina < abs(e_tr) / 10,
          f"({fmt(e_ina)[:8]} % against {fmt(abs(e_aug))[:7]} % and "
          f"{fmt(abs(e_tr))[:7]} % — more than an order of magnitude closer)")
    check("no_interpolating_weight_is_computed_here",
          True,
          "(the bracket means SOME convex combination hits Q_codata exactly; "
          "that is a one-parameter fit against a single anchor and is "
          "deliberately NOT computed — a weight must be DERIVED)")

    # ---- the admissible set is COMPLETE, not merely the two I thought of ----
    # The structural condition IS y_(1,1,1)(z) = 0. Solving it rather than
    # checking candidates: it is quadratic in z, so it has exactly two roots.
    yv = sp.symbols("yy0 yy1 yy2")
    solY = sp.solve([sp.Eq(sum(yv[k] * CHI[k](basis_vec(i)) for k in range(3)),
                           TR[i]) for i in (0, 1, 3)], yv, dict=True)[0]
    Y = [sp.simplify(sp.factor(solY[yv[k]])) for k in range(3)]
    roots = sp.solve(sp.Eq(sp.numer(sp.together(Y[2])), 0), Z)
    roots = [sp.simplify(r) for r in roots]
    check("the_two_row_condition_has_EXACTLY_two_roots_in_z", len(roots) == 2,
          f"(y_(1,1,1)(z) = 0 solved, not guessed: z = {roots})")
    check("one_root_is_z_D_and_the_other_is_z_equals_q",
          any(sp.simplify(r - Z_D) == 0 for r in roots)
          and any(sp.simplify(r - q) == 0 for r in roots),
          "(so the two-row forcing is NOT unique to z_D — z = q kills the "
          "(1,1,1) block too)")
    check("at_z_equals_q_the_markov_trace_IS_the_augmentation",
          all(sp.simplify(tr_M(basis_vec(i), q) - chi3(basis_vec(i))) == 0
              for i in range(N)),
          "(on ALL six basis elements, not just on Delta — so the second root "
          "reproduces the augmentation exactly and the admissible set is "
          "COMPLETE at two elements)")
    check("z_equals_one_is_NEITHER_root",
          sp.simplify(Y[2].subs(Z, 1)) != 0,
          "(y_(1,1,1)(1) != 0, so tr_M at the trivial loop value does NOT "
          "descend either — and epsNPq IS tr_M at z=1 on Delta)")

    for r in rows:
        w.add_data(r["functional"].split()[0] + "_" + r["functional"].split()[1], r)
    w.add_data("E0_MeV", fmt(E0))
    w.add_data("Q_codata_MeV", fmt(Qexp))
    w.add_data("markov_convention", "D canonical")
    w.add_data("assertion_notes", notes)

    verdict = (
        "The admissible set is COMPLETE and has exactly two elements. The "
        "structural condition is y_(1,1,1)(z) = 0; solved rather than sampled, "
        "it is quadratic with roots z = z_D and z = q — so the two-row forcing "
        "is NOT unique to z_D. At z = q the Markov trace IS the augmentation, "
        "on all six basis elements, so the two roots give exactly the two "
        "functionals available: "
        + fmt(e_tr)[:8] + " % and " + fmt(e_aug)[:7] + " %. They BRACKET "
        "Q_codata. Meanwhile epsNPq is tr_M at z = 1 on Delta, and z = 1 is "
        "NEITHER root — a loop value the corpus itself says is never attained "
        "on the substrate, and one that does not survive the convention-D "
        "quotient. So the +" + fmt(e_ina)[:6] + " % agreement is delivered "
        "entirely by an evaluation that is inadmissible on both counts, while "
        "the complete set of admissible ones misses by more than an order of "
        "magnitude in opposite directions. Evidence against the ansatz as it "
        "stands. The bracket means some convex combination hits the target; "
        "that is a one-parameter fit against a single anchor, is NOT computed "
        "here, and any weight must be DERIVED. Scope-(a); nothing wired."
        if all(ok) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
