#!/usr/bin/env python3
"""Can this arc's extrapolation DECIDE whether rho_inf = 2*sqrt(6)/5?  Measured: no, by 9.5x.

WHY THIS PROBE EXISTS.  `wlambda_covariance_epic_M1_margin_leg_decomposition.py` annotated the
merged-#5901 constant

    RHO_INF = 0.979796195657          # = 2 sqrt(6)/5

with a bare `=`.  The candidate is 2*sqrt(6)/5 = sqrt(24/25) = 0.9797958971133..., which differs
from the literal by 3.05e-07 relative -- they agree through SIX significant digits and part at the
seventh.  Read naively that looks like a refutation.  It is not, and the reason is measurable
rather than rhetorical.

THE METHOD IS CALIBRATABLE, WHICH IS THE WHOLE POINT.  RHO_INF is not a closed form; it is a
Richardson extrapolation of rho_P(theta) as theta -> infinity, run on a finite theta ladder.  The
sibling probe `wlambda_covariance_epic_M1_CA_to_margin_conversion.py` performs the SAME
extrapolation, on the SAME ladder, from the SAME `ingredients()` call, for a quantity whose exact
limit IS known:

    V_A / theta^2  ->  8 / pi^2      (exact)

So we can ask the method how well it does when we already know the answer, and only then ask it a
question we do not know the answer to.  That calibration is what this probe measures.

WHAT IT REPORTS
  1. the extrapolated V_A/theta^2 against exact 8/pi^2  -- the method's DEMONSTRATED error;
  2. the extrapolated rho against the recorded literal and against 2*sqrt(6)/5;
  3. the ratio (method error) / (gap between the two rho candidates), i.e. whether the arc's own
     numerics can separate them at all.

Nothing is extrapolated here that the arc does not already extrapolate; the only new thing is
running the known-answer case and the unknown case side by side and quoting the ratio.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged.  Writes no witness -- it decides an
epistemic question about existing constants and produces no new number for anyone to consume.
Bean qou-742w.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import mpmath as mp

mp.mp.dps = 40

# The ladder the arc itself uses, so the calibration is of the arc's numbers and not of a
# differently-tuned rerun.
THETAS = (80, 160, 320, 640, 1280, 2560)

# A longer ladder is the only thing that can move this verdict, so make it reachable:
#   python3 <this> 160 320 640 1280 2560 5120 10240
# The default is the arc's own ladder, so the calibration is of the arc's numbers.
if len(sys.argv) > 1:
    THETAS = tuple(int(a) for a in sys.argv[1:])

RHO_LITERAL = mp.mpf('0.979796195657')   # merged #5901, as recorded


def _load_ingredients():
    """The debye-CA probe's `ingredients()`, by explicit path (the _path_bridge bootstrap trap)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_debye_CA_investigation.py"
    spec = importlib.util.spec_from_file_location("_m1_debye_ca_rho", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def richardson(t, s):
    """The arc's own extrapolation: fit the decay exponent from the last three points, then
    accelerate.  Identical in form to CA_to_margin_conversion.py's v_A extraction."""
    a = mp.log(abs((s[-3] - s[-2]) / (s[-2] - s[-1]))) / mp.log(t[-2] / t[-3])
    r = t[-1] / t[-2]
    return s[-1] + (s[-1] - s[-2]) / (r ** a - 1), a


def main() -> int:
    mod = _load_ingredients()
    print(f"# can the arc's extrapolation decide rho_inf = 2 sqrt(6)/5?  dps={mp.mp.dps}; NO float64")
    print(f"# ladder theta = {list(THETAS)}")
    print("#")

    ts, vs, rs = [], [], []
    for th in THETAS:
        M = int(mp.floor(2 * mp.sqrt(th) + 8 * mp.power(mp.mpf(th), mp.mpf(1) / 6) + 20))
        VA, _VW, _P, rho = mod.ingredients(mp.mpf(th), M)
        ts.append(mp.mpf(th)); vs.append(VA / mp.mpf(th) ** 2); rs.append(rho)
        print(f"#   theta={th:>5}  M={M:>4}  V_A/theta^2={mp.nstr(vs[-1], 12):>16}  "
              f"rho={mp.nstr(rho, 13):>16}")
    print("#")

    # 1. CALIBRATION -- the same method on a quantity whose limit is known exactly.
    v_ext, v_a = richardson(ts, vs)
    v_exact = 8 / mp.pi ** 2
    method_err = abs(v_ext - v_exact) / v_exact
    print("# 1. CALIBRATION (known answer)")
    print(f"#    V_A/theta^2 extrapolated = {mp.nstr(v_ext, 12)}   (decay exponent {mp.nstr(v_a, 5)})")
    print(f"#    exact 8/pi^2             = {mp.nstr(v_exact, 12)}")
    print(f"#    METHOD ERROR             = {mp.nstr(method_err, 4)}")
    print("#")

    # 2. THE QUESTION -- the same method, unknown answer.
    r_ext, r_a = richardson(ts, rs)
    cand = 2 * mp.sqrt(6) / 5
    gap = abs(RHO_LITERAL - cand) / cand
    print("# 2. THE QUESTION (unknown answer)")
    print(f"#    rho extrapolated here    = {mp.nstr(r_ext, 13)}   (decay exponent {mp.nstr(r_a, 5)})")
    print(f"#    recorded RHO_INF         = {mp.nstr(RHO_LITERAL, 13)}")
    print(f"#    candidate 2 sqrt(6)/5    = {mp.nstr(cand, 13)}")
    print(f"#    gap between candidates   = {mp.nstr(gap, 4)}")
    print(f"#    this run vs literal      = {mp.nstr(abs(r_ext - RHO_LITERAL) / RHO_LITERAL, 4)}")
    print(f"#    this run vs candidate    = {mp.nstr(abs(r_ext - cand) / cand, 4)}")
    print("#")

    # 3. HOW THE METHOD ERROR DECAYS, and therefore what WOULD decide this.
    #
    # Run the calibration on nested sub-ladders of the ladder we were given -- points 0..3, 1..4,
    # 2..5 and so on -- and watch the known-answer error shrink as theta_max grows.  Fitting that
    # decay converts "still open" into a COST: the theta_max at which the method error drops a
    # decade below the candidate gap, i.e. at which the question becomes decidable.  This is the
    # only part of the probe that is forward-looking, and it is measured from this run's own data
    # rather than quoted from a previous one.
    sub = []
    for j in range(3, len(ts)):
        e, _ = richardson(ts[:j + 1], vs[:j + 1])
        sub.append((ts[j], abs(e - v_exact) / v_exact))
    print("# 3. HOW THE METHOD ERROR DECAYS (nested sub-ladders, known answer)")
    for tmax, err in sub:
        print(f"#    ladder ending theta={int(tmax):>6}   method error = {mp.nstr(err, 4)}")
    target = gap / 10
    # Fit an exponent from EVERY consecutive pair, not just the last one.  The decay is not a
    # clean power law here and a single-pair fit hides that: quote the SPREAD.
    exps = []
    for (t0, e0), (t1, e1) in zip(sub, sub[1:]):
        if e0 > 0 and e1 > 0 and e0 != e1:
            exps.append(mp.log(e0 / e1) / mp.log(t1 / t0))
    if exps:
        print(f"#    fitted decay exponents, pairwise: "
              f"{', '.join(mp.nstr(e, 4) for e in exps)}")
    costs = []
    for pexp in exps:
        if pexp > 0:
            costs.append(sub[-1][0] * (sub[-1][1] / target) ** (1 / pexp))
    if costs:
        lo, hi = min(costs), max(costs)
        print(f"#    to reach a method error one DECADE below the gap ({mp.nstr(target, 3)}),")
        if len(costs) > 1 and hi / lo > 3:
            print(f"#    theta_max ~ {mp.nstr(lo, 3)} to {mp.nstr(hi, 3)} -- a {mp.nstr(hi/lo, 3)}x")
            print("#    SPREAD, because the exponents above disagree.  The decay is DECELERATING,")
            print("#    so the pessimistic end is the one to plan against; treat this as an")
            print("#    order-of-magnitude bound, not an estimate.")
        else:
            print(f"#    theta_max ~ {mp.nstr(hi, 3)}")
        # M ~ 2 sqrt(theta) and the inner loop is O(M^2), so work per point grows LINEARLY in
        # theta -- the two factors are the same number, which is why only one is printed.
        print(f"#    (M ~ {int(2 * mp.sqrt(hi) + 8 * mp.power(hi, mp.mpf(1)/6) + 20)} at the "
              f"pessimistic end; work per point is O(M^2) = O(theta), so ~"
              f"{mp.nstr(hi / sub[-1][0], 3)}x this run's cost at the top of the ladder)")
    print("#")

    # 4. THE VERDICT.
    ratio = method_err / gap
    print("# 4. VERDICT")
    print(f"#    (method error) / (candidate gap) = {mp.nstr(ratio, 4)}x")
    d_lit = abs(r_ext - RHO_LITERAL) / RHO_LITERAL
    d_can = abs(r_ext - cand) / cand
    print(f"#    this run lands CLOSER to the {'CANDIDATE' if d_can < d_lit else 'RECORDED LITERAL'}"
          f"  ({mp.nstr(min(d_can, d_lit), 4)} vs {mp.nstr(max(d_can, d_lit), 4)})")
    print("#    -- directional only; it is inside the method error and must not be quoted as")
    print("#       evidence for either value.")
    if ratio > 1:
        print("#    The gap sits BELOW the method's demonstrated error.  The recorded 12 digits")
        print("#    of RHO_INF are NOT converged past roughly the sixth, so they are not evidence")
        print("#    about the candidate either way.  2 sqrt(6)/5 is CONSISTENT with this arc's")
        print("#    numerics; it is neither confirmed nor refuted by them.  Write the")
        print("#    identification with `approx`, never `=` (AGENTS.md section 7ab).")
    else:
        print("#    The method resolves the gap.  Compare the two 'this run vs' lines above:")
        print("#    the smaller one is the value this ladder actually converges to.")
    print("#")
    print("#    NOTE the internal consistency: the known-answer case ALSO departs from truth in")
    print("#    its sixth significant digit.  Both are ~6-digit extrapolations written to 12.")

    # The third check USED to assert `ratio > 1` -- i.e. that the ladder CANNOT decide.  That was
    # right while the arc's own ladder (theta <= 2560) was the only evidence, and it is wrong now:
    # extending to theta = 40960 drives the method error to 9.9e-08, a third of the gap, and the
    # probe then FAILED ON ITS OWN SUCCESS.  An assertion that a question stays open is not a
    # check, it is a prediction, and this one expired.
    #
    # What is checkable either way is that the run reaches a DETERMINATE verdict:
    #   * undecidable  -- the method error covers the gap, so neither value is excluded; or
    #   * decided      -- the method error is below the gap AND the extrapolation sits within one
    #                     method error of exactly one candidate and more than one from the other.
    # The failure mode this rules out is the middle case: an error small enough to look decisive
    # while the extrapolation is ambiguous between the two, which would invite reading a coin flip
    # as a result.
    d_lit = abs(r_ext - RHO_LITERAL) / RHO_LITERAL
    d_can = abs(r_ext - cand) / cand
    near, far = min(d_lit, d_can), max(d_lit, d_can)
    undecidable = ratio > 1
    decided = (not undecidable) and near < method_err < far
    checks = [
        ("calibration ran", v_ext > 0),
        ("rho extrapolation ran", 0 < r_ext < 1),
        ("verdict is determinate (undecidable, or decided with one candidate inside the "
         "method error and the other outside)", undecidable or decided),
    ]
    if decided:
        which = "2*sqrt(6)/5" if d_can < d_lit else "the recorded literal"
        print("#")
        print(f"#    DECIDED: this ladder converges to {which}.")
        print(f"#      within one method error : {mp.nstr(near, 4)}  (method error "
              f"{mp.nstr(method_err, 4)})")
        print(f"#      outside it              : {mp.nstr(far, 4)}  = "
              f"{mp.nstr(far / method_err, 3)}x the method error")
    print("#")
    for name, ok in checks:
        print(f"#   [{'PASS' if ok else 'FAIL'}] {name}")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
