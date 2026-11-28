#!/usr/bin/env python3
"""qbeta_g3_stokes_from_3d_index_52.py — the 5₂ Stokes matrix S⁺(x;q), and its
q→0 Stokes constants 4 and 3, computed FROM THE TRIANGULATION 3d INDEX
(bean qou-vr3q, the cross-knot test named in
docs/audits/2026-11-27-aomega-stokes-constant-from-3d-index.md §"Still open" 3).

Companion of `qbeta_g3_stokes_from_3d_index_41.py` (4₁, merged in #9849).

Chain (all from the in-repo GGM source
library/arxiv-2012.00062v3/source/files/GGM_peacock_20v4.tex):

  (a) eq (Sp-52), conj. 5₂ region matrices — the Stokes matrix
        S⁺(x;q) = P · W₋₁(x⁻¹;q⁻¹) · W₋₁(x;q)ᵀ · Q,
        P = [[0,1,0],[0,1,1],[-1,0,0]],  Q = [[0,0,-1],[1,1,0],[0,1,0]].
  (b) eq (Wmatrec), m = -1 (proved):  W₀ = K·W₋₁,
        K(x;q) = [[0,1,0],[0,0,1],[1,-s(x),s(x)-q]],  s(x) = x+x⁻¹+1.
  (c) eq (W52xm), m = 0 (proved):  𝒲₀ = M₀·W₀, M₀ the printed 3×3 matrix.
  (d) eq (eq:WW52): (𝒲₀(x⁻¹;q⁻¹)·𝒲₀(x;q)ᵀ)_{ij}
        = Σ_α B^α(q^{-i}x⁻¹;q⁻¹) B^α(q^j x;q),   B^α = (A₀, B₀, C₀)
      (GGM eqs Am, Bm, Cm, H52p, H52n), which GGM identify with the rotated
      index Ind^rot(j-i, q^{(i+j)/2}x; q), up to block normalisation
      (their footnote gives the Beem-convention form).

Hence S⁺ = L · Bil · R with L = P·K(x⁻¹;q⁻¹)⁻¹·M₀(x⁻¹;q⁻¹)⁻¹ and
R = M₀(x;q)⁻ᵀ·K(x;q)⁻ᵀ·Q, computed here symbolically from (a)-(c).

The block-to-index dictionary is MEASURED, not chosen
--------------------------------------------------------
Earlier attempts with the 4₁ prefactor (-q^{1/2})^{j-i} and with GGM's
footnote form did not give the printed S⁺(x;0).  Instead of trying further
conventions against that target, check B1 evaluates GGM's holomorphic blocks
numerically (mpmath, 40 digits, |q| < 1, the q⁻¹ side through H⁻ and
θ(x;q⁻¹) = θ(x;q)⁻¹) and compares the block bilinear with the index of the
SnapPy triangulation m015 (= 5₂; `half_class_3d_index.HalfIndex`, the GHRS
index at DGG's half-longitude classes).  The result is

    Bil_{ij} = e_i · Ind^rot(j-i, q^{(i+j)/2} x; q) / e_j,   e_k = (-q^k x²)^k,

i.e. GGM's main-text form conjugated by the diagonal E = diag(e_k).  It holds
to the working precision at several (x, q).  B2 checks, also numerically and
independently of any index, that L·Bil·R equals GGM's W-route
P·W₋₁(x⁻¹;q⁻¹)·W₋₁(x;q)ᵀ·Q.  So the gauge transcription is right.

Then S⁺(x;q) = L · E · N · E⁻¹ · R with N_{ij} = Ind^rot(j-i, q^{(i+j)/2}x; q),
assembled in exact integer Laurent arithmetic in (x, s), s = q^{1/2}.

Checks (exact unless marked numeric; any failure exits 1):
  B1  (numeric) block bilinear = E·N·E⁻¹ from the m015 index
  B2  (numeric) L·Bil·R = GGM W-route Stokes matrix, det = 1
  C1  S⁺(x;0) = [[1, s+1, 0],[0,1,0],[-s, -s², 1]]    (GGM eq S0px52)
  C2  S⁺₁₁(x;q) = Ind^rot(0,x;q) exactly (L row 1 and R column 1 are e₁)
  C3  GGM's printed 𝒮⁺_{σ₁σ₁}(x;q) = S⁺₁₁ - 1 through q²
  C4  det S⁺(x;q) = 1 through the truncation order
  C5  x = 1: equal to the W-route S⁺(q) of `qbeta_g3_5two_stokes_sandwich`
      (GGM 2007.10190, an independent W-series computation) coefficient by
      coefficient
  C6  no half-integer q-power survives in S⁺ (odd flux carries s^odd in N)
  C7  stability under a larger charge cutoff

No measured value enters any step, and nothing is fitted.  The one
normalisation (E) is an identity measured to 40 digits between two
independently defined objects, not a parameter.

-- Ref: [garoufalidis-gu-marino2023peacock] GGM 2012.00062 (eq Sp-52, Wmatrec, W52xm, WW52, S0px52)
-- Ref: [garoufalidis-gu-mariño2021] GGM 2007.10190 (W-route S⁺(q) at x = 1)
-- Ref: [dimofte-gaiotto-gukov2013] DGG 1112.5179 (3d index)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import _path_bridge as _bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qbeta_g3_stokes_from_3d_index_41 import add, mul, trunc, mono, lp, P_  # noqa: E402

D_S = 12          # keep s-degrees ≤ D_S in S⁺ (q⁶)
PAD = 14          # extra s-order in N (E⁻¹ and L carry negative s-powers)
E_MAX = 22        # electric-charge cutoff (C7 re-runs at E_MAX + 4; 16 is short at q⁵)
M_RANGE = range(-2, 3)

# ---------------------------------------------------------------- index ----

_TAB: dict = {}


def _half_index():
    import snappy
    from half_class_3d_index import HalfIndex
    return HalfIndex(snappy.Manifold("m015"))


def index_table(smax, emax):
    """I(m,e) as {s-power: int} for m ∈ M_RANGE, |e| ≤ emax, s-degree ≤ smax+2|e|·2."""
    key = (smax, emax)
    if key in _TAB:
        return _TAB[key]
    h = _half_index()
    tab = {}
    for m in M_RANGE:
        for e in range(-emax, emax + 1):
            need = smax + 4 * abs(e) + 8          # ζ = s^{i+j}x reaches s^{-4|e|}
            qcap = need // 2 + 1
            rmax = 2 * (abs(e) + abs(m)) + 10
            ser = h.index(e, m, qcap, rmax=rmax)
            tab[(m, e)] = {k: v for k, v in ser.items() if v and k <= need}
    _TAB[key] = tab
    return tab


def ind_rot(tab, m, shift, emax):
    """Ind^rot(m, s^shift x; q) = Σ_e I(m,e) s^{shift·e} x^e (untruncated)."""
    out: dict = {}
    for e in range(-emax, emax + 1):
        for k, v in tab.get((m, e), {}).items():
            kk = (e, k + shift * e)
            out[kk] = out.get(kk, 0) + v
    return {k: c for k, c in out.items() if c}


def conj_index_matrix(tab, emax, dmax):
    """(E N E⁻¹)_{ij} = (-1)^{i-j} s^{2(i²-j²)} x^{2(i-j)} Ind^rot(j-i, s^{i+j}x; q)."""
    out = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            m = j - i
            pre = mono(2 * (i - j), 2 * (i * i - j * j), (-1) ** ((i - j) % 2))
            out[i][j] = mul(pre, ind_rot(tab, m, i + j, emax), dmax)
    return out


# --------------------------------------------------------------- gauge ----

X, Q, S = sp.symbols("x q s")


def s_of(x):
    return x + 1 / x + 1


def K_mat(x, q):
    """GGM eq (Wmatrec) at m = -1."""
    return sp.Matrix([[0, 1, 0], [0, 0, 1], [1, -s_of(x), s_of(x) - q]])


def M0_mat(x, q, m=0):
    """GGM eq (W52xm), the printed 3×3 matrix M_m(x;q), at m = 0."""
    r = sp.zeros(3, 3)
    r[0, 0] = 1
    r[1, 0] = -q**(-1 - m) * (1 - q**(1 + m) - q * x**2)
    r[1, 1] = q**(-1 - m) / x * (1 - q**(1 + m) + x + (-q + q**(2 + m)) * x**2 - q * x**3)
    r[1, 2] = -q**(-1 - m) / x * (1 - q * x**2)
    r[2, 0] = q**(-5 - 2 * m) * x**-3 * (
        1 + (-q + q**(2 + m)) * x - (q + q**2 + q**3) * x**2
        + (q**2 + q**3 + q**4 - q**(3 + m) - 2 * q**(4 + m) - q**(5 + m) + q**(5 + 2 * m)) * x**3
        + (q**3 + q**4 + q**5) * x**4
        + (-q**4 - q**5 - q**6 + q**(5 + m) + q**(6 + m) + q**(7 + m)) * x**5
        - q**6 * x**6 + q**7 * x**7)
    r[2, 1] = -q**(-5 - 2 * m) * x**-4 * (1 - q * x) * (1 + q * x) * (
        1 + (1 - q + q**(2 + m)) * x + (-2 * q - q**3 + q**(2 + m)) * x**2
        + (-q + q**2 - q**3 + q**4 - 2 * q**(3 + m) - q**(4 + m) - q**(5 + m)
           + q**(4 + 2 * m) + q**(5 + 2 * m)) * x**3
        + (q**2 + 2 * q**4 - q**(3 + m) - q**(4 + m) - q**(5 + m)) * x**4
        + (q**4 - q**5 + q**(6 + m)) * x**5 - q**5 * x**6)
    r[2, 2] = q**(-5 - 2 * m) * x**-4 * (1 - q * x) * (1 + q * x) * (
        1 - q * x - (q + q**3) * x**2 + (q**2 + q**4 - q**(3 + m) - q**(4 + m)) * x**3
        + q**4 * x**4 - q**5 * x**5)
    return r


P_MAT = sp.Matrix([[0, 1, 0], [0, 1, 1], [-1, 0, 0]])
Q_MAT = sp.Matrix([[0, 0, -1], [1, 1, 0], [0, 1, 0]])


def gauge_closed():
    L = sp.simplify(P_MAT * K_mat(1 / X, 1 / Q).inv() * M0_mat(1 / X, 1 / Q).inv())
    R = sp.simplify(M0_mat(X, Q).inv().T * K_mat(X, Q).inv().T * Q_MAT)
    return L, R


def to_series(expr, dmax):
    """Rational function of (x,q) → {(x_deg, s_deg): int}, s-degree ≤ dmax."""
    lo = 20
    e = sp.series(sp.together(expr.subs(Q, S**2)), S, 0, dmax + 1).removeO()
    e = sp.expand(e * S**lo * X**40)
    out = {}
    if e == 0:
        return out
    for (ds, dx), c in sp.Poly(e, S, X).as_dict().items():
        if ds - lo <= dmax:
            out[(dx - 40, ds - lo)] = int(c)
    return out


def mat_mul(A, B, dmax):
    return [[add(*[mul(A[i][k], B[k][j], dmax) for k in range(3)]) for j in range(3)]
            for i in range(3)]


def det3(M, dmax):
    def m2(a, b, c, d):
        return add(mul(a, d, dmax), {k: -v for k, v in mul(b, c, dmax).items()})
    t1 = mul(M[0][0], m2(M[1][1], M[1][2], M[2][1], M[2][2]), dmax)
    t2 = mul(M[0][1], m2(M[1][0], M[1][2], M[2][0], M[2][2]), dmax)
    t3 = mul(M[0][2], m2(M[1][0], M[1][1], M[2][0], M[2][1]), dmax)
    return add(t1, {k: -v for k, v in t2.items()}, t3)


def stokes_from_index(L, R, dmax, emax):
    hi = dmax + PAD
    tab = index_table(hi, emax)
    Ls = [[to_series(L[i, j], hi) for j in range(3)] for i in range(3)]
    Rs = [[to_series(R[i, j], hi) for j in range(3)] for i in range(3)]
    N = conj_index_matrix(tab, emax, hi)
    Sm = mat_mul(mat_mul(Ls, N, hi), Rs, hi)
    return [[trunc(Sm[i][j], dmax) for j in range(3)] for i in range(3)], tab, Ls, Rs


# -------------------------------------------------------- numeric blocks ----

mp.mp.dps = 40


def _poch(a, q, n=None):
    p = mp.mpf(1)
    if n is not None:
        for k in range(n):
            p *= (1 - a * q**k)
        return p
    k = 0
    eps = mp.mpf(10) ** (-mp.mp.dps - 5)
    while True:
        t = a * q**k
        p *= (1 - t)
        k += 1
        if abs(t) < eps:
            return p


def _Hp(x, y, z, q, n_terms=80):
    """GGM eq (H52p)."""
    tot = mp.mpf(0)
    for n in range(n_terms):
        tot += q**(n * (n + 1)) * z**n / (_poch(q, q, n) * _poch(q * x, q, n) * _poch(q * y, q, n))
    return _poch(q * x, q) * _poch(q * y, q) * tot


def _Hm(x, y, z, q, n_terms=200):
    """GGM eq (H52n): H(x,y,z;q⁻¹) for |q| < 1."""
    tot = mp.mpf(0)
    for n in range(n_terms):
        tot += ((-1)**n * q**(mp.mpf(n * (n + 1)) / 2) * x**(-n) * y**(-n) * z**n
                / (_poch(q, q, n) * _poch(q / x, q, n) * _poch(q / y, q, n)))
    return tot / (_poch(x, q) * _poch(y, q))


def _theta(y, q):
    return _poch(-mp.sqrt(q) * y, q) * _poch(-mp.sqrt(q) / y, q)


def blocks(x, q, inverse, m=0):
    """(A_m, B_m, C_m)(x; q) (inverse=False) or (x; q⁻¹) (inverse=True), |q| < 1.
    GGM eqs (Am), (Bm), (Cm); θ(y;q⁻¹) = θ(y;q)⁻¹."""
    if inverse:
        def H(a, b, c): return _Hm(a, b, c, q)
        qq = 1 / q
        def T(y): return 1 / _theta(y, q)
    else:
        def H(a, b, c): return _Hp(a, b, c, q)
        qq = q
        def T(y): return _theta(y, q)
    r = mp.sqrt(qq)
    A = H(x, 1 / x, qq**m)
    B = T(-r * x)**(-2) * x**m * H(x, x**2, qq**m * x**2)
    C = T(-x / r)**(-2) * x**(-m) * H(1 / x, x**-2, qq**m * x**-2)
    return [A, B, C]


def block_bilinear(x, q):
    """GGM eq (eq:WW52): Σ_α B^α(q^{-i}x⁻¹;q⁻¹) B^α(q^j x;q)."""
    return mp.matrix([[sum(a * b for a, b in zip(blocks(q**(-i) / x, q, True), blocks(q**j * x, q, False)))
                       for j in range(3)] for i in range(3)])


def num_index(tab, m, zeta, q, emax):
    s = mp.sqrt(q)
    tot = mp.mpf(0)
    for e in range(-emax, emax + 1):
        for k, v in tab.get((m, e), {}).items():
            tot += v * s**k * zeta**e
    return tot


# ----------------------------------------------------------------- main ----


def main() -> int:
    ok = {}
    print("=" * 78)
    print(" 5₂ Stokes matrix S⁺(x;q) from the m015 3d index (qou-vr3q)")
    print("=" * 78)
    L, R = gauge_closed()
    print("L row 1:", list(L.row(0)), " R column 1:", list(R.col(0)))

    S_, tab, Ls, Rs = stokes_from_index(L, R, D_S, E_MAX)

    # B1: block bilinear = E N E⁻¹ (numeric)
    pts = [(mp.mpc(mp.mpf(7) / 10, mp.mpf(2) / 10), mp.mpf(10)**-7),
           (mp.mpc(mp.mpf(-1) / 2, mp.mpf(3) / 5), mp.mpf(10)**-7),
           (mp.mpc(mp.mpf(13) / 10, mp.mpf(-2) / 5), mp.mpf(10)**-6)]
    b1_worst = mp.mpf(0)
    for x, q in pts:
        Bm = block_bilinear(x, q)
        s = mp.sqrt(q)
        for i in range(3):
            for j in range(3):
                ei = (-q**i * x**2)**i
                ej = (-q**j * x**2)**j
                pred = ei / ej * num_index(tab, j - i, s**(i + j) * x, q, E_MAX)
                b1_worst = max(b1_worst, abs(Bm[i, j] / pred - 1))
    # truncation of N at s^{D_S+PAD} leaves a relative error ≪ q^{(D_S+PAD)/2-6}
    ok["B1_block_bilinear_equals_conjugated_index"] = b1_worst < mp.mpf(10)**-25
    print(f"[B1] max |Bil/(E N E⁻¹) - 1| over 3 points = {mp.nstr(b1_worst, 5)}")

    # B2: gauge, numeric, index-free
    Lf = sp.lambdify((X, Q), L, "mpmath")
    Rf = sp.lambdify((X, Q), R, "mpmath")
    Pm = mp.matrix(P_MAT.tolist())
    Qm = mp.matrix(Q_MAT.tolist())
    b2_worst = mp.mpf(0)
    det_worst = mp.mpf(0)
    for x, q in [(mp.mpc(mp.mpf(7) / 10, mp.mpf(1) / 5), mp.mpf(1) / 20),
                 (mp.mpc(mp.mpf(-1) / 2, mp.mpf(3) / 5), mp.mpf(1) / 10)]:
        W1 = mp.matrix([blocks(1 / x, q, True, m) for m in (-1, 0, 1)])
        W2 = mp.matrix([blocks(x, q, False, m) for m in (-1, 0, 1)])
        Sw = Pm * W1 * W2.T * Qm
        Si = mp.matrix(Lf(x, q).tolist()) * block_bilinear(x, q) * mp.matrix(Rf(x, q).tolist())
        b2_worst = max(b2_worst, mp.mnorm(Sw - Si, 1) / mp.mnorm(Sw, 1))
        det_worst = max(det_worst, abs(mp.det(Sw) - 1))
    ok["B2_gauge_LBilR_equals_W_route"] = b2_worst < mp.mpf(10)**-30 and det_worst < mp.mpf(10)**-30
    print(f"[B2] |W-route − L·Bil·R| / |W-route| = {mp.nstr(b2_worst, 5)},  |det − 1| = {mp.nstr(det_worst, 5)}")

    # C1: q → 0
    def q0(p):
        return {xd: c for (xd, sd), c in p.items() if sd == 0}
    sx = P_((-1, 1), (0, 1), (1, 1))
    sx2 = P_((-2, 1), (-1, 2), (0, 3), (1, 2), (2, 1))
    target = [[{0: 1}, P_((-1, 1), (0, 2), (1, 1)), {}],
              [{}, {0: 1}, {}],
              [{k: -v for k, v in sx.items()}, {k: -v for k, v in sx2.items()}, {0: 1}]]
    S0 = [[q0(S_[i][j]) for j in range(3)] for i in range(3)]
    ok["C1_Splus_x_q0_equals_GGM_S0px52"] = S0 == target
    for i in range(3):
        print(f"[C1] S⁺(x;0) row {i + 1}:", [lp(S0[i][j]) for j in range(3)])

    # C2: S11 = Ind^rot(0,x;q)
    ind0 = trunc(ind_rot(tab, 0, 0, E_MAX), D_S)
    ok["C2_S11_equals_zero_flux_index"] = (S_[0][0] == ind0
                                           and L.row(0) == sp.Matrix([[1, 0, 0]])
                                           and R.col(0) == sp.Matrix([1, 0, 0]))

    # C3: printed 𝒮⁺_{σ1σ1} = S11 - 1 through q²
    pr = {1: P_((-2, -1), (-1, -3), (0, -4), (1, -3), (2, -1)),
          2: P_((-3, 1), (-2, 1), (0, -1), (2, 1), (3, 1))}
    got = {k: {xd: c for (xd, sd), c in S_[0][0].items() if sd == 2 * k} for k in (1, 2)}
    ok["C3_printed_S11_through_q2"] = got == pr
    print("[C3] S⁺₁₁ q¹:", lp(got[1]), "  q²:", lp(got[2]))

    # C4: det = 1
    dt = det3(S_, D_S)
    ok["C4_det_Splus_eq_1"] = dt == {(0, 0): 1}
    print(f"[C4] det S⁺(x;q) = 1 through s^{D_S}: {ok['C4_det_Splus_eq_1']}")

    # C5: x = 1 against the W-route (GGM 2007.10190)
    def at1(p):
        o = [0] * (D_S // 2 + 1)
        for (xd, sd), c in p.items():
            if sd % 2 == 0 and 0 <= sd <= D_S:
                o[sd // 2] += c
        return o
    X1 = [[at1(S_[i][j]) for j in range(3)] for i in range(3)]
    try:
        import qbeta_g3_5two_stokes_sandwich as W
        Wq, Wqi = W.series_mat_raw(), W.series_mat_ext()
        Sp = W.sandwich(Wq, Wqi, W.L_P, W.R_P, first_is_qi=True)
        Wx1 = [[[int(Sp[i][j][t]) for t in range(D_S // 2 + 1)] for j in range(3)] for i in range(3)]
        ok["C5_x1_equals_W_route"] = Wx1 == X1
        if Wx1 != X1:
            print("[C5] W-route:", Wx1)
    except Exception as exc:  # pragma: no cover
        print("[C5] W-route unavailable:", exc)
        ok["C5_x1_equals_W_route"] = False
    for i in range(3):
        print(f"[C5] S⁺(1;q) row {i + 1}:", X1[i])

    # C6: integral q-powers only
    ok["C6_no_half_integer_q_powers"] = all(sd % 2 == 0 for row in S_ for p in row for (_, sd) in p)

    # C7: stability
    S2, _, _, _ = stokes_from_index(L, R, D_S, E_MAX + 4)
    ok["C7_stable_under_larger_charge_cutoff"] = S2 == S_

    # the 4 and the 3: which index coefficients reach S⁺(x;0)
    hi = D_S + PAD
    carriers = {}
    for (a, b, nm) in ((0, 1, "S12"), (2, 0, "S31")):
        rows = []
        for k in range(3):
            for l in range(3):
                m = l - k
                pre = mono(2 * (k - l), 2 * (k * k - l * l), (-1) ** ((k - l) % 2))
                for (mm, e), ser in tab.items():
                    if mm != m:
                        continue
                    for kk, v in ser.items():
                        t = mul(mul(Ls[a][k], mul(pre, mono(e, kk + (k + l) * e, v), hi), hi), Rs[l][b], hi)
                        c = {xd: cv for (xd, sd), cv in t.items() if sd == 0 and cv}
                        if c:
                            rows.append({"flux_m": m, "charge_e": e, "s_power": kk, "I": v,
                                         "via_N": [k + 1, l + 1], "contributes": {str(d): cv for d, cv in sorted(c.items())}})
        carriers[nm] = rows
        tot1 = sum(sum(r["contributes"].values()) for r in rows)
        print(f"[count] {nm}(1;0) = {tot1} from {len(rows)} index coefficients:")
        for r in rows:
            print("    ", r)

    print()
    for k, v in ok.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    allp = all(ok.values())

    verdict = ("The 5₂ Stokes matrix S⁺(x;q) is assembled from the m015 3d index through GGM's gauge "
               "(eqs Sp-52, Wmatrec, W52xm) and a block-to-index dictionary measured from GGM's own "
               "holomorphic blocks: Bil = E·N·E⁻¹, e_k = (-q^k x²)^k. It reproduces S⁺(x;0) = "
               "[[1,s+1,0],[0,1,0],[-s,-s²,1]] (GGM eq S0px52), det = 1, the printed 𝒮⁺_{σ₁σ₁} and, at x = 1, "
               "the independent W-route S⁺(q). The Stokes constants 4 = S⁺₁₂(1;0) and -3 = S⁺₃₁(1;0) are read "
               "from finitely many index coefficients; they are signed sums with cancellations, not "
               "positive state counts.")
    print("\n verdict:", verdict)

    wb = WitnessBuilder("qbeta-g3-stokes-from-3d-index-52", engine="python-int")
    wb.set_description("5₂ Stokes matrix S⁺(x;q) of GGM 2012.00062 assembled from the m015 3d index; "
                       "block-to-index normalisation measured from GGM's holomorphic blocks (bean qou-vr3q).")
    wb.add_data("source", "GGM 2012.00062 tex: eq Sp-52, Wmatrec, W52xm, eq:WW52, Am/Bm/Cm, H52p/H52n, S0px52; "
                "GGM 2007.10190 W-route at x=1; SnapPy m015")
    wb.add_data("dictionary", "Bil_ij = e_i Ind^rot(j-i, q^{(i+j)/2} x; q) / e_j, e_k = (-q^k x^2)^k")
    wb.add_data("B1_max_rel_residual", mp.nstr(b1_worst, 6))
    wb.add_data("B2_max_rel_residual", mp.nstr(b2_worst, 6))
    wb.add_data("Splus_x_q0", [[lp(S0[i][j]) for j in range(3)] for i in range(3)])
    wb.add_data("Splus_x1_q_series", X1)
    wb.add_data("index_coefficients_reaching_q0", carriers)
    wb.add_data("cutoffs", {"D_S": D_S, "PAD": PAD, "E_MAX": E_MAX})
    wb.add_data("verdict", verdict)
    for name, val in ok.items():
        wb.add_assertion(name, computed=1 if val else 0, expected=1, tolerance=0,
                         source="GGM 2012.00062 / 2007.10190; m015 index")
    wb.save()
    print(f" assertions: {sum(ok.values())}/{len(ok)} passed")
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
