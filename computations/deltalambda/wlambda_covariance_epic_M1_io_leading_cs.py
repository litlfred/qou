#!/usr/bin/env python3
"""M_1>0 CLOSING MOVE: the (CS) sufficient condition at LEADING order via the IO Kerov CLT.

Gap qou-k5r5, epic qou-x631. PR #5896 reduced M_1>0 to the Cauchy-Schwarz sufficient
condition (CS): sig(SumD2)/sig(Sum|c|) < rho(Sum|c|, omega3). Its three ingredients are
LEADING-ORDER CLT fluctuation quantities, so they are delivered by the same Ivanov-Olshanski
Kerov CLT (arxiv-math-0304010) that derived kappa = Omega-hat_3/3 = 128/(225 pi^2).

Setup (content-profile fluctuation field, from the merged kappa-IO derivation
2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md):
  field  Delta(2 cos t) = (1/pi) sum_{k>=2} (xi_k/sqrt k) sin(k t),  xi_k iid N(0,1)
  a linear content statistic  sum_u g(u) D(u)  has  delta = n^{(deg g + 1)/2} * int g dDelta,
  with  int g dDelta = sum_{k>=2} (xi_k/sqrt k) g-hat_k,
        g-hat_k = (2/pi) int_0^pi g(2 cos t) sin(k t) sin t dt,
  and Cov(int f, int g) = sum_{k>=2} f-hat_k g-hat_k / k.

The three statistics as functions of the content profile D(u):
  Sum|c|  = sum_u |u| D(u)     -> test function A(x) = |x|        (linear, order n)
  SumD2   = sum_u D(u)^2       -> linearises to 2<D>*dD, test fn  2 D_inf(x) = Omega(x) - |x|
  omega3  = sum_u u^2 D(u) - C -> test function x^2, PURE mode k=3 (k=1 frozen = R_2=n)

Leading-order limits (n -> infinity):
  Var(Sum|c|)/n^2 -> V_A = sum_{k>=2} A-hat_k^2 / k
  Var(SumD2)/n^2  -> V_D = sum_{k>=2} (Omega-hat_k - A-hat_k)^2 / k
  Var(omega3)/n^3 -> 1/3            (x^2-hat_k = delta_{k,3}; matches exact n(n-1)(n-2)/3)
  P = Cov(Sum|c|,omega3)/n^{5/2} -> A-hat_3 / 3
  rho(Sum|c|,omega3)    -> A-hat_3 / sqrt(3 V_A)
  sig(SumD2)/sig(Sum|c|) -> sqrt(V_D / V_A)

(CS) at leading order:  sqrt(V_D/V_A) < A-hat_3/sqrt(3 V_A)  <=>  V_D < A-hat_3^2 / 3.

This probe computes A-hat_k, Omega-hat_k (odd k only, by x->-x symmetry) at high precision
(mpmath, NO float64), assembles V_A, V_D, the leading rho and sig-ratio, cross-checks them
against the exact-data asymptotics (rho ~ 0.98, sig-ratio ~ 0.67), and TESTS the leading (CS)
inequality V_D < A-hat_3^2/3.

scope-(a) POSITIVE (a derivation, rigorous modulo the IO CLT theorem, cited not re-proved);
no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN (this settles the LEADING order;
a finite-n bound + exact check to n=78 would close all-n).
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40


def Omega_of_2cos(t):
    """VKLS limit shape Omega(2 cos t) = (4/pi)(cos t (pi/2 - t) + sin t)."""
    return (4 / mp.pi) * (mp.cos(t) * (mp.pi / 2 - t) + mp.sin(t))


def absx_of_2cos(t):
    return abs(2 * mp.cos(t))


def hat(fun, k):
    """g-hat_k = (2/pi) int_0^pi g(2 cos t) sin(k t) sin t dt (split at pi/2 for the |.| kink)."""
    integrand = lambda t: fun(t) * mp.sin(k * t) * mp.sin(t)
    return (2 / mp.pi) * mp.quad(integrand, [0, mp.pi / 2, mp.pi])


def main():
    KMAX = 61  # odd k up to 61; series decay ~1/k^2 (kink) so this is deep convergence
    odd = list(range(3, KMAX + 1, 2))  # k=1 frozen (R2=n conserved); even k vanish by symmetry
    Ahat = {k: hat(absx_of_2cos, k) for k in odd}
    Ohat = {k: hat(Omega_of_2cos, k) for k in odd}
    # sanity: even-k coefficients ~ 0
    even_check = max(abs(hat(absx_of_2cos, k)) for k in (2, 4, 6))
    # Omega-hat_3 must equal 128/(75 pi^2)
    Ohat3_closed = mp.mpf(128) / (75 * mp.pi ** 2)

    V_A = mp.fsum(Ahat[k] ** 2 / k for k in odd)
    V_D = mp.fsum((Ohat[k] - Ahat[k]) ** 2 / k for k in odd)
    A3 = Ahat[3]

    rho_P = A3 / mp.sqrt(3 * V_A)
    sig_ratio = mp.sqrt(V_D / V_A)
    cs_rhs = A3 / mp.sqrt(3 * V_A)          # = rho_P
    cs_lhs = sig_ratio
    cs_margin = cs_rhs - cs_lhs
    # equivalent scalar form
    ineq_lhs = V_D
    ineq_rhs = A3 ** 2 / 3

    print("# IO leading-order values (odd k = 3..%d):" % KMAX)
    print(f"#   A-hat_3           = {mp.nstr(A3,20)}")
    print(f"#   Omega-hat_3       = {mp.nstr(Ohat[3],20)}   closed 128/(75pi^2) = {mp.nstr(Ohat3_closed,20)}")
    print(f"#   |Omega-hat_3 - closed| = {mp.nstr(abs(Ohat[3]-Ohat3_closed),3)}  (must be ~0)")
    print(f"#   even-k A-hat (k=2,4,6) max |.| = {mp.nstr(even_check,3)}  (must be ~0)")
    print(f"#   V_A = Var(Sum|c|)/n^2  -> {mp.nstr(V_A,18)}")
    print(f"#   V_D = Var(SumD2)/n^2   -> {mp.nstr(V_D,18)}")
    print()
    print("## Cross-check leading-order predictions vs the exact-data asymptotics")
    print(f"#   rho(Sum|c|,omega3) -> A3/sqrt(3 V_A) = {mp.nstr(rho_P,12)}   (exact data ~0.98)")
    print(f"#   sig(SumD2)/sig(Sum|c|) -> sqrt(V_D/V_A) = {mp.nstr(sig_ratio,12)}   (exact data ~0.67)")
    # kappa cross-check: M1/n^{5/2} = Omega-hat_3/3
    print(f"#   kappa = Omega-hat_3/3 = {mp.nstr(Ohat[3]/3,15)}   (known 128/(225pi^2) = {mp.nstr(mp.mpf(128)/(225*mp.pi**2),15)})")
    print()
    print("## LEADING-ORDER (CS):  V_D < A-hat_3^2/3   <=>   sig-ratio < rho")
    print(f"#   V_D            = {mp.nstr(ineq_lhs,15)}")
    print(f"#   A-hat_3^2 / 3  = {mp.nstr(ineq_rhs,15)}")
    print(f"#   margin (rhs-lhs) = {mp.nstr(ineq_rhs-ineq_lhs,12)}   relative = {mp.nstr((ineq_rhs-ineq_lhs)/ineq_rhs,6)}")
    print(f"#   (CS) leading margin (rho - sig_ratio) = {mp.nstr(cs_margin,12)}")
    holds = ineq_lhs < ineq_rhs
    print()
    print(f"RESULT: leading-order (CS) holds (V_D < A3^2/3): {holds}; "
          f"sig-ratio={mp.nstr(sig_ratio,6)}, rho={mp.nstr(rho_P,6)}, margin={mp.nstr(cs_margin,4)}")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
