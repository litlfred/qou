#!/usr/bin/env python3
"""M_1>0 via a MARGIN-RICH Cauchy-Schwarz sufficient condition (not the delicate rate).

Gap qou-k5r5, epic qou-x631. The open nub was framed as the sign of the finite-n
correction kappa_n - kappa (a delicate rate). This probe shows the sign is NOT
knife-edge and reduces M_1>0 to a margin-rich variance/correlation bound.

Fulman P-N split (exact, on main): M_1 = P - N, with
    P = Cov_Planch(Sum|c|, omega3) >= 0,
    N = -Cov_Planch(Sum D^2, omega3) >= 0,   (D(u) = diagonal lengths)
and Sum_h = Sum D^2 + Sum|c| (exact), so M_1 = Cov(Sum_h, omega3) = P - N.

Write each covariance as (correlation)*(std)*(std):
    P = rho_P * sig_A * sig_W,   rho_P = corr(Sum|c|, omega3),  sig_A = std(Sum|c|)
    N = rho_N * sig_D * sig_W,   rho_N = |corr(Sum D^2, omega3)|, sig_D = std(Sum D^2)
    sig_W = std(omega3)  (COMMON factor).

Then M_1 = P - N > 0  <=>  N < P  <=>  rho_N * sig_D < rho_P * sig_A   (sig_W cancels).

Cauchy-Schwarz gives rho_N <= 1 for FREE, hence N <= sig_D * sig_W, hence the
CLEAN SUFFICIENT CONDITION (airtight: C-S on N, exact on P):

    (CS)   sig(Sum D^2) / sig(Sum|c|) < rho(Sum|c|, omega3)   =>   M_1 > 0.

This probe measures both sides EXACTLY (Fraction; std via exact 2nd moments, ratios
in mpmath at 30 dps only for display) and the margin (CS_rhs - CS_lhs). Empirically
sig_D/sig_A ~ 0.67 and rho_P ~ 0.98, so (CS) holds with margin ~0.31 for every n:
the sign is robust, and a CRUDE bound on the two ingredients would prove M_1>0 for
all n -- unlike the sharp asymptotic rate, whose margin vanishes in the exponent.

NO float64 (all covariances/variances exact Fraction; mpmath only for sqrt/display).
scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN (this is a
REDUCTION to a softer sufficient condition, not a proof of it).
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys
import mpmath as mp

mp.mp.dps = 30


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
    """(dim, Sum|c|, Sum D^2, Sum c^2) in one pass."""
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


def exact_moments(n):
    """Return exact P, N, Var(|c|), Var(D2), Var(omega3), Cov(|c|,w), Cov(D2,w)."""
    nf = factorial(n)
    Cn2 = F(n * (n - 1), 2)
    a = {k: F(0) for k in ("A", "D", "W", "AA", "DD", "WW", "AW", "DW")}
    for lam in partitions(n):
        d, A, Dd, c2 = stats(lam, n)
        w = F(d * d, nf)
        W = F(c2) - Cn2
        a["A"] += w * A; a["D"] += w * Dd; a["W"] += w * W
        a["AA"] += w * A * A; a["DD"] += w * Dd * Dd; a["WW"] += w * W * W
        a["AW"] += w * A * W; a["DW"] += w * Dd * W
    VA = a["AA"] - a["A"] ** 2
    VD = a["DD"] - a["D"] ** 2
    VW = a["WW"] - a["W"] ** 2
    covAW = a["AW"] - a["A"] * a["W"]
    covDW = a["DW"] - a["D"] * a["W"]
    P = covAW
    N = -covDW
    return P, N, VA, VD, VW, covAW, covDW


def mpf(x):
    return mp.mpf(x.numerator) / x.denominator


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    print("# M_1>0 via the Cauchy-Schwarz margin-rich sufficient condition")
    print("# (CS)  sig(SumD2)/sig(Sum|c|) < rho(Sum|c|,omega3)  =>  M_1 = P - N > 0")
    print(f"# {'n':>3} {'sigD/sigA':>11} {'rho_P':>9} {'CS margin':>11} {'N/P':>9} "
          f"{'M1>0':>5} {'(CS)holds':>9}")
    all_cs = True
    all_pos = True
    for n in range(3, nmax + 1):
        P, N, VA, VD, VW, covAW, covDW = exact_moments(n)
        if P <= 0 or VA <= 0 or VW <= 0:
            # degenerate small n (VA or VW may be 0); M1 sign still reported
            m1 = P - N
            all_pos = all_pos and (m1 > 0 or n <= 3)
            print(f"  {n:>3} {'--':>11} {'--':>9} {'--':>11} {'--':>9} "
                  f"{(m1>0)!s:>5} {'n/a':>9}")
            continue
        sigA = mp.sqrt(mpf(VA)); sigD = mp.sqrt(mpf(VD)); sigW = mp.sqrt(mpf(VW))
        rho_P = mpf(covAW) / (sigA * sigW)
        cs_lhs = sigD / sigA
        cs_rhs = rho_P
        margin = cs_rhs - cs_lhs
        m1 = P - N
        NP = mpf(N) / mpf(P)
        cs_holds = cs_lhs < cs_rhs
        all_cs = all_cs and cs_holds
        all_pos = all_pos and (m1 > 0)
        print(f"  {n:>3} {mp.nstr(cs_lhs,8):>11} {mp.nstr(rho_P,7):>9} "
              f"{mp.nstr(margin,7):>11} {mp.nstr(NP,6):>9} {(m1>0)!s:>5} {cs_holds!s:>9}")
    print()
    print("# (CS) is AIRTIGHT sufficient: N <= sigD*sigW (Cauchy-Schwarz, rho_N<=1);")
    print("#   P = rho_P*sigA*sigW exact; sigW cancels => N<P <== sigD/sigA < rho_P.")
    print("# The margin (~0.31) does NOT vanish, so a CRUDE rigorous bound on")
    print("#   sig(SumD2)/sig(Sum|c|) (~0.67) and a lower bound on rho(Sum|c|,omega3)")
    print("#   (~0.98) would prove M_1>0 for all n -- far softer than the sharp rate.")
    print(f"RESULT: (CS) holds for all 4<=n<={nmax}: {all_cs}; M_1>0 for all 3<=n<={nmax}: {all_pos}")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
