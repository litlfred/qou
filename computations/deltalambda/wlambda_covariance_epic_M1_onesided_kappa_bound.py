#!/usr/bin/env python3
"""M_1>0 sub-result (2) reframing: is kappa_n >= kappa (approach from ABOVE)?

Gap qou-k5r5. M_1 = Cov_Planch(Sum_h, Sum_c^2) = kappa_n * n^{5/2}, and (sub-result
1, proved) M_1 = Cov(T, omega3) with kappa = lim kappa_n = 128/(225 pi^2).

REFRAMING of the effective bound. Instead of M_1 >= kappa n^{5/2} - C n^2 with an
explicit C, observe: if kappa_n >= kappa for all n >= n_0 (i.e. kappa_n approaches
its limit FROM ABOVE past a small crossing), then
    n <= n_0-1 : M_1 > 0 by EXACT computation,
    n >= n_0   : M_1 = kappa_n n^{5/2} >= kappa n^{5/2} > 0,
so M_1 > 0 for ALL n. The remaining analytic task is then only the ONE-SIDED
statement "kappa_n >= kappa for large n" -- which needs the SIGN of the leading
correction (positive), not an explicit constant. Much cleaner target.

This probe: compute kappa_n EXACTLY (Fraction), compare to kappa=128/(225 pi^2) at
high precision, find the crossing n_0 where kappa_n goes above kappa and STAYS,
and report whether kappa_n >= kappa holds for every n in [n_0, NMAX].

Exact Fraction covariance; kappa and the comparison in mpmath at 60 dps. NO float64.
scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys
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


@lru_cache(maxsize=None)
def factorial(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def conj(lam):
    if not lam:
        return ()
    m = lam[0]
    c = [0] * m
    for part in lam:
        for j in range(part):
            c[j] += 1
    return tuple(c)


def dim_hook(lam, n):
    cj = conj(lam)
    prod = 1
    for i, part in enumerate(lam):
        for j in range(part):
            prod *= (part - j - 1) + (cj[j] - i - 1) + 1
    q, r = divmod(factorial(n), prod)
    assert r == 0
    return q, cj


def exact_M1(n):
    """Cov_Planch(Sum_h, Sum_c^2) exact Fraction."""
    nf = factorial(n)
    sX = sY = sXY = 0
    for lam in partitions(n):
        f, cj = dim_hook(lam, n)
        w = f * f
        H = 0
        C2 = 0
        for i, part in enumerate(lam):
            for j in range(part):
                H += (part - j - 1) + (cj[j] - i - 1) + 1
                C2 += (j - i) ** 2
        sX += w * H
        sY += w * C2
        sXY += w * H * C2
    EX = F(sX, nf); EY = F(sY, nf)
    return F(sXY, nf) - EX * EY


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 45
    kappa = mp.mpf(128) / (225 * mp.pi ** 2)
    print(f"# kappa = 128/(225 pi^2) = {mp.nstr(kappa, 15)}")
    print(f"# {'n':>3} {'kappa_n':>16} {'kappa_n - kappa':>18} {'sign':>5}")
    crossing = None
    above_from = None
    all_above_tail = True
    signs = []
    for n in range(3, nmax + 1):
        cov = exact_M1(n)
        kap = mp.mpf(cov.numerator) / cov.denominator / mp.power(n, mp.mpf(5) / 2)
        diff = kap - kappa
        sgn = "+" if diff > 0 else ("-" if diff < 0 else "0")
        signs.append((n, diff))
        print(f"  {n:>3} {mp.nstr(kap, 12):>16} {mp.nstr(diff, 6):>18} {sgn:>5}")
    # find the last n where kappa_n < kappa (the crossing); check all-above after
    last_below = None
    for n, d in signs:
        if d < 0:
            last_below = n
    if last_below is not None:
        above_from = last_below + 1
        all_above_tail = all(d > 0 for n, d in signs if n >= above_from)
    else:
        above_from = signs[0][0]
        all_above_tail = all(d > 0 for _, d in signs)
    print()
    print(f"# last n with kappa_n < kappa: {last_below}")
    print(f"# => kappa_n > kappa for all {above_from} <= n <= {nmax}: {all_above_tail}")
    print("#")
    print("# REFRAMING: if this one-sided 'kappa_n >= kappa for n >= n_0' holds for ALL n")
    print("#   (proved via the SIGN of the leading correction), then with the exact check")
    print("#   M_1>0 for n < n_0, we get M_1>0 for ALL n. Target = sign of correction, not C.")
    print(f"RESULT: crossing at n_0 = {above_from}; kappa_n > kappa on [{above_from},{nmax}]: {all_above_tail}")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
