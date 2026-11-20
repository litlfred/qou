#!/usr/bin/env python3
"""
weak_vertex_coupling_normalisation_probe.py — the decay-rate coupling s² IS the
q-dimension minus its classical value, and no constant rescales the
order-matched W-candidate onto it.

WHAT THIS SETTLES (bean qou-pfh7; owner: "coupling renorm", 2026-09-05).
qou-ix74 showed that substituting |W|² for s² in the beta-decay rate multiplies
every rate by 129.4 -- the figure read 1.19e4 until 2026-09-05, when the wrong
power was found (bean qou-xql6: S_SQ is already s^2 and was squared again; the
rate carries s^2 once, per prf:trace-ratio-observable) -- and left open what
normalisation relates the two.  The exclusion below is a statement about the
CANDIDATE FAMILY's functional form and does not depend on that magnitude.  Two
results here, one positive and one negative; neither fits a coefficient.

1. POSITIVE — s² is not an arbitrary amplitude.  Exactly, over any field:

       s^2 = (q^{1/2} - q^{-1/2})^2 = q - 2 + q^{-1} = [2]_q - [2]_1

   with [2]_q = q + q^{-1} the SU_q(2) fundamental dimension and [2]_1 = 2 its
   classical value.  So the coupling the rate uses is a CLASSICAL-VALUE
   DEVIATION, which is precisely why the rate vanishes at q = 1 and beta decay
   ceases classically.  That identity is the pattern any W-based replacement has
   to imitate, and it is what motivates the candidate family
   c * (W - W(1)) * (bridge), with W(1) = 1/4.
   Lean: QOU.Braiding.WeakVertexT35.sSq_eq_twoQ_sub_two (sorry-free).

2. NEGATIVE — the motivated family is excluded, and NOT merely by order.
   s² vanishes to SECOND order at q = 1 (s²(1) = 0, s²'(1) = 0, s²''(1) = 2)
   while W - W(1) vanishes to FIRST order (W'(1) = 5).  One bridge factor
   vanishing like (q-1) repairs the order, so order alone does not decide.
   What decides is that the resulting ratio RUNS:

       R(q) = (W(q) - 1/4) * hbar_q / s^2
            = (q+1)(4q^12 + 4q^10 + 8q^8 + 8q^6 + 8q^4 + 7q^2 + 1) / (4(q^2+1)^2)

       R -> 5 as q -> 1        R(q0) = 8.5242        R(3/2) = 65.269        R(2) = 695.91

   A normalisation CONSTANT cannot absorb a running ratio, so no c satisfies
   c*(W - 1/4)*hbar_q = s^2 identically: c would have to be 100/69591 at q = 2
   and 86528/5647625 at q = 3/2.  Lean: no_constant_rescaling,
   candidateRatio_two, candidateRatio_three_halves (all sorry-free, decided at
   two rational points).

   Every order-matched bridge in the corpus fails the same way, and for one
   reason: the leading coefficient of (W - 1/4)*X is W'(1) = 5 times X's own,
   never s²'s 1.  Measured below for X in {h, hbar_q, s, q-1, h/2}.

SCOPE.  This is a scope-(b) STRUCTURAL EXCLUSION of the parametrised family
c*(W - W(1))*X for X in that list — a proved non-constancy, not a bad number —
and it says NOTHING against W, whose closed form is unaffected (qou-egvf).  It
does not exclude a W-based coupling of some other shape: a ratio against
another trace, a Jones-normalised object (V_K(1) = 1 for every knot, so
V - 1 is the topologically canonical deviation), or a bar-parity component.
Those are untested here and are the live remainder on the bean.

Precision: sympy-exact throughout; numerics mpmath at 60 dps from exact
expressions; serialised at 50 digits.  No float is formed.

Output: computations/weak-vertex-coupling-normalisation.witness.json
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in ("computations", "computations/markov", "computations/hecke",
           "computations/substrate"):
    sys.path.insert(0, str(REPO / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
import hecke_symbolic as hs  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

q = hs.q
W = q ** 2 * (q ** 12 + q ** 8 - 1) / (q ** 2 + 1) ** 2
S_SQ = (q - 1) ** 2 / q
TWO_Q = q + 1 / q
H = q - 1 / q
HBAR = 1 - 1 / q
S = sp.sqrt(q) - 1 / sp.sqrt(q)
W_ONE = sp.Rational(1, 4)
BRIDGES = [("h", H), ("hbar_q", HBAR), ("s", S), ("q-1", q - 1), ("h/2", H / 2)]
R = sp.cancel(sp.simplify((W - W_ONE) * HBAR / S_SQ))


def leading(expr, order):
    """Coefficient of (q-1)^order in the expansion about q = 1."""
    return sp.nsimplify(sp.limit(sp.simplify(expr / (q - 1) ** order), q, 1))


def main() -> int:
    mp.mp.dps = 60
    q0 = Q_MP
    f = lambda e: sp.lambdify(q, e, "mpmath")(q0)  # noqa: E731
    n = lambda x, d=50: mp.nstr(x, d, strip_zeros=False)  # noqa: E731

    bridge_rows = []
    for name, X in BRIDGES:
        cand = (W - W_ONE) * X
        bridge_rows.append({
            "bridge": name,
            "candidate_at_q0": n(f(cand), 20),
            "ratio_to_s_sq_at_q0": n(f(cand / S_SQ), 20),
            "leading_coeff_order2": str(leading(cand, 2)),
        })

    ratio_pts = {str(pt): str(sp.nsimplify(R.subs(q, sp.Rational(pt))))
                 for pt in ("2", "3/2", "11/10")}
    c_two = sp.nsimplify(S_SQ.subs(q, 2) / ((W - W_ONE) * HBAR).subs(q, 2))
    c_three_halves = sp.nsimplify(
        S_SQ.subs(q, sp.Rational(3, 2)) / ((W - W_ONE) * HBAR).subs(q, sp.Rational(3, 2)))

    assertions = [
        {"name": "s_sq_equals_two_q_minus_classical_value",
         "passed": sp.simplify(S_SQ - (TWO_Q - 2)) == 0,
         "note": "s^2 = [2]_q - [2]_1 EXACTLY: the coupling is a classical-value deviation"},
        {"name": "W_at_one_is_one_quarter",
         "passed": sp.nsimplify(W.subs(q, 1)) == W_ONE,
         "note": "W(1) = 1/4, so W does not vanish classically and W - W(1) is the candidate"},
        {"name": "s_sq_vanishes_to_second_order",
         "passed": (S_SQ.subs(q, 1) == 0 and sp.diff(S_SQ, q).subs(q, 1) == 0
                    and sp.diff(S_SQ, q, 2).subs(q, 1) == 2),
         "note": "s^2(1) = 0, s^2'(1) = 0, s^2''(1) = 2"},
        {"name": "W_residual_vanishes_to_first_order",
         "passed": sp.simplify(sp.diff(W, q)).subs(q, 1) == 5,
         "note": "W'(1) = 5 != 0, so W - W(1) is first order — the order mismatch"},
        {"name": "every_order_matched_bridge_has_leading_coeff_five_times_bridge",
         "passed": all(leading((W - W_ONE) * X, 2) == 5 * leading(X, 1)
                       for _, X in BRIDGES),
         "note": "leading coeff of (W-1/4)*X is W'(1)*X'(1) = 5*X'(1), never s^2's 1"},
        {"name": "candidate_ratio_is_not_constant",
         "passed": sp.simplify(sp.diff(R, q)) != 0,
         "note": "R(q) runs: 5 as q->1, 8.524 at q0, 65.27 at 3/2, 695.91 at 2 — "
                 "no normalisation CONSTANT absorbs it (Lean no_constant_rescaling)"},
        {"name": "required_constant_differs_at_two_rational_points",
         "passed": c_two != c_three_halves,
         "note": f"c = {c_two} at q=2 vs {c_three_halves} at q=3/2"},
    ]

    witness = {
        "computation": "weak-vertex-coupling-normalisation",
        "description": (
            "The beta-decay coupling s^2 equals [2]_q - [2]_1 exactly, so it is the "
            "q-dimension minus its classical value; that pattern motivates the "
            "candidate family c*(W - W(1))*bridge for a W-based replacement. The "
            "family is EXCLUDED (scope-(b)): s^2 vanishes to second order at q=1 "
            "while W - W(1) vanishes to first, and once a bridge repairs the order "
            "the ratio still runs (5 -> 695.91 between q=1 and q=2), so no constant "
            "rescales one onto the other. Says nothing against W itself."
        ),
        "convention": {"markov_z": "q**3/(q**2+1) (D)", "hecke_h": "q - 1/q",
                       "anchor": "proton pin (Q_50_DIGIT_STR); identities exact in q"},
        "q0": Q_50_DIGIT_STR,
        "s_sq_identity": "(q**(1/2) - q**(-1/2))**2 == q + 1/q - 2 == [2]_q - [2]_1",
        "s_sq_at_q0": n(f(S_SQ)),
        "W_at_q0": n(f(W)), "W_at_one": "1/4",
        "W_residual_at_q0": n(f(W - W_ONE)),
        "vanishing_orders": {"s_sq": 2, "W_minus_W_one": 1,
                             "W_prime_at_one": "5", "s_sq_second_deriv_at_one": "2"},
        "order_matched_bridges": bridge_rows,
        "candidate_ratio": {
            "closed_form": str(sp.factor(R)),
            "limit_at_one": str(sp.limit(R, q, 1)),
            "at_q0": n(f(R), 20),
            "at_rational_points": ratio_pts,
            "required_constant_at_2": str(c_two),
            "required_constant_at_3_2": str(c_three_halves),
        },
        "scope": ("(b) structural exclusion of the family c*(W - W(1))*X for X in "
                  "{h, hbar_q, s, q-1, h/2}, by proved non-constancy of the ratio. "
                  "NOT an exclusion of a W-based coupling of another shape: a ratio "
                  "against another trace, a Jones-normalised object (V_K(1) = 1 for "
                  "every knot), or a bar-parity component are untested."),
        "lean": ["QOU.Braiding.WeakVertexT35.sSq_eq_twoQ_sub_two",
                 "QOU.Braiding.WeakVertexT35.hasDerivAt_sSq_one",
                 "QOU.Braiding.WeakVertexT35.hasDerivAt_weakVertexTrace_one",
                 "QOU.Braiding.WeakVertexT35.no_constant_rescaling",
                 "QOU.Braiding.WeakVertexT35.candidateRatio_two",
                 "QOU.Braiding.WeakVertexT35.candidateRatio_three_halves"],
        "reference_blocks": ["prop:hadron-half-life", "prf:hadron-half-life",
                            "rem:hadron-half-life-fermi"],
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from qou_substrate.witness import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy+mpmath")
    witness["scriptFile"] = str(pathlib.Path(__file__).resolve().relative_to(REPO / "computations"))
    out = REPO / "computations" / "weak-vertex-coupling-normalisation.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"  R(q) = {sp.factor(R)}")
    print(f"  R: 1->{sp.limit(R, q, 1)}  q0->{n(f(R), 12)}  3/2->{ratio_pts['3/2']}  2->{ratio_pts['2']}")
    for r in bridge_rows:
        print(f"  bridge {r['bridge']:6} ratio/s^2 {r['ratio_to_s_sq_at_q0'][:12]}  lead {r['leading_coeff_order2']}")
    print(f"  allPassed = {witness['allPassed']} -> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
