#!/usr/bin/env python3
"""Is sigma(x)/D(x) a GAUGE COBOUNDARY on the exact L6a4 class-1 Ptolemy point?  (#7092)

THE QUESTION (issue #7092, the falsifiable form of bean qou-qjhc).  The class-1 point x
of the L6a4 Ptolemy variety P^c is known exactly over K = Q[T]/(f), a degree-4 Galois
field containing zeta_3.  Two maps send it to a point of P^{-c}:

  * the SIGMA-TRANSPORT: apply a field automorphism sigma of K with sigma(zeta_3) =
    zeta_3^2 coordinate-wise (two such sigma; ptolemy_class1_galois_group.py);
  * DUALITY D: the action of rho -> rho^{-T} on Ptolemy coordinates, which is the
    relabelling 1<->2 on {2,1,0,0} indices and the bidegree-(1,3) determinant formula
    on {1,1,1,0} indices (ptolemy_duality_1110_plucker_identity.py).

Ptolemy coordinates are defined only up to the DECORATION GAUGE, so "D = sigma-transport
on this point" means: sigma(x) and D(x) differ by a gauge, i.e. the coordinate-wise ratio
r_t = sigma(x_t) / D(x)_t is a COBOUNDARY of the gauge action.  Definite yes / no.

THE GAUGE, and why there are three ansaetze rather than one.  A decoration is an
N-coset g_v N at each ideal vertex (cusp) v; changing it by the torus, g_v -> g_v d_v with
d_v = diag(d_0, d_1, d_2), det = 1, multiplies c_t by prod_v d_{v,0}^{[t_v>=1]}
d_{v,1}^{[t_v>=2]} d_{v,2}^{[t_v>=3]}.  That is the 128 x 6 exponent matrix snappy
exposes as _ptolemy_equations_action_by_decoration_change (two parameters per cusp,
three cusps) -- ansatz B, the actual gauge group of the variety (GGZ arXiv:1207.6711
section 5).  The issue as written asks for SCALARS lambda_v with ratio = prod
lambda_{v_i}^{t_i}: the sub-torus d_v = lambda_v * I, one parameter per cusp -- ansatz A.
On the vertex coordinates c_{3000} = 1 that sub-torus acts by lambda_v^3, so if the vertex
coordinates are counted (the issue says "every Ptolemy coordinate") lambda_v is forced
into mu_3 -- ansatz A'.  All three are tested; none is chosen for its answer.

THE DECISION IS BY THE Z-KERNEL, not a K-linear solve.  Write A for the exponent
matrix (rows = coordinates, columns = gauge parameters).  r is a coboundary iff
(i) for every INTEGER relation m with m^T A = 0, prod_t r_t^{m_t} = 1 in K, and
(ii) the induced homomorphism on the row lattice extends to Z^k, which is automatic
when the row lattice is all of Z^k (measured below).  (i) is decided on a genuine Z-basis
of the kernel, obtained by unimodular column reduction of A^T -- a Q-basis scaled to
integers would only span a finite-index sublattice and could miss a root-of-unity
obstruction.  A failing relation is the refutation and is printed in full.  If every
relation passes, the gauge element is produced explicitly and EVERY one of the 128
equations is re-verified.

EXACTNESS.  All arithmetic is in K: polynomials over Q reduced modulo f, inverses by
sympy's exact `invert`.  No floats, no tolerances.  An element is 1 or it is not.

WHAT IS NOT FITTED.  D is written down from the definition (dual decoration g* =
(v1 x v2, v1 x v3, v2 x v3), det g* = det(g)^2 = 1) and then CHECKED on random exact
SL(3) decorations before it touches the point; the point is checked against the GGZ
per-tetrahedron Ptolemy relation before D touches it; the sigma are checked to be
automorphisms inverting zeta_3.  No coefficient is solved for except the gauge element,
whose existence is the question, and no coordinate subset is selected: all 128 non-vertex
coordinates enter every test.

SCOPE.  A "yes" here is a point-level fact about the class-1 point: the two maps agree
ON THIS POINT up to gauge.  It is not an identity of maps on the variety, and it does not
by itself say that the duality involution on representations INDUCES the sigma-transport
(that needs the point-to-representation direction, still bean qou-qjhc).  A "no" is
scope-(a): these two explicit maps differ on this point by something that is not a gauge.

RESULT (run 2026-09-11; every figure below is in the witness, exact in K).

  Gal(K/Q) = Z/2 x Z/2.  sigma_a and sigma_b are both involutions; tau = sigma_a o sigma_b is the
  automorphism fixing Q(zeta_3).  Load-bearing for consistency: D is an involution on
  coordinates (g** = g), so D(x) ~ sigma(x) forces sigma^2(x) ~ x; with sigma of order 4 the two
  verdicts below would contradict each other, with sigma of order 2 they do not.

  sigma_a -- NOT A COBOUNDARY, for all three gauge groups.  91 of the 122 torus kernel
  relations have product != 1.  The simplest obstruction is two coordinates with IDENTICAL
  gauge exponents (vertices 1 and 2 of tetrahedron 0 both lie on cusp 1) whose ratios differ:

      sigma_a(x)/D(x) on c_0210_0  divided by the same on c_0120_0
          = -128*T^3/113642578125 - 53507/46548,      not a root of unity.

  sigma_b -- COBOUNDARY of the PGL(3) decoration gauge over K.  All 122 torus kernel relations
  have product exactly 1, so r = sigma_b(x)/D(x) is a homomorphism L -> K^x on the row lattice
  L = {e in Z^6 : sum e = 0 mod 3} (every row has entry-sum 3: the centre mu_3 of SL(3) acts
  trivially on Ptolemy coordinates).  L is the character lattice of T_SL(3)/mu_3 = T_PGL(3),
  the group that actually acts on the coordinates, so r IS an element of T_PGL(3)(K).  It is
  recorded on a Z-basis of L (r(3 e_0) = 256 T^3/189404296875 + 308/3879; r(e_1 - e_0) =
  r(e_3 - e_0) = r(e_5 - e_0) = 16315/23274 - 256 T^3/113642578125; r(e_2 - e_0) = 1;
  r(e_4 - e_0) = -256 T^3/113642578125 - 6959/23274) and all 128 equations are re-verified
  from it.  The ratio takes 4 distinct values; 48 of 128 coordinates have ratio exactly 1.

  The one thing sigma_b does NOT give: a lift to a diagonal SL(3) matrix over K.  That needs
  a cube root of w = r(3 e_0) in K, and Y^3 - w is IRREDUCIBLE over K (exact factorisation
  over the algebraic field).  So an SL(3)-decoration change exists only over K(w^(1/3)).  The
  class of w in K^x/(K^x)^3 = H^1(K, mu_3) is invariant under K-gauge changes of x and under
  the choice of the antidiagonal element in g*, so this is a property of the pair (x, sigma_b),
  not of a normalisation.

  Scalar ansatz (issue #7092 as literally written, lambda_v^{t_i}) -- NOT A COBOUNDARY for
  either sigma (first obstruction: c_0021_0 vs c_0111_0; 97-113 of 125 relations fail).  The
  scalars are the sub-torus d_v = lambda_v I, one parameter per cusp; the decoration gauge has
  two per cusp, and the difference is exactly what sigma_b's ratio uses.

  Guards: pure gauge g.x/x has all 122 kernel products = 1; kernel products of sigma(x)/D(x)
  unchanged under a random exact gauge of x (so the elimination gauge is irrelevant, and
  snappy uses the same 6 eliminated coordinates for P^c and P^-c, differing only by u -> u^2);
  D(x) is a genuine P^-c point (0 identification failures at u1, 16 at u2, all 32 Ptolemy
  relations hold); the duality formulas are exact on 25/25 random SL(3) decorations.

  WHAT THIS ANSWERS.  On the exact class-1 point, duality agrees with the sigma_b-transport up
  to the PGL(3) decoration gauge, and does NOT agree with the sigma_a-transport up to any
  gauge.  "The sigma-transport" is therefore not one map: the two automorphisms inverting
  zeta_3 differ by tau, and tau(x) is not gauge-equivalent to x.  Point-level, this point
  only; it does not by itself establish that rho -> rho^{-T} on representations induces
  sigma_b -- bean qou-qjhc stays open with that as its remaining content.
"""
from __future__ import annotations

import json
import random
import re
import sys
import time
import warnings
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings('ignore')
import sympy as sp  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

_T0 = time.monotonic()
T = sp.Symbol('T')
N = 3
NAME, KCLS = 'L6a4', 1
POINT_FILE = HERE / f'{NAME}-c{KCLS}-ptolemy-in-K.json'

# ----------------------------------------------------------------------------- K
d = json.load(open(POINT_FILE))
f = sp.Poly(sp.sympify(d['field']['min_poly'].replace('t', 'T')), T, domain='QQ')


def K(e):
    """Reduce an expression / Poly to its canonical representative in K = Q[T]/(f)."""
    p = e if isinstance(e, sp.Poly) else sp.Poly(sp.expand(e), T, domain='QQ')
    return p.rem(f)


ONE, ZERO = K(sp.Integer(1)), K(sp.Integer(0))


def kmul(a, b):
    return K(a * b)


def kinv(a):
    assert not a.is_zero, "inverse of 0 in K"
    return K(sp.Poly(sp.invert(a.as_expr(), f.as_expr(), T), T, domain='QQ'))


def kpow(a, n):
    if n < 0:
        a, n = kinv(a), -n
    r = ONE
    for _ in range(n):
        r = kmul(r, a)
    return r


def kdet3(m):
    """Exact 3x3 determinant of a matrix of K-elements."""
    (a, b, c), (dd, e, g), (h, i, j) = m
    return K(a * (e * j - g * i) - b * (dd * j - g * h) + c * (dd * i - e * h))


def kstr(a):
    return str(a.as_expr())


co = {k: K(sp.sympify(re.sub(r'\bt\b', 'T', v))) for k, v in d['ptolemy'].items()}
u2 = co.pop('u')            # the cube root the producer used  (recorded under key 'u')
co.pop('t', None)           # the generator itself, also recorded in the file
u1 = K(-1 - u2.as_expr())
assert K(u2 ** 2 + u2 + 1).is_zero and K(u1 ** 2 + u1 + 1).is_zero
assert K(u1 - u2 ** 2).is_zero, "u1 must be u2^2"
assert all(k.startswith('c_') for k in co), sorted(co)   # nothing but coordinates left

# --------------------------------------------------------------------------- sigma
SIGMA = {
    'sigma_a': sp.sympify("-64*T**3/101015625 - T + 760000/1293"),
    'sigma_b': sp.sympify("-T**3/625000 + 19*T**2/8000 - 1293*T/512 + 11875/8"),
}


def sig_apply(x, g):
    return K(x.as_expr().subs(T, g))


for nm, g in SIGMA.items():
    assert K(f.as_expr().subs(T, g)).is_zero, f"{nm}: f(sigma T) != 0"
    assert K(sig_apply(u2, g) - u1).is_zero, f"{nm}: does not invert zeta_3"
_comp = lambda g, h: K(g.subs(T, h)).as_expr()          # g o h on the generator
for nm, g in SIGMA.items():
    assert K(_comp(g, g) - T).is_zero, f"{nm} is not an involution"
_tau = _comp(SIGMA['sigma_a'], SIGMA['sigma_b'])
assert not K(_tau - T).is_zero and K(_comp(_tau, _tau) - T).is_zero
print("sigma_a, sigma_b: verified automorphisms of K with sigma(u2) = u1 = u2^2; both are INVOLUTIONS,")
print("   so Gal(K/Q) = Z/2 x Z/2 and tau = sigma_a o sigma_b is the nontrivial automorphism fixing Q(zeta_3)")

# -------------------------------------------------------------------------- snappy
import snappy  # noqa: E402
from snappy.ptolemy.ptolemyGeneralizedObstructionClass import (  # noqa: E402
    PtolemyGeneralizedObstructionClass as OC)

M = snappy.Manifold(NAME)
V = M.ptolemy_variety(N, obstruction_class=KCLS, eliminate_fixed_ptolemys=True)
V0 = M.ptolemy_variety(N, obstruction_class=KCLS)
ntet = M.num_tetrahedra()
cusp_of = M._get_cusp_indices_and_peripheral_curve_data()[0]     # [tet][vertex] -> cusp
ncusp = M.num_cusps()
assert set(V.variables) - {'u'} == set(co), "corpus point is not on this variety"
assert len(V.equations_with_non_zero_condition) == d['roundtrip']['original_equations']
ELIM = sorted(set(V0.variables) - set(V.variables))
print(f"triangulation {M.triangulation_isosig(decorated=False)}: {ntet} tets, {ncusp} cusps;"
      f" variables match the corpus point ({len(co)} canonical); "
      f"{len(ELIM)} coordinates eliminated by eliminate_fixed_ptolemys: {ELIM}")

act_rows, act_names, act_cols = M._ptolemy_equations_action_by_decoration_change(N)
assert len(act_names) == 16 * ntet == 128
IDX = {nm: i for i, nm in enumerate(act_names)}


def parse(nm):
    m = re.match(r'^c_(\d)(\d)(\d)(\d)_(\d+)$', nm)
    return tuple(int(m.group(i)) for i in range(1, 5)), int(m.group(5))


def cname(t, tet):
    return f"c_{''.join(map(str, t))}_{tet}"


# ----------------------------------------------------------- the point on all 128
def expand_point(canon, u):
    """All 128 non-vertex coordinates from the canonical ones, via snappy's
    canonical_representative (sign, u-power, canonical variable or the literal 1)."""
    out = {}
    for nm in act_names:
        s, p, var = V.canonical_representative[nm]
        base = ONE if var == 1 else canon[var]
        out[nm] = kmul(K(sp.Integer(s)) * kpow(u, p), base)
    return out


X = expand_point(co, u2)
assert all(not x.is_zero for x in X.values()), "a coordinate vanishes; D is undefined"


def ptolemy_relation_failures(P):
    """GGZ (5.2) on every tetrahedron: for each vertex i, with e_i the unit index,
    c_{e_i+e_0+e_1} c_{e_i+e_2+e_3} - c_{e_i+e_0+e_2} c_{e_i+e_1+e_3}
    + c_{e_i+e_0+e_3} c_{e_i+e_1+e_2} = 0   (vertex coordinates c_{3000} = 1)."""
    def val(t, tet):
        if max(t) == 3:
            return ONE
        return P[cname(t, tet)]

    def add(*ts):
        return tuple(sum(v) for v in zip(*ts))

    E = [tuple(int(i == j) for j in range(4)) for i in range(4)]
    bad = []
    for tet in range(ntet):
        for i in range(4):
            b = E[i]
            expr = (val(add(b, E[0], E[1]), tet) * val(add(b, E[2], E[3]), tet)
                    - val(add(b, E[0], E[2]), tet) * val(add(b, E[1], E[3]), tet)
                    + val(add(b, E[0], E[3]), tet) * val(add(b, E[1], E[2]), tet))
            if not K(expr).is_zero:
                bad.append((tet, i))
    return bad


bad = ptolemy_relation_failures(X)
assert not bad, f"corpus point violates GGZ (5.2) on {bad}"
print(f"corpus point: all {4 * ntet} per-tetrahedron Ptolemy relations hold exactly in K")


def identification_failures(P, u):
    """Face/edge identifications c_{t,tet} = sign * u^pow * c_{canonical}, read off the
    UNFIXED variety so every class member is compared with a genuine coordinate."""
    bad = []
    for nm in act_names:
        s, p, var = V0.canonical_representative[nm]
        if not K(P[nm] - kmul(K(sp.Integer(s)) * kpow(u, p), P[var])).is_zero:
            bad.append(nm)
    return bad


assert not identification_failures(X, u2)
print(f"corpus point: all 128 identifications hold at u = u2; "
      f"{len(identification_failures(X, u1))} fail at u = u1 (it is a P^c point)")

# -------------------------------------------------------------------- duality D
SWAP = {0: 0, 1: 2, 2: 1, 3: 3}


def dual_point(P):
    """D on every non-vertex coordinate of every tetrahedron.

    {2,1,0,0}:  D_t = x_{pi(t)},  pi = entrywise 1<->2, sign +1 (derived below, and
                checked on random SL(3) decorations in `check_duality_formulas`).
    {1,1,1,0}, zero at vertex j:  for EVERY choice of an omitted column-vertex k,
                D_t * x_{s(k)} = det[ x_{2 at i, 1 at m} ]_{i != j, m != k}   (0 if i = m),
                s(k) = 1 at the vertices != k.  All four k are computed and must agree.
    """
    out = {}
    for nm in act_names:
        t, tet = parse(nm)
        if sorted(t) == [0, 0, 1, 2]:
            out[nm] = P[cname(tuple(SWAP[v] for v in t), tet)]
        else:
            assert sorted(t) == [0, 1, 1, 1]
            j = t.index(0)
            vals = []
            for k in range(4):
                rows = [i for i in range(4) if i != j]
                cols = [m for m in range(4) if m != k]
                mat = [[ZERO if i == m else
                        P[cname(tuple(2 if v == i else 1 if v == m else 0 for v in range(4)), tet)]
                        for m in cols] for i in rows]
                s = tuple(0 if v == k else 1 for v in range(4))
                xs = ONE if max(s) == 3 else P[cname(s, tet)]
                vals.append(kmul(kdet3(mat), kinv(xs)))
            for v in vals[1:]:
                assert K(v - vals[0]).is_zero, f"the four (1,3) forms disagree on {nm}"
            out[nm] = vals[0]
    return out


def check_duality_formulas(trials=25, seed=7092):
    """Exact guard for D's formulas AND signs on random SL(3) decorations over Q:
    c_t = det of the column groups (GGZ Lemma 8.8), g* = (v1 x v2, v1 x v3, v2 x v3)."""
    rng = random.Random(seed)

    def det3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

    def cols(g):
        return [[g[r][c] for r in range(3)] for c in range(3)]

    def cross(a, b):
        return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]

    def rand_sl3():
        while True:
            g = [[Fraction(rng.randint(-6, 6)) for _ in range(3)] for _ in range(3)]
            dt = det3(g)
            if dt:
                for r in range(3):
                    g[r][2] /= dt
                assert det3(g) == 1
                return g

    def ptolemy(dec, t):
        colv = []
        for v in range(4):
            colv += cols(dec[v])[:t[v]]
        return det3([[colv[c][r] for c in range(3)] for r in range(3)])

    def dual(g):
        v1, v2, v3 = cols(g)
        w = [cross(v1, v2), cross(v1, v3), cross(v2, v3)]
        return [[w[c][r] for c in range(3)] for r in range(3)]

    shapes = [t for t in __import__('itertools').product(range(3), repeat=4)
              if sum(t) == 3 and max(t) < 3]
    assert len(shapes) == 16
    for _ in range(trials):
        dec = [rand_sl3() for _ in range(4)]
        ddec = [dual(g) for g in dec]
        assert all(det3(g) == 1 for g in ddec)
        c = {t: ptolemy(dec, t) for t in shapes}
        cs = {t: ptolemy(ddec, t) for t in shapes}
        for t in shapes:
            if sorted(t) == [0, 0, 1, 2]:
                assert cs[t] == c[tuple(SWAP[v] for v in t)], (t, cs[t], c)
            else:
                j = t.index(0)
                for k in range(4):
                    rows = [i for i in range(4) if i != j]
                    colsk = [m for m in range(4) if m != k]
                    mat = [[Fraction(0) if i == m else
                            c[tuple(2 if v == i else 1 if v == m else 0 for v in range(4))]
                            for m in colsk] for i in rows]
                    s = tuple(0 if v == k else 1 for v in range(4))
                    assert cs[t] * c[s] == det3(mat), (t, k)
    return trials


ntr = check_duality_formulas()
print(f"duality formulas (12 relabellings with sign +1, 4 x 4 determinant forms): "
      f"exact on {ntr}/{ntr} random SL(3) decorations")

DX = dual_point(X)
bad = ptolemy_relation_failures(DX)
assert not bad, f"D(x) violates GGZ (5.2) on {bad}"
idf1, idf2 = identification_failures(DX, u1), identification_failures(DX, u2)
print(f"D(x): all {4 * ntet} Ptolemy relations hold; identifications: "
      f"{len(idf1)} fail at u1, {len(idf2)} fail at u2  "
      f"({'D(x) is a P^-c point' if not idf1 and idf2 else 'UNEXPECTED'})")
assert not idf1 and idf2

# ------------------------------------------------------------ gauge exponent matrices
A_TORUS = [[int(v) for v in row] for row in act_rows]        # 128 x 6, snappy's action
TORUS_COLS = list(act_cols)
A_SCALAR = []                                                 # 128 x 3, lambda_v^{t_i}
for nm in act_names:
    t, tet = parse(nm)
    row = [0] * ncusp
    for v in range(4):
        row[cusp_of[tet][v]] += t[v]
    A_SCALAR.append(row)
SCALAR_COLS = [f'lambda_on_cusp_{k}' for k in range(ncusp)]
# A': the 32 vertex coordinates c_{3000..0003} = 1, on which the scalar gauge acts by lambda^3
VERTEX_NAMES, A_VERTEX = [], []
for tet in range(ntet):
    for v in range(4):
        VERTEX_NAMES.append(cname(tuple(3 if w == v else 0 for w in range(4)), tet))
        row = [0] * ncusp
        row[cusp_of[tet][v]] = 3
        A_VERTEX.append(row)

# sanity: snappy's torus rows are what the GGZ action says they are
for nm, row in zip(act_names, A_TORUS):
    t, tet = parse(nm)
    exp = {}
    for v in range(4):
        cp = cusp_of[tet][v]
        for lev in range(2):                       # diagonal entries 0 and 1 (2 is dependent)
            exp[(lev, cp)] = exp.get((lev, cp), 0) + (1 if t[v] >= lev + 1 else 0)
        # entry 2 = 1/(d0 d1): t_v = 3 never occurs on these rows
        assert t[v] <= 2
    for ci, cn in enumerate(TORUS_COLS):
        lev, cp = int(cn.split('_')[2]), int(cn.split('_')[-1])
        assert row[ci] == exp.get((lev, cp), 0), (nm, cn)
print("snappy's decoration-change matrix agrees with the GGZ torus action row by row")


# ------------------------------------------------------- integer kernel + solving
def egcd(a, b):
    if b == 0:
        return (abs(a), (1 if a > 0 else -1), 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)


def column_reduce(Mrows):
    """Unimodular column reduction of an integer matrix M (k x n): returns (H, U) with
    M U = H, U in GL_n(Z), H in column echelon form.  Columns of U over the zero columns
    of H are a Z-basis of ker(M) = {m : M m = 0}."""
    k, n = len(Mrows), len(Mrows[0])
    H = [list(r) for r in Mrows]
    U = [[int(i == j) for j in range(n)] for i in range(n)]

    def colop(j1, j2, a, b, c, dd):        # (col j1, col j2) <- (a col j1 + b col j2, c col j1 + dd col j2)
        for Mx in (H, U):
            for r in Mx:
                x, y = r[j1], r[j2]
                r[j1], r[j2] = a * x + b * y, c * x + dd * y

    piv = 0
    pivots = []
    for i in range(k):
        for j in range(piv + 1, n):
            if H[i][j] != 0:
                if H[i][piv] == 0:
                    colop(piv, j, 0, 1, 1, 0)
                    continue
                g, s, t = egcd(H[i][piv], H[i][j])
                a, b = H[i][piv] // g, H[i][j] // g
                # new piv col = s*piv + t*j (entry g); new j col = -b*piv + a*j (entry 0); det = 1
                colop(piv, j, s, t, -b, a)
        if piv < n and H[i][piv] != 0:
            if H[i][piv] < 0:
                for Mx in (H, U):
                    for r in Mx:
                        r[piv] = -r[piv]
            pivots.append((i, piv))
            piv += 1
    for r in H:
        assert all(v == 0 for v in r[piv:])
    return H, U, pivots


def kernel_basis(A):
    """Z-basis of {m in Z^rows : m^T A = 0} for A given as a list of rows."""
    k = len(A[0])
    Mt = [[A[r][c] for r in range(len(A))] for c in range(k)]        # k x n
    H, U, pivots = column_reduce(Mt)
    rank = len(pivots)
    n = len(A)
    ker = [[U[r][j] for r in range(n)] for j in range(rank, n)]
    for m in ker:
        assert all(sum(m[r] * A[r][c] for r in range(n)) == 0 for c in range(k))
    Hsq = [[H[i][j] for j in range(rank)] for i in range(k)]
    return ker, rank, Hsq, U, pivots


def prod_pow(vals, m):
    r = ONE
    for v, e in zip(vals, m):
        if e:
            r = kmul(r, kpow(v, e))
    return r


def coboundary_test(label, A, cols, names, ratio, ratio_vertex=None):
    """The full decision for one ansatz.  Returns a dict for the witness."""
    rows = list(A)
    nms = list(names)
    vals = [ratio[n] for n in nms]
    if ratio_vertex is not None:                  # ansatz A': append the vertex rows
        rows += A_VERTEX
        nms += VERTEX_NAMES
        vals += [ratio_vertex[n] for n in VERTEX_NAMES]
    ker, rank, Hsq, U, pivots = kernel_basis(rows)
    k = len(cols)
    # index of the row lattice in Z^k: |det| of the k x rank echelon block (rank == k here)
    index = None
    if rank == k:
        index = abs(int(sp.Matrix(Hsq).det()))
    fails = []
    for m in ker:
        p = prod_pow(vals, m)
        if not K(p - 1).is_zero:
            fails.append((m, p))
    out = {
        'ansatz': label, 'gauge_parameters': cols, 'rows': len(rows), 'rank': rank,
        'kernel_rank': len(ker), 'row_lattice_index_in_Zk': index,
        'kernel_relations_failing': len(fails),
    }
    print(f"\n[{label}]  {len(rows)} coordinates, {k} gauge parameters, rank {rank}, "
          f"kernel rank {len(ker)}, row-lattice index {index}")
    if fails:
        m, p = fails[0]
        support = [(nms[i], m[i]) for i in range(len(m)) if m[i]]
        cube = K(p ** 3 - 1).is_zero
        ru6 = K(p ** 6 - 1).is_zero
        print(f"   NOT A COBOUNDARY: {len(fails)} of {len(ker)} kernel relations have product != 1")
        print(f"   first obstructing relation (coordinate, exponent): {support}")
        print(f"   its product in K: {kstr(p)}")
        print(f"   product is a cube root of unity: {cube}; a 6th root of unity: {ru6}")
        out.update({'verdict': 'NOT a coboundary',
                    'obstructing_relation': support, 'obstructing_product': kstr(p),
                    'obstructing_product_is_cube_root_of_unity': cube,
                    'all_failing_products_roots_of_unity_order_dividing_6':
                        all(K(q ** 6 - 1).is_zero for _, q in fails)})
        return out, None
    print(f"   every kernel relation has product exactly 1 in K -- r is a homomorphism on the row lattice L")
    out['coboundary_on_row_lattice'] = True
    n = len(vals)
    Hm = sp.Matrix(Hsq)                                  # k x rank, rank == k here

    def phi(ell):
        """r evaluated on a lattice vector ell in L: find integer m with m^T A = ell via the
        unimodular reduction (M U = [H|0] => ell = H c, m = U[:, :rank] c), return prod r^m."""
        c = Hm.solve(sp.Matrix(ell))
        assert all(ci.is_integer for ci in c), f"{ell} is not in the row lattice"
        m = [sum(U[r][j] * int(c[j]) for j in range(rank)) for r in range(n)]
        assert [sum(m[r] * rows[r][cc] for r in range(n)) for cc in range(k)] == list(ell)
        return prod_pow(vals, m)

    if index == 1:
        dparams = [phi([int(i == j) for i in range(k)]) for j in range(k)]
        out['extension'] = 'row lattice is all of Z^k; gauge element unique'
    else:
        # L has index `index` in Z^k.  Here every row has entry-sum 3 (the centre mu_3 of
        # SL(3) acts trivially on Ptolemy coordinates), so L = {e : sum e = 0 mod 3},
        # index 3, and Z^k = L + Z e_0.  A gauge element over K exists iff w := r(3 e_0)
        # has a CUBE ROOT in K: then d_0 = w^(1/3) and d_j = d_0 * r(e_j - e_0).
        assert index == 3 and all(sum(rw) % 3 == 0 for rw in rows), "unexpected lattice"
        # The group that ACTS on Ptolemy coordinates is T_SL / mu_3 = T_PGL(3), whose character
        # lattice is exactly L.  So r in Hom(L, K^x) = T_PGL(3)(K) IS a gauge element over K
        # of the PGL(3) decoration torus.  Record it on a Z-basis of L and re-verify every row.
        e0 = [3] + [0] * (k - 1)
        basis = [e0] + [[int(i == j) - int(i == 0) for i in range(k)] for j in range(1, k)]
        tpgl = {f"r({'+'.join(f'{c}*e{i}' for i, c in enumerate(b) if c)})": kstr(phi(b)) for b in basis}
        nbad = sum(1 for rw, v in zip(rows, vals) if not K(phi(rw) - v).is_zero)
        assert nbad == 0, f"{nbad} rows fail against the lattice homomorphism -- internal error"
        print(f"   T_PGL(3)(K) gauge element (values of r on a Z-basis of L):")
        for kk, vv in tpgl.items():
            print(f"      {kk} = {vv}")
        print(f"   all {len(rows)} equations re-verified exactly from it")
        out.update({'pgl3_gauge_element_on_L_basis': tpgl, 'equations_verified': len(rows)})
        w = phi(e0)
        out['w_eq_r_of_3e0'] = kstr(w)
        alpha = sp.CRootOf(f.as_expr(), 0)
        Y = sp.Symbol('Y')
        t0 = time.monotonic()
        fl = sp.Poly(Y ** 3 - w.as_expr().subs(T, alpha), Y, extension=alpha).factor_list()[1]
        lin = [fac for fac, _ in fl if fac.degree() == 1]
        print(f"   L has index 3 in Z^{k}; w = r(3 e_0) = {kstr(w)}")
        print(f"   Y^3 - w over K factors into degrees {[fac.degree() for fac, _ in fl]} "
              f"({time.monotonic() - t0:.0f} s, exact algebraic-field factorisation)")
        if not lin:
            print(f"   w is NOT a cube in K: the PGL(3) gauge element does not LIFT to a diagonal SL(3)")
            print(f"   matrix over K (it does over K(w^(1/3))).  Verdict: COBOUNDARY of the PGL(3)")
            print(f"   decoration torus over K; not of the SL(3) torus over K.")
            out.update({'verdict': 'coboundary of the PGL(3) decoration torus over K (r in Hom(L,K^x), all 128 '
                                   'equations verified); the SL(3) lift needs the cube root of r(3 e_0), '
                                   'which is not in K',
                        'w_is_cube_in_K': False})
            return out, None
        # root of the linear factor Y - rho (monic up to unit)
        fac = lin[0]
        co_ = fac.all_coeffs()
        rho_alpha = sp.simplify(-co_[1] / co_[0])
        rho = K(sp.expand(rho_alpha.subs(alpha, T)))
        assert K(rho ** 3 - w).is_zero, "cube root does not verify"
        out['w_is_cube_in_K'] = True
        dparams = [None] * k
        dparams[0] = rho
        for j in range(1, k):
            ej = [int(i == j) - int(i == 0) for i in range(k)]
            dparams[j] = kmul(rho, phi(ej))
        out['extension'] = ('row lattice has index 3; cube root of r(3 e_0) exists in K, so a gauge '
                            'element exists over K (unique up to the mu_3 centre)')
    # verify every equation
    nbad = 0
    for nm, row, v in zip(nms, rows, vals):
        if not K(prod_pow(dparams, row) - v).is_zero:
            nbad += 1
    assert nbad == 0, f"{nbad} equations fail after solving -- internal error"
    print(f"   COBOUNDARY: gauge element found and all {len(rows)} equations re-verified exactly")
    for cn, dv in zip(cols, dparams):
        print(f"      {cn} = {kstr(dv)}")
    out.update({'verdict': 'coboundary', 'gauge_element': {cn: kstr(dv) for cn, dv in zip(cols, dparams)},
                'equations_verified': len(rows)})
    return out, dparams


# ------------------------------------------------------------- the ratios, and run
results = {}
ratio_by_sigma = {}
for snm, g in SIGMA.items():
    SX = {nm: sig_apply(X[nm], g) for nm in act_names}
    assert not identification_failures(SX, u1)       # sigma(x) is a P^-c point too
    assert not ptolemy_relation_failures(SX)
    r = {nm: kmul(SX[nm], kinv(DX[nm])) for nm in act_names}
    r_vertex = {nm: ONE for nm in VERTEX_NAMES}      # sigma(1)/D(1) = 1/1
    ratio_by_sigma[snm] = r
    print(f"\n==================== {snm} ====================")
    ncls = len({kstr(v) for v in r.values()})
    print(f"ratio sigma(x)/D(x): {ncls} distinct values over the 128 coordinates "
          f"({sum(1 for v in r.values() if K(v - 1).is_zero)} equal to 1)")
    res = {}
    res['B_torus'], _ = coboundary_test('B: GGZ decoration torus (2 params / cusp)',
                                        A_TORUS, TORUS_COLS, act_names, r)
    res['A_scalar'], _ = coboundary_test('A: scalars lambda_v^{t_i} (issue #7092 as written)',
                                         A_SCALAR, SCALAR_COLS, act_names, r)
    res["A_scalar_with_vertex_coords"], _ = coboundary_test(
        "A': scalars, vertex coordinates c_3000 = 1 included (forces lambda_v^3 = 1)",
        A_SCALAR, SCALAR_COLS, act_names, r, ratio_vertex=r_vertex)
    results[snm] = res

# ----------------------------------------------------- guards on the machinery
# (1) a PURE gauge must be a coboundary under B: kernel products of g.x / x are all 1
rng = random.Random(1)
gauge = [K(sp.Rational(rng.randint(2, 9), rng.randint(2, 9))) for _ in TORUS_COLS]
GX = {nm: kmul(X[nm], prod_pow(gauge, row)) for nm, row in zip(act_names, A_TORUS)}
assert not ptolemy_relation_failures(GX) and not identification_failures(GX, u2)
pure = {nm: kmul(GX[nm], kinv(X[nm])) for nm in act_names}
ker_B, *_ = kernel_basis(A_TORUS)
assert all(K(prod_pow([pure[n] for n in act_names], m) - 1).is_zero for m in ker_B)
# (2) the verdict is GAUGE-INVARIANT: recompute the kernel products from g.x instead of x
print("\nguards:")
for snm, g in SIGMA.items():
    SGX = {nm: sig_apply(GX[nm], g) for nm in act_names}
    DGX = dual_point(GX)
    r2 = {nm: kmul(SGX[nm], kinv(DGX[nm])) for nm in act_names}
    for m in ker_B:
        p1 = prod_pow([ratio_by_sigma[snm][n] for n in act_names], m)
        p2 = prod_pow([r2[n] for n in act_names], m)
        assert K(p1 - p2).is_zero
print(f"   pure gauge g.x/x: all {len(ker_B)} torus kernel products are 1  (matrix and kernel are right)")
print(f"   kernel products of sigma(x)/D(x) unchanged under a random exact gauge of x  "
      f"(verdict is independent of the elimination gauge)")

# (3) the elimination gauge of P^c vs P^-c
c_cls = list(V._obstruction_class.H2_class)
Vn = M.ptolemy_variety(N, obstruction_class=OC([(-x) % N for x in c_cls]), eliminate_fixed_ptolemys=True)
elim_n = sorted(set(V0.variables) - set(Vn.variables))
diff = [(k, V.canonical_representative[k], Vn.canonical_representative[k])
        for k in V.canonical_representative if V.canonical_representative[k] != Vn.canonical_representative[k]]
same_elim = elim_n == ELIM
only_upow = all(a[0] == b[0] and a[2] == b[2] for _, a, b in diff)
print(f"   elimination gauge P^c vs P^-c: same {len(ELIM)} eliminated coordinates: {same_elim}; "
      f"{len(diff)} canonical representatives differ, all by u-power only: {only_upow}")

# ----------------------------------------------------------------------- witness
verdicts = {s: {a: results[s][a]['verdict'] for a in results[s]} for s in results}
all_passed = True
payload = {
    'description': ("#7092: is sigma(x)/D(x) a gauge coboundary on the exact L6a4 class-1 Ptolemy "
                    "point?  Decided by the Z-kernel of the gauge exponent lattice, exactly in "
                    "K = Q[T]/(f).  Three ansaetze: B = GGZ decoration torus (the gauge of the "
                    "variety), A = per-cusp scalars as the issue is written, A' = A with the vertex "
                    "coordinates included.  Scope: point-level fact about this point; not an identity "
                    "of maps; says nothing yet about the representation-level induction (qou-qjhc)."),
    'manifold': NAME, 'obstruction_class': KCLS,
    'triangulation_isosig': M.triangulation_isosig(decorated=False),
    'snappy_version': snappy.__version__,
    'field': d['field'],
    'point_source': POINT_FILE.name,
    'coordinates_total_nonvertex': len(act_names), 'coordinates_canonical': len(co),
    'coordinates_eliminated_by_snappy': ELIM,
    'elimination_gauge_same_for_negated_class': same_elim,
    'elimination_gauge_differs_only_by_u_power': only_upow,
    'sigma': {k: str(v) for k, v in SIGMA.items()},
    'galois_group': 'Z/2 x Z/2 (sigma_a^2 = sigma_b^2 = 1; tau = sigma_a sigma_b fixes Q(zeta_3))',
    'duality_formula_guard_trials': ntr,
    'D_of_x_is_P_minus_c_point': {'identification_failures_at_u1': len(idf1),
                                  'identification_failures_at_u2': len(idf2)},
    'results': results,
    'verdicts': verdicts,
    'guards': {'pure_gauge_kernel_products_all_one': True,
               'verdict_gauge_invariant': True},
    'exact_arithmetic': 'K = Q[T]/(f), sympy Poly over QQ; no floats, no tolerances',
    'allPassed': all_passed,
}
b = WitnessBuilder.wrap_legacy('ptolemy-duality-sigma-coboundary-test', payload,
                               script_path=__file__, engine='sympy+snappy',
                               engine_version=f"sympy {sp.__version__}, snappy {snappy.__version__}",
                               output_dir=HERE, start_time=_T0)
out = b.save({"q0Anchor": "independent",
              "q0AnchorReason": "Pure algebra over K = Q[T]/(f), the class-1 Ptolemy field: "
                                "no substrate q0 is read, computed or compared anywhere in this probe."})
print(f"\nverdicts: {json.dumps(verdicts, indent=1)}")
print(f"witness -> {out}")
