#!/usr/bin/env python3
"""Route 57 -- the 5_2 conjugate pair is ON the branch cut, at the plastic number;
so what is missing is boundary continuity, not a region.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Follows Route 56,
which proved the FLATTENED pentagon (Neumann's `R(z;p,q)`) has vanishing
derivative under regularity alone, and left exactly one thing owed: a connected
regular region joining the real square to `(y_1, conj y_1)`.

THE ANSWER: THERE IS NO SUCH REGION, AND THE REASON IS EXACT
------------------------------------------------------------
From `y_1 y_2 y_3 = 1`, in one line,

    y_3 * (1 - y_1 y_2) = y_3 - 1        so   1 - y_1 conj(y_1) = (y_3 - 1)/y_3

and `y_3 = 0.4301597...` lies in (0,1), so that is a NEGATIVE REAL:
`-1.3247179...`, the negated plastic number -- Route 55's map `y -> 1 - 1/y`
surfacing a third time. A negative real is off `slitPlane`, so `log(1 - xy)` sits
exactly on its branch cut and `PentagonRegular` FAILS at the pair `Vol(5_2)`
needs. Proved in Lean:
`FiveTwoFlattenedPentagon.not_pentagonRegular_of_prod_eq_one`.

WHY THAT IS BETTER NEWS THAN IT SOUNDS
--------------------------------------
On the boundary is not outside. Two measurements sharpen it:

* G2 -- the straight segment from ANY real `a` in (0,1) to `y_1`, with
  `conj(y_1)` fixed, is regular at every interior point. Only `t = 1` fails, and
  only in the single argument `1 - w y`.
* G3 -- the approach is from the UPPER half-plane:
  `Im(1 - w conj(y_1)) = a(1-t) Im(y_1) > 0`, decreasing to 0. That is the side on
  which the principal `Complex.log` is continuous (`arg` in `(-pi, pi]`).

So the remaining gap is a **boundary-continuity** argument at one point, not a
search for a region. That is a different and much smaller problem than the one
Route 56 left open, and this probe exists to say so precisely rather than to
claim the gap is closed. **It is not closed.**

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (conj, fabs, im, linspace, log, mp, mpf, nstr, pi, polylog,
                    polyroots, re)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

SADDLE = [1, -2, 3, -1]


def pentagon_args(w, y):
    d = 1 - w * y
    return {"w": w, "a3": (1 - w) / d, "a4": d, "a5": (1 - y) / d}


def off_both_cuts(z, tol):
    if fabs(im(z)) > tol:
        return True
    return bool(0 < re(z) < 1)


def main() -> int:
    set_compute_dps()
    tol = mpf(10) ** -25
    gates = []

    roots = polyroots(SADDLE, maxsteps=1200, extraprec=5000)
    y3 = re([r for r in roots if fabs(im(r)) < mpf(10) ** -35][0])
    y1 = [r for r in roots if im(r) > mpf(10) ** -35][0]
    y2 = conj(y1)
    rho = re([r for r in polyroots([1, 0, -1, -1], maxsteps=1200, extraprec=5000)
              if fabs(im(r)) < mpf(10) ** -35][0])

    # ---- G1: the pair is ON the cut, exactly -------------------------------
    a4 = 1 - y1 * y2
    gates.append({
        "gate": "G1",
        "claim": "THE ANSWER TO ROUTE 56'S OPEN ITEM, and it is a negative. From y1*y2*y3 = 1, "
                 "y3*(1 - y1*y2) = y3 - 1, so 1 - y1*conj(y1) = (y3-1)/y3 -- and y3 = 0.43016 in "
                 "(0,1) makes that a NEGATIVE REAL, namely minus the plastic number. A negative "
                 "real is off slitPlane, so log(1-xy) sits exactly on its branch cut and "
                 "PentagonRegular fails at the pair Vol(5_2) needs. No region reaches it because "
                 "the configuration is on the boundary of the domain",
        "one_minus_y1_y2": nstr(a4, 25),
        "predicted_(y3-1)/y3": nstr((y3 - 1) / y3, 25),
        "residual_vs_prediction": nstr(fabs(a4 - (y3 - 1) / y3), 8),
        "minus_plastic_rho": nstr(-rho, 25),
        "residual_vs_minus_rho": nstr(fabs(a4 + rho), 8),
        "imaginary_part": nstr(fabs(im(a4)), 8),
        "is_negative_real": bool(fabs(im(a4)) < tol and re(a4) < 0),
        "pass": bool(fabs(a4 - (y3 - 1) / y3) < tol and fabs(a4 + rho) < tol
                     and fabs(im(a4)) < tol and re(a4) < 0),
    })

    # ---- G2: only the endpoint fails, and only in one argument -------------
    per_a = []
    for a in [mpf("0.1"), mpf("0.3"), y3, mpf("0.8"), mpf("0.95")]:
        interior_bad, endpoint_bad = [], []
        for t in linspace(0, 1, 1501):
            w = a + t * (y1 - a)
            bad = [k for k, z in pentagon_args(w, y2).items()
                   if not off_both_cuts(z, tol)]
            if bad:
                (endpoint_bad if t == 1 else interior_bad).append((nstr(t, 6), bad))
        per_a.append({"a": nstr(a, 10),
                      "interior_failures": len(interior_bad),
                      "endpoint_failing_arguments": endpoint_bad[0][1] if endpoint_bad else []})
    gates.append({
        "gate": "G2",
        "claim": "on the boundary is not outside. The straight segment from ANY real a in (0,1) "
                 "to y_1, with conj(y_1) fixed, is regular at EVERY interior point -- 1500 "
                 "samples each, five values of a, zero interior failures. Only t = 1 fails, and "
                 "only in the single argument 1 - w*y. (A sampled sweep cannot prove the absence "
                 "of an interior failure; it is reported as what it is)",
        "sweeps": per_a,
        "samples_per_sweep": 1501,
        "sampling_caveat": "interior regularity is sampled, not certified",
        "pass": bool(all(p["interior_failures"] == 0 for p in per_a)
                     and all(p["endpoint_failing_arguments"] == ["a4"] for p in per_a)),
    })

    # ---- G3: the approach is from the continuous side ----------------------
    a = mpf("0.3")
    approach = []
    for t in [mpf("0.5"), mpf("0.9"), mpf("0.99"), mpf("0.9999"), mpf("0.999999")]:
        w = a + t * (y1 - a)
        z = 1 - w * y2
        approach.append({"t": nstr(t, 8), "one_minus_wy": nstr(z, 16),
                         "im": nstr(im(z), 8), "im_positive": bool(im(z) > 0)})
    gates.append({
        "gate": "G3",
        "claim": "and the approach is from the CONTINUOUS side. Im(1 - w*conj(y1)) = "
                 "a*(1-t)*Im(y1) > 0 all along, decreasing to 0 -- the upper half-plane, which is "
                 "where the principal Complex.log (arg in (-pi, pi]) is continuous at a negative "
                 "real. So what is owed is a BOUNDARY-CONTINUITY argument at one point, not a "
                 "search for a region: a different and much smaller problem than Route 56 left "
                 "open. It is NOT closed here",
        "approach": approach,
        "pass": bool(all(p["im_positive"] for p in approach)),
    })

    # ---- G4: the exceptional structure at the pair -------------------------
    args = pentagon_args(y1, y2)
    a3, a5 = args["a3"], args["a5"]
    gates.append({
        "gate": "G4",
        "claim": "the exceptional structure at the pair, all equivalent to the cubic itself: "
                 "(1-a)(1-b) = (1-ab)^2 for any two roots, so a5 = 1/a3; here additionally "
                 "a5 = conj(a3), hence |a3| = 1 -- the two composite arguments sit on the UNIT "
                 "CIRCLE. Verified symbolically by Groebner reduction against a+b+c=2, "
                 "ab+ac+bc=3, abc=1 before being measured",
        "a3": nstr(a3, 22),
        "a5": nstr(a5, 22),
        "a5_minus_inv_a3": nstr(fabs(a5 - 1 / a3), 8),
        "a5_minus_conj_a3": nstr(fabs(a5 - conj(a3)), 8),
        "abs_a3_minus_one": nstr(fabs(fabs(a3) - 1), 8),
        "pass": bool(fabs(a5 - 1 / a3) < tol and fabs(a5 - conj(a3)) < tol
                     and fabs(fabs(a3) - 1) < tol),
    })

    # ---- G5: target unmoved -------------------------------------------------
    A = re(sum(polylog(2, z) for z in roots))
    gates.append({
        "gate": "G5",
        "claim": "the target is unmoved. G1 is a negative -- the pair is on the cut, so Route "
                 "56's region does not exist. G2 and G3 say the residue is boundary continuity "
                 "at a single point, which is smaller but is not done. A = sum Li2(y_j) still "
                 "has no proof",
        "A": nstr(A, 30),
        "boundary_continuity_argument_supplied": False,
        "pass": bool(fabs(A - mpf("0.9717306814686482591277741699")) < mpf(10) ** -25),
    })

    out = {
        "probe": "qbeta_5two_route57_on_the_cut",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": "Route 56 (the flattened pentagon)",
        "lean": "QOU/QBeta/FiveTwoFlattenedPentagon.lean -- one_sub_mul_of_prod_eq_one, "
                "not_pentagonRegular_of_prod_eq_one",
        "gates": gates,
        "verdict": {
            "negative": "1 - y_1*conj(y_1) = (y_3-1)/y_3 is a NEGATIVE REAL (minus the plastic "
                        "number), so the 5_2 conjugate pair lies ON the branch cut and "
                        "PentagonRegular fails there. Route 56's region does not exist.",
            "sharpening": "but only the endpoint fails, only in one argument, and the approach is "
                          "from the upper half-plane where the principal log is continuous. The "
                          "residue is boundary continuity at one point.",
            "not_done": "no boundary-continuity argument is supplied here.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route57-on-the-cut.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the 5_2 conjugate pair is ON the branch cut -- 1 - y_1*conj(y_1) = (y_3-1)/y_3 is minus "
        "the plastic number -- so Route 56's region does not exist. But only the endpoint fails, "
        "only in one argument, and the approach is from the side where the principal log is "
        "continuous, so the residue is boundary continuity at a single point. That argument is "
        "NOT supplied. The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
