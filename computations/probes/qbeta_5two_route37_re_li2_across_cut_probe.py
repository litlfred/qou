#!/usr/bin/env python3
"""Route 37 -- `Re Li2` IS continuous across the cut, and the inversion formula
proves it. Route 36 G11's remaining obligation, priced before any Lean.

Bean `qou-glbl`, obligation (2): `envelope_integrate` wants
`ContinuousOn S (Icc 0 pi)` -- the CLOSED interval -- and at `phi = pi` two of
the three `Li2` arguments land exactly on the cut at `w0 = 2.2469796`.

G11 recorded the residue as "dominated convergence alone -- a uniform integrable
bound for ||log(1-wt)/t|| near w0". THAT IS NOT AVAILABLE, and this probe was
written after noticing why: the log singularity of the integrand sits at
`t = 1/w`, which MOVES with `w`. For each fixed `t` near `1/w0` there is a `w`
arbitrarily close to `w0` (namely `w = 1/t`, real, in the approach set) making
`|log(1-wt)|` arbitrarily large. So

    sup over the approach neighbourhood of |log(1-wt)/t|  =  +infinity  pointwise,

and no `w`-independent dominating function exists at all. Plain dominated
convergence cannot close G11; the obligation as recorded was not merely unpriced
but unachievable in that form. (Vitali / uniform integrability would work, and
is not in Mathlib in a usable shape.)

WHAT REPLACES IT
----------------
The inversion formula, on `C \\ [0,inf)`:

    Li2(w) + Li2(1/w) + log(-w)^2 / 2  =  -pi^2/6.

Every term on the right of `Li2(w) = -pi^2/6 - Li2(1/w) - log(-w)^2/2` is
harmless at `w0`: `1/w0 = 0.4450419` is an INTERIOR point of the domain of
analyticity (`Li2` is already known analytic on `C \\ [1,inf)` in the tree), and
`log(-w)^2` is elementary with a discontinuity only in its imaginary part. So
the singular structure at `w0` is entirely carried by an elementary function,
and `Re` kills what is left. `envelopeS` takes `.re` of every term, so `Re` is
exactly what the transport needs.

This is the FOURTH downward revision of this obligation: "2-D continuity of
Re Li2" -> "one-sided" -> "one-sided minus what Mathlib supplies" -> "not a
convergence theorem at all, an algebraic identity plus one already-proved
theorem (`re_inversion_identity`)". And the third revision's framing was wrong
in a way the first one was not: it named a technique that cannot work.

⚠ WHAT IS BEING MEASURED, AND AGAINST WHICH CONVENTION
------------------------------------------------------
`Li2` here means Lean's `cLiTwoExt w = -int_0^1 log(1 - w*t)/t dt` with Lean's
principal `Complex.log` (arg in (-pi, pi]), NOT mpmath's `polylog`. The two
agree off the cut (G1 checks that) and DISAGREE on it: at real `x > 1` the
integrand's `1 - x*t` is a negative real for `t > 1/x`, where Lean's branch
takes `arg = +pi`, so Lean's value is the boundary value from BELOW,
`Li2(x - i0)`, with `Im = -pi*log x`. Getting this backwards would put the sign
of the `log(-w)^2` correction the wrong way round and every gate here would
still "pass" against a self-consistent wrong reference. G3 pins it against the
independently-known jump `2*pi*i*log x`.

⚠ THE QUADRATURE TRAP THIS LANE HAS ALREADY BEEN BITTEN BY
-----------------------------------------------------------
`quad(f, [0, 1])` on this integrand converges to the WRONG value whenever
`Re(1/w)` is in `(0,1)` -- the log singularity is interior and mpmath's
tanh-sinh does not see it. A partial fix that splits only when `1/w` is EXACTLY
real repairs the on-cut reference value and leaves every off-cut comparison
quietly wrong, which is worse than not fixing it. Here the split point is
`Re(1/w)` whenever it lies in `(0,1)`, independent of `Im(1/w)`. G0 is a
regression gate on exactly that: it re-runs the unsplit quadrature and requires
it to DISAGREE, so the split cannot be silently deleted.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (arg, cos, exp, fabs, im, log, mp, mpc, mpf, nstr, pi,
                    polylog, polyroots, quad, re, sin, sqrt)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def li2_ext(w):
    """Lean's `cLiTwoExt w = -int_0^1 log(1 - w*t)/t dt`, principal branch.

    The `1/t` singularity at `t = 0` is removable (`log(1-wt)/t -> -w`); the
    LOG singularity at `t = 1/w` is not, and the quadrature must be split there
    whenever `Re(1/w)` lands in `(0,1)` -- see the module docstring.
    """
    if w == 0:
        return mpc(0, 0)

    def f(t):
        if t == 0:
            return -w
        return log(1 - w * t) / t

    c = re(1 / w)
    pts = [mpf(0), c, mpf(1)] if 0 < c < 1 else [mpf(0), mpf(1)]
    return -quad(f, pts)


def li2_ext_unsplit(w):
    """The WRONG version -- no split at the interior log singularity. G0 only."""
    def f(t):
        if t == 0:
            return -w
        return log(1 - w * t) / t

    return -quad(f, [mpf(0), mpf(1)])


def inv_combo(w):
    """`invCombo w = Li2(w) + Li2(1/w) + log(-w)^2 / 2`, Lean's spelling."""
    return li2_ext(w) + li2_ext(1 / w) + log(-w) ** 2 / 2


def in_inv_domain(w):
    """Lean's `invDomain = -slitPlane = C \\ [0,inf) = {w | Re w < 0 or Im w != 0}`."""
    return (re(w) < 0) or (im(w) != 0)


def roots_at(ph):
    """The three y-roots of the deformed curve at x = exp(i*phi)."""
    x = exp(mpc(0, 1) * ph)
    return polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                     maxsteps=200, extraprec=200)


def main() -> int:
    set_compute_dps()
    gates = []

    # The three roots at phi = pi are the roots of `unitCubic (-1) t = t^3 + 2t^2 - t - 1`.
    # `Ypair.2` is the most negative of them; `x = -1`, so `x*y = -Ypair.2 > 1` is
    # the point ON the cut where the transport needs continuity. Built from the
    # cubic rather than typed in, so it is the same number the rest of the lane uses.
    endpoint_roots = sorted(re(r) for r in polyroots([1, 2, -1, -1],
                                                     maxsteps=200, extraprec=200))
    w0 = -endpoint_roots[0]               # 2.2469796 = 1 + 2*cos(2*pi/7)
    y_real_pi = endpoint_roots[2]         # 0.8019377 = 2*cos(pi/7) - 1, Route 36 G6

    # ---- G0: the split is LOAD-BEARING (regression gate) --------------------
    unsplit_gap = mpf(0)
    for w in [mpc("2.2469796", 0), mpc("2.2469796", "-0.001"),
              mpc("3.7", "0.4"), mpc("-5.5", "0.25")]:
        c = re(1 / w)
        if 0 < c < 1:
            d = fabs(li2_ext(w) - li2_ext_unsplit(w))
            unsplit_gap = max(unsplit_gap, d)
    gates.append({
        "gate": "G0",
        "claim": "REGRESSION GATE on the quadrature split. Re-runs the integral WITHOUT splitting "
                 "at the interior log singularity `t = Re(1/w)` and requires the answer to be "
                 "DIFFERENT. This lane has already shipped a partial fix that split only when "
                 "`1/w` was exactly real -- which repaired the on-cut reference value and left "
                 "every off-cut comparison wrong, i.e. looked converged and was not. If someone "
                 "deletes the split, this gate fails instead of the numbers quietly drifting",
        "worst_gap_between_split_and_unsplit": nstr(unsplit_gap, 12),
        "pass": bool(unsplit_gap > mpf(10) ** -6),
    })

    # ---- G1: `li2_ext` agrees with mpmath's polylog OFF the cut -------------
    # An independent implementation, so this is a check on the integral routine
    # itself rather than on the identity it will be used to test.
    off_cut = [mpc("0.3", "0.4"), mpc("-1.7", "0.9"), mpc("-3", 0), mpc("0.5", 0),
               mpc("2.2469796", "0.35"), mpc("2.2469796", "-0.35"),
               mpc("-0.25", "-1.4"), mpc("5", "2")]
    worst_polylog = mpf(0)
    for w in off_cut:
        worst_polylog = max(worst_polylog, fabs(li2_ext(w) - polylog(2, w)))
    gates.append({
        "gate": "G1",
        "claim": "the integral used here reproduces mpmath's `polylog(2, .)` at 8 points off the "
                 "cut, including both sides of the cut at the target's real part. So every later "
                 "gate is testing an IDENTITY, not testing a quadrature against itself",
        "points": len(off_cut),
        "worst_abs_difference": nstr(worst_polylog, 12),
        "pass": bool(worst_polylog < mpf(10) ** -20),
    })

    # ---- G2: the inversion identity on C \ [0,inf) --------------------------
    # Points chosen OFF the arc configuration: the identity is being checked
    # where it will NOT be used, so a coincidence peculiar to the 5_2 locus
    # cannot carry it.
    probe_pts = [mpc("0.3", "0.4"), mpc("-1.7", "0.9"), mpc("-3", 0), mpc("-1", 0),
                 mpc("-0.2", 0), mpc("0.5", "0.5"), mpc("5", "2"), mpc("5", "-2"),
                 mpc("-0.25", "-1.4"), mpc("0.9", "-0.05"), mpc("1", "0.001"),
                 mpc("1", "-0.001"), mpc("2.2469796", "0.35"),
                 mpc("2.2469796", "-0.35"), mpc("100", "0.5"), mpc("-1000", 0)]
    K = -(pi ** 2) / 6
    worst_inv = mpf(0)
    worst_pt = None
    for w in probe_pts:
        assert in_inv_domain(w), f"probe point {w} is not in invDomain"
        d = fabs(inv_combo(w) - K)
        if d > worst_inv:
            worst_inv, worst_pt = d, w
    gates.append({
        "gate": "G2",
        "claim": "THE IDENTITY THE LEAN PROOF RESTS ON: Li2(w) + Li2(1/w) + log(-w)^2/2 = -pi^2/6 "
                 "on all of C \\ [0,inf), as a FULL COMPLEX equation (not just its real part). "
                 "Checked at 16 points spread over both half planes, the negative reals, both "
                 "sides of the cut, near the branch point w = 1, and far out -- all OFF the 5_2 "
                 "arc configuration, so nothing peculiar to that locus can be carrying it",
        "points": len(probe_pts),
        "worst_abs_residual": nstr(worst_inv, 12),
        "worst_point": nstr(worst_pt, 12) if worst_pt is not None else None,
        "pass": bool(worst_inv < mpf(10) ** -20),
    })

    # ---- G3: which boundary value Lean's branch actually computes -----------
    # If this is backwards, every other gate still passes against a
    # self-consistent wrong reference. Pinned against the KNOWN jump 2*pi*i*log x.
    worst_jump = mpf(0)
    worst_side = mpf(0)
    eps = mpf(10) ** -25
    for x in [mpf("1.3"), w0, mpf("4.5"), mpf("17")]:
        above = li2_ext(mpc(x, eps))
        below = li2_ext(mpc(x, -eps))
        # independently known: Li2(x+i0) - Li2(x-i0) = 2*pi*i*log x
        worst_jump = max(worst_jump, fabs((above - below) - 2 * pi * mpc(0, 1) * log(x)))
        # Lean's on-cut value must be the limit from BELOW, not from above
        worst_side = max(worst_side, fabs(li2_ext(mpc(x, 0)) - below))
    gates.append({
        "gate": "G3",
        "claim": "BRANCH PINNING, and the gate that stops this probe from being self-consistently "
                 "wrong. Lean's `Complex.log` takes arg = +pi on the negative reals, so for real "
                 "x > 1 the integrand's `1 - x*t` past t = 1/x is evaluated on the UPPER lip of "
                 "log's cut -- which makes `cLiTwoExt x` the boundary value from BELOW in w, "
                 "Li2(x - i0), with Im = -pi*log x. Checked against the independently known jump "
                 "Li2(x+i0) - Li2(x-i0) = 2*pi*i*log x. Get this backwards and the sign of the "
                 "log(-w)^2 correction flips while every other gate still passes",
        "jump_residual": nstr(worst_jump, 12),
        "on_cut_equals_limit_from_below": nstr(worst_side, 12),
        "pass": bool(worst_jump < mpf(10) ** -18 and worst_side < mpf(10) ** -18),
    })

    # ---- G4: Re is continuous across the cut, Li2 itself is NOT -------------
    # Gated on the RATIO gap/eps, not on the gap: the gap at eps = 1e-3 is 2.4e-3
    # and a fixed small threshold would simply be reporting how small eps was.
    # `Re Li2` has a one-sided derivative of modulus pi/x in the imaginary
    # direction, so gap/eps must stay bounded by pi/1.3 < 2.42 across every
    # decade -- a Lipschitz statement, which a single small residual is not.
    worst_ratio, im_gap = mpf(0), mpf(0)
    ratio_by_decade = {}
    for x in [mpf("1.3"), w0, mpf("4.5")]:
        v0 = li2_ext(mpc(x, 0))
        for k in (3, 6, 10, 15, 20, 25):
            e = mpf(10) ** -k
            for s in (1, -1):
                v = li2_ext(mpc(x, s * e))
                r = fabs(re(v) - re(v0)) / e
                worst_ratio = max(worst_ratio, r)
                ratio_by_decade[f"1e-{k}"] = nstr(max(
                    mpf(ratio_by_decade.get(f"1e-{k}", "0")), r), 8)
                if s == 1:
                    im_gap = max(im_gap, fabs(im(v) - im(v0)))
    gates.append({
        "gate": "G4",
        "claim": "the statement being proved, measured directly: Re cLiTwoExt is continuous at "
                 "cut points from BOTH sides, while cLiTwoExt itself is NOT -- the imaginary part "
                 "jumps by 2*pi*log x. Gated on the RATIO gap/eps rather than on the gap, because "
                 "the gap at eps = 1e-3 is 2.4e-3 and any fixed small threshold would just be "
                 "reporting how small eps was. The ratio is bounded by pi/x < 2.42 over SIX "
                 "decades, which is a Lipschitz statement a single residual cannot make. So `.re` "
                 "is load-bearing and a theorem about `cLiTwoExt` unqualified would be FALSE",
        "worst_ratio_re_gap_over_eps": nstr(worst_ratio, 12),
        "ratio_by_decade": ratio_by_decade,
        "predicted_bound_pi_over_smallest_x": nstr(pi / mpf("1.3"), 12),
        "im_gap_from_above": nstr(im_gap, 12),
        "pass": bool(worst_ratio < pi / mpf("1.3") and im_gap > 1),
    })

    # ---- G5: the arg-sum side condition, and where it FAILS -----------------
    # `log(1 - 1/w) + log(-w) = log(1 - w)` needs arg(1-1/w) + arg(-w) in (-pi, pi].
    # That is the one non-formal step in the derivative computation.
    holds_in_domain = 0
    worst_margin = pi
    for w in probe_pts:
        s = arg(1 - 1 / w) + arg(-w)
        assert fabs(log((1 - 1 / w) * (-w)) - log(1 - w)) < mpf(10) ** -30
        if -pi < s <= pi:
            holds_in_domain += 1
            worst_margin = min(worst_margin, min(s + pi, pi - s))
    # and it FAILS on (0,1), which is why the domain excludes [0,inf)
    fails_outside = []
    for x in [mpf("0.2"), mpf("0.5"), mpf("0.9")]:
        w = mpc(x, 0)
        s = arg(1 - 1 / w) + arg(-w)
        if not (-pi < s <= pi):
            fails_outside.append(nstr(x, 6))
    gates.append({
        "gate": "G5",
        "claim": "the ONE non-formal step in the derivative computation -- "
                 "log(1 - 1/w) + log(-w) = log(1 - w) needs arg(1-1/w) + arg(-w) in (-pi, pi], "
                 "which is NOT automatic. It holds throughout C \\ [0,inf) because the two args "
                 "have strictly opposite signs there, and it FAILS on (0,1) where both are +pi "
                 "and the sum is 2*pi. So the domain restriction is load-bearing rather than "
                 "defensive, and dropping it gives a false lemma rather than a harder one",
        "in_domain_points_holding": holds_in_domain,
        "in_domain_points_total": len(probe_pts),
        "worst_distance_to_the_endpoints_of_(-pi,pi]": nstr(worst_margin, 12),
        "fails_at_these_points_of_(0,1)": fails_outside,
        "pass": bool(holds_in_domain == len(probe_pts) and len(fails_outside) == 3),
    })

    # ---- G6: the elementary rewrite that makes Re log(-w)^2 continuous ------
    # ((log (-w))^2).re = (log |w|)^2 - (|arg w| - pi)^2, valid for every w != 0.
    worst_sq = mpf(0)
    for w in probe_pts + [mpc("0.5", 0), mpc("2", 0), mpc("0.3", "-0.7")]:
        lhs = re(log(-w) ** 2)
        rhs = log(fabs(w)) ** 2 - (fabs(arg(w)) - pi) ** 2
        worst_sq = max(worst_sq, fabs(lhs - rhs))
    gates.append({
        "gate": "G6",
        "claim": "the elementary rewrite that carries the whole continuity claim: "
                 "Re(log(-w)^2) = (log|w|)^2 - (|arg w| - pi)^2 for every w != 0. `arg(-w)` jumps "
                 "by 2*pi across the positive reals; `|arg w|` does not jump there at all, so the "
                 "right-hand side is manifestly continuous at every w with Re w > 0. Checked "
                 "including on the positive reals, on the negative reals, and in both half planes "
                 "-- i.e. ON the jump locus, not merely near it",
        "points": len(probe_pts) + 3,
        "worst_abs_residual": nstr(worst_sq, 12),
        "pass": bool(worst_sq < mpf(10) ** -30),
    })

    # ---- G7: cross-check against the tree's `re_inversion_identity` ---------
    # Re cLiTwoExt(x) + Re cLiTwoExt(1/x) + (log x)^2/2 = pi^2/3   for x >= 1,
    # already proved in ComplexDilogarithmOnCut.lean. The new real-part step is
    # exactly this identity rearranged, so a mismatch here means the Lean
    # assembly cannot close.
    worst_tree = mpf(0)
    for x in [mpf(1), mpf("1.3"), w0, mpf("4.5"), mpf("17")]:
        lhs = re(li2_ext(mpc(x, 0))) + re(li2_ext(mpc(1 / x, 0))) + log(x) ** 2 / 2
        worst_tree = max(worst_tree, fabs(lhs - pi ** 2 / 3))
        # and the rearrangement the Lean proof actually performs
        worst_tree = max(worst_tree, fabs(re(inv_combo(mpc(x, 0))) + pi ** 2 / 6))
    gates.append({
        "gate": "G7",
        "claim": "CROSS-CHECK against what the tree already proves: `re_inversion_identity` says "
                 "Re Li2(x) + Re Li2(1/x) + (log x)^2/2 = pi^2/3 for x >= 1. The new step is that "
                 "identity rearranged into Re(invCombo x) = -pi^2/6, so the two must agree "
                 "numerically or the Lean assembly cannot close. Checked at the branch point "
                 "x = 1 as well, where the derivative argument behind the tree's theorem does not "
                 "exist and its exceptional-point glue is what covers it",
        "worst_abs_residual": nstr(worst_tree, 12),
        "pass": bool(worst_tree < mpf(10) ** -18),
    })

    # ---- G8: the actual 5_2 configuration, both approach directions ---------
    # At phi -> pi, `x*Ypair.2` reaches w0 from BELOW and `Ypair.2/x` from ABOVE.
    # One-sided results alone would need BOTH sides; the 2-D theorem covers them.
    sides = {"x_times_y": set(), "y_over_x": set()}
    worst_arc_ratio = mpf(0)
    arc_by_decade = {}
    ref = re(li2_ext(mpc(w0, 0)))
    for k in (1, 2, 3, 4, 5, 6):
        delta = mpf(10) ** -k
        ph = pi - delta
        x = exp(mpc(0, 1) * ph)
        # the branch reaching the cut is the most negative real root
        y = min((r for r in roots_at(ph) if fabs(im(r)) < mpf(10) ** -25), key=re)
        worst_here = mpf(0)
        for name, val in (("x_times_y", x * y), ("y_over_x", y / x)):
            sides[name].add("below" if im(val) < 0 else "above")
            worst_here = max(worst_here, fabs(re(li2_ext(val)) - ref))
        arc_by_decade[f"pi-1e-{k}"] = nstr(worst_here, 8)
        worst_arc_ratio = max(worst_arc_ratio, worst_here / delta)
    gates.append({
        "gate": "G8",
        "claim": "the configuration this is FOR: as phi -> pi the branch Ypair.2 sends `x*y` to "
                 "the cut point w0 from BELOW and `y/x` to the SAME point from ABOVE. A one-sided "
                 "continuity theorem would therefore have to be proved twice, in mirror image; "
                 "the 2-D statement covers both at once. Convergence is gated on the RATIO "
                 "gap/(pi - phi) staying bounded over six decades, not on a small gap at the "
                 "finest sample -- the same reason as G4, and here the root itself is also moving",
        "x_times_y_approach_sides": sorted(sides["x_times_y"]),
        "y_over_x_approach_sides": sorted(sides["y_over_x"]),
        "re_gap_to_on_cut_value_by_decade": arc_by_decade,
        "worst_ratio_gap_over_delta": nstr(worst_arc_ratio, 12),
        "pass": bool(sides["x_times_y"] == {"below"} and sides["y_over_x"] == {"above"}
                     and worst_arc_ratio < 10),
    })

    # ---- G9: the base point, and that it is the only computable one ---------
    base = inv_combo(mpc(-1, 0))
    gates.append({
        "gate": "G9",
        "claim": "the constant is pinned at w = -1, where BOTH dilogarithm terms are "
                 "cLiTwoExt(-1) = -pi^2/12 (already in the tree, `cLiTwoExt_neg_one`) and "
                 "log(-w) = log 1 = 0 kills the third. -1 is an INTERIOR point of C \\ [0,inf), "
                 "so no boundary limit is needed -- which is why the domain is taken to be the "
                 "whole slit plane C \\ [0,inf) rather than a half plane. On a half plane the "
                 "only computable base point sits on the boundary and the constant would have to "
                 "be recovered by a limit",
        "invCombo_at_minus_one": nstr(base, 20),
        "target_minus_pi_sq_over_6": nstr(-(pi ** 2) / 6, 20),
        "minus_one_is_interior": bool(in_inv_domain(mpc(-1, 0))),
        "pass": bool(fabs(base - K) < mpf(10) ** -25 and in_inv_domain(mpc(-1, 0))),
    })

    # ---- G10: w0 is the number the rest of the lane uses --------------------
    tol10 = mpf(10) ** -(mp.dps - 5)
    d_w0 = fabs(w0 - (1 + 2 * cos(2 * pi / 7)))
    d_yr = fabs(y_real_pi - (2 * cos(pi / 7) - 1))
    gates.append({
        "gate": "G10",
        "claim": "the cut point is the number the rest of the lane uses. Route 36 G6 identified "
                 "the REAL branch at phi = pi as 2*cos(pi/7) - 1 = 0.8019377; the branch that "
                 "reaches the CUT is a different root of the same cubic, Ypair.2 = -2.2469796, "
                 "giving x*y = 1 + 2*cos(2*pi/7). Both are checked, from the cubic rather than "
                 "from transcribed decimals -- an earlier draft of this gate compared w0 against "
                 "2*cos(pi/7) - 1 and was off by exactly 1, i.e. was comparing two different roots",
        "w0_from_cubic": nstr(w0, 20),
        "one_plus_two_cos_2pi_over_7": nstr(1 + 2 * cos(2 * pi / 7), 20),
        "w0_difference": nstr(d_w0, 12),
        "y_real_at_pi_from_cubic": nstr(y_real_pi, 20),
        "two_cos_pi_over_7_minus_1": nstr(2 * cos(pi / 7) - 1, 20),
        "y_real_difference": nstr(d_yr, 12),
        "pass": bool(d_w0 < tol10 and d_yr < tol10),
    })

    out = {
        "probe": "qbeta_5two_route37_re_li2_across_cut",
        "bean": "qou-glbl", "dps": mp.dps,
        "pairs_with_lean": [
            "QOU/MathlibExt/ComplexDilogarithmInversion.lean (invCombo, continuousAt_re_cLiTwoExt)",
            "QOU/MathlibExt/ComplexDilogarithmOnCut.lean (re_inversion_identity)",
        ],
        "gates": gates,
        "verdict": {
            "measured": "Re cLiTwoExt is continuous at every point of the cut (1, inf), from both "
                        "sides, while cLiTwoExt itself is not. The carrier is the inversion "
                        "identity Li2(w) + Li2(1/w) + log(-w)^2/2 = -pi^2/6 on C \\ [0,inf).",
            "obligation_retired": "G11's 'dominated convergence alone' is NOT achievable: the log "
                                  "singularity of log(1-wt)/t sits at t = 1/w and MOVES with w, so "
                                  "sup over any approach neighbourhood is +infinity at every t "
                                  "near 1/w0 and no w-independent dominating function exists. The "
                                  "recorded next step named a technique that cannot work.",
            "why_re": "cLiTwoExt jumps by 2*pi*i*log x across the cut -- purely imaginary. "
                      "`envelopeS` takes `.re` of every term, so the jump is invisible to it. A "
                      "theorem about cLiTwoExt unqualified would be FALSE (G4).",
            "branch": "Lean's cLiTwoExt at real x > 1 is the boundary value from BELOW, "
                      "Li2(x - i0), Im = -pi*log x -- because Lean's Complex.log takes arg = +pi "
                      "on the negative reals where 1 - x*t sits for t > 1/x (G3).",
            "still_open": "obligation (1), he_j at the pair (k = 0), unaffected by this.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route37-re-li2-across-cut.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']:>3}  pass={g['pass']}  {g['claim'][:80]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("Re cLiTwoExt is continuous across the cut, carried by the inversion "
                         "identity on C \\ [0,inf). G11's dominated-convergence route is closed "
                         "as unachievable, not merely unpriced."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
