#!/usr/bin/env python3
"""M_1>0 machinery (qou-tvok, step 1): the EXACT leading constant of Var(Sum|c|) is v_A = 8/pi^2,
DERIVED (not fitted) and verified three ways.

Gap qou-k5r5, epic qou-h315. The (CS) closure needs |V_A(theta)/theta^2 - v_A| <= C_A theta^{-p}.
This script pins the leading constant v_A rigorously; the remainder constant C_A + rate is the rest
of qou-tvok.

DERIVATION (rigorous modulo the cited Ivanov-Olshanski Kerov CLT):
  1. IO Kerov CLT: v_A = sum_k hat_A_k^2 / k, where hat_A_k = (2/pi) int_0^pi |2cos phi| sin(k phi) sin phi dphi
     is the modified-Chebyshev coefficient of the test function |x| (the #5901 convention).
  2. CLOSED FORM (elementary integral): even k vanish; for odd k=2m+1,
        hat_A_{2m+1} = 8(-1)^{m+1} / (pi ((2m+1)^2 - 4)).
  3. Hence v_A = (64/pi^2) * sum_{n odd>=1} 1 / [ n (n^2-4)^2 ].
  4. ELEMENTARY RATIONAL-SERIES IDENTITY (partial fractions + telescoping):
        sum_{n odd>=1} 1/[n(n^2-4)^2] = 1/8,
     via  1/(n(n^2-4)^2) = 1/(16n) - 1/(32(n-2)) - 1/(32(n+2)) + 1/(32(n-2)^2) - 1/(32(n+2)^2):
       * linear parts: coeff of the divergent sum_{odd} 1/j is 1/16 - 1/32 - 1/32 = 0 (cancels);
         the boundary terms (j=-1 from n-2, and j=1 restored in n+2) leave 1/32 + 1/32 = 1/16.
       * quadratic parts: the sum_{odd} 1/j^2 (= pi^2/8) cancels; boundary terms 1/(-1)^2 and 1/1^2
         leave (1 + 1)/32 = 1/16.
       * total 1/16 + 1/16 = 1/8. (Both the divergent linear tail AND the pi^2/8 quadratic tail
         cancel exactly -- the result is purely rational.)
  5. => v_A = 64/(8 pi^2) = 8/pi^2 = 0.8105694691...

This script VERIFIES each step numerically (exact/mpmath; NO float64):
  A. hat closed form vs the integral (odd k);
  B. sum_k hat_k^2/k vs 8/pi^2;
  C. the rational series vs 1/8 (partial sum + partial-fraction termwise check);
  D. the descent-DPP measurement V_A/theta^2 -> 8/pi^2 (Richardson), cross-check.

scope-(a); no fit (v_A is DERIVED in closed form, then checked); nothing wired; no c_k; L2 unchanged.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40
TARGET = 8 / mp.pi ** 2


def hat_integral(k):
    """(2/pi) int_0^pi |2 cos phi| sin(k phi) sin phi dphi."""
    return (2 / mp.pi) * mp.quad(
        lambda p: abs(2 * mp.cos(p)) * mp.sin(k * p) * mp.sin(p), [0, mp.pi / 2, mp.pi])


def hat_closed(k):
    """Closed form: 0 for even k; 8(-1)^{m+1}/(pi((2m+1)^2-4)) for k=2m+1."""
    if k % 2 == 0:
        return mp.mpf(0)
    m = (k - 1) // 2
    return 8 * mp.mpf((-1) ** (m + 1)) / (mp.pi * ((2 * m + 1) ** 2 - 4))


def main():
    print(f"# v_A leading-constant derivation; dps={mp.mp.dps}; NO float64;  8/pi^2 = {mp.nstr(TARGET,18)}")

    # A. closed form vs integral (odd k)
    print("# A. hat_A_k closed form vs integral (odd k):")
    maxerr = mp.mpf(0)
    for k in (1, 3, 5, 7, 9, 11):
        d = abs(hat_closed(k) - hat_integral(k)); maxerr = max(maxerr, d)
        print(f"#     k={k:>2}: closed={mp.nstr(hat_closed(k),10):>13}  |closed-int|={mp.nstr(d,3)}")
    print(f"#   max |closed-integral| over odd k<=11: {mp.nstr(maxerr,3)}")

    # B. v_A = sum_k hat_k^2/k (odd k only; hat_k^2/k ~ 64/(pi^2 k^5), tail<1e-15 past k=9999)
    vA = mp.mpf(0)
    for k in range(1, 10000, 2):
        vA += hat_closed(k) ** 2 / k
    print(f"# B. sum_k hat_A_k^2/k = {mp.nstr(vA,16)}   |.-8/pi^2| = {mp.nstr(vA-TARGET,3)}")

    # C. rational series sum_{n odd} 1/[n(n^2-4)^2] = 1/8, and partial-fraction termwise identity
    def direct(n): return mp.mpf(1) / (n * (n * n - 4) ** 2)
    def pf(n):
        return (mp.mpf(1) / (16 * n) - mp.mpf(1) / (32 * (n - 2)) - mp.mpf(1) / (32 * (n + 2))
                + mp.mpf(1) / (32 * (n - 2) ** 2) - mp.mpf(1) / (32 * (n + 2) ** 2))
    pf_err = max(abs(pf(n) - direct(n)) for n in (1, 3, 5, 7, 9))
    ser = mp.nsum(lambda m: direct(2 * int(m) + 1), [0, mp.inf])
    print(f"# C. sum_{{n odd}} 1/[n(n^2-4)^2] = {mp.nstr(ser,16)}   |.-1/8| = {mp.nstr(ser-mp.mpf(1)/8,3)}")
    print(f"#     partial-fraction termwise |pf-direct| (n<=9): {mp.nstr(pf_err,3)}")
    print(f"#     => v_A = (64/pi^2)*(1/8) = 8/pi^2 : (64/pi^2)*ser = {mp.nstr(64/mp.pi**2*ser,16)}")

    # D. descent-DPP cross-check: V_A/theta^2 -> 8/pi^2 (values from the expansion probe, Richardson)
    dpp = [(mp.mpf(2048), mp.mpf('0.8105366966642052')),
           (mp.mpf(4096), mp.mpf('0.8105529725417662')),
           (mp.mpf(8192), mp.mpf('0.8105611744806201'))]
    (t0, s0), (t1, s1), (t2, s2) = dpp
    r = t2 / t1; v_rich = s2 - (s1 - s2) / (r - 1)     # assume theta^{-1} leading
    print(f"# D. descent-DPP V_A/theta^2 Richardson(theta^-1) = {mp.nstr(v_rich,12)}  "
          f"|.-8/pi^2| = {mp.nstr(v_rich-TARGET,3)}")

    ok = (maxerr < mp.mpf('1e-30') and abs(vA - TARGET) < mp.mpf('1e-9')
          and abs(ser - mp.mpf(1)/8) < mp.mpf('1e-9') and pf_err < mp.mpf('1e-30'))
    print()
    print("# RESULT: v_A = 8/pi^2 DERIVED (IO CLT + elementary closed form + rational identity 1/8)")
    print(f"#   all checks pass: {ok}. This is the exact leading constant of Var(Sum|c|).")
    print("#   Remaining in qou-tvok: the remainder constant C_A + rate (bulk EM + Airy edge).")
    print(f"RESULT: v_A = 8/pi^2 verified 3 ways; series identity = 1/8 proved by partial fractions. ok={ok}")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
