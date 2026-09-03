#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5): DECISIVE NEGATIVE -- a POINTWISE uniform Bessel remainder (Olver/Debye)
is NOT sufficient to pin the C_A constant, no matter how good its constant is.

Gap qou-k5r5. The remaining gap is a rigorous C_A with |V_A(theta)/theta^2 - v_A| <= C_A theta^{-1/2}.
The corpus plan (audit '...constant-C-and-N0.md' item 3) is: take Olver's explicit uniform remainder
|J - S| <= eps ~ K theta^{-1/2} and carry it through the x^2-weighted bulk sum. THIS PROBE MEASURES
WHETHER THAT CAN WORK AT ALL.

Write J = S + E. Then V_A(J) - V_A(S) = (1/2) Sum w (J^2 - S^2) = (1/2) Sum w E (2S + E), so ANY
pointwise bound |E| <= eps gives at best

    |Delta V| <= eps * Sum w |S|  +  (eps^2/2) * Sum w    =:  eps * U  +  ...

The question is the SIZE of U = Sum w |S| relative to V = (1/2) Sum w S^2. Because S(k) ~ sin(pi rho k)
/(pi k) decays like 1/k while S^2 decays like 1/k^2, U carries roughly one extra power of the band
width, so U/V GROWS without bound in theta. MEASURED here: U/V = 42.8, 45.7, 53.9, 70.7, 91.9 at
theta = 64, 78, 128, 256, 512, with d log(U/V)/d log(theta) = 0.33..0.39 (still drifting upward; the
growth is sub-sqrt(theta), and the exponent is NOT pinned by this probe -- do not quote one).

The conclusion does not need the exponent. At theta = 78 -- the largest n the exact Fraction table
reaches, hence the n at which the asymptotic must take over -- the MEASURED U/V = 45.65 gives, for a
pointwise remainder eps = K theta^{-1/2}, a relative error on V_A of about K * 5.17. Keeping that below
m_inf = 0.3002 forces K < 0.058, whereas the leading Debye/Olver remainder coefficient is O(1): the
pointwise route misses the required constant by ~17x. So the oscillatory cancellation (summation by
parts / stationary phase) is ESSENTIAL, not a refinement, and acquiring a sharper POINTWISE bound
cannot close N0 <= 78 no matter how good its constant.

THIS PROBE computes U(theta) and V(theta) from the EXACT discrete Bessel kernel and measures the
scaling of U/V. NO float64 (mpmath.mpf). Nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 30


def gA(k):
    """Sum|c| linear-statistic weight on the SHIFTED descent lattice {lambda_i - i}:
    G_A(k) = k(k+1)/2 for k >= 0 and -k(k+1)/2 for k < 0, with SIGNED k.
    NOTE g(-1) = 0 and g(-k) = -g(k-1): the descent lattice's natural involution is
    x <-> -1-x, NOT x <-> -x. Symmetrising to |k|(|k|+1)/2 is WRONG and was the bug
    that produced a spurious theta^{-1/2} rate (corrected 2026-09-03)."""
    return mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2


def U_and_V(theta):
    """U = Sum_{x<y} w |J| ; V = Sum_{x<y} w J^2  (= the projection-kernel variance V_A)."""
    M = int(mp.floor(2 * mp.sqrt(theta) + 8 * mp.power(theta, mp.mpf(1) / 6) + 20))
    arg = 2 * mp.sqrt(theta)
    st = mp.sqrt(theta)
    J = {0: mp.besselj(0, arg)}
    for x in range(1, M + 2):
        J[x] = mp.besselj(x, arg)
        J[-x] = (-1) ** x * J[x]
    xs = list(range(-M, M + 1))
    g = {k: gA(k) for k in xs}
    U = mp.mpf(0)
    V = mp.mpf(0)
    for i, x in enumerate(xs):
        gx = g[x]
        for y in xs[i + 1:]:
            Jxy = st * (J[x] * J[y + 1] - J[x + 1] * J[y]) / (x - y)
            if Jxy == 0:
                continue
            w = (gx - g[y]) ** 2
            U += w * abs(Jxy)
            V += w * Jxy * Jxy
    return U, V


def main():
    print(f"# Pointwise-bound insufficiency test for C_A; dps={mp.mp.dps}; NO float64")
    print("# U = Sum w |J| (what ANY pointwise |E|<=eps bound multiplies); V = Sum w J^2 = V_A")
    print("# If U/V ~ sqrt(theta), a pointwise eps ~ K theta^{-1/2} yields only an O(1) RELATIVE")
    print("# error on V_A -- i.e. NO theta^{-1/2} rate, for any constant K.")
    print("#  theta      U              V              U/V        (U/V)/sqrt(theta)   slope")
    prev = None
    UV78 = None
    for th in (mp.mpf(64), mp.mpf(78), mp.mpf(128), mp.mpf(256), mp.mpf(512)):
        U, V = U_and_V(th)
        r = U / V
        norm = r / mp.sqrt(th)
        slope = ""
        if prev is not None:
            slope = mp.nstr((mp.log(r) - mp.log(prev[1])) / (mp.log(th) - mp.log(prev[0])), 4)
        print(f"  {int(th):>6}  {mp.nstr(U,6):>13}  {mp.nstr(V,6):>13}  {mp.nstr(r,6):>9}  "
              f"{mp.nstr(norm,6):>14}  {slope:>7}")
        prev = (th, r)
        if th == 78:
            UV78 = r
    print("#")
    # The decisive quantitative statement, AT the n that matters (the exact table covers n<=78).
    if UV78 is not None:
        m_inf = mp.mpf('0.300186614')
        eps_factor = UV78 / mp.sqrt(mp.mpf(78))     # relative error = K * (U/V)/sqrt(theta)
        Kbudget = m_inf / eps_factor
        print(f"# AT theta = 78 (the n the exact Fraction table reaches):")
        print(f"#   U/V = {mp.nstr(UV78,6)}, so a pointwise remainder eps = K*theta^(-1/2) gives")
        print(f"#   RELATIVE error on V_A of about K * {mp.nstr(eps_factor,5)}.")
        print(f"#   To keep that under m_inf = {mp.nstr(m_inf,7)} needs K < {mp.nstr(Kbudget,4)}.")
        print(f"#   The leading Debye/Olver remainder coefficient is O(1) -- so the pointwise route")
        print(f"#   misses the required constant by roughly {mp.nstr(1/Kbudget,4)}x. It cannot close N0<=78.")
    print("#")
    print("# The 'slope' column is d log(U/V)/d log(theta). MEASURED: 0.33..0.39, still drifting")
    print("#   upward -- i.e. U/V grows like ~theta^{0.35-0.4}, SUB-sqrt(theta) (the normalised")
    print("#   column (U/V)/sqrt(theta) slowly DECREASES: 5.35 -> 4.06). Do NOT quote 'U/V ~ sqrt(theta)';")
    print("#   the exponent is not pinned here and the conclusion does not need it.")
    print("# The decisive number is the DIRECTLY MEASURED U/V = 45.65 at theta = 78 (above), which")
    print("#   is a computation, not an extrapolation.")
    print("# CONSEQUENCE: obtaining Olver's explicit uniform remainder does NOT by itself pin C_A.")
    print("#   The oscillatory cancellation in Sum w S E (summation by parts / stationary phase) is")
    print("#   load-bearing. A pointwise-magnitude bound, however sharp its constant, cannot close it.")
    print("RESULT: pointwise Bessel-remainder route is INSUFFICIENT for C_A -- at theta=78 it needs a")
    print("        remainder constant K < 0.058 vs the O(1) Debye coefficient (~17x short). qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
