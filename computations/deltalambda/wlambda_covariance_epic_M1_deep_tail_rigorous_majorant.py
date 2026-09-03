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

RIGOROUS ELEMENTARY BOUNDS USED (both corpus-free standards, real argument, integer order):
    (i)  |J_x(2 sqrt(theta))| <= theta^{|x|/2} / |x|!            (DLMF 10.14.4)
    (ii) |J_n(z)| <= 1                                            (universal, n integer, z real)
The code uses their MINIMUM, Jbound(x) = min( theta^{|x|/2}/|x|!, 1 ), which is valid everywhere.
Bound (i) alone is tight ONLY in the deep tail and is exponentially LOOSE in the bulk (it exceeds 1
there), which is why the min is needed: a tail index then contributes its tiny (i), while a bulk
index contributes at worst 1.

The cutoff is X* := the first index at which the (i)-factor drops below 1e-20 (NOT ceil(e sqrt th);
the (i)-factor first falls below 1 near e sqrt(theta), but reaching 1e-20 takes a further O(sqrt th)).
Beyond X* the far tail is rigorously negligible with NO uniform-asymptotic input. The band
2 sqrt(theta) < x <= X* is where only the trivial bound (ii) is available -- too crude to expose the
O(theta^{-1/2}) Bessel->sine cancellation -- so that band, plus the bulk oscillatory error, are the
regions that would require Olver.

THIS PROBE: (a) verifies |besselj(x,2sqrt th)| <= Jbound(x) on a grid (sanity of the bound);
(b) computes a RIGOROUS upper bound on the far-tail (|x| or |y| > X*) contribution to
V_A = (1/2) Sum (g(x)-g(y))^2 J(x,y;th)^2; (c) computes a RIGOROUS LOWER bound on V_A itself -- every
term of that sum is non-negative, so any windowed partial sum is a valid lower bound -- so that the
reported far-tail SHARE is a genuine rigorous upper bound on the true ratio, not a division by a
measured reference scale; (d) reports the width of the band that remains Olver-dependent.
NO float64 (mpmath.mpf). Nothing wired; no c_k; L2 unchanged. Gap OPEN.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 50


def gA(k):
    """Sum|c| linear-statistic weight on the SHIFTED descent lattice {lambda_i - i}:
    G_A(k) = k(k+1)/2 for k >= 0 and -k(k+1)/2 for k < 0, with SIGNED k.
    NOTE g(-1) = 0 and g(-k) = -g(k-1): the descent lattice's natural involution is
    x <-> -1-x, NOT x <-> -x. Symmetrising to |k|(|k|+1)/2 is WRONG and was the bug
    that produced a spurious theta^{-1/2} rate (corrected 2026-09-03)."""
    return mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2


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


def VA_lower_bound(theta, W):
    """RIGOROUS LOWER bound on V_A = Sum_{x<y} (gA(x)-gA(y))^2 J(x,y;theta)^2.
    EVERY term is a product of two squares, hence non-negative, so ANY partial sum over a sub-window
    is a valid lower bound for the full sum. Here: the window |x|,|y| <= W, evaluated with the EXACT
    kernel at 50 dps (arithmetic error ~1e-45 relative, far below any digit reported)."""
    arg = 2 * mp.sqrt(theta)
    st = mp.sqrt(theta)
    J = {0: mp.besselj(0, arg)}
    for x in range(1, W + 2):
        J[x] = mp.besselj(x, arg)
        J[-x] = (-1) ** x * J[x]
    xs = list(range(-W, W + 1))
    g = {k: gA(k) for k in xs}
    tot = mp.mpf(0)
    for i, x in enumerate(xs):
        gx = g[x]
        for y in xs[i + 1:]:
            Jxy = st * (J[x] * J[y + 1] - J[x + 1] * J[y]) / (x - y)
            tot += (gx - g[y]) ** 2 * Jxy * Jxy
    return tot


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
    print(f"# elementary bound Jbound(x) = min( theta^(|x|/2)/|x|! , 1 ) >= |J_x(2 sqrt th)|")
    print(f"#   [(i) DLMF 10.14.4 + (ii) universal |J_n(real)|<=1; both corpus-free]")
    print("#")
    for theta in (mp.mpf(100), mp.mpf(256), mp.mpf(640)):
        st = mp.sqrt(theta)
        edge = 2 * st
        Xstar = find_Xstar(theta, mp.mpf(10) ** (-20))   # Bdeep(X*) < 1e-20
        M = Xstar + int(mp.ceil(2 * st)) + 40             # truncation past X* (Bdeep already <1e-20)
        # (a) sanity: the rigorous bound dominates exact besselj across bulk+tail
        grid = list(range(2, M, max(1, M // 40)))
        worst = verify_bound(theta, grid)
        # (b) rigorous FAR-tail upper bound (at least one index beyond X*)
        tail = deep_tail_majorant(theta, Xstar, M)
        # (c) RIGOROUS LOWER bound on V_A (non-negative terms => windowed partial sum is valid).
        #     This is what makes the reported SHARE a genuine bound rather than a division by a
        #     measured reference scale.
        W = int(mp.ceil(2 * st))
        VA_lo = VA_lower_bound(theta, W)
        share = tail / VA_lo                      # rigorous: tail/V_A <= tail/VA_lo since V_A >= VA_lo
        # (d) the region <= X* that still needs Olver (trivial |J|<=1 too crude there)
        band_lo, band_hi = edge, Xstar
        print(f"# theta={int(theta)}: edge 2sqrt={mp.nstr(edge,5)}, X* (factor<1e-20)={Xstar}, M={M}")
        print(f"#   (a) max |besselj|/Jbound over grid = {mp.nstr(worst,4)}  (must be <=1 => "
              f"{'OK' if worst <= 1 else 'FAIL'})")
        print(f"#   (b) RIGOROUS far-tail ABSOLUTE bound (|x| or |y| > X*) <= {mp.nstr(tail,4)}")
        print(f"#   (c) RIGOROUS LOWER bound V_A >= {mp.nstr(VA_lo,6)} (window |.|<={W}, non-neg terms)")
        print(f"#       => RIGOROUS far-tail share  tail/V_A <= {mp.nstr(share,4)}")
        print(f"#   (d) Olver-dependent region x in ({mp.nstr(band_lo,5)}, {Xstar}] (edge+transition+")
        print(f"#       outer-bulk error) width {mp.nstr(band_hi-band_lo,4)} ~ O(sqrt(theta))")
        print("#")
    print("# VERDICT: the FAR tail (|x| > X*, where the DLMF-10.14.4 factor < 1e-20) contributes a")
    print("#   RIGOROUSLY negligible amount to V_A, using only the corpus-free elementary bounds")
    print("#   min(theta^{x/2}/x!, 1) >= |J_x(2sqrt th)|. NO Olver needed there. What the elementary")
    print("#   bounds CANNOT resolve is the region |x| <= X* (~ 2sqrt th .. e sqrt th + O(sqrt th)):")
    print("#   there |J|<=1 is too crude to see the O(theta^{-1/2}) Bessel->sine cancellation that sets")
    print("#   C_A.")
    print("# BUT NOTE (companion probe _pointwise_bound_insufficiency.py): supplying a sharper")
    print("#   POINTWISE bound on that band -- Olver's uniform remainder included -- does NOT close it")
    print("#   either. At theta=78 the pointwise route needs a remainder constant K<0.058 against an")
    print("#   O(1) Debye coefficient (~17x short). The band needs the OSCILLATORY CANCELLATION")
    print("#   (summation by parts / stationary phase), not a better magnitude bound. So this probe")
    print("#   localises WHERE the work is, and the companion probe shows a citation will not do it.")
    print("RESULT: far-tail |x|>X* pinned rigorously corpus-free (both directions); the O(sqrt th)-wide")
    print("        band x<=X* needs the oscillatory cancellation, not a pointwise bound. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
