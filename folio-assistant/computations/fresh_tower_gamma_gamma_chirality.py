#!/usr/bin/env python3
"""
Fresh derivation: tower for opposite-chirality same-flavor pairs
starting from γγ pair production.

Setup (per paper's pair-creation-energy.md + breit-wheeler):

  γγ → e⁻ + e⁺  at threshold E_pair = 2m_e
  Colored photon: γ = 𝟙 + φ·σ_0 + φ·σ_1
  Pair NF: γ·γ = e⁻ + e⁺ (trefoil + anti-trefoil) at fixed chirality

In the Hecke algebra:
  e⁻ = σ_0·σ_1·σ_0  (trefoil, chiral+)
  e⁺ = (σ_0·σ_1·σ_0)⁻¹  (anti-trefoil, chiral-)
         = σ_0⁻¹·σ_1⁻¹·σ_0⁻¹

These satisfy: closed-e⁻e⁺ = identity × 2m_e observable projection.

KEY MECHANISM: γγ pair creation REVERSES the per-strand chirality
between e⁻ (each strand σ) and e⁺ (each strand σ⁻¹).  The net mass
is 2·m_e — NOT m_e + 0; each carries the same SIZE mass.

APPLICATION TO uu vs dd:
  proton uu-pair:  σ-type (chiral+)         → V̂_0^uu = V̂ with c=1, d=0
  neutron dd-pair: σ⁻¹-type (chiral-)       → V̂_0^dd = V̂ with c=1, d=-H_A

Current direct tower: V̂_0^n = 0.854 (far from q_0 pole = 1.110)
                      V̂_0^p = 0.989 (close to pole)
Gap: factor ~1.16

The FRESH DERIVATION claim: by γγ-analogy, the dd-pair should yield
the SAME |V̂| as uu-pair, just with chirality flipped.  In Wedderburn
terms:
  V̂_0^dd(q) = V̂_0^uu(q⁻¹)   (chirality flip = q ↔ q⁻¹)

At real q₀, the magnitude |V̂_0^dd(q₀)| = |V̂_0^uu(q₀⁻¹)|.

Let's verify: compute V̂_0 for proton's chain vs neutron's chain
and for neutron but with q replaced by q⁻¹ in the proton computation.
Should give: |V̂_0^uu(q⁻¹)| matches neutron's V̂ by this hypothesis.

Then fix: use UNIVERSAL v̂_0 = (|V̂_0^uu(q)| + |V̂_0^uu(q⁻¹)|)/2 as
symmetrized tower input, and TRACK CHIRALITY via separate sign factor.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 50

from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
                          atom_per_generator_volumes, h as H_A_FLOAT,
                          vertex_volume)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
me = mp.mpf(str(M_E_MEV))
h = Q0 - QI
H_A = h

# Compute V̂_0 for proton chain at q_0 and at q_0⁻¹ (chirality flip)
def vertex_vol_at(chain, q_val):
    """Compute vertex_volume with q set to q_val (possibly q_0⁻¹)."""
    # vertex_volume transfer-matrix recurrence:
    #   a, b start = 0, 1
    #   each (c, d) factor: a, b = a·h + b, a  where h = q − q⁻¹
    # Not using c, d directly — use the chain's actual (c, d)
    h_val = q_val - mp.mpf(1) / q_val
    z_val = mp.mpf(1) / (mp.sqrt(q_val) + mp.sqrt(mp.mpf(1)/q_val))
    a = mp.mpf(0); b = mp.mpf(1)
    for (c, d) in chain:
        # Transfer-matrix update for Hecke element c·σ + d·I
        c_mp = mp.mpf(c); d_mp = mp.mpf(d)
        # Standard Hoefsmit 2×2 transfer: a' = a·(c·h + d) + b·c, b' = a·c + b·d
        a_new = a * (c_mp * h_val + d_mp) + b * c_mp
        b_new = a * c_mp + b * d_mp
        a, b = a_new, b_new
    return z_val * a + b


# Proton V̂_0 at q_0
V0_p_q = vertex_vol_at(_PROTON_G0, Q0)
V0_p_qinv = vertex_vol_at(_PROTON_G0, QI)

# Neutron V̂_0 at q_0 (actual) and at q_0⁻¹
V0_n_q = vertex_vol_at(_NEUTRON_G0, Q0)
V0_n_qinv = vertex_vol_at(_NEUTRON_G0, QI)

print("=" * 100)
print("FRESH DERIVATION: γγ pair-production tower for uu vs dd")
print("=" * 100)
print(f"  q_0 = {float(Q0):.8f}, q_0⁻¹ = {float(QI):.8f}")
print(f"  h = q − q⁻¹ = {float(h):.6f}")
print()
print(f"  V̂_0 computed from Hecke chain at q and at q⁻¹:")
print(f"  proton chain V̂_0(q)    = {float(V0_p_q):+.8f}")
print(f"  proton chain V̂_0(q⁻¹)  = {float(V0_p_qinv):+.8f}")
print(f"  neutron chain V̂_0(q)   = {float(V0_n_q):+.8f}")
print(f"  neutron chain V̂_0(q⁻¹) = {float(V0_n_qinv):+.8f}")
print()

# γγ-analogy claim: |V̂_0^dd(q)| ≈ |V̂_0^uu(q⁻¹)|?
print(f"  γγ-analog test: |V̂_0^n(q)| vs |V̂_0^p(q⁻¹)|")
print(f"    |V̂_0^n(q)|   = {float(abs(V0_n_q)):.8f}")
print(f"    |V̂_0^p(q⁻¹)| = {float(abs(V0_p_qinv)):.8f}")
print(f"    ratio n(q) / p(q⁻¹) = {float(abs(V0_n_q) / abs(V0_p_qinv)):.6f}")
print()

# Symmetric average (chirality-symmetrized) V̂_0:
V_sym = (mp.fabs(V0_p_q) + mp.fabs(V0_n_q)) / 2
V_geom = mp.sqrt(mp.fabs(V0_p_q) * mp.fabs(V0_n_q))
print(f"  Chirality-symmetrized V̂_0:")
print(f"    arithmetic mean (|V_p| + |V_n|)/2 = {float(V_sym):.6f}")
print(f"    geometric mean √(|V_p|·|V_n|)     = {float(V_geom):.6f}")
print(f"  Individual V̂_0^p = {float(V0_p_q):.6f}, V̂_0^n = {float(V0_n_q):.6f}")

# Test: does the symmetrized V̂ give matching mass for both p and n?
print()
print(f"  TEST: apply symmetrized V̂_0 in tower for both p and n")
V1_p = vertex_vol_at(_PROTON_G1, Q0)
V1_n = vertex_vol_at(_NEUTRON_G1, Q0)
print(f"    V̂_1^p = {float(V1_p):.6f},  V̂_1^n = {float(V1_n):.6f}")

# Compute tower mass for each using arithmetic vs geometric vs individual V̂_0
def Phi_q(v, max_iter=3000):
    if not isinstance(v, mp.mpf): v = mp.mpf(str(float(v)))
    prod = mp.mpf(1); coef = mp.mpf(1)/Q0
    for _ in range(1, max_iter+1):
        t = mp.mpf(1) - coef*v
        if abs(t) < mp.mpf('1e-40'): return mp.mpc('inf')
        prod /= t
        if abs(coef*v) < mp.mpf('1e-60'): break
        coef /= Q0
    return prod

def tower_level0(V_list):
    abs_V = [mp.fabs(v) for v in V_list]
    prod = mp.mpf(1)
    for v in abs_V: prod *= v
    phi = sum(Phi_q(v) if v < 1 else mp.mpf('inf') for v in abs_V)
    z = mp.mpf(1) / (mp.sqrt(Q0) + mp.sqrt(QI))
    z_sq = z*z
    pair_sum = mp.mpf(0)
    for i in range(len(abs_V)-1):
        pij = abs_V[i]*abs_V[i+1]
        if pij < 1: pair_sum += Phi_q(pij)
    return prod + phi + z_sq * pair_sum

m_p_H = tower_level0([V0_p_q, V1_p])
m_n_H = tower_level0([V0_n_q, V1_n])
m_n_sym = tower_level0([V_sym, V1_n])
m_n_geom = tower_level0([V_geom, V1_n])
m_e_H = tower_level0([vertex_vol_at([(1.0,0.0)]*3, Q0)])   # trefoil e⁻
print(f"    m_p_tower  (V̂_0=0.989, V̂_1=0.971) = {float(m_p_H):.4f}")
print(f"    m_n_tower  (V̂_0=0.854, V̂_1=0.976) = {float(m_n_H):.4f}")
print(f"    m_n_sym    (V̂_0=sym, V̂_1=0.976)    = {float(m_n_sym):.4f}")
print(f"    m_n_geom   (V̂_0=geom, V̂_1=0.976)   = {float(m_n_geom):.4f}")

calib = float(me) / float(m_e_H)
print()
print(f"  Calibration E_0 = m_e / m_e_H = {calib:.6e} MeV/cat-unit")
print(f"  m_p_tower_MeV  = {float(m_p_H)*calib:.4f} MeV (CODATA {M_P_MEV}, err {(float(m_p_H)*calib-M_P_MEV)/M_P_MEV*100:+.2f}%)")
print(f"  m_n_tower_MeV  = {float(m_n_H)*calib:.4f} MeV (CODATA {M_N_MEV}, err {(float(m_n_H)*calib-M_N_MEV)/M_N_MEV*100:+.2f}%)")
print(f"  m_n_sym_MeV    = {float(m_n_sym)*calib:.4f} MeV (err {(float(m_n_sym)*calib-M_N_MEV)/M_N_MEV*100:+.2f}%)")
print(f"  m_n_geom_MeV   = {float(m_n_geom)*calib:.4f} MeV (err {(float(m_n_geom)*calib-M_N_MEV)/M_N_MEV*100:+.2f}%)")

# Save witness
witness = {
    "computation": "fresh-tower-gamma-gamma-chirality",
    "description": (
        "Fresh derivation of opposite-chirality pair tower starting "
        "from γγ → e⁻e⁺ mechanism.  Tests whether V̂_0^n and V̂_0^p "
        "can be unified via chirality symmetrization (arithmetic or "
        "geometric mean of |V̂_0^p| and |V̂_0^n|)."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q_0": Q0_FLOAT,
    "V0_p": float(V0_p_q),
    "V0_p_inv": float(V0_p_qinv),
    "V0_n": float(V0_n_q),
    "V0_n_inv": float(V0_n_qinv),
    "V_sym_arithmetic": float(V_sym),
    "V_sym_geometric": float(V_geom),
    "m_p_MeV": float(m_p_H) * calib,
    "m_n_MeV": float(m_n_H) * calib,
    "m_n_sym_MeV": float(m_n_sym) * calib,
    "m_n_geom_MeV": float(m_n_geom) * calib,
}
out = Path(__file__).parent / "fresh-tower-gamma-gamma-chirality.witness.json"
out.write_text(json.dumps(witness, indent=2, default=str))
print(f"\n  Witness: {out}")
