#!/usr/bin/env python3
"""Route 24 -- the unevaluated real integral: what it is, and why residues do not touch it.

Beans `qou-0yqu` (the sum-rule gap) and `qou-clx8`. Answers four questions asked
of this lane, with numbers rather than assertions.

WHAT THE INTEGRAL IS
--------------------
    I  :=  -int_0^1 log P(z)/z dz,      P(z) = 1 - 2z + 3z^2 - z^3

P is the RECIPROCAL of the 5_2 saddle cubic y^3 - 2y^2 + 3y - 1 -- equivalently
P(z) = prod_j (1 - y_j z) over its three roots -- so P is a real integer cubic,
positive on [0,1], and I is one convergent real integral with no complex root in
sight. Numerically

    I = 0.9717306814686482591277741699385505...

CAN IT BE EVALUATED?
--------------------
Numerically, yes, to any precision. In closed form as a THEOREM, that IS the open
problem: G2 derives independently that

    3*sum_j Li2(y_j) + sum_j Re log^2(-y_j) = -3 pi^2 / 2

is exactly the 5_2 sum rule sum_j Re V_j = -3 pi^2/2 at x = 1. So "evaluate the
integral" and "prove the sum rule" are the same task, not two.

G4 pins the closed form by PSLQ at 120 dps and shows it is MINIMAL -- with
L = log y_3 and th = arg y_1,

    6 I  =  3 pi^2 - 3 L^2 + 4 th^2 - 8 pi th

and no sub-basis of {pi^2, L^2, th^2} supports any relation at all. All four
terms are genuinely needed.

RESIDUES?
---------
G3 runs the residue route to its end and it is CIRCULAR, for a sharp reason:
integrate by parts to get I = int_0^1 log z * P'(z)/P(z) dz, whose integrand is
rational apart from log z. Its poles are the roots of P -- but P'/P is a
logarithmic derivative with simple roots, so **every residue is exactly 1**.
Residues carry only the location of the roots and no arithmetic beyond it. The
transcendence lives in log z, which is not meromorphic; the branch-cut
contribution at each pole is int_0^1 log z/(z-r) dz = Li2(1/r), and summing
returns sum_j Li2(y_j) -- the quantity we started from. `qou-0yqu` warned that
expanding log P = sum log(1 - y_j z) is circular; this shows the residue route
is the same circle traversed the other way.

WHERE THE LITERATURE LEAD MAY MISPOINT
--------------------------------------
`qou-0yqu` records that the field has discriminant -23, the smallest |disc| among
complex cubic fields and the classical worked example in the dilogarithm-ladder /
Zagier-conjecture literature, and suggests "a lookup in a well-trodden one".

G5 is a caution. That literature computes zeta_F(2) via the BLOCH-WIGNER function
D, and D is the imaginary-part invariant. Here sum_j D(y_j) = 0 automatically (P
is real, so D(y_3) = 0 and D(conj y_1) = -D(y_1)) -- it carries no information.
Meanwhile PSLQ says D(y_1) = 0.9427... is INDEPENDENT of the whole log/arg basis,
while I lies inside it. So D and I are different invariants and the zeta_F(2)
machinery governs the one this problem does not need.

G6 is the constructive counterpart. Both prod_j y_j = 1 and prod_j (1 - y_j) = 1,
so y and 1-y are units; and a complex cubic field has unit rank r1 + r2 - 1 = 1,
whence the exterior square of the units (tensor Q) is ZERO and the wedge
obstruction y ^ (1-y) vanishes identically. That is the structural reason a
weight-2 ladder should exist here at all, and it points the attack at explicit
five-term functional equations -- which this branch already has as a Lean theorem
(`rogersL_fiveTerm`) -- rather than at a zeta-value lookup.

**The 5_2 sum rule remains verified to 80 dps, unproved.** Nothing here evaluates
the integral; it locates the difficulty and rules out one route.
"""

import json
import pathlib

from mpmath import (arg, conj, diff, fabs, im, log, mp, mpf, nstr, pi, polylog,
                    polyroots, pslq, quad, re)


def main() -> int:
    mp.dps = 120
    TOL = mpf(10) ** -90
    gates = []

    rts = polyroots([1, -2, 3, -1], maxsteps=2000, extraprec=6000)
    y3 = [r for r in rts if fabs(im(r)) < mpf(10) ** -90][0].real
    y1 = [r for r in rts if im(r) > mpf(10) ** -90][0]
    P = lambda z: 1 - 2 * z + 3 * z ** 2 - z ** 3
    Pp = lambda z: -2 + 6 * z - 3 * z ** 2
    L, th = log(y3), arg(y1)

    # ---- G1: what the integral is ------------------------------------------
    I = -quad(lambda z: log(P(z)) / z, [mpf(0), mpf(1)], maxdegree=14)
    I_sum = polylog(2, y3) + 2 * re(polylog(2, y1))
    pmin = min(P(mpf(k) / 40) for k in range(0, 41))
    gates.append({
        "gate": "G1",
        "claim": "the integral is I = -int_0^1 log P(z)/z dz with P(z) = 1-2z+3z^2-z^3, the "
                 "RECIPROCAL of the 5_2 cubic, i.e. P(z) = prod_j (1 - y_j z). It is a real "
                 "integer cubic, positive on [0,1], and I equals sum_j Li2(y_j)",
        "I": nstr(I, 45), "sum_Li2": nstr(I_sum, 45),
        "diff": nstr(fabs(I - I_sum), 8),
        "min_P_on_[0,1]": nstr(pmin, 12),
        "pass": bool(fabs(I - I_sum) < TOL and pmin > 0),
    })

    # ---- G2: evaluating it IS proving the sum rule --------------------------
    lhs = 3 * I_sum + (re(log(-y3) ** 2) + 2 * re(log(-y1) ** 2))
    gates.append({
        "gate": "G2",
        "claim": "derived independently here, not taken from the bean: 3*sum Li2(y_j) + sum "
                 "Re log^2(-y_j) = -3 pi^2/2, which is exactly sum_j Re V_j = -3 pi^2/2 at "
                 "x = 1 since V_j = 3 Li2(y_j) + log(-y_j)^2 there. So 'evaluate the integral' "
                 "and 'prove the sum rule' are ONE task, not two",
        "lhs": nstr(re(lhs), 40), "minus_3pi2_over_2": nstr(-3 * pi ** 2 / 2, 40),
        "diff": nstr(fabs(re(lhs) + 3 * pi ** 2 / 2), 8),
        "pass": bool(fabs(re(lhs) + 3 * pi ** 2 / 2) < TOL),
    })

    # ---- G3: the residue route, run to its end, is circular -----------------
    ibp = quad(lambda z: log(z) * Pp(z) / P(z), [mpf(0), mpf(1)], maxdegree=14)
    Proots = polyroots([-1, 3, -2, 1], maxsteps=2000, extraprec=6000)
    residues = [Pp(r) / diff(P, r) for r in Proots]
    per_pole = quad(lambda z: log(z) / (z - Proots[0]), [mpf(0), mpf(1)], maxdegree=14)
    back = sum(polylog(2, 1 / r) for r in Proots)
    gates.append({
        "gate": "G3",
        "claim": "RESIDUES ARE CIRCULAR, and the reason is sharp. IBP gives I = int_0^1 log z * "
                 "P'(z)/P(z) dz, rational apart from log z. But P'/P is a logarithmic "
                 "derivative with simple roots, so EVERY residue is exactly 1 -- they carry only "
                 "where the roots are, no arithmetic. The transcendence is in log z, whose "
                 "branch cut contributes int_0^1 log z/(z-r) dz = Li2(1/r) at each pole, and "
                 "the sum returns sum_j Li2(y_j): the quantity we started from",
        "ibp_matches_I": nstr(fabs(I - ibp), 8),
        "residues_of_Pprime_over_P": [nstr(rr, 12) for rr in residues],
        "all_residues_are_one": bool(all(fabs(rr - 1) < TOL for rr in residues)),
        "per_pole_integral": nstr(per_pole, 30),
        "per_pole_Li2": nstr(polylog(2, 1 / Proots[0]), 30),
        "residue_route_returns": nstr(re(back), 40),
        "equals_I": nstr(fabs(re(back) - I), 8),
        "pass": bool(fabs(I - ibp) < TOL
                     and all(fabs(rr - 1) < TOL for rr in residues)
                     and fabs(re(back) - I) < TOL),
    })

    # ---- G4: the closed form, by PSLQ, and it is MINIMAL --------------------
    basis = [I, pi ** 2, L ** 2, th ** 2, pi * th, pi * L, th * L]
    rel = pslq(basis, maxcoeff=10 ** 8, maxsteps=10 ** 6, tol=TOL)
    subs = {}
    for name, b in [("{I,pi^2}", [I, pi ** 2]),
                    ("{I,pi^2,L^2}", [I, pi ** 2, L ** 2]),
                    ("{I,pi^2,th^2}", [I, pi ** 2, th ** 2]),
                    ("{I,pi^2,L^2,th^2}", [I, pi ** 2, L ** 2, th ** 2])]:
        subs[name] = pslq(b, maxcoeff=10 ** 6, maxsteps=10 ** 5, tol=mpf(10) ** -80)
    gates.append({
        "gate": "G4",
        "claim": "PSLQ at 120 dps pins the closed form: 6I = 3 pi^2 - 3 L^2 + 4 th^2 - 8 pi th "
                 "with L = log y_3, th = arg y_1 -- and it is MINIMAL: no sub-basis of "
                 "{pi^2, L^2, th^2} supports any relation, so all four terms are needed. The "
                 "pi*L and th*L coefficients come out zero, so the relation is exactly the "
                 "form -pi^2/6 - L^2/2 + (2/3)(th - pi)^2 that qou-0yqu records",
        "relation_coeffs": [int(c) for c in rel] if rel else None,
        "basis_order": ["I", "pi^2", "L^2", "th^2", "pi*th", "pi*L", "th*L"],
        "subbasis_relations": {k: ([int(c) for c in v] if v else None) for k, v in subs.items()},
        "pass": bool(rel is not None and all(v is None for v in subs.values())),
    })

    # ---- G5: the Bloch-Wigner invariant is a DIFFERENT one ------------------
    D1 = im(polylog(2, y1)) + arg(1 - y1) * log(fabs(y1))
    D3 = im(polylog(2, y3)) + arg(1 - y3) * log(fabs(y3))
    Dsum = D3 + D1 + (im(polylog(2, conj(y1))) + arg(1 - conj(y1)) * log(fabs(conj(y1))))
    withD = pslq([I, pi ** 2, L ** 2, th ** 2, pi * th, D1],
                 maxcoeff=10 ** 6, maxsteps=10 ** 5, tol=mpf(10) ** -80)
    Dalone = pslq([D1, pi ** 2, L ** 2, th ** 2, pi * th, th * L],
                  maxcoeff=10 ** 6, maxsteps=10 ** 5, tol=mpf(10) ** -80)
    gates.append({
        "gate": "G5",
        "claim": "CAUTION on the disc -23 literature lead. That machinery computes zeta_F(2) via "
                 "the BLOCH-WIGNER D, the imaginary-part invariant. Here sum_j D(y_j) = 0 "
                 "automatically (P is real: D(y_3) = 0 and D(conj y_1) = -D(y_1)), so it says "
                 "nothing. And PSLQ finds D(y_1) INDEPENDENT of the whole log/arg basis, while "
                 "I lies inside it -- D enters the relation with coefficient 0. Different "
                 "invariants; the zeta_F(2) route governs the one this problem does not need",
        "D_y1": nstr(D1, 30), "sum_D": nstr(fabs(Dsum), 8),
        "relation_with_D": [int(c) for c in withD] if withD else None,
        "D_vs_log_arg_basis": [int(c) for c in Dalone] if Dalone else None,
        "pass": bool(fabs(Dsum) < TOL and withD is not None and withD[-1] == 0
                     and Dalone is None),
    })

    # ---- G6: why a ladder should exist at all -------------------------------
    prod_y = y3 * y1 * conj(y1)
    prod_1my = (1 - y3) * (1 - y1) * (1 - conj(y1))
    gates.append({
        "gate": "G6",
        "claim": "the constructive counterpart: prod_j y_j = 1 and prod_j (1 - y_j) = 1, so y "
                 "and 1-y are units. A complex cubic field has unit rank r1 + r2 - 1 = 1, so "
                 "the exterior square of the units (tensor Q) is ZERO and the wedge obstruction "
                 "y ^ (1-y) vanishes identically -- the structural reason a weight-2 ladder "
                 "should exist. That points the attack at explicit five-term functional "
                 "equations, which this branch already has as a Lean theorem (rogersL_fiveTerm), "
                 "rather than at a zeta-value lookup",
        "prod_y": nstr(re(prod_y), 20), "prod_one_minus_y": nstr(re(prod_1my), 20),
        "unit_rank_of_complex_cubic": "r1 + r2 - 1 = 1 + 1 - 1 = 1",
        "dim_exterior_square": "C(1,2) = 0",
        "pass": bool(fabs(prod_y - 1) < TOL and fabs(prod_1my - 1) < TOL),
    })

    out = {
        "probe": "qbeta_5two_route24_integral_evaluation",
        "bean": "qou-0yqu", "related_bean": "qou-clx8", "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "what_the_integral_is": "I = -int_0^1 log(1 - 2z + 3z^2 - z^3)/z dz = "
                                    "0.97173068146864825912777416993855050011..., a real "
                                    "integral of an integer cubic, positive on [0,1].",
            "can_we_evaluate": "Numerically to any precision. In closed form as a theorem: that "
                               "IS the sum rule (G2), so it is the open problem itself, not a "
                               "separable subproblem. The closed form is known and MINIMAL "
                               "(G4): 6I = 3 pi^2 - 3 L^2 + 4 th^2 - 8 pi th.",
            "lean_proof": "Not available and not close. What is Lean-proved is the restatement "
                          "(I equals the dilog sum) and now the continuation it needs; the "
                          "EVALUATION is the unproved step. A Lean proof would have to follow "
                          "whatever functional-equation argument establishes it on paper, and "
                          "no such argument is in hand.",
            "residues": "Ruled out, demonstrably (G3). IBP makes the integrand rational apart "
                        "from log z, but P'/P is a logarithmic derivative with simple roots so "
                        "every residue is exactly 1 -- no arithmetic content. The branch cut of "
                        "log z contributes Li2 at each pole and returns the original sum. It is "
                        "the circle qou-0yqu warns about, traversed the other way.",
            "where_to_attack": "G6: y and 1-y are units and the field's unit rank is 1, so the "
                               "wedge obstruction vanishes identically and a weight-2 ladder "
                               "should exist. Explicit five-term functional equations are the "
                               "route, and rogersL_fiveTerm is already a Lean theorem on this "
                               "branch. G5 cautions that the disc -23 zeta_F(2) literature "
                               "governs the Bloch-Wigner invariant, which is NOT this one.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route24-integral-evaluation.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: the integral IS the sum rule; residues are circular; five-term is the route.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
