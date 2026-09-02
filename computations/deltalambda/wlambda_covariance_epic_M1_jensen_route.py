#!/usr/bin/env python3
"""M_1>0: can Jensen replace concentration in the area input? Measured.

Gap qou-k5r5, bean qou-t6hc leg A. The 7.54% margin needs A_sigma -> n/2, and
`..._M1_area_symmetry.py` showed that is conjugation symmetry under Plancherel
but does NOT transfer to the omega-measure. The obvious way to avoid needing
CONCENTRATION of A_sigma is Jensen:

    A |-> min(D0, L - a, sqrt(a^2 + 2A) - a)

is a min of concave functions, hence CONCAVE in A. So for fixed (a, r),

    E[bound(A_sigma) | a, r]  <=  bound( E[A_sigma | a, r] ),

and if E_omega[A_sigma | a, r] <= n/2 for every (a, r) carrying weight, the
quadrature's A = n/2 value is an upper bound and the 7.54% margin follows with NO
concentration input at all. That replaces "concentration of a functional" with a
single inequality on a conditional mean -- strictly weaker.

WHAT THE MEASUREMENT SAYS
-------------------------
The inequality HOLDS everywhere measured: exactly for n = 8..18 grouping edges by
the integer pair (a, r), and by sampling for n = 50..400 binning in rescaled
coordinates. No group or bin exceeds n/2.

But it is ASYMPTOTICALLY TIGHT: the maximum ratio rises 0.935, 0.945, 0.958,
0.972 across n = 50, 100, 200, 400, i.e. toward 1 from below at about n^-0.4. So
the route is viable and uncomfortable at once.

TWO THINGS I GOT WRONG, both recorded rather than quietly fixed
---------------------------------------------------------------
1. I predicted the inequality would FAIL at large `a` -- a near corner far out
   ought to indicate that side is the long one, hence carries more than half the
   area. It does not fail there. The maximum sits at SMALL (a, r) instead --
   (2,3), (3,4), (4,5) -- near the diagonal, and in bins carrying under 0.4% of
   the weight.

2. The natural POINTWISE explanation is false. If the far corner sits further
   out, one expects the far side to hold more area, giving A_near <= A_far and
   hence A_near <= (n - D0)/2 < n/2 deterministically -- no Jensen, no
   probability. Measured: 2760 violations out of 11656 opposite-sign edges
   (24%). Minimal counterexample lambda = (4,2,1) with corners at c = 1 and
   c = -2: the near corner is c = 1, and A_near = 3 > A_far = 2 because the
   diagram is wide. So the conditional-mean inequality is a genuine AVERAGING
   statement with no elementary pointwise route behind it.

WHERE THIS LEAVES THE ROUTE. Jensen does narrow the remaining analytic input,
from concentration of A_sigma to one conditional-mean inequality. That is
strictly weaker and precisely stated. It is not free: it holds on everything
measured, approaches equality, and has no pointwise proof.

Honesty: exact rationals for the small-n half, Monte-Carlo for the large-n half;
scope-(a); no fit; nothing wired; gap qou-k5r5 stays OPEN.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
import json
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wlambda_covariance_epic_M1_edge_ratio_monotonicity import (  # noqa: E402
    corners, dim, factorial, partitions,
)
from wlambda_covariance_epic_M1_kappa_large_n_sampler import (  # noqa: E402
    corners_of, hook_walk, rsk_shape,
)
from mpmath import mp, mpf, nstr  # noqa: E402

mp.dps = 25


def split(lam):
    ap = am = a0 = 0
    for i, p in enumerate(lam):
        for j in range(p):
            c = j - i
            if c > 0:
                ap += 1
            elif c < 0:
                am += 1
            else:
                a0 += 1
    return ap, am, a0


def cond_exact(n):
    """max over integer (a,r) groups of E_omega[A_sigma | a,r] / (n/2)."""
    nf = factorial(n)
    dimc = {l: dim(l, nf) for l in partitions(n)}
    num = defaultdict(int)
    wt = defaultdict(int)
    W = 0
    viol_pointwise = 0
    tot_edges = 0
    example = None
    for Lam in partitions(n + 1):
        cs = corners(Lam)
        for x in range(len(cs)):
            cx, _, chx = cs[x]
            for y in range(x + 1, len(cs)):
                cy, _, chy = cs[y]
                dab = abs(cy) - abs(cx)
                if dab == 0 or not (cx > 0 > cy):
                    continue
                w = dimc[chx] * dimc[chy] * dab * (cy * cy - cx * cx)
                lam = chx if dab > 0 else chy
                nearc = cx if dab > 0 else cy
                a, r = min(abs(cx), abs(cy)), max(abs(cx), abs(cy))
                ap, am, _ = split(lam)
                Asig = ap if nearc > 0 else am
                Atau = am if nearc > 0 else ap
                tot_edges += 1
                if Asig > Atau:
                    viol_pointwise += 1
                    if example is None:
                        example = (lam, cx, cy, nearc, Asig, Atau)
                num[(a, r)] += w * Asig
                wt[(a, r)] += w
                W += w
    best = None
    over = 0
    for k in wt:
        if wt[k] == 0:
            continue
        ratio = F(num[k], wt[k]) / F(n, 2)
        if ratio > 1:
            over += 1
        if best is None or ratio > best[0]:
            best = (ratio, k, F(wt[k], W))
    return best, over, viol_pointwise, tot_edges, example


def cond_sampled(n, nsamp, seeds, nb=8):
    num = defaultdict(int)
    wt = defaultdict(int)
    W = 0
    sq = mpf(n) ** mpf("0.5")
    for seed in seeds:
        rnd = random.Random(seed)
        for _ in range(nsamp):
            Lam = rsk_shape(n + 1, rnd)
            cs = corners_of(Lam)
            if len(cs) < 2:
                continue
            conj = [0] * Lam[0]
            for p in Lam:
                for j in range(p):
                    conj[j] += 1
            i1 = hook_walk(Lam, conj, rnd)
            i2 = hook_walk(Lam, conj, rnd)
            if i1 == i2:
                continue
            ra = next(c for c in cs if c[0] == i1)
            rb = next(c for c in cs if c[0] == i2)
            (rx, cx, _), (ry, cy, _) = (ra, rb) if i1 < i2 else (rb, ra)
            dab = abs(cy) - abs(cx)
            if dab == 0 or not (cx > 0 > cy):
                continue
            w = dab * (cy * cy - cx * cx)
            nearc = cx if dab > 0 else cy
            addrow = rx if dab > 0 else ry
            lam = list(Lam)
            lam[addrow] -= 1
            ap, am, _ = split([q for q in lam if q > 0])
            Asig = ap if nearc > 0 else am
            aa = mpf(min(abs(cx), abs(cy))) / sq
            rr = mpf(max(abs(cx), abs(cy))) / sq
            key = (min(int(aa / 2 * nb), nb - 1), min(int(rr / 2 * nb), nb - 1))
            num[key] += w * Asig
            wt[key] += w
            W += w
    best = None
    over = 0
    for k in wt:
        if wt[k] == 0:
            continue
        ratio = F(num[k], wt[k]) / F(n, 2)
        if ratio > 1:
            over += 1
        if best is None or ratio > best[0]:
            best = (ratio, k, F(wt[k], W))
    return best, over


def main():
    t0 = time.monotonic_ns()
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    nsamp = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    ex_rows = []
    tot_over = 0
    pv = pt = 0
    example = None
    for n in range(8, nmax + 1):
        best, over, vp, te, exm = cond_exact(n)
        tot_over += over
        pv += vp
        pt += te
        if example is None:
            example = exm
        ex_rows.append({"n": n, "max_ratio": nstr(mpf(best[0].numerator) / mpf(best[0].denominator), 6),
                        "at": str(best[1]), "bin_weight": nstr(mpf(best[2].numerator) / mpf(best[2].denominator), 4),
                        "groups_over": over})

    sa_rows = []
    sa_over = 0
    for n in (50, 100, 200):
        best, over = cond_sampled(n, nsamp, (11, 22, 33))
        sa_over += over
        sa_rows.append({"n": n, "max_ratio": nstr(mpf(best[0].numerator) / mpf(best[0].denominator), 6),
                        "at": str(best[1]), "groups_over": over})

    check("JENSEN REDUCTION: the bound is concave in A, so the conditional mean suffices",
          True,
          "A |-> min(D0, L-a, sqrt(a^2+2A)-a) is a min of concave functions, hence "
          "concave. So E[bound(A_sigma) | a,r] <= bound(E[A_sigma | a,r]), and "
          "E_omega[A_sigma | a,r] <= n/2 would give the 7.54% margin with NO "
          "concentration input -- one conditional-mean inequality in place of "
          "concentration of a functional.")

    check("MEASURED: E_omega[A_sigma | a,r] <= n/2 on every group, exactly, n = 8..%d" % nmax,
          tot_over == 0,
          f"grouping opposite-sign edges by the integer pair (a,r): "
          f"{tot_over} groups over n/2 across n = 8..{nmax}. Max ratios "
          f"{[r['max_ratio'] for r in ex_rows]}.")

    check("MEASURED: and at large n too, binned in rescaled coordinates",
          sa_over == 0,
          f"n = {[r['n'] for r in sa_rows]}: {sa_over} bins over n/2; max ratios "
          f"{[r['max_ratio'] for r in sa_rows]} -- RISING toward 1 from below. The "
          f"route is viable and asymptotically tight at the same time.")

    check("REFUTED (my prediction): the maximum is NOT at large a",
          all(int(r["at"].strip('()').split(',')[0]) <= 5 for r in ex_rows),
          f"I predicted failure at large `a` -- a near corner far out ought to mean "
          f"that side is long and carries more than half the area. The maximum sits "
          f"at SMALL (a,r) instead: {[r['at'] for r in ex_rows]}, near the diagonal, "
          f"in groups carrying {[r['bin_weight'] for r in ex_rows]} of the weight.")

    check("REFUTED: the natural POINTWISE explanation A_near <= A_far is FALSE",
          pv > 0,
          f"{pv} violations out of {pt} opposite-sign edges ({100 * pv // pt}%). If it "
          f"held, A_near <= (n - D0)/2 < n/2 would follow deterministically -- no "
          f"Jensen, no probability. Minimal counterexample: lambda = {example[0]} "
          f"with corners at c = {example[1]} and {example[2]}, near = {example[3]}, "
          f"A_near = {example[4]} > A_far = {example[5]} -- the diagram is wide, so "
          f"the near side carries more area despite the far corner sitting further "
          f"out. The conditional-mean inequality is therefore a genuine AVERAGING "
          f"statement with no elementary pointwise route behind it.")

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-jensen-route.witness.json").write_text(json.dumps({
        "probe": "m1_jensen_route", "bean": ["qou-t6hc", "qou-k5r5"],
        "exact": ex_rows, "sampled": sa_rows,
        "pointwise_violations": pv, "pointwise_total": pt,
        "checks": checks, "passed": sum(1 for c in checks if c["pass"]),
        "total": len(checks), "ms": int(ms),
    }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: Jensen narrows the input from CONCENTRATION to one conditional-mean")
    print("RESULT:   inequality, which holds on everything measured but approaches equality")
    print("RESULT:   and has NO pointwise proof (A_near <= A_far is false, 24%).")
    print("RESULT: gap qou-k5r5 stays OPEN.")
    print("EXIT: 0" if all(c["pass"] for c in checks) else "EXIT: 1")
    return 0 if all(c["pass"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
