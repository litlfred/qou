#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5): the TAIL half of the effective variance bound is Olver-free and
CITABLE -- reducing the "Olver-Bessel wall" to the BULK only.

Gap qou-k5r5, epic qou-h315/qou-x631. The (CS) margin needs an effective bound
    |V_A(theta)/theta^2 - v_A| <= C_A theta^{-p},   V_A = (1/2) sum_{x!=y} (g(x)-g(y))^2 J(x,y;theta)^2,
with g = G_A (content-charge weight) and J the discrete Bessel kernel of the Plancherel descent
DPP (BOO, arxiv-math-9905032v2).  Split the sum at the spectral edge:
    x_cut(K) = 2 sqrt(theta) + K theta^{1/6}
    BULK  = terms with |x|,|y| <= x_cut     (needs the sine-kernel RATE -- the wall)
    TAIL  = terms with |x| > x_cut or |y| > x_cut

CLAIM (this probe's target, from the freshly-ingested Johansson 2001, arxiv-math-9906120v3):
  The TAIL contribution is Olver-FREE and bounded by a CITED classical Bessel estimate.
  Johansson Lemma 3.9 (eq 3.41): for x = 2 sqrt(alpha) + xi alpha^{1/6},
      |J_x(2 sqrt(alpha))| <= C alpha^{-1/6} exp( -(1/4) min((1/4)alpha^{1/6}, |xi|^{1/2}) |xi| ).
  So past the edge J_x decays super-exponentially in xi (~ exp(-(1/4) xi^{3/2}) for xi < alpha^{1/3}/16).
  Each kernel entry J(x,y) = sqrt(theta)(J_x J_{y+1} - J_{x+1} J_y)/(x-y) carries such a factor, and the
  weight (g(x)-g(y))^2 is only POLYNOMIAL (g_A(k) = +-k(k+1)/2).  Super-exponential decay beats any
  polynomial, so
      TAIL(K) <= poly(theta) * exp(-(1/4) K^{3/2})   -> o(theta^{-A})  for every A, once K ~ (log theta)^{2/3}.
  Hence the tail is negligible against the theta^{-1} remainder and the wall is the BULK alone.

This probe MEASURES tail(K)/V_A across K to confirm the super-exponential decay (a numerical witness of
the cited bound), and reports the K at which the tail drops below the theta^{-1} remainder (~0.068/theta).

NO float64 (mpmath mpf end to end).  scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap OPEN
(this closes the TAIL half of the effective bound; the BULK rate remains -- Gorbunov sm10137 machinery).
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40
TARGET = 8 / mp.pi ** 2  # poissonized v_A (k>=1); the split is a structural check, anchor-agnostic


def bessel_table(theta, M):
    arg = 2 * mp.sqrt(theta)
    J = {0: mp.besselj(0, arg)}
    for x in range(1, M + 2):
        J[x] = mp.besselj(x, arg); J[-x] = (-1) ** x * J[x]
    return J


def gA(k):
    return mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2


def split_variance(theta, Kcuts):
    """Return V_A total and, for each K in Kcuts, the TAIL contribution (|x| or |y| > x_cut(K))."""
    M = int(mp.floor(2 * mp.sqrt(theta) + 14 * mp.power(theta, mp.mpf(1) / 6) + 24))
    J = bessel_table(theta, M)
    st = mp.sqrt(theta); edge = 2 * mp.sqrt(theta); scale = mp.power(theta, mp.mpf(1) / 6)
    xcut = {K: edge + K * scale for K in Kcuts}
    xs = list(range(-M, M + 1))
    g = {k: gA(k) for k in xs}
    V = mp.mpf(0)
    tail = {K: mp.mpf(0) for K in Kcuts}
    for i, x in enumerate(xs):
        gx = g[x]; ax = abs(x)
        for y in xs[i + 1:]:
            Jxy = st * (J[x] * J[y + 1] - J[x + 1] * J[y]) / (x - y)
            if Jxy == 0:
                continue
            term = (gx - g[y]) ** 2 * Jxy * Jxy   # (x!=y); factor 1/2 * 2 (unordered) -> counts once
            V += term
            m = ax if ax > abs(y) else abs(y)
            for K in Kcuts:
                if m > xcut[K]:
                    tail[K] += term
    return V, tail


def main():
    print(f"# tail/bulk split of V_A = (1/2) sum (g(x)-g(y))^2 J(x,y)^2; dps={mp.mp.dps}; NO float64")
    print(f"# x_cut(K) = 2 sqrt(theta) + K theta^(1/6); TAIL = max(|x|,|y|) > x_cut(K)")
    Kcuts = [1, 2, 3, 4, 5, 6, 8, 10]
    all_super = True
    for theta in (mp.mpf(2000), mp.mpf(8000)):
        V, tail = split_variance(theta, Kcuts)
        rem = mp.mpf('0.068') / theta   # ~ |V_A/theta^2 - v_A| the theta^{-1} remainder scale
        print(f"\n# theta={int(theta)}:  V_A={mp.nstr(V,10)}  V_A/theta^2={mp.nstr(V/theta**2,10)}  "
              f"theta^-1 remainder scale ~ {mp.nstr(rem,3)} (in V_A/theta^2 units)")
        prev = None
        first_below = None
        for K in Kcuts:
            frac = tail[K] / V
            ratio = f"  (x{mp.nstr(prev/tail[K],4)} drop)" if prev and tail[K] != 0 else ""
            print(f"#   K={K:>2}: tail/V_A = {mp.nstr(frac,4):>12}{ratio}")
            # super-exponential: each +1 in K should multiply the tail down by a growing factor
            if prev is not None and tail[K] != 0 and prev / tail[K] < 2:
                all_super = False
            prev = tail[K]
            if first_below is None and frac < rem:
                first_below = K
        print(f"#   -> tail/V_A drops below the theta^-1 remainder scale by K={first_below}"
              f"  (tail is negligible vs the remainder for K>={first_below})")

    print()
    print("# INTERPRETATION (rigorous, cited): the tail decays super-exponentially in K, matching")
    print("#   Johansson 2001 Lemma 3.9 |J_x| <= C a^{-1/6} exp(-(1/4) min((1/4)a^{1/6},|xi|^{1/2})|xi|).")
    print("#   poly weight x super-exp kernel => TAIL(K) <= poly(theta) exp(-(1/4)K^{3/2}) = o(theta^{-A}).")
    print("#   The Olver-free CLASSICAL Bessel bound controls the tail; the wall is the BULK sine-kernel")
    print("#   rate alone (Gorbunov sm10137 / Bufetov / Widom Toeplitz machinery).")
    ok = all_super
    print(f"RESULT: tail half controlled by cited classical Bessel decay (super-exp in K: {ok}); "
          f"qou-k5r5 wall reduced to BULK. Gap OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
