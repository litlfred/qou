#!/usr/bin/env python3
"""takata_twist_knot_colored_jones_probe.py — bean qou-tiwv.

Cross-check of Takata, "A formula for the colored Jones polynomial of 2-bridge
knots", Kyungpook Math. J. 48 (2008) 255 [takata2008], held at
library/kmj-48-2-255/, against this corpus's 5_2 one-loop cross-check
(computations/probes/one_loop_ohtsuki_5_2_crosscheck_probe.py).

PRE-REGISTERED (written before running):

  Source facts used (PDF text layer, Corollary 5 and §3 examples):
    S1  (15) J_{S(4p1-1,2p1-1)}(n) = sum_{0<=m1<=...<=m_{p0}<=n-1}
          q^{ n(-1 + sum_{i=1}^{2p1-2} (-1)^i m_i - 2 m_{2p1-1})
              + 1 - sum_{i=1}^{p1-1} m_{2i-1}(1 + m_{2i}) }
          * (q)_{n-1} (q)_{m_{p0}} / (q)_{n-m_{p0}-1} * (-1)^{m_{p0}}
          / ( prod_{j=0}^{p1-1} (qbar)_{m_{2j+1}-m_{2j}}
              * prod_{j=1}^{p1-1} (q)_{m_{2j}-m_{2j-1}} ),
        p0 = 2p1 - 1, m0 = 0, (x)_k = (x-1)(x^2-1)...(x^k-1), qbar = 1/q.
        p1 = 1 is S(3,1) (trefoil, the paper's own example), p1 = 2 is
        S(7,3) = 5_2.
    S2  (14) with p1 = 1, the paper's figure-eight form
          J_{S(5,3)}(n) = sum_{m1<=m2} (qbar)_{n-1}(qbar)_{m2}
            / ((qbar)_{n-m2-1}(qbar)_{m1}(q)_{m2-m1}) q^{n m1} (-1)^{m2},
        and the Habiro/Le form it reduces to,
          sum_{0<=m<=n-1} (q)_{n-1}(q)_{n+m} / ((q)_n (q)_m (q)_{n-m-1}) q^{-n m}.
    S3  J_K(2) is the Jones polynomial, J(unknot) = 1.
    S4  Kashaev invariant <K>_N = J_K(N) at q = exp(2 pi i/N). Ohtsuki
        (library/ki52, Thm 1.1): <5_2>_N = e^{N zeta} N^{3/2} omega
        (1 + sum kappa_i (2 pi i/N)^i), |e^{N zeta}| = e^{N Vol/(2 pi)};
        the corpus probe quotes |omega| = 0.65620337047140662 (Ohtsuki's
        printed digits) and the closed form |omega| = (2 |tau_DG(5_2)|)^{-1/2}.

  Checks (exact sympy for A, B; mpmath at 60 dps for C):
    A  (15) at n = 2 for p1 = 1, 2 and (14) at n = 2 equal the Jones
       polynomial of 3_1, 5_2, 4_1 computed here independently by a Kauffman
       bracket state sum on SnapPy's PD code, under q = t or q = 1/t (Schubert
       notation does not fix the chirality).          PASS iff all three.
    B  (14) and the Habiro/Le form agree for n = 1..7, and (15) at n = 1 is 1.
                                                      PASS iff all equal.
    C  f(N) = |<5_2>_N| / (N^{3/2} e^{N Vol/(2 pi)}), Vol from SnapPy at high
       precision, for N = 40..100 step 4, Richardson-extrapolated in 1/N
       (order 10). PASS iff the limit agrees with Ohtsuki's printed
       |omega| = 0.65620337047140662 to 9 significant digits. Reported also:
       the digits of agreement with the closed form (2*1.16116273813391007312872008056)^{-1/2}
       (|tau(5_2)| from one_loop_torsion_crosscheck_probe.py, check H).

  AMENDMENTS after the first run (thresholds unchanged):
    1. B FAILED as pre-registered: the Habiro/Le form printed on p. 278,
       sum (q)_{n-1}(q)_{n+m}/((q)_n (q)_m (q)_{n-m-1}) q^{-nm}, does not equal
       the paper's own (14) for n >= 2 (at n = 2 it is (q^3+q^2-1)/q^2, not the
       Jones polynomial). The page image was read to rule out a text-layer
       error: the printed formula is as transcribed. Dropping the factor
       (q)_m from the denominator makes it agree with (14) for n = 1..6
       (check B2). Source finding, not a defect of the corpus.
    2. C's least-squares fit of order 10 was unstable (it returned 0.65617,
       while Neville extrapolation of the same values was stable to ~1e-9).
       C now uses N = 64..120 step 8 and Neville polynomial extrapolation in
       1/N on the last k points, k = 4..8; the reported value is k = 6 and the
       spread over k is printed. Threshold unchanged.

Run: python3 -u computations/probes/takata_twist_knot_colored_jones_probe.py
"""
from __future__ import annotations

import itertools
import sys

import mpmath as mp
import sympy as sp

q, A_, t = sp.symbols("q A t")


def poch(x, k):
    r = sp.Integer(1)
    for i in range(1, k + 1):
        r *= x ** i - 1
    return r


def takata15(p1, n):
    p0 = 2 * p1 - 1
    tot = sp.Integer(0)
    for ms in itertools.combinations_with_replacement(range(n), p0):
        m = (0,) + ms                      # m[0] = 0, m[1..p0]
        e = n * (-1 + sum((-1) ** i * m[i] for i in range(1, 2 * p1 - 1))
                 - 2 * m[2 * p1 - 1]) + 1 \
            - sum(m[2 * i - 1] * (1 + m[2 * i]) for i in range(1, p1))
        den = sp.Integer(1)
        for j in range(0, p1):
            den *= poch(1 / q, m[2 * j + 1] - m[2 * j])
        for j in range(1, p1):
            den *= poch(q, m[2 * j] - m[2 * j - 1])
        tot += q ** e * poch(q, n - 1) * poch(q, m[p0]) / poch(q, n - m[p0] - 1) \
            * (-1) ** m[p0] / den
    return sp.factor(sp.simplify(tot))


def takata14_p1(n):
    tot = sp.Integer(0)
    for m1 in range(n):
        for m2 in range(m1, n):
            tot += poch(1 / q, n - 1) * poch(1 / q, m2) / (
                poch(1 / q, n - m2 - 1) * poch(1 / q, m1) * poch(q, m2 - m1)) \
                * q ** (n * m1) * (-1) ** m2
    return sp.simplify(tot)


def habiro_41(n, printed=True):
    """Takata 2008 p. 278 Habiro/Le form; printed=False drops (q)_m."""
    tot = sp.Integer(0)
    for m in range(n):
        den = poch(q, n) * poch(q, n - m - 1) * (poch(q, m) if printed else 1)
        tot += poch(q, n - 1) * poch(q, n + m) / den * q ** (-n * m)
    return sp.simplify(tot)


def jones_bracket(name):
    """Jones polynomial in t from a Kauffman bracket state sum (KnotTheory
    PD convention: X[i,j,k,l], A-smoothing pairs (i,j),(k,l))."""
    import spherogram as sg
    L = sg.Link(name)
    pd = L.PD_code()
    w = L.writhe()
    br = sp.Integer(0)
    d = -A_ ** 2 - A_ ** -2
    for st in itertools.product((0, 1), repeat=len(pd)):
        parent = {}

        def find(a):
            while parent.get(a, a) != a:
                a = parent[a]
            return a

        def union(a, b):
            parent[find(a)] = find(b)
        for (i, j, k, l), s in zip(pd, st):
            if s == 0:
                union(i, j); union(k, l)
            else:
                union(i, l); union(j, k)
        labels = {x for c in pd for x in c}
        loops = len({find(x) for x in labels})
        na = st.count(0)
        br += A_ ** (na - (len(pd) - na)) * d ** (loops - 1)
    V = sp.expand((-A_ ** 3) ** (-w) * br)
    return sp.expand(V.subs(A_, t ** sp.Rational(-1, 4)))


def kashaev_52(N, dps):
    mp.mp.dps = dps
    qq = mp.expjpi(mp.mpf(2) / N)
    P = [mp.mpc(1)]
    Pb = [mp.mpc(1)]
    for k in range(1, N + 1):
        P.append(P[-1] * (qq ** k - 1))
        Pb.append(Pb[-1] * (qq ** (-k) - 1))
    pw = [qq ** k for k in range(N)]
    n = N
    tot = mp.mpc(0)
    for m1 in range(n):
        for m2 in range(m1, n):
            for m3 in range(m2, n):
                e = n * (-1 - m1 + m2 - 2 * m3) + 1 - m1 * (1 + m2)
                term = pw[e % N] * P[n - 1] * P[m3] / P[n - m3 - 1] \
                    / (Pb[m1] * Pb[m3 - m2] * P[m2 - m1])
                tot += -term if m3 % 2 else term
    return tot


def neville0(xs, ys):
    """Value at x = 0 of the interpolating polynomial through (xs, ys)."""
    p = list(ys)
    n = len(xs)
    for k in range(1, n):
        for i in range(n - k):
            p[i] = (xs[i] * p[i + 1] - xs[i + k] * p[i]) / (xs[i] - xs[i + k])
    return p[0]


def main() -> int:
    ok = True
    # A
    J31, J52, J41 = takata15(1, 2), takata15(2, 2), sp.factor(takata14_p1(2))
    a_ok = True
    for name, J in (("3_1", J31), ("5_2", J52), ("4_1", J41)):
        V = jones_bracket(name)
        m1 = sp.simplify(J.subs(q, t) - V) == 0
        m2 = sp.simplify(J.subs(q, 1 / t) - V) == 0
        print(f"A  {name}: Takata J(2) = {sp.expand(J)};  bracket V = {V};"
              f" q=t {m1}, q=1/t {m2}")
        a_ok &= (m1 or m2)
    ok &= a_ok
    # B
    b_ok = all(sp.simplify(takata14_p1(n) - habiro_41(n)) == 0 for n in range(1, 8))
    print(f"B  (14) = printed Habiro/Le form, n=1..7: {b_ok} (expected False, amendment 1)")
    b2 = all(sp.simplify(takata14_p1(n) - habiro_41(n, printed=False)) == 0
             for n in range(1, 7))
    b2 &= takata15(2, 1) == 1 and takata15(1, 1) == 1
    print(f"B2 (14) = Habiro/Le form without (q)_m, n=1..6, and (15)(n=1) = 1: {b2}")
    ok &= b2
    # C
    import snappy
    vol = mp.mpf(str(snappy.Manifold("5_2").high_precision().volume()))
    mp.mp.dps = 60
    vol = mp.mpf(str(snappy.Manifold("5_2").high_precision().volume()))
    Ns = list(range(64, 121, 8))
    vals = []
    for N in Ns:
        K = kashaev_52(N, 60)
        f = abs(K) / (mp.mpf(N) ** (mp.mpf(3) / 2) * mp.e ** (N * vol / (2 * mp.pi)))
        vals.append(f)
        print(f"C  N={N}: f(N) = {mp.nstr(f, 15)}", flush=True)
    ests = {k: neville0([1 / mp.mpf(N) for N in Ns[-k:]], vals[-k:])
            for k in range(4, 9)}
    for k, e in ests.items():
        print(f"C  Neville on last {k} points: {mp.nstr(e, 20)}")
    lim = ests[6]
    ohtsuki = mp.mpf("0.65620337047140662")
    closed = (2 * mp.mpf("1.16116273813391007312872008056")) ** (-mp.mpf(1) / 2)
    rel_o = abs(lim / ohtsuki - 1)
    rel_c = abs(lim / closed - 1)
    print(f"C  extrapolated |omega| = {mp.nstr(lim, 20)}")
    print(f"   Ohtsuki printed        {mp.nstr(ohtsuki, 20)}  rel {mp.nstr(rel_o, 3)}")
    print(f"   closed form            {mp.nstr(closed, 20)}  rel {mp.nstr(rel_c, 3)}")
    c_ok = rel_o < mp.mpf("5e-9")
    ok &= c_ok
    print("ALL PASS (A, B2, C; B fails as a source finding)" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
