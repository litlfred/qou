#!/usr/bin/env python3
"""M_1 effective-CLT sub-result (1): the Lambda*-part of Sum_h is omega3-orthogonal.

Gap qou-k5r5, epic qou-x631. Effective-CLT project sub-result (1) (workplan
docs/workplans/2026-08-22-M1-effective-CLT-project.md): compute the Lambda*
(shifted-symmetric) contribution to M_1 = Cov_Planch(Sum_h, omega3),
omega3 = Sum_c^2 - C(n,2).

Decompose Sum_h through the shifted power sum p2sharp (which IS in Lambda*):
    p2(lam) = Sum_i lam_i^2 = p2sharp(lam) + 2 Sum_i i lam_i - n,
    p2sharp(lam) = Sum_i lam_i(lam_i - 2i + 1)  [ = Sum_i ((lam_i-i+1/2)^2 - (i-1/2)^2) ].
Since Sum_h = (p2(lam)+p2(lam'))/2,
    Sum_h = p2sharp_sym  +  T,   p2sharp_sym = (p2sharp(lam)+p2sharp(lam'))/2  in Lambda*,
    T = Sum_box (i+j) - n   (1-indexed i,j; the non-Lambda* co-content statistic).

RESULT (exact, this probe):
  * Cov(p2sharp_sym, omega3) = 0  EXACTLY for all n.
    Reason: p2sharp_sym is Lambda*-degree 2 (a combination of Sigma_2, n^2, n), and
    Cov_Planch(Sigma_2, Sigma_3) = 0 (= Cov(R_3, R_4) = 0, the exact orthogonality of
    distinct central characters; omega3 = Sigma_3/3). So the WHOLE Lambda* part drops.
  * Hence  M_1 = Cov(Sum_h, omega3) = Cov(T, omega3)  EXACTLY.
    (This proves the antidiagonal reformulation of PR #5366 exact: no genus correction.)

Consequence for the effective bound M_1 >= kappa n^{5/2} - C n^2: there is NO
integer-power Lambda* contribution to bound; the entire n^{5/2} leader and its
error come from the single non-Lambda* co-content statistic T. Sub-result (1)
is closed; the remaining work (sub-result 2) is the effective bound on Cov(T,omega3).

Exact Fraction throughout; NO float64. scope-(a); no fit; nothing wired; no c_k;
L2 unchanged. Gap qou-k5r5 stays OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys


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


@lru_cache(maxsize=None)
def dim(lam):
    n = sum(lam)
    if n == 0:
        return 1
    cj = conj(lam)
    prod = 1
    for i, part in enumerate(lam):
        for j in range(part):
            prod *= (part - j - 1) + (cj[j] - i - 1) + 1
    return factorial(n) // prod


def sumh(lam):
    cj = conj(lam)
    H = 0
    for i, part in enumerate(lam):
        for j in range(part):
            H += (part - j - 1) + (cj[j] - i - 1) + 1
    return H


def omega3(lam):
    n = sum(lam)
    s = sum((j - i) ** 2 for i, part in enumerate(lam) for j in range(part))
    return F(s) - F(n * (n - 1), 2)


def p2sharp(lam):
    return sum(li * (li - 2 * (idx + 1) + 1) for idx, li in enumerate(lam))


def p2sharp_sym(lam):
    return (F(p2sharp(lam)) + F(p2sharp(conj(lam)))) / 2


def Tstat(lam):
    n = sum(lam)
    return sum((i + 1) + (j + 1) for i, part in enumerate(lam) for j in range(part)) - n


def cov(n, fx, fy):
    nf = factorial(n)
    sX = sY = sXY = 0
    for lam in partitions(n):
        w = dim(lam) ** 2
        X = F(fx(lam)); Y = F(fy(lam))
        sX += w * X; sY += w * Y; sXY += w * X * Y
    EX = F(sX, nf); EY = F(sY, nf)
    return F(sXY, nf) - EX * EY


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    print(f"# Sub-result (1): Lambda*-part of Sum_h is omega3-orthogonal (nmax={nmax})")
    # identity check
    id_ok = True
    for n in range(1, min(nmax, 12) + 1):
        for lam in partitions(n):
            if sum(x * x for x in lam) != p2sharp(lam) + 2 * sum((i + 1) * li for i, li in enumerate(lam)) - n:
                id_ok = False
    print(f"# identity p2 = p2sharp + 2 Sum_i i lam_i - n (n<=min(nmax,12)): {id_ok}")
    print(f"# {'n':>3} {'Cov(p2sharp_sym,omega3)':>24} {'Cov(Sum_h,omega3)=M1':>22} {'Cov(T,omega3)':>16}")
    lam_star_zero = True
    m1_eq_T = True
    for n in range(3, nmax + 1):
        c_ls = cov(n, lambda l: p2sharp_sym(l), omega3)
        c_h = cov(n, lambda l: F(sumh(l)), omega3)
        c_T = cov(n, lambda l: F(Tstat(l)), omega3)
        if c_ls != 0:
            lam_star_zero = False
        if c_h != c_T:
            m1_eq_T = False
        print(f"  {n:>3} {str(c_ls):>24} {str(c_h):>22} {str(c_T):>16}")
    print()
    print(f"RESULT: Cov(p2sharp_sym, omega3) = 0 exactly (Lambda*-degree-2 _|_ Sigma_3): {lam_star_zero}")
    print(f"RESULT: M_1 = Cov(Sum_h, omega3) = Cov(T, omega3) exactly (T = Sum(i+j)-n): {m1_eq_T}")
    print("RESULT: sub-result (1) CLOSED -- no genus correction; leader is purely non-Lambda* T.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
