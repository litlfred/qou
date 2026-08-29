#!/usr/bin/env python3
"""Track D (gap qou-k5r5, epic qou-x631): does Fulman's Stein / exchangeable-pair
ERROR-TERM machinery close the finite-n sign  kappa_n >= kappa  for n >= 13?

Target (established on main, 2026-08-22 one-sided reframing):
    kappa_n := M_1 / n^{5/2},  kappa := 128/(225 pi^2),
    M_1 = Cov_Planch(Sum_box h, Sum_box c^2).
    M_1 > 0 for ALL n  <==  (exact M_1>0, n<=12)  AND  (kappa_n >= kappa, n>=13).
The SOLE remaining analytic task is the ONE-SIDED sign  kappa_n - kappa >= 0 (n>=13).

Fulman (arxiv-math-0305423, TAMS 2005) supplies, for the NORMALIZED TRANSPOSITION
character ratio  W = (n-1)/sqrt(2) * chi^lam(12)/dim(lam):
  * Thm 1.2 (PROVED):   sup_x | P(W <= x) - Phi(x) |  <=  40.1 * n^{-1/4}.   [Kolmogorov distance]
  * Thm 1.3 (Stein):    that Kolmogorov distance <= 2*sqrt(Prop4.5) + (2pi)^{-1/4}*sqrt((1/tau)*E|W*-W|^3),
                        tau = 2/(n+1),
      Prop 4.5:  E[ (-1 + (n+1)/4 * E_lam(W*-W)^2)^2 ] = (3n^2 - 5n + 6)/(4 n^3),   [EXACT]
      Prop 4.6:  E|W*-W|^3 <= (4 e sqrt2 / sqrt n)^3 + 2 e^{-2e sqrt n} (2 sqrt2)^3. [bound]
  * Conjectured (UNPROVEN in Fulman): a C n^{-1/2} rate.

This probe QUANTIFIES why the error-term machinery cannot deliver the one-sided sign:

(1) TYPE MISMATCH (n-independent, fatal). Thm 1.2/1.3 bound a Kolmogorov distance
    sup_x|F_n(x)-Phi(x)| -- a distance between CDFs of the MARGINAL W. The target is
    the SIGN of a second-order COVARIANCE correction kappa_n - kappa. A magnitude/error
    bound |kappa_n - kappa| <= B_n can NEVER certify kappa_n - kappa >= 0: it is
    two-sided, the target is one-sided. Sign is not an error-term output.

(2) WRONG STATISTIC. W is the transposition character (~ Sum c, in the Kerov-Olshanski
    algebra Lambda*). M_1 pairs Sum c^2 (=> omega3, in Lambda*) with Sum h, which is NOT
    in Lambda* and is NOT a J-eigenfunction (the "wall", cf. qou-k5r5). Fulman gives no
    exact moment/covariance formula reaching Sum h.

(3) VACUOUS CONSTANT. Even pretending the Kolmogorov error bounded the moment gap, we
    print, at the crossing n0=13 and beyond: Fulman's bound value vs the exact margin
    kappa_n - kappa, and the counterfactual N0 at which each bound would first fall below
    the (shrinking) margin. Both N0 are astronomically past n0=13.

All arithmetic exact (Fraction) / mpmath. NO float64. scope-(a). Nothing wired. No c_k.
Gap qou-k5r5 stays OPEN; this probe is a NEGATIVE (Track D walls), not a closure.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys
import mpmath as mp

mp.mp.dps = 60


# ---------------------------------------------------------------- partitions / dim
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
    """Cov_Planch(Sum_h, Sum_c^2) exact Fraction (same routine as the onesided probe)."""
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
    EX = F(sX, nf)
    EY = F(sY, nf)
    return F(sXY, nf) - EX * EY


# ---------------------------------------------------------------- Fulman bounds
def fulman_thm12(n):
    """PROVED Thm 1.2 Kolmogorov bound: 40.1 * n^{-1/4}."""
    return mp.mpf("40.1") * mp.power(n, mp.mpf(-1) / 4)


def fulman_thm13(n):
    """Assembled Thm 1.3 pieces with the EXACT Prop 4.5 and the Prop 4.6 |W*-W|^3 bound,
    tau = 2/(n+1). This is the internal bound that yields the 40.1 n^{-1/4} rate."""
    nn = mp.mpf(n)
    tau = 2 / (nn + 1)
    # Prop 4.5 (exact): E[(-1 + (n+1)/4 E_lam(W*-W)^2)^2] = (3n^2-5n+6)/(4n^3)
    prop45 = (3 * nn**2 - 5 * nn + 6) / (4 * nn**3)
    # Prop 4.6 bound on E|W*-W|^3
    e = mp.e
    prop46 = (4 * e * mp.sqrt(2) / mp.sqrt(nn))**3 + 2 * mp.e**(-2 * e * mp.sqrt(nn)) * (2 * mp.sqrt(2))**3
    term1 = 2 * mp.sqrt(prop45)
    term2 = mp.power(2 * mp.pi, mp.mpf(-1) / 4) * mp.sqrt(prop46 / tau)
    return term1 + term2


def conjectured_rate(n, C):
    """Fulman's CONJECTURED (unproven) C n^{-1/2} rate."""
    return mp.mpf(C) * mp.power(n, mp.mpf(-1) / 2)


def solve_N0(bound_fn, target_mpf):
    """Smallest integer n where bound_fn(n) < target_mpf, scanning geometrically then
    bisecting. target is a fixed small positive number (a generous stand-in for the
    shrinking margin -- using a FIXED target only UNDERstates how hard the real,
    shrinking-margin problem is)."""
    lo, hi = 2, 2
    # geometric search for an upper bracket
    while bound_fn(hi) >= target_mpf:
        hi *= 2
        if hi > 10**40:
            return None
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if bound_fn(mid) >= target_mpf:
            lo = mid
        else:
            hi = mid
    return hi


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    kappa = mp.mpf(128) / (225 * mp.pi**2)
    print(f"# kappa = 128/(225 pi^2) = {mp.nstr(kappa, 20)}")
    print("#")
    print("# EXACT margin to certify positive  vs  Fulman's error bounds")
    print(f"# {'n':>3} {'kappa_n-kappa (exact)':>24} {'Thm1.2 40.1 n^-1/4':>20} "
          f"{'Thm1.3 assembled':>18} {'bound/margin':>14}")
    margins = {}
    for n in range(13, nmax + 1):
        cov = exact_M1(n)
        kap = mp.mpf(cov.numerator) / cov.denominator / mp.power(n, mp.mpf(5) / 2)
        diff = kap - kappa
        margins[n] = diff
        b12 = fulman_thm12(n)
        b13 = fulman_thm13(n)
        ratio = b12 / diff if diff > 0 else mp.inf
        print(f"  {n:>3} {mp.nstr(diff, 10):>24} {mp.nstr(b12, 8):>20} "
              f"{mp.nstr(b13, 8):>18} {mp.nstr(ratio, 6):>14}")

    # smallest exact margin observed on [13, nmax] -- a GENEROUS fixed target: the real
    # target shrinks to 0, so any finite fixed target understates the difficulty.
    min_margin = min(margins.values())
    max_margin = max(margins.values())
    print("#")
    print(f"# exact margin kappa_n - kappa on [13,{nmax}]: min={mp.nstr(min_margin,6)}, "
          f"max={mp.nstr(max_margin,6)} (target SHRINKS toward 0 as n->inf)")
    print("#")

    # (3) vacuity: counterfactual N0 where each bound would first drop below the margin.
    tgt = max_margin  # most generous: use the LARGEST margin in the window (~0.00156 peak)
    print(f"# counterfactual N0 = smallest n with bound(n) < {mp.nstr(tgt,6)} "
          f"(peak margin; a best case that STILL ignores the type mismatch):")
    N0_12 = solve_N0(fulman_thm12, tgt)
    N0_13 = solve_N0(fulman_thm13, tgt)
    N0_conj40 = solve_N0(lambda n: conjectured_rate(n, 40.1), tgt)
    N0_conj1 = solve_N0(lambda n: conjectured_rate(n, 1), tgt)
    print(f"#   Thm 1.2  (40.1 n^-1/4, PROVED)          : N0 = {N0_12}")
    print(f"#   Thm 1.3  (assembled Stein bound)        : N0 = {N0_13}")
    print(f"#   conj. C n^-1/2, C=40.1 (UNPROVEN)       : N0 = {N0_conj40}")
    print(f"#   conj. C n^-1/2, C=1    (optimistic)     : N0 = {N0_conj1}")
    print("#")
    print("# VERDICT (Track D):")
    print("#  (1) TYPE MISMATCH, fatal & n-independent: Thm 1.2/1.3 bound a Kolmogorov")
    print("#      distance of the MARGINAL W; a magnitude bound |kappa_n-kappa|<=B_n can")
    print("#      NEVER prove the ONE-SIDED sign kappa_n-kappa>=0. Sign is not an error output.")
    print("#  (2) WRONG STATISTIC: W ~ Sum c (in Lambda*); M_1 pairs omega3 with Sum h,")
    print("#      which is NOT in Lambda*/not a J-eigenfunction. No Fulman formula reaches it.")
    print("#  (3) VACUOUS at the n0=13 crossing: bound/margin ~ 1e4 there; even the")
    print("#      counterfactual N0 (ignoring (1),(2)) is astronomically past 13.")
    print("#  => Track D WALLS. The finite-n sign must come from a second-order-cumulant")
    print("#     (Sniady genus-1) computation, NOT from Fulman's first-order Berry-Esseen.")
    print("RESULT: Track-D Fulman-error route does NOT close kappa_n>=kappa; scope-(a) negative.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
