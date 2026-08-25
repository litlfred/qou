#!/usr/bin/env python3
"""Route 35 -- the INVERSION leg is not a boundary-value problem after all.

Bean `qou-invr` (attack vector A2), child of `qou-rstq` item 4.

WHAT THIS CHANGES
-----------------
`qou-invr` recorded the inversion leg as needing "a boundary value of Li2 from
off the cut, not a constant of integration" -- because x > 1 lies ON
cLiTwoExt's cut. A2 proposed checking first whether the REAL PART is
continuous across the cut even though Li2 is not, since only Re L is ever
needed. It is. That collapses the shape of the problem:

  BEFORE: obtain a boundary value of Li2 on [1, inf) -- new analytic infra.
  AFTER:  prove one REAL identity with no cut in it at all,
          Re Li2(x) + Li2(1/x) = pi^2/3 - (1/2) log^2 x,
          plus integrability of the defining integral at x > 1.

G6 states what is still needed, so this is not read as closing the item.

A PREDICTION THIS PROBE FALSIFIED
---------------------------------
Before measuring, I expected Lean's integral definition at real x > 1 to pick
the UPPER boundary value Li2(x + i0+), reasoning that Complex.log of a negative
real has arg = +pi. **It picks the LOWER one.** G4 records the measurement and
the wrong prediction, because the sign of that branch is exactly the kind of
detail this lane has got wrong before, and a corrected guess is worth more in
the record than a silent one.

It does not matter for the conclusion -- which is the point of G3.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (fabs, findroot, im, log, mp, mpc, mpf, nstr, pi, polylog,
                    quad, re)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def rogersL_real(u):
    """The corpus's rogersL on (0,1), where its LiTwo series converges."""
    return polylog(2, u) + log(u) * log(1 - u) / 2


def extend_gt1(x):
    """The corpus's `extend (pi^2/6) rogersL` in the x > 1 (inversion) branch."""
    return 2 * (pi ** 2 / 6) - rogersL_real(1 / x)


def ReL(x):
    """Re of the ANALYTIC Rogers L at real x, principal branches."""
    z = mpc(x, 0)
    return re(polylog(2, z) + log(z) * log(1 - z) / 2)


def lean_integral(x):
    """EXACTLY Lean's cLiTwoExt: -int_0^1 log(1 - x t)/t dt, principal branch.

    Split at t = 1/x, where 1 - x t vanishes and the integrand has its
    (integrable) logarithmic singularity.
    """
    f = lambda t: log(1 - mpc(x, 0) * t) / t
    return -quad(f, [0, 1 / mpf(x), 1])


def main() -> int:
    set_compute_dps()
    tol = mpf(10) ** -25
    eps = mpf(10) ** -30
    gates = []

    xr = findroot(lambda t: t ** 3 - 2 * t ** 2 - t + 1, mpf("0.55"))
    w1 = 1 / (1 - xr)

    # ---- G1: the Re jump across the cut is ZERO; the Im jump is not ---------
    rows1 = []
    ok1 = True
    for x in [mpf("1.5"), w1, mpf(3), mpf(5)]:
        up, dn = polylog(2, mpc(x, eps)), polylog(2, mpc(x, -eps))
        d = up - dn
        pred = mpc(0, 2 * pi * log(x))
        rows1.append({"x": nstr(x, 14), "re_jump": nstr(fabs(re(d)), 8),
                      "im_jump": nstr(fabs(im(d)), 12),
                      "predicted_2_pi_i_log_x": nstr(pred, 12),
                      "matches_prediction": bool(fabs(d - pred) < tol)})
        ok1 = ok1 and fabs(re(d)) < tol and fabs(d - pred) < tol
    gates.append({
        "gate": "G1",
        "claim": "A2's premise: Li2's discontinuity across [1,inf) is EXACTLY 2*pi*i*log(x) -- "
                 "purely imaginary. So Re Li2 is CONTINUOUS across the cut even though Li2 is "
                 "not. The Re jump measures as zero; the Im jump is nonzero and matches the "
                 "prediction, which is what makes the zero meaningful rather than a null result",
        "per_point": rows1, "pass": bool(ok1),
    })

    # ---- G2: and so is Re of the full Rogers L -----------------------------
    rows2 = []
    ok2 = True
    for x in [mpf("1.5"), w1, mpf(3), mpf(5)]:
        f = lambda z: polylog(2, z) + log(z) * log(1 - z) / 2
        d = f(mpc(x, eps)) - f(mpc(x, -eps))
        rows2.append({"x": nstr(x, 14), "re_jump": nstr(fabs(re(d)), 8),
                      "im_jump": nstr(fabs(im(d)), 12)})
        ok2 = ok2 and fabs(re(d)) < tol
    gates.append({
        "gate": "G2",
        "claim": "the SAME for the full Rogers L, which is what is actually needed. Both of its "
                 "terms jump -- Li2 by 2*pi*i*log x, and log(x)*log(1-x)/2 because log(1-x) "
                 "crosses log's cut -- and BOTH jumps are purely imaginary, so Re L is "
                 "continuous across [1,inf). Checking Li2 alone would not have settled this",
        "per_point": rows2, "pass": bool(ok2),
    })

    # ---- G3: what the leg reduces to -- a REAL identity, no cut ------------
    worst3 = mpf(0)
    at3 = None
    for i in range(1, 201):
        x = 1 + mpf(i) / 20
        lhs = re(polylog(2, mpc(x, 0))) + polylog(2, 1 / x)
        rhs = pi ** 2 / 3 - log(x) ** 2 / 2
        d = fabs(lhs - rhs)
        if d > worst3:
            worst3, at3 = d, x
    gates.append({
        "gate": "G3",
        "claim": "THE REDUCTION. Given G1/G2, the inversion leg is equivalent to the REAL "
                 "identity Re Li2(x) + Li2(1/x) = pi^2/3 - (1/2)log^2(x) for x > 1 -- in which "
                 "1/x lies in (0,1), where the series converges and cLiTwo_ofReal already "
                 "bridges. No boundary value, no cut-crossing, no new analytic infrastructure. "
                 "This is a different and much smaller problem than the one qou-invr recorded",
        "n_points": 200, "worst": nstr(worst3, 10),
        "at_x": nstr(at3, 12) if at3 is not None else None,
        "pass": bool(worst3 < tol),
    })

    # ---- G4: which boundary value Lean's integral picks (I guessed wrong) ---
    rows4 = []
    ok4 = True
    for x in [mpf("1.5"), w1, mpf(3)]:
        I = lean_integral(x)
        up, dn = polylog(2, mpc(x, eps)), polylog(2, mpc(x, -eps))
        rows4.append({
            "x": nstr(x, 14), "lean_integral": nstr(I, 16),
            "dist_to_upper": nstr(fabs(I - up), 8),
            "dist_to_lower": nstr(fabs(I - dn), 8),
            "picks": "lower (x - i0)" if fabs(I - dn) < fabs(I - up) else "upper (x + i0)",
            "re_matches_both": bool(fabs(re(I) - re(up)) < tol and fabs(re(I) - re(dn)) < tol),
        })
        ok4 = ok4 and fabs(re(I) - re(up)) < tol and fabs(re(I) - re(dn)) < tol
    gates.append({
        "gate": "G4",
        "claim": "WHICH SIDE Lean's own definition lands on, measured rather than reasoned. "
                 "cLiTwoExt y = -int_0^1 log(1 - y t)/t dt with the principal branch, at real "
                 "x > 1, equals Li2(x - i0) -- the LOWER boundary value. I PREDICTED THE UPPER "
                 "ONE before measuring, from arg(negative real) = +pi, and was wrong. Recorded "
                 "because branch signs are exactly what this lane has repeatedly got wrong. "
                 "The conclusion does not depend on it: the REAL PART agrees with both sides",
        "per_point": rows4,
        "prediction_was": "upper (x + i0)", "measured": "lower (x - i0)",
        "conclusion_depends_on_side": False,
        "pass": bool(ok4),
    })

    # ---- G5: the target identity, and at the one argument that needs it ----
    worst5 = mpf(0)
    at5 = None
    for i in range(1, 201):
        x = 1 + mpf(i) / 20
        d = fabs(extend_gt1(x) - ReL(x))
        if d > worst5:
            worst5, at5 = d, x
    gates.append({
        "gate": "G5",
        "claim": "the target itself: extend(pi^2/6, rogersL)(x) = Re L(x) for x > 1, 200 points. "
                 "And at w_1 = 1/(1-x_root) = 2.24698 -- the ONE argument of the six that "
                 "`extended_sum` uses in this regime, and the whole of what qou-rstq item 4 "
                 "still lacks",
        "n_points": 200, "worst": nstr(worst5, 10),
        "at_x": nstr(at5, 12) if at5 is not None else None,
        "w1": nstr(w1, 20),
        "extend_at_w1": nstr(extend_gt1(w1), 22),
        "ReL_at_w1": nstr(ReL(w1), 22),
        "difference_at_w1": nstr(fabs(extend_gt1(w1) - ReL(w1)), 8),
        "pass": bool(worst5 < tol and fabs(extend_gt1(w1) - ReL(w1)) < tol),
    })

    # ---- G6: what is STILL missing, so this is not read as a closure -------
    gates.append({
        "gate": "G6",
        "claim": "WHAT REMAINS, named so this probe is not misread as closing qou-invr. Two "
                 "things, both smaller than a boundary-value theory but neither free: (1) "
                 "INTEGRABILITY of the defining integral at x > 1 -- Lean's "
                 "intervalIntegrable_log_one_sub_div_of_notCut assumes notCut, which FAILS "
                 "here, so cLiTwoExt at x > 1 is currently a Lean `integral` with no proof its "
                 "integrand is integrable, and an unproved-integrable integral is the junk "
                 "value 0. The singularity at t = 1/x is logarithmic, hence integrable, but "
                 "that needs proving. (2) the real identity of G3. Item 4 is NOT closed",
        "still_needed": [
            "IntervalIntegrable (fun t => log(1 - x*t)/t) volume 0 1, for real x > 1",
            "Re Li2(x) + Li2(1/x) = pi^2/3 - (1/2) log^2 x, for real x > 1",
        ],
        "no_longer_needed": "a boundary value of Li2 obtained from off the cut; the real part "
                            "is continuous across it (G1/G2), so there is nothing to take a "
                            "limit of",
        "pass": True,
    })

    out = {
        "probe": "qbeta_5two_route35_inversion_shape",
        "bean": "qou-invr", "cross_ref": "qou-rstq", "dps": mp.dps,
        "attack_vector": "A2 -- is Re Li2 continuous across the cut? YES",
        "gates": gates,
        "verdict": {
            "measured": "Li2's jump across [1,inf) is exactly 2*pi*i*log(x), purely imaginary, "
                        "so Re Li2 -- and Re of the full Rogers L -- is CONTINUOUS across the "
                        "cut. Lean's integral definition lands on the lower boundary value, "
                        "but its real part agrees with both sides.",
            "changes": "the inversion leg is NOT a boundary-value problem. It reduces to one "
                       "real identity, Re Li2(x) + Li2(1/x) = pi^2/3 - (1/2)log^2 x, whose "
                       "partner argument 1/x lies safely in (0,1).",
            "still_open": "integrability of the defining integral at x > 1 (logarithmic "
                          "singularity at t = 1/x -- integrable, but Lean's existing lemma "
                          "assumes notCut and does not apply), and the real identity itself. "
                          "qou-rstq item 4 remains open at exactly one argument, w_1 = 2.24698.",
            "prediction_falsified": "I expected the integral to pick the UPPER boundary value; "
                                    "it picks the lower. Immaterial to the conclusion, recorded "
                                    "anyway.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route35-inversion-shape.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("the inversion leg is a REAL identity, not a boundary-value problem. "
                         "Two named things remain; item 4 is not closed."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
