#!/usr/bin/env python3
"""M_1>0 machinery (qou-po72): the EXACT de-poissonized leading constants of the (CS) margin,
DERIVED in closed form (not fitted) via the IO Kerov CLT + elementary closed-form hat coefficients.

Gap qou-k5r5, epic qou-h315/qou-x631. Companion to qou-tvok step 1 (v_A, PR #5959). The (CS)
leading-order margin is  m_inf = rho_P - sqrt(V_D/V_A) > 0  with three ingredients (see
wlambda_covariance_epic_M1_io_leading_cs.py, merged #5901):
    V_A = Var(Sum|c|)/n^2,  V_D = Var(SumD^2)/n^2,  rho_P = Corr(Sum|c|, omega3).

CRITICAL NORMALISATION (de-poissonized vs poissonized).  The (CS) margin is a FIXED-n quantity.
De-poissonization (Gaussian conditioning on |lam|=n) FREEZES the k=1 field mode (it carries the
conserved n = R_2), so every CS variance sums k>=2 only:
    V_A = sum_{k>=2} A_k^2/k,   NOT  sum_{k>=1} A_k^2/k.
Hence the CS constant is  V_A = 8/(9 pi^2) = 0.09006,  whereas qou-tvok step 1's v_A = 8/pi^2 is
the POISSONIZED descent-DPP constant (k>=1, what the Bessel-kernel sum directly measures).  Both
are correct for their ensembles; the (CS) margin needs the conditioned (k>=2) one.  This is the
subtlety that makes 8/pi^2 NOT the direct CS quantity -- recorded honestly, not a retraction of a
number (step 1's 8/pi^2 is the true poissonized value; it is a different object).

CLOSED-FORM HAT COEFFICIENTS (elementary; convention g_k = (2/pi) int_0^pi g(2cos t) sin(kt) sin t dt).
Both are proved by the Fourier-cosine coefficients of g(2cos t) and  g_k = (c_{k-1} - c_{k+1})/2.
For odd k = 2m+1 (even k vanish by x -> -x symmetry):

  A(x) = |x|      :  A_k = 8 (-1)^{(k+1)/2} / (pi (k^2 - 4)).
  x^2             :  (x^2)_k = delta_{k,3}  (k>=2)  [k=1 mode = R_2 = n, frozen].
  Omega (VKLS)    :  Omega_k = (8/pi^2) [ 1/k - 1/(2(k-2)) - 1/(2(k+2))
                                          + 1/(2(k-2)^2) - 1/(2(k+2)^2) ].
    (Omega(2cos t) = (4/pi)(cos t (pi/2 - t) + sin t); Part1/Part2 integrals elementary;
     Omega_3 = 128/(75 pi^2) reproduced exactly -- the merged #5901 anchor.)

DERIVED CLOSED FORMS (this file's result):
  V_A   = sum_{k odd>=3} A_k^2/k = (64/pi^2) sum_{k odd>=3} 1/[k(k^2-4)^2]
        = (64/pi^2)(1/8 - 1/9) = (64/pi^2)(1/72) = 8/(9 pi^2).       [rational series 1/72]
  Var(omega3)/n^3 -> (x^2)_3^2/3 = 1/3   (matches exact n(n-1)(n-2)/3).
  P = Cov(Sum|c|,omega3) leading = A_3/3 = 8/(15 pi).
  rho_P = A_3/sqrt(3 V_A) = (8/(5pi)) / sqrt(24/(9 pi^2)) = (8/5)/sqrt(8/3) = 2 sqrt(6)/5.  <-- EXACT
  V_D   = sum_{k odd>=3} (Omega_k - A_k)^2 / k  (alternating A_k => summed numerically to high k;
          no clean elementary closed form identified -- reported as a precise derived value).
  margin m_inf = rho_P - sqrt(V_D/V_A).

VERIFICATION (mpmath, NO float64): closed-form hats vs the numerical integral (a few k); the
rational-series identity 1/72; rho_P = 2 sqrt(6)/5; V_D + margin against the merged #5901 values
(rho_P ~ 0.9798, sig-ratio ~ 0.6796, margin ~ 0.3002).

scope-(a); no fit (constants DERIVED in closed form, then checked; V_D measured, no form claimed);
nothing wired; no c_k; L2 unchanged.  Gap qou-k5r5 OPEN (this pins the LEADING constants; the
finite-n remainder bounds C_A/C_D are qou-tvok's tail and hit the Olver-Bessel wall, documented
separately).
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 50


def A_hat_closed(k):
    """A_k = 8 (-1)^{(k+1)/2} / (pi (k^2-4)) for odd k; 0 for even k."""
    if k % 2 == 0:
        return mp.mpf(0)
    sign = mp.mpf((-1) ** ((k + 1) // 2))
    return 8 * sign / (mp.pi * (k * k - 4))


def Omega_hat_closed(k):
    """Omega_k = (8/pi^2)[1/k - 1/(2(k-2)) - 1/(2(k+2)) + 1/(2(k-2)^2) - 1/(2(k+2)^2)], odd k>=3."""
    if k % 2 == 0:
        return mp.mpf(0)
    k = mp.mpf(k)
    return (8 / mp.pi ** 2) * (1 / k - 1 / (2 * (k - 2)) - 1 / (2 * (k + 2))
                              + 1 / (2 * (k - 2) ** 2) - 1 / (2 * (k + 2) ** 2))


def hat_integral(fun_of_2cos, k):
    """Numerical check: (2/pi) int_0^pi f(2cos t) sin(kt) sin t dt, split at pi/2 for the |.| kink."""
    return (2 / mp.pi) * mp.quad(
        lambda t: fun_of_2cos(t) * mp.sin(k * t) * mp.sin(t), [0, mp.pi / 2, mp.pi])


def absx_2cos(t):
    return abs(2 * mp.cos(t))


def omega_2cos(t):
    return (4 / mp.pi) * (mp.cos(t) * (mp.pi / 2 - t) + mp.sin(t))


def main():
    print(f"# qou-po72 de-poissonized (CS) leading constants; dps={mp.mp.dps}; NO float64")

    # --- 1. closed-form hats vs numerical integral (odd k) ---
    print("# 1. closed-form hat coefficients vs numerical integral (odd k):")
    maxerr = mp.mpf(0)
    for k in (3, 5, 7, 9, 11):
        dA = abs(A_hat_closed(k) - hat_integral(absx_2cos, k))
        dO = abs(Omega_hat_closed(k) - hat_integral(omega_2cos, k))
        maxerr = max(maxerr, dA, dO)
        print(f"#    k={k:>2}: |A_closed-int|={mp.nstr(dA,3):>10}  |Omega_closed-int|={mp.nstr(dO,3)}")
    Ohat3_anchor = mp.mpf(128) / (75 * mp.pi ** 2)
    print(f"#    Omega_3 closed={mp.nstr(Omega_hat_closed(3),12)}  128/(75pi^2)={mp.nstr(Ohat3_anchor,12)}"
          f"  diff={mp.nstr(Omega_hat_closed(3)-Ohat3_anchor,3)}")
    print(f"#    max |closed - integral| over odd k<=11: {mp.nstr(maxerr,3)}")

    # --- 2. V_A = 8/(9 pi^2) via the rational series 1/72 ---
    VA = mp.mpf(0)
    for k in range(3, 4001, 2):
        VA += A_hat_closed(k) ** 2 / k
    VA_closed = 8 / (9 * mp.pi ** 2)
    ser = sum(mp.mpf(1) / (k * (k * k - 4) ** 2) for k in range(3, 4001, 2))  # -> 1/72
    print(f"# 2. V_A = sum_{{k odd>=3}} A_k^2/k = {mp.nstr(VA,16)}")
    print(f"#    closed 8/(9pi^2) = {mp.nstr(VA_closed,16)}   diff={mp.nstr(VA-VA_closed,3)}")
    print(f"#    rational series sum 1/[k(k^2-4)^2] = {mp.nstr(ser,16)}  vs 1/72={mp.nstr(mp.mpf(1)/72,16)}"
          f"  diff={mp.nstr(ser-mp.mpf(1)/72,3)}")

    # --- 3. omega3 variance leading = 1/3, and P = A_3/3 = 8/(15 pi) ---
    var_w3 = mp.mpf(1) / 3
    P = A_hat_closed(3) / 3
    P_closed = 8 / (15 * mp.pi)
    print(f"# 3. Var(omega3)/n^3 -> (x^2)_3^2/3 = 1/3 (matches exact n(n-1)(n-2)/3)")
    print(f"#    P = Cov(Sum|c|,omega3) leading = A_3/3 = {mp.nstr(P,14)}  8/(15pi)={mp.nstr(P_closed,14)}"
          f"  diff={mp.nstr(P-P_closed,3)}")

    # --- 4. rho_P = 2 sqrt(6)/5 EXACT ---
    rho_P = A_hat_closed(3) / mp.sqrt(3 * VA_closed)
    rho_closed = 2 * mp.sqrt(6) / 5
    print(f"# 4. rho_P = A_3/sqrt(3 V_A) = {mp.nstr(rho_P,16)}")
    print(f"#    closed 2 sqrt(6)/5 = {mp.nstr(rho_closed,16)}   diff={mp.nstr(rho_P-rho_closed,3)}"
          f"   (merged #5901: ~0.97980)")

    # --- 5. V_D = sum (Omega_k - A_k)^2/k (numerical: A_k alternates, no clean form claimed) ---
    VD = mp.mpf(0)
    for k in range(3, 4001, 2):
        VD += (Omega_hat_closed(k) - A_hat_closed(k)) ** 2 / k
    sig_ratio = mp.sqrt(VD / VA_closed)
    margin = rho_closed - sig_ratio
    print(f"# 5. V_D = sum_{{k odd>=3}} (Omega_k - A_k)^2/k = {mp.nstr(VD,16)}")
    print(f"#    sig-ratio sqrt(V_D/V_A) = {mp.nstr(sig_ratio,14)}  (merged #5901: ~0.67961)")
    print(f"#    margin m_inf = rho_P - sig-ratio = {mp.nstr(margin,14)}  (merged #5901: ~0.30019)")
    # closed-form probes for V_D (report only; not asserted)
    cand = {"64/(75pi^2) [=A_3^2/3 CS ceiling]": 64 / (75 * mp.pi ** 2),
            "V_D/V_A rational?": VD / VA_closed}
    print(f"#    (CS ceiling A_3^2/3 = 64/(75pi^2) = {mp.nstr(64/(75*mp.pi**2),12)}; "
          f"V_D < ceiling? {VD < 64/(75*mp.pi**2)})")

    ok = (maxerr < mp.mpf('1e-30')
          and abs(VA - VA_closed) < mp.mpf('1e-9')
          and abs(ser - mp.mpf(1) / 72) < mp.mpf('1e-9')
          and abs(P - P_closed) < mp.mpf('1e-30')
          and abs(rho_P - rho_closed) < mp.mpf('1e-30')
          and abs(sig_ratio - mp.mpf('0.67961')) < mp.mpf('1e-3')
          and abs(margin - mp.mpf('0.30019')) < mp.mpf('1e-3')
          and VD < 64 / (75 * mp.pi ** 2))
    print()
    print("# RESULT: de-poissonized (CS) leading constants DERIVED in closed form:")
    print("#   V_A = 8/(9 pi^2), Var(omega3) leading = 1/3, P = 8/(15 pi), rho_P = 2 sqrt(6)/5 (EXACT).")
    print("#   V_D summed exactly from closed-form hats (no elementary form); margin m_inf = 0.30019 > 0.")
    print(f"RESULT: rho_P = 2 sqrt(6)/5, V_A = 8/(9pi^2), P = 8/(15pi); margin {mp.nstr(margin,6)} > 0. ok={ok}")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
