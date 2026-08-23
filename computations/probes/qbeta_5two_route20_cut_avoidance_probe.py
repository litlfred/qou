#!/usr/bin/env python3
"""Route 20 -- the branch-pinning hypothesis, and WHY this lane keeps seeing spurious 2*pi.

Bean `qou-trns`. Pairs with the Lean lemma
`QOU/Archimedean/BranchIntegerPinning.lean`:

    eq_zero_of_continuousOn_of_exp_eq_one
      (hx : x in Icc a b) (hcont : ContinuousOn F (Icc a b))
      (hexp : forall y in Icc a b, Complex.exp (F y) = 1) (h0 : F a = 0) : F x = 0

instantiated at  F(phi) := Sum_j Log(1 - e^{i phi} y_j) - i*phi  on [0, pi].

WHY MEASURE THE HYPOTHESIS AND NOT THE CONCLUSION
-------------------------------------------------
Route 19 established branch integer 0 by measuring the CONCLUSION: over a grid,
the sum of logs never jumped. That is evidence for "the grid saw no jump", which
is not "there is no jump" -- and this lane has already been burned by exactly
that inference once, when `min |disc| = 0.348` (a 360-point grid minimum) was
recorded as a fact about a quantity whose true minimum is 0.

The Lean lemma moves the burden. It derives branch integer 0 from three inputs,
two of which are already theorems:

    exp(F) = 1     <- Vieta, `prod_one_sub_x_mul` (Lean, sorry-free, #4658)
    F(0)   = 0     <- the base point x = 1
    F continuous   <- THE ONLY OPEN INPUT

So the thing worth measuring is the open hypothesis.

WHAT THE FIRST RUN OF THIS PROBE FOUND
--------------------------------------
The first version of G3 tested the obvious sufficient condition -- "no factor
`1 - x*y_j` ever touches the cut (-inf, 0]" -- and it FAILED, with margin 9.3e-43
at phi/pi = 1.0, unmoved by a 1e4 refinement. That is not a grid artefact and not
a tolerance problem. **At the endpoint x = -1 a factor sits exactly on the cut:**

    y_1(-1) = -w_1  =>  1 - x*y_1 = 1 + y_1(-1)... = -(w_1 - 1) = -1.2469796...

where w_1 = 2.2469796... is the LARGEST ROOT OF THE WATSON CUBIC
w^3 - 2w^2 - w + 1 -- the same cubic that generates the level-7 ladder. And
`x = -1` is on the cut too. So the transport arc ends on the branch cut in two
independent ways, and it is structural, not bad luck.

**This is the cause of the recurring false alarm.** `qou-trns` records three
separate occasions on which a principal-vs-continuous `Log` produced a spurious
2*pi and calls it "the single most reliable source of false alarms in this work".
It is the endpoint. G6 below makes the mechanism explicit and falsifiable.

DOES THE LEMMA STILL APPLY? YES -- AND THE MARGIN OF SAFETY IS A CONVENTION
---------------------------------------------------------------------------
Continuity of F does NOT require avoiding the cut; it requires not CROSSING it.
The contact here is transversal (the margin is exactly w_1*(pi - phi), G3) and
one-sided: as phi rises to pi the factor approaches -1.2469796 from ABOVE
(Im > 0), so arg -> +pi, and the principal branch's value ON the cut is also
+pi. Left-limit meets value, so F is continuous on [0, pi] and `hcont` holds.

Traverse the same arc downward instead (phi: 0 -> -pi) and the factor arrives
from BELOW, arg -> -pi, while principal Log on the cut still returns +pi: a
genuine 2*pi*i discontinuity at the endpoint. G6 measures both directions. So
the transport's ORIENTATION is load-bearing, and it is load-bearing only because
of where the principal branch is defined to sit -- which is worth saying out
loud rather than relying on.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import acos, exp, fabs, im, log, mp, mpf, nstr, pi, polyroots, re, sqrt
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def phi_branch_point():
    """The branch point, computed at working precision rather than hardcoded.

    Square-root branch point: root separation near it grows like sqrt|dphi|, so a
    truncated constant leaves the roots far further apart than its digit count
    suggests. See the G4 note in Route 19."""
    u0 = [re(r) for r in polyroots([1, -6, 7, 6, -31], maxsteps=400, extraprec=400)
          if fabs(im(r)) < mpf(10) ** -30 and mpf(-2) < re(r) < mpf(2)][0]
    return acos(u0 / 2)


def watson_w1():
    """The largest root of w^3 - 2w^2 - w + 1 -- the level-7 ladder's own cubic."""
    return max(re(r) for r in polyroots([1, -2, -1, 1], maxsteps=400, extraprec=400)
               if fabs(im(r)) < mpf(10) ** -30)


def roots_x(x):
    """The three y-branches of the GGM deformed 5_2 curve at x."""
    return list(polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                          maxsteps=500, extraprec=1000))


def dist_to_cut(z):
    """Distance from z to the principal-log branch cut (-inf, 0].

    Re z <= 0: nearest point is the foot of the perpendicular, distance |Im z|.
    Re z > 0:  nearest point is the endpoint 0, distance |z|."""
    u, v = re(z), im(z)
    return fabs(v) if u <= 0 else sqrt(u ** 2 + v ** 2)


def margin_at(ph, which):
    """min_j dist(factor_j, cut) at phi, for `which` in {'A','B'}."""
    z = exp(1j * ph)
    ys = roots_x(z)
    facs = [1 - z * y for y in ys] if which == "A" else [1 - y / z for y in ys]
    return min(dist_to_cut(f) for f in facs)


def F_at(z, ph):
    """F = Sum_j Log(1 - x*y_j) - i*phi, principal branch throughout.

    `z` is passed separately from `ph` so the endpoint can be evaluated at
    EXACTLY x = -1 rather than at exp(1j*pi), which mpmath returns with a
    ~1e-43 positive imaginary part. That rounding artefact would otherwise be
    doing the work of the branch convention, and G6 would be testing rounding."""
    return sum(log(1 - z * y) for y in roots_x(z)) - 1j * ph


def main() -> int:
    set_compute_dps()
    TOL = mpf(10) ** -30
    gates = []
    ph0 = phi_branch_point()
    w1 = watson_w1()

    # ---- G1: exp(F) = 1 -- the lemma's `hexp` ------------------------------
    worst1 = mpf(0)
    for i in range(0, 41):
        ph = pi * i / 40
        z = mpf(-1) if i == 40 else exp(1j * ph)
        ys = roots_x(z)
        prodA = (1 - z * ys[0]) * (1 - z * ys[1]) * (1 - z * ys[2])
        prodB = (1 - ys[0] / z) * (1 - ys[1] / z) * (1 - ys[2] / z)
        worst1 = max(worst1, fabs(prodA - z), fabs(prodB - 1 / z))
    gates.append({
        "gate": "G1",
        "claim": "hexp: exp(F) = prod_j(1 - x*y_j)/x = 1 on the arc (and prod_j(1 - y_j/x) "
                 "= 1/x) -- ALREADY Lean-proved as prod_one_sub_x_mul / prod_x_sub; measured "
                 "only to confirm the instantiation is the one the lemma expects",
        "n_points": 41, "worst": nstr(worst1, 8), "pass": bool(worst1 < TOL),
    })

    # ---- G2: F(0) = 0 -- the lemma's `h0` ----------------------------------
    F0 = sum(log(1 - y) for y in roots_x(mpf(1)))
    gates.append({
        "gate": "G2",
        "claim": "h0: F(0) = Sum_j Log(1 - y_j) = 0 at the base point x = 1 -- this is what "
                 "selects the integer 0 rather than merely showing it is constant",
        "value": nstr(fabs(F0), 8), "pass": bool(fabs(F0) < TOL),
    })

    # ---- G3: the ONLY cut contact is the endpoint, and it is transversal ----
    # Interior contact, or tangential contact anywhere, would break `hcont`.
    # Linear (transversal) contact at a single endpoint does not.
    # (a) away from the endpoint the margin has a genuine interior minimum, and it
    #     is nowhere near zero -- so no interior cut crossing.
    M = 800
    hi = pi - mpf("0.2")
    prof = [(margin_at(hi * i / M, "A"), hi * i / M) for i in range(M + 1)]
    mInt, argInt = min(prof, key=lambda t: t[0])
    # (b) near the endpoint the margin collapses LINEARLY, at rate exactly w_1.
    ladder = []
    for d in ["0.05", "0.01", "0.001", "0.0001"]:
        hiD, MD = pi - mpf(d), 600
        mA = min(margin_at(hiD * i / MD, "A") for i in range(MD + 1))
        ladder.append({"delta": d, "min_margin": nstr(mA, 8),
                       "ratio_to_w1_delta": nstr(mA / (w1 * mpf(d)), 8)})
    ratios = [mpf(e["ratio_to_w1_delta"]) for e in ladder]
    gates.append({
        "gate": "G3",
        "claim": "the ONLY contact with the cut on the whole arc is at the endpoint phi = pi, "
                 "and it is TRANSVERSAL. (a) On [0, pi-0.2] the margin has an interior minimum "
                 "of 0.337 at phi/pi = 0.542 -- a real local minimum, bounded well away from "
                 "zero, so nothing crosses the cut inside. (b) On [0, pi-delta] for delta <= "
                 "0.05 the minimum moves to the right endpoint and equals w_1*delta, ratio -> 1 "
                 "over 3 further orders of magnitude: linear collapse, not tangential",
        "w1_largest_root_of_watson_cubic": nstr(w1, 20),
        "interior_min": nstr(mInt, 8), "interior_argmin_over_pi": nstr(argInt / pi, 8),
        "endpoint_ladder": ladder,
        "pass": bool(mInt > mpf("0.3")
                     and all(mpf("0.99") < r < mpf("1.01") for r in ratios)),
    })

    # ---- G4: the touching factor is exactly -(w_1 - 1) ----------------------
    zc = mpf(-1)
    facs_end = sorted((1 - zc * y for y in roots_x(zc)), key=lambda f: re(f))
    dev = fabs(facs_end[0] - (1 - w1))
    gates.append({
        "gate": "G4",
        "claim": "the factor that lands on the cut is exactly 1 - w_1 = -(w_1 - 1) = "
                 "-1.2469796..., with w_1 the largest root of the level-7 ladder's own cubic "
                 "w^3 - 2w^2 - w + 1. The arc's endpoint sitting on the cut is structural, "
                 "not coincidental -- and x = -1 is on the cut as well",
        "touching_factor": nstr(facs_end[0], 20), "one_minus_w1": nstr(1 - w1, 20),
        "deviation": nstr(dev, 8), "pass": bool(dev < TOL),
    })

    # ---- G5: the collision is invisible to the cut margin -------------------
    near = [margin_at(ph0 + mpf(d), "A") for d in
            ["-0.001", "-0.0001", "0", "0.0001", "0.001"]]
    gates.append({
        "gate": "G5",
        "claim": "the branch point is invisible to the cut margin -- margin ~0.77 at phi_0, "
                 "nowhere near zero. The cut condition and the collision condition are "
                 "independent, which is exactly why the symmetric repair survives a branch "
                 "point that killed the per-root argument",
        "phi_0_over_pi": nstr(ph0 / pi, 12),
        "margins_near_phi0": [nstr(v, 8) for v in near],
        "pass": bool(min(near) > mpf("0.5")),
    })

    # ---- G6: the mechanism of the recurring spurious 2*pi -------------------
    # Upward through the endpoint the principal branch is continuous; downward it
    # is not. Same arc, same factor, opposite orientation.
    Fend = F_at(zc, pi)
    up = [fabs(F_at(exp(1j * (pi - mpf(e))), pi - mpf(e)) - Fend)
          for e in ["0.01", "0.0001", "0.000001"]]
    # downward: phi -> -pi, where the factor arrives from Im < 0
    Fend_dn = F_at(zc, -pi)
    dn = [fabs(F_at(exp(-1j * (pi - mpf(e))), -(pi - mpf(e))) - Fend_dn)
          for e in ["0.01", "0.0001", "0.000001"]]
    gates.append({
        "gate": "G6",
        "claim": "ORIENTATION IS LOAD-BEARING, and this is the mechanism behind the three "
                 "spurious 2*pi's recorded on qou-trns. Rising to phi = pi the factor reaches "
                 "-(w_1-1) from ABOVE, arg -> +pi, matching the principal branch's value ON "
                 "the cut: F is continuous, hcont holds. Descending to phi = -pi it arrives "
                 "from BELOW, arg -> -pi, while principal Log still returns +pi: a genuine "
                 "2*pi*i discontinuity at the endpoint",
        "upward_|F(pi-eps) - F(pi)|": [nstr(v, 8) for v in up],
        "downward_|F(-pi+eps) - F(-pi)|": [nstr(v, 8) for v in dn],
        "two_pi": nstr(2 * pi, 8),
        "pass": bool(max(up) < mpf("0.05") and min(dn) > mpf("6.0")),
    })

    # ---- G7: the conclusion (the lemma's OUTPUT, not new evidence) ----------
    worst7 = mpf(0)
    for i in range(0, 41):
        ph = pi * i / 40
        z = mpf(-1) if i == 40 else exp(1j * ph)
        worst7 = max(worst7, fabs(F_at(z, ph)))
    gates.append({
        "gate": "G7",
        "claim": "conclusion (this is what the lemma OUTPUTS, recorded so the instantiation "
                 "is seen to close): F = Sum_j Log(1 - x*y_j) - i*phi vanishes on the arc -- "
                 "branch integer 0, endpoint included",
        "n_points": 41, "worst": nstr(worst7, 8), "pass": bool(worst7 < TOL),
    })

    out = {
        "probe": "qbeta_5two_route20_cut_avoidance",
        "bean": "qou-trns", "parent_bean": "qou-0yqu", "dps": mp.dps,
        "pairs_with_lean": "QOU/Archimedean/BranchIntegerPinning.lean "
                           "(eq_zero_of_continuousOn_of_exp_eq_one)",
        "gates": gates,
        "verdict": {
            "outcome": "The branch-integer step is now a Lean theorem with its hypotheses "
                       "separated: exp(F)=1 and F(0)=0 are already theorems (Vieta), and the "
                       "only open input is continuity of F on [0, pi].",
            "the_finding": "the transport arc ENDS ON THE BRANCH CUT, twice over: x = -1 is on "
                           "it, and the factor 1 - x*y_1 equals -(w_1 - 1) = -1.2469796 there, "
                           "with w_1 the largest root of the level-7 ladder's cubic. The first "
                           "version of this probe tested 'no factor touches the cut' and failed "
                           "at 9.3e-43; the condition was too strong, but the failure was real "
                           "information.",
            "why_hcont_still_holds": "continuity forbids CROSSING the cut, not touching it. The "
                                     "contact is transversal (margin = w_1*(pi-phi), G3) and "
                                     "one-sided from above, and the principal branch's value on "
                                     "the cut is the limit from above. So F is continuous on "
                                     "[0, pi] and the lemma applies.",
            "cause_of_the_recurring_2pi": "G6. Rising through the endpoint the principal branch "
                                          "is continuous; descending through it, it jumps by "
                                          "2*pi*i. qou-trns records three spurious 2*pi's and "
                                          "calls them the most reliable false alarm in this "
                                          "work; this is their mechanism, and it is structural.",
            "still_not_proved": "hcont is MEASURED, not proved. Proving it means showing from "
                                "the curve that no factor 1 - x*y_j meets (-inf, 0] for phi in "
                                "[0, pi), a real-algebraic statement, plus the one-sided limit "
                                "at the endpoint. NOT written. Until it is, hcont is an "
                                "assumption and the transport is open.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route20-cut-avoidance.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: pinning is a Lean theorem; the arc ends ON the cut, and orientation saves it.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
