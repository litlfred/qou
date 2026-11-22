#!/usr/bin/env python3
"""
Meson mass predictions from the Hecke H_3(q) framework.

Models the pion and kaon mass calculations after the two existing
calibration instances:

  GENERIC STRUCTURE (two instances in QOU)
  =========================================

  Instance 1 — LEPTONIC (CAL-2):
      Mass RATIO of adjacent torus-knot leptons pinned by hyperbolic volume.
          ℏ_q² = Vol(4_1) / (m_μ/m_e)
          q_0  = 1 / (1 - ℏ_q)
      The figure-eight knot 4_1 = closure of (σ_1 σ_2^{-1})² is the
      "transition knot" connecting T_{2,3} (electron) → T_{2,5} (muon).
      Inputs: Vol(4_1), m_μ/m_e.  Output: q_0.

  Instance 2 — HADRONIC (derived from CAL-1 + CAL-2, NOT independent):
      Energy DIFFERENCE between flavor partners via Hecke NF.
          Q_β = m_e · |q_0² - 2q_0 - 1| · (q_0 + 1) / (2 q_0³)
      Q_β is DERIVED from (m_e, q_0) — it is NOT an independent CAL.
      It was historically listed as CAL-3 but is redundant with CAL-2.
      The proton–neutron transition is a flavor-flip cost in H_3(q_0).
      Inputs: m_e, q_0.  Output: Q_β (derived check, 0.168% miss).

  Instance 3 — MESONIC (the genuine CAL-3):
      m_π is genuinely independent of (m_e, q_0) — 8,354 ppm miss on
      best categorical formula. The pion mass carries chiral-condensate
      information absent from the substrate.

      If the meson sector follows the SAME generic pattern, then:
          m_K/m_π = f(q_0)  [some algebraic q-function]
      analogous to m_μ/m_e = Vol(4_1)/ℏ_q².

      The GENERIC PATTERN is:
          mass_ratio = (knot invariant) / (q-function)
      with one instance per independent scale in the framework.

  This script probes ALL candidate formulas systematically.

References:
  - constants.py (substrate q_0 derivation)
  - derived_masses.py (Q_β derivation chain)
  - categorical-meson.md (meson braid M+ in H_3)
  - knot-formula-table.md (quark → torus knot assignments)
  - strangelet-crossing-energy.md (s = T_{2,5}^σ)
"""

import json, time, math
from pathlib import Path

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
try:
    from mpmath import mp, mpf, fabs, sqrt, log, clsin, pi as mppi
    set_compute_dps()
    HAS_MP = True
except ImportError:
    HAS_MP = False
    from decimal import Decimal as mpf

HERE = Path(__file__).resolve().parent

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
mp.dps = 50

# CODATA-2022 / PDG constants — centralised in the registry
# (computations/substrate/codata_constants.py) per the hidden-codata-
# literals consolidation.  The inline literals are kept only on the
# degraded no-mpmath (Decimal) path, since the registry requires mpmath.
if HAS_MP:
    import sys as _sys
    _sys.path.insert(0, str(HERE / "substrate"))
    from codata_constants import (  # noqa: E402
        M_E_MEV, M_PI_PM_MEV_VALIDATION, M_PI_0_MEV_VALIDATION,
        M_K_PM_MEV_VALIDATION, M_K_0_MEV_VALIDATION,
        M_MU_MEV_VALIDATION, M_P_MEV_VALIDATION,
    )
else:
    M_E_MEV                = mpf("0.51099895069")
    M_PI_PM_MEV_VALIDATION = mpf("139.57039")
    M_PI_0_MEV_VALIDATION  = mpf("134.9768")
    M_K_PM_MEV_VALIDATION  = mpf("493.677")
    M_K_0_MEV_VALIDATION   = mpf("497.611")
    M_MU_MEV_VALIDATION    = mpf("105.6583755")
    M_P_MEV_VALIDATION     = mpf("938.27208816")  # noqa: P31 — no-mpmath except-fallback; HAS_MP path imports codata_constants

# ══════════════════════════════════════════════════════════════════
#  SUBSTRATE (from constants.py — replicated here for standalone)
# ══════════════════════════════════════════════════════════════════

VOL_4_1 = 2 * clsin(2, mppi / 3) if HAS_MP else mpf("2.029883212819307")
# CAL-2 m_mu/m_e from the registry, NOT a private copy. This line read
# `mpf("206.7682830")` behind a comment asserting `(= experimental_constants
# .MU_OVER_E)`. That equality ended with PR #4860 / #5149: 206.7682830 is the
# CODATA-2018 figure and the registry now READS the vendored NIST table
# (206.7682827). A private literal cannot track an edition bump, which is the
# whole reason the registry exists -- and here it feeds q0 itself, so the
# staleness propagated into every number this script emits.
from q_parameter import MASS_RATIO_MU_E_STR as _MU_E_STR  # noqa: E402
MASS_RATIO_MU_E = mpf(_MU_E_STR)

HBAR_Q_SQ = VOL_4_1 / MASS_RATIO_MU_E
HBAR_Q = sqrt(HBAR_Q_SQ) if HAS_MP else mpf(str(math.sqrt(float(HBAR_Q_SQ))))
q0 = mpf(1) / (mpf(1) - HBAR_Q)
h_q = q0 - 1/q0
m_e = M_E_MEV  # MeV, CODATA 2022 (registry)

# ══════════════════════════════════════════════════════════════════
#  PDG 2024 (comparison targets — NOT inputs)
# ══════════════════════════════════════════════════════════════════

PDG_PI_PM = M_PI_PM_MEV_VALIDATION   # ± 0.00018 MeV
PDG_PI_0  = M_PI_0_MEV_VALIDATION    # ± 0.0005 MeV
PDG_K_PM  = M_K_PM_MEV_VALIDATION    # ± 0.013 MeV
PDG_K_0   = M_K_0_MEV_VALIDATION     # ± 0.013 MeV
PDG_MU    = M_MU_MEV_VALIDATION      # ± 30e-7 MeV
PDG_P     = M_P_MEV_VALIDATION       # ± 29e-8 MeV

# ══════════════════════════════════════════════════════════════════
#  H_3(q) HECKE ALGEBRA — 6-dimensional basis
# ══════════════════════════════════════════════════════════════════
# Basis: {1, σ_0, σ_1, L+ = σ_0σ_1, L- = σ_1σ_0, e- = σ_0σ_1σ_0}
# Hecke relation: σ_i² = h·σ_i + 1 where h = q - q⁻¹

h = h_q
h2 = h*h
h3 = h2*h

# ── Meson braid NF (from categorical-meson.md) ──────────────────
# M+ = (σ_0σ_1)² · σ_1σ_0 = T_01 · L_H · T_10
# NF(M+) = h·σ_1 + (h²+1)·L+ + h²·L- + (h³+h)·e-

MESON_NF = {
    '1':      mpf(0),
    'sigma_0': mpf(0),
    'sigma_1': h,
    'L+':     h2 + 1,
    'L-':     h2,
    'e-':     h3 + h,
}
MESON_NET = sum(MESON_NF.values())

# ── Proton and neutron typed-crossing nets ───────────────────────
# From beta-decay-energy-scale.witness.json
NET_PROTON  = mpf("0.99913")
NET_NEUTRON = mpf("0.81083")
DELTA_NET_PN = NET_NEUTRON - NET_PROTON  # ≈ -0.18830

# ── Energy scale ─────────────────────────────────────────────────
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E_0 = _qbeta_e0.canonical(q=q0, m_e=m_e)  # tower-summed E_0, canonical (owner ruling 2026-11-20, #8590); was order-zero m_e/(q(q-1))

# ══════════════════════════════════════════════════════════════════
#  INSTANCE 1 CHECK: m_μ/m_e = Vol(4_1) / ℏ_q²
# ══════════════════════════════════════════════════════════════════

ratio_mu_e_predicted = VOL_4_1 / HBAR_Q_SQ
err_mu_e_ppb = float(fabs(ratio_mu_e_predicted - MASS_RATIO_MU_E) / MASS_RATIO_MU_E * 1e9)

# ══════════════════════════════════════════════════════════════════
#  INSTANCE 2 CHECK: Q_β = m_e · |q² - 2q - 1| · (q+1) / (2q³)
# ══════════════════════════════════════════════════════════════════

Q_BETA_CODATA = mpf("0.78233341")
Q_beta_pred = m_e * fabs(q0**2 - 2*q0 - 1) * (q0 + 1) / (2 * q0**3)
err_Qbeta_ppm = float(fabs(Q_beta_pred - Q_BETA_CODATA) / Q_BETA_CODATA * 1e6)

# ══════════════════════════════════════════════════════════════════
#  INSTANCE 3: MESON MASSES — systematic probe
# ══════════════════════════════════════════════════════════════════

# ── Strategy A: m(meson) = net(meson) · E_0 ─────────────────────
# (Same as Q_β = |Δnet| · E_0 but using absolute net, not difference)
m_pi_A = MESON_NET * E_0
err_pi_A = float(fabs(m_pi_A - PDG_PI_PM) / PDG_PI_PM * 1e6)

# ── Strategy B: m(meson) = m_e · Geom(meson_braid, q_0) ────────
# VolDensity for baryons = |tr_M(T_w)| × linking_weight
# For mesons, try: Geom = net(M+) × Vol(transition_knot) / ℏ_q
# where transition_knot connects the quark flavors
m_pi_B = m_e * MESON_NET * VOL_4_1 / HBAR_Q
err_pi_B = float(fabs(m_pi_B - PDG_PI_PM) / PDG_PI_PM * 1e6)

# ── Strategy C: Use the SAME closed-form pattern as Q_β ─────────
# Q_β uses the algebraic expression |q² - 2q - 1|·(q+1)/(2q³)
# For meson, the natural analog uses the meson-braid eigenvalues.
# In H_3(q), the meson NF involves h = q - q⁻¹.
# Try: m_π = m_e · F_meson(q_0) where F_meson is an algebraic function
# F_meson = net(M+) · (q+1)²/(2q) = the meson net times a normalisation
F_meson_pi = MESON_NET * (q0 + 1)**2 / (2 * q0)
m_pi_C = m_e * F_meson_pi
err_pi_C = float(fabs(m_pi_C - PDG_PI_PM) / PDG_PI_PM * 1e6)

# ── Strategy D: Meson mass from H_3 Markov trace ────────────────
# tr_M(M+) in H_3 with Markov parameter z = 1/([3]_q)
# [3]_q = q² + 1 + q⁻²
three_q = q0**2 + 1 + 1/q0**2
z3 = 1 / three_q
# tr_M(M+) = z3 · (coefficient sum weighted by Markov weights)
# For the universal meson braid, NF is known. The Markov trace:
# tr_M(x) = z^{exponent_sum} · NF-weighted trace
# Simplified: tr_M(net) ≈ net · z3  (leading order)
tr_M_meson = float(MESON_NET) * float(z3)
m_pi_D = m_e * fabs(mpf(str(tr_M_meson))) * (q0 + 1/q0)**2 / 4
err_pi_D = float(fabs(m_pi_D - PDG_PI_PM) / PDG_PI_PM * 1e6)

# ── Strategy E: Exact leptonic-tower transposition ───────────────
# For leptons: m_μ/m_e = Vol(4_1)/ℏ_q². The figure-eight 4_1
# connects T_{2,3} (e) → T_{2,5} (μ).
# For mesons: π uses d = T_{2,3}^σ, K uses s = T_{2,5}^σ.
# SAME torus-knot pair, just mirrored!
# So by exact parallel: m_K/m_π = Vol(4_1)/ℏ_q² = m_μ/m_e ??
# This would give m_K/m_π = 206.77 — obviously wrong (actual 3.54).
# But the STRUCTURE is right: same transition knot.
# The difference: mesons are COMPOSITE (q-qbar), not fundamental.
# The mass formula for composites involves the binding topology.
# Try: m_K/m_π = Vol(4_1)/ℏ_q^{2·(strand_ratio)}
# where strand_ratio = n_meson/n_lepton = 3/2

m_K_over_m_pi_E1 = VOL_4_1 / HBAR_Q**(2 * mpf(3)/mpf(2))
err_E1 = float(fabs(m_K_over_m_pi_E1 - PDG_K_PM/PDG_PI_PM) / (PDG_K_PM/PDG_PI_PM) * 1e6)

# ── Strategy F: h_q scaling with crossing difference ─────────────
# The d→s transition adds 2 crossings (3→5).
# Each crossing contributes h_q to the NF.
# Try: m_K/m_π = (1 + h_q)^2 (two extra crossings, each contributing h_q)
m_K_over_m_pi_F = (1 + h_q)**2
err_F = float(fabs(m_K_over_m_pi_F - PDG_K_PM/PDG_PI_PM) / (PDG_K_PM/PDG_PI_PM) * 1e6)

# ── Strategy G: q^Δn where Δn = 5-3 = 2 (crossing difference) ───
# For leptons: the mass ratio involves q^{large power} via Vol/ℏ_q²
# For mesons: try q_0^(Δn) where Δn is the crossing count difference
m_K_over_m_pi_G = q0**(5-3)  # = q_0²
err_G = float(fabs(m_K_over_m_pi_G - PDG_K_PM/PDG_PI_PM) / (PDG_K_PM/PDG_PI_PM) * 1e6)

# ── Strategy H: [Δn]_q (quantum integer of crossing difference) ──
# [2]_q = q + q⁻¹ ≈ 2.011
delta_n = 5 - 3  # crossing count difference between s and d
two_q = q0 + 1/q0
m_K_over_m_pi_H = two_q**delta_n  # [2]_q² ≈ 4.04 — closest yet?
err_H = float(fabs(m_K_over_m_pi_H - PDG_K_PM/PDG_PI_PM) / (PDG_K_PM/PDG_PI_PM) * 1e6)

# Quantum integer [2]_q itself
qi_2 = (q0**2 - 1/q0**2) / h_q  # [2]_q = (q²-q⁻²)/(q-q⁻¹) = q+q⁻¹
m_K_over_m_pi_H2 = qi_2
err_H2 = float(fabs(qi_2 - PDG_K_PM/PDG_PI_PM) / (PDG_K_PM/PDG_PI_PM) * 1e6)

# ── Strategy I: Net ratio with E_0 correction ────────────────────
# m_π = net(π_braid) · E_0, m_K = net(K_braid) · E_0
# where K_braid has h_s = h·(5/3) enhanced coupling
h_s = h * 5 / 3
h_s2, h_s3 = h_s*h_s, h_s*h_s*h_s
KAON_NET = h_s + (h_s2 + 1) + h_s2 + (h_s3 + h_s)  # same NF structure, enhanced h
m_K_over_m_pi_I = KAON_NET / MESON_NET
err_I = float(fabs(m_K_over_m_pi_I - PDG_K_PM/PDG_PI_PM) / (PDG_K_PM/PDG_PI_PM) * 1e6)

# ── Strategy J: Vol(4_1)^{1/3} / ℏ_q^{2/3} ─────────────────────
# Dimensional analysis: mesons are qq-bar (2 body), baryons qqq (3 body)
# Try fractional power of the lepton relation
m_K_over_m_pi_J = (VOL_4_1 / HBAR_Q_SQ) ** (mpf(1)/mpf(3))
err_J = float(fabs(m_K_over_m_pi_J - PDG_K_PM/PDG_PI_PM) / (PDG_K_PM/PDG_PI_PM) * 1e6)

# ══════════════════════════════════════════════════════════════════
#  RESULTS
# ══════════════════════════════════════════════════════════════════

actual_ratio = float(PDG_K_PM / PDG_PI_PM)

print("=" * 76)
print("MESON MASS PREDICTIONS FROM HECKE H_3(q)")
print("=" * 76)
print()
print("╔══════════════════════════════════════════════════════════════════════╗")
print("║  GENERIC STRUCTURE: two calibration instances in QOU               ║")
print("║                                                                    ║")
print("║  Instance 1 (leptonic, CAL-2):                                     ║")
print(f"║    ℏ_q² = Vol(4_1) / (m_μ/m_e)                                     ║")
print(f"║    m_μ/m_e = {float(ratio_mu_e_predicted):.4f}  (exact by construction)            ║")
print("║                                                                    ║")
print("║  Instance 2 (hadronic, derived):                                   ║")
print(f"║    Q_β = m_e·|q²-2q-1|·(q+1)/(2q³) = {float(Q_beta_pred):.6f} MeV              ║")
print(f"║    vs CODATA {float(Q_BETA_CODATA):.8f} MeV  (err = {err_Qbeta_ppm:.0f} ppm)               ║")
print("║                                                                    ║")
print("║  Instance 3 (mesonic, THIS PROBE):                                 ║")
print("║    m_K/m_π = ???                                                    ║")
print("╚══════════════════════════════════════════════════════════════════════╝")
print()

print(f"Substrate: q_0 = {float(q0):.10f}, h_q = {float(h_q):.10f}")
print(f"Meson NF net(M+) = {float(MESON_NET):.6f}")
print(f"E_0 = {float(E_0):.6f} MeV")
print(f"PDG: m_π± = {float(PDG_PI_PM):.5f}, m_K± = {float(PDG_K_PM):.3f}, ratio = {actual_ratio:.6f}")
print()

# Absolute pion mass candidates
print("── Absolute m_π predictions ──")
print(f"  A: net·E_0                   = {float(m_pi_A):>10.3f} MeV  (err {err_pi_A:>10.0f} ppm)")
print(f"  B: m_e·net·Vol/ℏ_q           = {float(m_pi_B):>10.3f} MeV  (err {err_pi_B:>10.0f} ppm)")
print(f"  C: m_e·net·(q+1)²/(2q)       = {float(m_pi_C):>10.3f} MeV  (err {err_pi_C:>10.0f} ppm)")
print(f"  D: m_e·|tr_M|·[2]_q²/4       = {float(m_pi_D):>10.3f} MeV  (err {err_pi_D:>10.0f} ppm)")
print()

# Ratio m_K/m_π candidates
print(f"── m_K/m_π ratio predictions (target = {actual_ratio:.6f}) ──")
print(f"  E1: Vol(4_1)/ℏ_q³            = {float(m_K_over_m_pi_E1):>10.6f}  (err {err_E1:>10.0f} ppm)")
print(f"  F: (1+h_q)²                  = {float(m_K_over_m_pi_F):>10.6f}  (err {err_F:>10.0f} ppm)")
print(f"  G: q_0²                      = {float(m_K_over_m_pi_G):>10.6f}  (err {err_G:>10.0f} ppm)")
print(f"  H: [2]_q² = (q+q⁻¹)²        = {float(m_K_over_m_pi_H):>10.6f}  (err {err_H:>10.0f} ppm)")
print(f"  H2: [2]_q = q+q⁻¹            = {float(m_K_over_m_pi_H2):>10.6f}  (err {err_H2:>10.0f} ppm)")
print(f"  I: net(K)/net(π) [h→5h/3]    = {float(m_K_over_m_pi_I):>10.6f}  (err {err_I:>10.0f} ppm)")
print(f"  J: (m_μ/m_e)^{1/3}            = {float(m_K_over_m_pi_J):>10.6f}  (err {err_J:>10.0f} ppm)")
print()

# Find best
results = [
    ("E1: Vol/ℏ_q³",           float(m_K_over_m_pi_E1), err_E1),
    ("F: (1+h)²",              float(m_K_over_m_pi_F),  err_F),
    ("G: q₀²",                 float(m_K_over_m_pi_G),  err_G),
    ("H: [2]_q²",              float(m_K_over_m_pi_H),  err_H),
    ("H2: [2]_q",              float(m_K_over_m_pi_H2), err_H2),
    ("I: net_K/net_π",         float(m_K_over_m_pi_I),  err_I),
    ("J: (m_μ/m_e)^{1/3}",    float(m_K_over_m_pi_J),  err_J),
]
results.sort(key=lambda x: x[2])

print("── Ranked by closeness ──")
for name, val, err in results:
    marker = " ← BEST" if err == results[0][2] else ""
    print(f"  {name:30s}  {val:>10.6f}  err = {err:>10.0f} ppm{marker}")

# ══════════════════════════════════════════════════════════════════
#  WITNESS
# ══════════════════════════════════════════════════════════════════

witness = {
    "engine": "python3/mpmath",
    "engineVersion": "50dps",
    "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "computation": "meson-mass-from-hecke",
    "scriptFile": "meson_mass_from_hecke.py",
    "description": (
        "Systematic probe of pion and kaon mass predictions following the "
        "same generic structure as the leptonic (CAL-2: m_μ/m_e = Vol(4_1)/ℏ_q²) "
        "and hadronic (Q_β = m_e·|q²-2q-1|·(q+1)/(2q³)) derivation instances. "
        "Tests 10+ candidate formulas for absolute m_π and ratio m_K/m_π."
    ),
    "contentBlock": "prop:meson-mass-hecke-prediction",
    "parameters": {
        "q0": str(q0),
        "h_q": str(h_q),
        "Vol_4_1": str(VOL_4_1),
        "m_e_MeV": str(m_e),
        "meson_net": str(MESON_NET),
        "E_0_MeV": str(E_0),
    },
    "generic_structure": {
        "description": (
            "Two calibration instances in QOU share a generic pattern: "
            "a mass observable is determined by an algebraic function of q_0 "
            "built from Hecke-algebra eigenvalues and hyperbolic-knot invariants."
        ),
        "instance_1_leptonic": {
            "formula": "m_μ/m_e = Vol(4_1) / ℏ_q²",
            "transition_knot": "4_1 (figure-eight)",
            "transition_braid": "(σ_1 σ_2^{-1})^2 in B_3",
            "connects": "T_{2,3} (electron) → T_{2,5} (muon)",
            "predicted": str(ratio_mu_e_predicted),
            "observed": str(MASS_RATIO_MU_E),
            "err_ppb": err_mu_e_ppb,
        },
        "instance_2_hadronic": {
            "formula": "Q_β = m_e · |q² - 2q - 1| · (q+1) / (2q³)",
            "transition": "proton → neutron flavor flip",
            "connects": "uud → udd (Borromean typed-crossing shift)",
            "predicted_MeV": str(Q_beta_pred),
            "observed_MeV": "0.78233341",
            "err_ppm": err_Qbeta_ppm,
        },
        "instance_3_mesonic": {
            "formula": "m_K/m_π = ??? (probing)",
            "transition": "pion (ud-bar) → kaon (us-bar)",
            "connects": "d = T_{2,3}^σ → s = T_{2,5}^σ (same pair as e→μ, mirrored)",
            "best_candidate": results[0][0],
            "best_value": results[0][1],
            "best_err_ppm": results[0][2],
            "all_candidates": [
                {"name": n, "value": v, "err_ppm": e} for n, v, e in results
            ],
        },
    },
    "pion_absolute_mass": {
        "strategy_A": {"formula": "net·E_0", "predicted_MeV": str(m_pi_A), "err_ppm": err_pi_A},
        "strategy_B": {"formula": "m_e·net·Vol/ℏ_q", "predicted_MeV": str(m_pi_B), "err_ppm": err_pi_B},
        "strategy_C": {"formula": "m_e·net·(q+1)²/(2q)", "predicted_MeV": str(m_pi_C), "err_ppm": err_pi_C},
        "strategy_D": {"formula": "m_e·|tr_M|·[2]_q²/4", "predicted_MeV": str(m_pi_D), "err_ppm": err_pi_D},
    },
    "assertions": [
        {"label": "Instance 1 (CAL-2) exact by construction", "passed": err_mu_e_ppb < 1},
        {"label": "Instance 2 (Q_β) within 2000 ppm", "passed": err_Qbeta_ppm < 2000},
        {"label": "At least one meson ratio within 50%", "passed": results[0][2] < 500000},
    ],
}
witness["allPassed"] = all(a["passed"] for a in witness["assertions"])

import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
_sys.path.insert(0, str(HERE / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402

# DECLARE the anchor rather than let the resolver infer one. witness.py states
# the stamped label "always matches the value the producer actually computed"
# BECAUSE it resolves from the same source the runtime uses to pick q0 -- but
# that holds only for a producer that CALLS q_at(). This one never does: it
# DERIVES q0 from Vol(4_1) and the registry m_mu/m_e, which is the whole
# content of Instance 1. So the manifest describes a q0 that was never used,
# and the inferred label was `proton` while every number here is muon-route.
#
# The label is `ambiguous` TRANSITIONALLY, and the reason is not the one I
# first wrote. I recorded "undetermined pending the A-vs-C ruling"; THE RULING
# EXISTS and predates that commit by three days -- owner, 2026-08-22 on PR
# #5500: "2022 CODATA better than 2018. A --> CODATA 2022." Recorded in
# .beans/qou-bred, docs/audits/2026-08-23-q0-literal-transcription-
# classification.md and q0_literal_classification_audit.py:240. Declaring an
# item open that the corpus has closed is the failure the corpus-grep
# checklist exists to prevent, and I made it.
#
# So the value this producer derives -- C, 1.109978595642739... -- IS the
# ruled muon anchor. What is not yet true is that MAIN carries it: the
# anchor-defining witness still holds A (1.109978595557334...) while its own
# calibration_inputs declare 206.7682827, the contradiction #5500 exists to
# close, and #5500 is unmerged and red on 53 witnesses awaiting regeneration.
#
# Stamping `muon` today would therefore read as a Q0_FLIP against main's stale
# anchor table. `ambiguous` + this reason is the honest transitional record.
# WHEN #5500 LANDS, THIS SHOULD BECOME `muon` -- at that point the derived
# value and the anchor agree and no declaration is needed.
witness["q0Anchor"] = "ambiguous"
witness["q0AnchorReason"] = (
    "Derives q0 = 1/(1 - sqrt(Vol(4_1)/(m_mu/m_e))) from the registry ratio "
    "rather than reading an anchor, so no manifest entry describes it. The "
    f"result, {str(q0)[:22]}, is value C of qou-khac -- which the owner RULED "
    "canonical for the muon anchor on 2026-08-22 (PR #5500, 'A --> CODATA "
    "2022'). This is ambiguous only transitionally: main's anchor witness "
    "still holds A, so a 'muon' stamp would read as a Q0_FLIP until #5500 "
    "lands. Revisit then; the correct label at that point is 'muon'."
)
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
witness["scriptFile"] = Path(__file__).name
out_path = HERE / "meson-mass-from-hecke.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2, default=str)

print(f"\nWitness: {out_path.name}")
