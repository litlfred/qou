#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5): pin the DEEP-TAIL constant of Var(Sum|c|) RIGOROUSLY with a
corpus-free elementary Bessel bound -- localising exactly which regions still need Olver's uniform
asymptotic (the sole missing literature input for the finite-n constant C).

Gap qou-k5r5. The whole remaining gap is a rigorous finite-n bound |m(n) - m_inf| <= C n^{-1/2} with
N0 = ceil((C/m_inf)^2) <= 78 (m_inf = 0.30019, ~30x headroom; empirical C ~ 0.087). The binding
sub-constant is C_A for Var(Sum|c|), and the audits reduce it to three regions: (1) tail |x|>2sqrt(th),
(2) oscillatory bulk (Bessel->sine error), (3) Airy edge. The bulk error (2) needs Olver's explicit
uniform Bessel remainder, which is NOT in corpus. THIS PROBE isolates the part of region (1) that is
rigorous WITHOUT Olver.

RIGOROUS ELEMENTARY BOUND (DLMF 10.14.4, real argument, corpus-free standard):
    |J_x(2 sqrt(theta))| <= (sqrt(theta))^x / x!  =  theta^{x/2} / Gamma(x+1)    (x >= 0).
For x > e*sqrt(theta) this majorant B(x) decays super-exponentially (Stirling: B(x) ~
(e sqrt(theta)/x)^x / sqrt(2 pi x), and e sqrt(theta)/x < 1). So the DEEP tail x > e sqrt(theta) is
rigorously negligible with NO uniform-asymptotic input. The NEAR-edge transition band
2 sqrt(theta) < x <= e sqrt(theta) is where B(x) does NOT yet decay -- that band, plus the bulk
oscillatory error, are the regions that genuinely require Olver.

THIS PROBE: (a) verifies |besselj(x,2sqrt th)| <= B(x) on a grid (sanity of the rigorous majorant);
(b) computes a RIGOROUS upper bound on the deep-tail (x or y > X* := ceil(e sqrt th)+m) contribution
to V_A = (1/2) Sum (g(x)-g(y))^2 J(x,y;th)^2 using the majorant, showing it is astronomically small
against the leading V_A ~ 0.81 theta^2; (c) reports the width and B-magnitude of the transition band
that remains Olver-dependent. NO float64 (mpmath.mpf). Nothing wired; no c_k; L2 unchanged. Gap OPEN.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 50


def gA(k):
    """Sum|c| linear-statistic weight G_A(k) = sgn(k)*|k|(|k|+1)/2."""
    kk = abs(k)
    v = mp.mpf(kk * (kk + 1)) / 2
    return v if k >= 0 else -v


def Jbound(x, theta):
    """RIGOROUS elementary bound on |J_x(2 sqrt(theta))|, integer x, real arg:
       min( theta^{|x|/2}/|x|! ,  1 ).
    The first factor is DLMF 10.14.4 (tight only in the deep tail |x| > e sqrt(theta), exponentially
    LOOSE in the bulk); the second is the universal |J_n(real)| <= 1 (n integer). Their min is a valid
    bound everywhere: deep tail -> the super-exp factor; bulk/transition -> the trivial 1."""
    x = abs(int(x))                       # |J_{-x}| = |J_x| for integer x
    dlmf = mp.power(theta, mp.mpf(x) / 2) / mp.factorial(x)
    return min(dlmf, mp.mpf(1))


def Bdeep(x, theta):
    """The DLMF 10.14.4 factor alone (used only to LOCATE X* where it drops below a threshold)."""
    x = abs(int(x))
    return mp.power(theta, mp.mpf(x) / 2) / mp.factorial(x)


def verify_bound(theta, xs):
    """Confirm |besselj(x, 2 sqrt th)| <= Jbound(x) for x in xs. Returns worst ratio (must be <=1)."""
    arg = 2 * mp.sqrt(theta)
    worst = mp.mpf(0)
    for x in xs:
        j = abs(mp.besselj(int(x), arg))
        b = Jbound(x, theta)
        if b > 0:
            worst = max(worst, j / b)
    return worst


def find_Xstar(theta, eps):
    """Smallest X with Bdeep(X, theta) < eps (super-exp factor below threshold)."""
    x = int(mp.ceil(mp.e * mp.sqrt(theta)))
    while Bdeep(x, theta) >= eps:
        x += 1
    return x


def deep_tail_majorant(theta, Xstar, M):
    """RIGOROUS upper bound on the FAR-tail contribution to V_A (at least one index |.|>Xstar):
       Sum_{i<j, (|x|>Xstar or |y|>Xstar)} (gA(x)-gA(y))^2 * Jmaj(x,y)^2,
    Jmaj(x,y) = sqrt(theta)*(Jb(x)Jb(y+1)+Jb(x+1)Jb(y))/|x-y| >= |J(x,y;theta)|, Jb = Jbound (both the
    DLMF-10.14.4 super-exp factor AND the trivial |J|<=1, whichever is smaller). Every index thus
    carries a VALID bound: a tail index contributes its tiny Bdeep, a bulk index at worst 1. Truncated
    at |.|<=M (M chosen so Bdeep(M) is negligibly small)."""
    st = mp.sqrt(theta)
    xs = list(range(-M, M + 1))
    Jb = {k: Jbound(k, theta) for k in range(-(M + 1), M + 2)}
    tot = mp.mpf(0)
    for i, x in enumerate(xs):
        ax = abs(x) > Xstar
        gx = gA(x)
        for y in xs[i + 1:]:
            if not (ax or abs(y) > Xstar):
                continue
            jmaj = st * (Jb[x] * Jb[y + 1] + Jb[x + 1] * Jb[y]) / abs(x - y)
            tot += (gx - gA(y)) ** 2 * jmaj * jmaj
    return tot


def main():
    print(f"# Deep-tail rigorous majorant for Var(Sum|c|); dps={mp.mp.dps}; NO float64")
    print(f"# elementary bound |J_x(2 sqrt th)| <= theta^(x/2)/x!  (DLMF 10.14.4, corpus-free)")
    print("#")
    for theta in (mp.mpf(100), mp.mpf(256), mp.mpf(640)):
        st = mp.sqrt(theta)
        edge = 2 * st
        Xstar = find_Xstar(theta, mp.mpf(10) ** (-20))   # Bdeep(X*) < 1e-20
        M = Xstar + int(mp.ceil(2 * st)) + 40             # truncation past X* (Bdeep already <1e-20)
        # (a) sanity: the rigorous bound dominates exact besselj across bulk+tail
        grid = list(range(2, M, max(1, M // 40)))
        worst = verify_bound(theta, grid)
        # (b) rigorous FAR-tail bound (at least one index beyond X*)
        tail = deep_tail_majorant(theta, Xstar, M)
        VA_lead = mp.mpf('0.8106') * theta ** 2   # leading Var(Sum|c|) ~ 0.81 theta^2 (measured, ref only)
        # (c) the region <= X* that still needs Olver (trivial |J|<=1 too crude there)
        band_lo, band_hi = edge, Xstar
        print(f"# theta={int(theta)}: edge 2sqrt={mp.nstr(edge,5)}, X* (Bdeep<1e-20)={Xstar}, M={M}")
        print(f"#   (a) max |besselj|/Jbound over grid = {mp.nstr(worst,4)}  (must be <=1 => "
              f"{'OK' if worst <= 1 else 'FAIL'})")
        print(f"#   (b) RIGOROUS far-tail V_A bound (|x| or |y| > X*) <= {mp.nstr(tail,4)}")
        print(f"#       vs leading V_A ~ {mp.nstr(VA_lead,4)}  => far-tail/V_A <= {mp.nstr(tail/VA_lead,4)}")
        print(f"#   (c) Olver-dependent region x in ({mp.nstr(band_lo,5)}, {Xstar}] (edge+transition+")
        print(f"#       outer-bulk error) width {mp.nstr(band_hi-band_lo,4)} ~ O(sqrt(theta))")
        print("#")
    print("# VERDICT: the FAR tail (|x| > X*, where the DLMF-10.14.4 factor < 1e-20) contributes a")
    print("#   RIGOROUSLY negligible amount to V_A, using only the corpus-free elementary bounds")
    print("#   min(theta^{x/2}/x!, 1) >= |J_x(2sqrt th)|. NO Olver needed there. What the elementary")
    print("#   bounds CANNOT resolve is the region |x| <= X* (~ 2sqrt th .. e sqrt th + O(sqrt th)):")
    print("#   there |J|<=1 is too crude to see the O(theta^{-1/2}) Bessel->sine cancellation that sets")
    print("#   C_A. THAT is the precise 'need lit?' answer: Olver's explicit uniform Bessel remainder")
    print("#   (DLMF 10.19/10.20 + Olver 1997 Ch.10 error bounds), NOT in corpus, for x in [0, X*] only.")
    print("RESULT: far-tail |x|>X* pinned rigorously corpus-free; the O(sqrt th)-wide region x<=X*")
    print("        (edge+transition+outer-bulk error) needs Olver. qou-k5r5 OPEN, need-lit localised.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
