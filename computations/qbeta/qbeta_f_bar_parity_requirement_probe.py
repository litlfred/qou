#!/usr/bin/env python3
"""Is the Q_beta correction factor F REQUIRED to be bar-even?  No — and it
cannot be, because Q_A carries no bar parity to divide out.

WHAT WAS ASKED
--------------
Bean `qou-cds1` closes its 2026-08-18 follow-on with the one question it did
not settle, and names it the cheapest next step:

    "NOT SETTLED, and flagged rather than assumed: whether F is REQUIRED to
     be bar-even. ... If bar-evenness is not required this is a curiosity;
     if it is, the ladder violates it in BOTH conventions by a 15% term and
     the projection is incomplete rather than forced-and-final. Resolving
     that question looks like the cheapest next step, because it decides
     whether the u/2 term needs replacing before any new functional form is
     attempted."

`F = Q_beta^exp / Q_A(q)` is the multiplicative correction from the Form-A
closed form to the measured Q-value (`qbeta_utils.py:293`):

    Q_A = m_e * |q^2 - 2q - 1| * (q + 1) / (2 q^3)

`Q_beta^exp` is an experimental scalar, so it is bar-even trivially — bar
acts on `q`, not on measured data.  All of F's parity therefore comes from
`Q_A`.  This is a structural question with an exact symbolic answer and no
search, which is what the bean's Discipline section asks for.

RESULT — Q_A HAS NO BAR PARITY, AND NO NORMALISATION SUPPLIES ONE
-----------------------------------------------------------------
On the substrate domain `q^2 - 2q - 1 < 0` (true at q0 ~ 1.11 AND at its bar
image 1/q0 ~ 0.901, so the absolute value resolves consistently on both
sides and the unsigned rational function is the honest object):

    bar(Q_A)/Q_A  =  -q^3 (q^2 + 2q - 1) / (q^2 - 2q - 1)

  * = +1 (bar-even) only at q = 1, where bar is the identity anyway;
  * = -1 (bar-odd)  at NO positive real q.

Stronger, and this is what makes it structural rather than conventional:
stripping the `-q^3` leaves `(q^2+2q-1)/(q^2-2q-1)`, a ratio of two DISTINCT
irreducible quadratics (roots -1+sqrt2 and 1+sqrt2).  It is not a monomial,
so there is no integer `n` for which `q^n * Q_A` is bar-even or bar-odd.  The
failure is not a framing or normalisation choice that could be argued away.

Controls, to show the test can see parity when it is there:
`h = q - 1/q` returns exactly -1 (bar-odd) and `[2]_q = q + 1/q` exactly +1.

ANSWER TO THE BEAN, AND IT IS THE FIRST BRANCH OF ITS DICHOTOMY -- BUT FOR A
STRONGER REASON THAN "NOT REQUIRED"
---------------------------------------------------------------------------
Bar-evenness of F is not merely un-required: given this Q_A it is
UNSATISFIABLE.  `bar(F)/F = Q_A/bar(Q_A)`, the reciprocal of the ratio above,
so F inherits exactly the non-parity of Q_A.  No choice of correction factor
multiplying this Q_A can be bar-even.

CONSEQUENCE the bean asked this question in order to decide: the `u/2` term
does NOT need replacing on bar-parity grounds before a new functional form is
attempted.  The 15% shift from replacing `u/2` by its bar-odd part
`u(1-q^2)/4` remains a real measured quantity, but it is not the repair of a
violated requirement, because there is no requirement to violate.

SCOPE (a) -- on the requirement, not on the physics.  This shows the chain as
written imposes no bar-evenness on F.  It does NOT show that no
representation-theoretic argument could impose one; it shows that if such an
argument exists it is inconsistent with the Q_A closed form, so one of the
two would have to give.

A TENSION THIS SURFACES, recorded and NOT resolved here
------------------------------------------------------
`observations/three-calibration-discipline-proof.md:33-36` presents this same
closed form as

    "the bar-odd ($\\sinh$) partner of the bar-even ($\\cosh$) meson scale
     $m_\\pi$"

and `AGENTS.md:1937` echoes it.  The expression is provably not bar-odd (it
is -1 at no positive real q) and not bar-definite up to any q^n.

Two readings, and this probe does not choose between them:
  (i) the prose describes the CHANNEL Q_beta arises from (a sinh-type,
      bar-odd channel) rather than the parity of the final expression --
      in which case the wording should say so; or
  (ii) the closed form and the parity claim are inconsistent, and one is
      wrong.
Deciding that is an owner call about physics, not a symbolic computation, so
it is flagged rather than corrected.  It does not affect the answer above:
either way Q_A carries no parity, so F cannot be required to have one.

PRECISION.  Entirely symbolic (sympy exact rational functions).  No float
enters, so there is nothing for the float64 gates to act on.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate")]

q = sp.symbols("q", positive=True)
bar = lambda e: sp.simplify(e.subs(q, 1 / q))


def main() -> int:
    print("=" * 76)
    print(" Is F = Q_beta^exp / Q_A REQUIRED to be bar-even?  (bean qou-cds1)")
    print("=" * 76)

    # Q_A/m_e on the substrate domain, where q^2-2q-1 < 0 at q0 AND at 1/q0.
    QA = (1 + 2 * q - q**2) * (q + 1) / (2 * q**3)
    ratio = sp.cancel(sp.simplify(bar(QA) / QA))

    print("\n[1] the object")
    print(f"    Q_A/m_e            = {sp.factor(QA)}")
    print(f"    bar(Q_A)/Q_A       = {sp.factor(ratio)}")

    even = sp.simplify(ratio - 1) == 0
    odd = sp.simplify(ratio + 1) == 0
    print("\n[2] definite parity?  (needs the ratio identically +1 or -1)")
    print(f"    identically +1 (bar-even) : {even}")
    print(f"    identically -1 (bar-odd)  : {odd}")
    sol_e = [s for s in sp.solve(sp.Eq(ratio, 1), q) if s.is_real and s.is_positive]
    sol_o = [s for s in sp.solve(sp.Eq(ratio, -1), q) if s.is_real and s.is_positive]
    print(f"    ratio = +1 only at q = {sol_e or 'nowhere'}")
    print(f"    ratio = -1 only at q = {sol_o or 'nowhere'}")

    print("\n[3] stronger: bar-definite up to a power of q?")
    stripped = sp.cancel(ratio / (-(q**3)))
    num, den = sp.fraction(stripped)
    monomial = stripped.is_Pow or stripped.is_Symbol or stripped.is_number
    print(f"    ratio / (-q^3)     = {sp.factor(stripped)}")
    print(f"    numerator roots    = {sp.solve(num, q)}")
    print(f"    denominator roots  = {sp.solve(den, q)}")
    print(f"    is a monomial?     = {monomial}  -> no q^n normalisation helps")

    print("\n[4] controls -- the test can see parity when it is there")
    ctl = {}
    for nm, e in (("h = q - 1/q", q - 1 / q), ("[2]_q = q + 1/q", q + 1 / q)):
        v = sp.simplify(bar(e) / e)
        ctl[nm] = int(v)
        print(f"    {nm:20s} bar/self = {v}")

    print("\n[5] F inherits it")
    print("    Q_beta^exp is an experimental scalar => bar-even trivially,")
    print("    so bar(F)/F = Q_A/bar(Q_A), the reciprocal of [1].")
    print("    F is therefore NOT bar-even, and cannot be made so.")

    assertions = [
        {"name": "Q_A_is_not_bar_even",
         "passed": not even,
         "detail": "bar(Q_A)/Q_A is not identically +1; it equals +1 only at q=1, "
                   "where bar is the identity"},
        {"name": "Q_A_is_not_bar_odd",
         "passed": not odd and not sol_o,
         "detail": "bar(Q_A)/Q_A = -1 at no positive real q"},
        {"name": "no_power_of_q_restores_parity",
         "passed": not monomial,
         "detail": "after stripping -q^3 the residue is a ratio of two distinct "
                   "irreducible quadratics (roots -1+sqrt2, 1+sqrt2), not a monomial"},
        {"name": "controls_detect_known_parities",
         "passed": ctl["h = q - 1/q"] == -1 and ctl["[2]_q = q + 1/q"] == 1,
         "detail": "h -> -1 (bar-odd), [2]_q -> +1 (bar-even)"},
        {"name": "F_bar_evenness_is_unsatisfiable_not_merely_unrequired",
         "passed": not even and not odd,
         "detail": "F = Q_beta^exp/Q_A with Q_beta^exp bar-even trivially, so F's "
                   "parity is Q_A's; Q_A has none, so no F multiplying it is bar-even"},
    ]
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
        print(f"           {a['detail']}")
    ok = all(a["passed"] for a in assertions)
    print(f"\n  allPassed: {ok}  ({sum(a['passed'] for a in assertions)}/{len(assertions)})")

    out = HERE / "qbeta-f-bar-parity-requirement.witness.json"
    w = {
        "description": "Is the Q_beta correction factor F required to be bar-even? "
                       "No -- Q_A carries no bar parity to divide out, so bar-evenness "
                       "of F is unsatisfiable, not merely un-required. Answers the open "
                       "question at the end of bean qou-cds1.",
        "engine": "sympy (exact symbolic; no floating point)",
        "data": {
            "Q_A_over_me": sp.srepr(sp.factor(QA)),
            "Q_A_over_me_pretty": str(sp.factor(QA)),
            "bar_ratio": str(sp.factor(ratio)),
            "bar_ratio_equals_plus_one_at": [str(s) for s in sol_e],
            "bar_ratio_equals_minus_one_at": [str(s) for s in sol_o],
            "residue_after_stripping_minus_q_cubed": str(sp.factor(stripped)),
            "residue_is_monomial": bool(monomial),
            "controls": ctl,
            "domain_note": "q^2-2q-1 < 0 at q0~1.11 and at its bar image 1/q0~0.901, "
                           "so |.| resolves consistently on both sides",
            "scope": "(a) -- on the requirement as the chain states it, not a proof "
                     "that no representation-theoretic argument could impose one",
            "flagged_not_resolved": "three-calibration-discipline-proof.md:33-36 and "
                                    "AGENTS.md:1937 call this same closed form 'the "
                                    "bar-odd (sinh) partner'; it is not bar-odd. Either "
                                    "the prose means the channel rather than the "
                                    "expression, or the two are inconsistent -- an "
                                    "owner call, not a symbolic one.",
        },
        "assertions": assertions,
        "allPassed": ok,
    }
    out.write_text(json.dumps(w, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
