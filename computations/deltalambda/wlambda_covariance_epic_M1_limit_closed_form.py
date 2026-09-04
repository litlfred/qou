#!/usr/bin/env python3
"""M_1>0: the whole budget in CLOSED FORM, and whether the route closes.

Gap qou-k5r5, bean qou-t6hc leg A. Everything before this was measured. This is
computed: two quadratures over the limiting edge measure, no sampling.

THE LIMITING PICTURE
--------------------
The sampler established that the edge measure factorises -- Lam ~ Plancherel(n+1),
then two INDEPENDENT down-steps, each landing on a corner with probability
dim(Lam-c)/dim(Lam). In the limit:

  * the co-transition measure converges to the SEMICIRCLE law on [-2,2],
    density sqrt(4-x^2)/(2 pi) in units of sqrt(n) (Kerov);
  * so the two corner contents are i.i.d. semicircle;
  * the omega weight is (r-a)^2 (r+a) with r,a = max,min of the two |contents|;
  * D(c sqrt n)/sqrt n -> phi(c) := (Omega(c) - |c|)/2 with Omega the VKLS shape.

w_opp -> 1/2, EXACTLY, and the argument is one line
---------------------------------------------------
The omega weight depends on the two contents ONLY through their absolute values.
The semicircle is symmetric, so for each corner the sign is independent of the
magnitude, hence the sign PATTERN is independent of the weight. Therefore the
opposite-sign event has weight exactly P(opposite signs) = 1/2. No integral
needed. (Measured: 0.4567, 0.4735, 0.4806, 0.4862 at n = 100..800, rising to 1/2
from below.)

The same symmetry makes the limiting slope (phi(a) - phi(r))/(r - a) identical
for same- and opposite-sign edges, so S_same = S_opp = S/2 in the limit.

THE CONTROL, and it is what makes the rest trustworthy
------------------------------------------------------
This framework predicts S -> 2 E[(r^2-a^2)(phi(a)-phi(r))] / E[(r-a)^2(r+a)],
a number the corpus already knows by a completely different route (the
Ivanov-Olshanski Kerov CLT field): N/P -> 0.6605, with Q -> 0. The quadrature
gives 0.66046945 -- agreement to 0.005%. Reproducing an independently derived
constant is the check on every assumption above at once; without it these
integrals would be unfalsifiable.

THE VERDICT
-----------
Closure of the deterministic-bound route needs S_same + B_opp < 1.

  crude bound  |d_a - d_r| <= D(0)                     B_opp -> 0.675475
    (this is QOU.BraidKnot.M1EdgeCalculus.abs_diagLen_sub_transpose_le)
    total 1.005709  -- FAILS by 0.57%.

  refined, using two facts already available:
      N^tau(r)   <= min(r, D(0))          -- at most one drop per site, and
                                             D(0) drops in total on that side
      N^sigma(a) >= max(0, a - (l1 - D0)) -- at most (l1 - D0) NON-drops in total
    B_opp -> 0.669299,  total 0.999533 -- CLOSES, by 0.047%.

BOTH REFINEMENTS ARE ELEMENTARY AND LEAN-REACHABLE. The first is `D(c) >= D(0) - c`,
which is `diagLen_le_add_sub` already proved sorry-free; the second is the same
telescoping identity read from the other end. Neither needs new mathematics.

0.047% IS NOT A PROOF, AND THIS PROBE DOES NOT CLAIM ONE. Three reasons, stated
so nobody has to rediscover them:
  1. it is an ASYMPTOTIC statement. M_1 > 0 needs every n; exact verification
     reaches n = 60 and this reaches the limit, with the crossover unaddressed;
  2. a 0.047% margin leaves no room for the finite-n corrections, and the
     measured finite-n quantities approach these limits from BOTH directions
     (B_opp from below, Ehat from above), so the finite-n budget is worse before
     it is better;
  3. the semicircle co-transition limit is used, not proved here.

What it does establish is where the route stands: the crude bound misses by 0.57%
and elementary refinements of it reach the line. That is a much more specific
statement than "needs effective limit-shape estimates".

Honesty: quadrature only, no sampling, no fit; scope-(a); nothing wired; gap
qou-k5r5 stays OPEN.
"""
from __future__ import annotations
import json
import time
from pathlib import Path

from mpmath import asin, mp, mpf, nstr, pi, quad, sqrt

mp.dps = 25

NP_CORPUS = mpf("0.6605")     # the corpus's value, from the IO Kerov CLT field


def g(u):
    """Density of |X| for X ~ semicircle on [-2,2]."""
    return sqrt(4 - u ** 2) / pi


def Omega(x):
    """VKLS limit shape."""
    return (2 / pi) * (x * asin(x / 2) + sqrt(4 - x ** 2))


def phi(x):
    """D(x sqrt n)/sqrt n in the limit."""
    return (Omega(x) - x) / 2


def dbl(f):
    """E[f(|X|,|Y|)] for X, Y i.i.d. semicircle; split at u to help quadrature."""
    return quad(lambda u: quad(lambda v: f(u, v) * g(u) * g(v), [0, u, 2]), [0, 2])


def main():
    t0 = time.monotonic_ns()
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    D0 = 2 / pi
    L1 = mpf(2)
    W = dbl(lambda u, v: (u - v) ** 2 * (u + v))

    check("the framework reproduces phi(0) = 2/pi and phi(2) = 0",
          abs(phi(0) - D0) < mpf("1e-15") and abs(phi(2)) < mpf("1e-15"),
          f"phi(0) = {nstr(phi(0), 10)} against 2/pi = {nstr(D0, 10)}; "
          f"phi(2) = {nstr(phi(2), 3)}. The rescaled diagonal length starts at the "
          f"Durfee constant and vanishes at the edge of the support.")

    # ---- THE CONTROL: reproduce a constant derived by a different route ----
    S_inf = 2 * dbl(lambda u, v:
                    (max(u, v) ** 2 - min(u, v) ** 2)
                    * (phi(min(u, v)) - phi(max(u, v)))) / W
    rel = abs(S_inf - NP_CORPUS) / NP_CORPUS
    check("CONTROL: the limiting framework reproduces N/P -> 0.6605",
          rel < mpf("0.001"),
          f"quadrature gives S = {nstr(S_inf, 10)} against the corpus's "
          f"{nstr(NP_CORPUS, 5)} (from the Ivanov-Olshanski field, an entirely "
          f"different route) -- agreement {nstr(rel * 100, 3)}%. This checks the "
          f"semicircle co-transition limit, the independence of the two corners, "
          f"the omega weight and phi, all at once. Without it the integrals below "
          f"would be unfalsifiable.")

    S_same = S_inf / 2
    check("w_opp -> 1/2 EXACTLY, by symmetry -- no integral needed",
          True,
          f"the omega weight (r-a)^2(r+a) depends on the two contents only through "
          f"their ABSOLUTE values, and the semicircle is symmetric, so each sign is "
          f"independent of its magnitude and the sign pattern is independent of the "
          f"weight. Hence opposite-sign weight = P(opposite signs) = 1/2. Measured "
          f"0.4567, 0.4735, 0.4806, 0.4862 at n = 100..800, rising to it from below. "
          f"The same symmetry gives S_same = S_opp = S/2 = {nstr(S_same, 8)}.")

    def Bopp(bound):
        return dbl(lambda u, v:
                   (max(u, v) ** 2 - min(u, v) ** 2)
                   * bound(min(u, v), max(u, v))) / W

    crude = Bopp(lambda a, r: D0)
    refined = Bopp(lambda a, r: min(r, D0) - max(mpf(0), a - (L1 - D0)))
    thr = 1 - S_same

    check("the CRUDE bound (the one proved in Lean) does NOT close the limit",
          S_same + crude > 1,
          f"|d_a - d_r| <= D(0) gives B_opp -> {nstr(crude, 8)}, so the total is "
          f"{nstr(S_same + crude, 8)} -- over 1 by {nstr(S_same + crude - 1, 3)}, "
          f"i.e. {nstr((S_same + crude - 1) * 100, 3)}%. That is "
          f"QOU.BraidKnot.M1EdgeCalculus.abs_diagLen_sub_transpose_le, and it is "
          f"sharp per edge, so the shortfall is not slack in the inequality.")

    check("REFINED elementary bounds reach the line (they do not settle it)",
          S_same + refined < 1,
          f"adding N^tau(r) <= min(r, D(0)) and N^sigma(a) >= max(0, a - (l1-D0)) "
          f"gives B_opp -> {nstr(refined, 8)}, total {nstr(S_same + refined, 8)} -- "
          f"under 1 by only {nstr(1 - S_same - refined, 3)} "
          f"({nstr((1 - S_same - refined) * 100, 3)}%). Both refinements are "
          f"elementary: the first is D(c) >= D(0) - c, i.e. `diagLen_le_add_sub`, "
          f"already proved sorry-free; the second is the same telescoping identity "
          f"read from the other end. NOT A PROOF -- see the header for the three "
          f"reasons, of which the sharpest is that this is asymptotic and the "
          f"finite-n budget is WORSE (B_opp rises to its limit, Ehat falls to its).")

    # ---- THE AREA CONSTRAINT: the big unused lever ----
    #
    # Everything above uses only D(0), lambda_1 and 1-Lipschitz. The global
    # constraint sum_c D(c) = n was never used, and it is worth far more than
    # either refinement so far. Two consequences, both elementary:
    #
    #   monotonicity:  a * D(a) <= sum_{c<a} D(c)
    #   1-Lipschitz:   D(a)(D(a)+1)/2 <= sum_{c>=a} D(c)   (the tail triangle)
    #   together:      a D(a) + D(a)^2/2 <= A_sigma
    #             =>   D(a) <= sqrt(a^2 + 2 A) - a
    #
    # in rescaled units with A = A_sigma/n. That is a MUCH better near-side bound
    # than min(D0, L-a), which is nearly vacuous away from the origin.
    A_half = mpf(1) / 2      # A_sigma/n -> 1/2, by conjugation symmetry of VKLS
    A_det = mpf(1)           # A_sigma <= n, with no limit-shape input at all
    far = lambda r: max(mpf(0), D0 - r)                                # noqa: E731
    b_area = Bopp(lambda a, r: min(D0, L1 - a, sqrt(a * a + 2 * A_half) - a) - far(r))
    b_det = Bopp(lambda a, r: min(D0, L1 - a, sqrt(a * a + 2 * A_det) - a) - far(r))

    check("THE AREA CONSTRAINT buys ~160x more room than the refinement above",
          S_same + b_area < 1 and (1 - S_same - b_area) > 50 * (1 - S_same - refined),
          f"adding D(a) <= sqrt(a^2 + 2A) - a with A = 1/2 gives B_opp -> "
          f"{nstr(b_area, 7)}, total {nstr(S_same + b_area, 7)} -- a margin of "
          f"{nstr(1 - S_same - b_area, 3)} ({nstr((1 - S_same - b_area) * 100, 3)}%) "
          f"against the {nstr((1 - S_same - refined) * 100, 3)}% of the previous "
          f"refinement. The near-side bound min(D0, L-a) is nearly vacuous away "
          f"from the origin -- it allows D(1) = 0.637 where the truth is 0.218 -- "
          f"and the area constraint is what closes that.")

    check("HONEST: the big margin needs A -> n/2, one more limit-shape fact",
          S_same + b_det < 1,
          f"with only the fully deterministic A_sigma <= n (no limit-shape input) "
          f"the bound gives {nstr(b_det, 7)}, total {nstr(S_same + b_det, 7)} -- a "
          f"margin of just {nstr(1 - S_same - b_det, 3)}. The jump to "
          f"{nstr((1 - S_same - b_area) * 100, 3)}% comes from A_sigma -> n/2, "
          f"i.e. the boxes splitting evenly between the two sides, which is the "
          f"conjugation symmetry of the limit shape -- the same CLASS of input as "
          f"D(0)/sqrt(n) -> 2/pi, and arguably more robust, but an input all the "
          f"same. Quoting 7.5% without saying so would be dishonest.")

    check("for scale: the bound is ~2x the truth, and 2x is nearly enough",
          crude / S_same > 2,
          f"S_opp itself -> {nstr(S_same, 7)} while the crude bound gives "
          f"{nstr(crude, 7)} -- a factor of {nstr(crude / S_same, 4)}. The refined "
          f"bound is {nstr(refined / S_same, 4)}x. The budget tolerates a factor of "
          f"{nstr(thr / S_same, 4)}x, which is why refinements of a few tenths of a "
          f"percent decide it.")

    # ---- CONTROL: the refined bound the quadrature ASSUMES, on real diagrams ----
    #
    # The integrals above are only as good as the per-edge inequality they
    # integrate. Verify it directly by brute force over every opposite-sign edge
    # at small n, and measure its slack -- a bound that is never close would mean
    # the refinement is not where the gain comes from.
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from wlambda_covariance_epic_M1_edge_ratio_monotonicity import (  # noqa: E402
        corners as _corners, partitions as _partitions,
    )

    def _prof(lam):
        Dp = {}
        for i, q in enumerate(lam):
            for j in range(q):
                Dp[j - i] = Dp.get(j - i, 0) + 1
        return Dp

    def _durfee(Lm):
        k = 0
        for i, q in enumerate(Lm):
            if q >= i + 1:
                k += 1
            else:
                break
        return k

    nedge = vcrude = vref = tighter = 0
    minslack = None
    tight2 = 0
    for nn in range(6, 21):
        for Lm in _partitions(nn + 1):
            cs = _corners(Lm)
            for xi in range(len(cs)):
                cxx, _dx, chx = cs[xi]
                for yi in range(xi + 1, len(cs)):
                    cyy, _dy, chy = cs[yi]
                    dab = abs(cyy) - abs(cxx)
                    if dab == 0 or not (cxx > 0 > cyy):
                        continue
                    lam = chx if dab > 0 else chy
                    Dp, d0, l1, lt = _prof(lam), _durfee(lam), (lam[0] if lam else 0), len(lam)
                    aa, rr = min(abs(cxx), abs(cyy)), max(abs(cxx), abs(cyy))
                    nearc = cxx if dab > 0 else cyy
                    farc = cyy if dab > 0 else cxx
                    delta = Dp.get(nearc, 0) - Dp.get(farc, 0)
                    lnear = l1 if nearc >= 0 else lt
                    ref = min(d0, lnear - aa) - max(0, d0 - rr)
                    nedge += 1
                    if delta > d0:
                        vcrude += 1
                    if delta > ref:
                        vref += 1
                    if ref < d0:
                        tighter += 1
                    sl = ref - delta
                    minslack = sl if minslack is None else min(minslack, sl)
                    if sl - 2 < 0:
                        tight2 += 1

    check("CONTROL: the refined per-edge bound holds on real diagrams",
          vref == 0 and vcrude == 0,
          f"brute force over every opposite-sign edge at n = 6..20 "
          f"({nedge} edges): {vcrude} violations of the crude bound, {vref} of the "
          f"refined one. The refined bound is STRICTLY TIGHTER on {tighter} of them "
          f"({100 * tighter // nedge}%), which is where the gain in the integrals "
          f"comes from. Corresponds to "
          f"QOU.BraidKnot.M1EdgeCalculus.diagLen_sub_transpose_le_refined.")

    # CONTROL for the area inequality itself, with the bookkeeping that first
    # got it wrong: the c = 0 diagonal belongs to the POSITIVE side's sum, so the
    # negative side's total is A_- + D(0), not A_-. Checking against A_- alone
    # reported 3974 violations -- of a true statement.
    apos = aneg = badp = badn = 0
    for nn in range(1, 23):
        for lam in _partitions(nn):
            Dp = _prof(lam)
            Ap = sum(v for c, v in Dp.items() if c >= 0)
            Am = sum(v for c, v in Dp.items() if c < 0) + Dp.get(0, 0)
            for c, dv in Dp.items():
                aa = abs(c)
                lhs = aa * dv + dv * (dv + 1) // 2
                if c >= 0:
                    apos += 1
                    if lhs > Ap:
                        badp += 1
                else:
                    aneg += 1
                    if lhs > Am:
                        badn += 1
    check("CONTROL: the AREA inequality a·D(a) + D(a)(D(a)+1)/2 <= A_side holds",
          badp == 0 and badn == 0,
          f"all partitions n <= 22: {apos} positive-side diagonals with {badp} "
          f"violations, {aneg} negative-side with {badn}. The negative side is "
          f"measured against A_- + D(0), because the c = 0 diagonal is counted on "
          f"the positive side -- checking it against A_- alone reports 3974 "
          f"violations of a true statement, which is how this was first got wrong.")

    check("CONTROL: ...and that check discriminates -- tightening by 2 fails",
          tight2 > 0,
          f"minimum slack of the refined bound over the same edges is "
          f"{minslack}, and tightening it by 2 is violated on {tight2} edges. So "
          f"the bound is essentially attained -- the residual slack is O(1), hence "
          f"o(sqrt n) and invisible to the rescaled integrals above. Without this "
          f"the 'no violations' line would be consistent with a hopelessly loose "
          f"bound.")

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-limit-closed-form.witness.json").write_text(
        json.dumps({
        "q0Anchor": "independent",
        "q0AnchorReason": "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: M_1>0: the whole budget in CLOSED FORM, and whether the route closes.",
            "probe": "m1_limit_closed_form",
            "bean": ["qou-t6hc", "qou-k5r5"],
            "S_inf": nstr(S_inf, 12), "S_same": nstr(S_same, 12),
            "B_opp_crude": nstr(crude, 12), "B_opp_refined": nstr(refined, 12),
            "total_crude": nstr(S_same + crude, 12),
            "total_refined": nstr(S_same + refined, 12),
            "w_opp": "1/2 exactly",
            "checks": checks, "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print(f"RESULT: w_opp -> 1/2 exactly; S_same = S_opp -> {nstr(S_same, 8)}.")
    print(f"RESULT: crude bound total {nstr(S_same + crude, 8)} (fails); refined "
          f"{nstr(S_same + refined, 8)} (reaches the line).")
    print("RESULT: gap qou-k5r5 stays OPEN -- asymptotic only, and the margin is "
          "0.047%.")
    print("EXIT: 0" if all(c["pass"] for c in checks) else "EXIT: 1")
    return 0 if all(c["pass"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
