#!/usr/bin/env python3
"""Route 36 -- `VSide` is NON-VACUOUS on the arc, and which disjunct carries it.

Bean `qou-glbl` (Gap A), the assembly step. Run BEFORE writing any Lean for
`VSide`, because `VSide` is the hypothesis that was once **vacuous**: correction
6 on PR #4701 found an earlier version carrying `−y in slitPlane`, which fails
at ALL 199 arc points because exactly one root is real and positive at every
phi. A theorem carrying it was true and about nothing.

So the first question about the corrected `VSide` is not "can I prove it" but
"is it satisfiable at all". It is: all six conditions hold SIMULTANEOUSLY at
every one of the 597 checks.

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
from mpmath import exp, fabs, im, mp, mpc, mpf, nstr, pi, polyroots, re, sqrt


def roots_at(ph):
    """The three y-roots of the deformed curve at x = exp(i*phi)."""
    x = exp(mpc(0, 1) * ph)
    return polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                     maxsteps=200, extraprec=200)


def in_not_cut(w):
    """Lean's `notCut = {w | Im w != 0 or Re w < 1}` -- Li2's cut is [1, inf)."""
    return (im(w) != 0) or (re(w) < 1)


def main() -> int:
    mp.dps = 40
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

    # ---- G3: x*y and y/x are NEVER real on the arc -------------------------
    worst_xy, worst_ydx = None, None
    at_xy = None
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        x = exp(mpc(0, 1) * ph)
        for y in roots_at(ph):
            a, b = fabs(im(x * y)), fabs(im(y / x))
            if worst_xy is None or a < worst_xy:
                worst_xy, at_xy = a, ph
            if worst_ydx is None or b < worst_ydx:
                worst_ydx = b
    gates.append({
        "gate": "G3",
        "claim": "x*y and y/x are NEVER real on the arc -- both are carried by Im != 0 at every "
                 "one of the 597 checks, with a genuine margin rather than a near-miss. So their "
                 "notCut membership needs no case split at all, unlike `y`'s. This is the cheapest "
                 "part of VSide to prove and `exists_pinning_data` already supplies part of it: "
                 "it gives (x*y_3).im < 0, and (x*y_2).im < 0 when c < 0",
        "min_abs_Im_x_times_y": nstr(worst_xy, 10) if worst_xy is not None else None,
        "at_phi": nstr(at_xy, 10) if at_xy is not None else None,
        "min_abs_Im_y_over_x": nstr(worst_ydx, 10) if worst_ydx is not None else None,
        "margin_is_genuine_not_noise": bool(worst_xy is not None and worst_xy > mpf(10) ** -6),
        "pass": bool(worst_xy is not None and worst_xy > mpf(10) ** -6),
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
