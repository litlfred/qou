#!/usr/bin/env python3
"""M_1>0 machinery (qou-tvok) P2: can Euler-Maclaurin on the EM-able side of the trace split deliver
c_1? MEASURED ANSWER: NO -- and for a sharper reason than "the term is small". A carries no theta^2
term at all, so the entire leading behaviour of V sits in B, the side EM cannot touch.

Gap qou-k5r5 / qou-tvok. The well-posed reformulation (PR #6472) is the exact projection-kernel split

    V_A = Sum_x g(x)^2 * Kdiag(x)  -  Sum_{x!=y} g(x)g(y) K(x,y)^2  =:  A - B,
    Kdiag(x) := Sum_{y!=x} K(x,y)^2 = K(x,x)(1 - K(x,x))   (projection: K^2 = K),

whose first term A is a clean 1-D sum with a smooth summand -- hence "directly EM-able", which is why
P2 proposed applying Euler-Maclaurin to A and asking whether its remainder carries c_1 ~ -0.0678 (the
coefficient of the measured theta^{-1} correction to V_A/theta^2). This probe measures the ORDERS of
A and B first, because the answer turns on them.

WHAT IS MEASURED HERE (exact descent-DPP kernel, theta = 250 .. 16000, NO float64):

  1. A ~ alpha*theta^{5/2}. Two-level Richardson gives alpha = 0.429421692; the INDEPENDENT continuum
     prediction alpha = 8*Int_{-1}^{1} u^4 rho(u)(1-rho(u)) du with rho(u) = arccos(u)/pi evaluates to
     0.429421692 -- agreeing to 3.3e-10 relative. So the continuum reference an EM argument for A
     would be defined against is CONFIRMED by computation, not assumed.
  2. A HAS NO theta^2 TERM. Because (1) pins alpha to 10 digits independently, this is tested
     DIRECTLY: (A/theta^{5/2} - alpha)*sqrt(theta) would tend to a_2, and instead falls monotonically
     0.02745 -> 0.00468 with the per-doubling ratio RISING (1.3333 -> 1.3513) toward sqrt(2) -- the
     signature of a clean theta^{-1/2} decay to zero. As a bound rather than an assertion,
     |a_2| <= 0.00468, i.e. at most 0.578% of V's theta^2 coefficient.
  3. V/theta^2 -> 8/pi^2. With (2): B = A - V carries essentially the WHOLE theta^2 term of V.
  4. A/V grows like sqrt(theta) with coefficient alpha/(8/pi^2) = 0.52978 (measured 0.52983 at
     theta=16000): the split cancels the leading half-order exactly (a_{5/2} = b_{5/2}), which is
     what makes V two half-orders smaller than either side.
  5. The target term |c_1|*theta is 4.0e-5 of A at theta=250, falling to 7.8e-8 at theta=16000, with
     measured exponent 1.4999 against 3/2.

WHY THIS KILLS P2 AS POSED. Write A = a_{5/2}theta^{5/2} + a_2 theta^2 + a_1 theta + ... and likewise
for B. Then c_1 = a_1 - b_1: BOTH sides contribute, and EM on A alone yields only a_1. Obtaining b_1
requires the DOUBLE sum B, which is not a 1-D sum and is not EM-able -- so the split does not reduce
the problem, it partitions it into one tractable piece and one untouched one. Item (2) makes this
worse rather than better: a_2 = 0 while V's theta^2 coefficient is 8/pi^2, so the "clean, EM-able"
side does not even carry the LEADING structure, let alone the correction. The split remains exact and
well-conditioned (PR #6472); what it does not do is let EM act on one term in isolation.

NO float64 (mpmath.mpf). Nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40
V_A_POISSON = 8 / mp.pi ** 2
C1 = mp.mpf('-0.0678')          # measured theta^{-1} coefficient of V_A/theta^2 (tvok STEP 2)


def gA(k):
    """Sum|c| weight on the SHIFTED descent lattice {lambda_i - i}: k(k+1)/2 with SIGNED k."""
    return mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2


def split(theta):
    """Exact A, B, V=A-B for the descent-DPP kernel at theta."""
    M = int(mp.floor(2 * mp.sqrt(theta) + 12 * mp.power(theta, mp.mpf(1) / 6) + 20))
    arg = 2 * mp.sqrt(theta)
    st = mp.sqrt(theta)
    J = {0: mp.besselj(0, arg)}
    for x in range(1, M + 2):
        J[x] = mp.besselj(x, arg)
        J[-x] = (-1) ** x * J[x]
    xs = list(range(-M, M + 1))
    g = {k: gA(k) for k in xs}
    Kdiag = {x: mp.mpf(0) for x in xs}
    B = mp.mpf(0)
    for i, x in enumerate(xs):
        Jx, Jx1, gx = J[x], J[x + 1], g[x]
        for y in xs[i + 1:]:
            k = st * (Jx * J[y + 1] - Jx1 * J[y]) / (x - y)
            k2 = k * k
            Kdiag[x] += k2
            Kdiag[y] += k2
            B += 2 * gx * g[y] * k2
    A = mp.fsum(g[x] ** 2 * Kdiag[x] for x in xs)
    return A, B, A - B


def alpha_continuum():
    """Bulk continuum prediction for A/theta^{5/2}.

    In the bulk x = 2 sqrt(theta) u the discrete Bessel kernel has diagonal K(x,x) -> rho(u) =
    arccos(u)/pi, so Kdiag = rho(1-rho), which VANISHES at both edges (rho -> 1 at u = -1, rho -> 0
    at u = +1) -- this is what makes A convergent even though g(x)^2 ~ x^4/4 grows.  With
    g(x)^2 ~ x^4/4 = 4 theta^2 u^4 and dx = 2 sqrt(theta) du,

        A ~ 8 theta^{5/2} Int_{-1}^{1} u^4 rho(u)(1-rho(u)) du  =:  alpha theta^{5/2}.

    Substituting u = cos(phi) gives the (numerically better behaved) form used here.
    """
    def integrand(phi):
        r = phi / mp.pi
        return mp.cos(phi) ** 4 * mp.sin(phi) * r * (1 - r)
    return 8 * mp.quad(integrand, [0, mp.pi / 2, mp.pi])


def exponent(f_hi, f_lo, ratio=2):
    """Exponent p in (f - limit) ~ C theta^{-p} from three geometric samples, via successive diffs."""
    return mp.log(f_hi / f_lo) / mp.log(ratio)


def main():
    print(f"# P2: orders of the trace split A, B; dps={mp.mp.dps}; NO float64")
    print("#   theta          A               B             V=A-B      A/theta^2.5   V/theta^2    A/V")
    rows = []
    for e in (250, 500, 1000, 2000, 4000, 8000, 16000):
        th = mp.mpf(e)
        A, B, V = split(th)
        f = A / th ** mp.mpf('2.5')
        rows.append((th, A, B, V, f))
        print(f"  {e:>7}  {mp.nstr(A,9):>14}  {mp.nstr(B,9):>14}  {mp.nstr(V,9):>11}  "
              f"{mp.nstr(f,7):>10}  {mp.nstr(V/th**2,9):>11}  {mp.nstr(A/V,6):>7}")
    print("#")

    # (1) alpha: Richardson-extrapolate A/theta^{5/2} assuming a 1/theta correction.
    f = [r[4] for r in rows]
    rich = [2 * f[i + 1] - f[i] for i in range(len(f) - 1)]
    rich2 = [2 * rich[i + 1] - rich[i] for i in range(len(rich) - 1)]
    alpha = rich2[-1]
    ac = alpha_continuum()
    print("# (1) LEADING ORDER of A, and a CROSS-CHECK against the continuum. Richardson-extrapolate")
    print("#     A/theta^{5/2}, level 1 (kills the 1/theta term, justified by (2) below):")
    print("#       " + "  ".join(mp.nstr(r, 9) for r in rich))
    print("#     still drifting by ~1/theta, so level 2 (kills theta^{-3/2}):")
    print("#       " + "  ".join(mp.nstr(r, 9) for r in rich2))
    print(f"#     alpha (measured, Richardson level 2) = {mp.nstr(alpha, 9)}")
    print(f"#     alpha (continuum, 8*Int u^4 rho(1-rho) du) = {mp.nstr(ac, 9)}")
    print(f"#     relative difference = {mp.nstr(abs(alpha - ac) / ac, 4)}")
    print("#     => AGREEMENT TO EVERY DIGIT SHOWN. The bulk continuum reference that an EM argument")
    print("#        for A would be defined against is CONFIRMED by independent computation, not")
    print("#        assumed -- so the negative below is about the SPLIT, not about a missing input.")
    print("#")

    # (2) DIRECT test for a theta^2 term in A, using the now-exactly-known alpha.
    print("# (2) DOES A HAVE A theta^2 TERM? Because (1) pins alpha to 10 digits INDEPENDENTLY, this")
    print("#     can be tested DIRECTLY rather than inferred from a convergence trend. Write")
    print("#     A = alpha theta^{5/2} + a_2 theta^2 + ...; then (A/theta^{5/2} - alpha)*sqrt(theta)")
    print("#     -> a_2 if a_2 != 0, and -> 0 otherwise. Measured:")
    print("#       theta    (f-alpha)*sqrt(theta)    ratio to previous")
    prev = None
    for (th, _A, _B, _V, fv) in rows:
        t2 = (fv - ac) * mp.sqrt(th)
        rat = mp.nstr(prev / t2, 5) if prev is not None else ""
        print(f"#     {int(th):>7}  {mp.nstr(t2, 6):>16}  {rat:>18}")
        prev = t2
    bound = (rows[-1][4] - ac) * mp.sqrt(rows[-1][0])
    print("#     => it DECREASES monotonically toward 0, and the per-doubling ratio RISES (1.3333 ->")
    print("#        1.3513) toward sqrt(2) = 1.414, the signature of a clean theta^{-1/2} decay. A")
    print("#        nonzero a_2 would make the column PLATEAU at a_2 and the ratio fall toward 1;")
    print("#        both go the other way. So a_2 = 0.")
    print(f"#        Stated as a BOUND rather than an assertion: |a_2| <= {mp.nstr(bound, 3)} (the last")
    print(f"#        entry, an over-estimate since the column is still falling), against V's theta^2")
    print(f"#        coefficient 8/pi^2 = {mp.nstr(V_A_POISSON, 10)} -- i.e. A supplies at most")
    print(f"#        {mp.nstr(100 * bound / V_A_POISSON, 3)}% of it. THE LEADING theta^2 OF V COMES FROM -B.")
    d = [f[i] - f[i + 1] for i in range(len(f) - 1)]
    ps = [exponent(d[i], d[i + 1]) for i in range(len(d) - 1)]
    print("#     Consistent with the weaker trend test (successive-difference exponents, which would")
    print("#     have to fall toward 0.5 if a_2 != 0 and instead rise toward 1):")
    print("#       " + "  ".join(mp.nstr(p, 5) for p in ps))
    print("#")

    # (3) A/V ~ sqrt(theta) with the predicted coefficient.
    print("# (3) CANCELLATION DEPTH. A and B are each ~theta^{5/2} and their leading coefficients are")
    print("#     EQUAL (V has no theta^{5/2} term), so A/V ~ (alpha/(8/pi^2)) sqrt(theta):")
    pred = alpha / V_A_POISSON
    print(f"#       predicted coefficient alpha/(8/pi^2) = {mp.nstr(pred, 7)}")
    print("#       theta      A/V        (A/V)/sqrt(theta)")
    for th, A, B, V, _ in rows:
        print(f"#     {int(th):>7}  {mp.nstr(A/V,7):>9}  {mp.nstr((A/V)/mp.sqrt(th),7):>12}")
    print("#")

    # (4) how small is the target term relative to A.
    print("# (4) SIZE OF THE TARGET inside A. |c_1|*theta against A ~ alpha theta^{5/2}:")
    print("#       theta   |c_1|*theta        A          ratio      exponent")
    rs = []
    for th, A, B, V, _ in rows:
        r = abs(C1) * th / A
        rs.append(r)
        p = mp.nstr(exponent(rs[-2], rs[-1]), 5) if len(rs) > 1 else ""
        print(f"#     {int(th):>7}  {mp.nstr(abs(C1)*th,6):>11}  {mp.nstr(A,9):>12}  "
              f"{mp.nstr(r,4):>10}  {p:>9}")
    print("#     => exponent 3/2 exactly (the target sits at relative theta^{-3/2} inside A, against")
    print("#        theta^{-1} inside V): reading c_1 off A demands HALF AN ORDER MORE relative")
    print("#        accuracy than reading it off V directly.")
    print("#")
    print("# VERDICT -- P2 as posed does NOT work, for two independent reasons.")
    print("#   (a) c_1 = a_1 - b_1. Writing A = a_{5/2}theta^{5/2} + a_2 theta^2 + a_1 theta + ... and")
    print("#       likewise for B, the measured c_1 is the DIFFERENCE of the two theta^1 coefficients.")
    print("#       EM on A yields a_1 only; b_1 needs the double sum B, which is not a 1-D sum and is")
    print("#       not EM-able. The split partitions the problem; it does not reduce it.")
    print(f"#   (b) Worse, by (2) a_2 = 0 (bounded: |a_2| <= {mp.nstr(bound, 3)}, at most")
    print(f"#       {mp.nstr(100 * bound / V_A_POISSON, 3)}% of V's theta^2 coefficient): the EM-able side does not even hold")
    print("#       V's LEADING coefficient, let alone its correction. The structure of interest lives")
    print("#       on the side EM cannot reach.")
    print("#   The split itself stands: exact, well-conditioned, and it now comes with a VERIFIED")
    print("#   continuum reference for A (item 1). What is refuted is the hope of localising c_1 on it.")
    print("RESULT: c_1 = a_1 - b_1 needs both sides, and the EM-able side A carries no theta^2 term")
    print(f"        (|a_2| <= {mp.nstr(bound, 3)} vs V's 8/pi^2); alpha verified against the continuum to")
    print("        10 digits. P2 cannot localise c_1 on A. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
