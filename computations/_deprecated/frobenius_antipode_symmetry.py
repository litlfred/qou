#!/usr/bin/env python3
"""
Frobenius antipode + Yekutieli rigid dualizing symmetry probe.

The Frobenius antipode S on H_n(q) sends σ ↦ σ⁻¹.  Under this:
  S(uu-pair (c=1,d=0))  = σ⁻¹ = (c=1, d=-h)    (→ becomes dd-style)
  S(dd-pair (c=1,d=-h)) = σ   = (c=1, d=0)     (→ becomes uu-style)
  S(ud-pair) = ud-pair (self-dual under S, since d = -h/2 symmetric).

If the Markov trace |tr_M| is S-INVARIANT (up to sign), then V̂_0^n
and V̂_0^p should have equal magnitudes when computed with proper
Frobenius-dualized formula.

Under Yekutieli's rigid dualizing complex, the self-dual Frobenius
structure of H_n(q) gives tr_M(x) = tr_M(S(x)) · sign, where sign
depends on parity of inverses.

This script tests:
  1. Apply S to neutron chain element-wise
  2. Compute resulting V̂_0 and compare to proton V̂_0
  3. If equal: the Frobenius antipode symmetry gives us the 'missing'
     structural equivalence

For the proton chain 6σ + 1ud:
  S(proton gen 0) = 6σ⁻¹ + 1ud = chain with (1, -h) × 6 + (1, -h/2) × 1
For the neutron chain 5σ + 2ud:
  S(neutron gen 0) = 5σ⁻¹ + 2ud = chain with (1, -h) × 5 + (1, -h/2) × 2
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
                          h as H_A_F, vertex_volume)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
h = Q0 - QI


def apply_frobenius_antipode(chain: list) -> list:
    """S: σ ↦ σ⁻¹.  In (c, d) representation:
        (1, 0) [σ]  ↦ (1, -h) [σ⁻¹]
        (1, -h) [σ⁻¹] ↦ (1, 0) [σ]
        (1, -h/2) [ud mixed] ↦ (1, -h/2) (self-dual, (σ+σ⁻¹)/2 is S-invariant)
    """
    h_f = float(H_A_F)
    out = []
    for c, d in chain:
        c_f, d_f = float(c), float(d)
        if abs(c_f - 1) < 1e-10 and abs(d_f) < 1e-10:
            out.append((1.0, -h_f))      # σ → σ⁻¹
        elif abs(c_f - 1) < 1e-10 and abs(d_f + h_f) < 1e-10:
            out.append((1.0, 0.0))       # σ⁻¹ → σ
        elif abs(c_f - 1) < 1e-10 and abs(d_f + h_f/2) < 1e-10:
            out.append((1.0, -h_f/2))    # ud stays
        else:
            out.append((c, d))
    return out


def V_hat_std(chain, q_val):
    """V̂^std via 2×2 transfer matrix."""
    h_val = q_val - mp.mpf(1)/q_val
    z_val = mp.mpf(1) / (mp.sqrt(q_val) + mp.sqrt(mp.mpf(1)/q_val))
    a = mp.mpf(0); b = mp.mpf(1)
    for (c, d) in chain:
        c_m, d_m = mp.mpf(c), mp.mpf(d)
        a_new = a * (c_m * h_val + d_m) + b * c_m
        b_new = a * c_m + b * d_m
        a, b = a_new, b_new
    return z_val * a + b


print("=" * 100)
print("FROBENIUS ANTIPODE SYMMETRY PROBE")
print("=" * 100)
print(f"  q_0 = {float(Q0):.8f}, h = q − q⁻¹ = {float(h):.6f}")
print()

# Baseline V̂_0 values
V_p = V_hat_std(_PROTON_G0, Q0)
V_n = V_hat_std(_NEUTRON_G0, Q0)

# Apply S (Frobenius antipode) to each
Sp_chain = apply_frobenius_antipode(_PROTON_G0)
Sn_chain = apply_frobenius_antipode(_NEUTRON_G0)

V_Sp = V_hat_std(Sp_chain, Q0)
V_Sn = V_hat_std(Sn_chain, Q0)

print(f"  Original proton V̂_0^std  = {float(V_p):+.8f}")
print(f"  Original neutron V̂_0^std = {float(V_n):+.8f}")
print(f"  S(proton) V̂_0^std       = {float(V_Sp):+.8f}")
print(f"  S(neutron) V̂_0^std      = {float(V_Sn):+.8f}")
print()

# Check various symmetry combinations
print(f"  Symmetry tests:")
print(f"    S(p) = n?       {abs(float(V_Sp - V_n)) < 1e-6}  Δ={float(V_Sp - V_n):+.6f}")
print(f"    S(n) = p?       {abs(float(V_Sn - V_p)) < 1e-6}  Δ={float(V_Sn - V_p):+.6f}")
print(f"    |S(p)| = |n|?   {abs(float(mp.fabs(V_Sp) - mp.fabs(V_n))) < 1e-6}  Δ={float(mp.fabs(V_Sp) - mp.fabs(V_n)):+.6f}")
print()

# Frobenius-symmetrized V̂ (average of V and S(V))
V_p_sym = (V_p + V_Sp) / 2
V_n_sym = (V_n + V_Sn) / 2
print(f"  Frobenius-symmetrized V̂^std (average with antipode):")
print(f"    proton  (V + S(V))/2 = {float(V_p_sym):+.8f}")
print(f"    neutron (V + S(V))/2 = {float(V_n_sym):+.8f}")
print(f"    Δ(n,p) = {float(V_n_sym - V_p_sym):+.6f}")
print()

# Yekutieli dualized: |tr_M|·K_yekutieli·|tr_M(S)| (geometric mean)
V_p_geom = mp.sqrt(mp.fabs(V_p * V_Sp))
V_n_geom = mp.sqrt(mp.fabs(V_n * V_Sn))
print(f"  Yekutieli rigid-dual (geometric mean |V·S(V)|^½):")
print(f"    proton  = {float(V_p_geom):.8f}")
print(f"    neutron = {float(V_n_geom):.8f}")
print(f"    Δ(n,p) = {float(V_n_geom - V_p_geom):+.6f}")
print()

# Save witness
witness = {
    "computation": "frobenius-antipode-symmetry",
    "description": (
        "Frobenius antipode S: σ↦σ⁻¹ applied to proton/neutron gen-0 "
        "chains.  Tests whether V̂_0 ≡ V̂_0^S gives a symmetry that "
        "equalizes proton and neutron Wedderburn projections."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q_0": Q0_FLOAT,
    "V_p": float(V_p), "V_n": float(V_n),
    "V_Sp": float(V_Sp), "V_Sn": float(V_Sn),
    "V_p_sym_average": float(V_p_sym),
    "V_n_sym_average": float(V_n_sym),
    "V_p_geometric": float(V_p_geom),
    "V_n_geometric": float(V_n_geom),
}
out = Path(__file__).parent / "frobenius-antipode-symmetry.witness.json"
out.write_text(json.dumps(witness, indent=2, default=str))
print(f"  Witness: {out}")
