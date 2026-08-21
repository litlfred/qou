#!/usr/bin/env python3
"""M_1 leading term via the IO Kerov-CLT MODE decomposition (exact).

Gap qou-k5r5. M_1 = Cov_Planch(Sum_h, Sum_c^2) ~ kappa n^{5/2}. Sum_c^2 = R_4/3
+ const (a SINGLE free-cumulant mode). Sum_h is OUTSIDE Lambda*, so its
fluctuation spreads over the even free-cumulant tower R_4, R_6, R_8, ... . The
Kerov CLT (Ivanov-Olshanski) makes the R_m asymptotically INDEPENDENT Gaussians
with Var(R_m) ~ (m-1) n^{m-1}. Then
    kappa = lim  Cov(Sum_h, Sum_c^2)/n^{5/2}
          = (1/3) lim Cov(Sum_h, R_4)/n^{5/2},
i.e. kappa is fixed by the R_4-MODE OVERLAP of Sum_h alone; the other even modes
do NOT enter M_1 (Sum_c^2 has no R_6+ component). This probe:

  1. Builds the Kerov TRANSITION MEASURE mu_lambda of each partition exactly
     (Lagrange weights on addable contents interlacing removable contents),
  2. Extracts free cumulants R_1..R_8 from its moments (exact Fraction, via the
     free moment-cumulant functional equation M = 1 + sum_k R_k z^k M^k),
  3. Verifies R_2 == n exactly (the diagnostic that the measure is correct),
  4. Under Plancherel, decomposes Var(Sum_h) across the even modes R_4,R_6,R_8
     and reports how much each explains, and the R_4 regression coefficient
     beta_4 = Cov(Sum_h,R_4)/Var(R_4) whose n^{1/2}-scaled limit is 3*kappa...
     (actually kappa = Cov(Sum_h,R_4)/(3 n^{5/2}); beta_4 ~ kappa n^{-1/2}).

Purpose: decide whether the raw kappa_n non-monotonicity (peak n=32, then
descending) is R_6/R_8 modes leaking in at finite n -- in which case the PURE
R_4 overlap may converge more cleanly and pin kappa. Exact arithmetic; NO
float64 (mpmath.mpf only for the final rescalings).

Honesty: scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys
import mpmath as mp

mp.mp.dps = 50


def partitions(n: int):
    def gen(n, maxp):
        if n == 0:
            yield ()
            return
        for p in range(min(n, maxp), 0, -1):
            for rest in gen(n - p, p):
                yield (p,) + rest
    yield from gen(n, n)


@lru_cache(maxsize=None)
def factorial(n: int) -> int:
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def conj_of(lam):
    if not lam:
        return ()
    m = lam[0]
    c = [0] * m
    for part in lam:
        for j in range(part):
            c[j] += 1
    return tuple(c)


def hook_sum(lam) -> int:
    conj = conj_of(lam)
    H = 0
    for i, part in enumerate(lam):
        for j in range(part):
            H += (part - j - 1) + (conj[j] - i - 1) + 1
    return H


def syt_count(lam, n) -> int:
    conj = conj_of(lam)
    prod = 1
    for i, part in enumerate(lam):
        for j in range(part):
            prod *= (part - j - 1) + (conj[j] - i - 1) + 1
    q, r = divmod(factorial(n), prod)
    assert r == 0
    return q


def addable_removable_contents(lam):
    """Return (addable_contents sorted asc, removable_contents sorted asc).

    Contents c = j - i (0-indexed i,j -> content = j - i). Removable = corners
    (i,lam_i-1). Addable = the outer boundary positions where a box can be added.
    They interlace: x_1 < y_1 < x_2 < ... < y_{d-1} < x_d, addables x, removables y.
    """
    lam = list(lam)
    ell = len(lam)
    # removable corners: rows i where lam[i] > lam[i+1] (or last row)
    removable = []
    for i in range(ell):
        nxt = lam[i + 1] if i + 1 < ell else 0
        if lam[i] > nxt:
            removable.append((lam[i] - 1) - i)  # content j-i with j=lam_i-1
    # addable positions: content where a new box (i, lam_i) can go, i=0..ell
    # a box can be added at row i (0-indexed, i from 0..ell) at column lam_i
    # (with lam_ell = 0) when lam_{i-1} > lam_i (or i=0 / i=ell)
    addable = []
    prev = None
    # augment: row -1 has "infinite" width; check each i=0..ell
    ext = lam + [0]
    for i in range(ell + 1):
        above = ext[i - 1] if i - 1 >= 0 else None
        width = ext[i]
        if i == 0 or above > width:
            addable.append(width - i)  # content j-i with j=width (new column index)
    return sorted(addable), sorted(removable)


def transition_moments(lam, pmax):
    """Moments M_1..M_pmax of the Kerov transition measure of lam (exact F)."""
    xs, ys = addable_removable_contents(lam)
    xs = [F(x) for x in xs]
    ys = [F(y) for y in ys]
    weights = []
    for k, xk in enumerate(xs):
        num = F(1)
        for yj in ys:
            num *= (xk - yj)
        den = F(1)
        for l, xl in enumerate(xs):
            if l != k:
                den *= (xk - xl)
        weights.append(num / den)
    # moments
    M = [F(0)] * (pmax + 1)
    M[0] = sum(weights)  # should be 1
    for p in range(1, pmax + 1):
        M[p] = sum(w * (xk ** p) for w, xk in zip(weights, xs))
    return M  # M[0]=1, M[1..pmax]


def free_cumulants(M, nmax):
    """Free cumulants R_1..R_nmax from moments M[0..] via
    M(z) = 1 + sum_{k>=1} R_k z^k M(z)^k. Exact Fraction.
    M is list with M[0]=1, M[1], M[2], ... (length >= nmax+1)."""
    R = [F(0)] * (nmax + 1)  # R[1..nmax]

    def poly_pow_coeff(Mcoeffs, k, m):
        # [z^m] (sum_{j>=0} Mcoeffs[j] z^j)^k  via iterated convolution up to deg m
        # base = Mcoeffs truncated to degree m
        base = [F(0)] * (m + 1)
        for j in range(min(len(Mcoeffs), m + 1)):
            base[j] = Mcoeffs[j]
        acc = [F(0)] * (m + 1)
        acc[0] = F(1)
        for _ in range(k):
            new = [F(0)] * (m + 1)
            for a in range(m + 1):
                if acc[a] == 0:
                    continue
                for b in range(m + 1 - a):
                    if base[b] == 0:
                        continue
                    new[a + b] += acc[a] * base[b]
            acc = new
        return acc[m]

    for n in range(1, nmax + 1):
        # M_n = R_n * [z^0]M^n + sum_{k=1}^{n-1} R_k [z^{n-k}] M^k
        s = F(0)
        for k in range(1, n):
            s += R[k] * poly_pow_coeff(M, k, n - k)
        R[n] = M[n] - s
    return R  # R[1..nmax]


def main() -> int:
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 26
    NMODE = 8  # highest free cumulant
    print(f"# IO mode decomposition of Var(Sum_h); nmax={nmax}")
    print(f"# sanity: R_2 == n for all partitions checked exactly")

    header = f"# {'n':>3} {'Var(Sh)/n^2':>12} {'C(Sh,R4)/n^2.5':>15} {'beta4*sqrt(n)':>13} {'R4 expl%':>9} {'R6 expl%':>9}"
    print(header)

    for n in range(4, nmax + 1):
        nfac = factorial(n)
        # accumulate exact rational Plancherel moments (denominator n!)
        wsum = 0
        SH = 0      # sum f^2 Sum_h
        acc = {}    # sums for R_m and products
        for m in range(1, NMODE + 1):
            acc[('R', m)] = 0
        acc[('SH2',)] = 0
        for m in (4, 6, 8):
            acc[('SHR', m)] = 0
            acc[('R2', m)] = 0  # E[R_m^2]
        acc[('R46',)] = 0
        for lam in partitions(n):
            f = syt_count(lam, n)
            w = f * f
            wsum += w
            H = hook_sum(lam)
            Mmom = transition_moments(lam, NMODE)
            assert Mmom[0] == 1, "transition measure not a probability measure"
            R = free_cumulants(Mmom, NMODE)
            assert R[2] == n, f"R_2 must equal n; got {R[2]} for {lam} (n={n})"
            SH += w * H
            acc[('SH2',)] += w * H * H
            for m in (4, 6, 8):
                rm = R[m]
                acc[('R', m)] += w * rm  # numerator over n!
                acc[('R2', m)] += w * rm * rm
                acc[('SHR', m)] += w * H * rm
            acc[('R46',)] += w * R[4] * R[6]
        assert wsum == nfac
        EH = F(SH, nfac)
        EH2 = F(acc[('SH2',)], nfac)
        VarH = EH2 - EH * EH
        stats = {}
        for m in (4, 6, 8):
            Em = F(acc[('R', m)], nfac)
            Em2 = F(acc[('R2', m)], nfac)
            Vm = Em2 - Em * Em
            EHm = F(acc[('SHR', m)], nfac)
            Cm = EHm - EH * Em
            stats[m] = (Vm, Cm)
        # explained variance by mode m (treating modes as ~independent): C_m^2/V_m
        def frac(m):
            Vm, Cm = stats[m]
            if Vm == 0:
                return F(0)
            return (Cm * Cm) / (Vm * VarH)
        r4f = frac(4)
        r6f = frac(6)
        # rescaled quantities (mpmath)
        vH = mp.mpf(VarH.numerator) / VarH.denominator
        C4 = mp.mpf(stats[4][1].numerator) / stats[4][1].denominator
        V4 = mp.mpf(stats[4][0].numerator) / stats[4][0].denominator
        beta4 = C4 / V4
        print(f"  {n:>3} {mp.nstr(vH/mp.mpf(n)**2,8):>12} "
              f"{mp.nstr(C4/mp.power(n,mp.mpf(5)/2),8):>15} "
              f"{mp.nstr(beta4*mp.sqrt(n),8):>13} "
              f"{mp.nstr(mp.mpf(r4f.numerator)/r4f.denominator*100,6):>9} "
              f"{mp.nstr(mp.mpf(r6f.numerator)/r6f.denominator*100,6):>9}")

    print()
    print("# reading: 'C(Sh,R4)/n^2.5' = 3*kappa_n (since Cov(Sh,Sum_c^2)=Cov(Sh,R4)/3).")
    print("#   R4 expl% = fraction of Var(Sum_h) explained by the R_4 mode alone.")
    print("#   If R4 expl% -> 100, Sum_h ~ (const) R_4 at leading order and kappa is clean.")
    print("#   If R6 expl% stays > 0, the even TOWER contributes and the raw kappa_n")
    print("#   non-monotonicity is finite-n mode leakage.")
    print("RESULT: exact transition-measure free cumulants; R_2==n verified all partitions.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
