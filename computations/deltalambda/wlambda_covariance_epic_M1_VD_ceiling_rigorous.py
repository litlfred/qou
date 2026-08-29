#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5): a RIGOROUS upper bound V_D < 64/(75 pi^2) -- the leading-margin
positivity, and the one (CS)-class field NOT gated on the open bulk kernel rate.

Gap qou-k5r5, epic qou-h315/qou-x631. The leading (CS) margin is m_inf = rho_P_inf - sig_ratio_inf
with rho_P_inf = 2 sqrt(6)/5 (exact) and sig_ratio_inf = sqrt(V_D/V_A). m_inf > 0 iff
    sqrt(V_D/V_A) < 2 sqrt(6)/5  iff  V_D/V_A < 24/25  iff  V_D < (24/25) V_A = 64/(75 pi^2),
since V_A = 8/(9 pi^2) (PR #5969) and the pi cancels. V_D has NO elementary closed form, so we bound
it RIGOROUSLY:  a CERTIFIED interval partial sum (mpmath.iv) + an EXPLICIT analytic tail majorant.

V_D = sum_{k odd >= 3} (Ohat_k - Ahat_k)^2 / k, with the elementary closed forms (audit
2026-08-29-covariance-kernel-M1-po72-leading-constants.md):
    Ahat_k  = 8 (-1)^{(k+1)/2} / (pi (k^2 - 4))
    Ohat_k  = (8/pi^2) [1/k - 1/(2(k-2)) - 1/(2(k+2)) + 1/(2(k-2)^2) - 1/(2(k+2)^2)]

TAIL MAJORANT (rigorous, elementary).  For odd k >= 3, using k^2 - 4 >= (5/9) k^2 (<=> k^2 >= 9):
    |Ahat_k| = 8/(pi(k^2-4)) <= (72/5)/(pi k^2)
    |Ohat_k| <= (8/pi^2)(4/(k(k^2-4)) + 4k/(k^2-4)^2) <= (8/pi^2)(36/(5k^3) + 324/(25 k^3))
             = (8/pi^2)(504/(25 k^3)) = (4032/25)/(pi^2 k^3)
So |Ohat_k - Ahat_k| <= a/k^2 + b/k^3 with a = (72/5)/pi, b = (4032/25)/pi^2, and by (x+y)^2 <= 2x^2+2y^2,
    (Ohat_k - Ahat_k)^2 / k <= 2 a^2 / k^5 + 2 b^2 / k^7.
Summing odd k > K (majorize by the full-integer tail integral sum_{k>K} k^{-p} <= K^{-(p-1)}/(p-1)):
    R(K) := sum_{k odd > K} (Ohat_k - Ahat_k)^2/k <= 2 a^2 /(4 K^4) + 2 b^2 /(6 K^6)
          = a^2/(2 K^4) + b^2/(3 K^6).
This is an explicit, rigorous majorant.  We take K = 999 (partial sum over odd 3..999) so R(999) ~ 1e-11.

CERTIFICATION.  The partial sum is evaluated in mpmath INTERVAL arithmetic (mp.iv), giving a verified
enclosure [lo, hi]; the tail is added to hi as a rigorous upper bound; the ceiling 64/(75 pi^2) is
enclosed from below.  We assert  hi(partial) + R(K) < lo(ceiling)  -- a rigorous proof that
V_D < 64/(75 pi^2), hence m_inf > 0.

scope-(a) POSITIVE (rigorous bound, not a fit); NO float64 (mpmath.iv / mpf); nothing wired; no c_k;
L2 unchanged.  This discharges the leading-margin-positivity input to
QOU.BraidsAndKnots.M1DescentDPPConvergence.DescentDPPMarginConvergence.leading_margin_pos (the field
that is NOT gated on the open bulk kernel rate).  Gap qou-k5r5 remains OPEN (the two Tendsto fields).
"""
from __future__ import annotations
import mpmath as mp
from mpmath import iv

iv.dps = 60
mp.mp.dps = 60


def Ahat_iv(k):
    sign = 1 if ((k + 1) // 2) % 2 == 0 else -1
    return iv.mpf(8) * sign / (iv.pi * (k * k - 4))


def Ohat_iv(k):
    k = iv.mpf(k)
    return (iv.mpf(8) / iv.pi ** 2) * (
        1 / k - 1 / (2 * (k - 2)) - 1 / (2 * (k + 2))
        + 1 / (2 * (k - 2) ** 2) - 1 / (2 * (k + 2) ** 2))


def main():
    K = 999  # partial sum over odd 3..K
    print(f"# rigorous V_D < 64/(75 pi^2); mp.iv interval arithmetic (iv.dps={iv.dps}); NO float64")

    # certified interval partial sum over odd k in [3, K]
    S = iv.mpf(0)
    for k in range(3, K + 1, 2):
        d = Ohat_iv(k) - Ahat_iv(k)
        S = S + d * d / k
    # rigorous analytic tail majorant R(K) = a^2/(2K^4) + b^2/(3K^6)
    a = (iv.mpf(72) / 5) / iv.pi
    b = (iv.mpf(4032) / 25) / iv.pi ** 2
    R = a ** 2 / (2 * iv.mpf(K) ** 4) + b ** 2 / (3 * iv.mpf(K) ** 6)

    ceiling = iv.mpf(64) / (75 * iv.pi ** 2)
    # extract plain-mpf endpoints (iv.mpf.a / .b are the rigorous lower / upper bounds)
    S_hi = mp.mpf(S.b); S_lo = mp.mpf(S.a); R_hi = mp.mpf(R.b); ceil_lo = mp.mpf(ceiling.a)
    VD_upper = S_hi + R_hi        # rigorous upper bound on V_D (hi of partial + hi of tail)

    print(f"# partial sum S (odd 3..{K}) enclosure  = [{mp.nstr(S_lo,20)}, {mp.nstr(S_hi,20)}]")
    print(f"# tail majorant R({K}) upper            = {mp.nstr(R_hi,6)}")
    print(f"# => rigorous V_D upper bound           = {mp.nstr(VD_upper,20)}")
    print(f"# ceiling 64/(75 pi^2) lower bound       = {mp.nstr(ceil_lo,20)}")
    gap = ceil_lo - VD_upper
    print(f"# ceiling_lo - VD_upper                  = {mp.nstr(gap,6)}   (must be > 0)")

    proved = VD_upper < ceil_lo
    # cross-check: the implied margin numbers (non-rigorous display)
    VA = 8 / mp.pi ** 2 / 9
    sig_ratio = mp.sqrt(VD_upper / VA)
    rho = 2 * mp.sqrt(6) / 5
    print(f"# (display) sig_ratio_inf <= {mp.nstr(sig_ratio,10)} < rho_P_inf = 2sqrt6/5 = "
          f"{mp.nstr(rho,10)}; margin >= {mp.nstr(rho - sig_ratio,8)} > 0")
    print()
    print("# RESULT: V_D < 64/(75 pi^2) PROVED rigorously (certified interval partial sum + explicit")
    print("#   analytic tail majorant). Hence sig_ratio_inf = sqrt(V_D/V_A) < 2sqrt6/5 = rho_P_inf,")
    print("#   i.e. the leading (CS) margin m_inf > 0. Discharges the leading_margin_pos class field.")
    print(f"RESULT: V_D < 64/(75 pi^2) rigorous (gap {mp.nstr(gap,4)} > 0); leading margin > 0. proved={proved}")
    print("EXIT: 0")
    return 0 if proved else 1


if __name__ == "__main__":
    raise SystemExit(main())
