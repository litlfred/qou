#!/usr/bin/env python3
"""ksel3_modular_double_probe.py — kernel selection principle 3: Faddeev
modular-double covariance of the (REP) kernel family.

Bean qou-q5zq. AUDIT-ONLY — scope-(a), NO FIT, nothing wired; the target
conjecture (conj:schwinger-measure-computational-time, hypothesis (REP))
stays a conjecture. Sibling of ksel1/ksel2 (parallel agents, disjoint
namespaces) and of rep_jackson_identification_probe.py (bean qou-u5p0),
whose u-translate continuum this probe re-organizes in the modular frame.

STRUCTURAL FINDING (derived by hand, asserted symbolically BEFORE the
numeric layer — formalize-first):

  In log coordinates t = ln s, with L := ln q̃ = (ln q)/2, the u-translate
  atomic B-factor (atoms u·q̃^j, masses ∝ q̃^{−j(j+1)/2}u^{−j}; Attack B /
  R4 of rep_jackson_identification_probe.py) is EXACTLY the lattice
  sampling, on ln u + Lℤ, of ONE fixed Gaussian

      g(t) = exp(−(t − μ̂)²/(2σ²)),   μ̂ = −L/2,  σ² = L,

  and that Gaussian is EXACTLY the log-normal a.c. B-factor of Attack B
  (σ² = ln q /2 = L, μ̂ = −ln q /4 = −L/2). So the "two known
  realizations" of the balanced B-factor are ONE object: the atomic one
  is its lattice sampling, the a.c. one its continuum (equivalently, the
  a.c. kernel is the zero dual-Fourier mode = the Haar average of the
  atomic family over the translate circle u ∈ ℝ_{>0}/q̃^ℤ). Poisson
  summation (the Jacobi imaginary transform) converts each lattice sum
  into a dual-lattice sum with dual nome

      Q_d = exp(−4π²/L)      (pairing  L · ln(1/Q_d) = 4π²),

  and — because σ² equals the lattice step L — the k-th exponential
  moment shifts the sampling by the LATTICE vector k·L, so every dual
  mode m carries the SAME normalized moment ladder q^{k(k−1)/4}: the
  moment functional is blind to the whole dual-mode sector. The R4
  u-continuum indeterminacy IS the nonzero dual-mode sector, exactly.

WHAT THIS PROBE CHECKS:

  M1  (sympy exact) The lattice-Gaussian identification: the mass
      exponent −L·j(j+1)/2 − j·ln u equals −(t_j − μ̂)²/(2L) + C(u) with
      t_j = ln u + jL, μ̂ = −L/2, C(u) = (ln u + L/2)²/(2L)·(−1); and the
      Attack-B log-normal parameters (σ² = ln q /2, μ̂ = −ln q /4) equal
      (L, −L/2) under q = q̃².
  M2  (sympy exact) Dual-mode moment covariance: for the complex shift
      z = k + 2πi m/L,   z·μ̂ + z²L/2 = L·k(k−1)/2 + [2πi m μ̂/L −
      2π²m²/L] + 2πi·m·k, and e^{2πi m k} = 1 (integers) — so mode-m's
      contribution to the k-th moment is (mode-m mass) × q^{k(k−1)/4}:
      every dual mode has the same normalized moments. Also
      e^{L·k(k−1)/2} = q^{k(k−1)/4} at q = q̃² = e^{2L}, exact.
  M3  (mpmath 80 dps, tol 1e−40) The Poisson / Jacobi-imaginary identity
      at an exercised base L = 1 (q̃ = e): direct lattice sum Z(u) equals
      √(2π/L)·Σ_m e^{−2π²m²/L}·e^{2πi m φ_u}, φ_u = (ln u − μ̂)/L, at
      u ∈ {1, 1.3, e^{−1/2}}; classical-θ tie-in (Gaussian-sampled sums,
      the u-constant e^{C(u)} absorbed): Z(1) = θ₂(0, e^{−L/2}) and
      Z(q̃^{−1/2}) = θ₃(0, e^{−L/2}) (mpmath.jtheta, independent
      implementation).
  M4  (mpmath 80 dps) The dual-pair verdict made quantitative at L = 1:
      (a) two members (u = 1, u = 1.3) share all normalized moments
      k = 0..8 (rel < 1e−40) yet have total-variation distance 1
      (disjoint supports) — the difference lives entirely in the
      moment-blind dual-mode sector; (b) the circle average over
      ln u ∈ [0, L) of the unnormalized family equals the continuum
      (log-normal) object: moment-by-moment (k = 0..4) AND for a
      non-moment test function (rel < 1e−35, tanh-sinh quadrature).
  M5  (sympy exact + mpmath) Selection classification on the translate
      circle via the dual coefficients c_m(u) ∝ e^{−2π²m²/L}e^{2πimφ_u}:
      * u ≡ 1        (φ = 1/2):  c_m ∝ (−1)^m  — θ₂-characteristic;
      * u ≡ q̃^{∓1/2} (φ = 0):    c_m ∝ +1      — θ₃-characteristic;
      * reality of ALL c_m  ⟺  2φ ∈ ℤ  ⟺  bar-reflection σ-invariance
        (the R4 fixed pair — the modular frame RE-DERIVES σ, adds no cut;
        the σ-symmetrized continuum has cos-real duals for EVERY u);
      * positivity of ALL c_m ⟺ φ ∈ ℤ — UNIQUE point u ≡ q̃^{±1/2}
        (exhibits: φ = 1/2 fails at m = 1; generic u = 1.3 fails at
        m = 2);
      * Jacobi characteristic bookkeeping (classical imaginary
        transform, mpmath, rel < 1e−45): θ₃(e^{−πx}) = x^{−1/2}·
        θ₃(e^{−π/x}) (θ₃ shape-SELF-dual) and θ₂(e^{−πx}) = x^{−1/2}·
        θ₄(e^{−π/x}) (θ₂ ↦ θ₄, NOT shape-fixed) — so the unique
        shape-self-dual atomic member is u ≡ q̃^{±1/2}, which is NOT the
        Attack-B presentation u = 1.
  M6  (mpmath 80 dps, both q₀ pins) Regime map + scale facts at the real
      substrate: b² = ±i·t/(2π) (t = ln q₀) — verify e^{2πib²} ∈
      {1/q₀, q₀} per branch (the corpus b-map, phi_b_substrate_regime.py,
      cited not re-derived); the modular-double pairing ln q · ln q̃ = 4π²
      (numerically, 1e−45); the EXACT resonance identities
      q̃_F := e^{−4π²/t} = (q̃_W8b)⁵ (W8b cusp variable, level 5) and
      kernel first-dual-mode amplitude e^{−2π²/L} = q̃_F, Q_d = q̃_F²
      (L = t/2); NO measure-level fixed point at the substrate:
      L′ = 4π²/L with L′/L ≈ 1.45×10⁴ ≫ 1 (self-dual locus L = 2π ⟺
      q₀ = e^{4π} ≈ 2.87×10⁵); and the substrate flatness statement
      |Z(u)·√(L/2π) − 1| < 1e−55 for u ∈ {1, 1.3} (the analytic dual
      correction 2·q̃_F·|cos| ≈ 10^{−164.3} is below any resolvable
      precision — atomic and a.c. realizations are numerically
      indistinguishable at the substrate).

VERDICT SHAPE (scope-(a)): the dual-pair claim is EXACT — the atomic and
a.c. realizations are one Gaussian seen in dual frames (lattice sampling
vs continuum / zero mode). The selection outcome is honest-graded: strict
measure-level self-duality is EMPTY at the substrate (the transform maps
base L to 4π²/L ≠ L); dual-coefficient reality exactly re-derives the σ
pair (no new cut; the symmetrized continuum survives); dual-coefficient
positivity / θ₃ shape-self-duality picks the UNIQUE member u ≡ q̃^{±1/2};
modular inertness (no dual modes at all) picks the log-normal a.c.
member. Distinct covariance notions pick DISTINCT objects, so
"modular-double covariance" is a symmetry-normalization, not a
derivation, absent an independent corpus input. Nothing here proves or
refutes the conjecture.

Exit 0 iff all assertions pass. Witness:
ksel3-modular-double.witness.json (audit-only).
Audit doc: docs/audits/2026-08-01-ksel3-modular-double-covariance.md.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _bridge

import json  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import jtheta, mp, mpc, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

TOL_EXACT = 0        # sympy exact comparisons
TOL_40 = 1e-40       # 80-dps Poisson / moment identities
TOL_45 = 1e-45       # 80-dps classical-theta / pairing identities
TOL_55 = 1e-55       # substrate flatness floor (dual corr ~ 1e-164)
L_TEST = "1"         # exercised base for M3-M5 (q̃ = e — dual corr ~ 3e-9)
U_GENERIC = "1.3"    # generic translate parameter (matches rep probe R4)

# q₀, both pins, 50-digit strings with provenance (muon from the canonical
# witness; proton from qou_substrate.constants Q_50_DIGIT_STR).
_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
# tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR
# (proton re-pin 2026-05-28; _solve_q_proton_f64 + mpmath refine):
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"


# ---------------------------------------------------------- lattice helpers

def gauss(t: mpf, L: mpf) -> mpf:
    """The ONE Gaussian: g(t) = exp(−(t − μ̂)²/(2σ²)), μ̂ = −L/2, σ² = L —
    simultaneously the log-density of the Attack-B log-normal B-factor
    and (M1) the mass profile of every u-translate atomic B-factor."""
    return mp.exp(-(t + L / 2) ** 2 / (2 * L))


def z_lattice(a: mpf, L: mpf, J: int) -> mpf:
    """Direct lattice sum Z(u) = Σ_j g(ln u + jL), a = ln u."""
    return sum(gauss(a + j * L, L) for j in range(-J, J + 1))


def n_k_lattice(a: mpf, L: mpf, k: int, J: int) -> mpf:
    """Unnormalized k-th exponential moment Σ_j e^{k t_j} g(t_j)."""
    return sum(mp.exp(k * (a + j * L)) * gauss(a + j * L, L)
               for j in range(-J, J + 1))


def z_dual(a: mpf, L: mpf, M: int) -> mpc:
    """Poisson dual frame: √(2π/L)·Σ_m e^{−2π²m²/L}·e^{2πi m φ},
    φ = (a − μ̂)/L = (a + L/2)/L."""
    phi = (a + L / 2) / L
    tot = mpc(0)
    for m in range(-M, M + 1):
        tot += mp.exp(-2 * mp.pi ** 2 * m ** 2 / L) * \
            mp.exp(mpc(0, 2 * mp.pi * m) * phi)
    return mp.sqrt(2 * mp.pi / L) * tot


# ---------------------------------------------------------------- Block M1

def block_m1_gaussian_identification(wb: WitnessBuilder) -> None:
    """M1: the u-translate atomic masses ARE lattice samples of the
    Attack-B log-normal Gaussian — sympy exact."""
    _ok: list[bool] = []
    L, a = sp.symbols("L a", positive=True, real=True)
    j = sp.symbols("j", integer=True)
    t_j = a + j * L
    mu = -L / 2
    log_mass = -L * j * (j + 1) / 2 - j * a          # ln[q̃^{−j(j+1)/2}u^{−j}]
    C = -(a + L / 2) ** 2 / (2 * L)                  # u-only constant
    d = sp.expand(-(t_j - mu) ** 2 / (2 * L) - C - log_mass)
    _ok.append(bool(d == 0))
    assert _ok[-1], d
    # Attack-B log-normal parameters under q = q̃² = e^{2L}:
    ln_q = 2 * L
    _ok.append(bool(sp.simplify(ln_q / 2 - L) == 0))
    assert _ok[-1]
    _ok.append(bool(sp.simplify(-ln_q / 4 - mu) == 0))
    assert _ok[-1]
    wb.add_assertion(
        "gaussian_identification_exact", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="sympy exact: the u-translate atomic mass exponent "
               "−L·j(j+1)/2 − j·ln u equals −(t_j − μ̂)²/(2L) + C(u) at "
               "t_j = ln u + jL, μ̂ = −L/2 (C(u) independent of j), and the "
               "Attack-B log-normal B-factor parameters σ² = ln q /2, "
               "μ̂ = −ln q /4 equal (L, −L/2) at L = ln q̃ = (ln q)/2 — the "
               "atomic (theta) and a.c. (log-normal) realizations of the "
               "balanced B-factor are ONE Gaussian: lattice sampling on "
               "ln u + Lℤ vs continuum. The 'two realizations' of Attack B "
               "§3 are one object seen in dual frames")


# ---------------------------------------------------------------- Block M2

def block_m2_dual_mode_covariance(wb: WitnessBuilder) -> None:
    """M2: every Poisson dual mode carries the same normalized moment
    ladder q^{k(k−1)/4} — the moment functional is blind to the dual-mode
    sector. Sympy exact."""
    _ok: list[bool] = []
    L = sp.symbols("L", positive=True)
    k, m = sp.symbols("k m", integer=True)
    mu = -L / 2
    z = k + 2 * sp.pi * sp.I * m / L
    lhs = z * mu + z ** 2 * L / 2
    rhs = L * k * (k - 1) / 2 \
        + (2 * sp.pi * sp.I * m * mu / L - 2 * sp.pi ** 2 * m ** 2 / L) \
        + 2 * sp.pi * sp.I * m * k
    d = sp.expand(lhs - rhs)
    _ok.append(bool(d == 0))
    assert _ok[-1], d
    # e^{2πi m k} = 1 for integers (concrete exact check on a grid):
    for mm in range(-3, 4):
        for kk in range(0, 6):
            _ok.append(bool(sp.exp(2 * sp.pi * sp.I * mm * kk) == 1))
            assert _ok[-1], (mm, kk)
    # e^{L·k(k−1)/2} = q^{k(k−1)/4} at q = e^{2L}: exact.
    q = sp.exp(2 * L)
    d2 = sp.simplify(sp.exp(L * k * (k - 1) / 2) - q ** (k * (k - 1) / 4))
    _ok.append(bool(d2 == 0))
    assert _ok[-1], d2
    wb.add_assertion(
        "dual_mode_moment_covariance_exact", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="sympy exact: with z = k + 2πi m/L, the Gaussian moment "
               "exponent z·μ̂ + z²L/2 splits as L·k(k−1)/2 + (mode-m mass "
               "exponent) + 2πi·mk, and e^{2πi·mk} = 1 — so the m-th "
               "Poisson dual mode contributes to the k-th exponential "
               "moment exactly (its own mass) × e^{L·k(k−1)/2} = (mass) × "
               "q^{k(k−1)/4}. EVERY dual mode carries the same normalized "
               "moment ladder: the balanced moment functional is blind to "
               "the entire dual-mode sector. Mechanism: σ² = L (variance = "
               "lattice step), so the k-th moment shifts the sampling by "
               "the LATTICE vector kL. The R4 u-continuum indeterminacy IS "
               "the nonzero-dual-mode sector, exactly")


# ---------------------------------------------------------------- Block M3

def block_m3_poisson_identity(wb: WitnessBuilder) -> None:
    """M3: the Poisson / Jacobi-imaginary identity, numerically exact at
    the exercised base L = 1, plus classical-theta tie-ins."""
    L = mpf(L_TEST)
    worst = mpf(0)
    for a in (mpf(0), mp.log(mpf(U_GENERIC)), -L / 2):
        direct = z_lattice(a, L, 60)
        dual = z_dual(a, L, 8)
        assert abs(dual.imag) < mpf(str(TOL_45)), dual.imag
        worst = max(worst, abs(direct / dual.real - 1))
    assert worst < mpf(str(TOL_40)), worst
    # classical-theta tie-in (mpmath.jtheta — independent implementation):
    p = mp.exp(-L / 2)
    # z_lattice samples the normalized Gaussian g, which absorbs the
    # j-independent constant e^{C(u)} (= e^{−L/8} at u = 1 relative to the
    # raw masses q̃^{−j(j+1)/2}), so Z(1) = θ₂(0, p) directly:
    d_th2 = abs(z_lattice(mpf(0), L, 60) / jtheta(2, 0, p) - 1)
    d_th3 = abs(z_lattice(-L / 2, L, 60) / jtheta(3, 0, p) - 1)
    assert max(d_th2, d_th3) < mpf(str(TOL_45)), (d_th2, d_th3)
    wb.add_assertion(
        "poisson_jacobi_identity", computed=mp.nstr(worst, 5), expected="0",
        tolerance=TOL_40,
        source=f"L = {L_TEST} (q̃ = e), 80 dps: the direct lattice sum "
               f"Z(u) = Σ_j g(ln u + jL) equals the Poisson dual frame "
               f"√(2π/L)·Σ_m e^(−2π²m²/L)·e^(2πi m φ_u) at u = 1, "
               f"u = {U_GENERIC}, u = e^(−1/2) (rel < 1e−40; first dual "
               f"correction ~ 5e−9, so the check is two-sided nontrivial); "
               f"and the family lands on the classical theta frame "
               f"(Gaussian-sampled sums, u-constant absorbed): "
               f"Z(1) = θ₂(0, e^(−L/2)), Z(q̃^(−1/2)) = "
               f"θ₃(0, e^(−L/2)) via mpmath.jtheta (rel < 1e−45). The "
               f"dual nome is Q_d = e^(−4π²/L): the modular pairing "
               f"L·ln(1/Q_d) = 4π²")


# ---------------------------------------------------------------- Block M4

def block_m4_dual_pair(wb: WitnessBuilder) -> None:
    """M4: dual-pair verdict quantitative — moment blindness + circle
    average = log-normal (zero mode)."""
    L = mpf(L_TEST)
    a1, a2 = mpf(0), mp.log(mpf(U_GENERIC))
    # (a) shared normalized moments, disjoint supports
    z1, z2 = z_lattice(a1, L, 80), z_lattice(a2, L, 80)
    worst = mpf(0)
    for k in range(0, 9):
        m1 = n_k_lattice(a1, L, k, 80) / z1
        m2 = n_k_lattice(a2, L, k, 80) / z2
        cont = mp.exp(L * k * (k - 1) / 2)     # = q^{k(k−1)/4}
        worst = max(worst, abs(m1 / cont - 1), abs(m2 / cont - 1))
    assert worst < mpf(str(TOL_40)), worst
    # total-variation distance: grids ℤ vs ln1.3 + ℤ are disjoint
    # (frac(ln 1.3) ≈ 0.2624 — atom sets never meet), so TV = 1.
    frac = mp.frac(abs(a1 - a2) / L)
    grid_gap = min(frac, 1 - frac)
    assert grid_gap > mpf("0.05"), grid_gap
    tv = mpf(1)   # disjoint supports of two probability measures
    # (b) circle average of the UNNORMALIZED family = continuum object
    worst_avg = mpf(0)
    for k in range(0, 5):
        avg = mp.quad(lambda aa, kk=k: n_k_lattice(aa, L, kk, 80),
                      [0, L]) / L
        cont = mp.sqrt(2 * mp.pi * L) * mp.exp(L * k * (k - 1) / 2) / L
        worst_avg = max(worst_avg, abs(avg / cont - 1))
    # non-moment test function φ(t) = e^{−(t−0.3)²/2}
    def phi(t):
        return mp.exp(-(t - mpf("0.3")) ** 2 / 2)

    def lattice_phi(aa):
        return sum(phi(aa + j * L) * gauss(aa + j * L, L)
                   for j in range(-80, 81))
    avg_phi = mp.quad(lattice_phi, [0, L]) / L
    cont_phi = mp.quad(lambda t: phi(t) * gauss(t, L),
                       [-mp.inf, mp.inf]) / L
    worst_avg = max(worst_avg, abs(avg_phi / cont_phi - 1))
    assert worst_avg < mpf("1e-35"), worst_avg
    wb.add_assertion(
        "dual_pair_moment_blind_circle_average",
        computed=mp.nstr(max(worst, worst_avg), 5), expected="0",
        tolerance=1e-35,
        source=f"L = {L_TEST}, 80 dps: (a) the members u = 1 and "
               f"u = {U_GENERIC} share ALL normalized moments k = 0..8 "
               f"with the continuum ladder q^(k(k−1)/4) (rel < 1e−40) yet "
               f"have DISJOINT supports (grid offset {mp.nstr(grid_gap, 5)} "
               f"of a step) — total-variation distance 1: the difference "
               f"measure lives entirely in the moment-blind dual-mode "
               f"sector (M2); (b) the circle (Haar) average over "
               f"ln u ∈ [0, L) of the unnormalized atomic family equals "
               f"the continuum Gaussian object moment-by-moment (k = 0..4) "
               f"AND against a non-moment test function (rel < 1e−35, "
               f"tanh-sinh quadrature): the log-normal a.c. B-factor is "
               f"EXACTLY the zero dual mode / circle average of the atomic "
               f"family. DUAL-PAIR VERDICT: exact — one object, two frames")
    wb.add_data("tv_distance_u1_vs_generic", mp.nstr(tv, 3))


# ---------------------------------------------------------------- Block M5

def block_m5_selection(wb: WitnessBuilder) -> None:
    """M5: selection classification on the translate circle — dual
    coefficients, reality = σ, positivity = θ₃ point, Jacobi
    characteristic bookkeeping."""
    # exact characteristic values of the phase φ_u = (ln u − μ̂)/L:
    L_s, a_s = sp.symbols("L a", positive=True, real=True)
    phi_s = (a_s + L_s / 2) / L_s
    assert sp.simplify(phi_s.subs(a_s, 0) * 2 - 1) == 0          # u=1: φ=1/2
    # u = q̃^{−1/2} ⇒ a = −L/2 ⇒ φ = 0 (formal substitution, exact):
    assert sp.simplify(phi_s.subs(a_s, -L_s / 2)) == 0
    # c_m phases: φ = 1/2 ⇒ e^{2πim/2} = (−1)^m; φ = 0 ⇒ 1 (exact):
    m_s = sp.symbols("m", integer=True)
    assert sp.simplify(sp.exp(sp.pi * sp.I * m_s) - (-1) ** m_s) == 0
    # reality ⟺ 2φ ∈ ℤ: sufficiency exact ((±1)^m real); necessity via
    # m = 1 at the generic point (numeric below). σ-equivalence: 2φ ∈ ℤ ⟺
    # 2·ln u ∈ Lℤ — the R4 σ-invariance condition (same congruence).
    L = mpf(L_TEST)
    a_gen = mp.log(mpf(U_GENERIC))
    phi_gen = (a_gen + L / 2) / L
    assert abs(mp.sin(2 * mp.pi * phi_gen)) > mpf("0.1")   # c_1 not real
    # positivity ⟺ φ ∈ ℤ: φ = 1/2 fails at m = 1 (cos π = −1, exact):
    assert sp.simplify(sp.cos(sp.pi) + 1) == 0
    # generic u fails: search smallest m with cos(2πmφ) < −0.1:
    m_neg = None
    for m in range(1, 31):
        if mp.cos(2 * mp.pi * m * phi_gen) < mpf("-0.1"):
            m_neg = m
            break
    assert m_neg is not None
    # Jacobi characteristic bookkeeping (classical imaginary transform):
    worst_j = mpf(0)
    for x in (mpf("1.7"), L / (2 * mp.pi)):
        p, pd = mp.exp(-mp.pi * x), mp.exp(-mp.pi / x)
        worst_j = max(
            worst_j,
            abs(jtheta(3, 0, p) / (jtheta(3, 0, pd) / mp.sqrt(x)) - 1),
            abs(jtheta(2, 0, p) / (jtheta(4, 0, pd) / mp.sqrt(x)) - 1))
    assert worst_j < mpf(str(TOL_45)), worst_j
    wb.add_assertion(
        "selection_classification", computed=mp.nstr(worst_j, 5),
        expected="0", tolerance=TOL_45,
        source=f"sympy exact + 80 dps at L = {L_TEST}: dual coefficients "
               f"c_m(u) ∝ e^(−2π²m²/L)·e^(2πimφ_u), φ_u = (ln u − μ̂)/L. "
               f"(i) u ≡ 1: φ = 1/2, c_m ∝ (−1)^m (θ₂-characteristic); "
               f"u ≡ q̃^(∓1/2): φ = 0, c_m ∝ +1 (θ₃-characteristic) — "
               f"exact. (ii) REALITY of all c_m ⟺ 2φ ∈ ℤ ⟺ 2·ln u ∈ Lℤ — "
               f"EXACTLY the R4 bar-reflection σ-invariance condition "
               f"(fixed pair u ≡ 1, u ≡ q̃^(1/2)); necessity witnessed at "
               f"u = {U_GENERIC} (|sin 2πφ| = "
               f"{mp.nstr(abs(mp.sin(2 * mp.pi * phi_gen)), 4)}); the "
               f"σ-symmetrized continuum has cos-real duals for EVERY u, "
               f"so reality does NOT cut the continuum. (iii) POSITIVITY "
               f"of all c_m ⟺ φ ∈ ℤ — the UNIQUE point u ≡ q̃^(±1/2); "
               f"φ = 1/2 fails at m = 1 (cos π = −1, exact), generic "
               f"u = {U_GENERIC} fails at m = {m_neg}. (iv) Jacobi "
               f"imaginary transform (mpmath jtheta, rel < 1e−45, x = 1.7 "
               f"and x = L/2π): θ₃(e^(−πx)) = x^(−1/2)·θ₃(e^(−π/x)) — "
               f"θ₃ is shape-SELF-dual; θ₂(e^(−πx)) = x^(−1/2)·"
               f"θ₄(e^(−π/x)) — θ₂ maps to θ₄, NOT shape-fixed. So the "
               f"unique shape-self-dual / dual-positive atomic member is "
               f"u ≡ q̃^(±1/2) — NOT the Attack-B presentation u = 1 "
               f"(which is σ-fixed but θ₂-type, alternating duals)")


# ---------------------------------------------------------------- Block M6

def block_m6_regime_and_scales(wb: WitnessBuilder, q_name: str,
                               q_str: str) -> None:
    """M6: regime map + exact scale/resonance identities at one q₀ pin."""
    q0 = mpf(q_str)
    t = mp.log(q0)
    L = t / 2                                   # kernel base q̃ = √q₀
    two_pi_i = mpc(0, 2 * mp.pi)
    worst = mpf(0)
    # b-map, both branches (corpus: phi_b_substrate_regime.py, cited):
    for sgn, target in ((+1, 1 / q0), (-1, q0)):
        b2 = mpc(0, sgn * t / (2 * mp.pi))      # b² = ±i·t/2π
        qq = mp.exp(two_pi_i * b2)
        worst = max(worst, abs(qq / target - 1))
        # modular-double pairing ln q · ln q̃ = 4π², q̃ = e^{−2πi/b²}:
        pair = mp.log(qq) * (-two_pi_i / b2)
        worst = max(worst, abs(pair / (4 * mp.pi ** 2) - 1))
    # exact resonance identities:
    qF = mp.exp(-4 * mp.pi ** 2 / t)            # convergent-branch dual nome
    qW8b = mp.exp(-4 * mp.pi ** 2 / (5 * t))    # W8b cusp variable (level 5)
    worst = max(worst, abs(qW8b ** 5 / qF - 1))
    worst = max(worst, abs(mp.exp(-2 * mp.pi ** 2 / L) / qF - 1))   # m=1 amp
    worst = max(worst, abs(mp.exp(-4 * mp.pi ** 2 / L) / qF ** 2 - 1))  # Q_d
    assert worst < mpf(str(TOL_45)), worst
    # no measure-level fixed point: L′ = 4π²/L vs L
    Lp = 4 * mp.pi ** 2 / L
    ratio = Lp / L
    assert ratio > mpf("1e3"), ratio
    q_selfdual = mp.exp(4 * mp.pi)              # L = 2π ⟺ q₀ = e^{4π}
    # substrate flatness: dual corrections unresolvable at any corpus dps
    worst_flat = mpf(0)
    for a in (mpf(0), mp.log(mpf(U_GENERIC))):
        worst_flat = max(worst_flat,
                         abs(z_lattice(a, L, 260) * mp.sqrt(L / (2 * mp.pi))
                             - 1))
    assert worst_flat < mpf(str(TOL_55)), worst_flat
    log10_qF = -4 * mp.pi ** 2 / t / mp.log(10)
    log10_qW8b = log10_qF / 5
    wb.add_assertion(
        f"regime_map_and_scales_{q_name}", computed=mp.nstr(worst, 5),
        expected="0", tolerance=TOL_45,
        source=f"q₀ = {q_name} pin ({mp.nstr(q0, 12)}…), 80 dps: b-map "
               f"b² = ±i·t/2π (t = ln q₀) gives e^(2πib²) = 1/q₀ (b₊, "
               f"|q| < 1, convergent modular double) and q₀ (b₋) — the "
               f"corpus b-map (phi_b_substrate_regime.py) reproduced, rel "
               f"< 1e−45; the modular-double pairing ln q · ln q̃ = 4π² "
               f"verified on both branches. EXACT resonance identities: "
               f"q̃_F := e^(−4π²/t) satisfies q̃_F = (q̃_W8b)⁵ (the W8b "
               f"level-5 cusp variable e^(−4π²/(5t)), tau-dictionary "
               f"audit), and the kernel's first Poisson dual amplitude at "
               f"base q̃ = √q₀ (L = t/2) is e^(−2π²/L) = q̃_F with dual "
               f"nome Q_d = e^(−4π²/L) = q̃_F². Scales: log10 q̃_F ≈ "
               f"{mp.nstr(log10_qF, 6)}, log10 q̃_W8b ≈ "
               f"{mp.nstr(log10_qW8b, 6)}. NO measure-level fixed point: "
               f"L′/L = 4π²/L² ≈ {mp.nstr(ratio, 6)} ≫ 1 (self-dual locus "
               f"q₀ = e^(4π) ≈ {mp.nstr(q_selfdual, 6)}); substrate "
               f"flatness |Z(u)·√(L/2π) − 1| < 1e−55 at u ∈ "
               f"{{1, {U_GENERIC}}} (J = 260) — the analytic dual "
               f"correction 2·q̃_F·|cos 2πφ| ~ 10^({mp.nstr(log10_qF, 5)}) "
               f"is below ANY corpus precision floor: atomic and a.c. "
               f"realizations are numerically indistinguishable at the "
               f"substrate; the u-continuum is doubly-exponentially "
               f"degenerate there")


def main() -> int:
    set_compute_dps(80)
    wb = WitnessBuilder("ksel3-modular-double", engine="sympy+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "Kernel selection principle 3 — Faddeev modular-double covariance "
        "of the (REP) kernel family (bean qou-q5zq; audit-only, scope-(a), "
        "NO FIT, nothing wired). STRUCTURAL FINDING (exact): in t = ln s "
        "the u-translate atomic B-factor (rep_jackson_identification R4) "
        "is the lattice sampling on ln u + Lℤ (L = ln q̃) of ONE Gaussian "
        "g(t) = exp(−(t+L/2)²/(2L)) — exactly the Attack-B log-normal "
        "a.c. B-factor (σ² = ln q/2 = L, μ̂ = −ln q/4 = −L/2). Poisson/"
        "Jacobi transform: dual nome Q_d = e^(−4π²/L); because σ² = "
        "lattice step, EVERY dual mode carries the same normalized moment "
        "ladder q^(k(k−1)/4) — the moment functional is blind to the "
        "dual-mode sector, which IS the R4 indeterminacy continuum. "
        "DUAL-PAIR VERDICT: exact — the atomic and a.c. realizations are "
        "one object in dual frames (a.c. = zero dual mode = circle/Haar "
        "average of the atomic family; verified moment-wise and against a "
        "non-moment test function). SELECTION VERDICT (honest-graded): "
        "measure-level self-duality EMPTY at the substrate (base L ↦ "
        "4π²/L, ratio ~1.45e4; self-dual locus q₀ = e^(4π)); "
        "dual-coefficient REALITY ⟺ the R4 bar-reflection σ-invariance "
        "(re-derives the σ pair {u ≡ 1, u ≡ q̃^(1/2)}, adds NO new cut; "
        "symmetrized continuum survives); dual-coefficient POSITIVITY / "
        "θ₃ shape-self-duality picks the UNIQUE atomic member u ≡ "
        "q̃^(±1/2) (NOT the Attack-B u = 1, which is θ₂ ↦ θ₄); modular "
        "INERTNESS (no dual modes) picks the log-normal a.c. member. "
        "Distinct covariance notions pick distinct objects ⇒ modular-"
        "double covariance is a symmetry-normalization, not a derivation. "
        "REGIME MAP (both q₀ pins): real q₀ > 1 ⇒ b² = ±i·ln q₀/2π "
        "(b on e^(∓iπ/4) rays — NOT the unitary |q| = 1 / real-b regime); "
        "the double acts as the real involution ln q ↦ 4π²/ln q. EXACT "
        "resonances: q̃_F = e^(−4π²/ln q₀) = (q̃_W8b)⁵ (the W8b level-5 "
        "cusp variable) = the kernel's first dual amplitude at base √q₀ "
        "(recorded, not physically interpreted); dual corrections at the "
        "substrate ~ 10^(−164.3) — below any corpus precision floor. "
        "Nothing here proves or refutes the conjecture.")
    wb.set_audit_only(
        "docs/audits/2026-08-01-ksel3-modular-double-covariance.md")

    block_m1_gaussian_identification(wb)
    print("M1: lattice-Gaussian identification exact — atomic = sampled "
          "log-normal Gaussian.")
    block_m2_dual_mode_covariance(wb)
    print("M2: dual-mode moment covariance exact — moment functional "
          "blind to dual modes.")
    block_m3_poisson_identity(wb)
    print("M3: Poisson/Jacobi identity + classical-theta tie-in verified "
          "(rel < 1e-40).")
    block_m4_dual_pair(wb)
    print("M4: dual-pair verdict — moment-blind TV-1 pair; a.c. = circle "
          "average / zero mode.")
    block_m5_selection(wb)
    print("M5: selection — reality = sigma (no new cut); positivity/"
          "theta3 unique at u = q-tilde^(1/2); log-normal = inert.")
    for name, qs in (("muon", Q0_MUON_STR), ("proton", Q0_PROTON_STR)):
        block_m6_regime_and_scales(wb, name, qs)
        print(f"M6[{name}]: regime map + exact resonances verified; no "
              f"measure-level fixed point at the substrate.")

    wb.add_data("q0_pins", {
        "muon": Q0_MUON_STR, "proton": Q0_PROTON_STR,
        "source": "computations/q-pinning-50-digit.witness.json (muon, "
                  "canonical 3-CAL layer); qou_substrate.constants."
                  "Q_50_DIGIT_STR (proton, precision layer)"})
    wb.add_data("selection_summary", {
        "measure_level_self_dual": "EMPTY at substrate (L' = 4pi^2/L, "
                                   "ratio ~1.45e4; locus q0 = e^(4pi))",
        "reality_cut": "= bar-reflection sigma-invariance (R4 pair; "
                       "symmetrized continuum survives — no new cut)",
        "positivity_cut": "unique atomic member u = q-tilde^(+-1/2) "
                          "(theta3 characteristic, shape-self-dual)",
        "inertness_cut": "unique a.c. member (log-normal = zero dual "
                         "mode = circle average)",
        "verdict": "distinct covariance notions pick distinct objects — "
                   "symmetry-normalization, not a derivation",
        "promotion_fact_needed": "an independent corpus derivation that "
                                 "the substrate machinery uses the "
                                 "self-dual (theta3) characteristic — "
                                 "e.g. the Phi_b state integrals entering "
                                 "the BINDING chain (currently Q_beta "
                                 "sector only, measurement-tier: "
                                 "qbeta_dladder_ecalle_phib_resummation)"})
    wb.add_data("w8b_resonance", {
        "identity": "q-tilde_F := e^(-4pi^2/ln q0) = (q-tilde_W8b)^5, "
                    "q-tilde_W8b = e^(-4pi^2/(5 ln q0)) — exact at the "
                    "level of definitions (both are the L <-> 4pi^2/L "
                    "involution: level 1 on ln q0 vs Fricke level 5); "
                    "kernel first dual amplitude at base sqrt(q0) equals "
                    "q-tilde_F, dual nome Q_d = q-tilde_F^2",
        "status": "RECORDED, NOT INTERPRETED — no physical identification "
                  "claimed between the W8b cusp chart and the kernel dual "
                  "frame beyond the shared involution shape",
        "w8b_source": "docs/audits/2026-07-24-tau-dictionary-fricke-cusp-"
                      "spin.md (t5(iy) = 125*q-tilde*(1+O(q-tilde)); "
                      "t5(tau)*t5(-1/(5tau)) = 125)"})
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
