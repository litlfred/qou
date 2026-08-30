#!/usr/bin/env python3
"""M_1>0 sign (b1): deficit-rate structure of 'N lags P'.

Gap qou-k5r5. kappa_n > kappa (one-sided) holds because P and N approach their
VKLS limits at different rates. With
    p_n = P_n/n^{5/2} -> P_lead = (1/3)|x|_3      = 0.1697652726...
    nu_n = N_n/n^{5/2} -> N_lead = -(1/3)(2Dinf)_3 = 0.1121252230...
(P = Cov(Sum|c|,omega3) >= 0, N = -Cov(SumD2,omega3) >= 0; both approach FROM BELOW),
    kappa_n - kappa = (p_n - P_lead) - (nu_n - N_lead) = dN - dP,
    dP := P_lead - p_n >= 0,  dN := N_lead - nu_n >= 0  (deficits).
So kappa_n >= kappa  <=>  dN >= dP  ("N lags P": N's deficit is the larger).

This probe measures dP, dN EXACTLY (P_n, N_n exact Fraction via direct Plancherel;
limits via theta-quadrature at 40 dps) and their rates dP*n^b, dN*n^b, plus the
gap dN - dP (= kappa_n - kappa) and the ratio dN/dP, to pin the mechanism of
'N lags P' and look for a provable structure.

Direct Plancherel sums (no chain) -> fast to n~40. NO float64.
scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys
import mpmath as mp

mp.mp.dps = 40


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


def stats(lam, n):
    """Return (dim, Sum|c|, SumD2, omega3-as-int Sum_c^2) via one pass."""
    m = lam[0] if lam else 0
    conj = [0] * m
    for part in lam:
        for j in range(part):
            conj[j] += 1
    prod = 1
    absc = 0
    c2 = 0
    D = {}
    for i, part in enumerate(lam):
        for j in range(part):
            prod *= (part - j - 1) + (conj[j] - i - 1) + 1
            u = j - i
            absc += abs(u)
            c2 += u * u
            D[u] = D.get(u, 0) + 1
    d = factorial(n) // prod
    sumD2 = sum(v * v for v in D.values())
    return d, absc, sumD2, c2


def PN_exact(n):
    """P_n = Cov(Sum|c|, omega3), N_n = -Cov(SumD2, omega3), exact Fractions."""
    nf = factorial(n)
    Cn2 = F(n * (n - 1), 2)
    sA = sD = sW = 0        # sum w*Sum|c|, w*SumD2, w*omega3
    sAW = sDW = 0
    for lam in partitions(n):
        d, absc, sumD2, c2 = stats(lam, n)
        w = d * d
        om = F(c2) - Cn2
        sA += w * absc
        sD += w * sumD2
        sW += w * om
        sAW += w * absc * om
        sDW += w * sumD2 * om
    EA = F(sA, nf); ED = F(sD, nf); EW = F(sW, nf)
    P = F(sAW, nf) - EA * EW
    covD2 = F(sDW, nf) - ED * EW
    return P, -covD2   # P, N


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 34
    # limits via theta-quadrature
    Om = lambda t: (4 / mp.pi) * (mp.cos(t) * (mp.pi / 2 - t) + mp.sin(t))
    absx = lambda t: abs(2 * mp.cos(t))
    hat = lambda f, k: (2 / mp.pi) * mp.quad(lambda t: f(t) * mp.sin(k * t) * mp.sin(t), [0, mp.pi / 2, mp.pi])
    P_lead = hat(absx, 3) / 3
    twoD3 = hat(Om, 3) - hat(absx, 3)
    N_lead = -twoD3 / 3
    kappa = P_lead - N_lead
    print(f"# P_lead = {mp.nstr(P_lead,12)}  N_lead = {mp.nstr(N_lead,12)}  kappa = {mp.nstr(kappa,12)}")
    print(f"# {'n':>3} {'dP=P_lead-p_n':>14} {'dN=N_lead-nu_n':>14} {'dN-dP(=k_n-k)':>14} {'dN/dP':>8} {'dP*sqrtn':>9} {'dN*sqrtn':>9}")
    allNlagsP = True
    for n in range(4, nmax + 1):
        P, N = PN_exact(n)
        pn = mp.mpf(P.numerator) / P.denominator / mp.power(n, mp.mpf(5) / 2)
        nun = mp.mpf(N.numerator) / N.denominator / mp.power(n, mp.mpf(5) / 2)
        dP = P_lead - pn
        dN = N_lead - nun
        gap = dN - dP
        if gap <= 0 and n >= 13:
            allNlagsP = False
        ratio = dN / dP if dP != 0 else mp.mpf('nan')
        print(f"  {n:>3} {mp.nstr(dP,8):>14} {mp.nstr(dN,8):>14} {mp.nstr(gap,8):>14} "
              f"{mp.nstr(ratio,6):>8} {mp.nstr(dP*mp.sqrt(n),6):>9} {mp.nstr(dN*mp.sqrt(n),6):>9}")
    print()
    print("# dN - dP = kappa_n - kappa. 'N lags P' (dN >= dP) for n>=13 <=> kappa_n >= kappa.")
    print("# If dP*sqrtn, dN*sqrtn -> constants a_P < a_N, both deficits ~ a/sqrt(n) and the")
    print("#   gap ~ (a_N - a_P)/sqrt(n) > 0 -> the sign is the inequality a_N > a_P (leading")
    print("#   1/sqrt(n) deficit coefficients). That is the concrete second-order target.")
    print(f"RESULT: dN >= dP (N lags P) for all 13<=n<={nmax}: {allNlagsP}")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
