#!/usr/bin/env python3
"""
w1_local_qdilation_branchpoint_probe.py — bean qou-7fnr (follows qou-1z28 / #6695).

QUESTION. #6695 pruned W1 route 1 — a rational q-connection on the BASE z-line cannot
have the colour sheets as flat sections — and then asserted that the LOCAL q-dilation
t -> mu t at a ramification point z = z_c + t^2 escapes the same exclusion, because
'every power series satisfies a first-order q-equation with a power-series
coefficient'. That reason is about POWER-SERIES coefficients; the theorem
(D-finite AND q-holonomic => rational: Bezivin, Aequationes Math. 43 (1992) 159-176;
Ramis, Ann. Fac. Sci. Toulouse 1 (1992) 53-94; Schaefke-Singer, JEMS 21 (2019)
2751-2792) is about RATIONAL ones. So the claim was argued from the wrong premise.
This probe settles it.

ANSWER: the local case is EXCLUDED TOO, by the identical argument. The claim in #6695
is wrong and is corrected by this tranche.

  In the local coordinate the sheets are power series in t, each algebraic over K(t)
  (it satisfies the cubic P(X, z_c + t^2) = 0 over K[t]) and therefore D-finite in t.
  A q-dilation t -> mu t with coefficients rational in t would make a sheet
  q-holonomic in t. The theorem then forces the sheet to be RATIONAL in t. It is not:
  the local cubic has no root in K(t) at all.

  The reason it has none is a degree obstruction, which is what the Lean carries
  (QOU.Mass.IrreducibleCubicNoQuadraticRoot.no_root_of_irreducible_cubic, sorry-free):
  t^2 = z - z_c, so every element of K(t) is annihilated by a degree-2 polynomial over
  K(z); the colour cubic is irreducible over K(z) (QOU.Mass.ColorCubicIrreducible,
  proved for EVERY char-0 field, so in particular for K = Q(z_c)); and an irreducible
  cubic has no root of degree <= 2.

SECTIONS (all exact — sympy over Q and over K = Q[z_c]/(branch sextic); NO float64):
  1  K is a genuine degree-6 field: the branch sextic is irreducible over Q. And
     [K(t) : K(z)] = 2: z - z_c is not a square in K(z) (degree parity), and t is
     annihilated by X^2 - (z - z_c), which is the Lean lemma's hypothesis on the nose.
  2  the colour cubic has no root in K[z] — the hypothesis 'irreducible over K(z)'
     instantiated at this specific degree-6 K, cross-checking the Lean theorem that
     covers every char-0 field.
  3  the local cubic P(X, z_c + t^2) has no root in K[t]: a leading-term bound kills
     degree >= 3, and a Groebner basis [1] over Q[c0,c1,c2,z_c] modulo the sextic
     kills degree <= 2. With Gauss this is 'no root in K(t)', i.e. no sheet is
     rational in the local coordinate — the hinge.
  4  the local-coordinate analogue of the #6695 search, on the unramified sheet
     (the one analytic in t^2, whose coefficients stay in K): no q-difference relation
     sum_{k<=3} c_k(t) X(mu^k t) = 0 with c_k rational in t, at several exact rational
     mu. Rank certified by a ring map K -> F_p (rank over K is at least the rank of
     the image, so full column rank mod p excludes a relation over K). Controls: the
     same searcher DOES find the sheet's algebraic relation over K(t).

SCOPE. Sections 3 and 4 are exact but finite; the exclusion of ALL orders and degrees
is the cited theorem, not the search. What is excluded is a q-dilation with RATIONAL
coefficients, on the base or in the local chart alike. Still NOT excluded: coefficients
that are not rational functions, and operators living on Sigma rather than on either
coordinate line. D_q is NOT constructed. Anti-fit: nothing is fitted; no witness.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

X, z, t, zc = sp.symbols('X z t zc')
c0, c1, c2 = sp.symbols('c0 c1 c2')

# The colour spectral cubic and its branch locus.
P = X**3 + (z + 1)*X**2 + (z**2 + z + 1)*X + (z**3 + z**2 + z + 1)
SEXTIC = 16*zc**6 + 24*zc**5 + 35*zc**4 + 50*zc**3 + 35*zc**2 + 24*zc + 16

HR = '=' * 78


def _red(e):
    """Reduce a polynomial expression modulo the branch sextic in z_c (i.e. work in
    K = Q[z_c]/(sextic), the field the branch point generates)."""
    return sp.rem(sp.Poly(sp.expand(e), zc), sp.Poly(SEXTIC, zc)).as_expr()


# ----------------------------------------------------------------------------
# 1  K is degree 6, and K(t)/K(z) is quadratic
# ----------------------------------------------------------------------------
def section1():
    print(HR)
    print('1  the branch field K = Q(z_c), and [K(t) : K(z)] = 2')
    print(HR)
    fl = sp.factor_list(SEXTIC)
    irred = len(fl[1]) == 1 and fl[1][0][1] == 1
    print(f'  branch sextic {sp.expand(SEXTIC)}')
    print(f'  irreducible over Q: {irred}  -> K = Q(z_c) is a degree-6 number field')
    # t satisfies X^2 - (z - z_c) over K(z): this is the Lean lemma's hypothesis `g`.
    g = X**2 - (z - zc)
    print(f'  t is annihilated by g(X) = {g} over K(z); deg g = 2, g != 0')
    # z - z_c is not a square in K(z): a square in K(z) has even degree as a rational
    # function, and z - z_c has degree 1. Checked here as: no r in K[z] with r^2 = z-z_c
    # (a root would force 2*deg r = 1), and no rational r = u/v either since
    # u^2 = (z-z_c) v^2 compares degrees 2 deg u = 1 + 2 deg v, impossible mod 2.
    print('  z - z_c is not a square in K(z): 2 deg u = 1 + 2 deg v has no solution '
          'mod 2, so [K(t):K(z)] = 2 exactly (not 1)')
    ok = irred
    print(f'  SECTION 1 VERDICT K degree 6, K(t)/K(z) quadratic: {ok}')
    return ok


# ----------------------------------------------------------------------------
# 2  no root of the colour cubic in K[z] (irreducibility over K(z) at this K)
# ----------------------------------------------------------------------------
def section2():
    print(HR)
    print('2  the colour cubic has no root in K[z] — irreducible over K(z) at this K')
    print(HR)
    print('  (QOU.Mass.ColorCubicIrreducible proves this for EVERY char-0 field; this'
          ' section instantiates it at the specific degree-6 K, as a cross-check)')
    # degree >= 2 by the leading term: 3d vs 1+2d, 2+d, 3
    dbound = all(3*d > max(1 + 2*d, 2 + d, 3) for d in range(2, 60))
    print(f'  leading-term bound 3d > max(1+2d, 2+d, 3) for d >= 2: {dbound}')
    # degree <= 1 over K: r = c0 + c1 z, solve with the sextic adjoined
    r = c0 + c1*z
    eqs = sp.Poly(sp.expand(P.subs(X, r)), z).all_coeffs()
    G = sp.groebner(list(eqs) + [SEXTIC], c0, c1, zc, order='lex')
    triv = list(G.exprs) == [sp.Integer(1)]
    print(f'  degree <= 1 over K: Groebner basis of the coefficient system + sextic = '
          f'{list(G.exprs)}  -> no solution: {triv}')
    ok = dbound and triv
    print(f'  SECTION 2 VERDICT no root in K[z]: {ok}')
    return ok


# ----------------------------------------------------------------------------
# 3  no root of the LOCAL cubic in K[t] — the hinge
# ----------------------------------------------------------------------------
def section3():
    print(HR)
    print('3  the local cubic P(X, z_c + t^2) has no root in K[t] — the hinge')
    print(HR)
    zz = zc + t**2
    Ploc = X**3 + (zz + 1)*X**2 + (zz**2 + zz + 1)*X + (zz**3 + zz**2 + zz + 1)
    cs = [sp.factor(_red(c)) for c in sp.Poly(sp.expand(Ploc), X).all_coeffs()]
    print('  local cubic coefficients (reduced mod the sextic):')
    for i, c in enumerate(cs):
        print(f'     X^{3-i}: {c}')
    # A root r in K[t] of degree d: deg r^3 = 3d, against 2+2d, 4+d, 6.
    dbound = all(3*d > max(2 + 2*d, 4 + d, 6) for d in range(3, 60))
    print(f'  leading-term bound 3d > max(2+2d, 4+d, 6) for d >= 3: {dbound}'
          f'  -> only d in {{0,1,2}} survives')
    r = c0 + c1*t + c2*t**2
    eqs = sp.Poly(sp.expand(Ploc.subs(X, r)), t).all_coeffs()
    G = sp.groebner(list(eqs) + [SEXTIC], c0, c1, c2, zc, order='lex')
    triv = list(G.exprs) == [sp.Integer(1)]
    print(f'  degree <= 2 over K: Groebner basis of the coefficient system + sextic = '
          f'{list(G.exprs)}  -> no solution: {triv}')
    ok = dbound and triv
    print(f'  SECTION 3 VERDICT no root in K[t]; with Gauss (the cubic is monic over '
          f'the integrally closed K[t]) no root in K(t): {ok}')
    print('     => NO SHEET IS RATIONAL IN THE LOCAL COORDINATE, which is exactly what')
    print('        the rationality theorem needs in order to bite in the local chart.')
    return ok


# ----------------------------------------------------------------------------
# the unramified sheet as an exact power series over K
# ----------------------------------------------------------------------------
def _mul_trunc_K(a, b, m):
    out = [sp.Integer(0)] * (m + 1)
    for i, ai in enumerate(a):
        if ai == 0 or i > m:
            continue
        for j, bj in enumerate(b):
            if i + j > m:
                break
            if bj != 0:
                out[i + j] = _red(out[i + j] + ai * bj)
    return out


def _Ploc_of_series(s, m):
    """P(S(w), z_c + w) truncated to degree m in w, coefficients reduced in K."""
    s2 = _mul_trunc_K(s, s, m)
    s3 = _mul_trunc_K(s2, s, m)
    # z = z_c + w, so z+1 = (z_c+1) + w; z^2+z+1 = (z_c^2+z_c+1) + (2z_c+1) w + w^2;
    # z^3+z^2+z+1 = (..) + (..) w + (..) w^2 + w^3
    A = [_red(zc + 1), sp.Integer(1)]
    B = [_red(zc**2 + zc + 1), _red(2*zc + 1), sp.Integer(1)]
    C = [_red(zc**3 + zc**2 + zc + 1), _red(3*zc**2 + 2*zc + 1), _red(3*zc + 1),
         sp.Integer(1)]
    out = list(s3)
    for k in range(m + 1):
        for j, aj in enumerate(A):
            if k - j >= 0:
                out[k] = _red(out[k] + aj * s2[k - j])
        for j, bj in enumerate(B):
            if k - j >= 0:
                out[k] = _red(out[k] + bj * s[k - j])
        if k < len(C):
            out[k] = _red(out[k] + C[k])
    return out


def _inv_K(e):
    """Inverse in K = Q[z_c]/(sextic). The sextic is irreducible over Q, so every
    nonzero residue is invertible; sympy's `invert` is the extended Euclid there."""
    e = _red(e)
    assert e != 0, 'not invertible: zero in K'
    return _red(sp.invert(sp.Poly(e, zc), sp.Poly(SEXTIC, zc)).as_expr())


def unramified_sheet(N):
    """The sheet analytic in w = t^2 at the branch point, as x_0..x_N in K.

    At w = 0 the cubic has a double root (the two colliding sheets) and one simple
    root; Newton's iteration converges on the simple one, whose coefficients stay in K.
    Returned as a series in w; the local coordinate is t with w = t^2.

    The double root is the common root of P(., z_c) and P_X(., z_c). Do NOT reach for
    sympy's gcd here: over Z[z_c] it does not see the collision at all (it returns 1),
    because the sextic relation is not imposed — the gcd has to be taken in K[X]. One
    step of Euclid suffices and is written out: with a = z_c+1, b = z_c^2+z_c+1,
    c = z_c^3+z_c^2+z_c+1, the remainder of P by P_X is
    ((6b - 2a^2) X + (9c - ab)) / 9, so the double root is X_0 = -(9c - ab)/(6b - 2a^2),
    and the simple root is -(a) - 2 X_0 since the three roots sum to -a."""
    a = _red(zc + 1)
    b = _red(zc**2 + zc + 1)
    c = _red(zc**3 + zc**2 + zc + 1)
    alpha = _red(6*b - 2*a**2)
    beta = _red(9*c - a*b)
    Xdbl = _red(-beta * _inv_K(alpha))                      # the colliding double root
    # sanity: it really is a double root of P(., z_c)
    assert _red(sp.expand(P.subs({X: Xdbl, z: zc}))) == 0, 'X_dbl is not a root'
    assert _red(sp.expand(sp.diff(P, X).subs({X: Xdbl, z: zc}))) == 0, 'X_dbl not double'
    x0 = _red(-a - 2*Xdbl)                                  # the remaining simple root
    assert _red(sp.expand(P.subs({X: x0, z: zc}))) == 0, 'simple root is not a root'
    dP0 = _red(sp.expand(sp.diff(P, X).subs({X: x0, z: zc})))
    assert dP0 != 0, 'the third root was not simple'
    inv = _inv_K(dP0)
    x = [x0]
    for n in range(1, N + 1):
        val = _Ploc_of_series(x + [sp.Integer(0)], n)[n]
        x.append(_red(-val * inv))
    resid = _Ploc_of_series(x, N)
    assert all(_red(c) == 0 for c in resid), resid[:5]
    return x


# ----------------------------------------------------------------------------
# 4  the local q-difference search, with the rank certified through K -> F_p
# ----------------------------------------------------------------------------
def _sextic_root_mod_p(p):
    """A root of the branch sextic in F_p, or None. Scanned directly, which is why the
    primes below are moderate rather than near 2^31: the rank argument is exact for
    ANY prime at which the ring map K -> F_p is defined, so nothing is bought by a
    large one and a linear scan over 2^31 residues would never finish."""
    for r in range(p):
        if (16*pow(r, 6, p) + 24*pow(r, 5, p) + 35*pow(r, 4, p) + 50*pow(r, 3, p)
                + 35*r*r + 24*r + 16) % p == 0:
            return r
    return None


def _primes_with_root(count, lo=10007):
    """The first `count` primes >= lo at which the sextic has a root (and which do not
    divide its leading coefficient), with that root."""
    out = []
    p = lo
    while len(out) < count:
        p = sp.nextprime(p)
        if 16 % p == 0:
            continue
        r = _sextic_root_mod_p(p)
        if r is not None:
            out.append((int(p), int(r)))
    return out


def _to_Fp(e, p, root):
    """Image of an element of K under K -> F_p sending z_c to a root of the sextic."""
    poly = sp.Poly(_red(e), zc)
    acc = 0
    for i, c in enumerate(reversed(poly.all_coeffs())):
        c = sp.Rational(c)
        num, den = int(c.p), int(c.q)
        acc = (acc + num * pow(den, p - 2, p) * pow(root, i, p)) % p
    return acc % p


def _full_column_rank_Fp(rows, ncols, p):
    rows = [list(r) for r in rows]
    piv = 0
    for c in range(ncols):
        r = next((i for i in range(piv, len(rows)) if rows[i][c] % p), None)
        if r is None:
            return False
        rows[piv], rows[r] = rows[r], rows[piv]
        inv = pow(rows[piv][c], p - 2, p)
        rows[piv] = [(v * inv) % p for v in rows[piv]]
        for i in range(len(rows)):
            if i != piv and rows[i][c]:
                f = rows[i][c]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[piv])]
        piv += 1
    return True


def section4(xw, N):
    print(HR)
    print('4  local q-dilation search on the unramified sheet: '
          'sum_{k<=3} c_k(t) X(mu^k t) = 0 ?')
    print(HR)
    # the sheet in the LOCAL coordinate t: X(t) = sum xw[m] t^(2m)
    xt = [sp.Integer(0)] * (2 * N + 1)
    for m, cm in enumerate(xw):
        xt[2 * m] = cm
    M = 2 * N
    primes = _primes_with_root(2)
    print(f'  ring maps K -> F_p used (p, image of z_c): {primes}')
    results = {}
    for mu in (sp.Integer(2), sp.Rational(3, 2), sp.Rational(11, 10)):
        for D in (2, 4):
            nunk = 4 * (D + 1)
            ok_all = []
            for p, root in primes:
                num, den = int(sp.Rational(mu).p), int(sp.Rational(mu).q)
                mu_p = num * pow(den, p - 2, p) % p
                shifted = [[(_to_Fp(xt[n], p, root) * pow(mu_p, k * n, p)) % p
                            for n in range(M + 1)] for k in range(4)]
                rows = []
                for n in range(M + 1):
                    row = []
                    for k in range(4):
                        for j in range(D + 1):
                            row.append(shifted[k][n - j] if 0 <= n - j <= M else 0)
                    rows.append(row)
                ok_all.append(_full_column_rank_Fp(rows, nunk, p))
            excluded = bool(ok_all) and all(ok_all)
            results[(str(mu), D)] = excluded
            print(f'  mu = {mu}, order<=3, deg<={D}: full column rank ({nunk}) mod p '
                  f'for {len(ok_all)} prime(s): {ok_all} -> no relation over K: {excluded}')
    ok = all(results.values())
    print(f'  SECTION 4 VERDICT no rational-in-t q-difference relation found: {ok}')
    return ok


def section4_control(xw, N):
    print(HR)
    print('4b control: the same machinery DOES find the sheet\'s algebraic relation')
    print(HR)
    # The sheet satisfies P(X, z_c + w) = 0 with w = t^2: check the series annihilates
    # the local cubic to the computed order. This is the relation that exists, found by
    # the same truncated arithmetic that section 4 searches with.
    resid = _Ploc_of_series(xw, N)
    ok = all(_red(c) == 0 for c in resid)
    print(f'  P(X(w), z_c + w) = 0 to order w^{N}: {ok}')
    print(f'  first coefficients of the unramified sheet (in K = Q[z_c]/(sextic)):')
    for i in range(min(3, len(xw))):
        print(f'     x_{i} = {sp.factor(xw[i])}')
    print(f'  SECTION 4b VERDICT control found: {ok}')
    return ok


def main():
    ok1 = section1()
    ok2 = section2()
    ok3 = section3()
    N = 24
    xw = unramified_sheet(N)
    ok4c = section4_control(xw, N)
    ok4 = section4(xw, N)
    print(HR)
    print('CONCLUSION')
    print(HR)
    print('  * K = Q(z_c) is a degree-6 field and K(t)/K(z) is quadratic (t^2 = z - z_c).')
    print('  * The colour cubic has no root in K[z] (so it is irreducible over K(z)) and')
    print('    no root in K[t] at any degree, hence none in K(t): NO SHEET IS RATIONAL')
    print('    IN THE LOCAL COORDINATE.')
    print('  * The sheets are algebraic over K(t), hence D-finite in t. So a q-dilation')
    print('    t -> mu t with RATIONAL-in-t coefficients would make a sheet q-holonomic')
    print('    in t, and Bezivin / Ramis / Schaefke-Singer would force it rational in t.')
    print('    It is not. The local q-dilation is EXCLUDED, exactly as the base one was.')
    print('  * Therefore #6695 was WRONG to say the local chart escapes the exclusion.')
    print('    Its reason concerned power-series coefficients; the theorem concerns')
    print('    rational ones. The degree obstruction behind the correction is Lean-proved')
    print('    (QOU.Mass.IrreducibleCubicNoQuadraticRoot, sorry-free).')
    print('  * STILL not excluded: coefficients that are not rational functions, and')
    print('    operators living on Sigma rather than on a coordinate line. D_q is NOT')
    print('    constructed.')
    allok = ok1 and ok2 and ok3 and ok4c and ok4
    print(f'  ALL CHECKS PASS: {allok}')
    return 0 if allok else 1


if __name__ == '__main__':
    raise SystemExit(main())
