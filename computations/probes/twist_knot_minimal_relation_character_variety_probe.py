#!/usr/bin/env python3
"""twist_knot_minimal_relation_character_variety_probe.py — bean qou-t579.

Cross-check of Gelca–Nagasato, "Some results about the Kauffman bracket skein
module of the twist knot exterior" [gelca-nagasato], held at library/gn2/.

PRE-REGISTERED (written before running):

  Source facts used (checked against library/gn2/sections/sec-001-...md):
    S1  Theorem 4: R_m(t) = S_{m+1}(y) + (t^-6 - t^-2 x^2) S_m(y)
          + ((2 t^4 + t^-8) x^2 - t^-4) S_{m-1}(y) - t^-10 S_{m-2}(y)
          + 2 x^2 (t^{-2m-2} + t^{-2m-6}) sum_{i=0}^{m-2} t^{2i} S_i(y)
          - t^{-2m-6} x^2,
        S_n the Chebyshev polynomials of the second kind, S_0=1, S_1=y,
        S_{n+1} = y S_n - S_{n-1}, extended to all integers (S_{-1}=0,
        S_{-2}=-1).
    S2  §3 printed factorizations of R_m(-1) for m = 0..5.
    S3  Lemma 7: R_m(-1) = (y+2) * Rt_m,  Rt_m = S_m(y) - S_{m-1}(y)
          + x^2 sum_{i=0}^{m-1} S_i(y).
    S4  Theorem 6 (Bullock, Przytycki–Sikora): at t=-1 a skein K maps to
        -tr[K]. K_m has crossing number m+2 (Remark 1), so K_2 = 4_1, K_3 = 5_2.

  Checks (all exact, sympy rationals; no floats anywhere):
    A  Theorem 4 at t = -1 expands to the printed list S2 for m = 0..5.
                                                          PASS iff all equal.
    B  Lemma 7 holds for m = 0..8.                        PASS iff all equal.
    C  Independent: Riley's parabolic-free representation of the two-bridge
       knot b(2m+1, 2) (the m-twist knot up to mirror image, which does not
       change the character variety), a = [[M,1],[0,1/M]], b = [[M,0],[s,1/M]].
       With X = tr a = M + 1/M and Y = -tr(a b^-1) (the identification is
       fixed by the factor y+2: on abelian characters a and b are conjugate
       meridians, tr(a b^-1) = 2, Y = -2), the nonabelian component
       (the Riley polynomial in s over Q(M)) annihilates Rt_m(X, Y),
       for m = 1, 2, 3, 4.                                PASS iff the
       remainder of Rt_m(X,Y) modulo the Riley polynomial is 0 for all four.
    D  The corpus 4_1 A-polynomial quoted in
       computations/probes/qbeta_substrate_meridian_branchpoint_probe.py,
         A(l, m) = -m^4 + l (1 - m^2 - 2 m^4 - m^6 + m^8) - l^2 m^4,
       vanishes on the Riley component of b(5,2) with l the (1,1) entry of
       the longitude (which commutes with a modulo the Riley polynomial)
       and m = M.                                         PASS iff the
       remainder of A(l(s,M), M) modulo the Riley polynomial is 0.

  AMENDMENTS after the first run (criteria for A-D unchanged):
    1. The first run evaluated t**-6 at the Python int -1 and produced floats;
       t is now passed as sympy.Integer(-1).
    2. A FAILED as pre-registered: Theorem 4 as printed does not reproduce the
       paper's own S2 list. Added check A2: compose the paper's Lemma 1
       recursion with Lemma 3 (R := X_{m+1} + t^-4 X_m + t^-2 x^2) and
       compare. A2 locates the discrepancy in two coefficients of Theorem 4.
       B (Lemma 7) checks against S2, so it uses the composed relation.
    3. The first run's C and D were VACUOUS: Riley's normal form needs q odd,
       and with q = 2 the gcd of the relation entries was a constant, so every
       remainder was 0. Now q = 2m - 1 (odd; b(2m+1, 2m-1) is the mirror of
       b(2m+1, 2), the m-twist knot), a guard requires deg phi >= 1, and a
       decoy check E requires Rt_m(X, Y) + 1 to be NONZERO mod phi.
    4. With q odd, D's first longitude guess (w~ w a^{-2 sigma}, w~ the
       reversed word with a and b swapped) did not commute with a. Of the
       standard forms, w w* a^{-2 sigma} (w* the reversed word, same letters)
       is the one that commutes with a mod phi, as D requires; D also gets a
       decoy (A + M must be nonzero mod phi).

  Target note: the bean names computations/complex_volume_witness.py as the
  comparison. That script uses no SL(2,C) character-variety polynomial (it
  packages a binding energy and Q_beta). The only 4_1 character-variety
  object in computations/ is the A-polynomial in check D, so D is the
  corpus comparison. Recorded as a finding, not a check.

Run: python3 -u computations/probes/twist_knot_minimal_relation_character_variety_probe.py
"""
from __future__ import annotations

import sys

import sympy as sp

x, y, t, M, s, l = sp.symbols("x y t M s l")


def S(n, v):
    """Chebyshev polynomial of the second kind, extended to negative n."""
    if n == 0:
        return sp.Integer(1)
    if n == 1:
        return v
    if n == -1:
        return sp.Integer(0)
    if n < -1:
        return -S(-n - 2, v)
    a, b = sp.Integer(1), v
    for _ in range(n - 1):
        a, b = b, sp.expand(v * b - a)
    return b


def R(m, tt):
    sm = sum((tt ** (2 * i) * S(i, y) for i in range(0, m - 1)), sp.Integer(0))
    return (S(m + 1, y) + (tt ** -6 - tt ** -2 * x ** 2) * S(m, y)
            + ((2 * tt ** 4 + tt ** -8) * x ** 2 - tt ** -4) * S(m - 1, y)
            - tt ** -10 * S(m - 2, y)
            + 2 * x ** 2 * (tt ** (-2 * m - 2) + tt ** (-2 * m - 6)) * sm
            - tt ** (-2 * m - 6) * x ** 2)


def X_lemma1(n, tt):
    """Lemma 1: X_{i+2} = t^2 y X_{i+1} - t^4 X_i - 2 t^2 x^2."""
    a, b = -tt ** 2 - tt ** -2, -tt ** 2 * x ** 2 - tt ** 4 * y
    if n == 0:
        return a
    for _ in range(n - 1):
        a, b = b, sp.expand(tt ** 2 * y * b - tt ** 4 * a - 2 * tt ** 2 * x ** 2)
    return b


def R_lemmas(m, tt):
    """Lemma 3 handle slide applied to the Lemma 1 skeins."""
    return sp.expand(X_lemma1(m + 1, tt) + tt ** -4 * X_lemma1(m, tt)
                     + tt ** -2 * x ** 2)


def R_corrected(m, tt):
    """Theorem 4 with the two coefficients A2 finds: +t^-2 x^2 on S_m and
    2 t^-4 (not 2 t^4) on S_{m-1}."""
    sm = sum((tt ** (2 * i) * S(i, y) for i in range(0, m - 1)), sp.Integer(0))
    return (S(m + 1, y) + (tt ** -6 + tt ** -2 * x ** 2) * S(m, y)
            + ((2 * tt ** -4 + tt ** -8) * x ** 2 - tt ** -4) * S(m - 1, y)
            - tt ** -10 * S(m - 2, y)
            + 2 * x ** 2 * (tt ** (-2 * m - 2) + tt ** (-2 * m - 6)) * sm
            - tt ** (-2 * m - 6) * x ** 2)


def Rt(m):
    return S(m, y) - S(m - 1, y) + x ** 2 * sum((S(i, y) for i in range(m)),
                                                sp.Integer(0))


PRINTED = {
    0: (y + 2),
    1: (y + 2) * (y + x ** 2 - 1),
    2: (y + 2) * (y ** 2 + x ** 2 * y - y + x ** 2 - 1),
    3: (y + 2) * (y ** 3 + x ** 2 * y ** 2 - y ** 2 - 2 * y + x ** 2 * y + 1),
    4: (y + 2) * (y ** 4 + x ** 2 * y ** 3 - y ** 3 - 3 * y ** 2
                  + x ** 2 * y ** 2 - x ** 2 * y + 2 * y + 1),
    5: (y + 2) * (y ** 5 + x ** 2 * y ** 4 - y ** 4 - 4 * y ** 3
                  + x ** 2 * y ** 3 - 2 * x ** 2 * y ** 2 + 3 * y ** 2
                  + 3 * y - x ** 2 * y + x ** 2 - 1),
}

A_ = sp.Matrix([[M, 1], [0, 1 / M]])
B_ = sp.Matrix([[M, 0], [s, 1 / M]])


def word(p, q):
    """Riley word w = b^e1 a^e2 b^e3 ... a^e_{p-1}, e_i = (-1)^floor(iq/p)."""
    eps = [(-1) ** ((i * q) // p) for i in range(1, p)]
    letters = [("b" if i % 2 == 0 else "a", e) for i, e in enumerate(eps)]
    return letters, eps


def mat(letters):
    W = sp.eye(2)
    for g, e in letters:
        G = A_ if g == "a" else B_
        W = W * (G if e == 1 else G.inv())
    return W.applyfunc(sp.simplify)


DOM = sp.QQ.frac_field(M)


def riley_poly(p, q):
    letters, _ = word(p, q)
    W = mat(letters)
    rel = (A_ * W - W * B_).applyfunc(sp.cancel)
    g = None
    for e in rel:
        if e == 0:
            continue
        P = sp.Poly(sp.numer(sp.together(e)), s, domain=DOM)
        g = P if g is None else sp.gcd(g, P)
    # drop the reducible locus s = 0
    while g.eval(0) == 0:
        g = sp.Poly(sp.quo(g, sp.Poly(s, s, domain=DOM)), s, domain=DOM)
    return g.monic(), letters


def reduce_mod(expr, phi):
    num, den = sp.fraction(sp.together(sp.expand(expr)))
    rnum = sp.Poly(num, s, domain=DOM).rem(phi)
    return rnum.is_zero, sp.Poly(den, s, domain=DOM).rem(phi).is_zero


def main() -> int:
    ok = True
    m1 = sp.Integer(-1)
    # A (pre-registered; expected to fail, see amendment 2)
    a_ok = all(sp.expand(R(m, m1) - PRINTED[m]) == 0 for m in range(6))
    print(f"A  Theorem 4 as printed, at t=-1, equals the printed list m=0..5: {a_ok}")
    for m in range(6):
        d = sp.factor(sp.expand(R(m, m1) - PRINTED[m]))
        print(f"     m={m}: Theorem4(-1) - printed = {d}")
    # A2
    a2_lists = all(sp.expand(R_lemmas(m, m1) + PRINTED[m]) == 0 for m in range(6))
    a2_corr = all(sp.expand(R_lemmas(m, t) - sp.Poly(R_lemmas(m, t), y).LC()
                            * R_corrected(m, t)) == 0 for m in range(2, 9))
    print(f"A2 Lemma1+Lemma3 at t=-1 equals -(printed list) m=0..5: {a2_lists}")
    print(f"A2 Lemma1+Lemma3 equals corrected Theorem 4 up to a unit, generic t, m=2..8: {a2_corr}")
    ok &= a2_lists and a2_corr
    # B
    b_ok = all(sp.expand(-R_lemmas(m, m1) - (y + 2) * Rt(m)) == 0 for m in range(9))
    print(f"B  Lemma 7 on the composed relation, m=0..8: {b_ok}")
    ok &= b_ok
    # C, E
    c_ok = True
    phi5 = lets5 = None
    for m in (1, 2, 3, 4):
        p, q = 2 * m + 1, 2 * m - 1
        phi, letters = riley_poly(p, q)
        X = M + 1 / M
        Y = -(A_ * B_.inv()).trace()
        expr = Rt(m).subs({x: X, y: Y})
        z, dz = reduce_mod(expr, phi)
        decoy, _ = reduce_mod(expr + 1, phi)
        good = phi.degree() >= 1 and z and not dz and not decoy
        print(f"C  b({p},{q}): Riley degree {phi.degree()} (expected {m}),"
              f" Rt_{m}(X,Y) = 0 mod phi: {z}; E decoy nonzero: {not decoy}")
        c_ok &= good and phi.degree() == m
        if m == 2:
            phi5, lets5 = phi, letters
    ok &= c_ok
    # D: longitude w w* a^{-2 sigma}, w* = w read backwards (amendment 4)
    rev = list(reversed(lets5))
    sigma = sum(e for _, e in lets5)
    Lm = (mat(lets5) * mat(rev) * (A_ ** (-2 * sigma))).applyfunc(sp.cancel)
    comm = (Lm * A_ - A_ * Lm).applyfunc(sp.cancel)
    comm_ok = all(reduce_mod(e, phi5)[0] for e in comm)
    low_ok = reduce_mod(Lm[1, 0], phi5)[0]
    lam = Lm[0, 0]
    Apoly = -M ** 4 + l * (1 - M ** 2 - 2 * M ** 4 - M ** 6 + M ** 8) - l ** 2 * M ** 4
    d_ok, _ = reduce_mod(Apoly.subs(l, lam), phi5)
    d_decoy, _ = reduce_mod(Apoly.subs(l, lam) + M, phi5)
    print(f"D  longitude commutes with a mod phi: {comm_ok}; lower-left 0: {low_ok};"
          f" corpus A_4_1(l, M) = 0 mod phi: {d_ok}; decoy nonzero: {not d_decoy}")
    ok &= comm_ok and low_ok and d_ok and not d_decoy
    print("ALL PASS (A fails as a finding about the source)" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
