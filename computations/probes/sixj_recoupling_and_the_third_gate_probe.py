#!/usr/bin/env python3
"""sixj_recoupling_and_the_third_gate_probe.py

The 6j route, and the third gate it exposed.

WHY 6j WAS THE RIGHT PLACE TO LOOK
----------------------------------
The b3 enumeration left four candidates outside its decision procedure, and the
6j symbol / monoidal associator was the most apt: it is defined on a TRIPLE with
no two-object analogue (so it passes the arity gate by construction), it is NOT
normalised (unlike Milnor mu-bar, which is +-1), and QOU is built on a rigid
monoidal category, so it is native rather than imported.

RESULT 1 -- A TRACE CANNOT SEE AN ASSOCIATOR
--------------------------------------------
By Mac Lane coherence every bracketing of a tensor product is CANONICALLY
isomorphic, and the isomorphism is unique. So any functional depending only on
the isomorphism class -- a trace, a dimension, a binding energy -- is
bracketing-independent. The 6j symbols are basis-dependent structure constants of
that canonical isomorphism, not an invariant a trace can detect.

So the associator itself cannot carry b3, for ANY such functional. What can, in
the categorical picture, is the MULTIPLICITY STRUCTURE: blocks present at n = 3
and absent at n = 2 -- concretely the 2-dimensional Specht module S^(2,1) of
H_3(q), which has no counterpart in H_2(q).

RESULT 2 -- TWO CANDIDATES PASS BOTH KNOWN GATES, THE FIRST ALL SESSION
-----------------------------------------------------------------------
Following the multiplicity reading to Hecke-natural quantities:

    quantity            D^3       D^4     b4/b3     gates
    dim H_n = n!        2.0       9.0     4.5       arity OK, SIGN OK
    [n]_q!              2.0879    9.7367  4.663     arity OK, SIGN OK
    [n]_q               0.011     0.00024 0.0217    arity OK, SIGN OK
    p(n)               -1.0       2.0    -2.0       wrong sign
    largest Specht dim  1.0      -2.0    -2.0       wrong sign

against a measured b4/b3 = +6.481. Three pass both gates.

RESULT 3 -- A THIRD GATE KILLS THEM, AND THE KILL IS STRUCTURAL
----------------------------------------------------------------
QOU.Mass.CoordinationSaturation requires B(A)/A bounded (observed ~8.8 MeV at
56Fe). All three diverge: n!/A reaches 1.2e17 at A = 20.

And the three gates are in STRUCTURAL tension, not merely awkward:

  * the SIGN gate wants D^3 and D^4 of the same sign  -> locally CONVEX
  * SATURATION wants f(A) = O(A)                      -> eventually SUBLINEAR
  * a sublinear increasing function has ALTERNATING high differences,
    so D^4/D^3 < 0.

Measured across the sublinear family: sqrt(A) -0.905, log(1+A) -0.687,
A^(2/3) -0.869, A - sqrt(A) -0.905. Every one fails the sign gate.

**So no single term of one variable can pass all three.** b3 > 0 and b4 > 0 with
a saturating binding force AT LEAST TWO contributions of opposite curvature.
Formalised in QOU/Mass/SaturationSignGateTension.lean (sorry-free).

This is the cumulant-side restatement of the coordination weight's proved
non-monotonicity (CoordinationWeightDifferences): w must rise then turn over. The
two derivations agree, which is a check on both.

SCOPE
-----
Derives no magnitude. The 6j / recoupling data is NOT refuted -- what is refuted
is the hope that supplying a genuinely three-object quantity is SUFFICIENT.
Passing the arity gate is cheap; the binding constraint is the joint
sign-plus-saturation condition, which is a statement about curvature across the
whole mass range that no single categorical scalar of one variable satisfies.

Bean qou-edt7.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import factorial  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from q_parameter import Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)
PARTS = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 8: 22, 12: 77, 16: 231, 20: 627}


def d3(f):
    return f(3) - 3 * f(2) + 3 * f(1) - f(0)


def d4(f):
    return f(4) - 4 * f(3) + 6 * f(2) - 4 * f(1) + f(0)


def main() -> int:
    wb = WitnessBuilder("sixj-recoupling-and-the-third-gate", engine="mpmath")
    wb.set_description(
        "The 6j route: a trace cannot see an associator (Mac Lane coherence), so "
        "the carrier must be the multiplicity structure. Following that to "
        "Hecke-natural quantities finds the first candidates to pass BOTH the "
        "arity and sign gates (n!, [n]_q!, [n]_q) -- and a third gate, "
        "saturation, kills all three. The three gates are structurally opposed: "
        "no single term of one variable can satisfy them, so at least two "
        "contributions of opposite curvature are forced."
    )
    ok = True

    q = mp.mpf(str(Q))

    def qint(n):
        return sum(q ** (n - 1 - 2 * k) for k in range(n)) if n > 0 else mp.mpf(0)

    def qfact(n):
        r = mp.mpf(1)
        for k in range(1, n + 1):
            r *= qint(k)
        return r

    D = ame_binding_mev(1, 2)
    T3, He3, He4 = ame_binding_mev(1, 3), ame_binding_mev(2, 3), ame_binding_mev(2, 4)
    B3 = (T3 + He3) / 2
    target = (He4 - 4 * B3 + 6 * D) / (B3 - 3 * D)
    print(f"measured b4/b3 = {mp.nstr(target,8)}\n")

    cands = [("dim_H_n_factorial", lambda n: mp.mpf(factorial(n))),
             ("q_factorial", qfact),
             ("q_integer", qint),
             ("partition_count", lambda n: mp.mpf(PARTS[n])),
             ("largest_specht_dim", lambda n: mp.mpf({0: 1, 1: 1, 2: 1, 3: 2, 4: 3}[n]))]
    rows, passers = [], []
    for nm, f in cands:
        a, b = d3(f), d4(f)
        r = b / a if a != 0 else mp.mpf("nan")
        p = a != 0 and r > 0
        if p:
            passers.append((nm, f))
        rows.append({"quantity": nm, "d3": fmt(a), "d4": fmt(b),
                     "b4_over_b3": fmt(r), "passes_arity_and_sign": bool(p)})
        print(f"  {nm:<22} D3={mp.nstr(a,6):>10} D4={mp.nstr(b,6):>10} "
              f"b4/b3={mp.nstr(r,6):>10}  {'BOTH GATES OK' if p else 'fails'}")
    wb.add_data("arity_and_sign", rows)
    print(f"\n  {len(passers)} pass both -- the first all session.")

    # third gate
    print("\nTHIRD GATE, saturation: B(A)/A must stay bounded (~8.8 MeV at 56Fe)")
    sat, diverged = [], 0
    for nm, f in passers:
        vals = {A: f(A) / A for A in (4, 8, 12, 16, 20)}
        grows = vals[20] > vals[4]
        diverged += grows
        sat.append({"quantity": nm, **{f"A_{A}": fmt(v) for A, v in vals.items()},
                    "diverges": bool(grows)})
        print(f"  {nm+'/A':<24} A=4 {mp.nstr(vals[4],6):>10}   "
              f"A=20 {mp.nstr(vals[20],6):>12}   {'DIVERGES' if grows else 'bounded'}")
    wb.add_data("saturation_gate", sat)
    wb.add_assertion(
        name="all_arity_sign_passers_fail_saturation",
        computed=str(diverged), expected=str(len(passers)), tolerance="0",
        unit="passers that diverge", source="B(A)/A must be bounded; all diverge",
    )
    ok &= diverged == len(passers)

    # the tension
    print("\nTHE TENSION -- sublinear f has alternating differences:")
    tension, n_alt = [], 0
    for nm, f in (("sqrt(A)", lambda n: mp.sqrt(n)),
                  ("log(1+A)", lambda n: mp.log(1 + n)),
                  ("A^(2/3)", lambda n: mp.mpf(n) ** (mp.mpf(2) / 3)),
                  ("A_minus_sqrt(A)", lambda n: n - mp.sqrt(n))):
        a, b = d3(f), d4(f)
        r = b / a
        n_alt += r < 0
        tension.append({"f": nm, "d3": fmt(a), "d4": fmt(b), "ratio": fmt(r)})
        print(f"  {nm:<18} D4/D3 = {mp.nstr(r,6):>10}   {'alternates' if r<0 else '!'}")
    wb.add_data("sublinear_family", tension)
    wb.add_assertion(
        name="sublinear_terms_fail_the_sign_gate",
        computed=str(n_alt), expected="4", tolerance="0",
        unit="sublinear f with D4/D3 < 0",
        source=("sign gate wants convexity, saturation wants sublinearity, and a "
                "sublinear increasing f alternates -- so no single term passes "
                "both. Lean: SaturationSignGateTension.two_terms_necessary"),
    )
    ok &= n_alt == 4

    wb.add_data("verdict", {
        "trace_can_see_associator": False,
        "why": "Mac Lane coherence -- all bracketings canonically isomorphic, so a "
               "functional of the isomorphism class is bracketing-independent; 6j "
               "symbols are basis-dependent structure constants, not invariants",
        "categorical_carrier_if_any": "the multiplicity structure -- blocks present "
                                      "at n=3 and absent at n=2, concretely S^(2,1)",
        "single_term_possible": False,
        "forced_conclusion": "b3>0 and b4>0 with saturation force >= 2 contributions "
                             "of opposite curvature; cumulant-side restatement of the "
                             "proved w non-monotonicity",
        "sixj_refuted": False,
        "what_is_refuted": "the hope that being genuinely three-object is SUFFICIENT",
        "derives_a_magnitude": False,
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
