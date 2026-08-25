#!/usr/bin/env python3
"""gk_d5_cyclic_dilog_4one_probe.py — the B4 residue of the Vector-2 double
pincer: the Garoufalidis–Kashaev cyclic quantum dilogarithm D₅ product on the
explicit 4₁ state-integral data at b² = 1/5.

Closes the **B4 open sub-item** of
`docs/audits/2026-07-18-vector2-double-pincer-a5-b4.md` ("the full algebraic
number multiplying 1/√5 in Cor 1.2's 4₁ evaluation is 1/√5 × (root of unity)
× (Rogers exp) × ∏ D₅(θ,ζ₅) — needs GK's explicit 4₁ triangulation data").

SOURCE DATA (GK = Garoufalidis–Kashaev, arXiv:1411.6062v2,
library/arxiv-1411.6062v2/1411.6062v2.pdf; equations read from the rendered PDF pages 2–5, 16):
  (1)   I_{A,B}(b) = ∫_{ℝ+iε} Φ_b(x)^B e^{−Aπi x²} dx;  4₁ ↔ (A,B) = (1,2)
        (§2.2: "(A,B) = (1,2) and (1,3) ... correspond to the state-integrals
        of the knots 4₁ and 5₂"; two tetrahedra ⇒ B = 2 quantum dilogarithms).
  (9)   D_N(x;q)  = ∏_{k=1}^{N−1} (1 − q^k x)^{k/N}   (cyclic dilogarithm)
  (10)  /D_N(x;q) = ∏_{k=1}^{N} (1 − x q^k)^{k/N} = (1 − x q^N) D_N(x;q)
  (fun) D_N(ζ_N x; ζ_N)^N / D_N(x; ζ_N)^N = (1 − x)^N / (1 − x^N)
  (4/7) g⁺_k(x,q) = (−x)^{Ak} q^{Ak(k+1)/2} / (qx;q)_k^B;
        G⁺_N(x) = Σ_{k=0}^{N−1} g⁺_k(x, ζ_N)
  (18)  Cor 1.2 (M = 1):  I_{A,B}(b) = e^{πi[(B+3A(N+2)²−6N)/(12N)]} · (1/√N)
        · Σ_{w∈S} e^{iB R(z)/(2πN)} (1−z)^{(2N+3)B/(4N)}
          / [(A + Bz/(1−z)) · /D_N(θ₊, ζ_N)^B] · G⁺_N(θ₊),
        z = e^{2πsw}, θ₊ = z^{1/N}, q₊ = ζ_N.
  Cor 1.3 (the 4₁ data): g(z) = −z(1−z)^{−2}; S = {z± = e(±1/6)} with branch
        log z₊ = 2πi/6, log z₋ = 10πi/6; Rogers R(z) per (8) with those logs.
  App A (75): Φ_b(x) = exp( ∫_{ℝ+iε} e^{−2ixz}/(4 sinh(zb) sinh(z/b)) dz/z ).

AT N = 5, M = 1 (b = 1/√5, s = √5) FOR 4₁:
  θ₊(z₊) = e^{iπ/15} = ζ₃₀   and   θ₊(z₋) = e^{iπ/3} = ζ₃₀⁵;  q₊ = ζ₅ = ζ₃₀⁶.
  ALL algebraic data live in ℚ(ζ₃₀) (deg 8; real subfield ℚ(ζ₃₀)⁺ deg 4);
  exact arithmetic here = polynomial arithmetic mod Φ₃₀(t).

WHAT IS EXACT AND MACHINE-CHECKED:
  E1  the functional equation of D₅ at q = ζ₅, as a polynomial identity in
      ℚ(ζ₅)[x]:  D₅(ζ₅x)⁵ (1−x⁵) = D₅(x)⁵ (1−x)⁵.
  E2  (/D₅(θ; ζ₅))⁵ for both θ's is REAL (conj-invariant in ℚ(ζ₃₀)) with
      exact minimal polynomials
        θ₊ = ζ₃₀ :  x⁴ − 46x³ − 94x² + 79x + 1     (value ≈ −0.0124742…)
        θ₋ = ζ₆  :  x⁴ + 29x³ − 69x² + 29x + 1     (value ≈ −0.0320118…)
      Both are DEGREE 4 = [ℚ(ζ₃₀)⁺ : ℚ]: each value generates the full real
      quartic field ℚ(ζ₃₀)⁺ ⊋ ℚ(√5). They factor over ℚ(√5) into quadratics
      (ℚ(√5) IS the quadratic subfield) but do NOT lie in ℚ(√5).
  E3  the state sums G₅⁺(θ) are REAL with exact minimal polynomials
        θ₊ :  x⁴ − 60x³ + 960x² − 5175x + 6525    (value ≈ 1.7916727…)
        θ₋ :  x⁴ − 60x³ + 885x² − 4500x + 6525    (value ≈ 2.4215348…)
      — again degree 4, full ℚ(ζ₃₀)⁺, not ℚ(√5).
  E4  branch invariance (GK Remarks 1.4/1.5): replacing θ → ζ₅θ leaves the
      combination G₅⁺(θ)⁵ · /D₅⁻²·⁵ invariant — exact identity
      G₅⁺(ζ₅θ)⁵ /D₅(θ)^{2·5}... precisely: G(ζ₅θ)⁵ P(θ)² = G(θ)⁵ P(ζ₅θ)²
      with P = (/D₅)⁵, for both θ's.
  E5  the N = 1 machinery reproduces Cor 1.3 exactly:
      (1−z±)^{1/2}/(A+Bz±/(1−z±)) = (1/√3) e(∓1/3), and the Rogers branches
      R(z₊) = −π²/12 + iV/2, R(z₋) = −5π²/12 − iV/2 (40-digit check against
      Cor 1.3's printed (e^{∓C}·roots of unity), V = Vol(4₁)).
  E6  END-TO-END GOLD CHECK: the assembled Cor 1.2 evaluation at N = 5 equals
      the DIRECT numerical state integral ∫ Φ_b(x)² e^{−πix²} dx at
      b = 1/√5 (Faddeev integral rep, App A (75); vectorized double-precision
      tensor quadrature validated first at b = 1 against GK's closed form (2)
      to ~5e-9):  I_{1,2}(1/√5) ≈ 0.0286196521 + 0.1346448862 i.

THE ANSWER TO THE B4 QUESTION (recorded-not-interpreted, scope-(a)):
  I_{1,2}(1/√5) = (1/√5) [ c₊ e^{−V/(10π)} + c₋ e^{+V/(10π)} ],  where the
  algebraic prefactors c± have exact magnitude
      |c±| = G₅⁺(θ±) / (√3 · |/D₅(θ±)|²),   |c±|¹⁰ ∈ ℚ(ζ₃₀)⁺ exactly,
      |c₊| ≈ 5.9743802…,  |c₋| ≈ 5.5386782….
  FIELD: the D₅ data and the prefactor magnitudes live in the full real
  quartic cyclotomic field ℚ(ζ₃₀)⁺ (and, for |c±| itself, a degree-5 radical
  extension thereof) — NOT in ℚ(√5). The golden-ratio combinations
  (2/√5)sin(π/5) ≈ 0.5257, (2/√5)sin(2π/5) ≈ 0.8507 (the Σ(2,3,5) S-matrix
  vacuum row) do NOT appear: the exact in-field comparisons
  |c±|¹⁰ = ((5∓√5)/10)⁵ are all FALSE, and the 40-digit numerics are
  separated by factors ≈ 7–11. The only √5 in the 4₁ evaluation at b² = 1/5
  remains the Gauss-sum prefactor 1/√N = 1/√5 (pinned by the parent probe).

VERDICT (scope-(a)): the GK leg of Vector 2 CLOSES at scope (a): the
cyclic-dilogarithm product on the explicit 4₁ data, alone, does not reproduce
the icosahedral S-matrix vacuum-row entries — the shared object remains the
bare algebraic number √5 (Gauss sum ↔ S-matrix normalization), with no
object-level map. The magnitude scalar m ∈ (0, 1/√5) stays OPEN; nothing is
wired to production.
"""
from __future__ import annotations

# Path bridge (probes/ subdirectory refactor). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

t, x = sp.symbols("t x")
PHI30 = sp.cyclotomic_poly(30, t)          # t^8+t^7-t^5-t^4-t^3+t+1
Z30_NUM = sp.exp(sp.I * sp.pi / 15)        # ζ₃₀ = e^{2πi/30}

A_KNOT, B_KNOT = 1, 2                      # 4₁ state integral (GK §2.2)


# ── exact arithmetic in ℚ(ζ₃₀) = ℚ[t]/Φ₃₀ ──────────────────────────────────
def red(e):
    return sp.rem(sp.expand(e), PHI30, t)


def inv(e):
    return sp.invert(sp.Poly(red(e), t), sp.Poly(PHI30, t)).as_expr()


def conj(e):
    return red(sp.expand(red(e).subs(t, t**29)))


def num(e, dps=50):
    return sp.N(red(e).subs(t, Z30_NUM), dps)


def slashD5_pow5(theta):
    """(/D₅(θ; ζ₅))⁵ = ∏_{k=1}^{5} (1 − θ ζ₅^k)^k, exact in ℚ(ζ₃₀). ζ₅ = t⁶."""
    return red(sp.prod([red((1 - red(theta) * t**((6 * k) % 30)) ** k)
                        for k in range(1, 6)]))


def G5plus(theta):
    """G₅⁺(θ) = Σ_{k=0}^{4} (−θ)^{Ak} ζ₅^{Ak(k+1)/2} / (ζ₅θ;ζ₅)_k^B, exact."""
    tot = sp.Integer(0)
    for k in range(5):
        poch = sp.Integer(1)
        for j in range(1, k + 1):
            poch = red(poch * (1 - red(theta) * t**((6 * j) % 30)))
        term = red(red((-red(theta)) ** (A_KNOT * k))
                   * t**((6 * (A_KNOT * k * (k + 1) // 2)) % 30)
                   * red(inv(poch) ** B_KNOT))
        tot = red(tot + term)
    return tot


# ── direct state integral (App A (75) + eq (1)), vectorized numpy ───────────
def _leg_nodes(a, b, n, pieces):
    xs, ws = np.polynomial.legendre.leggauss(n)
    edges = np.linspace(a, b, pieces + 1)
    X, W = [], []
    for i in range(pieces):
        m, h = (edges[i] + edges[i + 1]) / 2, (edges[i + 1] - edges[i]) / 2
        X.append(m + h * xs)
        W.append(h * ws)
    return np.concatenate(X), np.concatenate(W)


def state_integral(b, A=1, B=2):
    """I_{A,B}(b) by tensor Gauss–Legendre quadrature (double precision)."""
    tt, wt = _leg_nodes(-40.0, 40.0, 24, 60)     # inner (Faddeev) contour ℝ+0.2i
    z = tt + 0.2j
    base = 1.0 / (4 * np.sinh(z * b) * np.sinh(z / b) * z)
    xt, wx = _leg_nodes(-12.0, 12.0, 24, 80)     # outer contour ℝ+0.5i
    xx = xt + 0.5j
    E = np.exp(-2j * np.outer(xx, z))
    phib = np.exp(E @ (base * wt))
    return complex(np.sum(phib**B * np.exp(-A * np.pi * 1j * xx**2) * wx))


def main() -> int:  # noqa: PLR0915
    wb = WitnessBuilder("gk-d5-cyclic-dilog-4one", engine="sympy")
    mp.mp.dps = 60

    # ── E1: functional equation of D₅ at q = ζ₅, exact in ℚ(ζ₅)[x] ─────────
    z5x, xx = sp.symbols("z5x xx")
    Phi5 = sp.cyclotomic_poly(5, z5x)

    def red5(e):
        return sp.rem(sp.expand(e), Phi5, z5x)

    D5x = sp.prod([(1 - z5x**k * xx) ** k for k in range(1, 5)])
    D5zx = sp.prod([(1 - z5x**k * (z5x * xx)) ** k for k in range(1, 5)])
    fe = sp.expand(D5zx * (1 - xx**5) - D5x * (1 - xx) ** 5)
    fe_red = sp.expand(sp.rem(sp.Poly(fe, z5x).as_expr(), Phi5, z5x))
    assert fe_red == 0, "D₅ functional equation must hold in ℚ(ζ₅)[x]"
    # /D₅ = (1 − x q⁵) D₅ = (1 − x) D₅ at q = ζ₅ (q⁵ = 1) — definitional.

    # ── the 4₁ data at b² = 1/5 ─────────────────────────────────────────────
    th_p = t          # θ₊(z₊) = e^{iπ/15} = ζ₃₀   (log z₊ = 2πi/6)
    th_m = t**5       # θ₊(z₋) = e^{iπ/3}          (log z₋ = 10πi/6)

    P5p, P5m = slashD5_pow5(th_p), slashD5_pow5(th_m)
    Gp, Gm = G5plus(th_p), G5plus(th_m)

    # ── E2 + E3: reality and exact minimal polynomials ──────────────────────
    assert sp.expand(conj(P5p) - P5p) == 0, "(/D₅(θ₊))⁵ must be real"
    assert sp.expand(conj(P5m) - P5m) == 0, "(/D₅(θ₋))⁵ must be real"
    assert sp.expand(conj(Gp) - Gp) == 0, "G₅⁺(θ₊) must be real"
    assert sp.expand(conj(Gm) - Gm) == 0, "G₅⁺(θ₋) must be real"

    mp_P5p = sp.minimal_polynomial(red(P5p).subs(t, Z30_NUM), x)
    mp_P5m = sp.minimal_polynomial(red(P5m).subs(t, Z30_NUM), x)
    mp_Gp = sp.minimal_polynomial(red(Gp).subs(t, Z30_NUM), x)
    mp_Gm = sp.minimal_polynomial(red(Gm).subs(t, Z30_NUM), x)
    assert sp.expand(mp_P5p - (x**4 - 46 * x**3 - 94 * x**2 + 79 * x + 1)) == 0
    assert sp.expand(mp_P5m - (x**4 + 29 * x**3 - 69 * x**2 + 29 * x + 1)) == 0
    assert sp.expand(mp_Gp - (x**4 - 60 * x**3 + 960 * x**2 - 5175 * x + 6525)) == 0
    assert sp.expand(mp_Gm - (x**4 - 60 * x**3 + 885 * x**2 - 4500 * x + 6525)) == 0
    # degree 4 = [ℚ(ζ₃₀)⁺:ℚ] ⇒ NOT in ℚ(√5) (degree 2); but each factors over
    # ℚ(√5) into quadratics (ℚ(√5) is the quadratic subfield of ℚ(ζ₃₀)⁺):
    for mpol in (mp_P5p, mp_P5m, mp_Gp, mp_Gm):
        assert sp.Poly(mpol, x).degree() == 4
        facs = sp.factor_list(mpol, extension=sp.sqrt(5))[1]
        assert len(facs) == 2 and all(sp.Poly(f, x).degree() == 2
                                      for f, _ in facs), sp.factor(
            mpol, extension=sp.sqrt(5))

    # ── E4: ζ₅-branch invariance (GK Remarks 1.4/1.5), exact ────────────────
    for th, P_, G_ in ((th_p, P5p, Gp), (th_m, P5m, Gm)):
        th_shift = red(t**6 * th)
        lhs = red(red(G5plus(th_shift) ** 5) * red(P_**2))
        rhs = red(red(G_**5) * red(slashD5_pow5(th_shift) ** 2))
        assert sp.expand(lhs - rhs) == 0, "branch invariance must hold exactly"

    # ── E5: Cor 1.3 (N = 1) machinery, exact + 40-digit Rogers branches ─────
    zp = sp.exp(sp.I * sp.pi / 3)
    zm = sp.exp(-sp.I * sp.pi / 3)
    # (1−z₊) = e^{−iπ/3}, (1−z₋) = e^{iπ/3}; (A+Bz/(1−z)) = (1+z)/(1−z) = ±i√3
    simp0 = lambda e: sp.simplify(sp.expand_complex(e)) == 0  # noqa: E731
    assert simp0(1 - zp - sp.exp(-sp.I * sp.pi / 3))
    assert simp0((1 + zp) / (1 - zp) - sp.I * sp.sqrt(3))
    lhs_p = sp.exp(-sp.I * sp.pi / 6) / (sp.I * sp.sqrt(3))
    lhs_m = sp.exp(sp.I * sp.pi / 6) / (-sp.I * sp.sqrt(3))
    assert simp0(lhs_p - sp.exp(-2 * sp.pi * sp.I / 3) / sp.sqrt(3))
    assert simp0(lhs_m - sp.exp(2 * sp.pi * sp.I / 3) / sp.sqrt(3))
    # Rogers with GK branches log z₊ = iπ/3, log z₋ = 10iπ/6 (Li₂ principal):
    V = 2 * mp.im(mp.polylog(2, mp.e**(1j * mp.pi / 3)))
    Rp = (mp.polylog(2, mp.e**(1j * mp.pi / 3))
          + mp.mpf(1) / 2 * (1j * mp.pi / 3) * (-1j * mp.pi / 3)
          - mp.pi**2 / 6)
    Rm = (mp.polylog(2, mp.e**(-1j * mp.pi / 3))
          + mp.mpf(1) / 2 * (10j * mp.pi / 6) * (1j * mp.pi / 3)
          - mp.pi**2 / 6)
    err_Rp = abs(Rp - (-mp.pi**2 / 12 + 1j * V / 2))
    err_Rm = abs(Rm - (-5 * mp.pi**2 / 12 - 1j * V / 2))
    assert err_Rp < mp.mpf(10) ** (-40), err_Rp
    assert err_Rm < mp.mpf(10) ** (-40), err_Rm
    # Cor 1.3's printed values e^{iR/π} = e^{∓C}·(roots of unity), C = V/2π:
    eq_ = lambda a, b: mp.e**(2j * mp.pi * mp.mpf(a) / mp.mpf(b))  # noqa: E731
    err13p = abs(mp.e**(1j * Rp / mp.pi)
                 - mp.e**(-V / (2 * mp.pi)) * eq_(-1, 24))
    err13m = abs(mp.e**(1j * Rm / mp.pi)
                 + mp.e**(V / (2 * mp.pi)) * eq_(-1, 24) * eq_(1, 3))
    assert err13p < mp.mpf(10) ** (-40) and err13m < mp.mpf(10) ** (-40)

    # ── assemble Cor 1.2 at N = 5 (50-dps principal branches) ───────────────
    i = mp.mpc(0, 1)
    z5n = mp.e**(2j * mp.pi / 5)
    thp_n = mp.e**(1j * mp.pi / 15)
    thm_n = mp.e**(1j * mp.pi / 3)

    def slashD5_num(theta):
        out = mp.mpc(1)
        for k in range(1, 6):
            out *= (1 - theta * z5n**k) ** (mp.mpf(k) / 5)
        return out

    Gp_n = mp.mpc(str(sp.re(num(Gp))), str(sp.im(num(Gp))))
    Gm_n = mp.mpc(str(sp.re(num(Gm))), str(sp.im(num(Gm))))
    glob = eq_(-1, 120)   # e^{πi(B+3A(N+2)²−6N)/(12N)} = e^{119πi/60} = e(−1/120)
    pw = mp.mpf(13) / 10  # (2N+3)B/(4N) = 26/20
    c_p = (glob * eq_(-1, 120) * (mp.e**(-1j * mp.pi / 3)) ** pw
           * (1 / (i * mp.sqrt(3))) * Gp_n / slashD5_num(thp_n) ** B_KNOT)
    c_m = (glob * eq_(-1, 24) * (mp.e**(1j * mp.pi / 3)) ** pw
           * (1 / (-i * mp.sqrt(3))) * Gm_n / slashD5_num(thm_n) ** B_KNOT)
    I_assembled = (c_p * mp.e**(-V / (10 * mp.pi))
                   + c_m * mp.e**(V / (10 * mp.pi))) / mp.sqrt(5)

    # ── E6: gold checks against the direct Faddeev state integral ──────────
    target_N1 = complex(mp.e**(1j * mp.pi / 6) / mp.sqrt(3)
                        * (mp.e**(V / (2 * mp.pi)) - mp.e**(-V / (2 * mp.pi))))
    got_N1 = state_integral(1.0)
    err_N1 = abs(got_N1 - target_N1)
    assert err_N1 < 5e-7, err_N1      # validates the quadrature itself (eq (2))
    got_N5 = state_integral(1 / np.sqrt(5))
    err_N5 = abs(complex(I_assembled) - got_N5)
    assert err_N5 < 5e-7, err_N5      # validates the whole Cor 1.2 assembly

    # ── the B4 answer: field identification + vacuum-row comparison ─────────
    # exact: |c±|¹⁰ = G¹⁰ / (3⁵ (P⁵)⁴) ∈ ℚ(ζ₃₀)⁺;  √5 = 1 + 2(ζ₅+ζ₅⁻¹) in-field
    sqrt5 = red(1 + 2 * (t**6 + t**24))
    assert sp.expand(red(sqrt5**2) - 5) == 0
    vacuum_match = {}
    c10 = {}
    for name, G_, P_ in (("+", Gp, P5p), ("-", Gm, P5m)):
        c10[name] = red(red(G_**10) * inv(red(3**5 * red(P_**4))))
        for sgn, tgt_name in ((-1, "sin_pi_5"), (1, "sin_2pi_5")):
            # ((2/√5) sin(kπ/5))¹⁰ = ((5∓√5)/10)⁵
            tgt = red(red((5 + sgn * sqrt5) * inv(sp.Integer(10))) ** 5)
            vacuum_match[f"c{name}_vs_{tgt_name}"] = \
                sp.expand(red(c10[name] - tgt)) == 0
    assert not any(vacuum_match.values()), vacuum_match  # exact NO match

    abs_cp = abs(c_p)
    abs_cm = abs(c_m)
    tgt1 = 2 / mp.sqrt(5) * mp.sin(mp.pi / 5)
    tgt2 = 2 / mp.sqrt(5) * mp.sin(2 * mp.pi / 5)
    # 40-digit separation from both vacuum-row entries
    for c_ in (abs_cp, abs_cm):
        for tg in (tgt1, tgt2):
            assert abs(c_ - tg) > 1, (c_, tg)

    # ── report ──────────────────────────────────────────────────────────────
    print("=" * 74)
    print(" B4 residue: GK D₅ cyclic-dilog product on the explicit 4₁ data")
    print(" at b² = 1/5 — audit-only / scope-(a) / no fit / nothing wired")
    print("=" * 74)
    print("E1  D₅ functional equation at q=ζ₅: exact polynomial identity  ✓")
    print("E2  (/D₅(θ;ζ₅))⁵ exact (both REAL, deg-4 minpolys over ℚ):")
    print(f"    θ₊=ζ₃₀: {mp_P5p}   value ≈ {num(P5p, 30)}")
    print(f"    θ₋=ζ₆ : {mp_P5m}   value ≈ {num(P5m, 30)}")
    print("E3  G₅⁺(θ) exact (both REAL, deg-4 minpolys):")
    print(f"    θ₊: {mp_Gp}   value ≈ {num(Gp, 30)}")
    print(f"    θ₋: {mp_Gm}   value ≈ {num(Gm, 30)}")
    print("    all four generate the FULL quartic ℚ(ζ₃₀)⁺ ⊋ ℚ(√5) "
          "(factor over ℚ(√5) into quadratics; do not lie in it)")
    print("E4  ζ₅-branch invariance G⁵P² identity: exact  ✓ (both θ)")
    print("E5  Cor 1.3 (N=1) machinery + Rogers branches: exact / 40-digit  ✓")
    print(f"E6  gold: |I_quad(b=1) − closed form (2)| = {err_N1:.2e}")
    print(f"         |I_assembled(b²=1/5) − I_quad| = {err_N5:.2e}")
    print(f"    I_{{1,2}}(1/√5) = {mp.nstr(I_assembled, 30)}")
    print("B4 ANSWER:  I = (1/√5)[c₊ e^{−V/10π} + c₋ e^{V/10π}]")
    print(f"    |c₊| = {mp.nstr(abs_cp, 40)}")
    print(f"    |c₋| = {mp.nstr(abs_cm, 40)}")
    print(f"    vs vacuum row (2/√5)sin(π/5)  = {mp.nstr(tgt1, 40)}")
    print(f"       vacuum row (2/√5)sin(2π/5) = {mp.nstr(tgt2, 40)}")
    print(f"    exact |c±|¹⁰ = ((5∓√5)/10)⁵ comparisons: {vacuum_match}")
    print("VERDICT: the D₅ product data live in ℚ(ζ₃₀)⁺ (quartic), NOT ℚ(√5);")
    print("  no vacuum-row match (exact + 40-digit). The GK leg of Vector 2")
    print("  CLOSES at scope-(a); the only √5 is the Gauss-sum 1/√N. m OPEN.")

    # ── witness ─────────────────────────────────────────────────────────────
    wb.set_description(
        "B4 residue of the Vector-2 double pincer: the Garoufalidis–Kashaev "
        "(arXiv:1411.6062) cyclic quantum dilogarithm D₅ product evaluated on "
        "the explicit 4₁ state-integral data ((A,B)=(1,2), g(z)=−z(1−z)⁻², "
        "z± = e(±1/6)) at b² = 1/5. Exact results in ℚ(ζ₃₀): (/D₅(θ;ζ₅))⁵ is "
        "real with minpoly x⁴−46x³−94x²+79x+1 (θ₊=ζ₃₀) / x⁴+29x³−69x²+29x+1 "
        "(θ₋=ζ₆); the state sums G₅⁺ are real with minpolys "
        "x⁴−60x³+960x²−5175x+6525 / x⁴−60x³+885x²−4500x+6525 — all degree 4, "
        "generating the FULL real quartic field ℚ(ζ₃₀)⁺, not ℚ(√5). The "
        "assembled Cor 1.2 evaluation I_{1,2}(1/√5) = (1/√5)[c₊e^{−V/10π} + "
        "c₋e^{V/10π}] (|c₊|≈5.97438, |c₋|≈5.53868) matches the DIRECT "
        "Faddeev state integral to quadrature precision (~2e-9 scale; "
        "quadrature itself validated at b=1 against GK eq (2)). The "
        "icosahedral Σ(2,3,5) vacuum-row entries (2/√5)sin(kπ/5) do NOT "
        "appear: exact in-field comparisons |c±|¹⁰ = ((5∓√5)/10)⁵ all FALSE. "
        "Scope-(a): the GK leg closes; the only √5 in the 4₁ evaluation "
        "remains the Gauss-sum prefactor 1/√N = 1/√5; m stays OPEN; nothing "
        "wired."
    )
    wb.set_audit_only("docs/audits/2026-07-24-vector2-residues-sprime-d5.md")
    wb.add_parameter("N", 5)
    wb.add_parameter("M", 1)
    wb.add_parameter("A_B", "(1, 2)  — the 4₁ state integral (GK §2.2)")
    wb.add_parameter("theta_plus_of_z_plus", "e^{iπ/15} = ζ₃₀  (log z₊ = 2πi/6)")
    wb.add_parameter("theta_plus_of_z_minus", "e^{iπ/3}  (log z₋ = 10πi/6)")
    wb.add_data("exact_values", {
        "slashD5_pow5_theta_plus": {
            "minpoly": str(mp_P5p.as_expr() if hasattr(mp_P5p, "as_expr")
                           else mp_P5p),
            "value_30dps": str(num(P5p, 30)),
            "real": True,
        },
        "slashD5_pow5_theta_minus": {
            "minpoly": str(mp_P5m),
            "value_30dps": str(num(P5m, 30)),
            "real": True,
        },
        "G5plus_theta_plus": {"minpoly": str(mp_Gp),
                              "value_30dps": str(num(Gp, 30)), "real": True},
        "G5plus_theta_minus": {"minpoly": str(mp_Gm),
                               "value_30dps": str(num(Gm, 30)), "real": True},
        "field": "all four values generate the full real quartic ℚ(ζ₃₀)⁺; "
                 "each minpoly factors over ℚ(√5) into two quadratics "
                 "(ℚ(√5) is the quadratic subfield) but none lies in ℚ(√5)",
    })
    wb.add_data("evaluation_structure", {
        "form": "I_{1,2}(1/√5) = (1/√5)[c₊ e^{−V/(10π)} + c₋ e^{V/(10π)}]",
        "c_plus_50dps": mp.nstr(c_p, 50),
        "c_minus_50dps": mp.nstr(c_m, 50),
        "abs_c_plus_40dps": mp.nstr(abs_cp, 40),
        "abs_c_minus_40dps": mp.nstr(abs_cm, 40),
        "abs_c_relation": "|c±| = G₅⁺(θ±)/(√3·|/D₅(θ±)|²); |c±|¹⁰ ∈ ℚ(ζ₃₀)⁺ "
                          "exactly (= G¹⁰/(3⁵(P⁵)⁴))",
        "I_assembled_30dps": mp.nstr(I_assembled, 30),
        "I_direct_quadrature": repr(got_N5),
        "vacuum_row_targets_40dps": [mp.nstr(tgt1, 40), mp.nstr(tgt2, 40)],
        "exact_vacuum_row_comparisons": {k: bool(v)
                                         for k, v in vacuum_match.items()},
    })
    wb.add_caveat(
        "Scope-(a): 'the cyclic-dilogarithm product on the explicit 4₁ data, "
        "alone, does not reproduce the icosahedral vacuum-row entries.' The "
        "shared object between the exchange ceiling, the Gauss sum and the "
        "S-matrix normalization remains the bare algebraic number √5 — no "
        "object-level map, anti-numerology gate in full force. |c±| involve "
        "principal-branch 5th roots ( /D₅ is multivalued; the assembled sum "
        "is branch-invariant per E4 and is pinned end-to-end by the direct "
        "integral E6). m ∈ (0, 1/√5) remains OPEN; nothing wired."
    )
    wb.add_assertion(
        "D5_functional_equation_exact",
        computed="0",
        expected="0",
        tolerance=0,
        source="D₅(ζ₅x)⁵(1−x⁵) − D₅(x)⁵(1−x)⁵ ≡ 0 in ℚ(ζ₅)[x] (GK eq after "
               "(9)), exact polynomial identity.",
    )
    wb.add_assertion(
        "slashD5_pow5_minpolys_exact",
        computed=f"{mp_P5p}; {mp_P5m}",
        expected="x**4 - 46*x**3 - 94*x**2 + 79*x + 1; "
                 "x**4 + 29*x**3 - 69*x**2 + 29*x + 1",
        tolerance=0,
        source="(/D₅(θ;ζ₅))⁵ real for both 4₁ θ's; degree-4 minpolys ⇒ the "
               "values generate ℚ(ζ₃₀)⁺, NOT ℚ(√5).",
    )
    wb.add_assertion(
        "G5plus_minpolys_exact",
        computed=f"{mp_Gp}; {mp_Gm}",
        expected="x**4 - 60*x**3 + 960*x**2 - 5175*x + 6525; "
                 "x**4 - 60*x**3 + 885*x**2 - 4500*x + 6525",
        tolerance=0,
        source="state sums G₅⁺(θ±) real; degree-4 minpolys — same field "
               "ℚ(ζ₃₀)⁺.",
    )
    wb.add_assertion(
        "zeta5_branch_invariance_exact",
        computed="True",
        expected="True",
        tolerance=0,
        source="G₅⁺(ζ₅θ)⁵·(/D₅(θ)⁵)² = G₅⁺(θ)⁵·(/D₅(ζ₅θ)⁵)² exactly for both "
               "θ's — GK Remarks 1.4/1.5 verified at N=5.",
    )
    wb.add_assertion(
        "quadrature_validated_at_N1",
        computed=float(err_N1),
        expected=0.0,
        tolerance=5e-7,
        source="direct Faddeev-integral quadrature vs GK closed form (2) at "
               "b=1: |Δ| ≈ 5e-9 (double-precision tensor Gauss–Legendre).",
    )
    wb.add_assertion(
        "assembled_cor12_equals_direct_integral",
        computed=float(err_N5),
        expected=0.0,
        tolerance=5e-7,
        source="assembled Cor 1.2 evaluation at b²=1/5 vs direct state "
               "integral ∫Φ_b(x)²e^{−πix²}dx — end-to-end gold check of the "
               "entire transcription (root of unity, Rogers branches, "
               "(1−z)^{13/10}, 1-loop (1+z)/(1−z), /D₅ branches, G₅⁺).",
    )
    wb.add_assertion(
        "no_vacuum_row_match_exact",
        computed=str(any(vacuum_match.values())),
        expected="False",
        tolerance=0,
        source="exact in-field comparisons |c±|¹⁰ = ((5∓√5)/10)⁵ (i.e. "
               "|c±| = (2/√5)sin(kπ/5)) are all FALSE; 40-digit numerics "
               "separated by factors ≈7–11. The D₅ product does NOT "
               "reproduce the Σ(2,3,5) vacuum row.",
    )
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
