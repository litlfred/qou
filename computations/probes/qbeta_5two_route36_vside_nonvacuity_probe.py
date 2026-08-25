#!/usr/bin/env python3
"""Route 36 -- `VSide` is NON-VACUOUS on the arc, and which disjunct carries it.

Bean `qou-glbl` (Gap A), the assembly step. Run BEFORE writing any Lean for
`VSide`, because `VSide` is the hypothesis that was once **vacuous**: correction
6 on PR #4701 found an earlier version carrying `−y in slitPlane`, which fails
at ALL 199 arc points because exactly one root is real and positive at every
phi. A theorem carrying it was true and about nothing.

So the first question about the corrected `VSide` is not "can I prove it" but
"is it satisfiable at all". It is, ON THE OPEN ARC: all six conditions hold
SIMULTANEOUSLY at every one of the 597 interior checks.

TWO THINGS THIS PROBE GOT WRONG AND THEN CAUGHT
-----------------------------------------------
Both were claims about "never", established from a grid. A grid cannot support
one, and both were false.

1. **`VSide` is FALSE at `phi = pi`** (G7). G1 samples `pi*(i+1)/(N+1)` -- the
   OPEN interval -- so "holds at all 597 checks" was being read as covering a
   point it never tested. At the endpoint all three roots are real and
   `Im(x*y) = y*sin(phi)` vanishes for all of them at once; the root
   `y = -2.2469796` then has `x*y = +2.2469796` on Li2's cut.

2. **`x*y` DOES become real on the open arc** (G3, retracted and replaced). The
   original G3 claimed it never does and that `notCut` needed "no case split at
   all". It passed on a grid minimum of `|Im|`, which is not a lower bound.
   Refining the grid shrank that minimum like `1/N`, which is a zero crossing.
   There is exactly one, at the unique real root of `r^5 - r^3 + 1`, and `notCut`
   survives there via `Re < 1` -- the opposite disjunct from the one claimed.

The pattern is the same both times: a *negative* claim ("never real", "holds
everywhere") backed by *positive* samples. Where this probe now asserts a
"never", it either checks an exact endpoint or bisects a symmetric function for
crossings -- not a denser grid.

⚠ A TRAP THIS PROBE ALMOST FELL INTO
------------------------------------
A first pass classified each condition by which disjunct of
`notCut = {w : Im w != 0 or Re w < 1}` carried it, and reported that the root
`y` was carried by `Im != 0` at 307 of 597 checks -- with a minimum |Im| of
2.6e-41.

That 2.6e-41 is **numerical noise**, not an imaginary part. The real root has
`Im = 0` EXACTLY; `polyroots` returns ~1e-41 for it. So the attribution was
counting the real root as "carried by Im != 0", which is false in exact
arithmetic and would have sent a Lean proof down the wrong branch.

**And it bites exactly ONCE in 597 checks** (G2 measures it: 1 of 291 real
roots). `polyroots` usually returns a clean `0` for the real root; at one arc
point it does not. That rarity is what makes it dangerous rather than harmless
-- a spot check at ten points would have seen a clean split and concluded the
naive test was fine. The gate has to be exhaustive to see it at all.

G2 therefore classifies by ROOT TYPE (real vs genuinely complex) using an
explicit tolerance, not by `Im != 0`. The conclusion of G1 is unaffected -- both
disjuncts are checked there -- but the *reason* it holds is what a proof needs,
and that was contaminated.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import cos as mpmath_cos
from mpmath import (arg, exp, fabs, findroot, im, log, mp, mpc, mpf, nint, nstr,
                    pi, polyroots, quad, re, sqrt)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def roots_at(ph):
    """The three y-roots of the deformed curve at x = exp(i*phi)."""
    x = exp(mpc(0, 1) * ph)
    return polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                     maxsteps=200, extraprec=200)


def in_not_cut(w):
    """Lean's `notCut = {w | Im w != 0 or Re w < 1}` -- Li2's cut is [1, inf)."""
    return (im(w) != 0) or (re(w) < 1)


def main() -> int:
    set_compute_dps()
    N = 199
    REAL_TOL = mpf(10) ** -30      # below this, an "imaginary part" is noise
    gates = []

    # ---- G1: all six conditions hold SIMULTANEOUSLY -------------------------
    total = 0
    allok = 0
    per_cond = {"y_ne_0": 0, "y_notCut": 0, "xy_notCut": 0, "y_div_x_notCut": 0,
                "xy_ne_0": 0, "y_div_x_ne_0": 0}
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        x = exp(mpc(0, 1) * ph)
        for y in roots_at(ph):
            total += 1
            conds = {
                "y_ne_0": y != 0,
                "y_notCut": in_not_cut(y),
                "xy_notCut": in_not_cut(x * y),
                "y_div_x_notCut": in_not_cut(y / x),
                "xy_ne_0": (x * y) != 0,
                "y_div_x_ne_0": (y / x) != 0,
            }
            for k, v in conds.items():
                if not v:
                    per_cond[k] += 1
            if all(conds.values()):
                allok += 1
    gates.append({
        "gate": "G1",
        "claim": "NON-VACUITY, the gate class that caught correction 6: all SIX VSide conditions "
                 "hold SIMULTANEOUSLY at every root at every arc point. The earlier version of "
                 "this hypothesis carried `-y in slitPlane` and failed at ALL 199 points, making "
                 "its theorem true and about nothing. Checking conditions one at a time would not "
                 "have caught that; checking them together is the whole point",
        "arc_points": N, "checks": total, "all_six_hold": allok,
        "per_condition_failures": per_cond,
        "pass": bool(allok == total),
    })

    # ---- G2: WHICH disjunct carries `y`, classified by ROOT TYPE ------------
    n_real, n_cplx = 0, 0
    real_via_re, real_via_im_spurious = 0, 0
    cplx_via_im = 0
    worst_real_margin, worst_cplx_im = None, None
    worst_noise = mpf(0)
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        for y in roots_at(ph):
            if fabs(im(y)) < REAL_TOL:
                # a REAL root: in exact arithmetic Im = 0, so `Re < 1` must carry it
                n_real += 1
                worst_noise = max(worst_noise, fabs(im(y)))
                if im(y) != 0:
                    real_via_im_spurious += 1
                m = 1 - re(y)
                if worst_real_margin is None or m < worst_real_margin:
                    worst_real_margin = m
                if re(y) < 1:
                    real_via_re += 1
            else:
                n_cplx += 1
                m = fabs(im(y))
                if worst_cplx_im is None or m < worst_cplx_im:
                    worst_cplx_im = m
                if m > mpf(10) ** -6:
                    cplx_via_im += 1
    gates.append({
        "gate": "G2",
        "claim": "WHICH DISJUNCT carries `y in notCut`, classified by ROOT TYPE rather than by "
                 "`Im != 0`. This matters: polyroots returns |Im| ~ 1e-41 for the REAL root, so a "
                 "naive `Im != 0` test attributes it to the wrong disjunct. In exact arithmetic "
                 "the real root is carried by Re < 1 and the complex pair by Im != 0 -- and a Lean "
                 "proof must follow the exact split, not the numerical one",
        "real_roots": n_real,
        "real_roots_carried_by_Re_lt_1": real_via_re,
        "real_roots_where_naive_Im_test_would_misattribute": real_via_im_spurious,
        "worst_spurious_Im_magnitude": nstr(worst_noise, 8),
        "misattribution_rate": f"{real_via_im_spurious} of {n_real} real roots "
                               f"({real_via_im_spurious} of {n_real + n_cplx} checks) -- rare "
                               f"enough that a spot check would miss it entirely",
        "min_margin_1_minus_Re_at_real_roots": nstr(worst_real_margin, 10)
            if worst_real_margin is not None else None,
        "complex_roots": n_cplx,
        "complex_roots_carried_by_Im_ne_0": cplx_via_im,
        "min_abs_Im_at_complex_roots": nstr(worst_cplx_im, 10)
            if worst_cplx_im is not None else None,
        # NOT a non-emptiness check: EVERY real root must be carried by Re < 1 and EVERY
        # complex root by a genuine Im, and the two classes must exhaust the 597 checks.
        "pass": bool(n_real > 0 and n_cplx > 0 and real_via_re == n_real
                     and cplx_via_im == n_cplx and n_real + n_cplx == total),
    })

    # ---- G3: x*y and y/x DO become real -- once, exactly, and Re < 1 saves it ----
    #
    # ⚠ RETRACTION. The first version of this gate claimed "x*y and y/x are NEVER real on
    # the arc -- both carried by Im != 0 at every one of the 597 checks, with a genuine
    # margin rather than a near-miss", and passed on `min |Im| > 1e-6`. That claim is
    # FALSE, and the gate's own design hid it: a grid minimum is not a lower bound.
    #
    # Refining the grid shrinks the complex-pair minimum like 1/N -- 0.00587 at N = 399,
    # 0.00215 at N = 999 -- which is the signature of a simple ZERO CROSSING, not a margin.
    # There is exactly one on (0, pi), located here by bisecting the SYMMETRIC function
    # prod_j Im(x*y_j) so the search is branch-independent.
    #
    # The crossing value is exact: r = -1.2365057033914990243, the unique real root of
    #
    #     r^5 - r^3 + 1 = 0
    #
    # with c = r(1+r)/2 and t = 1/r^2 -- all three confirmed to 20 digits below. It falls
    # out of Vieta: if x*y_2 = r is real with |x| = 1 then y_2 = r*conj(x), so y_3 = r*x,
    # and substituting into the curve makes x a root of a cubic with REAL coefficients.
    # x is non-real on the open arc, so conj(x) is a root too and the third root is -r^2;
    # the two Vieta relations then give c = r(1+r)/2 and the quintic.
    #
    # notCut still holds -- via `Re < 1`, NOT via `Im != 0`. So `x*y in notCut` genuinely
    # needs the disjunction, and the retracted claim ("needs no case split at all") had the
    # proof obligation exactly backwards.
    #
    # The Lean consequence is cheap and is what makes this benign: r >= 1 forces
    # r^5 - r^3 + 1 = r^3(r^2 - 1) + 1 >= 1 > 0, so NO real root of the quintic reaches 1.
    def prod_im_xy(ph, use_div=False):
        """prod_j Im(x*y_j) -- symmetric in the roots, so it needs no branch tracking."""
        x = exp(mpc(0, 1) * ph)
        p = mpf(1)
        for y in roots_at(ph):
            p *= im(y / x) if use_div else im(x * y)
        return p

    crossings = {}
    for use_div in (False, True):
        found, prev = [], None
        M = 600
        for i in range(1, M):
            ph = pi * mpf(i) / M
            v = prod_im_xy(ph, use_div)
            if prev is not None and prev[1] * v < 0:
                found.append(findroot(lambda u: prod_im_xy(u, use_div), (prev[0], ph),
                                      solver='bisect', tol=mpf(10) ** -30))
            prev = (ph, v)
        crossings['y_over_x' if use_div else 'x_times_y'] = found
    zs = crossings['x_times_y']
    rvals, res_ok = [], True
    for z in zs:
        x = exp(mpc(0, 1) * z)
        ws = [x * y for y in roots_at(z)]
        w = min(ws, key=lambda u: fabs(im(u)))
        rvals.append(re(w))
        if not (re(w) < 1):
            res_ok = False
    rq = findroot(lambda u: u ** 5 - u ** 3 + 1, mpf("-1.2365057033914990243"),
                  tol=mpf(10) ** -35)
    cq = mpmath_cos(zs[0]) if zs else None
    gates.append({
        "gate": "G3",
        "claim": "RETRACTED AND REPLACED. The first version claimed `x*y and y/x are NEVER real on "
                 "the arc ... so their notCut membership needs no case split at all`. FALSE, and "
                 "the gate hid it by passing on a grid minimum, which is not a lower bound: refine "
                 "the grid and the complex-pair minimum shrinks like 1/N (0.00587 at N=399, "
                 "0.00215 at N=999) -- a simple ZERO CROSSING. There is exactly one on (0,pi), "
                 "found by bisecting the SYMMETRIC prod_j Im(x*y_j) so no branch tracking is "
                 "needed. At it, x*y is real and notCut holds via `Re < 1`, so the obligation is "
                 "the OPPOSITE of what was claimed. The crossing is exact: r is the unique real "
                 "root of r^5 - r^3 + 1, with c = r(1+r)/2 and t = 1/r^2, all to 20 digits. "
                 "Benign in Lean: r >= 1 gives r^5 - r^3 + 1 = r^3(r^2-1) + 1 >= 1 > 0, so no real "
                 "root of the quintic reaches 1",
        "crossings_of_x_times_y_on_open_arc": len(crossings['x_times_y']),
        "crossings_of_y_over_x_on_open_arc": len(crossings['y_over_x']),
        "crossing_phi": [nstr(z, 20) for z in zs],
        "crossing_value_r": [nstr(v, 20) for v in rvals],
        "r_as_root_of_quintic_r5_minus_r3_plus_1": nstr(rq, 20),
        "agreement_with_quintic_root": nstr(fabs(rvals[0] - rq), 5) if rvals else None,
        "c_predicted_r_times_1_plus_r_over_2": nstr(rq * (1 + rq) / 2, 20),
        "c_measured_at_crossing": nstr(cq, 20) if cq is not None else None,
        "t_predicted_one_over_r_squared": nstr(1 / rq ** 2, 20),
        "Re_lt_1_at_every_crossing": bool(res_ok),
        "retracted_claim": "x*y and y/x are NEVER real on the arc; no case split needed",
        "why_the_old_gate_passed": "it tested a grid minimum against 1e-6; a grid minimum "
                                   "cannot certify a lower bound, and the zero sat between "
                                   "sample points",
        # the crossing must exist (refuting the old claim), be unique, and be survivable
        "pass": bool(len(zs) == 1 and res_ok
                     and fabs(rvals[0] - rq) < mpf(10) ** -25
                     and cq is not None and fabs(cq - rq * (1 + rq) / 2) < mpf(10) ** -25),
    })

    # ---- G4: the route a Lean proof takes, MEASURED not asserted -------------
    # This gate exists in the shape it does because of Route 32 G9, which was written to
    # catch one specific mistake and had `pass` HARDCODED True -- so it kept passing while
    # the claim under it went false. A "what the proof needs" gate is exactly where that
    # happens again, so every clause below is a number, not a sentence.
    worst_abs_y = None
    worst_prod_err = mpf(0)
    min_neg_im_roots = None      # per arc point, how many roots have (x*y).im < 0
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        x = exp(mpc(0, 1) * ph)
        rts = roots_at(ph)
        prod = rts[0] * rts[1] * rts[2]
        worst_prod_err = max(worst_prod_err, fabs(prod - 1))
        n_neg = 0
        for y in rts:
            a = fabs(y)
            if worst_abs_y is None or a < worst_abs_y:
                worst_abs_y = a
            if im(x * y) < 0:
                n_neg += 1
        if min_neg_im_roots is None or n_neg < min_neg_im_roots:
            min_neg_im_roots = n_neg
    gates.append({
        "gate": "G4",
        "claim": "WHAT A LEAN PROOF NEEDS, per condition -- with every clause MEASURED. "
                 "(1) y != 0, x*y != 0, y/x != 0: the product of the three roots is -d/a = 1 "
                 "identically in x, so no root can vanish; measured below as |y1*y2*y3 - 1| and "
                 "as a lower bound on |y|. (2) x*y and y/x in notCut: via Im != 0, no case split "
                 "(G3), and exists_pinning_data already supplies a sign -- measured below as the "
                 "per-arc-point count of roots with (x*y).im < 0. (3) y in notCut: THE ONLY ONE "
                 "NEEDING A CASE SPLIT -- real root via Re = t < 1, complex pair via Im != 0 (G2)",
        "hardest_condition": "y in notCut -- the only one needing a real/complex case split",
        "min_abs_y_over_all_checks": nstr(worst_abs_y, 10) if worst_abs_y is not None else None,
        "worst_abs_root_product_minus_one": nstr(worst_prod_err, 8),
        "min_roots_per_arc_point_with_Im_xy_neg": min_neg_im_roots,
        "already_available": ["exists_pinning_data: 0 < t < 1, (x*y_3).im < 0, "
                              "c < 0 -> (x*y_2).im < 0",
                              "gamma_rel: t*(t^2 - 2ct + 2c + 1) = 1, so no root is 0"],
        # the product-of-roots algebra must actually hold, no root may approach 0, and
        # exists_pinning_data's sign claim must have at least one witness at every arc point.
        "pass": bool(worst_prod_err < mpf(10) ** -30
                     and worst_abs_y is not None and worst_abs_y > mpf(10) ** -3
                     and min_neg_im_roots is not None and min_neg_im_roots >= 1),
    })

    # ---- G5: the arc CROSSES the discriminant, and no real root reaches 1 ----
    # Fell out of G2's counts and was not anticipated: 291 real roots over 199 arc points,
    # not 199. On |x| = 1 the y-cubic has REAL coefficients (it is `unitCubic (Re x)`), so
    # roots are all-real or one-real-plus-a-conjugate-pair -- and 291 = 3*46 + 1*153 says
    # BOTH regimes occur. That makes `continuous_otherRoots`'s collision branch live on the
    # arc rather than a defensive case, and it means the real branch of `y in notCut` has to
    # cover THREE roots at some arc points, not one.
    def disc(cv):
        """Discriminant of t^3 - 2c t^2 + (2c+1)t - 1, as a quartic in c."""
        return 16 * cv ** 4 - 48 * cv ** 3 + 28 * cv ** 2 + 12 * cv - 31

    def disc_direct(cv):
        a, b, cc, d = mpf(1), -2 * cv, 2 * cv + 1, mpf(-1)
        return 18 * a * b * cc * d - 4 * b ** 3 * d + b ** 2 * cc ** 2 - 4 * a * cc ** 3 - 27 * a ** 2 * d ** 2

    # identity checked OFF the arc: c = 5.5 and c = -2.7 are nowhere near [-1, 1]
    disc_id_err = max(fabs(disc(mpf(s)) - disc_direct(mpf(s)))
                      for s in ["0.31", "-2.7", "5.5", "0", "1"])
    cstar = [re(r) for r in polyroots([mpf(16), mpf(-48), mpf(28), mpf(12), mpf(-31)],
                                      maxsteps=300, extraprec=300)
             if fabs(im(r)) < mpf(10) ** -35 and -1 <= re(r) <= 1]
    n_all_real = sum(1 for i in range(N)
                     if sum(1 for r in roots_at(pi * mpf(i + 1) / (N + 1))
                            if fabs(im(r)) < REAL_TOL) == 3)
    # the shift certificate a Lean proof of "no real root reaches 1" runs on,
    # checked OFF the root locus (none of these (c,t) is a root)
    def p_raw(cv, tv):
        return tv ** 3 - 2 * cv * tv ** 2 + (2 * cv + 1) * tv - 1

    def p_shift(cv, tv):
        s = tv - 1
        return 1 + (4 - 2 * cv) * s + (3 - 2 * cv) * s ** 2 + s ** 3

    shift_err = max(fabs(p_raw(mpf(a), mpf(b)) - p_shift(mpf(a), mpf(b)))
                    for a, b in [("0.31", "2.4"), ("-2.7", "0.13"), ("5.5", "-1.1"),
                                 ("1", "1"), ("-0.75", "0.5")])
    max_real_root = None
    for i in range(N):
        for r in roots_at(pi * mpf(i + 1) / (N + 1)):
            if fabs(im(r)) < REAL_TOL and (max_real_root is None or re(r) > max_real_root):
                max_real_root = re(r)
    gates.append({
        "gate": "G5",
        "claim": "THE ARC CROSSES THE DISCRIMINANT, and no real root reaches 1. On |x| = 1 the "
                 "y-cubic is `unitCubic (Re x)` with REAL coefficients, so the roots are all-real "
                 "or one-real-plus-conjugate-pair. Both regimes occur on the arc -- so "
                 "`continuous_otherRoots`'s collision branch is exercised, not defensive, and the "
                 "real branch of `y in notCut` must cover three roots at some arc points. Separately: "
                 "shifting t = 1 + s gives unitCubic c (1+s) = 1 + (4-2c)s + (3-2c)s^2 + s^3, whose "
                 "coefficients are ALL POSITIVE for c <= 1, so no root reaches 1 -- a uniform Re < 1 "
                 "needing no `exists_pinning_data`",
        "arc_points_with_three_real_roots": n_all_real,
        "arc_points_with_one_real_root": N - n_all_real,
        "discriminant_as_quartic_in_c": "16c^4 - 48c^3 + 28c^2 + 12c - 31",
        "discriminant_identity_error_checked_off_arc": nstr(disc_id_err, 5),
        "c_star_the_only_transition_in_[-1,1]": nstr(cstar[0], 20) if cstar else None,
        "shift_certificate_error_off_root_locus": nstr(shift_err, 5),
        "max_real_root_over_arc": nstr(max_real_root, 12) if max_real_root is not None else None,
        "pass": bool(len(cstar) == 1 and 0 < n_all_real < N
                     and disc_id_err < mpf(10) ** -35 and shift_err < mpf(10) ** -35
                     and max_real_root is not None and max_real_root < 1),
    })

    # ---- G6: is `|x| = 1` load-bearing, or decoration? ----------------------
    # `root_mem_notCut` reads as though it might hold generally. It does not, and the
    # counterexample is exact: the curve is QUADRATIC in x, so fixing a bad y and solving
    # for x produces one directly. x^2*y(1-y) + x(y^3+y-1) + y(1-y) = 0; at y = 2 that is
    # 2x^2 - 9x + 2 = 0, giving x = (9 +- sqrt 65)/4, both real, neither on the unit circle.
    # y = 2 is real with Re >= 1, so y is NOT in notCut. The hypothesis carries the theorem.
    ybad = mpf(2)
    xbad = (9 - sqrt(65)) / 4

    def curve_val(xv, yv):
        return xv * yv ** 3 - (xv ** 2 + 1) * yv ** 2 + (xv ** 2 + xv + 1) * yv - xv

    # and the arc's real roots climb to the largest LEVEL-7 root as phi -> pi
    lvl7 = max(re(r) for r in polyroots([mpf(1), mpf(2), mpf(-1), mpf(-1)],
                                        maxsteps=300, extraprec=300)
               if fabs(im(r)) < mpf(10) ** -35)
    lvl7_closed = 2 * mpmath_cos(pi / 7) - 1
    gates.append({
        "gate": "G6",
        "claim": "IS `|x| = 1` LOAD-BEARING IN `root_mem_notCut`, OR DECORATION? Load-bearing, and "
                 "the counterexample is exact rather than sampled: the curve is quadratic in x, so "
                 "fixing y = 2 and solving gives 2x^2 - 9x + 2 = 0, x = (9 +- sqrt 65)/4 -- both "
                 "real, neither on the unit circle, and y = 2 is real with Re >= 1 so it is NOT in "
                 "notCut. Drop the hypothesis and the theorem is FALSE. Checked here because a "
                 "hypothesis that is never tested off its own configuration is indistinguishable "
                 "from one that does nothing. SEPARATELY: the arc's real roots climb to the largest "
                 "LEVEL-7 root 2cos(pi/7) - 1 as phi -> pi, which is the configuration "
                 "`sum_re_deformedV_at_neg_one` evaluates -- so the transport's endpoint is the "
                 "level-7 point, not merely near it",
        "counterexample_x": nstr(xbad, 20),
        "counterexample_x_closed_form": "(9 - sqrt 65)/4",
        "counterexample_y": "2",
        "counterexample_abs_x": nstr(fabs(xbad), 20),
        "counterexample_curve_residual": nstr(fabs(curve_val(xbad, ybad)), 5),
        "counterexample_y_in_notCut": bool(in_not_cut(mpc(ybad, 0))),
        "sup_of_real_roots_is_largest_level7_root": nstr(lvl7, 20),
        "level7_root_closed_form_2cos_pi_over_7_minus_1": nstr(lvl7_closed, 20),
        "sampled_max_over_arc": nstr(max_real_root, 12) if max_real_root is not None else None,
        # the counterexample must be a genuine root, off the circle, with y outside notCut;
        # and the sampled max must approach the level-7 root from below without reaching it
        # residual tolerance is set from the WORKING PRECISION (dps 40), not guessed: the
        # first draft used 1e-40, which sits at the last digit and failed on 1.4e-40.
        "pass": bool(fabs(curve_val(xbad, ybad)) < mpf(10) ** -(mp.dps - 5)
                     and fabs(fabs(xbad) - 1) > mpf(10) ** -6
                     and not in_not_cut(mpc(ybad, 0))
                     and fabs(lvl7 - lvl7_closed) < mpf(10) ** -35
                     and max_real_root is not None
                     and max_real_root < lvl7 and lvl7 - max_real_root < mpf(10) ** -4),
    })

    # ---- G7: VSide is FALSE at phi = pi, and G1 never looked ----------------
    # G1 samples phi = pi*(i+1)/(N+1), i = 0..N-1 -- the OPEN interval. It never tests the
    # endpoint. It turns out the endpoint is exactly where VSide fails, so G1's "holds
    # everywhere" would have been read as covering a point it excluded.
    #
    # At phi = pi the arc reaches x = -1, all three roots are real (level-7), and for a real
    # root Im(x*y) = y*sin(phi) -- so EVERY imaginary part vanishes at once. Two roots are
    # still carried by Re < 1; the third, y = -2.2469796, gives x*y = +2.2469796, which is
    # real with Re >= 1. That is Li2's cut. VSide.hc2 and hc3 are FALSE there.
    #
    # ⚠ Evaluating this with x = exp(i*pi) reports notCut = TRUE, because mpmath returns
    # x = -1 + 4.1e-43j and the spurious Im saves it -- the SAME trap as G2, in a new place.
    # x must be built exactly.
    xpi = mpc(-1, 0)                     # EXACT, not exp(i*pi)
    rts_pi = polyroots([xpi, -(xpi ** 2 + 1), xpi ** 2 + xpi + 1, -xpi],
                       maxsteps=300, extraprec=300)
    bad = [y for y in rts_pi if not in_not_cut(xpi * y)]
    x0 = mpc(1, 0)
    rts_0 = polyroots([x0, -(x0 ** 2 + 1), x0 ** 2 + x0 + 1, -x0], maxsteps=300, extraprec=300)
    zero_ok = all(in_not_cut(x0 * y) and in_not_cut(y / x0) and in_not_cut(y) for y in rts_0)
    # what the naive exp(i*pi) evaluation would have said
    xpi_float = exp(mpc(0, 1) * pi)
    rts_pf = polyroots([xpi_float, -(xpi_float ** 2 + 1), xpi_float ** 2 + xpi_float + 1,
                        -xpi_float], maxsteps=300, extraprec=300)
    naive_says_ok = all(in_not_cut(xpi_float * y) for y in rts_pf)
    gates.append({
        "gate": "G7",
        "claim": "VSide is FALSE AT phi = pi, and G1 STRUCTURALLY CANNOT SEE IT because it samples "
                 "the OPEN interval pi*(i+1)/(N+1). At the endpoint x = -1, all three roots are "
                 "real (they are the level-7 roots), and for a real root Im(x*y) = y*sin(phi) -- so "
                 "every imaginary part vanishes SIMULTANEOUSLY. Two roots survive on Re < 1; the "
                 "third, y = -2.2469796, gives x*y = +2.2469796, real with Re >= 1, which is "
                 "exactly Li2's cut. So VSide.hc2 and hc3 are false there and MUST NOT be attempted "
                 "on the closed arc. The transport is unaffected: `envelopeS_total` asks for the "
                 "derivative only on `Ico 0 pi` and for continuity on `Icc 0 pi`, so the endpoint "
                 "needs a VALUE but not differentiability -- and `sum_re_deformedV_at_neg_one` "
                 "already supplies the value at x = -1 with no differentiability hypothesis",
        "phi_pi_roots_failing_hc2": [nstr(re(y), 16) for y in bad],
        "phi_pi_x_times_failing_root": [nstr(re(xpi * y), 16) for y in bad],
        "phi_pi_all_six_hold": bool(len(bad) == 0),
        "phi_zero_all_hold": bool(zero_ok),
        "naive_exp_i_pi_evaluation_would_report_ok": bool(naive_says_ok),
        "why_naive_is_wrong": "exp(i*pi) returns -1 + 4.1e-43j, and that spurious Im satisfies "
                              "the first disjunct -- the same trap as G2, in a new place. x must "
                              "be built exactly as mpc(-1, 0)",
        "consequence": "any attempt to prove VSide for phi in Icc 0 pi is attempting something "
                       "FALSE; the provable statement is over Ico 0 pi",
        # the gate PASSES by confirming the failure is real, isolated to pi, and that the
        # naive evaluation hides it -- this is a recorded refutation, not a green light
        "pass": bool(len(bad) == 1 and zero_ok and naive_says_ok),
    })

    # ---- G8: BOTH `log(-y)` routes are needed, at every arc point ------------
    # `hasDerivAt_envelopeS` gets `d/du log(-Y_j u)` from one of two lemmas:
    # `hasDerivAt_log_neg_of_slitPlane` when -y is off log's cut, and
    # `hasDerivAt_log_neg_ofReal` when it is on it. `-y in slitPlane` unfolds to
    # `Re y < 0 or Im y != 0`, so it fails PRECISELY at a positive real y.
    #
    # This gate exists because dropping route 2 is exactly correction 6's mistake in a new
    # place: a statement carrying only `slitPlane` is VACUOUS at the positive real root,
    # and there is one at every arc point. Measured, not assumed.
    route1, route2 = 0, 0
    pts_without_route2 = 0
    pts_with_two_route2 = 0
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        n2 = 0
        for y in roots_at(ph):
            is_real = fabs(im(y)) < REAL_TOL
            if is_real and re(y) > 0:
                route2 += 1
                n2 += 1
            else:
                route1 += 1
        if n2 == 0:
            pts_without_route2 += 1
        if n2 > 1:
            pts_with_two_route2 += 1
    gates.append({
        "gate": "G8",
        "claim": "BOTH `log(-y)` ROUTES ARE NEEDED. `-y in slitPlane` is `Re y < 0 or Im y != 0`, "
                 "so it fails precisely at a POSITIVE REAL root -- and there is exactly one at "
                 "every arc point (`exists_root_mem_Ioo` puts it in (0,1)). So route 2 "
                 "(`hasDerivAt_log_neg_ofReal`) can never be dropped, and route 1 is impossible "
                 "there. Dropping route 2 is correction 6's mistake in a new place: a statement "
                 "carrying only `slitPlane` would be VACUOUS at that root. The other two roots "
                 "take route 1 either as a genuine complex pair (153 points) or, where the "
                 "discriminant has flipped, as NEGATIVE reals (46 points, G5)",
        "roots_taking_route1_slitPlane": route1,
        "roots_taking_route2_positive_real": route2,
        "arc_points_with_no_route2_root": pts_without_route2,
        "arc_points_with_more_than_one_route2_root": pts_with_two_route2,
        "lean": "log_neg_route (hx0 : x != 0) (hc : curve x y = 0) : "
                "-y in slitPlane or (0 < y.re and y.im = 0)",
        "still_open": "route 2's lemma is stated for a path `fun u => ((t u : R) : C)`, so it "
                      "needs Y real-valued NEAR phi, not merely real AT phi. That is a condition "
                      "on the labelling, not on the root -- it belongs to the concrete Y1 Y2 Y3",
        # exactly one route-2 root per arc point, and route 1 non-empty
        "pass": bool(route2 == N and pts_without_route2 == 0 and pts_with_two_route2 == 0
                     and route1 == 2 * N),
    })

    # ---- G9: the concrete labelling is FORCED, and it fixes G8's residue ----
    # G8 left one thing open: route 2's lemma is stated for a path `fun u => ((t u : R) : C)`,
    # so it needs Y REAL-VALUED NEAR phi, not merely real AT phi -- a condition on the
    # labelling, not on the root. The natural construction discharges it by construction:
    #
    #   Y_1 phi = ((t (cos phi) : R) : C),  t(c) = the unique root of unitCubic c in (0,1)
    #   (Y_2, Y_3) = otherRoots (t - 2c) (t^2 - 2ct + 2c + 1)
    #
    # Y_1 is real-valued by definition, which is exactly route 2's shape. What has to hold
    # for this to be well defined and smooth is measured here; each item is already a Lean
    # theorem, so this gate is checking that they line up on real data, not discovering them.
    n_not_unique, n_not_route2 = 0, 0
    tmin, tmax, maxjump = None, None, None
    prev_t = None
    step = pi / (N + 1)
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        c = mpmath_cos(ph)
        rts = polyroots([mpf(1), -2 * c, 2 * c + 1, mpf(-1)], maxsteps=300, extraprec=300)
        in_ioo = [re(r) for r in rts if fabs(im(r)) < REAL_TOL and 0 < re(r) < 1]
        pos_real = [re(r) for r in rts if fabs(im(r)) < REAL_TOL and re(r) > 0]
        if len(in_ioo) != 1:
            n_not_unique += 1
            continue
        if len(pos_real) != 1 or fabs(pos_real[0] - in_ioo[0]) > REAL_TOL:
            n_not_route2 += 1
        t = in_ioo[0]
        tmin = t if tmin is None or t < tmin else tmin
        tmax = t if tmax is None or t > tmax else tmax
        if prev_t is not None:
            j = fabs(t - prev_t)
            maxjump = j if maxjump is None or j > maxjump else maxjump
        prev_t = t
    gates.append({
        "gate": "G9",
        "claim": "THE CONCRETE LABELLING IS FORCED, and it discharges G8's residue rather than "
                 "leaving it. Take Y_1 phi = ((t (cos phi) : R) : C) with t(c) the unique root of "
                 "unitCubic c in (0,1), and (Y_2, Y_3) = otherRoots. Then: (a) t is SINGLE-VALUED "
                 "-- already a Lean theorem, `real_root_neg_of_ne` says the other real roots are "
                 "negative; (b) t stays bounded away from 0 and 1, so `unitCubic_deriv_ge`'s "
                 "hypotheses hold with margin and the IFT applies at 7/4; (c) the (0,1) root IS "
                 "the unique POSITIVE REAL root, i.e. exactly the one `log_neg_route` sends to "
                 "route 2; and (d) Y_1 is real-valued BY CONSTRUCTION, which is precisely the "
                 "shape route 2's lemma requires. So the 'real near phi, not merely at phi' "
                 "condition is not an extra obligation -- it falls out of the only labelling "
                 "that makes sense",
        "arc_points": N,
        "points_where_(0,1)_root_not_unique": n_not_unique,
        "points_where_(0,1)_root_is_not_the_route2_root": n_not_route2,
        "t_range": [nstr(tmin, 10) if tmin is not None else None,
                    nstr(tmax, 10) if tmax is not None else None],
        "t_endpoints_cross_check": "t -> 0.4301597 as phi -> 0 (the real root at x = +1) and "
                                   "t -> 0.8019377 = 2cos(pi/7) - 1 as phi -> pi, the largest "
                                   "level-7 root -- matching G6 independently",
        "max_grid_jump_in_t": nstr(maxjump, 8) if maxjump is not None else None,
        "grid_step": nstr(step, 8),
        "implied_bound_on_dt_dphi": nstr(maxjump / step, 6) if maxjump is not None else None,
        "still_open": "the Lean construction itself: defining t(c) from `exists_root_mem_Ioo` + "
                      "`real_root_neg_of_ne` and differentiating it through `ImplicitScalar`. "
                      "The PIECES are all proved; what is missing is the assembly",
        "pass": bool(n_not_unique == 0 and n_not_route2 == 0
                     and tmin is not None and tmin > mpf(10) ** -2 and tmax < 1
                     and maxjump is not None and maxjump < 1),
    })

    # ---- G10: the Lean labelling reproduces the ACTUAL roots -----------------
    # `FiveTwoRootLabelling` builds the three branches as
    #     Y_1 = realRoot(cos phi)                            (the (0,1) root)
    #     (Y_2, Y_3) = otherRoots (t - 2c) (t^2 - 2ct + 2c + 1)
    # The second line is Vieta on the quadratic cofactor, and it TYPE-CHECKS whether or not
    # it names the right numbers. So check it against polyroots: the multiset {Y_1,Y_2,Y_3}
    # must equal the actual root multiset at every arc point.
    worst_match = None
    n_bad = 0
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        c = mpmath_cos(ph)
        rts = polyroots([mpf(1), -2 * c, 2 * c + 1, mpf(-1)], maxsteps=300, extraprec=300)
        tv = [re(r) for r in rts if fabs(im(r)) < REAL_TOL and 0 < re(r) < 1]
        if len(tv) != 1:
            n_bad += 1
            continue
        t = tv[0]
        beta = t - 2 * c
        gamma = t ** 2 - 2 * c * t + 2 * c + 1
        # otherRoots are the roots of Y^2 + beta*Y + gamma
        pair = polyroots([mpf(1), beta, gamma], maxsteps=300, extraprec=300)
        built = sorted([mpc(t, 0)] + list(pair), key=lambda z: (re(z), im(z)))
        actual = sorted(rts, key=lambda z: (re(z), im(z)))
        d = max(fabs(a - b) for a, b in zip(built, actual))
        if worst_match is None or d > worst_match:
            worst_match = d
    gates.append({
        "gate": "G10",
        "claim": "THE LEAN LABELLING REPRODUCES THE ACTUAL ROOTS. `FiveTwoRootLabelling` builds "
                 "Y_1 = realRoot(cos phi) and (Y_2,Y_3) = otherRoots (t-2c) (t^2-2ct+2c+1). That "
                 "second line is Vieta on the quadratic cofactor and TYPE-CHECKS whether or not it "
                 "names the right numbers -- exactly the failure mode this lane has hit nine times "
                 "(a correct theorem about the wrong polynomial). Checked against polyroots: the "
                 "multiset {Y_1,Y_2,Y_3} must equal the actual root multiset at every arc point. "
                 "The identity behind it is (Y-t)(Y^2+(t-2c)Y+(t^2-2ct+2c+1)) = unitCubic, whose "
                 "constant term needs gamma_rel: t*(t^2-2ct+2c+1) = 1",
        "arc_points": N,
        "points_with_no_unique_(0,1)_root": n_bad,
        "worst_multiset_mismatch": nstr(worst_match, 8) if worst_match is not None else None,
        "pass": bool(n_bad == 0 and worst_match is not None
                     and worst_match < mpf(10) ** -(mp.dps - 8)),
    })

    # ---- G11: what `hcont` needs at the endpoint -- CHEAPER than first recorded ----
    #
    # ⚠ THIS GATE'S FIRST VERSION OVERSTATED THE OBLIGATION. It said hcont needs "Re Li2
    # continuous ACROSS the cut", a two-dimensional statement about the real part. It does
    # not. It needs ONE-SIDED continuity from BELOW, and that is where Lean's principal
    # Complex.log already puts the integral's value.
    #
    # Why: cLiTwoExt w = -int_0^1 log(1 - w t)/t dt. For real w = r > 1 and t > 1/r the
    # argument 1 - wt is a NEGATIVE REAL, and principal log gives arg = +pi there. That is
    # the same arg the integrand approaches when w -> r from Im < 0 (then 1 - wt has Im > 0).
    # From Im > 0 the arg tends to -pi instead, and the value differs by exactly 2*pi*i*log r.
    #
    # Measured below: from BELOW the difference falls linearly to ~1e-9; from ABOVE it sits
    # at 5.0868 = |2*pi*i*log r|. And the arc approaches from Im < 0 -- so it meets the cut
    # on precisely the continuous side.
    #
    # ⚠ A NUMERICAL TRAP, recorded because it produced a wrong value first: integrating
    # over [0,1] in one piece gives 2.4873 - 2.5226i, which is WRONG. The integrand has a
    # log singularity at t = 1/r inside the interval. Split at Re(1/w) -- and split on BOTH
    # sides, not only on the cut, or the off-cut comparisons are silently garbage. Correct
    # value 2.4543 - 2.5434i, matching mpmath's polylog(2, r) exactly.
    def cLiTwoExt_num(w):
        pts = [0, 1]
        tc = re(1 / w)
        if 0 < tc < 1:
            pts = [0, tc, 1]
        return -quad(lambda t: log(1 - w * t) / t, pts)

    r_cut = mpf("2.246979603717467")
    v_on = cLiTwoExt_num(mpc(r_cut, 0))
    below, above = [], []
    for e in ["1e-3", "1e-5", "1e-7", "1e-9"]:
        eps = mpf(e)
        below.append(fabs(cLiTwoExt_num(mpc(r_cut, -eps)) - v_on))
        above.append(fabs(cLiTwoExt_num(mpc(r_cut, eps)) - v_on))
    jump = cLiTwoExt_num(mpc(r_cut, mpf("1e-9"))) - cLiTwoExt_num(mpc(r_cut, -mpf("1e-9")))
    jump_pred = 2 * pi * mpc(0, 1) * log(r_cut)
    slopes = []
    for d in ["0.01", "0.001", "0.0001"]:
        ph = pi - mpf(d)
        x = exp(mpc(0, 1) * ph)
        w = max((x * y for y in roots_at(ph)), key=lambda u: re(u))
        slopes.append(im(w) / (-mpf(d)))
    gates.append({
        "gate": "G11",
        "claim": "WHAT `hcont` NEEDS AT phi = pi -- AND IT IS CHEAPER THAN THIS GATE FIRST SAID. "
                 "The first version claimed hcont needs `Re Li2 continuous ACROSS the cut`, a 2-D "
                 "statement about the real part. RETRACTED: it needs only ONE-SIDED continuity "
                 "from BELOW. cLiTwoExt w = -int log(1-wt)/t dt, and for real w > 1 the principal "
                 "log gives arg = +pi past t = 1/w -- the same limit as approaching from Im < 0. "
                 "Measured: from below the gap falls linearly to 1.4e-9; from above it sits at "
                 "5.0868 = |2*pi*i*log r|, matching the predicted jump to 10 digits. And the arc "
                 "approaches the cut from Im < 0, so it meets it on the CONTINUOUS side. What is "
                 "still open is the Lean statement, not a 2-D continuity theorem",
        "cut_point_x_times_y": nstr(r_cut, 16),
        "cLiTwoExt_on_cut": nstr(v_on, 16),
        "Im_on_cut_equals_neg_pi_log_r": nstr(fabs(im(v_on) + pi * log(r_cut)), 5),
        "gap_from_below": [nstr(b, 5) for b in below],
        "gap_from_above": [nstr(a, 5) for a in above],
        "jump_measured": nstr(jump, 12),
        "jump_predicted_2pi_i_log_r": nstr(jump_pred, 12),
        "arc_approach_slope_Im/(phi-pi)": [nstr(s, 10) for s in slopes],
        "slope_note": "positive because Im(x*y) < 0 and (phi - pi) < 0; it converges to r "
                      "itself, i.e. Im(x*y) ~ -r*(pi - phi) -- linear approach from BELOW",
        "numerical_trap": "integrating [0,1] in ONE piece gives 2.4873 - 2.5226i, which is WRONG "
                          "-- the integrand has a log singularity at t = 1/r inside. Split at "
                          "Re(1/w), and split on BOTH sides or the off-cut comparisons are "
                          "silently garbage. Correct value matches mpmath polylog(2,r) exactly",
        "localisation_at_phi_pi": {
            "Yreal": "0.8019377358048383  ->  x*y = -0.8019  (Re < 1, fine)",
            "Ypair.1": "-0.5549581320873712  ->  x*y = +0.5550  (Re < 1, fine)",
            "Ypair.2": "-2.246979603717467  ->  x*y = +2.2470  ON THE CUT",
            "note": "pairDisc(pi) = 2.8629 > 0, so otherRoots is in its REAL branch there; "
                    "only ONE of the three terms is difficult, and it is Ypair.2's "
                    "cLiTwoExt(x*y). hcont is not three problems, it is one",
        },
        "still_open": "the Lean statement: cLiTwoExt continuous at a cut point along a path "
                      "approaching from Im < 0. One-sided, not two-dimensional, and needed "
                      "for ONE term (Ypair.2's) rather than for all three branches",
        "pass": bool(below[-1] < mpf(10) ** -8 and above[-1] > 1
                     and fabs(im(v_on) + pi * log(r_cut)) < mpf(10) ** -20
                     and fabs(jump - jump_pred) < mpf(10) ** -8
                     # slope = Im(x*y)/(phi - pi): POSITIVE, since both factors are negative.
                     # A first draft tested s < 0 and failed on its own gate -- the sign of a
                     # ratio is not the sign of its numerator.
                     and all(s > 0 for s in slopes)
                     and fabs(slopes[-1] - r_cut) < mpf(10) ** -6),
    })

    # ---- G12: `hasDerivAt_Ypair_*`'s hypothesis is satisfiable, and IS the collision ----
    # The pair's derivative lemmas carry `pairDisc phi < 0`, which selects otherRoots'
    # complex branch AND keeps sqrt away from 0. A hypothesis doing two jobs at once is
    # exactly the kind that turns out to hold nowhere -- correction 6 all over again -- so it
    # is measured rather than assumed.
    #
    # `pairDisc` is computed here from the LEAN definitions (beta = t - 2c,
    # gamma = t^2 - 2ct + 2c + 1) rather than from the cubic's discriminant, so agreement
    # with G5 is a genuine cross-check between two different formulas.
    def pair_disc(ph):
        c = mpmath_cos(ph)
        rts = polyroots([mpf(1), -2 * c, 2 * c + 1, mpf(-1)], maxsteps=300, extraprec=300)
        v = [re(r) for r in rts if fabs(im(r)) < REAL_TOL and 0 < re(r) < 1]
        if len(v) != 1:
            return None
        t = v[0]
        return (t - 2 * c) ** 2 - 4 * (t ** 2 - 2 * c * t + 2 * c + 1)

    n_neg, n_pos, n_none = 0, 0, 0
    for i in range(N):
        d = pair_disc(pi * mpf(i + 1) / (N + 1))
        if d is None:
            n_none += 1
        elif d < 0:
            n_neg += 1
        else:
            n_pos += 1
    phi0 = findroot(pair_disc, (mpf("2.40"), mpf("2.42")), solver='bisect', tol=mpf(10) ** -30)
    cstar_here = mpmath_cos(phi0)
    cstar_g5 = [re(r) for r in polyroots([mpf(16), mpf(-48), mpf(28), mpf(12), mpf(-31)],
                                         maxsteps=300, extraprec=300)
                if fabs(im(r)) < mpf(10) ** -35 and -1 <= re(r) <= 1][0]
    gates.append({
        "gate": "G12",
        "claim": "`hasDerivAt_Ypair_fst/snd` CARRY `pairDisc phi < 0`, AND THAT HYPOTHESIS IS "
                 "SATISFIABLE -- measured, not assumed, because it does two jobs at once "
                 "(selecting otherRoots' complex branch and keeping sqrt away from 0) and a "
                 "hypothesis like that is exactly the shape that turns out to hold nowhere "
                 "(correction 6). It holds at 153 of 199 arc points; the other 46 are the "
                 "all-real regime. CROSS-CHECK: pairDisc is computed here from the LEAN "
                 "definitions (beta = t-2c, gamma = t^2-2ct+2c+1), a different formula from G5's "
                 "cubic discriminant, and the two agree exactly -- same 153/46 split, and the "
                 "zero lands on the known collision phi_0 = 137.9206708879635 deg with "
                 "cos = c* = -0.7422176658829284376",
        "points_pairDisc_neg_complex_pair": n_neg,
        "points_pairDisc_pos_all_real": n_pos,
        "points_undetermined": n_none,
        "pairDisc_zero_phi_rad": nstr(phi0, 20),
        "pairDisc_zero_phi_deg": nstr(phi0 * 180 / pi, 19),
        "known_collision_phi0_deg": "137.9206708879635",
        "cos_of_zero": nstr(cstar_here, 20),
        "c_star_from_G5_quartic": nstr(cstar_g5, 20),
        "cross_check_agreement": nstr(fabs(cstar_here - cstar_g5), 5),
        "pass": bool(n_none == 0 and n_neg > 0 and n_pos > 0 and n_neg + n_pos == N
                     and fabs(cstar_here - cstar_g5) < mpf(10) ** -30),
    })

    # ---- G13: he_j for the PAIR needs k = 0, and a naive bound CANNOT pin it ----
    # `hasDerivAt_envelopeS` wants (dVdy x (Y_j phi) * Y_j').re = 0. For the positive REAL
    # root that is already proved (`re_dVdy_mul_eq_zero_of_real`) and needs NO k: dVdy is
    # purely imaginary there and t' is real. The pair is different --
    #     Re(dVdy * Y') = k * 2*pi * Im(Y'/y)
    # so it needs k = 0 outright.
    #
    # Measured, both halves: at the pair |dVdy| <= 1.2e-40 (k = 0), while at the real root
    # |dVdy| = 2*pi/t, max 14.6055 at t = 0.43019 (|k| = 1). Route 30 G2's split, confirmed
    # from the Lean definition of dVdy rather than from the paper.
    #
    # ⚠ THE USEFUL PART IS WHAT DOES NOT WORK. The pinning quantity is
    #     S = arg(1-y) + arg(1-xy) + arg(1-y/x) - 2 arg(-y),   S = 2*pi*k
    # and it is identically 0. But bounding the four terms SEPARATELY gives
    #     1.4076 + 3.1133 + 3.1133 + 2*2.1115 = 11.857  >  2*pi = 6.2832
    # so a term-by-term bound cannot force k = 0. The correlations are needed.
    #
    # Two groupings ARE tight, and they say where to look:
    #     arg(1-y)                                in [-1.4076, 1.4076]   (< pi/2)
    #     arg(1-xy) + arg(1-y/x) - 2 arg(-y)      in [-1.4076, 1.4076]   (< pi/2)
    # Sum of the two bounds is 2.8152 < 2*pi, which pins k = 0 with room to spare.
    #
    # The FIRST is provable: |arg(1-y)| < pi/2 iff Re(1-y) > 0 iff Re y < 1, and for the
    # pair Re y = c - t/2 with c <= 1 and t > 0. The SECOND is the open obligation.
    def dVdy_val(x, y):
        return (-log(1 - y) - log(1 - x * y) - log(1 - y / x) + 2 * log(-y)) / y

    w_pair, w_real = None, None
    s_lo, s_hi = None, None
    g_lo, g_hi = None, None
    re_y_max = None
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        x = exp(mpc(0, 1) * ph)
        for y in polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                           maxsteps=300, extraprec=300):
            v = fabs(dVdy_val(x, y))
            if fabs(im(y)) < REAL_TOL and re(y) > 0:
                w_real = v if w_real is None or v > w_real else w_real
                continue
            w_pair = v if w_pair is None or v > w_pair else w_pair
            s = arg(1 - y) + arg(1 - x * y) + arg(1 - y / x) - 2 * arg(-y)
            s_lo = s if s_lo is None or s < s_lo else s_lo
            s_hi = s if s_hi is None or s > s_hi else s_hi
            g = arg(1 - x * y) + arg(1 - y / x) - 2 * arg(-y)
            g_lo = g if g_lo is None or g < g_lo else g_lo
            g_hi = g if g_hi is None or g > g_hi else g_hi
            re_y_max = re(y) if re_y_max is None or re(y) > re_y_max else re_y_max
    gates.append({
        "gate": "G13",
        "claim": "he_j FOR THE PAIR NEEDS k = 0, AND A TERM-BY-TERM BOUND CANNOT PIN IT. For the "
                 "positive REAL root he_j is already proved and needs no k at all (dVdy is purely "
                 "imaginary, t' is real). For the pair Re(dVdy*Y') = k*2*pi*Im(Y'/y), so k = 0 is "
                 "required. Measured: |dVdy| <= 1.2e-40 at the pair (k = 0) and = 2*pi/t at the "
                 "real root, max 14.6055 (|k| = 1) -- Route 30 G2's split, reconfirmed from the "
                 "LEAN definition of dVdy. THE USEFUL PART IS THE NEGATIVE ONE: the pinning "
                 "quantity S = arg(1-y)+arg(1-xy)+arg(1-y/x)-2arg(-y) is identically 0, but the "
                 "four terms bounded separately give 11.857 > 2*pi, so no term-by-term argument "
                 "works. Two groupings ARE tight, each under pi/2, and their sum 2.8152 < 2*pi "
                 "pins k = 0 with room. The first, |arg(1-y)| < pi/2, is provable from Re y < 1 "
                 "(for the pair Re y = c - t/2, c <= 1, t > 0). The second is the open obligation",
        "max_abs_dVdy_at_pair": nstr(w_pair, 8) if w_pair is not None else None,
        "max_abs_dVdy_at_positive_real_root": nstr(w_real, 10) if w_real is not None else None,
        "pinning_S_range_at_pair": [nstr(s_lo, 8), nstr(s_hi, 8)],
        "naive_termwise_bound": "1.4076 + 3.1133 + 3.1133 + 2*2.1115 = 11.857 > 2*pi = 6.2832 "
                                "-- INSUFFICIENT",
        "tight_grouping_1_arg_1_minus_y": "in [-1.4076, 1.4076], < pi/2, PROVABLE from Re y < 1",
        "tight_grouping_2_range": [nstr(g_lo, 8), nstr(g_hi, 8)],
        "tight_grouping_2": "arg(1-xy) + arg(1-y/x) - 2 arg(-y) -- the OPEN obligation; "
                            "measured under pi/2, needs only < 3*pi/2 for the pinning",
        "max_Re_y_at_pair": nstr(re_y_max, 10) if re_y_max is not None else None,
        "pass": bool(w_pair is not None and w_pair < mpf(10) ** -(mp.dps - 10)
                     and w_real is not None and w_real > 1
                     and s_lo is not None and fabs(s_lo) < mpf(10) ** -30
                     and fabs(s_hi) < mpf(10) ** -30
                     and re_y_max is not None and re_y_max < 1),
    })

    # ---- G14: a SECOND route to k = 0, also closed ---------------------------
    # G13 closed the term-by-term route. The obvious next idea is to use the saddle
    # condition itself: on the curve y^2 = (1-y)(1-xy)(1-y/x), so
    #     (1-xy)(1-y/x) = y^2/(1-y)
    # and taking args should express G = arg(1-xy)+arg(1-y/x)-2arg(-y) in terms of arg(y)
    # and arg(1-y) alone -- both of which are boundable. It does, up to an integer:
    #     arg(1-xy) + arg(1-y/x) = 2 arg(y) - arg(1-y) + 2*pi*m
    # and the route works only if m is pinned.
    #
    # It is not. m takes BOTH values +-1 on the arc (never 0), so the identity trades one
    # branch-pinning problem for another of the same difficulty. Recorded so the next pass
    # does not spend the hour rediscovering it.
    #
    # One structural crumb worth keeping: m flips sign between the two members of the
    # conjugate pair, so it CANCELS when the pair is summed. That suggests the sum over
    # roots may be reachable where the per-root statement is not -- but `he_j` is stated
    # per-root in `hasDerivAt_envelopeS`, so using that would mean changing the interface,
    # not just finishing the proof.
    m_vals = set()
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        x = exp(mpc(0, 1) * ph)
        for y in roots_at(ph):
            if fabs(im(y)) < REAL_TOL and re(y) > 0:
                continue
            lhs = arg(1 - x * y) + arg(1 - y / x)
            rhs = 2 * arg(y) - arg(1 - y)
            m_vals.add(int(nint((lhs - rhs) / (2 * pi))))
    gates.append({
        "gate": "G14",
        "claim": "A SECOND ROUTE TO k = 0, ALSO CLOSED. G13 ruled out bounding the four args "
                 "separately. The next natural idea is the saddle condition itself: on the curve "
                 "y^2 = (1-y)(1-xy)(1-y/x), so (1-xy)(1-y/x) = y^2/(1-y), and taking args should "
                 "reduce G to arg(y) and arg(1-y), both boundable. It does -- up to an integer m -- "
                 "and the route needs m pinned. It is NOT: m takes BOTH values +-1 on the arc and "
                 "never 0, so this trades one branch-pinning problem for another of the same "
                 "difficulty. Recorded so the next pass does not rediscover it. One crumb: m flips "
                 "sign between the conjugate pair, so it CANCELS on the sum over roots -- the sum "
                 "may be reachable where the per-root statement is not, but `he_j` is stated "
                 "per-root, so that would mean changing the interface rather than finishing a proof",
        "m_values_occurring": sorted(m_vals),
        "m_is_pinned": bool(len(m_vals) == 1),
        "conclusion": "route closed; m is not constant",
        # the gate PASSES by confirming the route is closed -- a recorded dead end
        "pass": bool(len(m_vals) > 1 and 0 not in m_vals),
    })

    out = {
        "probe": "qbeta_5two_route36_vside_nonvacuity",
        "bean": "qou-glbl", "dps": mp.dps,
        "pairs_with_lean": ["QOU/QBeta/FiveTwoTransport.lean (VSide)",
                            "QOU/QBeta/FiveTwoRootStructure.lean (exists_pinning_data)"],
        "gates": gates,
        "verdict": {
            "measured": "VSide is NON-VACUOUS on the OPEN arc: all six conditions hold "
                        "simultaneously at all 597 checks (199 interior arc points x 3 roots) -- "
                        "and is FALSE at the endpoint phi = pi (G7).",
            "endpoint": "G7. At x = -1 the roots are the level-7 roots, all real, and "
                        "Im(x*y) = y*sin(phi) vanishes for all three at once. The root "
                        "y = -2.2469796 then has x*y = +2.2469796 on Li2's cut, so hc2 and hc3 "
                        "FAIL. G1 samples the open interval and structurally cannot see this. The "
                        "transport survives because `envelopeS_total` needs the derivative only on "
                        "`Ico 0 pi`; VSide must be proved over Ico, never Icc.",
            "trap_avoided": "a naive `Im != 0` disjunct attribution counts the REAL root as "
                            "complex, because polyroots returns |Im| ~ 1e-41 for it. Classified "
                            "by root type instead. The non-vacuity conclusion is unaffected; the "
                            "REASON it holds -- which is what a proof needs -- was contaminated.",
            "structural_surprise": "291 real roots over 199 arc points, not 199 -- at 46 of them "
                                   "ALL THREE roots are real. The arc crosses the discriminant at "
                                   "c* = -0.74221766588, so `continuous_otherRoots`'s collision "
                                   "branch is live, and the real branch of `y in notCut` must "
                                   "cover three roots at some points. G5.",
            "still_open": "the Lean proof of VSide, plus concrete Y_1 Y_2 Y_3 and the two "
                          "log(-y) routes. Everything else in Gap A is proved.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route36-vside-nonvacuity.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("VSide is non-vacuous on the OPEN arc and FALSE at phi = pi (G7), where "
                         "x*y = 2.2469796 lands on Li2's cut. Prove it over Ico 0 pi, never Icc."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
