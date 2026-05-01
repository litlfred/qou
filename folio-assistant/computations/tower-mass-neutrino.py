#!/usr/bin/env python3
"""
Task 3: Tower/mass ratio investigation
Task 4: Neutrino mass from L₋ channel — DEPRECATED (see resolution below)

The corrected Markov trace gives:
  tr_M(proton) ≈ -0.012
  tr_M(neutron) ≈ -0.134
  ratio |tr_M(n)|/|tr_M(p)| ≈ 11.6

CODATA: m_n/m_p = 1.00138

The tower mechanism must amplify these traces through iterated
self-interaction (Φ_q composition tower).

╔══════════════════════════════════════════════════════════════════════╗
║  TASK 4 (NEUTRINO MASS) IS DEPRECATED                                ║
║                                                                      ║
║  Resolution: The neutrino IS the unknot per the paper's              ║
║  knot-particle dictionary (knot-particle-dictionary.md,              ║
║  knot-particle-generation.md, recursive-atom-knot-atlas.md).         ║
║  The categorical mass of the unknot is 𝔪(𝟏) = 0 by definition       ║
║  (Markov trace of the identity vanishes for the mass-endomorphism    ║
║  formula). The neutrino has no mass.                                 ║
║                                                                      ║
║  This script's V̂_ν = z² assignment is wrong: the unknot has         ║
║  trivial braiding (zero crossings), not a vertex volume of z².      ║
║  The "off by 10⁶" discrepancy in old runs was a confusion between    ║
║  the GS-reduction coefficient on 𝟏 (a sector index) and the        ║
║  categorical mass of the resulting particle. Different quantities.  ║
║                                                                      ║
║  Task 3 (proton/neutron mass-ratio investigation) remains valid.    ║
║  Do not consume `m_nu_*` fields from the witness JSON.              ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import json
import math
from pathlib import Path
from datetime import datetime, timezone

DIR = Path(__file__).parent

from q_parameter import Q as q0, Q_INV as qi0, HA as HA0, Q_ERR, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

z = 1.0 / (math.sqrt(q0) + 1.0 / math.sqrt(q0))

# ── Load nucleon NF from beta-decay-energy-scale witness ─────────
esc_w = json.loads((DIR / "beta-decay-energy-scale.witness.json").read_text())
esc_nf = esc_w.get("nucleon_nf", {})

# NF basis traces (corrected: e⁻ = z³, not hz²+z)
TR_M = [1.0, z, z, z**2, z**2, z**3]
NF_NAMES = ["ν", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]

# Map witness keys to NF indices
KEY_MAP = {"ν": 0, "H\u2070": 1, "H\u00b9": 2, "L\u208a": 3, "L\u208b": 4, "e\u207b": 5}

def nf_to_vec(nf_dict):
    """Convert witness NF dict to 6-element vector."""
    return [nf_dict.get(k, 0.0) for k in KEY_MAP]

p_vec = nf_to_vec(esc_nf.get("proton", {}))
n_vec = nf_to_vec(esc_nf.get("neutron", {}))

tr_p = sum(c * t for c, t in zip(p_vec, TR_M))
tr_n = sum(c * t for c, t in zip(n_vec, TR_M))

print("=" * 70)
print("  TASK 3: TOWER/MASS RATIO INVESTIGATION")
print("=" * 70)

print(f"\n─── Corrected Markov traces (z³ for e⁻) ───")
print(f"  tr_M(e⁻) = z³ = {z**3:.10f}")
print(f"  z = {z:.10f}")

print(f"\n  Proton NF:  {[f'{c:+.6f}' for c in p_vec]}")
print(f"  Neutron NF: {[f'{c:+.6f}' for c in n_vec]}")
print(f"  TR_M basis: {[f'{t:.6f}' for t in TR_M]}")

print(f"\n  tr_M(proton)  = {tr_p:+.10f}")
print(f"  tr_M(neutron) = {tr_n:+.10f}")
print(f"  |tr_M(n)|/|tr_M(p)| = {abs(tr_n)/abs(tr_p):.4f}")
print(f"  CODATA m_n/m_p      = {M_N_MEV/M_P_MEV:.6f}")

# ── Decompose the trace by basis element ────────────────────────
print(f"\n─── Trace decomposition by basis element ───")
print(f"  {'Basis':<6} {'c_p':>10} {'c_n':>10} {'tr_M(b)':>10} {'c_p×tr':>12} {'c_n×tr':>12}")
print("  " + "-" * 62)
for i in range(6):
    print(f"  {NF_NAMES[i]:<6} {p_vec[i]:>+10.6f} {n_vec[i]:>+10.6f} {TR_M[i]:>10.6f} {p_vec[i]*TR_M[i]:>+12.8f} {n_vec[i]*TR_M[i]:>+12.8f}")
print(f"  {'TOTAL':<6} {'':>10} {'':>10} {'':>10} {tr_p:>+12.8f} {tr_n:>+12.8f}")

# ── Tower mechanism ──────────────────────────────────────────────
print(f"\n─── Tower mechanism analysis ───")

# The mass formula uses the tower Φ_q^(k)(V̂) where V̂ is the vertex volume
# Mass = lim_{k→∞} |Φ_q^(k)(V̂)| × μ₀
# where Φ_q(x) = (q^x - q^{-x})/(q - q^{-1}) = [x]_q evaluated at x=V̂
# and μ₀ is the Planck mass scale

# For the proton, the dominant NF term is σ₁ with coefficient ≈ +0.998
# Its vertex volume is V̂ = z × c + d where c,d come from the NF coefficient
# In the simplest case: V̂_proton ≈ z × 0.998 ≈ 0.498 (close to z)

V_hat_p = abs(tr_p)  # Single-level: mass ∝ |tr_M|
V_hat_n = abs(tr_n)

print(f"  Single-level (no tower):")
print(f"    |tr_M(p)| = {V_hat_p:.10f}")
print(f"    |tr_M(n)| = {V_hat_n:.10f}")
print(f"    ratio = {V_hat_n/V_hat_p:.4f} (need 1.0014)")

# Tower iteration: Φ_q(x) = [x]_q = (q^x - q^{-x})/(q - q^{-1})
def phi_q(x, qq=q0):
    """q-integer function: Φ_q(x) = (q^x - q^{-x})/(q - q^{-1})"""
    return (qq**x - qq**(-x)) / (qq - 1.0/qq)

# Iterate tower
print(f"\n  Tower iteration Φ_q^(k)(V̂):")
print(f"  {'k':>3} {'Φ^k(|tr_p|)':>16} {'Φ^k(|tr_n|)':>16} {'ratio':>10}")
print("  " + "-" * 48)

v_p = V_hat_p
v_n = V_hat_n
for k in range(15):
    ratio = v_n / v_p if v_p != 0 else float('inf')
    print(f"  {k:>3} {v_p:>16.10f} {v_n:>16.10f} {ratio:>10.6f}")
    if abs(v_p) > 1e10 or abs(v_n) > 1e10:
        print("  ... (diverging)")
        break
    v_p_new = phi_q(v_p)
    v_n_new = phi_q(v_n)
    v_p = v_p_new
    v_n = v_n_new

# ── Alternative: use net instead of tr_M ─────────────────────────
print(f"\n─── Alternative: tower on net (not tr_M) ───")
net_p = sum(p_vec)
net_n = sum(n_vec)
print(f"  net(p) = {net_p:.10f}")
print(f"  net(n) = {net_n:.10f}")

v_p = net_p
v_n = net_n
print(f"\n  {'k':>3} {'Φ^k(net_p)':>16} {'Φ^k(net_n)':>16} {'ratio':>10}")
print("  " + "-" * 48)
for k in range(15):
    ratio = v_n / v_p if v_p != 0 else float('inf')
    print(f"  {k:>3} {v_p:>16.10f} {v_n:>16.10f} {ratio:>10.6f}")
    if abs(v_p) > 1e10 or abs(v_n) > 1e10:
        print("  ... (diverging)")
        break
    v_p = phi_q(v_p)
    v_n = phi_q(v_n)

# ═══════════════════════════════════════════════════════════════
# TASK 4: NEUTRINO MASS
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  TASK 4: NEUTRINO MASS FROM L₋ CHANNEL")
print("=" * 70)

# The neutrino is the unknot (trivial knot), so J_ν(q) = 1
# Its vertex volume is V̂_ν = z² (from the L₋ channel, handover)
# The tower gives m_ν/m_e = Φ_q^(∞)(z²) / Φ_q^(∞)(V̂_e)

V_hat_nu = z**2  # neutrino vertex volume
V_hat_e = z**3   # electron vertex volume (corrected)

print(f"\n  Neutrino: unknot K₀₁, trivial Jones polynomial J_ν(q) = 1")
print(f"  V̂_ν = z² = {V_hat_nu:.10f}")
print(f"  V̂_e = z³ = {V_hat_e:.10f}")

# Tower iteration
print(f"\n  Tower iteration:")
print(f"  {'k':>3} {'Φ^k(V̂_ν)':>16} {'Φ^k(V̂_e)':>16} {'m_ν/m_e':>12}")
print("  " + "-" * 50)

v_nu = V_hat_nu
v_e = V_hat_e
mass_ratio_history = []
for k in range(20):
    ratio = v_nu / v_e if v_e != 0 else float('inf')
    mass_ratio_history.append(ratio)
    print(f"  {k:>3} {v_nu:>16.10f} {v_e:>16.10f} {ratio:>12.8f}")
    if abs(v_nu) > 1e10 or abs(v_e) > 1e10:
        print("  ... (diverging)")
        break
    v_nu = phi_q(v_nu)
    v_e = phi_q(v_e)

# The ratio should converge to m_ν/m_e
if len(mass_ratio_history) > 5:
    converged_ratio = mass_ratio_history[-1]
    m_nu_eV = converged_ratio * M_E_MEV * 1e6  # convert MeV to eV
    print(f"\n  Converged ratio m_ν/m_e ≈ {converged_ratio:.8f}")
    print(f"  Predicted m_ν ≈ {m_nu_eV:.4f} eV")
    print(f"  Observed upper bound: m_ν < 0.8 eV (KATRIN 2022)")
    print(f"  Cosmological bound: Σm_ν < 0.12 eV (Planck 2018)")

# ── Alternative: mass from vacuum drag ───────────────────────────
print(f"\n─── Alternative: vacuum drag formula ───")
# m_ν ∝ μ₀ × (q - 1) where μ₀ is the vacuum drag coefficient
# If μ₀ = m_e / (something), then m_ν = m_e × (q-1) / (something)
print(f"  ℏ_q = 1 - q⁻¹ = {HBAR_Q:.10f}")
print(f"  q - 1 = {q0 - 1:.10f}")
print(f"  If m_ν = m_e × ℏ_q² = {M_E_MEV * HBAR_Q**2 * 1e6:.4f} eV")
print(f"  If m_ν = m_e × ℏ_q³ = {M_E_MEV * HBAR_Q**3 * 1e6:.4f} eV")
print(f"  If m_ν = m_e × (q-1)³ = {M_E_MEV * (q0-1)**3 * 1e6:.4f} eV")

# ── Write witness ────────────────────────────────────────────────
witness = {
    "computation": "tower-mass-neutrino",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q0": q0,
    "corrected_traces": {
        "tr_M_proton": tr_p,
        "tr_M_neutron": tr_n,
        "ratio_abs": abs(tr_n) / abs(tr_p),
        "codata_mn_mp": M_N_MEV / M_P_MEV,
    },
    "neutrino": {
        "V_hat_nu": V_hat_nu,
        "V_hat_e": V_hat_e,
        "mass_ratio_history": mass_ratio_history[:10],
        "m_nu_hbar_q2_eV": M_E_MEV * HBAR_Q**2 * 1e6,
        "m_nu_hbar_q3_eV": M_E_MEV * HBAR_Q**3 * 1e6,
    },
}
out = DIR / "tower-mass-neutrino.witness.json"
out.write_text(json.dumps(witness, indent=2))
print(f"\n  Witness written to {out.name}")
print("=" * 70)
