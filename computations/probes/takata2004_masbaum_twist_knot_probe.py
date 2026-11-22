#!/usr/bin/env python3
"""takata2004_masbaum_twist_knot_probe.py — bean qou-7q3s.

Cross-check of Takata, "The colored Jones polynomial and the A-polynomial for
twist knots", arXiv:math/0401068 [takata2004], held at
library/arxiv-math-0401068v1/, against the corpus twist-knot towers in
computations/aj_masbaum_crosscheck.py and the corpus 4_1 A-polynomial.

PRE-REGISTERED (written before running):

  Source facts used (PDF text layer):
    S1  (1)-(2) Masbaum: J_{K_p}(n) = sum_k C(k) {n-k}...{n+k}/{n},
        C(k) = (-1)^{k+1} s^{k(k+3)/2} sum_{l<=k} (-1)^l q^{l(l+1)p} {2l+1}
               {k}! / ({k+l+1}! {k-l}!),  {n} = s^n - s^-n, s^2 = q.
        K_1 = left trefoil, K_-1 = 4_1 (the corpus script's reading of
        Masbaum's Fig. 3), K_2 = 5_2, K_-2 = 6_1 (Takata §4).
    S2  the rearranged form J = sum_k sum_{l<=k} F(n,k,l),
        F = (-1)^{k+1} q^{k(k+3)/2} q^{nk} (q^-1)_{n+k}(q^-1)_{n-1}
            / ((q^-1)_n (q^-1)_{n-k-1})
            * (-1)^l q^{l(l+1)p + l(l-1)/2} (q^{2l+1} - 1) (q)_k
            / ((q)_{k+l+1} (q)_{k-l}),   (x)_n = (1-x)(1-x^2)...(1-x^n).
    S3  (3)-(5): f0 = F(n+1,k,l)/F = q^k (1-q^{-n-k-1})(1-q^-n)/((1-q^{-n-1})(1-q^{-n+k})),
        f1 = F(n,k+1,l)/F = -q^{k+n+2}(1-q^{-n-k-1})(1-q^{-n+k+1})(1-q^k)
             /((1-q^{k+l+2})(1-q^{k-l+1})),
        f2 = F(n,k,l+1)/F = -q^{(2p+1)l+2p} (q^{2(l+1)+1}-1)(1-q^{k-l})
             /((q^{2l+1}-1)(1-q^{k+l+2})).
    S4  Hoste–Shanahan initial values: A_{K_1} = l + m^6,
        A_{K_-1} = -l + l m^2 + m^4 + 2 l m^4 + l^2 m^4 + l m^6 - l m^8,
        A_{K_2} = -l^2 + l^3 + 2l^2m^2 + lm^4 + 2l^2m^4 - lm^6 - l^2m^8
                  + 2lm^10 + l^2m^10 + 2lm^12 + m^14 - lm^14.
        Theorem 2.2: x = (l m^2 + 1)/(m^2 + l), (7): y^2 + 1 =
        (y/m^2)(m^4 - x m^4 + x^2 m^2 + m^2 + 1 - x), and f2(1, m^2, x, y) = 1,
        i.e. -y^{2p+1}(1 - x/y) = 1 - x y, eliminate y.
    S5  (16): the Kashaev evaluation is the rearranged form with q^n = 1.

  Checks (sympy exact for A-D; mpmath 60 dps for E):
    A  (1)-(2) equals the rearranged sum for p in {1,-1,2,-2}, n = 1..5.
    B  (3)-(5) equal the F ratios at (n,k,l) in {(4,2,1),(5,3,2),(6,2,0)},
       p in {2,-1}.
    C  K_-1 equals the corpus 4_1 Habiro tower (corpus_fig8, transcribed here
       and checked numerically against the corpus function), n = 1..6; K_1
       equals the corpus trefoil tower (corpus_trefoil) under q or 1/q,
       n = 1..5; K_2 at n = 2, 3 equals Takata 2008 (15) with p1 = 2 (5_2)
       under q or 1/q; K_-2 at n = 2 equals the bracket Jones polynomial of
       6_1 under t = q or 1/q.
    D  printed A_{K_-1} = -(corpus A_4_1 of
       qbeta_substrate_meridian_branchpoint_probe.py); and for p in {1,-1,2}
       the Theorem 2.2 elimination (resultant in y, numerator in l, m) has
       the printed A_{K_p} as a factor.
    E  (16) with p = -1, inner l-sum simplified symbolically first, at
       q = exp(2 pi i/N), equals the corpus 4_1 tower at the same q for
       N = 5..9 (rel < 1e-40). And with the corpus tower, the SnapPy volume
       of 4_1 equals 2 Cl_2(pi/3) to 1e-50, and
       |J_N| / (N^{3/2} e^{N Vol/(2 pi)}) Neville-extrapolated (N = 80..160
       step 10, last 6 points) equals 3^{-1/4} to 1e-8 relative.
    PASS iff A-E all hold. Vol is an input to E only; nothing is fitted
    and no anchor value is adopted from this probe.

  AMENDMENTS after the first run (thresholds unchanged; C, D, E passed):
    1. A and B FAILED as pre-registered, and the page images were read to
       rule out text-layer errors. (2) as printed gives J(1) = -1 (the k = 0
       term is -1); it carries an extra (-1)^{k+1} relative to Masbaum's own
       coefficients (f_{K_-1,k} = 1, f_{K_1,k} = (-1)^k a^{k(k+3)}, quoted in
       computations/aj_masbaum_crosscheck.py). Check A2: (2) without that sign
       equals the rearranged form. In (4) the factor (1 - q^k) should be
       (1 - q^{k+1}), since F carries (q)_k; check B2. Neither slip reaches
       Theorem 2.2: at q = 1 both factors become (1 - x).
    2. The first run's masbaum() used s^{k(k+3)}, not the printed
       s^{k(k+3)/2}; fixed before the A2 run.

Run: python3 -u computations/probes/takata2004_masbaum_twist_knot_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

s, q, l, m, x, y, w = sp.symbols("s q l m x y w")


def br(k):
    return s ** k - s ** (-k)


def brf(k):
    r = sp.Integer(1)
    for i in range(1, k + 1):
        r *= br(i)
    return r


def masbaum(p, n, printed_sign=True):
    """(1)-(2). The first run had s^{k(k+3)} here, a transcription slip;
    the printed exponent is k(k+3)/2. printed_sign=False drops (-1)^{k+1}."""
    tot = sp.Integer(0)
    for k in range(n):
        sg = (-1) ** (k + 1) if printed_sign else 1
        C = sg * s ** sp.Rational(k * (k + 3), 2) * sum(
            (-1) ** j * s ** (2 * j * (j + 1) * p) * br(2 * j + 1) * brf(k)
            / (brf(k + j + 1) * brf(k - j)) for j in range(k + 1))
        prod = sp.Integer(1)
        for i in range(n - k, n + k + 1):
            prod *= br(i)
        tot += C * prod / br(n)
    return sp.simplify(sp.factor(tot).subs(s, sp.sqrt(q)))


def poch(xx, n):
    r = sp.Integer(1)
    for i in range(1, n + 1):
        r *= 1 - xx ** i
    return r


def F(p, n, k, j, qq=q):
    return ((-1) ** (k + 1) * qq ** sp.Rational(k * (k + 3), 2) * qq ** (n * k)
            * poch(1 / qq, n + k) * poch(1 / qq, n - 1)
            / (poch(1 / qq, n) * poch(1 / qq, n - k - 1))
            * (-1) ** j * qq ** (j * (j + 1) * p + sp.Rational(j * (j - 1), 2))
            * (qq ** (2 * j + 1) - 1) * poch(qq, k) / (poch(qq, k + j + 1) * poch(qq, k - j)))


def rearranged(p, n):
    return sp.simplify(sum(F(p, n, k, j) for k in range(n) for j in range(k + 1)))


def corpus_fig8_sym(N):
    tot = sp.Integer(0)
    for k in range(N):
        p1 = sp.Mul(*[1 - q ** (-(N + 1 + j)) for j in range(k)])
        p2 = sp.Mul(*[1 - q ** (j + 1) * q ** (-N) for j in range(k)])
        tot += q ** (N * k) * p1 * p2
    return sp.expand(tot)


def corpus_trefoil_sym(N):
    def qint(v, k):
        return (v ** k - v ** (-k)) / (v - 1 / v)
    n = N - 1
    num = sum(((-1) ** ((n - j) % 2) * w ** (2 * j * (j + 1) - n * (n + 2))) ** 3
              * qint(w ** 2, 2 * j + 1) for j in range(n + 1))
    return sp.simplify((w ** (-3 * n * (n + 2)) * num / qint(w ** 2, N)).subs(w, q ** sp.Rational(1, 4)))


def eq_up_to_mirror(a, b):
    return sp.simplify(a - b) == 0 or sp.simplify(a.subs(q, 1 / q) - b) == 0


def main() -> int:
    ok = True
    # A
    a_ok = all(sp.simplify(masbaum(p, n) - rearranged(p, n)) == 0
               for p in (1, -1, 2, -2) for n in range(1, 6))
    print(f"A  Masbaum (1)-(2) as printed = rearranged form, p in {{1,-1,2,-2}}, n=1..5: {a_ok}"
          f" (expected False, amendment 1)", flush=True)
    print(f"   (1)-(2) as printed at n=1, p=-1: {masbaum(-1, 1)} (a knot invariant normalised to 1)")
    a2 = all(sp.simplify(masbaum(p, n, printed_sign=False) - rearranged(p, n)) == 0
             for p in (1, -1, 2, -2) for n in range(1, 6))
    print(f"A2 (1)-(2) without (-1)^(k+1) = rearranged form, same range: {a2}", flush=True)
    ok &= a2
    # B
    b_ok = True
    b2_ok = True
    for p in (2, -1):
        for (n, k, j) in ((4, 2, 1), (5, 3, 2), (6, 2, 0)):
            f0 = q ** k * (1 - q ** (-n - k - 1)) * (1 - q ** -n) / ((1 - q ** (-n - 1)) * (1 - q ** (-n + k)))
            f1 = -q ** (k + n + 2) * (1 - q ** (-n - k - 1)) * (1 - q ** (-n + k + 1)) * (1 - q ** k) \
                / ((1 - q ** (k + j + 2)) * (1 - q ** (k - j + 1)))
            f2 = -q ** ((2 * p + 1) * j + 2 * p) * (q ** (2 * (j + 1) + 1) - 1) * (1 - q ** (k - j)) \
                / ((q ** (2 * j + 1) - 1) * (1 - q ** (k + j + 2)))
            base = F(p, n, k, j)
            b_ok &= sp.simplify(F(p, n + 1, k, j) / base - f0) == 0
            b_ok &= sp.simplify(F(p, n, k + 1, j) / base - f1) == 0
            f1c = f1 * (1 - q ** (k + 1)) / (1 - q ** k)
            b2_ok &= sp.simplify(F(p, n, k + 1, j) / base - f1c) == 0
            b_ok &= sp.simplify(F(p, n, k, j + 1) / base - f2) == 0
    print(f"B  ratios (3)-(5) as printed: {b_ok} (expected False, amendment 1)", flush=True)
    print(f"B2 ratios with (1 - q^(k+1)) in place of (1 - q^k) in (4): {b2_ok}", flush=True)
    ok &= b2_ok
    # C
    import aj_masbaum_crosscheck as AJ
    mp.mp.dps = 60
    tr_ok = all(abs(AJ.corpus_fig8(mp.mpf(2), N)
                    - mp.mpf(sp.N(corpus_fig8_sym(N).subs(q, 2), 70))) < mp.mpf("1e-40")
                for N in range(1, 7))
    tr_ok &= all(abs(AJ.corpus_trefoil(mp.mpf(2) ** (mp.mpf(1) / 4), N)
                     - mp.mpf(sp.N(corpus_trefoil_sym(N).subs(q, 2), 70))) < mp.mpf("1e-40")
                 for N in range(1, 6))
    c41 = all(sp.simplify(rearranged(-1, n) - corpus_fig8_sym(n)) == 0 for n in range(1, 7))
    c31 = all(eq_up_to_mirror(rearranged(1, n), corpus_trefoil_sym(n)) for n in range(1, 6))
    from takata_twist_knot_colored_jones_probe import takata15, jones_bracket, t as tt
    c52 = all(eq_up_to_mirror(rearranged(2, n), takata15(2, n).subs(sp.Symbol("q"), q))
              for n in (2, 3))
    V61 = jones_bracket("6_1").subs(tt, q)
    c61 = eq_up_to_mirror(rearranged(-2, 2), V61)
    print(f"C  transcription of corpus towers matches corpus functions: {tr_ok}")
    print(f"C  K_-1 = corpus 4_1 tower n=1..6: {c41}; K_1 = corpus trefoil n=1..5: {c31};"
          f" K_2 = Takata2008 S(7,3) n=2,3: {c52}; K_-2(2) = Jones(6_1): {c61}", flush=True)
    ok &= tr_ok and c41 and c31 and c52 and c61
    # D
    A41_corpus = -m ** 4 + l * (1 - m ** 2 - 2 * m ** 4 - m ** 6 + m ** 8) - l ** 2 * m ** 4
    AK = {1: l + m ** 6,
          -1: -l + l * m ** 2 + m ** 4 + 2 * l * m ** 4 + l ** 2 * m ** 4 + l * m ** 6 - l * m ** 8,
          2: (-l ** 2 + l ** 3 + 2 * l ** 2 * m ** 2 + l * m ** 4 + 2 * l ** 2 * m ** 4 - l * m ** 6
              - l ** 2 * m ** 8 + 2 * l * m ** 10 + l ** 2 * m ** 10 + 2 * l * m ** 12 + m ** 14
              - l * m ** 14)}
    d1 = sp.expand(AK[-1] + A41_corpus) == 0
    d_ok = d1
    X = (l * m ** 2 + 1) / (m ** 2 + l)
    for p in (1, -1, 2):
        e7 = sp.numer(sp.together(m ** 2 * (y ** 2 + 1) - y * (m ** 4 - X * m ** 4 + X ** 2 * m ** 2 + m ** 2 + 1 - X)))
        e8 = sp.numer(sp.together(-y ** (2 * p + 1) * (1 - X / y) - (1 - X * y)))
        res = sp.factor(sp.resultant(sp.Poly(e7, y), sp.Poly(e8, y)))
        has = sp.rem(sp.Poly(sp.numer(sp.together(res)), l, m), sp.Poly(AK[p], l, m)).is_zero \
            or any(sp.expand(fct - AK[p]) == 0 or sp.expand(fct + AK[p]) == 0
                   for fct, _ in sp.factor_list(sp.numer(sp.together(res)))[1])
        print(f"D  p={p}: printed A_K_p is a factor of the Theorem 2.2 elimination: {has}")
        d_ok &= has
    print(f"D  printed A_K_-1 = -(corpus A_4_1): {d1}", flush=True)
    ok &= d_ok
    # E
    mp.mp.dps = 60
    e_ok = True
    for N in range(5, 10):
        z = mp.expjpi(mp.mpf(2) / N)
        tot = mp.mpc(0)
        for k in range(N):
            inner = sp.cancel(sp.together(sum(
                (-1) ** (k + j) * q ** sp.Rational(k * (k + 3), 2) * poch(q, k) * poch(1 / q, k)
                * q ** (j * (j + 1) * (-1) + sp.Rational(j * (j - 1), 2))
                * poch(q, 2 * j + 1) / poch(q, 2 * j) * poch(q, k) / (poch(q, k + j + 1) * poch(q, k - j))
                for j in range(k + 1))))
            tot += sp.lambdify(q, inner, "mpmath")(z)
        ref = sp.lambdify(q, corpus_fig8_sym(N), "mpmath")(z)
        rel = abs(tot - ref) / abs(ref)
        e_ok &= rel < mp.mpf("1e-40")
        print(f"E  N={N}: (16) vs corpus 4_1 tower rel {mp.nstr(rel, 3)}")
    import snappy
    vol = mp.mpf(str(snappy.Manifold("4_1").high_precision().volume()))
    cl = 2 * mp.clsin(2, mp.pi / 3)
    vol_ok = abs(vol - cl) < mp.mpf("1e-50")
    print(f"E  SnapPy Vol(4_1) = {mp.nstr(vol, 25)}; 2 Cl_2(pi/3) = {mp.nstr(cl, 25)}: {vol_ok}")
    Ns = list(range(80, 161, 10))
    vals = []
    for N in Ns:
        z = mp.expjpi(mp.mpf(2) / N)
        J = mp.mpc(0)
        P = mp.mpc(1)
        for k in range(N):
            if k:
                P *= (1 - z ** (-(N + k))) * (1 - z ** k * z ** (-N))
            J += z ** (N * k) * P
        vals.append(abs(J) / (mp.mpf(N) ** (mp.mpf(3) / 2) * mp.e ** (N * vol / (2 * mp.pi))))
    xs = [1 / mp.mpf(N) for N in Ns[-6:]]
    pp = list(vals[-6:])
    for kk in range(1, 6):
        for i in range(6 - kk):
            pp[i] = (xs[i] * pp[i + 1] - xs[i + kk] * pp[i]) / (xs[i] - xs[i + kk])
    target = mp.mpf(3) ** (-mp.mpf(1) / 4)
    relv = abs(pp[0] / target - 1)
    print(f"E  extrapolated {mp.nstr(pp[0], 15)} vs 3^(-1/4) = {mp.nstr(target, 15)}, rel {mp.nstr(relv, 3)}")
    e_ok &= vol_ok and relv < mp.mpf("1e-8")
    ok &= e_ok
    print("ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
