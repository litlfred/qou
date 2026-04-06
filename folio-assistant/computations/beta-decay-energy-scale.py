"""
Beta-decay energy scale: normalizing Hecke NF debts to physical MeV.

The Gröbner normal form of each nucleon in H₃(q) has six terms with
dimensionless coefficients.  The two negative terms (ν and e⁻) represent
"leptonic debt" — the vacuum input required to build the nucleon.

Beta decay n → p + e⁻ + ν̄ₑ releases the neutron's excess debt over
the proton's.  This script derives the energy scale E₀ (in MeV) that
converts the dimensionless debt difference Δ(net) to the observed
decay energy Q = m_n − m_p − m_e = 0.78233 MeV.

Usage:
    cd folio-assistant/computations
    python3 beta-decay-energy-scale.py
"""

import json
import math
import os
from datetime import datetime, timezone

from q_parameter import Q, Q_INV, HA, E_CROSS, S_SKEIN, HBAR_Q, LN_Q
from experimental_constants import (
    M_E_MEV, M_P_MEV, M_N_MEV,
    M_E_MEV_ERR, M_P_MEV_ERR, M_N_MEV_ERR,
    KAPPA, VOL_BORROMEAN,
)

# ── Load witness data ────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WITNESS_PATH = os.path.join(SCRIPT_DIR, "free-neutron-decay.witness.json")
with open(WITNESS_PATH) as f:
    witness = json.load(f)

# Extract NF coefficients from witness
neutron_nf = {t["particle"]: t["coefficient_numeric"] for t in witness["neutron"]["nf_terms"]}
proton_nf  = {t["particle"]: t["coefficient_numeric"] for t in witness["proton"]["nf_terms"]}

neutron_net = witness["neutron"]["net_coefficient"]
proton_net  = witness["proton"]["net_coefficient"]

# ── Debt differences ─────────────────────────────────────────────
delta_nu = neutron_nf["ν"] - proton_nf["ν"]       # < 0 (neutron owes more)
delta_e  = neutron_nf["e⁻"] - proton_nf["e⁻"]     # < 0 (neutron owes more)
delta_net = neutron_net - proton_net                # > 0

# Total leptonic debt excess
debt_total = abs(delta_nu) + abs(delta_e)

# ── Observed decay energy ────────────────────────────────────────
# Q = m_n − m_p − m_e (neutrino mass negligible)
Q_decay = M_N_MEV - M_P_MEV - M_E_MEV
Q_decay_err = math.sqrt(M_N_MEV_ERR**2 + M_P_MEV_ERR**2 + M_E_MEV_ERR**2)

# Mass difference (before subtracting electron mass)
delta_m = M_N_MEV - M_P_MEV
delta_m_err = math.sqrt(M_N_MEV_ERR**2 + M_P_MEV_ERR**2)

print("=" * 70)
print("BETA-DECAY ENERGY SCALE: Hecke NF → physical MeV")
print("=" * 70)

# ── Print debt differences ───────────────────────────────────────
print("\n── Leptonic debt differences (neutron − proton) ──")
print(f"  Δν  = {delta_nu:+.16f}  (neutron's excess ν debt)")
print(f"  Δe⁻ = {delta_e:+.16f}  (neutron's excess e⁻ debt)")
print(f"  |Δν| + |Δe⁻| = {debt_total:.16f}")
print(f"  Δ(net) = {delta_net:+.16f}")

# ── Observed values ──────────────────────────────────────────────
print(f"\n── Observed (CODATA 2022) ──")
print(f"  m_n − m_p      = {delta_m:.6f} ± {delta_m_err:.8f} MeV")
print(f"  Q = m_n−m_p−m_e = {Q_decay:.6f} ± {Q_decay_err:.8f} MeV")

# ── Derive energy scales ─────────────────────────────────────────
print(f"\n── Energy scale derivations ──")

# Method 1: E₀ from net coefficient difference
E0_from_net = Q_decay / delta_net
print(f"\n  Method 1: E₀ = Q / Δ(net)")
print(f"    E₀ = {Q_decay:.6f} / {delta_net:.10f}")
print(f"    E₀ = {E0_from_net:.6f} MeV")

# Method 2: E₀ from total leptonic debt
E0_from_debt = Q_decay / debt_total
print(f"\n  Method 2: E₀ = Q / (|Δν| + |Δe⁻|)")
print(f"    E₀ = {Q_decay:.6f} / {debt_total:.10f}")
print(f"    E₀ = {E0_from_debt:.6f} MeV")

# Method 3: E₀ from mass difference (not Q-value)
E0_from_mass = delta_m / delta_net
print(f"\n  Method 3: E₀ = (m_n − m_p) / Δ(net)")
print(f"    E₀ = {delta_m:.6f} / {delta_net:.10f}")
print(f"    E₀ = {E0_from_mass:.6f} MeV")

# ── Check against candidate expressions ──────────────────────────
print(f"\n── Candidate interpretations for E₀ ──")

# Check E₀ / m_e
ratio_me = E0_from_net / M_E_MEV
print(f"\n  E₀(net) / m_e = {ratio_me:.6f}")
print(f"  E₀(net) / κ   = {E0_from_net / KAPPA:.6f}  (κ = m_e/3)")

# Check against q-expressions
print(f"\n  q₀             = {Q:.10f}")
print(f"  q − q⁻¹        = {HA:.10f}")
print(f"  E_× = ½(q−q⁻¹) = {E_CROSS:.10f}")
print(f"  ℏ_q = 1 − q⁻¹  = {HBAR_Q:.10f}")

# E₀ in units of m_e × powers of q
for name, val in [
    ("E₀(net)", E0_from_net),
    ("E₀(debt)", E0_from_debt),
    ("E₀(mass)", E0_from_mass),
]:
    ratio = val / M_E_MEV
    print(f"\n  {name} = {val:.6f} MeV = {ratio:.6f} × m_e")
    print(f"    = {val / (M_E_MEV * HA):.6f} × m_e(q−q⁻¹)")
    print(f"    = {val / (M_E_MEV * E_CROSS):.6f} × m_e E_×")
    print(f"    = {val / (M_E_MEV * HBAR_Q):.6f} × m_eℏ_q")
    print(f"    = {val / KAPPA:.6f} × κ")

# ── The key relation: Δ(net) × E₀ = Q ───────────────────────────
print(f"\n── Verification ──")
Q_predicted_net = delta_net * E0_from_net
Q_predicted_debt = debt_total * E0_from_debt
print(f"  Δ(net)  × E₀(net)  = {Q_predicted_net:.6f} MeV  (obs: {Q_decay:.6f})")
print(f"  debt    × E₀(debt) = {Q_predicted_debt:.6f} MeV  (obs: {Q_decay:.6f})")

# ── Per-channel energy ───────────────────────────────────────────
print(f"\n── Per-channel energy decomposition (using E₀ from net) ──")
for particle, delta_val in [("ν", delta_nu), ("e⁻", delta_e)]:
    energy = abs(delta_val) * E0_from_net
    frac = abs(delta_val) / delta_net * 100
    print(f"  |Δ{particle}| × E₀ = {energy:.4f} MeV  ({frac:.1f}% of Q)")

# Also show: what fraction of Q goes to each channel
E_nu_channel = abs(delta_nu) * E0_from_net
E_e_channel = abs(delta_e) * E0_from_net
print(f"\n  ν̄ₑ channel:  {E_nu_channel:.4f} MeV")
print(f"  e⁻ channel:  {E_e_channel:.4f} MeV")
print(f"  Sum:         {E_nu_channel + E_e_channel:.4f} MeV")
print(f"  Remaining:   {Q_decay - E_nu_channel - E_e_channel:.4f} MeV")

# ── Positive-term differences ────────────────────────────────────
print(f"\n── Positive-term differences (virtual + observable) ──")
for particle in ["H⁰", "H¹", "L₊", "L₋"]:
    dn = neutron_nf[particle]
    dp = proton_nf[particle]
    delta = dn - dp
    energy = delta * E0_from_net
    print(f"  Δ({particle}) = {delta:+.10f}  →  {energy:+.4f} MeV")

# ── Total budget ─────────────────────────────────────────────────
print(f"\n── Full energy budget (all 6 terms × E₀) ──")
total_check = 0
for particle in ["ν", "H⁰", "H¹", "L₊", "L₋", "e⁻"]:
    dn = neutron_nf[particle]
    dp = proton_nf[particle]
    delta = dn - dp
    energy = delta * E0_from_net
    total_check += energy
    print(f"  Δ({particle:3s}) × E₀ = {energy:+.6f} MeV")
print(f"  {'─' * 35}")
print(f"  Sum          = {total_check:+.6f} MeV")
print(f"  Q (observed) = {Q_decay:+.6f} MeV")

# ── Generate witness JSON ────────────────────────────────────────
output = {
    "computation": "beta-decay-energy-scale",
    "description": (
        "Derives the energy scale E₀ (MeV) converting dimensionless "
        "Hecke NF coefficient differences to physical decay energy. "
        "E₀ = Q_decay / Δ(net) where Q = m_n − m_p − m_e."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q0": Q,
    "observed": {
        "m_n_MeV": M_N_MEV,
        "m_p_MeV": M_P_MEV,
        "m_e_MeV": M_E_MEV,
        "delta_m_MeV": delta_m,
        "Q_decay_MeV": Q_decay,
        "Q_decay_MeV_err": Q_decay_err,
    },
    "hecke_nf_differences": {
        "delta_nu": delta_nu,
        "delta_e": delta_e,
        "delta_net": delta_net,
        "debt_total": debt_total,
    },
    "energy_scales": {
        "E0_from_net_MeV": E0_from_net,
        "E0_from_debt_MeV": E0_from_debt,
        "E0_from_mass_diff_MeV": E0_from_mass,
    },
    "per_channel_MeV": {
        "nu_bar": E_nu_channel,
        "electron": E_e_channel,
        "sum": E_nu_channel + E_e_channel,
    },
    "full_budget_MeV": {
        particle: (neutron_nf[particle] - proton_nf[particle]) * E0_from_net
        for particle in ["ν", "H⁰", "H¹", "L₊", "L₋", "e⁻"]
    },
    "verification": {
        "delta_net_times_E0": Q_predicted_net,
        "Q_observed": Q_decay,
        "match": abs(Q_predicted_net - Q_decay) < 1e-10,
    },
}

witness_out = os.path.join(SCRIPT_DIR, "beta-decay-energy-scale.witness.json")
with open(witness_out, "w") as f:
    json.dump(output, f, indent=2)
print(f"\n✓ Witness written to {witness_out}")
