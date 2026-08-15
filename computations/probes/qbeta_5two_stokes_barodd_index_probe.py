#!/usr/bin/env python3
"""A2 (bean qou-ls2y): the 5₂ Stokes matrix S⁺(q) at the substrate point — the
bar-odd (antisymmetric) Stokes datum, derived from published integer q-series.

Implements the Garoufalidis–Gu–Mariño 5₂ resurgent data (library/arxiv-2007.10190v2/2007.10190v2.pdf,
transcribed + machine-verified 2026-07-18; Peacock = library/arxiv-2012.00062v3/2012.00062v3.pdf):

  t_{n,λ}(q)  = q^{n(n+1)+nλ}/(q;q)_n³                                (GGM 113)
  T_{n,μ}(q)  = (−1)^n q^{n(n+1)/2+nμ}/(q;q)_n³                       (GGM 114)
  E_l^{(n)}(q): E1n = Σ_{s≥1} q^{s(n+1)}/(1−q^s), E2n = Σ s·q^{s(n+1)}/(1−q^s)
  p⁰=1, p¹_{n,λ}=1+2n−3E1n(n,q)+λ, p²=p¹²−1/6−3E2n(n,q)+4E2n(0,q)     (115–117)
  P⁰=1, P¹_{n,μ}=1/2+n−3E1n(n,q)+μ, P²=P¹²−1/12−3E2n(n,q)+2E2n(0,q)  (118–120)
  H±_{j,λ}(q) = Σ_n p/P j-polys × t/T                                  (112)
  W±_m(q): 3×3, entry (i,j) = H±_{j,m+i};  det W_m = 2                 (24–26)
  |q|>1 glue: W_m(Q) = antidiag(1,1,1)·W−_{−m−2}(1/Q)·diag(1,−1,1)     (25)
  S⁺(q) = ½·A⁺·W_{−1}(1/q)·B·W_{−1}(q)ᵀ·C⁺                              (29a)
  S⁻(q) = ½·A⁻·W_{−1}(q)·B·W_{−1}(1/q)ᵀ·C⁻                              (29b)
      A⁺ = [[0,1,0],[0,1,1],[−1,0,0]], B = [[0,0,1],[0,−2,0],[1,0,0]],
      C⁺ = [[0,0,−1],[1,1,0],[0,1,0]],
      A⁻ = [[0,3,−1],[0,−1,0],[1,0,0]], C⁻ = [[0,0,1],[3,−1,0],[−1,0,0]]
  Index identity: S⁺_{σ1,σ1}(q) = 2·H+_{1,0}(q)·H−_{1,0}(q)
                = 1−12q+3q²+74q³+90q⁴+O(q⁵) = Ind^rot_{5₂}(q)          (102)
  Bar glue: H+_{j,λ}(q) = (−1)^j·H−_{j,−λ}(1/q)                         (124)
  q→0 limits (eqs 100a/b): S⁺(0) = [[1,4,0],[0,1,0],[−3,−9,1]],
                           S⁻(0) = the eq-100b product
  Inversion (Conjecture 1(b), eq 4): S⁺(q)ᵀ·S⁻(q) = 1.

NOTE (learned the hard way, first run of this probe): the Peacock eq-99
"Stokes towers" S^{(k)}_{si,sj} are the per-ray factors of the ordered radar
product (GGM eq 68), NOT the entries of the assembled matrix S⁺(q) — only the
(σ1,σ1) entry coincides with a printed series (the index, eq 102). The
assembled-matrix gates are therefore: the exact q→0 limit matrices, det = 1
(SL(3)), the index entry, and the inversion relation S⁺ᵀ·S⁻ = 1 with the two
matrices assembled INDEPENDENTLY (29a vs 29b).

GATES (all machine-checked before any claim): the 18 printed H-series tables
(GGM eqs 121–123) exact in sympy to O(q⁶); det W_{−1} = 2; index identity
(eq 102) as the (0,0) entry of the assembled S⁺; S⁺(0)/S⁻(0) limits; det
S⁺ = det S⁻ = 1 in series; S⁺(q)ᵀ·S⁻(q) = 1 in series AND numerically at the
substrate point.

THE MEASUREMENT: evaluate S⁺, S⁻ at the substrate point q = 1/q₀ ≈ 0.90092
(inside the unit disk — all series converge geometrically; the |q|>1 side
enters only through the eq-124/25 glue, also convergent). Extract:
  • the ODD (chirality) part O = ½(S⁺ − S⁻) — the derived, calibration-free
    fibre-level odd-Stokes datum of the chiral knot 5₂ at the substrate
    (S⁺ and S⁻ are the two half-plane Stokes automorphisms exchanged by the
    bar/mirror structure; their difference is the odd channel);
  • the rotated 3D index Ind^rot_{5₂}(1/q₀) — bar-EVEN by eq 124 despite 5₂
    being chiral (structural finding);
  • the anchor-dependence of the datum (proton vs muon q₀) — honest report:
    a smooth O(10²)-slope function of q₀ (the SRigidityPrune still binds; this
    is NOT the swing, it is the derived odd ingredient the capstone dresses).

No fit (every number is an integer-coefficient q-series evaluation); no c_k
wired; auditOnly; comparison to structure only, no ontological claims.

Run: python3 -u computations/probes/qbeta_5two_stokes_barodd_index_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_stokes_barodd.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
Q0 = {"muon": mp.mpf("1.10997859555733471"),
      "proton": mp.mpf("1.1099785827513808075916690956107688798744991218736")}

qs = sp.symbols("q")
ORD = 6            # series gates to O(q^6)

A_M = sp.Matrix([[0, 1, 0], [0, 1, 1], [-1, 0, 0]])
B_M = sp.Matrix([[0, 0, 1], [0, -2, 0], [1, 0, 0]])
C_M = sp.Matrix([[0, 0, -1], [1, 1, 0], [0, 1, 0]])
Am_M = sp.Matrix([[0, 3, -1], [0, -1, 0], [1, 0, 0]])
Cm_M = sp.Matrix([[0, 0, 1], [3, -1, 0], [-1, 0, 0]])
J_M = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
D_M = sp.diag(1, -1, 1)
# q→0 limit of the assembled S⁺ (GGM eq 100a product):
SP0 = sp.Matrix([[1, 4, 0], [0, 1, 0], [-3, -9, 1]])

# ---------------- exact sympy series (gates) ----------------


def ser(e):
    return sp.expand(sp.series(e, qs, 0, ORD).removeO())


def qpoch_n(n):
    p = sp.Integer(1)
    for k in range(n):
        p *= (1 - qs ** (k + 1))
    return p


def E1n_ser(n):
    s_ = sp.Integer(0)
    for s in range(1, ORD + 1):
        if s * (n + 1) < ORD:
            s_ += qs ** (s * (n + 1)) / (1 - qs ** s)
    return ser(s_)


def E2n_ser(n):
    s_ = sp.Integer(0)
    for s in range(1, ORD + 1):
        if s * (n + 1) < ORD:
            s_ += s * qs ** (s * (n + 1)) / (1 - qs ** s)
    return ser(s_)


def H_series(sign, j, lam):
    """H±_{j,λ}(q) as an exact series to O(q^ORD)."""
    total = sp.Integer(0)
    n = 0
    while True:
        expo = n * (n + 1) + n * lam if sign > 0 else sp.Rational(n * (n + 1), 2) + n * lam
        if expo >= ORD and n > 0:
            break
        if sign > 0:
            t = qs ** (n * (n + 1) + n * lam) / qpoch_n(n) ** 3
            p1 = 1 + 2 * n - 3 * E1n_ser(n) + lam
            if j == 0:
                pj = sp.Integer(1)
            elif j == 1:
                pj = p1
            else:
                pj = p1 ** 2 - sp.Rational(1, 6) - 3 * E2n_ser(n) + 4 * E2n_ser(0)
        else:
            t = sp.Integer(-1) ** n * qs ** (sp.Rational(n * (n + 1), 2) + n * lam) / qpoch_n(n) ** 3
            p1 = sp.Rational(1, 2) + n - 3 * E1n_ser(n) + lam
            if j == 0:
                pj = sp.Integer(1)
            elif j == 1:
                pj = p1
            else:
                pj = p1 ** 2 - sp.Rational(1, 12) - 3 * E2n_ser(n) + 2 * E2n_ser(0)
        total += pj * t
        n += 1
        if n > 2 * ORD:
            break
    return ser(total)


# printed tables (GGM eqs 121-123), coefficients q^0..q^5
PRINTED = {
    (+1, 0, -1): [1, 1, 3, 6, 11, 18],
    (+1, 1, -1): [0, -1, 0, 3, 3, 3],
    (+1, 2, -1): [sp.Rational(-1, 6), sp.Rational(29, 6), sp.Rational(55, 2), 72,
                  sp.Rational(895, 6), 270],
    (-1, 0, -1): [0, -2, -3, -2, 1, 9],
    (-1, 1, -1): [-1, -3, sp.Rational(-3, 2), 12, sp.Rational(69, 2), sp.Rational(153, 2)],
    (-1, 2, -1): [0, sp.Rational(5, 3), sp.Rational(27, 2), sp.Rational(143, 3),
                  sp.Rational(541, 6), sp.Rational(263, 2)],
    (+1, 0, 0): [1, 0, 1, 3, 6, 10],
    (+1, 1, 0): [1, -3, -3, 3, 6, 12],
    (+1, 2, 0): [sp.Rational(5, 6), -5, sp.Rational(53, 6), sp.Rational(117, 2), 117,
                 sp.Rational(601, 3)],
    (-1, 0, 0): [1, -1, -3, -5, -7, -6],
    (-1, 1, 0): [sp.Rational(1, 2), sp.Rational(-9, 2), sp.Rational(-21, 2),
                 sp.Rational(-19, 2), sp.Rational(-9, 2), 27],
    (-1, 2, 0): [sp.Rational(1, 6), sp.Rational(-37, 6), sp.Rational(-17, 2),
                 sp.Rational(115, 6), sp.Rational(389, 6), 181],
    (+1, 0, 1): [1, 0, 0, 1, 3, 6],
    (+1, 1, 1): [2, -3, -6, -2, 3, 15],
    (+1, 2, 1): [sp.Rational(23, 6), -11, -12, sp.Rational(191, 6), sp.Rational(189, 2), 200],
    (-1, 0, 1): [1, 0, -1, -3, -6, -9],
    (-1, 1, 1): [sp.Rational(3, 2), -3, sp.Rational(-17, 2), sp.Rational(-27, 2), -21,
                 sp.Rational(-31, 2)],
    (-1, 2, 1): [sp.Rational(13, 6), -10, sp.Rational(-109, 6), sp.Rational(-13, 2), 7,
                 sp.Rational(173, 2)],
}

# q→0 limit of the assembled S⁻ (GGM eq 100b product; hand-checked:
# S⁺(0)ᵀ·S⁻(0) = 1 exactly, consistent with Conjecture 1(b))
SM0 = sp.Matrix([[1, 0, 3], [-4, 1, -3], [0, 0, 1]])

# ---------------- numeric (mpmath) evaluation ----------------


def qpoch_num(x, n=None, tol=None):
    """(x; x)_n numeric (x real, |x|<1); n=None → run to stabilization."""
    p = mp.mpf(1)
    k = 1
    while True:
        f = 1 - x ** k
        p *= f
        k += 1
        if n is not None and k > n:
            break
        if n is None and abs(x ** k) < mp.mpf("1e-70"):
            break
    return p


def E_num(l, n, x):
    tot = mp.mpf(0)
    s = 1
    while True:
        t = x ** (s * (n + 1)) / (1 - x ** s)
        if l == 2:
            t *= s
        tot += t
        if abs(t) < mp.mpf("1e-65") * max(1, abs(tot)):
            break
        s += 1
        if s > 20000:
            break
    return tot


def H_num(sign, j, lam, x, nmax=120):
    """H±_{j,λ}(x) numeric at real 0<x<1."""
    E2n0 = E_num(2, 0, x)
    tot = mp.mpf(0)
    pq = mp.mpf(1)      # (x;x)_n running
    for n in range(nmax):
        if n > 0:
            pq *= (1 - x ** n)
        if sign > 0:
            t = x ** (n * (n + 1) + n * lam) / pq ** 3
            p1 = 1 + 2 * n - 3 * E_num(1, n, x) + lam
            pj = mp.mpf(1) if j == 0 else p1 if j == 1 else \
                p1 ** 2 - mp.mpf(1) / 6 - 3 * E_num(2, n, x) + 4 * E2n0
        else:
            t = (-1) ** n * x ** (mp.mpf(n * (n + 1)) / 2 + n * lam) / pq ** 3
            p1 = mp.mpf(1) / 2 + n - 3 * E_num(1, n, x) + lam
            pj = mp.mpf(1) if j == 0 else p1 if j == 1 else \
                p1 ** 2 - mp.mpf(1) / 12 - 3 * E_num(2, n, x) + 2 * E2n0
        term = pj * t
        tot += term
        if n > 10 and abs(term) < mp.mpf("1e-55") * max(1, abs(tot)):
            break
    return tot


def W_plus_num(m, x):
    return mp.matrix([[H_num(+1, j, m + i, x) for j in range(3)] for i in range(3)])


def W_minus_num(m, x):
    return mp.matrix([[H_num(-1, j, m + i, x) for j in range(3)] for i in range(3)])


def S_pm_num(x):
    """S⁺(x), S⁻(x) at q=x (0<x<1). W_{−1}(1/x) via the |q|>1 glue (GGM eq
    25): W_m(Q)|_{|Q|>1} = J·W−_{−m−2}(1/Q)·D ⇒ W_{−1}(1/x) = J·W−_{−1}(x)·D."""
    Wq = W_plus_num(-1, x)
    Winv = mp.matrix(J_M.tolist()) * W_minus_num(-1, x) * mp.matrix(D_M.tolist())
    B = mp.matrix(B_M.tolist())
    Sp = 0.5 * mp.matrix(A_M.tolist()) * Winv * B * Wq.T * mp.matrix(C_M.tolist())
    Sm = 0.5 * mp.matrix(Am_M.tolist()) * Wq * B * Winv.T * mp.matrix(Cm_M.tolist())
    return Sp, Sm


def main() -> int:
    print("=" * 78)
    print(" A2 — 5₂ Stokes matrix S⁺(q) at the substrate: bar-odd datum + index")
    print("=" * 78)

    # ---- G1: the 18 printed H-series tables (GGM eqs 121-123) ----
    print("\n[G1] 18 printed H±_{j,λ} tables (GGM eqs 121-123) vs sympy series ...")
    Hs = {}
    bad = []
    for (sgn, j, lam), coeffs in PRINTED.items():
        s_ = H_series(sgn, j, lam)
        Hs[(sgn, j, lam)] = s_
        for k, c in enumerate(coeffs):
            if sp.simplify(s_.coeff(qs, k) - c) != 0:
                bad.append((sgn, j, lam, k))
    g1 = not bad
    print(f"     {'PASS — all 18 series, coefficients q^0..q^5 exact' if g1 else f'FAIL {bad}'}")

    # ---- G2: index identity (GGM eq 102) ----
    idx_ser = ser(2 * Hs[(+1, 1, 0)] * Hs[(-1, 1, 0)])
    idx_expect = [1, -12, 3, 74, 90]
    g2 = all(sp.simplify(idx_ser.coeff(qs, k) - c) == 0 for k, c in enumerate(idx_expect))
    print(f"[G2] Ind^rot_5₂ = 2·H+₁₀·H−₁₀ = 1−12q+3q²+74q³+90q⁴: {'PASS' if g2 else 'FAIL'}")

    # ---- G3: det W_{−1}(q) = 2 (GGM eq 26), series + numeric ----
    Wq_ser = sp.Matrix([[Hs[(+1, j, -1 + i)] for j in range(3)] for i in range(3)])
    detW = ser(Wq_ser.det())
    g3a = sp.simplify(detW - 2) == 0
    x_test = mp.mpf("0.37")
    detW_num = mp.det(W_plus_num(-1, x_test))
    g3b = abs(detW_num - 2) < mp.mpf("1e-30")
    print(f"[G3] det W_{{-1}} = 2: series {'PASS' if g3a else 'FAIL'}; "
          f"numeric at q=0.37: {mp.nstr(detW_num, 20)} {'PASS' if g3b else 'FAIL'}")

    # ---- G4: assembled S⁺/S⁻ series — q→0 limits, det = 1, inversion ----
    Winv_ser = J_M * sp.Matrix([[Hs[(-1, j, -1 + i)] for j in range(3)]
                                for i in range(3)]) * D_M
    Sp_ser = (A_M * Winv_ser * B_M * Wq_ser.T * C_M) / 2
    Sm_ser = (Am_M * Wq_ser * B_M * Winv_ser.T * Cm_M) / 2
    Sp_ser = Sp_ser.applyfunc(ser)
    Sm_ser = Sm_ser.applyfunc(ser)
    Sp0 = Sp_ser.applyfunc(lambda e: e.coeff(qs, 0))
    Sm0 = Sm_ser.applyfunc(lambda e: e.coeff(qs, 0))
    g4a = sp.simplify(Sp0 - SP0) == sp.zeros(3)
    g4b = sp.simplify(Sm0 - SM0) == sp.zeros(3)
    print(f"[G4] q→0 limits: S⁺(0) = eq-100a product [[1,4,0],[0,1,0],[−3,−9,1]]: "
          f"{'PASS' if g4a else 'FAIL'}; S⁻(0) = eq-100b product: {'PASS' if g4b else 'FAIL'}")

    # index entry of the assembled matrix (eq 102, entry (0,0))
    g4c = all(sp.simplify(Sp_ser[0, 0].coeff(qs, k) - c) == 0
              for k, c in enumerate([1, -12, 3, 74, 90]))
    print(f"     assembled S⁺(0,0) = Ind^rot series (eq 102): {'PASS' if g4c else 'FAIL'}")

    # ---- G5: det = 1 and Conjecture 1(b) inversion, in exact series ----
    detSp = ser(sp.expand(Sp_ser.det()))
    detSm = ser(sp.expand(Sm_ser.det()))
    g5a = sp.simplify(detSp - 1) == 0 and sp.simplify(detSm - 1) == 0
    inv_ser = (Sp_ser.T * Sm_ser).applyfunc(lambda e: ser(sp.expand(e)))
    g5b = sp.simplify(inv_ser - sp.eye(3)) == sp.zeros(3)
    print(f"[G5] det S⁺ = det S⁻ = 1 (series): {'PASS' if g5a else 'FAIL'};  "
          f"S⁺(q)ᵀ·S⁻(q) = 1 (Conjecture 1b, series): {'PASS' if g5b else 'FAIL'}")

    # ---- THE MEASUREMENT: S⁺, S⁻ at the substrate point q = 1/q₀ ----
    print("\n[M] S⁺(1/q₀), S⁻(1/q₀) — derived fibre-level Stokes data at the substrate:")
    results = {}
    for name, q0v in Q0.items():
        x = 1 / q0v
        Sp, Sm = S_pm_num(x)
        idx = 2 * H_num(+1, 1, 0, x) * H_num(-1, 1, 0, x)
        Odd = 0.5 * (Sp - Sm)
        results[name] = {"Sp": Sp, "Sm": Sm, "index": idx, "Odd": Odd}
    Sp_mu = results["muon"]["Sp"]
    Sm_mu = results["muon"]["Sm"]
    Odd_mu = results["muon"]["Odd"]
    print(f"     q = 1/q₀(muon) = {mp.nstr(1/Q0['muon'], 12)}")
    print("     S⁺:")
    for i in range(3):
        print("      [" + "  ".join(f"{mp.nstr(Sp_mu[i, j], 12):>18}" for j in range(3)) + "]")
    print("     S⁻:")
    for i in range(3):
        print("      [" + "  ".join(f"{mp.nstr(Sm_mu[i, j], 12):>18}" for j in range(3)) + "]")
    print(f"     Ind^rot_5₂(1/q₀) = {mp.nstr(results['muon']['index'], 15)}  "
          "(= S⁺₍₀,₀₎; bar-EVEN by eq 124 despite chirality)")

    # G6: inversion relation numerically at the substrate — the strong gate:
    # S⁺ and S⁻ are assembled INDEPENDENTLY (29a vs 29b); their product tests
    # every entry of both.
    inv_num = Sp_mu.T * Sm_mu
    inv_res = max(abs(inv_num[i, j] - (1 if i == j else 0))
                  for i in range(3) for j in range(3))
    g6 = inv_res < mp.mpf("1e-30")
    print(f"\n[G6] S⁺ᵀ·S⁻ − 1 at the substrate: max residual = {mp.nstr(inv_res, 4)}  "
          f"{'PASS' if g6 else 'FAIL'}")

    print("\n     ODD (chirality) datum O = ½(S⁺ − S⁻) [muon]:")
    for i in range(3):
        print("      [" + "  ".join(f"{mp.nstr(Odd_mu[i, j], 12):>18}" for j in range(3)) + "]")
    O_norm = mp.sqrt(sum(abs(Odd_mu[i, j]) ** 2 for i in range(3) for j in range(3)))
    print(f"     ‖O‖_F = {mp.nstr(O_norm, 15)}  (nonzero — the chiral odd channel is live)")
    g7 = O_norm > mp.mpf("0.01")

    # ---- anchor-dependence (honest) ----
    dq = Q0["muon"] - Q0["proton"]
    dO = results["muon"]["Odd"] - results["proton"]["Odd"]
    slopes = {(i, j): abs(dO[i, j]) / dq for i in range(3) for j in range(3)}
    max_slope = max(float(v) for v in slopes.values())
    print(f"\n[H] anchor-dependence of O (Δq = {mp.nstr(dq, 4)}):")
    print(f"     max |dO_ij/dq| = {max_slope:.4e}  (S-swing needs ~3.84e6; "
          "SRigidityPrune binds — this datum is smooth, NOT the swing)")
    honest_smooth = max_slope < 1e5

    ok_gates = g1 and g2 and g3a and g3b and g4a and g4b and g4c and g5a and g5b and g6

    wb = WitnessBuilder("qbeta-5two-stokes-barodd-index", engine="sympy+mpmath",
                        _script_path=__file__)
    wb.set_description(
        "A2 (bean qou-ls2y): the 5₂ GGM Stokes automorphisms S⁺(q), S⁻(q) "
        "(2007.10190 eqs 29a/29b, 112-124) evaluated at the substrate point "
        "q=1/q₀ from the published integer-coefficient q-series. Gates: all 18 "
        "printed H-series tables exact to O(q⁵); det W=2; assembled q→0 limits "
        "= the eq-100a/b products; assembled (0,0) entry = Ind^rot (eq 102); "
        "det S± = 1; S⁺ᵀ·S⁻ = 1 (Conjecture 1b) in series AND numerically with "
        "independently-assembled matrices. Measurement: the ODD chirality datum "
        "O = ½(S⁺−S⁻) at the substrate — a DERIVED, calibration-free "
        "fibre-level odd-Stokes datum of the chiral 5₂; the rotated 3D index "
        "at 1/q₀ (bar-EVEN by eq 124 despite chirality); honest "
        "anchor-dependence (smooth O(10²) slope, NOT the swing — SRigidityPrune "
        "binds). Note: the Peacock eq-99 towers are per-ray radar factors, not "
        "entries of the assembled matrix (first-run lesson). No fit; no c_k "
        "wired; auditOnly.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("printed_H_tables_exact",
                     computed=1.0 if g1 else 0.0, expected=1.0, tolerance=0.5,
                     source="18 H±_{j,λ} series (GGM eqs 121-123) reproduced exactly to q^5")
    wb.add_assertion("index_identity_eq102",
                     computed=1.0 if (g2 and g4c) else 0.0, expected=1.0, tolerance=0.5,
                     source="2·H+₁₀·H−₁₀ = 1−12q+3q²+74q³+90q⁴ (eq 102), and it is "
                            "the assembled S⁺(0,0) entry")
    wb.add_assertion("det_W_is_2",
                     computed=1.0 if (g3a and g3b) else 0.0, expected=1.0, tolerance=0.5,
                     source="det W_{−1}(q) = 2 in series (GGM eq 26) and numerically")
    wb.add_assertion("q0_limits_eq100",
                     computed=1.0 if (g4a and g4b) else 0.0, expected=1.0, tolerance=0.5,
                     source="assembled S⁺(0), S⁻(0) equal the eq-100a/b Stokes-constant "
                            "products [[1,4,0],[0,1,0],[−3,−9,1]] / [[1,0,3],[−4,1,−3],[0,0,1]]")
    wb.add_assertion("sl3_and_inversion_series",
                     computed=1.0 if (g5a and g5b) else 0.0, expected=1.0, tolerance=0.5,
                     source="det S± = 1 and S⁺(q)ᵀ·S⁻(q) = 1 (Conjecture 1b) in exact series")
    wb.add_assertion("inversion_numeric_at_substrate",
                     computed=float(inv_res), expected=0.0, tolerance=1e-30,
                     source="S⁺ᵀ·S⁻ = 1 numerically at q=1/q₀ with independently-"
                            "assembled matrices (29a vs 29b)")
    wb.add_assertion("odd_channel_nonzero",
                     computed=1.0 if g7 else 0.0, expected=1.0, tolerance=0.5,
                     source="‖½(S⁺−S⁻)‖_F > 0.01 at the substrate — the chiral odd "
                            "channel is live (4₁'s would vanish by amphichirality)")
    wb.add_assertion("anchor_smooth_honest",
                     computed=1.0 if honest_smooth else 0.0, expected=1.0, tolerance=0.5,
                     source="max |dO_ij/dq| ≪ 3.84e6 — the derived datum is anchor-smooth; "
                            "it is the odd ingredient, NOT the swing (SRigidityPrune)")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("substrate_point", {"q_inv_muon": mp.nstr(1 / Q0["muon"], 30),
                                    "q_inv_proton": mp.nstr(1 / Q0["proton"], 30)})
    wb.add_data("S_plus_at_substrate_muon",
                [[mp.nstr(Sp_mu[i, j], 25) for j in range(3)] for i in range(3)])
    wb.add_data("S_minus_at_substrate_muon",
                [[mp.nstr(Sm_mu[i, j], 25) for j in range(3)] for i in range(3)])
    wb.add_data("odd_datum_O_muon",
                [[mp.nstr(Odd_mu[i, j], 25) for j in range(3)] for i in range(3)])
    wb.add_data("odd_datum_O_proton",
                [[mp.nstr(results["proton"]["Odd"][i, j], 25) for j in range(3)]
                 for i in range(3)])
    wb.add_data("odd_datum_frobenius_norm_muon", mp.nstr(O_norm, 25))
    wb.add_data("rotated_index_at_substrate",
                {"muon": mp.nstr(results["muon"]["index"], 25),
                 "proton": mp.nstr(results["proton"]["index"], 25),
                 "note": "bar-EVEN by GGM eq 124 despite 5₂ chirality"})
    wb.add_data("anchor_max_slope", f"{max_slope:.6e}")
    wb.add_data("verdict",
                ("DERIVED ODD-STOKES DATUM LANDED: both 5₂ Stokes automorphisms "
                 "S⁺, S⁻ at the substrate point from published integer q-series, "
                 "with 6 exact gates including the independently-assembled "
                 "inversion S⁺ᵀ·S⁻ = 1. The odd chirality datum O = ½(S⁺−S⁻) is "
                 "nonzero (‖O‖_F given) and calibration-free in form — the "
                 "derived fibre-level odd ingredient for the capstone. It is "
                 "anchor-smooth (honest: not the swing; SRigidityPrune binds), "
                 "and the rotated index is bar-EVEN despite chirality "
                 "(structural). No fit; no c_k wired; auditOnly."
                 if (ok and ok_gates) else "INCONCLUSIVE — a gate failed; inspect."))
    wb.save()
    print(f"\n  assertions passed: {ok}")
    print("  witness -> computations/probes/qbeta-5two-stokes-barodd-index.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
