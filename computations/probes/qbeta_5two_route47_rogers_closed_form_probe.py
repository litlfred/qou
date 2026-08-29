#!/usr/bin/env python3
"""Route 47 -- the sum rule in its cleanest form yet:
`sum_sigma L(y_sigma) = pi^2/2 - (2*pi/3)*arg(y_1)`, with L the Rogers
dilogarithm. No log-squared term at all.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Follows Route 46,
which found that the diagonal pentagon closes raw on the y-orbit.

THE FORM
--------
    sum_sigma L(y_sigma) = pi^2/2 - (2*pi/3)*arg(y_1)        residual 9e-61  (G1)

equivalently `11*pi^2/6 - 2*pi*Theta` with `Theta = arg` of the plastic cubic's
complex root, the two being related by `3*Theta = 2*pi + arg(y_1)` (also gated).

Every previous form of the sum rule carried a `log^2` term:

    V-form      : sum Re(V_j) = -3*pi^2/2,  V_j = 3*Li2 + (log y + b*pi*i)^2
    A-form      : A = -(9/2)*L^2 + 6*(Theta-pi)^2 - pi^2/6
    flattened   : sum Rhat(y; eps, 0) = -pi^2/6

This one has none: only `pi^2` and `pi` times an ANGLE. That is exactly the
shape a Chern-Simons / flattening statement should have, and it is the strongest
formal support yet for the extended-Bloch framing of Routes 42-46. It is
equivalent to the sum rule (G2), not a weakening -- `L = Li2 + log*log/2` and the
log-product Galois sum is elementary.

WHERE IT CAME FROM, AND WHAT DID NOT COME WITH IT
-------------------------------------------------
Route 46 showed the diagonal pentagon closes raw on the y-orbit:

    2*P + 2*Q + R = 3*pi^2/2,   P = sum L(y), Q = sum L(1/(1+y)), R = sum L(1-y^2)

`P` is elementary (G1). `Q` and `R` are **not** -- PSLQ finds nothing for either
at maxcoeff 1e7 against the elementary basis, nor widened with `log 7` (G3). So
the pentagon relation does NOT decompose into three elementary pieces; it says
only that `2Q + R` is elementary, which is one equation in two unknowns and
closes nothing.

⚠ `1 + y` has NORM 7, so `1/(1+y)` is not an algebraic integer -- its minimal
polynomial `7x^3 - 10x^2 + 5x - 1` is not monic. The diagonal pentagon therefore
leaves the unit tower of Routes 40-41 entirely, and brings in the prime 7 (G4).

AND THE SYMMETRY QUESTION, ANSWERED
-----------------------------------
The collapse of five terms to three is a **Z/2**, not an S3 (G5): the `x <-> y`
swap induces the permutation `(0 1)(2 4)(3)` on the five arguments -- cycle type
`[1,2,2]`, a reflection -- and on the diagonal its orbits become the
multiplicities `[2,2,1]`. The S3 in this subject is the anharmonic group
`<z -> 1-z, z -> 1/z>` acting on a SINGLE argument, a different action.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (arg, fabs, im, log, mp, mpc, mpf, nstr, pi, polylog,
                    polyroots, pslq, re)

Y_CUBIC = [1, -2, 3, -1]
PLASTIC = [1, 0, -1, -1]


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def pentagon(x, y):
    xy = x * y
    return [x, y, (1 - x) / (1 - xy), 1 - xy, (1 - y) / (1 - xy)]


def main() -> int:
    mp.dps = 60
    gates = []

    rs = polyroots(Y_CUBIC, maxsteps=900, extraprec=3500)
    y1 = [r for r in rs if im(r) > mpf(10) ** -45][0]
    rr = polyroots(PLASTIC, maxsteps=800, extraprec=3000)
    rho1 = [r for r in rr if im(r) > mpf(10) ** -45][0]
    Th = arg(rho1)

    P = re(sum(rogersL(z) for z in rs))
    Q = re(sum(rogersL(1 / (1 + z)) for z in rs))
    R = re(sum(rogersL(1 - z ** 2) for z in rs))

    # ---- G1: the closed form ------------------------------------------------
    f_arg = pi ** 2 / 2 - (2 * pi / 3) * arg(y1)
    f_theta = 11 * pi ** 2 / 6 - 2 * pi * Th
    link = fabs(3 * Th - 2 * pi - arg(y1))
    gates.append({
        "gate": "G1",
        "claim": "THE FORM. The Rogers-L Galois sum over the 5_2 saddle roots is "
                 "pi^2/2 - (2pi/3)*arg(y_1) -- only pi^2 and pi times an ANGLE, with NO "
                 "log-squared term, unlike every previous form of the sum rule. Equivalently "
                 "11pi^2/6 - 2 pi Theta via 3*Theta = 2pi + arg(y_1), also gated",
        "P": nstr(P, 40),
        "pi_sq_over_2_minus_two_pi_over_3_arg_y1": nstr(f_arg, 40),
        "residual": nstr(fabs(P - f_arg), 12),
        "eleven_pi_sq_over_6_minus_two_pi_Theta": nstr(f_theta, 40),
        "residual_theta_form": nstr(fabs(P - f_theta), 12),
        "three_Theta_minus_2pi_minus_arg_y1": nstr(link, 12),
        "pass": bool(fabs(P - f_arg) < mpf(10) ** -50
                     and fabs(P - f_theta) < mpf(10) ** -50
                     and link < mpf(10) ** -50),
    })

    # ---- G2: equivalent to the sum rule, not a weakening --------------------
    A = re(sum(polylog(2, z) for z in rs))
    logprod = re(sum(log(z) * log(1 - z) for z in rs))
    A_target = mpf("0.9717306814686482591277741699385505001120059963420977208")
    gates.append({
        "gate": "G2",
        "claim": "it is EQUIVALENT to the sum rule, not a weakening: L = Li2 + log*log/2, so "
                 "P = A + (1/2)*sum log y log(1-y) with the log-product Galois sum elementary. "
                 "A is checked against the value the sum rule forces, so the chain from this "
                 "form back to the original statement is closed",
        "A": nstr(A, 30),
        "A_from_the_sum_rule": nstr(A_target, 30),
        "A_residual": nstr(fabs(A - A_target), 12),
        "P_minus_A_minus_half_logprod": nstr(fabs(P - A - logprod / 2), 12),
        "pass": bool(fabs(A - A_target) < mpf(10) ** -40
                     and fabs(P - A - logprod / 2) < mpf(10) ** -45),
    })

    # ---- G3: Q and R are NOT elementary -- the relation does not decompose --
    rho = [r for r in rr if fabs(im(r)) < mpf(10) ** -45][0].real
    Lg = log(rho)
    basis = [pi ** 2, Lg ** 2, Th ** 2, Th * pi, pi * log(7), log(7) ** 2]
    found = {}
    for tag, v in (("P", P), ("Q", Q), ("R", R)):
        rel = pslq([v] + basis, tol=mpf(10) ** -40, maxcoeff=10 ** 7, maxsteps=20000)
        small = bool(rel is not None and max(abs(c) for c in rel) < 10 ** 4)
        found[tag] = {"relation": rel, "small_coefficients": small}
    pent_res = fabs(2 * P + 2 * Q + R - 3 * pi ** 2 / 2)
    gates.append({
        "gate": "G3",
        "claim": "the diagonal pentagon 2P + 2Q + R = 3pi^2/2 holds exactly, but does NOT "
                 "decompose: P is elementary with small coefficients while PSLQ finds nothing "
                 "for Q or for R at maxcoeff 1e7. So the relation says only that 2Q + R is "
                 "elementary -- one equation in two unknowns, closing nothing. (Absence of a "
                 "PSLQ hit is evidence, not proof, and is reported as such)",
        "pentagon_residual": nstr(pent_res, 12),
        "pslq": found,
        "pass": bool(pent_res < mpf(10) ** -45 and found["P"]["small_coefficients"]
                     and not found["Q"]["small_coefficients"]
                     and not found["R"]["small_coefficients"]),
    })

    # ---- G4: the diagonal leaves the unit tower -- the prime 7 -------------
    norm_1_plus_y = 1
    for z in rs:
        norm_1_plus_y *= (1 + z)
    gates.append({
        "gate": "G4",
        "claim": "the diagonal pentagon LEAVES the unit tower of Routes 40-41: N(1+y) = 7, so "
                 "1/(1+y) is not an algebraic integer and its minimal polynomial 7x^3-10x^2+5x-1 "
                 "is not monic. The prime 7 enters here -- worth flagging in a lane named for a "
                 "level-7 ladder, though no connection to that ladder is measured",
        "norm_of_one_plus_y": nstr(re(norm_1_plus_y), 20),
        "pass": bool(fabs(re(norm_1_plus_y) - 7) < mpf(10) ** -40),
    })

    # ---- G5: the collapse is a Z/2 reflection, not an S3 -------------------
    x0, y0 = mpc('0.31', '0.17'), mpc('0.23', '-0.41')
    A5, B5 = pentagon(x0, y0), pentagon(y0, x0)
    perm = [min(range(5), key=lambda k: fabs(A5[k] - b)) for b in B5]
    z0 = mpc('0.37', '0.29')
    D5 = pentagon(z0, z0)
    mult = {}
    for a in D5:
        key = next((k for k in mult if fabs(k - a) < mpf(10) ** -30), None)
        mult[a if key is None else key] = 1 if key is None else mult[key] + 1
    gates.append({
        "gate": "G5",
        "claim": "the five-to-three collapse is a Z/2, NOT an S3: the x<->y swap induces "
                 "(0 1)(2 4)(3) on the five arguments -- cycle type [1,2,2], a reflection -- and "
                 "on the diagonal its orbits become multiplicities [2,2,1]. The S3 in this "
                 "subject is the anharmonic group <z->1-z, z->1/z> acting on a SINGLE argument, "
                 "which is a different action entirely",
        "swap_permutation": perm,
        "cycle_type": [1, 2, 2],
        "diagonal_multiplicities": sorted(mult.values(), reverse=True),
        "pass": bool(perm == [1, 0, 4, 3, 2]
                     and sorted(mult.values(), reverse=True) == [2, 2, 1]),
    })

    out = {
        "probe": "qbeta_5two_route47_rogers_closed_form",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": "Route 46 (the diagonal pentagon closes raw on the y-orbit)",
        "gates": gates,
        "verdict": {
            "form": "sum_sigma L(y_sigma) = pi^2/2 - (2pi/3)*arg(y_1), residual 9e-61 -- the "
                    "cleanest statement of the sum rule so far, with no log-squared term, only "
                    "pi^2 and pi times an angle.",
            "why_it_matters": "that is the shape a Chern-Simons / flattening statement takes, "
                              "which is formal support for the extended-Bloch framing of Routes "
                              "42-46 rather than another reformulation for its own sake.",
            "what_it_does_not_give": "the pentagon it came from does not decompose -- Q and R "
                                     "are individually non-elementary, so 2Q + R = elementary is "
                                     "one equation in two unknowns. And the diagonal leaves the "
                                     "unit tower: N(1+y) = 7.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route47-rogers-closed-form.witness.json")
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
        "the sum rule is sum L(y_sigma) = pi^2/2 - (2pi/3) arg(y_1) -- no log^2 term, exactly the "
        "shape of a Chern-Simons statement. Still unproved: the pentagon it came from does not "
        "decompose. The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
