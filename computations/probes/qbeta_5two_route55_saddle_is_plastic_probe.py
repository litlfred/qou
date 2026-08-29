#!/usr/bin/env python3
"""Route 55 -- the 5_2 saddle cubic IS the plastic cubic, anharmonically; so the
pentagon relation Route 54 proved was already inside every alphabet tested.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Follows Route 54,
whose theorem (`FiveTwoComplexPentagon.pentagonSum_eq_pi_sq_div_two`, Lean,
sorry-free) reaches the pair `(y_3, y_1)`. This probe asks what that relation
actually says there, and the answer is a negative.

THE STRUCTURE
-------------
At `(y_3, y_1)` -- the saddle cubic's real root against a complex one -- the five
pentagon arguments are exceptional. All four facts below are EXACT, verified
symbolically (sympy Groebner reduction against the symmetric-function relations)
before being measured here:

    ((y-1)/y)^3 - (y-1)/y + 1  =  (y^3 - 2y^2 + 3y - 1) / y^3    [identity of
                                                                  RATIONAL FUNCTIONS]
    a_5 = 1/a_3                      <=>  (1-a)(1-b) = (1-ab)^2
    1 - a_3 = conj(a_3)              <=>  a_3 + conj(a_3) = 1
    |a_3|^2 = y_3                    <=>  a_3 * conj(a_3) = y_3

THE NEGATIVE THAT MATTERS
-------------------------
The first identity has no modular reduction in it: the anharmonic map
`y -> 1 - 1/y` carries the 5_2 saddle cubic ONTO `X^3 - X + 1`, whose roots are
the negatives of the plastic numbers. So the saddle orbit and the plastic orbit
are ONE orbit of the anharmonic group `<z -> 1-z, z -> 1/z>`.

Routes 41, 47 and 48 closed their alphabets under exactly those two maps. So
every relation the pentagon produces at `(y_3, y_1)` was already inside those
alphabets -- and the rank gap was exactly 1 in all of them. **Route 54's theorem
does not add rank.** What it does is explain why the plastic tower kept surfacing
through Routes 40-48: it was never a coincidence, it is the same orbit.

The degree-6 elements do not rescue it either: `a_3` and `a_5` share the
palindromic minimal polynomial `X^6-3X^5+5X^4-5X^3+5X^2-3X+1`, but `a_5 = 1/a_3`
makes `L(a_3) + L(a_5)` elementary by inversion, so they cancel out of the
relation and only the degree-3 orbit survives.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (arg, conj, fabs, im, log, mp, mpf, nstr, pi, polylog,
                    polyroots, re)

SADDLE = [1, -2, 3, -1]        # y^3 - 2y^2 + 3y - 1
PLASTIC_NEG = [1, 0, -1, 1]    # X^3 - X + 1, roots = -(plastic numbers)


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def main() -> int:
    mp.dps = 60
    tol = mpf(10) ** -45
    gates = []

    roots = polyroots(SADDLE, maxsteps=1200, extraprec=6000)
    y3 = re([r for r in roots if fabs(im(r)) < tol][0])
    y1 = [r for r in roots if im(r) > tol][0]
    y2 = conj(y1)
    d = 1 - y3 * y1
    a3 = (1 - y3) / d
    a5 = (1 - y1) / d

    # ---- G1: the anharmonic map, as an identity of rational functions ------
    resid = []
    for r in roots:
        u = (r - 1) / r
        resid.append(fabs(u ** 3 - u + 1))
    # and the identity itself at generic points, where the cubic does NOT vanish
    generic = []
    for t in [mpf("0.37"), mpf("2.5"), mpf("-1.75"), mpf(1) / 3]:
        u = (t - 1) / t
        generic.append(fabs((u ** 3 - u + 1)
                            - (t ** 3 - 2 * t ** 2 + 3 * t - 1) / t ** 3))
    pl_roots = polyroots(PLASTIC_NEG, maxsteps=1200, extraprec=6000)
    gates.append({
        "gate": "G1",
        "claim": "THE NEGATIVE THAT MATTERS. The anharmonic map y -> 1 - 1/y carries the 5_2 "
                 "saddle cubic ONTO X^3-X+1 (roots = negated plastic numbers), and it does so as "
                 "an identity of RATIONAL FUNCTIONS -- checked at generic points where the cubic "
                 "does not vanish, so it is not a modular coincidence. Routes 41/47/48 closed "
                 "their alphabets under 1-z and 1/z, which generate that group, so every relation "
                 "Route 54's pentagon produces at (y_3,y_1) was ALREADY inside them. Route 54's "
                 "theorem does not add rank; it explains the plastic tower of Routes 40-48",
        "max_residual_at_roots": nstr(max(resid), 8),
        "max_residual_generic": nstr(max(generic), 8),
        "plastic_neg_roots": [nstr(r, 18) for r in pl_roots],
        "pass": bool(max(resid) < tol and max(generic) < tol),
    })

    # ---- G2: a_4 is one of those roots -------------------------------------
    hit = min(fabs(d - r) for r in pl_roots)
    gates.append({
        "gate": "G2",
        "claim": "the pentagon's fourth argument lands there: a_4 = 1 - y_3*y_1 = 1 - 1/y_2 is a "
                 "root of X^3-X+1, i.e. minus a plastic number. This is the concrete face of G1",
        "a4": nstr(d, 25),
        "distance_to_nearest_plastic_neg_root": nstr(hit, 8),
        "pass": bool(hit < tol),
    })

    # ---- G3: the exceptional structure of a_3, a_5 -------------------------
    gates.append({
        "gate": "G3",
        "claim": "the two composite arguments are exceptional, all four facts exact and verified "
                 "symbolically by Groebner reduction against a+b+c=2, ab+ac+bc=3, abc=1: "
                 "a_5 = 1/a_3 (equivalent to the cubic itself), 1-a_3 = conj(a_3), and "
                 "|a_3|^2 = y_3. So L(a_3)+L(a_5) is elementary by inversion and the degree-6 "
                 "elements CANCEL out of the relation, leaving only the degree-3 orbit -- which "
                 "is why the degree-6 field does not rescue the rank either",
        "a3": nstr(a3, 25),
        "a5_minus_inv_a3": nstr(fabs(a5 - 1 / a3), 8),
        "re_a3_minus_half": nstr(fabs(re(a3) - mpf(1) / 2), 8),
        "abs_a3_sq_minus_y3": nstr(fabs(fabs(a3) ** 2 - y3), 8),
        "minpoly_a3": "X^6 - 3X^5 + 5X^4 - 5X^3 + 5X^2 - 3X + 1  (palindromic)",
        "pass": bool(fabs(a5 - 1 / a3) < tol and fabs(re(a3) - mpf(1) / 2) < tol
                     and fabs(fabs(a3) ** 2 - y3) < tol),
    })

    # ---- G4: the pentagon relation itself, at that pair --------------------
    pent = rogersL(y3) + rogersL(y1) + rogersL(a3) + rogersL(d) + rogersL(a5)
    inv = rogersL(a3) + rogersL(1 / a3)
    rest = rogersL(y3) + rogersL(y1) + rogersL(d)
    sum_y = sum(rogersL(z) for z in roots)
    route47 = pi ** 2 / 2 - (2 * pi / 3) * arg(y1)
    gates.append({
        "gate": "G4",
        "claim": "the relation Route 54 proves, written out at (y_3,y_1): "
                 "L(y_3)+L(y_1)+L(a_4) = pi^2/2 - [L(a_3)+L(1/a_3)], with a_4 minus a plastic "
                 "number and the bracket elementary. Route 47's closed form for the y-orbit sum "
                 "is re-verified alongside it at 60 dps, unchanged",
        "pentagon_minus_pi_sq_over_2": nstr(fabs(pent - pi ** 2 / 2), 8),
        "L_y3_plus_L_y1_plus_L_a4": nstr(rest, 25),
        "pi_sq_over_2_minus_inversion": nstr(pi ** 2 / 2 - inv, 25),
        "sum_L_over_y_cubic": nstr(re(sum_y), 25),
        "route47_closed_form": nstr(route47, 25),
        "pass": bool(fabs(pent - pi ** 2 / 2) < tol
                     and fabs(rest - (pi ** 2 / 2 - inv)) < tol
                     and fabs(re(sum_y) - route47) < mpf(10) ** -40),
    })

    # ---- G5: target unmoved -------------------------------------------------
    A = re(sum(polylog(2, z) for z in roots))
    gates.append({
        "gate": "G5",
        "claim": "the target is unmoved, and this route moves it FURTHER from reach, not closer: "
                 "G1 says the relation Route 54 proved was already in the alphabets whose rank "
                 "gap has been exactly 1 four times over. A = sum Li2(y_j) still has no proof",
        "A": nstr(A, 30),
        "pass": bool(fabs(A - mpf("0.9717306814686482591277741699")) < mpf(10) ** -25),
    })

    out = {
        "probe": "qbeta_5two_route55_saddle_is_plastic",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": "Route 54 (the unconditional one-variable pentagon)",
        "lean": "QOU/QBeta/FiveTwoComplexPentagon.lean -- saddle_to_plastic, "
                "plastic_of_saddle, saddle_of_plastic, pentagon_arg_reciprocal",
        "gates": gates,
        "verdict": {
            "structural": "y -> 1 - 1/y carries the 5_2 saddle cubic onto X^3-X+1 as an identity "
                          "of rational functions. The saddle orbit and the (negated) plastic "
                          "orbit are ONE anharmonic orbit.",
            "negative": "so Route 54's pentagon relation was already inside the alphabets of "
                        "Routes 41/47/48, all closed under 1-z and 1/z. It does not add rank.",
            "explains": "why the plastic tower kept surfacing through Routes 40-48 -- same orbit, "
                        "not a coincidence.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route55-saddle-is-plastic.witness.json")
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
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "y -> 1 - 1/y carries the 5_2 saddle cubic onto X^3-X+1 as an identity of RATIONAL "
        "FUNCTIONS, so the saddle orbit and the negated-plastic orbit are one anharmonic orbit. "
        "Route 54's pentagon relation was therefore already inside every alphabet tested and "
        "adds no rank -- but it explains the plastic tower of Routes 40-48. The 5_2 sum rule "
        "remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
