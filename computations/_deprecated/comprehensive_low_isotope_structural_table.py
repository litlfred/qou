#!/usr/bin/env python3
"""
40a + 40b: Comprehensive low-isotope mass / binding / Q-value table
using STRUCTURAL α_k (no per-isotope fitting).

Builds on the cross-fork mass-table from earlier sessions.

Framework:
  m(β) = Σ_k α_k · Φ_k(β)

where (per prop:explicit-alpha-k-h3 + prop:gravity-spectral-prefactor):
  α_0 = 1                              (canonical, volume / trivial block)
  α_1 = 0                              (vanishing direct pairing)
  α_2 = z²                             (Markov pair, Λ_2 stratum)
  α_3 = h·z² + z                       (Hecke + cyclicity at H_3)
  α_(k≥4) = m_e · 8G                   (universal Term 7, gravity prefactor)

with z = 1/(√q + 1/√q), h = q − q⁻¹, all q-algebraic.

Φ_k(β) = Σ_{depth(λ)=k} w_λ · log|χ_λ(β)|  (Plancherel-weighted log functional)

For each isotope:
  1. Use Φ_k from depth-resolved-phi-k-hoefsmit.witness.json (D, T, ³He, ⁴He)
  2. Apply structural α_k (NO fits)
  3. Compute m(β) = Z·m_p + N·m_n + Z·m_e − B(β)
     where B(β) = -Σ_k α_k · Φ_k(β)  (binding contribution from Hecke structure)
  4. Compare to AME mass + binding

Output table: per-isotope mass, binding, Q-values with % and ppb errors.
"""
from __future__ import annotations
import json, sys, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 25

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
m_p = mp.mpf("938.27208816")
m_n = mp.mpf("939.56542052")
G_catalan = mp.catalan
m_e_8G = m_e * 8 * G_catalan  # universal Term 7 prefactor (gravity-spectral)

h_amp = Q0 - QI
z_mark = 1/(mp.sqrt(Q0) + 1/mp.sqrt(Q0))


# Structural α_k from prop:explicit-alpha-k-h3 + prop:gravity-spectral-prefactor
def alpha_k_structural(k):
    """All structural — NO fitting."""
    if k == 0: return mp.mpf(1)              # volume / trivial block
    if k == 1: return mp.mpf(0)              # vanishing direct pairing
    if k == 2: return z_mark ** 2            # z²
    if k == 3: return h_amp * z_mark**2 + z_mark  # h·z² + z
    return m_e_8G                            # universal Term 7 (k ≥ 4)


# Load existing depth-resolved Φ_k per isotope
phi_k_data = json.load(open(Path(__file__).parent / "depth-resolved-phi-k-hoefsmit.witness.json"))
phi_k_per_iso = phi_k_data["isotope_Phi_k"]


# AME 2020 reference (atomic masses + bindings + Q-values)
AME = {
    # iso, Z, N, M_atom_AME (MeV), B_AME (MeV), Q_value_MeV (decay)
    "p":   ( 1, 0,   938.78308711,    0.0,           None),
    "n":   ( 0, 1,   939.56542052,    0.0,           0.78233341),  # n→p β-decay
    "D":   ( 1, 1,  1876.12393,       2.22456612,    None),
    "T":   ( 1, 2,  2809.43215,       8.481798,      0.018592),    # ³H→³He β-decay
    "3He": ( 2, 1,  2809.41347,       7.718058,      None),
    "4He": ( 2, 2,  3728.40133,      28.29566,       None),
    # ⁶Li, ⁷Li would need atom-knot identification first
}


def predict_mass_binding(iso, Z, N):
    """Apply structural α_k to Φ_k for this isotope's Hecke structure."""
    if iso not in phi_k_per_iso:
        return None
    Phi_k = phi_k_per_iso[iso]["Phi_k"]
    # Compute Σ_k α_k · Φ_k
    structural_sum = mp.mpf(0)
    for k_str, phi_val in Phi_k.items():
        k = int(k_str)
        ak = alpha_k_structural(k)
        structural_sum += ak * mp.mpf(str(phi_val))
    # Convert to MeV — already in MeV-class (Φ_k uses log|χ|, multiplied by α_k in MeV/dimensionless)
    return float(structural_sum)


print("=" * 110)
print("40a + 40b: Comprehensive low-isotope structural prediction (NO fitting)")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f}")
print(f"  m_e = {float(m_e):.6f} MeV,  m_p = {float(m_p):.6f},  m_n = {float(m_n):.6f}")
print()
print(f"  Structural α_k (per prop:explicit-alpha-k-h3 + gravity-spectral-prefactor):")
print(f"    α_0 = 1")
print(f"    α_1 = 0")
print(f"    α_2 = z² = {float(z_mark**2):.6f}")
print(f"    α_3 = h·z² + z = {float(h_amp*z_mark**2 + z_mark):.6f}")
print(f"    α_(k≥4) = m_e·8G = {float(m_e_8G):.6f} MeV (universal Term 7)")
print()

# ── MASS TABLE ─────────────────────────────────────────────────────
print("=" * 110)
print("MASS TABLE: m(atom) prediction vs AME (% and ppb errors)")
print("=" * 110)
print(f"  {'iso':<5} {'A':>3} {'Z':>3} {'N':>3} {'M_AME':>13} {'M_pred':>13} {'err MeV':>11} {'err %':>10} {'err ppb':>13}")
print("-" * 110)
mass_results = []
for iso, (Z, N, M_AME, B_AME, Q_AME) in AME.items():
    A = Z + N
    sigma_M = float(structural_sum := predict_mass_binding(iso, Z, N) or 0)

    # The structural sum gives the Hecke-derived contribution.  Combine with
    # constituent baseline:
    #   M(atom) = Z·m_p + N·m_n + Z·m_e − B_pred
    #   B_pred = -structural_sum  (Hecke structure contributes BINDING)
    # OR:
    #   M_pred = constituent baseline + structural_sum  (sign convention)

    constituent = Z * m_p + N * m_n + Z * m_e
    # Use sign convention: structural sum is the BINDING contribution (negative for bound)
    B_pred = -structural_sum if structural_sum != 0 else 0
    M_pred = constituent - B_pred

    err_M_abs = M_pred - M_AME
    err_M_pct = err_M_abs / M_AME * 100 if M_AME != 0 else 0
    err_M_ppb = err_M_abs / M_AME * 1e9 if M_AME != 0 else 0
    print(f"  {iso:<5} {A:>3} {Z:>3} {N:>3} {M_AME:>13.6f} {M_pred:>13.6f} {err_M_abs:>+11.6f} {err_M_pct:>+10.4f} {err_M_ppb:>+13.0f}")
    mass_results.append({
        "iso": iso, "A": A, "Z": Z, "N": N,
        "M_AME": M_AME, "M_pred": M_pred,
        "err_MeV": err_M_abs, "err_pct": err_M_pct, "err_ppb": err_M_ppb,
        "B_AME": B_AME, "B_pred": B_pred,
        "structural_sum": structural_sum
    })


# ── BINDING TABLE ──────────────────────────────────────────────────
print()
print("=" * 110)
print("BINDING TABLE: B(atom) prediction vs AME (% and ppb errors)")
print("=" * 110)
print(f"  {'iso':<5} {'A':>3} {'B_AME':>10} {'B_pred':>10} {'err MeV':>11} {'err %':>11} {'err ppb':>13}")
print("-" * 110)
for r in mass_results:
    if r["B_AME"] == 0:
        print(f"  {r['iso']:<5} {r['A']:>3} {r['B_AME']:>10.4f} {r['B_pred']:>10.4f} {'(no binding)':>11}")
        continue
    err_B = r["B_pred"] - r["B_AME"]
    err_B_pct = err_B / r["B_AME"] * 100
    err_B_ppb = err_B / r["B_AME"] * 1e9
    print(f"  {r['iso']:<5} {r['A']:>3} {r['B_AME']:>10.4f} {r['B_pred']:>10.4f} {err_B:>+11.4f} {err_B_pct:>+11.4f} {err_B_ppb:>+13.0f}")
    r["B_err"] = err_B; r["B_err_pct"] = err_B_pct


# ── Q-VALUE TABLE ──────────────────────────────────────────────────
print()
print("=" * 110)
print("Q-VALUE TABLE: β-decay / transition Q-value vs CODATA")
print("=" * 110)
print(f"  {'transition':<14} {'Q_AME':>12} {'Q_pred':>12} {'err MeV':>11} {'err %':>10} {'err ppb':>13}")
print("-" * 110)
# Q_β(n→p) = m_n - m_p - m_e (in absolute terms)
# Q(³H→³He+e+ν̄) similar
Q_predictions = {
    "n → p":      ("n",   "p"),      # m_n - m_p - m_e
    "³H → ³He":   ("T",   "3He"),    # m_T - m_3He - m_e (atomic)
}
for label, (parent, daughter) in Q_predictions.items():
    par_data = next((r for r in mass_results if r["iso"] == parent), None)
    dau_data = next((r for r in mass_results if r["iso"] == daughter), None)
    if not par_data or not dau_data:
        continue
    Q_AME = par_data["M_AME"] - dau_data["M_AME"] - float(m_e)
    Q_pred = par_data["M_pred"] - dau_data["M_pred"] - float(m_e)
    err_Q = Q_pred - Q_AME
    err_Q_pct = err_Q / Q_AME * 100 if Q_AME != 0 else 0
    err_Q_ppb = err_Q / Q_AME * 1e9 if Q_AME != 0 else 0
    print(f"  {label:<14} {Q_AME:>12.6f} {Q_pred:>12.6f} {err_Q:>+11.6f} {err_Q_pct:>+10.4f} {err_Q_ppb:>+13.0f}")


# ── Comparison to existing mass_table_ppb (cross-fork) ─────────────
print()
print("=" * 110)
print("Comparison to existing mass_table_ppb framework (no Hecke structure):")
print("=" * 110)
mt_ppb = json.load(open(Path(__file__).parent / "mass-table-ppb.witness.json"))
mt_rows = mt_ppb.get("isotopes", [])
mt_lookup = {r.get("atom"): r for r in mt_rows}
sup = {"D": "2H", "T": "3H", "3He": "3He", "4He": "4He"}
print(f"  {'iso':<5} {'B_AME':>10} {'B_mass_table':>14} {'B_struct (this)':>16}")
for r in mass_results:
    if r["iso"] in ("p", "n"): continue
    mt_label = sup.get(r["iso"], r["iso"])
    mt_row = mt_lookup.get(mt_label)
    mt_B = mt_row.get("B_pred_MeV") if mt_row else None
    mt_err = mt_row.get("err_pct") if mt_row else None
    print(f"  {r['iso']:<5} {r['B_AME']:>10.4f} {mt_B if mt_B else '—':>14} (err {mt_err if mt_err else '?'}%) "
          f"{r.get('B_pred', 0):>16.4f} (err {r.get('B_err_pct', 0):+.2f}%)")

# Save comprehensive witness
out = {
    "computation": "comprehensive-low-isotope-structural-table",
    "description": ("40a+40b: Comprehensive low-isotope mass + binding + Q-value table "
                    "using STRUCTURAL α_k from prop:explicit-alpha-k-h3 (this branch) "
                    "and prop:gravity-spectral-prefactor (universal Term 7).  "
                    "NO per-isotope fitting.  Φ_k from depth-resolved Hoefsmit "
                    "characters per partition."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "alpha_k_structural": {
        "alpha_0": 1.0, "alpha_1": 0.0,
        "alpha_2": float(z_mark**2),
        "alpha_3": float(h_amp*z_mark**2 + z_mark),
        "alpha_k_ge_4": float(m_e_8G)
    },
    "mass_results": mass_results,
}
out_path = Path(__file__).parent / "comprehensive-low-isotope-structural-table.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2, default=str)
print(f"\nWitness: {out_path}")
