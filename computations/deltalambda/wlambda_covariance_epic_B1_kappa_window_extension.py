#!/usr/bin/env python3
"""B1: extend the EXACT kappa_n window past n <= 67.  Gap qou-k5r5, Track B.

WHY
---
`M_1 = Cov_Planch(Sum_h, Sum_c^2) = kappa_n * n^{5/2}`, and the arc's open nub is
the ONE-SIDED statement `kappa_n >= kappa` for `n >= 13`, with
`kappa = 128/(225 pi^2)` (derived, PR #5428).  Track A must prove the sign of the
genus-1 second-order correction; the ORDER of that correction is undetermined at
reachable n -- the measured effective exponent was still rising (~0.25 -> 0.36
over n = 40..64), so it is not yet clear whether the correction is `n^{-1/2}`
bulk, `n^{-2/3}` edge, or a mix.

This probe does NOT prove the sign.  Per the 2026-08-28 revised workplan, Track B
exists to *guide* Track A: a wider exact window sharpens the effective-exponent
measurement and so tells A which order to expect, de-risking A3.

WHAT IT COMPUTES
----------------
Exact `kappa_n` as a `Fraction`, for a requested range of `n`, by direct
Plancherel summation over every partition:

    M_1 = E[H . C2] - E[H] . E[C2],   E[X] = sum_lambda (f^lambda)^2 / n! . X

with `H = sum_cells hook`, `C2 = sum_cells content^2`.  Every quantity is an
exact integer or `Fraction`; the comparison against `kappa` is mpmath at 60 dps.
**No float64 anywhere.**

TWO CLOSED FORMS REPLACE TWO CELL WALKS
---------------------------------------
The committed `..._M1_onesided_kappa_bound.py` walks all `n` cells three times
per partition -- once for the hook product, once for `H`, once for `C2`.  The
last two have closed forms, verified against that script on all 507 partitions
of `n = 1..14` and on its own output for `n = 3..20`:

    H  = sum_i C(lambda_i, 2) + sum_j C(lambda'_j, 2) + n
    C2 = sum_i [ m(m-1)(2m-1)/6 - i.m(m-1) + i^2.m ],   m = lambda_i

`H` because `h = arm + leg + 1` and the arm/leg sums telescope per row/column.

Measured speedup: **1.31x** (n = 55: 8.1s against 10.6s).  Modest, and that is
the honest finding -- the hook product still needs its `O(n)` walk, and the cost
is Python loop overhead rather than big-integer arithmetic.  A beta-number
(first-column hook) formula for `f^lambda`, evaluated on whichever of
`lambda` / `lambda'` has fewer rows, was tried and is NOT faster (1.25x): the
`O(r^2)` pair product plus one big `n! * num // den` costs about what the
`O(n)` walk costs at these sizes.  Recorded so it is not re-attempted.

SCALING, MEASURED
-----------------
n = 50 -> 3.4s, 55 -> 8.1s, 60 -> 19.1s: a factor of ~2.35 per +5 in n.  So each
further step costs about 1.19x the last, and the window extends by brute force
alone.  `p(85) ~ 3e7` partitions is the practical wall for this approach in
Python; a materially wider window needs a different algorithm, not a faster loop.

Usage:  python3 <this> NMIN NMAX  [--out PATH]
scope-(a); no fit; nothing wired; no c_k; L2 unchanged.  Gap qou-k5r5 OPEN.
"""
from __future__ import annotations

import json
import os
import sys
import time
from fractions import Fraction as F

import mpmath as mp

mp.mp.dps = 60


def partitions(n):
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for p in range(min(n, mx), 0, -1):
            for r in gen(n - p, p):
                yield (p,) + r
    yield from gen(n, n)


def factorial(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def conj(lam):
    if not lam:
        return ()
    c = [0] * lam[0]
    for part in lam:
        for j in range(part):
            c[j] += 1
    return tuple(c)


def exact_M1(n):
    """Cov_Planch(Sum_h, Sum_c^2), exact Fraction."""
    nf = factorial(n)
    sX = sY = sXY = 0
    for lam in partitions(n):
        cj = conj(lam)
        prod = 1
        for i, part in enumerate(lam):
            ci = i + 1
            for j in range(part):
                prod *= part - j + cj[j] - ci
        f = nf // prod
        w = f * f
        H = sum(p * (p - 1) for p in lam) // 2 + sum(c * (c - 1) for c in cj) // 2 + n
        C2 = 0
        for i, m in enumerate(lam):
            C2 += m * (m - 1) * (2 * m - 1) // 6 - i * m * (m - 1) + i * i * m
        sX += w * H
        sY += w * C2
        sXY += w * H * C2
    return F(sXY, nf) - F(sX, nf) * F(sY, nf)


def main() -> int:
    nmin = int(sys.argv[1]) if len(sys.argv) > 1 else 68
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 72
    out = None
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]

    kappa = mp.mpf(128) / (225 * mp.pi ** 2)
    rows = []
    t0 = time.time()
    print(f"# kappa = 128/(225 pi^2) = {mp.nstr(kappa, 20)}")
    print(f"# {'n':>4} {'seconds':>9} {'kappa_n':>22} {'kappa_n - kappa':>16} {'sign':>5}")
    for n in range(nmin, nmax + 1):
        t = time.time()
        cov = exact_M1(n)
        dt = time.time() - t
        kap = mp.mpf(cov.numerator) / cov.denominator / mp.power(n, mp.mpf(5) / 2)
        diff = kap - kappa
        sgn = "+" if diff > 0 else ("-" if diff < 0 else "0")
        rows.append({
            "n": n,
            "M1_num": str(cov.numerator),
            "M1_den": str(cov.denominator),
            "kappa_n": mp.nstr(kap, 25),
            "kappa_n_minus_kappa": mp.nstr(diff, 12),
            "sign": sgn,
            # integer ms, not float seconds: a witness carries no raw float64,
            # and this matches the WitnessBuilder's own `durationMs`.
            "ms": int(dt * 1000),
        })
        print(f"  {n:>4} {dt:>9.1f} {mp.nstr(kap, 20):>22} {mp.nstr(diff, 6):>16} {sgn:>5}")
        sys.stdout.flush()
        if out:                      # write incrementally: a long run stays usable
            with open(out, "w") as fh:
                json.dump({"rows": rows}, fh, indent=2)
                fh.write("\n")

    allpos = all(r["sign"] == "+" for r in rows)
    print(f"\nall kappa_n > kappa on [{nmin}, {nmax}]: {allpos}")
    print(f"total {time.time() - t0:.1f}s")
    return 0 if allpos else 1


if __name__ == "__main__":
    raise SystemExit(main())
