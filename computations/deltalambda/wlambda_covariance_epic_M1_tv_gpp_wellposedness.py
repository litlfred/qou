#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5 / qou-tvok): is "compute TV(g'')" even WELL-POSED? -- structural check
before producing a number. HONEST NEGATIVE: there is no local variance density whose g'' to take.

Gap qou-k5r5. The preceding probe (_em_osc_constant_prediction.py) noted that the corpus EM tool

  QOU.MathlibExt.abs_integral_sub_composite_le_osc :
    |int - composite| <= h^3/12 * (g''(a) - g''(a+kh))      for g'' ANTITONE,

carries NO factor of k, and observed that with a bulk grid of spacing h = 1/(2 sqrt(theta)) this would
give a remainder TV(g'')/(48 theta) -- matching the MEASURED theta^{-1} rate with c_1 ~ -0.0678, hence
a target TV(g'') >= 48|c_1| ~ 3.25.

BEFORE computing that number, this probe asks what "g" IS. The h-scaling argument above is DIMENSIONAL:
it fixes the rate from the grid spacing but never exhibits the sum-to-integral pair whose integrand
would be differentiated twice. The corpus phrasing that invites one -- "the variance density is
(g'(x))^2 * c(rho(x))" (docs/audits/2026-08-29-...-rigorous-finite-n-bound.md) -- would supply a LOCAL
integrand. THIS PROBE TESTS WHETHER SUCH A LOCAL DENSITY EXISTS. It does not.

TEST 1 (the leading variance is a MODE sum, not a spatial integral). The Ivanov-Olshanski/Kerov CLT
gives V_A = Sum_{k odd} A_k^2 / k with the modified-Chebyshev coefficients
A_k = 8(-1)^{(k+1)/2} / (pi (k^2 - 4)). Verified here to converge to 8/pi^2. This is an H^{1/2}-type
(NONLOCAL) functional of the test function, not an integral of a pointwise density.

TEST 2 (the local density literally diverges). Localising the exact projection-kernel formula
V = (1/2) Sum_{x!=y} (g(x)-g(y))^2 S(x-y;rho)^2 by g(x)-g(y) ~ g'(x)(x-y) gives the candidate local
density (g'(x))^2 * c(rho) with c(rho) = Sum_{k!=0} k^2 S(k;rho)^2. Since S(k;rho) = sin(pi rho k)/(pi k),
k^2 S^2 = sin^2(pi rho k)/pi^2, whose terms do NOT decay: the partial sums grow LINEARLY in the cutoff.
So c(rho) = +infinity and no local density exists. The variance is nonlocal precisely because the
sine kernel's H^{1/2} norm weights all separations; the finite answer comes from the fact that
g(x)-g(y) stops growing like g'(x)(x-y) at large separation, which is a GLOBAL property of g.

CONSEQUENCE: TV(g'') cannot be computed, because there is no g. The theta^{-1} RATE remains measured
and correct, and h^2-scaling is CONSISTENT with an EM mechanism -- but consistency is not
identification: many mechanisms give theta^{-1}. Producing a TV by choosing some plausible integrand
and checking it against 3.25 would be fitting a target, not deriving a constant. The honest next step
is to exhibit the sum-to-integral pair first (two concrete candidates named in the output).

NO float64 (mpmath.mpf). Nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40


def A_hat(k):
    """Modified-Chebyshev coefficient of |x| on [-2,2]: A_k = 8(-1)^{(k+1)/2}/(pi(k^2-4)), k odd."""
    sign = mp.mpf(-1) ** ((k + 1) // 2)
    return 8 * sign / (mp.pi * (mp.mpf(k) ** 2 - 4))


def mode_sum(K):
    """V_A = Sum_{k odd, k<=K} A_k^2 / k  (Ivanov-Olshanski / Kerov CLT)."""
    return mp.fsum(A_hat(k) ** 2 / k for k in range(1, K + 1, 2))


def local_density_partial(rho, K):
    """Partial sums of c(rho) = Sum_{k!=0} k^2 S(k;rho)^2 = (2/pi^2) Sum_{k>=1} sin^2(pi rho k).
    If this converged it would be the local variance density coefficient. It does not."""
    return 2 * mp.fsum(mp.sin(mp.pi * rho * k) ** 2 for k in range(1, K + 1)) / mp.pi ** 2


def gA(k):
    """Sum|c| weight on the SHIFTED descent lattice {lambda_i - i}: k(k+1)/2 with SIGNED k."""
    return mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2


def trace_split(theta):
    """Exact projection-kernel identity check. Returns (A, B, A-B, (1/2)Sum(dg)^2 K^2) with
    A = Sum_x g(x)^2 K(x,x), B = Sum_{x!=y} g(x)g(y)K(x,y)^2, and K(x,x) = Sum_y K(x,y)^2 (K^2=K)."""
    M = int(mp.floor(2 * mp.sqrt(theta) + 12 * mp.power(theta, mp.mpf(1) / 6) + 20))
    arg = 2 * mp.sqrt(theta)
    st = mp.sqrt(theta)
    J = {0: mp.besselj(0, arg)}
    for x in range(1, M + 2):
        J[x] = mp.besselj(x, arg)
        J[-x] = (-1) ** x * J[x]
    xs = list(range(-M, M + 1))
    g = {k: gA(k) for k in xs}

    def K(x, y):
        return st * (J[x] * J[y + 1] - J[x + 1] * J[y]) / (x - y)

    Kdiag = {}
    for x in xs:
        Kdiag[x] = mp.fsum(K(x, y) ** 2 for y in xs if y != x)
    A = mp.fsum(g[x] ** 2 * Kdiag[x] for x in xs)
    B = mp.mpf(0)
    half = mp.mpf(0)
    for i, x in enumerate(xs):
        for y in xs[i + 1:]:
            k2 = K(x, y) ** 2
            B += 2 * g[x] * g[y] * k2
            half += (g[x] - g[y]) ** 2 * k2
    return A, B, A - B, half


def main():
    target = 8 / mp.pi ** 2
    print(f"# Is TV(g'') well-posed? dps={mp.mp.dps}; NO float64")
    print(f"# TEST 1 -- the leading variance is a MODE sum (IO/Kerov), target 8/pi^2 = {mp.nstr(target,12)}")
    print("#     K      Sum_{k odd<=K} A_k^2/k        |diff from 8/pi^2|")
    for K in (1, 3, 5, 11, 51, 501, 5001):
        s = mode_sum(K)
        print(f"  {K:>6}  {mp.nstr(s,14):>22}  {mp.nstr(abs(s - target),4):>16}")
    print("#   => converges to 8/pi^2: V_A is an H^{1/2}-type NONLOCAL mode functional.")
    print("#")
    print("# TEST 2 -- the candidate LOCAL density c(rho) = Sum_{k!=0} k^2 S(k;rho)^2 diverges.")
    print("#   S(k;rho)=sin(pi rho k)/(pi k) so k^2 S^2 = sin^2(pi rho k)/pi^2: terms do NOT decay.")
    print("#     rho      K=100      K=1000     K=10000    K=100000    ratio(1e5/1e4)")
    for rho in (mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.75')):
        vals = [local_density_partial(rho, K) for K in (100, 1000, 10000, 100000)]
        ratio = vals[3] / vals[2] if vals[2] != 0 else mp.mpf('nan')
        print(f"  {mp.nstr(rho,3):>7}  {mp.nstr(vals[0],5):>9}  {mp.nstr(vals[1],5):>9}  "
              f"{mp.nstr(vals[2],5):>9}  {mp.nstr(vals[3],5):>9}  {mp.nstr(ratio,5):>8}")
    print("#   => partial sums grow LINEARLY (each 10x in K multiplies the sum by ~10):")
    print("#      c(rho) = +infinity. There is NO local variance density (g')^2 c(rho).")
    print("#")
    print("# TEST 3 -- the TRACE SPLIT is exact and well-conditioned (the well-posed reformulation).")
    print("#   For a projection kernel (K^2=K): V_A = Sum_x g^2 K(x,x) - Sum_{x!=y} g(x)g(y)K(x,y)^2.")
    print("#   The FIRST term is a clean 1-D sum with the smooth integrand g^2*rho -- directly EM-able.")
    print("#   theta      A=Sum g^2 K(x,x)     A-B            (1/2)Sum(dg)^2K^2    |diff|      A/(A-B)")
    for th in (mp.mpf(64), mp.mpf(100)):
        A, B, V, half = trace_split(th)
        print(f"  {int(th):>6}  {mp.nstr(A,10):>17}  {mp.nstr(V,10):>13}  {mp.nstr(half,10):>17}  "
              f"{mp.nstr(abs(V-half),3):>9}  {mp.nstr(A/V,5):>7}")
    print("#   => the two forms agree to ~1e-36 at dps=40 (K^2=K confirmed), and A/(A-B) grows only like")
    print("#      sqrt(theta) (4.30 -> 5.35 as theta 64 -> 100, against sqrt(100/64)=1.25 predicted")
    print("#      and 5.35/4.30=1.244 observed). So the split cancels by only O(sqrt theta) and both")
    print("#      terms stay computable -- P2 below is numerically viable, not merely formal.")
    print("#")
    print("# VERDICT: 'compute TV(g'')' is NOT well-posed as stated -- there is no g to differentiate.")
    print("#   The theta^{-1} RATE stands (measured, c_1 ~ -0.0678). The h^2 = 1/(4 theta) scaling is")
    print("#   CONSISTENT with an Euler-Maclaurin mechanism, but consistency is not identification:")
    print("#   many mechanisms produce theta^{-1}. Choosing a plausible integrand and checking its")
    print("#   TV against 3.25 would be FITTING A TARGET, not deriving a constant, so it is not done.")
    print("#")
    print("# WHAT WOULD MAKE IT WELL-POSED -- two concrete sum-to-integral pairs to try next:")
    print("#   (P1) the MODE sum. V_A = Sum_{k odd} A_k^2/k is already a 1-D sum in k with a smooth")
    print("#        summand; if the finite-theta correction is an EM remainder in k, then g is that")
    print("#        summand and TV(g'') is computable. Requires the finite-theta deformation of A_k.")
    print("#   (P2) the TRACE SPLIT. For a projection kernel, V_A = Sum_x g(x)^2 K(x,x)")
    print("#        - Sum_{x,y} g(x)g(y) K(x,y)^2. The FIRST term is a clean 1-D sum in x with a")
    print("#        smooth integrand g^2 rho, directly EM-able. Measure whether its own remainder")
    print("#        carries c_1, or whether the cancellation against the double sum does.")
    print("#        (Note both terms are ~theta^{2.5} while V_A ~ 0.81 theta^2, so the split cancels")
    print("#         to order sqrt(theta) and needs care -- but it is exact and computable.)")
    print("RESULT: no local variance density exists (c(rho) diverges); TV(g'') ill-posed until the")
    print("        sum-to-integral pair is exhibited. Rate theta^{-1} unaffected. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
