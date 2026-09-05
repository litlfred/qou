#!/usr/bin/env python3
"""
w1_base_qshift_rationality_prune_probe.py — bean qou-1z28 (follows qou-an6y / #6652).

QUESTION. W1 (`qou-d8de`: construct the q-difference prolongation D_q from the colour
spectral curve Sigma) names as its first route a q-shift on the BASE, z -> q^2 z, with a
q-connection lift. Formalize-first: can such a thing exist at all?

STRUCTURAL ARGUMENT (the prune; scope-(b) with a cited invariant).
  (1) The colour cubic  P(X,z) = X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1)  is
      irreducible over C(z)  — Lean: QOU.Mass.ColorCubicIrreducible.colorCubicAt_ne_zero
      (no root in K[z], any char-0 field K) and colorCubic_no_ratFunc_root (no root in
      K(z), by Gauss).
  (2) Each sheet X_i(z) is algebraic, hence D-FINITE: it satisfies a linear ODE with
      polynomial coefficients (this IS the classical prolongation, proved exact and
      therefore dead in prop:sw-classical-jet-exactness).
  (3) If a rational rank-3 q-difference system in z -> lambda z (lambda not a root of
      unity) had the three sheets as solutions, then X_1(z), X_1(lz), X_1(l^2 z),
      X_1(l^3 z) would be four vectors in the 3-dimensional C(z)-span of the sheets,
      hence X_1 would be q-HOLONOMIC (scalar linear q-difference equation with rational
      coefficients).
  (4) D-finite AND q-holonomic => RATIONAL  (Bezivin, Aequationes Math. 43 (1992)
      159-176; Ramis, Ann. Fac. Sci. Toulouse 1 (1992) 53-94; unified with the Mahler
      case in Schaefke-Singer, "Consistent systems of linear differential and difference
      equations", J. Eur. Math. Soc. 21 (2019) 2751-2792).
  (1)+(4) contradict. So NO rational base q-connection has the SW sheets as flat
  sections. The classical connection exists and is exact; the rational q-analogue does
  not exist. Whatever D_q is, it is not a q-holonomic system on the z-line.

WHAT THIS PROBE DOES (all exact — sympy over Q / Q(q); NO float64):
  1  irreducibility cross-check: no constant / affine root, degree >= 2 excluded by the
     leading term; and the two integer Bezout certificates the Lean uses (5 and 65).
  2  the D-finite side made explicit: the ODE of order <= 3 that a sheet satisfies,
     found by exact linear algebra in the Q(z)-basis {1, X, X^2} (no series).
  3  the q-holonomic side: on the sheet through X(0) = -1 (a simple root of
     P(X,0) = (X+1)(X^2+1)), an exact search for  sum_{k<=3} c_k(z) X(q^k z) = 0  with
     deg c_k <= D, at exact rational q and (by rank) over Q(q). The theorem says the
     nullspace is trivial; the search must find NONE. CORROBORATION, not proof — a
     finite search cannot exclude larger (order, degree); the theorem does.
  4  two controls on the same machinery: the differential search on the same series
     DOES find the section-2 ODE, and the q-search on the rational function 1/(1-z) DOES
     find its first-order q-equation. So a null result in section 3 is a property of the
     sheet, not of the searcher.

SCOPE. This prunes route 1 of W1 as stated — GLOBAL, RATIONAL coefficients on the base.
It says nothing about a q-difference operator with non-rational (algebraic in z, or
defined on Sigma rather than on the base) coefficients, nor about a LOCAL q-dilation
t -> qt at a ramification point (where every power series trivially satisfies a
first-order q-equation with a power-series coefficient). Those are where the level-
reading results of #6628/#6652 already live. Anti-fit: nothing is fitted; no witness.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

X, z, q = sp.symbols('X z q')
a, b = sp.symbols('a b')
P = X**3 + (z + 1)*X**2 + (z**2 + z + 1)*X + (z**3 + z**2 + z + 1)
PX = sp.diff(P, X)
Pz = sp.diff(P, z)

HR = '=' * 78


# ----------------------------------------------------------------------------
# 1  irreducibility over Q(z) (and the char-0 certificates the Lean uses)
# ----------------------------------------------------------------------------
def section1():
    print(HR)
    print('1  irreducibility of P over Q(z): no root in Q[z]')
    print(HR)
    fl = sp.factor_list(P)
    print(f'  factor_list over Q[X,z]: {len(fl[1])} irreducible factor(s)')
    c0 = sp.Poly(sp.expand(P.subs(X, b)), z).all_coeffs()
    print(f'  constant root b: system {[sp.factor(c) for c in c0]} -> solutions {sp.solve(c0, b)}')
    cs = sp.Poly(sp.expand(P.subs(X, a*z + b)), z).all_coeffs()
    print('  affine root a z + b: z-coefficients')
    for i, c in enumerate(cs):
        print(f'     z^{3-i}: {sp.factor(c)}')
    print(f'     solutions over Qbar: {sp.solve(cs, [a, b], dict=True)}')
    print(f'  degree d >= 2: 3d > max(1+2d, 2+d, 3) for all d >= 2: '
          f'{all(3*k > max(1+2*k, 2+k, 3) for k in range(2, 50))} (checked d=2..49; '
          f'symbolically 3d-(1+2d)=d-1>0, 3d-(2+d)=2d-2>0, 3d-3>0)')
    e2 = cs[1]
    e0 = cs[3]
    # branch a = -1
    h2 = sp.expand(e2 - ((3*b + 1)*a - b)*(a + 1))
    cert5 = sp.expand(8*e0 - (4*b**2 + 2*b + 3)*h2)
    # branch a^2 = -1
    h2b = sp.expand(e2 - (3*b + 1)*(a**2 + 1))
    hb = sp.expand((2*b + 1)**2*(a**2 + 1) - (a*(2*b + 1) + 2*b)*h2b)
    cert65 = sp.expand((8*b**2 - 4*b + 1)*hb + (64 - 64*b)*e0)
    print(f'  certificates: branch a=-1: e2 - ((3b+1)a-b)(a+1) = {h2};'
          f'  8 e0 - (4b^2+2b+3)(2b+1) = {cert5}')
    print(f'                branch a^2=-1: e2 - (3b+1)(a^2+1) = {h2b};'
          f'  (2b+1)^2(a^2+1) - (a(2b+1)+2b)*that = {hb};'
          f'  (8b^2-4b+1)*that + (64-64b) e0 = {cert65}')
    ok = (len(fl[1]) == 1 and sp.solve(c0, b) == [] and sp.solve(cs, [a, b], dict=True) == []
          and cert5 == 5 and cert65 == 65)
    print(f'  SECTION 1 VERDICT irreducible over Q(z), certificates 5 and 65 exact: {ok}')
    return ok


# ----------------------------------------------------------------------------
# 2  the D-finite side: the linear ODE of order <= 3 for a sheet, exactly
# ----------------------------------------------------------------------------
def reduce_mod_P(expr):
    """Reduce a polynomial in X (coefficients in Q(z)) modulo P to degree <= 2."""
    num, den = sp.fraction(sp.together(expr))
    r = sp.rem(sp.Poly(sp.expand(num), X), sp.Poly(P, X))
    return sp.simplify(r.as_expr() / den)


def sheet_derivatives(nmax):
    """X^(k) as elements of Q(z)[X]/(P), k = 0..nmax, via X' = -P_z/P_X (implicit)."""
    Xp = -Pz / PX
    ders = [X]
    cur = X
    for _ in range(nmax):
        cur = sp.together(sp.diff(cur, z) + sp.diff(cur, X) * Xp)
        ders.append(cur)
    return ders


def section2():
    print(HR)
    print('2  D-finite: exact linear ODE of order <= 3 for a colour sheet X(z)')
    print(HR)
    ders = sheet_derivatives(3)
    # P is squarefree over Q(z) (disc_X P = -(16z^6+...+16) != 0), so P_X is invertible
    # in Q(z)[X]/(P); get its inverse by extended gcd and clear all P_X denominators.
    U, _V, G = sp.gcdex(sp.Poly(PX, X, domain='QQ(z)'), sp.Poly(P, X, domain='QQ(z)'))
    assert G.as_expr() == 1, G
    Uinv = U.as_expr()
    vecs = []
    for k, dk in enumerate(ders):
        num, den = sp.fraction(sp.together(dk))
        m = 0
        dz = den
        while m < 20:
            qq, rr = sp.div(sp.Poly(dz, X), sp.Poly(PX, X))
            if rr.is_zero:
                m += 1
                dz = qq.as_expr()
            else:
                break
        assert sp.Poly(dz, X).degree() <= 0, (k, dz)
        expr = sp.expand(num * Uinv**m) / dz
        red = reduce_mod_P(expr)
        poly = sp.Poly(sp.expand(sp.numer(sp.together(red))), X)
        denr = sp.denom(sp.together(red))
        coeffs = [sp.together(poly.coeff_monomial(X**j) / denr) for j in range(3)]
        vecs.append(coeffs)
        print(f'  X^({k}) = ' + ' + '.join(f'({sp.factor(c)})*X^{j}' for j, c in enumerate(coeffs)))
    # 4 vectors in a 3-dim Q(z)-space: the nullspace is the ODE
    M = sp.Matrix([[vecs[k][j] for k in range(4)] for j in range(3)])
    ns = M.nullspace()
    assert len(ns) >= 1
    v = ns[0]
    den = sp.lcm([sp.denom(sp.together(x)) for x in v])
    v = [sp.factor(sp.together(x * den)) for x in v]
    g = sp.gcd_list([sp.numer(sp.together(x)) for x in v])
    v = [sp.factor(sp.cancel(x / g)) for x in v]
    print('  ODE  sum_k p_k(z) X^(k) = 0  with polynomial coefficients:')
    for k, pk in enumerate(v):
        print(f'     p_{k}(z) = {pk}')
    order = max(k for k, pk in enumerate(v) if pk != 0)
    print(f'  order {order}; coefficient degrees '
          f'{[sp.Poly(pk, z).degree() if pk != 0 else None for pk in v]}')
    return v, order


# ----------------------------------------------------------------------------
# series of the sheet through X(0) = -1, exact rationals
# ----------------------------------------------------------------------------
def sheet_series(N):
    """Coefficients x_0..x_N of the sheet X(z) = -1 + sum x_n z^n (a simple root at z=0)."""
    x = [sp.Integer(-1)]
    PX0 = PX.subs({X: -1, z: 0})
    assert PX0 != 0
    for n in range(1, N + 1):
        S = sum(x[i] * z**i for i in range(n))
        val = sp.Poly(sp.expand(P.subs(X, S)), z).coeff_monomial(z**n)
        x.append(sp.Rational(-val, PX0))
    S = sum(x[i] * z**i for i in range(N + 1))
    resid = sp.Poly(sp.expand(P.subs(X, S)), z)
    low = [resid.coeff_monomial(z**n) for n in range(N + 1)]
    assert all(c == 0 for c in low), low
    return x


def _rows(shifted, order, D, N):
    rows = []
    for n in range(N + 1):
        row = []
        for k in range(order + 1):
            for j in range(D + 1):
                row.append(shifted[k][n - j] if 0 <= n - j <= N else 0)
        rows.append(row)
    return sp.Matrix(rows)


def search_relation(shifted, order, D, N):
    """Exact nullspace search for sum_{k<=order} c_k(z) f_k(z) = 0, deg c_k <= D."""
    nunk = (order + 1) * (D + 1)
    M = _rows(shifted, order, D, N)
    assert M.shape[0] >= nunk + 5, 'not enough equations'
    return M.nullspace()


def section3(x):
    print(HR)
    print('3  q-holonomic search on the sheet X(0) = -1: sum_{k<=3} c_k(z) X(q^k z) = 0 ?')
    print(HR)
    N = len(x) - 1
    results = {}
    # Direct nullspace at exact rational q (the specialised statement, which is what the
    # theorem is about: q fixed, not a root of unity).
    for qv in (sp.Rational(11, 10), sp.Integer(2), sp.Rational(3, 2)):
        for D in (2, 4, 6):
            shifted = [[x[n] * qv**(k * n) for n in range(N + 1)] for k in range(4)]
            ns = search_relation(shifted, 3, D, N)
            results[(str(qv), D)] = len(ns)
            print(f'  q = {qv}, order<=3, deg<={D}: nullspace dim = {len(ns)}')
    # Symbolic q, via rank: rank over Q(q) >= rank at any rational specialisation, so
    # FULL COLUMN RANK at one specialisation already excludes a relation over Q(q) (an
    # identity in q). Exact rational arithmetic; no symbolic elimination needed.
    for D in (2, 4, 6):
        nunk = 4 * (D + 1)
        full = []
        for qv in (sp.Rational(17, 5), sp.Rational(7, 3)):
            shifted = [[x[n] * qv**(k * n) for n in range(N + 1)] for k in range(4)]
            full.append(_rows(shifted, 3, D, N).rank() == nunk)
        results[('symbolic q (rank)', D)] = 0 if all(full) else 1
        print(f'  symbolic q, order<=3, deg<={D}: full column rank ({nunk}) at '
              f'q = 17/5, 7/3: {full} -> relation over Q(q) excluded: {all(full)}')
    ok = all(v == 0 for v in results.values())
    print(f'  SECTION 3 VERDICT no q-difference relation in any tested (order,degree): {ok}')
    print('     (corroboration of Bezivin-Ramis / Schaefke-Singer on this sheet; the')
    print('      theorem excludes ALL orders and degrees, the search only those tested)')
    return ok


def section4(x, ode):
    print(HR)
    print('4  controls: the same searcher finds what exists')
    print(HR)
    N = len(x) - 1
    order = max(k for k, pk in enumerate(ode) if pk != 0)
    D = max(sp.Poly(pk, z).degree() for pk in ode if pk != 0)
    derivs = []
    for k in range(order + 1):
        derivs.append([sp.Integer(0)] * (N + 1))
        for n in range(N + 1 - k):
            derivs[k][n] = x[n + k] * sp.factorial(n + k) / sp.factorial(n)
    # use only equations up to z^(N-order), where every derivative coefficient is exact
    Ncut = N - order
    derivs_cut = [d[:Ncut + 1] for d in derivs]
    ns = search_relation(derivs_cut, order, D, Ncut)
    found = len(ns) >= 1
    print(f'  (a) differential search, order<={order}, deg<={D}: nullspace dim = {len(ns)} '
          f'(expect >= 1)')
    if found:
        v = ns[0]
        cs = [sum(v[k * (D + 1) + j] * z**j for j in range(D + 1)) for k in range(order + 1)]
        k0 = next(k for k, pk in enumerate(ode) if pk != 0)
        ratios = {sp.simplify(sp.cancel(cs[k] * ode[k0] - cs[k0] * ode[k]))
                  for k in range(order + 1)}
        same = ratios == {0}
        print(f'      found ODE proportional to the section-2 ODE: {same}')
        found = found and same
    # (b) q-search on the rational function 1/(1-z): (1-z) f(z) = (1-qz) f(qz)
    y = [sp.Integer(1)] * (N + 1)
    shifted = [[y[n] * q**(k * n) for n in range(N + 1)] for k in range(2)]
    ns = search_relation(shifted, 1, 1, N)
    okb = len(ns) >= 1
    print(f'  (b) q-search on 1/(1-z), order<=1, deg<=1, symbolic q: nullspace dim = '
          f'{len(ns)} (expect >= 1)')
    if okb:
        v = ns[0]
        cs = [sp.factor(sum(v[k * 2 + j] * z**j for j in range(2))) for k in range(2)]
        print(f'      relation: ({cs[0]}) f(z) + ({cs[1]}) f(qz) = 0')
    ok = found and okb
    print(f'  SECTION 4 VERDICT both controls found: {ok}')
    return ok


def main():
    ok1 = section1()
    ode, order = section2()
    N = 40
    x = sheet_series(N)
    print(f'  sheet through X(0) = -1: x_0..x_6 = {x[:7]} (exact Q, verified to z^{N})')
    ok3 = section3(x)
    ok4 = section4(x, ode)
    print(HR)
    print('CONCLUSION')
    print(HR)
    print('  * P is irreducible over Q(z) (Lean: colorCubicAt_ne_zero +')
    print('    colorCubic_no_ratFunc_root, any char-0 field).')
    print(f'  * A sheet is D-finite: explicit order-{order} ODE with polynomial coefficients.')
    print('  * No rational q-difference relation in any tested class, at exact rational q')
    print('    and over Q(q) by rank, while the same searcher recovers the ODE and the')
    print('    q-equation of a rational function.')
    print('  * With Bezivin-Ramis / Schaefke-Singer (D-finite AND q-holonomic => rational)')
    print('    this is a scope-(b) exclusion of W1 route 1: no rational base q-connection')
    print('    on the z-line has the colour sheets as flat sections. The classical')
    print('    prolongation exists and is exact (dead); the rational q-analogue does not')
    print('    exist.')
    print('  * NOT excluded: non-rational coefficients, operators living on Sigma rather')
    print('    than on the base, the local q-dilation at a branch point. D_q is NOT')
    print('    constructed.')
    allok = ok1 and ok3 and ok4
    print(f'  ALL CHECKS PASS: {allok}')
    return 0 if allok else 1


if __name__ == '__main__':
    raise SystemExit(main())
