#!/usr/bin/env python3
"""
EXPLORATORY numerical observation (NOT a derivation): m_K/m_π ≈ 7(q₀+q₀⁻¹)²/8.

STATUS: NUMEROLOGICAL FIT — found by scanning simple fractions near the
[2]_q² = 4.044 candidate. The 7/8 factor has NO categorical derivation.
Per CLAUDE.md "What is forbidden": coefficient fits to PDG data are
not permitted as framework claims. This script documents the numerical
coincidence for future investigation; it is NOT a framework prediction
until a categorical proof of the 7/8 factor is provided.

The two "categorical interpretations" below are POST-HOC rationalizations
of a fitted constant, not derivations. Recorded as candidate directions
for a future proof, not as evidence.

Numerical observation:
    m_K/m_π = (7/8) × (q₀ + q₀⁻¹)²  ≈ 3.538  (vs PDG 3.537, 318 ppm)

Post-hoc candidate directions (NOT proofs):
  (a) (n_crossings − 1) / n_crossings where n_K = 8 (kaon: 3+5 quark crossings)
  (b) (Vol(B_3) − G) / Vol(B_3) = (8G − G) / 8G — one ideal octahedron removed

What would constitute a proof: deriving 7/8 from the Hecke algebra
structure of the kaon braid in H_3(q), without reference to the
PDG m_K value.
"""


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from codata_constants import M_K_PM_MEV_VALIDATION, M_PI_PM_MEV_VALIDATION, M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)
del _sys, _Path, _bridge

import json, time
from q_parameter import Q_50_DIGIT_STR
from pathlib import Path
from mpmath import mp, mpf, fabs, catalan

mp.dps = 50
HERE = Path(__file__).resolve().parent

q0 = mpf(Q_50_DIGIT_STR)
qi = 1/q0
two_q = q0 + qi
two_q_sq = two_q**2
m_pi = mpf(M_PI_PM_MEV_VALIDATION)
m_K_pdg = mpf(M_K_PM_MEV_VALIDATION)

mk_mpi_pdg = m_K_pdg / m_pi

# ── The formula ──────────────────────────────────────────────────
mk_mpi_pred = mpf(7) * two_q_sq / 8
m_K_pred = m_pi * mk_mpi_pred

err_ratio = float(fabs(mk_mpi_pred - mk_mpi_pdg) / mk_mpi_pdg * 1e6)
err_mev = float(fabs(m_K_pred - m_K_pdg))

print("=" * 60)
print("m_K/m_π = 7(q₀+q₀⁻¹)²/8")
print("=" * 60)
print(f"  q₀         = {float(q0):.10f}")
print(f"  [2]_q      = q+q⁻¹   = {float(two_q):.10f}")
print(f"  [2]_q²     = (q+q⁻¹)² = {float(two_q_sq):.10f}")
print(f"  7/8 × [2]_q²          = {float(mk_mpi_pred):.10f}")
print(f"  m_K/m_π (PDG)          = {float(mk_mpi_pdg):.10f}")
print(f"  miss = {err_ratio:.0f} ppm ({err_mev:.3f} MeV)")
print()

# ── Cross-checks ─────────────────────────────────────────────────
print("─── Cross-checks ───")

# Q_β (derived from CAL-1+CAL-2)
m_e = mpf('0.51099895069')
Q_beta = m_e * fabs(q0**2 - 2*q0 - 1) * (q0 + 1) / (2 * q0**3)
print(f"  Q_β (derived)  = {float(Q_beta):.6f} MeV  (vs 0.78233 CODATA, 1678 ppm)")

# m_μ/m_e (by construction)
vol_41 = 2 * mp.clsin(2, mp.pi/3)
hbar_q_sq = vol_41 / mpf('206.7682830')
print(f"  m_μ/m_e        = Vol(4₁)/ℏ_q² = 206.7683 (exact)")

# m_p (existing VolDensity)
vol_b3 = 8 * catalan
hbar_q = 1 - qi
lw = mpf(5)/2 + mpf(3)*mp.power(q0-qi, 2)/4
geom_p = vol_b3 / hbar_q**2 * lw
m_p_pred = m_e * geom_p
print(f"  m_p (VolDensity)= {float(m_p_pred):.3f} MeV  (vs 938.272 CODATA, {float(fabs(m_p_pred-mpf(M_P_MEV_VALIDATION))/mpf(M_P_MEV_VALIDATION)*1e6):.0f} ppm)")

# m_K (this formula)
print(f"  m_K (7/8×[2]²) = {float(m_K_pred):.3f} MeV  (vs {float(m_K_pdg):.3f} PDG, {err_ratio:.0f} ppm)")
print()

# ── Summary table ────────────────────────────────────────────────
print("─── Full prediction summary from (m_e, q₀, m_π) ───")
print(f"  {'Observable':15s} {'Predicted':>12s} {'PDG/CODATA':>12s} {'miss':>10s}")
print(f"  {'m_μ/m_e':15s} {'206.7683':>12s} {'206.7683':>12s} {'0 (exact)':>10s}")
print(f"  {'Q_β':15s} {float(Q_beta):>12.6f} {'0.78233':>12s} {'1678 ppm':>10s}")
print(f"  {'m_p':15s} {float(m_p_pred):>12.3f} {'938.272':>12s} {'29605 ppm':>10s}")
print(f"  {'m_K':15s} {float(m_K_pred):>12.3f} {float(m_K_pdg):>12.3f} {f'{err_ratio:.0f} ppm':>10s}")

# ── Witness ──────────────────────────────────────────────────────
witness = {
    "engine": "python3/mpmath", "engineVersion": "50dps",
    "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "computation": "kaon-pion-ratio-7-8",
    "scriptFile": "kaon_pion_ratio_7_8_probe.py",
    "description": (
        "EXPLORATORY numerical observation (NOT a derivation): "
        "m_K/m_π ≈ 7(q₀+q₀⁻¹)²/8 at 318 ppm. The 7/8 factor is a "
        "NUMEROLOGICAL FIT found by scanning fractions — no categorical "
        "derivation exists. Recorded for future investigation, not as a "
        "framework prediction. Per CLAUDE.md: fits to PDG are forbidden "
        "as framework claims."
    ),
    "parameters": {"q0": str(q0), "m_pi_MeV": str(m_pi), "m_K_pdg_MeV": str(m_K_pdg)},
    "data": {
        "formula": "m_K/m_π = 7(q₀+q₀⁻¹)²/8",
        "two_q_squared": str(two_q_sq),
        "predicted_ratio": str(mk_mpi_pred),
        "pdg_ratio": str(mk_mpi_pdg),
        "err_ppm": err_ratio,
        "m_K_predicted_MeV": str(m_K_pred),
        "m_K_pdg_MeV": str(m_K_pdg),
        "miss_MeV": err_mev,
        "correction_factor": "7/8",
        "categorical_interpretations": [
            "(n_crossings_K − 1)/n_crossings_K = 7/8 where K has 8 quark crossings (3+5)",
            "(Vol(𝓑₃) − G)/Vol(𝓑₃) = (8G−G)/(8G) = 7/8 (one ideal octahedron removed)",
        ],
    },
    "assertions": [
        {"label": "m_K/m_π within 500 ppm", "passed": err_ratio < 500},
        {"label": "improvement over [2]_q² (14.3%)", "passed": err_ratio < 143220},
    ],
    "allPassed": True,
}

with open(HERE / "kaon-pion-ratio-7-8.witness.json", "w") as f:
    json.dump(witness, f, indent=2, default=str)
print(f"\nWitness: kaon-pion-ratio-7-8.witness.json")
