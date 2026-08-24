#!/usr/bin/env python3
"""
Meson PerKnotDensity: the meson-sector analog of per_knot_density_borromean.

For baryons:  m_p = 2·(m_μ·F_Bor − 6·m_e) — the canonical muon-anchored
              Hecke energy (canonical_mass facade; the former
              Vol(𝓑₃)/ℏ_q²·λ_A path is the excised 966-MeV fit)

For mesons:   m(meson) = m_π × Geom_meson(braid, q₀)
              Geom_meson = NF-weighted Frobenius evaluation in H_3(q)

The key structural difference: baryons are anchored through the muon
(hyperbolic 4₁ volume in the anchor, dressed by the dimensionless
F_Bor). Mesons are built from torus knots (Vol=0), so the mass formula
uses the H_3 Frobenius pairing directly, with m_π (CAL-3) as the
dimensional anchor instead of m_e alone.

GENERIC PATTERN (two instances):
  Baryon sector: m_p = 2·(m_μ·F_Bor − 6·m_e)  (canonical_mass facade)
  Meson sector:  m = m_π × (NF_ratio)

This script derives:
  - Absolute m_π (as CAL-3 input, not predicted)
  - m_K from m_π × Geom_meson(K_braid / π_braid)
  - m_p/m_π ratio from the canonical baryon reference / Geom_meson
  - Q_β from CAL-1 + CAL-2 (cross-check)
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json, time
from q_parameter import Q_50_DIGIT_STR
from pathlib import Path
from mpmath import mp, mpf, fabs

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
HERE = Path(__file__).resolve().parent

# ── substrate (from constants.py) ────────────────────────────────
q0 = mpf(Q_50_DIGIT_STR)
qi = 1/q0
h_q = q0 - qi
hbar_q = 1 - qi  # ℏ_q = (q-1)/q
# Masses routed through the codata_constants registry — no inline CODATA
# literals (AGENTS.md P31 / three-CAL purity). _path_bridge (above) puts
# substrate/ on sys.path so `codata_constants` resolves.
from codata_constants import (  # noqa: E402
    M_E_MEV, M_PI_PM_MEV_VALIDATION, M_K_PM_MEV_VALIDATION,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
)
m_e = M_E_MEV

# ── CAL-3: pion mass ─────────────────────────────────────────────
M_PI = M_PI_PM_MEV_VALIDATION  # PDG charged-pion mass

# ── PDG targets (validation, not inputs) ─────────────────────────
M_K  = M_K_PM_MEV_VALIDATION
M_P  = M_P_MEV_VALIDATION
M_N  = M_N_MEV_VALIDATION

# ══════════════════════════════════════════════════════════════════
#  BARYON REFERENCE — canonical muon-anchored Hecke energy
# ══════════════════════════════════════════════════════════════════
# λ_A excision (owner ruling 2026-06-24): the former inline baryon
# reference linking_weight_A = 5/2 + 3h²/4 on Vol(𝓑₃)/ℏ_q² is the
# fitted 966-MeV path. The canonical absolute nucleon mass is the
# muon-anchored Hecke energy m_p = 2·(m_μ·F_Bor − 6·m_e), routed
# through the canonical_mass facade.
from canonical_mass import proton_mass_mev  # noqa: E402

m_p_pred = mpf(str(proton_mass_mev()))
geom_baryon = m_p_pred / m_e  # dimensionless factor m_p/m_e (was Vol/ℏ_q²·λ_A)
err_mp = float(fabs(m_p_pred - M_P) / M_P * 1e6)

# ══════════════════════════════════════════════════════════════════
#  MESON GEOM — NF-based mass ratios in H_3(q)
# ══════════════════════════════════════════════════════════════════
# Universal meson braid M+ in H_3: NF coefficients
# NF(M+) = h·σ₁ + (h²+1)·L+ + h²·L- + (h³+h)·e⁻
h, h2, h3 = h_q, h_q**2, h_q**3

meson_nf = {
    'sigma_1': h,
    'L+': h2 + 1,
    'L-': h2,
    'e-': h3 + h,
}
meson_net = sum(meson_nf.values())

# ── Kaon: same braid, but s-quark crossings (5) replace d (3) ───
# The flavor typing changes the effective h for the quark strand.
# The pion has 3+3=6 quark crossings, kaon has 3+5=8.
# The crossing-energy model: each extra crossing contributes h_q.
# The Hecke-reduction NF for the kaon uses h_eff = h × (n_K/n_π)
# where n_K=8 (total crossings), n_π=6.
h_K = h * 8/6  # enhanced by crossing ratio
h_K2, h_K3 = h_K**2, h_K**3
kaon_nf = {
    'sigma_1': h_K,
    'L+': h_K2 + 1,
    'L-': h_K2,
    'e-': h_K3 + h_K,
}
kaon_net = sum(kaon_nf.values())

# ── Geom_meson: mass ratio from NF ──────────────────────────────
# m_K = m_π × Geom_meson(K/π)
# where Geom_meson = kaon_net / pion_net (NF ratio)
geom_meson_K = kaon_net / meson_net
m_K_pred_nf = M_PI * geom_meson_K
err_mK_nf = float(fabs(m_K_pred_nf - M_K) / M_K * 1e6)

# ── Alternative: [2]_q correction ────────────────────────────────
# Best candidate from prior probe: [2]_q² = (q+q⁻¹)² ≈ 4.044
# vs m_K/m_π = 3.537.  The 14.3% gap might close with a
# dimensional correction from the meson's H_3 structure.
two_q = q0 + qi
geom_meson_K_twoq = two_q**2
m_K_pred_twoq = M_PI * geom_meson_K_twoq
err_mK_twoq = float(fabs(m_K_pred_twoq - M_K) / M_K * 1e6)

# ── Goldstone correction: subtract sym-block contribution ────────
# The Δ_λ probe found Δ_sym < 0 for mesons (Goldstone reduction).
# The sym block eigenvalue is q^n; the correction is:
# Geom_meson = [2]_q² - (sym_correction)
# Try: [2]_q² × (1 - y_sym/y_total) where y_sym is the sym-block
# Markov weight fraction
y_sym = mpf('0.41539578633456654389')
y_total = mpf('0.71907036601012591')  # sum of all 3 y_λ
sym_frac = y_sym / y_total

geom_meson_K_goldstone = two_q**2 * (1 - sym_frac / two_q)
m_K_pred_goldstone = M_PI * geom_meson_K_goldstone
err_mK_goldstone = float(fabs(m_K_pred_goldstone - M_K) / M_K * 1e6)

# ── Frobenius pairing ratio ──────────────────────────────────────
# From proton data: Σ(y·χ_p) = 1.06531, Σ(y·χ_meson) = 1.12684
# m_p/m_π = Geom_baryon × m_e / m_π
mp_over_mpi = float(M_P / M_PI)
geom_ratio = float(geom_baryon * m_e / M_PI)

# ══════════════════════════════════════════════════════════════════
#  Q_β CROSS-CHECK (derived from CAL-1 + CAL-2)
# ══════════════════════════════════════════════════════════════════
Q_beta_pred = m_e * fabs(q0**2 - 2*q0 - 1) * (q0 + 1) / (2 * q0**3)
Q_BETA_CODATA = mpf('0.78233341')
err_Qbeta = float(fabs(Q_beta_pred - Q_BETA_CODATA) / Q_BETA_CODATA * 1e6)

# ══════════════════════════════════════════════════════════════════
#  OUTPUT
# ══════════════════════════════════════════════════════════════════

print("=" * 70)
print("MESON PerKnotDensity: mass predictions from (m_e, q₀, m_π)")
print("=" * 70)
print()
print("─── BARYON (reference — canonical muon-anchored facade) ───")
print(f"  m_p = 2·(m_μ·F_Bor − 6·m_e)   [canonical_mass.proton_mass_mev()]")
print(f"  m_p = m_e × {float(geom_baryon):.4f} = {float(m_p_pred):.3f} MeV  (err {err_mp:.3g} ppm)")
print()
print("─── MESON (this work) ───")
print(f"  m_π = {float(M_PI):.5f} MeV  (CAL-3 input)")
print(f"  meson_net(π) = {float(meson_net):.6f}")
print(f"  kaon_net(K)  = {float(kaon_net):.6f}  (h_eff = h × 8/6)")
print()
print(f"  Candidate m_K predictions (m_K = m_π × Geom_meson):")
print(f"    A. NF ratio (net_K/net_π):          {float(m_K_pred_nf):>8.2f} MeV  (err {err_mK_nf:>8.0f} ppm)")
print(f"    B. [2]_q² = (q+q⁻¹)²:              {float(m_K_pred_twoq):>8.2f} MeV  (err {err_mK_twoq:>8.0f} ppm)")
print(f"    C. [2]_q² × Goldstone correction:   {float(m_K_pred_goldstone):>8.2f} MeV  (err {err_mK_goldstone:>8.0f} ppm)")
print(f"    PDG target:                         {float(M_K):>8.3f} MeV")
print()
print("─── Q_β CROSS-CHECK (derived from CAL-1+CAL-2) ───")
print(f"  Q_β = m_e·|q²-2q-1|·(q+1)/(2q³) = {float(Q_beta_pred):.6f} MeV")
print(f"  CODATA = {float(Q_BETA_CODATA):.8f} MeV  (err {err_Qbeta:.0f} ppm)")
print()
print("─── PROTON-PION RATIO ───")
print(f"  m_p/m_π (PDG)  = {mp_over_mpi:.6f}")
print(f"  Geom_baryon × m_e / m_π = {geom_ratio:.6f}  (err {abs(mp_over_mpi-geom_ratio)/mp_over_mpi*100:.2f}%)")
print()

# ── Witness ──────────────────────────────────────────────────────
witness = {
    "engine": "python3/mpmath", "engineVersion": "50dps",
    "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "computation": "meson-per-knot-density",
    "scriptFile": "meson_per_knot_density.py",
    "description": (
        "Meson-sector mass ratios (per-knot twin). Baryon reference routes through "
        "the canonical muon-anchored facade (canonical_mass.proton_mass_mev; λ_A "
        "excised 2026-06-24); mesons use m=m_π×Geom_meson where m_π is CAL-3. Tests "
        "three m_K candidates. Also cross-checks Q_β as derived from CAL-1+CAL-2."
    ),
    "parameters": {"q0": str(q0), "m_e": str(m_e), "m_pi": str(M_PI)},
    "data": {
        "baryon_geom": {"route": "canonical_mass.proton_mass_mev", "m_p_over_m_e": float(geom_baryon), "m_p_pred": float(m_p_pred), "err_ppm": err_mp},
        "meson_geom_candidates": {
            "A_nf_ratio": {"geom": float(geom_meson_K), "m_K_pred": float(m_K_pred_nf), "err_ppm": err_mK_nf},
            "B_two_q_sq": {"geom": float(geom_meson_K_twoq), "m_K_pred": float(m_K_pred_twoq), "err_ppm": err_mK_twoq},
            "C_goldstone": {"geom": float(geom_meson_K_goldstone), "m_K_pred": float(m_K_pred_goldstone), "err_ppm": err_mK_goldstone},
        },
        "q_beta_crosscheck": {"pred": float(Q_beta_pred), "codata": float(Q_BETA_CODATA), "err_ppm": err_Qbeta},
        "proton_pion_ratio": {"pdg": mp_over_mpi, "geom": geom_ratio},
    },
    "assertions": [
        {"label": "m_p (canonical facade) within 1 ppm", "passed": err_mp < 1},
        {"label": "Q_β within 2000 ppm", "passed": err_Qbeta < 2000},
    ],
    "allPassed": True,
}
witness["allPassed"] = all(a["passed"] for a in witness["assertions"])

import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
_sys.path.insert(0, str(HERE / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
witness["scriptFile"] = Path(__file__).name
with open(HERE / "meson-per-knot-density.witness.json", "w") as f:
    json.dump(witness, f, indent=2, default=str)
print(f"Witness: meson-per-knot-density.witness.json")
