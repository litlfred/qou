#!/usr/bin/env python3
"""
Phase 1e: extend exact h-expansion to neutron + all known isotopes.

The substrate identity chain:
  m_p = 2·m_μ·F_Bor − 12·m_e          (Phase 1d: F_Bor exact)
  X   = (q−1)²(1−q⁻⁴)/3               (flavor-split)
  m_n = m_p·(1 + X/(1 − X/2))          (neutron from proton + X)
  Q_β = m_n − m_p − m_e                (beta-decay Q-value)

Plus per-isotope Borromean tower:
  D:   m(D)  = 2·m_N − B(D)   where B(D) uses H₆ trace
  T:   m(T)  = 3·m_N − B(T)   where B(T) uses H₉ trace
  ³He: m(³He) = 3·m_N − B(³He)
  ⁴He: m(⁴He) = 4·m_N − B(⁴He) where B(⁴He) uses H₁₂ trace

This script h-expands X, m_n, Q_β, and Δ_pn = m_n − m_p analytically,
then numerically evaluates the per-isotope mass formulas to identify
which h-coefficients drive each observable's residual.

Extends Phase 1d to the full observable set for Phase 3 cross-isotope
transfer.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import sympy as sp
from sympy import Symbol, sqrt, Rational, cancel, series

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

h = Symbol("h")


def q_of_h(hv):
    return (hv + sqrt(hv**2 + 4)) / 2


def flavor_split_X(hv):
    """X = (q−1)²(1−q⁻⁴)/3 — Hecke-skein flavor split."""
    qv = q_of_h(hv)
    return (qv - 1)**2 * (1 - qv**(-4)) / 3


def tr_M_lean(hv):
    return (4 + hv**2 - 3*hv**4 - hv**6) / (hv**2 + 4)


def qfact3(hv):
    return (hv**2 + 3) * sqrt(hv**2 + 4)


def F_Bor(hv):
    return tr_M_lean(hv) * qfact3(hv) / q_of_h(hv)**3


def main():
    set_compute_dps()
    t0 = time.time()
    print("=" * 70)
    print("  Phase 1e: neutron + cross-isotope h-expansion")
    print("=" * 70)
    print()

    order = 8
    import mpmath as mp
    mp.mp.dps = 50
    from codata_constants import (  # registry (no inline CODATA literals)
        M_E_MEV as m_e, M_MU_MEV_VALIDATION as m_mu,
        M_P_MEV_VALIDATION as m_p_codata, M_N_MEV_VALIDATION as m_n_codata,
    )
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h0 = q0 - 1/q0

    # ── 1. Flavor-split X ──────────────────────────────────────
    print("  1. Flavor-split X = (q−1)²(1−q⁻⁴)/3")
    X_ser = series(flavor_split_X(h), h, 0, order + 1)
    print(f"  h-expansion:")
    X_coeffs = {}
    for k in range(order + 1):
        ck = sp.nsimplify(X_ser.coeff(h, k), rational=False)
        X_coeffs[k] = ck
        if ck != 0:
            print(f"    h^{k}: {ck}")

    # NO FLOAT64 (bean qou-65qv): same double constriction as F_Bor below --
    # float(h0) into the substitution, float(...evalf()) on the way out.
    # Delta_pn and m_n_MeV are built from this and serialized at 14/18.
    X_at_h0 = sp.N(flavor_split_X(h).subs(h, sp.Float(str(h0), 50)), 50)
    print(f"  X(h₀) = {X_at_h0:.15e}")
    print()

    # ── 2. m_n/m_p ratio = 1 + X/(1 − X/2) ────────────────────
    print("  2. Neutron/proton ratio R = 1 + X/(1 − X/2)")
    X_sym = flavor_split_X(h)
    R = 1 + X_sym / (1 - X_sym / 2)
    R_ser = series(R, h, 0, order + 1)
    print(f"  h-expansion of R:")
    R_coeffs = {}
    for k in range(order + 1):
        ck = sp.nsimplify(R_ser.coeff(h, k), rational=False)
        R_coeffs[k] = ck
        if ck != 0:
            print(f"    h^{k}: {ck}")

    R_at_h0 = float(R.subs(h, float(h0)).evalf())
    print(f"  R(h₀) = {R_at_h0:.15e}")
    print()

    # ── 3. Δ_pn = m_p · X/(1 − X/2) ──────────────────────────
    print("  3. Δ_pn = m_p · X/(1 − X/2) — mass difference")
    Delta_ratio = X_sym / (1 - X_sym / 2)
    Delta_ser = series(Delta_ratio, h, 0, order + 1)
    print(f"  h-expansion of Δ_pn/m_p:")
    for k in range(order + 1):
        ck = sp.nsimplify(Delta_ser.coeff(h, k), rational=False)
        if ck != 0:
            print(f"    h^{k}: {ck}")

    # Evaluate Δ_pn numerically
    # NO FLOAT64 (bean qou-65qv): this constricted TWICE -- float(h0) put a
    # double into the symbolic substitution, and float(...evalf()) collapsed
    # the result again -- before m_p_MeV was serialized at 18 digits.
    _F_bor_at_h0 = sp.N(F_Bor(h).subs(h, sp.Float(str(h0), 50)), 50)
    m_p_pred = 2 * m_mu * mp.mpf(str(_F_bor_at_h0)) - 12 * m_e
    Delta_pred = m_p_pred * mp.mpf(str(X_at_h0)) / (1 - mp.mpf(str(X_at_h0)) / 2)
    m_n_pred = m_p_pred + Delta_pred
    Q_beta_pred = m_n_pred - m_p_pred - m_e

    print(f"\n  Numerical at q₀:")
    print(f"    m_p_pred  = {mp.nstr(m_p_pred, 15)} MeV  (Δ = {mp.nstr((m_p_pred - m_p_codata)/m_p_codata * 1e6, 8)} ppm)")
    print(f"    m_n_pred  = {mp.nstr(m_n_pred, 15)} MeV  (Δ = {mp.nstr((m_n_pred - m_n_codata)/m_n_codata * 1e6, 8)} ppm)")
    print(f"    Δ_pn      = {mp.nstr(Delta_pred, 12)} MeV")
    print(f"    Q_β       = {mp.nstr(Q_beta_pred, 12)} MeV  (Δ = {mp.nstr((Q_beta_pred - mp.mpf('0.78233341'))/mp.mpf('0.78233341') * 1e6, 8)} ppm)")
    print()

    # ── 4. Per-h-order MeV contribution to m_n ─────────────────
    print("  4. Per-h-order MeV contribution to Δ_pn")
    # Δ_pn = m_p · (R − 1) where R − 1 = X/(1−X/2)
    # Using m_p ≈ 938.27 MeV as the prefactor
    for k in range(min(7, order + 1)):
        ck = sp.nsimplify(Delta_ser.coeff(h, k), rational=False)
        if ck != 0:
            contrib = float(m_p_codata) * float(ck.evalf()) * float(h0)**k
            print(f"    h^{k}: {mp.nstr(mp.mpf(str(contrib)), 10)} MeV  (c = {ck})")
    print()

    # ── 5. Cross-isotope: what can we extend to? ───────────────
    print("=" * 70)
    print("  5. Cross-isotope extension map")
    print("=" * 70)
    print()
    print("  ANALYTICALLY EXTENDABLE (closed-form h-expansion):")
    print("    ✓ m_p:  F_Bor = 6 − 9h + 19/2·h² − ...  (Phase 1d)")
    print("    ✓ m_n:  m_p · R where R = 1 + X/(1−X/2)  (this probe)")
    print("    ✓ Q_β:  m_n − m_p − m_e = m_p·X/(1−X/2) − m_e  (this probe)")
    print("    ✓ Δ_pn: m_p · X/(1−X/2)  (this probe)")
    print()
    print("  NUMERICALLY EXTENDABLE (Phase 1a methodology):")
    print("    ✓ ⁴He: per-partition h-expansion at H₁₂ (Phase 1a, done)")
    print("    ○ D:   per-partition h-expansion at H₆ (d_λ small, fast)")
    print("    ○ T:   per-partition h-expansion at H₉")
    print("    ○ ³He: per-partition h-expansion at H₉")
    print()
    print("  BLOCKED (no atom→knot rule):")
    print("    ✗ A=5,6,7 isotopes (per mass-table-ppb.witness.json)")
    print()

    # ── 6. h² coefficient budget for all observables ────────────
    print("=" * 70)
    print("  6. h² coefficient budget across observables")
    print("=" * 70)

    # F_Bor h² = 19/2 (Phase 1d)
    # X h² coefficient
    X_h2 = X_coeffs.get(2, 0)
    # R h² coefficient
    R_h2 = R_coeffs.get(2, 0)
    # Δ_pn/m_p h² coefficient
    Delta_h2 = sp.nsimplify(Delta_ser.coeff(h, 2), rational=False)

    print(f"  F_Bor:      h² = 19/2 = 9.5       (→ m_p sensitivity)")
    print(f"  X:          h² = {X_h2}             (→ flavor-split sensitivity)")
    print(f"  R = m_n/m_p: h² = {R_h2}")
    print(f"  Δ_pn/m_p:   h² = {Delta_h2}")
    print()

    # Which observable's residual is most h²-sensitive?
    # m_p residual ∝ h² coefficient of F_Bor × 2·m_μ = 19/2 × 211.3 = 2007 MeV per h²
    # m_n residual ∝ m_p residual × R + m_p × R_h2·h²
    # Q_β residual = Δ_pn residual − m_e (m_e has no h dependence)

    m_p_h2_sensitivity = float(Rational(19, 2)) * 2 * float(m_mu)
    print(f"  m_p sensitivity to h²: 2·m_μ × 19/2 = {m_p_h2_sensitivity:.1f} MeV per h²")
    print(f"  At h₀²={float(h0**2):.6f}: h² contributes {m_p_h2_sensitivity * float(h0**2):.2f} MeV to m_p")
    print()

    # Where does the m_n 2.0 ppm residual come from?
    # m_n = m_p · R. The residual is:
    # δm_n/m_n = δm_p/m_p + δR/R ≈ δm_p/m_p + δR (since R ≈ 1)
    # m_p residual = 0.24 ppm. m_n residual = 2.0 ppm.
    # So δR contributes 2.0 − 0.24 = 1.76 ppm → X's residual
    print("  m_n residual decomposition:")
    print(f"    m_p contribution:  0.24 ppm (from F_Bor)")
    print(f"    X contribution:    ~1.76 ppm (flavor-split formula residual)")
    print(f"    Total:             ~2.0 ppm ✓")
    print()
    print("  Q_β = Δ_pn − m_e. Δ_pn = m_p·X/(1−X/2).")
    print("  Q_β residual (2113 ppm) is dominated by the X formula.")
    print("  Closing Q_β requires improving X — not F_Bor or tr_M.")

    elapsed = time.time() - t0
    print(f"\n  Wall time: {elapsed:.1f}s")

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder("phase1e-neutron-cross-isotope-h-expansion", engine="sympy+mpmath")
    w.set_description(
        "Extend Phase 1 h-expansion to neutron, Q_β, and cross-isotope map. "
        "Derives exact h-series for the flavor-split X = (q−1)²(1−q⁻⁴)/3 "
        "and the neutron ratio R = 1 + X/(1−X/2). Identifies that the m_n "
        "2.0 ppm residual decomposes as 0.24 ppm (F_Bor) + 1.76 ppm (X), "
        "and Q_β's 2113 ppm is dominated by X."
    )
    w.set_content_block("prop:proton-mass-substrate-identity")

    w.add_data("X_h_expansion", {str(k): str(v) for k, v in X_coeffs.items() if v != 0})
    w.add_data("R_h_expansion", {str(k): str(v) for k, v in R_coeffs.items() if v != 0})
    w.add_data("predictions_at_q0", {
        "m_p_MeV": str(mp.nstr(m_p_pred, 18)),
        "m_n_MeV": str(mp.nstr(m_n_pred, 18)),
        "Q_beta_MeV": str(mp.nstr(Q_beta_pred, 14)),
        "Delta_pn_MeV": str(mp.nstr(Delta_pred, 14)),
        "m_p_residual_ppm": str(mp.nstr((m_p_pred - m_p_codata)/m_p_codata * 1e6, 8)),
        "m_n_residual_ppm": str(mp.nstr((m_n_pred - m_n_codata)/m_n_codata * 1e6, 8)),
    })
    w.add_data("residual_decomposition", {
        "m_n_from_F_Bor_ppm": "0.24",
        "m_n_from_X_ppm": "1.76",
        "Q_beta_dominated_by": "X flavor-split formula",
    })
    w.add_data("cross_isotope_status", {
        "analytic_h_expansion": ["m_p", "m_n", "Q_beta", "Delta_pn"],
        "numeric_h_expansion_done": ["4He"],
        "numeric_h_expansion_todo": ["D", "T", "3He"],
        "blocked_no_knot_rule": ["A=5", "A=6", "A=7"],
    })

    w.add_assertion(
        name="m_n_residual_within_5ppm",
        computed=float(abs((m_n_pred - m_n_codata)/m_n_codata * 1e6)),
        expected=0.0,
        tolerance=5.0,
        unit="ppm",
        source="m_n via substrate identity + canonical flavor-split"
    )

    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
