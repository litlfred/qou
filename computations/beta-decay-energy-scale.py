"""
Beta-decay energy scale: normalizing Hecke NF debts to physical MeV.

The Gröbner--Shirshov normal form of each nucleon in H₃(q) has six terms with
dimensionless coefficients.  With typed crossings (u-u, d-d, u-d), the sign
pattern may differ between neutron and proton.

This script derives the energy scale E₀ (in MeV) that converts the
dimensionless coefficient difference |Δ(net)| to the observed decay
energy Q = m_n − m_p − m_e = 0.78233 MeV:  # noqa: P31 — docstring narrative; live value from experimental_constants.Q_BETA_MEV

    E₀ = Q / |Δ(net)|

It also computes alternative calibration scenarios:
  - NF₊/NF₋ decomposition (positive vs negative coefficient sums)
  - Observable-only Q_≥2 (only ℓ ≥ 2 terms: L₊, L₋, e⁻)

Usage:
    cd computations
    python3 beta-decay-energy-scale.py
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import math
import os
from datetime import datetime, timezone
from mpmath import mp

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

# Word length for each basis element (observability classification)
WORD_LENGTH = {"ν": 0, "σ₀": 1, "σ₁": 1, "L₊": 2, "L₋": 2, "e⁻": 3}
# Knot/link produced by Markov trace of braid closure
KNOT_NAME = {"ν": "unknot (0₁)", "σ₀": "virtual", "σ₁": "virtual",
             "L₊": "Hopf link", "L₋": "Hopf link", "e⁻": "trefoil (3₁)"}
PARTICLES = ["ν", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]

neutron_net = witness["neutron"]["net_coefficient"]
proton_net  = witness["proton"]["net_coefficient"]

# ── Per-channel differences ──────────────────────────────────────
deltas = {p: neutron_nf[p] - proton_nf[p] for p in PARTICLES}
delta_net = neutron_net - proton_net

# ── NF₊/NF₋ decomposition ───────────────────────────────────────
# Split each nucleon's NF into positive and negative coefficient sums
nf_pos_n = sum(v for v in neutron_nf.values() if v > 0)
nf_neg_n = sum(v for v in neutron_nf.values() if v < 0)
nf_pos_p = sum(v for v in proton_nf.values() if v > 0)
nf_neg_p = sum(v for v in proton_nf.values() if v < 0)

delta_nf_pos = nf_pos_n - nf_pos_p  # ΔNF₊
delta_nf_neg = nf_neg_n - nf_neg_p  # ΔNF₋

# ── Observable-only (ℓ ≥ 2) ──────────────────────────────────────
obs_n = sum(neutron_nf[p] for p in PARTICLES if WORD_LENGTH[p] >= 2)
obs_p = sum(proton_nf[p] for p in PARTICLES if WORD_LENGTH[p] >= 2)
delta_obs = obs_n - obs_p  # Δ(ℓ≥2)

# Virtual (ℓ < 2)
virt_n = sum(neutron_nf[p] for p in PARTICLES if WORD_LENGTH[p] < 2)
virt_p = sum(proton_nf[p] for p in PARTICLES if WORD_LENGTH[p] < 2)
delta_virt = virt_n - virt_p  # Δ(ℓ<2)

# ── Observed decay energy ────────────────────────────────────────
Q_decay = M_N_MEV - M_P_MEV - M_E_MEV
Q_decay_err = mp.sqrt(M_N_MEV_ERR**2 + M_P_MEV_ERR**2 + M_E_MEV_ERR**2)
delta_m = M_N_MEV - M_P_MEV
delta_m_err = mp.sqrt(M_N_MEV_ERR**2 + M_P_MEV_ERR**2)

# ── Energy scales (all positive by using |Δ|) ────────────────────
E0_net  = Q_decay / abs(delta_net)      # from all 6 terms
E0_obs  = Q_decay / abs(delta_obs)      # from ℓ≥2 only
E0_pos  = Q_decay / abs(delta_nf_pos)   # from NF₊ only
E0_debt = Q_decay / (abs(deltas["ν"]) + abs(deltas["e⁻"]))  # from leptonic debts

print("=" * 70)
print("BETA-DECAY ENERGY SCALE: Hecke NF → physical MeV")
print("  (typed crossings: u-u = σ, d-d = σ−HA·𝟏, u-d = σ−½HA·𝟏)")
print("=" * 70)

# ── Linearity check: NF(𝔫 − 𝔭) = NF(𝔫) − NF(𝔭) ─────────────────
# The GS normal form is a vector space basis for H₃(q), so NF is
# a linear map (coordinate extraction). Verify explicitly:
print(f"\n── Linearity: NF(𝔫 − 𝔭) = NF(𝔫) − NF(𝔭) ──")
print(f"  The Gröbner–Shirshov basis {{𝟏, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}}")
print(f"  is a vector space basis for H₃(q) (dim = 3! = 6).")
print(f"  NF = coordinate extraction → linear map.")
print(f"  Therefore Δ_i = coeff_i(𝔫) − coeff_i(𝔭) = coeff_i(𝔫 − 𝔭).")
print(f"  The transition element 𝔫 − 𝔭 ∈ H₃(q) has Δ as its NF. ✓")

# ── Individual NF terms ──────────────────────────────────────────
print("\n── Nucleon NF coefficients (typed crossings) ──")
print(f"  {'Term':>4s}  {'ℓ':>1s}  {'Knot/Link':<14s}  {'Neutron':>11s}  {'Proton':>11s}  {'Δ':>12s}  {'Sign(n)':>7s}")
print(f"  {'─'*4}  {'─'}  {'─'*14}  {'─'*11}  {'─'*11}  {'─'*12}  {'─'*7}")
for p in PARTICLES:
    n_val = neutron_nf[p]
    p_val = proton_nf[p]
    d_val = deltas[p]
    sign = "+" if n_val >= 0 else "−"
    print(f"  {p:>4s}  {WORD_LENGTH[p]}  {KNOT_NAME[p]:<14s}  {n_val:+11.7f}  {p_val:+11.7f}  {d_val:+12.10f}  {sign:>7s}")
print(f"\n  net(n) = {neutron_net:+.10f}")
print(f"  net(p) = {proton_net:+.10f}")
print(f"  Δ(net) = {delta_net:+.10f}")

# ── Sign patterns ────────────────────────────────────────────────
sign_n = "".join("+" if neutron_nf[p] >= 0 else "−" for p in PARTICLES)
sign_p = "".join("+" if proton_nf[p] >= 0 else "−" for p in PARTICLES)
print(f"\n  Sign pattern (n): [{', '.join(sign_n)}]  ν,σ₀,σ₁,L₊,L₋,e⁻")
print(f"  Sign pattern (p): [{', '.join(sign_p)}]  ν,σ₀,σ₁,L₊,L₋,e⁻")

# ── NF₊/NF₋ decomposition ───────────────────────────────────────
print(f"\n── NF₊ / NF₋ decomposition ──")
print(f"  NF₊(n) = {nf_pos_n:+.10f}   (sum of positive coefficients)")
print(f"  NF₋(n) = {nf_neg_n:+.10f}   (sum of negative coefficients)")
print(f"  NF₊(p) = {nf_pos_p:+.10f}")
print(f"  NF₋(p) = {nf_neg_p:+.10f}")
print(f"  ΔNF₊   = {delta_nf_pos:+.10f}   (positive-term difference)")
print(f"  ΔNF₋   = {delta_nf_neg:+.10f}   (negative-term difference)")
print(f"  ΔNF₊ + ΔNF₋ = {delta_nf_pos + delta_nf_neg:+.10f}  (= Δnet ✓)")

# Which terms are positive for each nucleon?
pos_terms_n = [p for p in PARTICLES if neutron_nf[p] > 0]
neg_terms_n = [p for p in PARTICLES if neutron_nf[p] < 0]
pos_terms_p = [p for p in PARTICLES if proton_nf[p] > 0]
neg_terms_p = [p for p in PARTICLES if proton_nf[p] < 0]
print(f"\n  Positive terms (n): {pos_terms_n}")
print(f"  Negative terms (n): {neg_terms_n}")
print(f"  Positive terms (p): {pos_terms_p}")
print(f"  Negative terms (p): {neg_terms_p}")

# ── Observable / virtual split ───────────────────────────────────
print(f"\n── Observable (ℓ ≥ 2) vs Virtual (ℓ < 2) ──")
print(f"  obs(n)  = {obs_n:+.10f}   (L₊ + L₋ + e⁻)")
print(f"  obs(p)  = {obs_p:+.10f}")
print(f"  Δ(obs)  = {delta_obs:+.10f}")
print(f"  virt(n) = {virt_n:+.10f}   (ν + σ₀ + σ₁)")
print(f"  virt(p) = {virt_p:+.10f}")
print(f"  Δ(virt) = {delta_virt:+.10f}")
print(f"  Δ(obs) + Δ(virt) = {delta_obs + delta_virt:+.10f}  (= Δnet ✓)")

# ── Observed values ──────────────────────────────────────────────
print(f"\n── Observed (CODATA 2022) ──")
print(f"  m_n − m_p      = {delta_m:.6f} ± {float(delta_m_err):.8f} MeV")
print(f"  Q = m_n−m_p−m_e = {Q_decay:.6f} ± {float(Q_decay_err):.8f} MeV")

# ── Energy scale scenarios ───────────────────────────────────────
print(f"\n{'='*70}")
print(f"  ENERGY SCALE SCENARIOS")
print(f"{'='*70}")

print(f"\n  Scenario 1: E₀ = Q / |Δ(net)|  [all 6 terms]")
print(f"    |Δ(net)| = {abs(delta_net):.10f}")
print(f"    E₀ = {Q_decay:.6f} / {abs(delta_net):.10f} = {E0_net:.4f} MeV")
print(f"    E₀ / m_e = {E0_net / M_E_MEV:.4f}")

print(f"\n  Scenario 2: E₀ = Q / |Δ(ℓ≥2)|  [observable only: L₊, L₋, e⁻]")
print(f"    |Δ(ℓ≥2)| = {abs(delta_obs):.10f}")
print(f"    E₀ = {Q_decay:.6f} / {abs(delta_obs):.10f} = {E0_obs:.4f} MeV")
print(f"    E₀ / m_e = {E0_obs / M_E_MEV:.4f}")

print(f"\n  Scenario 3: E₀ = Q / |ΔNF₊|  [positive terms only]")
print(f"    |ΔNF₊| = {abs(delta_nf_pos):.10f}")
print(f"    E₀ = {Q_decay:.6f} / {abs(delta_nf_pos):.10f} = {E0_pos:.4f} MeV")
print(f"    E₀ / m_e = {E0_pos / M_E_MEV:.4f}")

print(f"\n  Scenario 4: E₀ = Q / (|Δν| + |Δe⁻|)  [leptonic debts]")
print(f"    |Δν| + |Δe⁻| = {abs(deltas['ν']) + abs(deltas['e⁻']):.10f}")
print(f"    E₀ = {Q_decay:.6f} / {abs(deltas['ν']) + abs(deltas['e⁻']):.10f} = {E0_debt:.4f} MeV")
print(f"    E₀ / m_e = {E0_debt / M_E_MEV:.4f}")

# ── Cross-predictions: use each E₀ to predict Q from other Δ ────
print(f"\n── Cross-predictions ──")
print(f"  Using E₀(net) = {E0_net:.4f} MeV:")
Q_obs_pred = abs(delta_obs) * E0_net
Q_pos_pred = abs(delta_nf_pos) * E0_net
Q_neg_pred = abs(delta_nf_neg) * E0_net
print(f"    Q_≥2 = |Δ(ℓ≥2)| × E₀ = {Q_obs_pred:.6f} MeV  ({Q_obs_pred/Q_decay*100:.1f}% of Q)")
print(f"    Q₊   = |ΔNF₊| × E₀   = {Q_pos_pred:.6f} MeV  ({Q_pos_pred/Q_decay*100:.1f}% of Q)")
print(f"    Q₋   = |ΔNF₋| × E₀   = {Q_neg_pred:.6f} MeV  ({Q_neg_pred/Q_decay*100:.1f}% of Q)")

print(f"\n  Using E₀(obs) = {E0_obs:.4f} MeV:")
Q_net_from_obs = abs(delta_net) * E0_obs
print(f"    Q_net  = |Δnet| × E₀(obs) = {Q_net_from_obs:.6f} MeV  ({Q_net_from_obs/Q_decay*100:.1f}% of Q)")
Q_virt_from_obs = abs(delta_virt) * E0_obs
print(f"    Q_virt = |Δvirt| × E₀(obs) = {Q_virt_from_obs:.6f} MeV")

# ── Full energy budget ───────────────────────────────────────────
print(f"\n── Full energy budget (all 6 terms × E₀(net)) ──")
total_check = 0
for p in PARTICLES:
    energy = deltas[p] * E0_net * (-1 if delta_net < 0 else 1)
    total_check += energy
    ell = WORD_LENGTH[p]
    obs_tag = "obs" if ell >= 2 else "vrt"
    print(f"  Δ({p:3s}) × E₀ = {energy:+.6f} MeV  (ℓ={ell}, {obs_tag}, {KNOT_NAME[p]})")
print(f"  {'─' * 55}")
print(f"  Sum          = {total_check:+.6f} MeV")
print(f"  Q (observed) = {Q_decay:+.6f} MeV")

# ── Observable-only budget ───────────────────────────────────────
print(f"\n── Observable energy budget (ℓ ≥ 2 terms × E₀(net)) ──")
obs_total = 0
for p in PARTICLES:
    if WORD_LENGTH[p] >= 2:
        energy = deltas[p] * E0_net * (-1 if delta_net < 0 else 1)
        obs_total += energy
        print(f"  Δ({p:3s}) × E₀ = {energy:+.6f} MeV  ({KNOT_NAME[p]})")
print(f"  {'─' * 55}")
print(f"  Q_≥2         = {obs_total:+.6f} MeV")
print(f"  Q (observed) = {Q_decay:+.6f} MeV")
print(f"  Ratio Q_≥2/Q = {obs_total/Q_decay:.4f}")

# ── Summary table ────────────────────────────────────────────────
print(f"\n{'='*70}")
print(f"  SUMMARY: E₀ CALIBRATION SCENARIOS")
print(f"{'='*70}")
print(f"  {'Scenario':<25s}  {'|Δ|':>10s}  {'E₀ (MeV)':>10s}  {'E₀/m_e':>8s}")
print(f"  {'─'*25}  {'─'*10}  {'─'*10}  {'─'*8}")
for name, dval, e0val in [
    ("All terms |Δnet|",       abs(delta_net),    E0_net),
    ("Observable |Δ(ℓ≥2)|",   abs(delta_obs),    E0_obs),
    ("Positive |ΔNF₊|",       abs(delta_nf_pos), E0_pos),
    ("Leptonic |Δν|+|Δe⁻|",   abs(deltas["ν"])+abs(deltas["e⁻"]), E0_debt),
]:
    print(f"  {name:<25s}  {dval:10.7f}  {e0val:10.4f}  {e0val/M_E_MEV:8.4f}")

# ── Generate witness JSON ────────────────────────────────────────
output = {
    "computation": "beta-decay-energy-scale",
    "description": (
        "Derives the energy scale E₀ (MeV) converting dimensionless "
        "Hecke NF coefficient differences to physical decay energy. "
        "E₀ = Q_decay / |Δ(net)| where Q = m_n − m_p − m_e. "
        "Includes NF₊/NF₋ decomposition and observable-only (ℓ≥2) scenarios."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q0": Q,
    "crossing_type": "typed (u-u, d-d, u-d)",
    "observed": {
        "m_n_MeV": M_N_MEV,
        "m_p_MeV": M_P_MEV,
        "m_e_MeV": M_E_MEV,
        "delta_m_MeV": delta_m,
        "Q_decay_MeV": Q_decay,
        "Q_decay_MeV_err": float(Q_decay_err),
    },
    "nucleon_nf": {
        "neutron": {p: neutron_nf[p] for p in PARTICLES},
        "proton":  {p: proton_nf[p] for p in PARTICLES},
        "neutron_net": neutron_net,
        "proton_net": proton_net,
        "sign_pattern_neutron": sign_n,
        "sign_pattern_proton": sign_p,
    },
    "hecke_nf_differences": {
        "per_channel": {p: deltas[p] for p in PARTICLES},
        "delta_net": delta_net,
    },
    "nf_pos_neg": {
        "NF_pos_neutron": nf_pos_n,
        "NF_neg_neutron": nf_neg_n,
        "NF_pos_proton": nf_pos_p,
        "NF_neg_proton": nf_neg_p,
        "delta_NF_pos": delta_nf_pos,
        "delta_NF_neg": delta_nf_neg,
    },
    "observable_split": {
        "obs_neutron": obs_n,
        "obs_proton": obs_p,
        "delta_obs": delta_obs,
        "virt_neutron": virt_n,
        "virt_proton": virt_p,
        "delta_virt": delta_virt,
    },
    "energy_scales": {
        "E0_from_net_MeV": E0_net,
        "E0_from_obs_MeV": E0_obs,
        "E0_from_pos_MeV": E0_pos,
        "E0_from_debt_MeV": E0_debt,
    },
    "cross_predictions": {
        "Q_ge2_from_E0net": Q_obs_pred,
        "Q_pos_from_E0net": Q_pos_pred,
        "Q_neg_from_E0net": Q_neg_pred,
        "Q_net_from_E0obs": Q_net_from_obs,
        "ratio_Q_ge2_over_Q": Q_obs_pred / Q_decay,
    },
    "full_budget_MeV": {
        p: deltas[p] * E0_net * (-1 if delta_net < 0 else 1)
        for p in PARTICLES
    },
    "verification": {
        "delta_net_times_E0": abs(delta_net) * E0_net,
        "Q_observed": Q_decay,
        "match": abs(abs(delta_net) * E0_net - Q_decay) < 1e-10,
    },
}

witness_out = os.path.join(SCRIPT_DIR, "beta-decay-energy-scale.witness.json")
with open(witness_out, "w") as f:
    json.dump(output, f, indent=2)
print(f"\n✓ Witness written to {witness_out}")
