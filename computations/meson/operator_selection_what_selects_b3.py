#!/usr/bin/env python3
"""What CAN select B_3? Not a linear objective — it is relative-interior.

Companion to `operator_selection_lp_objective_audit.py`, which showed the
operator-selection LP's objective is vacuous. The natural next question is
whether some OTHER objective would work. This answers it, and the answer is a
structural negative that applies to the LP form itself rather than to one
objective.

THE GEOMETRY. At NF(B_3) all six Frobenius positivity constraints are
STRICTLY slack (min slack 0.3425), and the boundedness constraints are slack by
any sane M. So with only `sum x = n_target` active, B_3 lies in the RELATIVE
INTERIOR of the feasible polyhedron inside that hyperplane.

A linear functional on a polyhedron attains its extrema on a FACE. If a
relative-interior point is a minimiser then the functional is constant on the
whole polyhedron -- i.e. the objective vector is parallel to the equality
normal, in which case every feasible point is equally optimal. Hence:

    NO linear objective selects B_3 as a unique minimiser.

That also refutes the `t.x = n_target` substitution floated as a hypothesis in
the sibling audit: swapping which hyperplane is the equality does not change the
Frobenius slacks, so B_3 stays relative-interior.

TWO NATURAL NON-LINEAR PRINCIPLES ALSO FAIL:
  * minimum norm  -> the uniform point (n/6).1, which is feasible and is not B_3;
  * maximum minimum-slack -> B_3 loses to that same uniform point, 0.6110
    against 0.3425, so B_3 is not the most robustly feasible point either.

AND `rem:b3-local-minimum`'S TWO CLAIMS ARE BOTH FALSE. It says B_3 is "a local
minimum at a vertex of the LP feasible polytope". Zero of six Frobenius
constraints are active, so it is not a vertex (a vertex in R^6 needs six active
constraints; B_3 has one, the equality). And an explicit feasible descent
direction is exhibited below: the component of -t orthogonal to 1, which keeps
`sum x` fixed, stays strictly feasible, and lowers tr_M from 0.9986 to 0.8642.

WHAT SURVIVES, AND IT IS NOT NOTHING. B_3 is STRICTLY feasible: it satisfies
every Frobenius positivity constraint with room to spare. That is a real
certificate. It says the LP's honest role here is VERIFICATION -- B_3 is
robustly compatible with the Frobenius structure -- and not SELECTION. Whatever
picks B_3 out is topological or physical, not an optimum of this program.

Emits no witness: a decision probe whose output is an argument. Arithmetic is
exact (sympy over Q(q), Rational at the pin); `float` only for display.

Bean qou-v7qj.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_REPO = Path(__file__).resolve().parents[2]
for _p in (_REPO / "computations", _REPO / "computations" / "meson",
           _REPO / "tools" / "qou-substrate" / "python"):
    sys.path.insert(0, str(_p))

from operator_selection_lattice_symbolic import (  # noqa: E402
    NF_BASIS, q, h, structure_constants, derive_trace, build_gram, _reduce_nf,
)


def rmul(y, gen, inv=False):
    """Right-multiply an NF vector by sigma_gen, or sigma_gen^-1 = sigma_gen - h."""
    terms: dict[tuple[int, ...], sp.Expr] = {}
    for i, b in enumerate(NF_BASIS):
        if y[i] == 0:
            continue
        terms[b + (gen,)] = terms.get(b + (gen,), 0) + y[i]
        if inv:
            terms[b] = terms.get(b, 0) - h * y[i]
    red = _reduce_nf(terms)
    return [sp.simplify(red.get(b, 0)) for b in NF_BASIS]


def main() -> int:
    from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

    C = structure_constants()
    t = derive_trace(C)
    G = build_gram(C, t)
    q0 = sp.Rational(Q_50_DIGIT_STR)
    Gn = G.subs(q, q0)
    tn = sp.Matrix([e.subs(q, q0) for e in t])

    y = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for _ in range(3):                       # B_3 = (sigma_0 sigma_1^-1)^3
        y = rmul(y, 0)
        y = rmul(y, 1, inv=True)
    B3 = sp.Matrix([e.subs(q, q0) for e in y])
    n_t = sum(B3)
    gx = [sp.N((Gn * B3)[i], 30) for i in range(6)]

    print("=" * 72)
    print("WHERE B_3 SITS")
    print("=" * 72)
    for i, g in enumerate(gx):
        state = "TIGHT" if abs(float(g)) < 1e-12 else "slack"
        print(f"   (Gx)_{i} = {float(g):+.9f}   {state}")
    active = sum(1 for g in gx if abs(float(g)) < 1e-12)
    print(f"\n   active Frobenius constraints : {active} of 6")
    print(f"   min slack                    : {float(min(gx)):+.9f}")
    print(f"   => B_3 is RELATIVE-INTERIOR in the hyperplane sum x = n_target")
    assert active == 0, "B_3 must be strictly feasible for this argument"

    print("\n" + "=" * 72)
    print("CONSEQUENCE: no linear objective can select it")
    print("=" * 72)
    print("   A linear functional attains its extrema on a FACE. A")
    print("   relative-interior minimiser forces the functional to be constant")
    print("   on the whole polyhedron, making every feasible point optimal too.")
    print("   This is about the LP FORM, not about one objective. It also")
    print("   refutes swapping 'sum x = n' for 't.x = n': that changes which")
    print("   hyperplane is the equality and leaves every Frobenius slack alone.")

    print("\n" + "=" * 72)
    print("TWO NON-LINEAR PRINCIPLES, BOTH FAIL")
    print("=" * 72)
    uni = sp.Matrix([n_t / 6] * 6)
    g_uni = [sp.N((Gn * uni)[i], 30) for i in range(6)]
    print(f"   min-norm on the hyperplane = (n/6).1, feasible: {min(g_uni) >= 0}")
    print(f"     equals B_3? {uni == B3}")
    print(f"   max-min-slack: uniform point scores {float(min(g_uni)):+.6f}")
    print(f"                  B_3 scores           {float(min(gx)):+.6f}")
    print(f"     => B_3 is NOT the most robustly feasible point either")
    assert min(g_uni) > min(gx), "the uniform point should beat B_3 on min slack"

    print("\n" + "=" * 72)
    print("rem:b3-local-minimum — BOTH CLAIMS FALSE")
    print("=" * 72)
    print(f"   'at a vertex'      : {active + 1} active constraints, a vertex needs 6")
    one = sp.Matrix([1] * 6)
    d = -(tn - (tn.dot(one) / 6) * one)      # -t projected onto {sum d = 0}
    deriv = tn.dot(d)
    print(f"   'a local minimum'  : exhibit a feasible descent direction")
    print(f"      sum d      = {float(sum(d)):+.1e}   (stays on the hyperplane)")
    print(f"      t.d        = {float(deriv):+.9f}   (< 0, so tr_M decreases)")
    step = sp.Rational(1, 2)
    xnew = B3 + step * d
    gnew = [sp.N((Gn * xnew)[i], 30) for i in range(6)]
    print(f"      at step {float(step)}: feasible {min(gnew) >= 0}, "
          f"min slack {float(min(gnew)):+.6f}")
    print(f"      tr_M(B_3) = {float(tn.dot(B3)):+.9f}")
    print(f"      tr_M(new) = {float(tn.dot(xnew)):+.9f}   STRICTLY LOWER")
    assert deriv < 0 and min(gnew) >= 0 and tn.dot(xnew) < tn.dot(B3)

    print("\n" + "=" * 72)
    print("WHAT SURVIVES")
    print("=" * 72)
    print("   B_3 satisfies every Frobenius positivity constraint STRICTLY,")
    print(f"   with min slack {float(min(gx)):.6f}. That is a genuine certificate:")
    print("   B_3 is robustly compatible with the Frobenius structure, not")
    print("   marginally so. The LP's defensible role is VERIFICATION, not")
    print("   SELECTION — whatever picks B_3 out is topological or physical,")
    print("   not an optimum of this program.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
