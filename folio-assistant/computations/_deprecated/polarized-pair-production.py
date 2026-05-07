#!/usr/bin/env python3
"""
Pair production with distinct polarization modes: γ(φ₁)·γ(φ₂) → e⁻ + e⁺

Each photon is represented as a linear combination of the two pure
polarization modes in H₃(q):

    γ(φ) = φ·σ₀ + (1−φ)·σ₁      φ ∈ [0, 1]

  φ = 1  ↔  pure mode A  (σ₀, horizontal crossing)
  φ = 0  ↔  pure mode B  (σ₁, vertical crossing)
  φ = ½  ↔  equal mix

The two-photon state γ(φ₁)·γ(φ₂) expands to four products:

    φ₁φ₂·σ₀²  +  φ₁(1−φ₂)·σ₀σ₁  +  (1−φ₁)φ₂·σ₁σ₀  +  (1−φ₁)(1−φ₂)·σ₁²

Applying the Hecke relation σᵢ² = (q−q⁻¹)σᵢ + 𝟏 to the same-mode terms:

    σ₀² → HA·σ₀ + 𝟏
    σ₁² → HA·σ₁ + 𝟏
    σ₀σ₁  = L₊  (already NF — Hopf link)
    σ₁σ₀  = L₋  (already NF — Hopf link, reversed)

The NF of the two-photon state is therefore EXACT and CLOSED-FORM:

    NF(γ(φ₁)·γ(φ₂))
        = S·𝟏                        (S = φ₁φ₂ + (1−φ₁)(1−φ₂))
        + φ₁φ₂·HA·σ₀
        + (1−φ₁)(1−φ₂)·HA·σ₁
        + C₊·L₊                      (C₊ = φ₁(1−φ₂))
        + C₋·L₋                      (C₋ = (1−φ₁)φ₂)

where   S + C₊ + C₋ = 1   (partition of amplitude).

The net coefficient simplifies beautifully:

    net(γγ) = 1 + S·HA

ranging from 1 (distinct modes, S=0) to 1+HA ≈ 1.209 (same mode, S=1).

The pair-production calibration of E₀ then depends on polarization:

    Δ(pair)(φ₁,φ₂) = net(e⁻) + net(e⁺) − net(γγ)
                    = net(e⁺) − S·HA            (since net(e⁻)=1)
    E₀(φ₁,φ₂)      = 2mₑ / Δ(pair)(φ₁,φ₂)

Special cases:
  Same mode (φ₁=φ₂): S=1,   E₀ = 2mₑ/(net(e⁺)−HA)  ≈ 4.22 MeV
  Distinct modes:    S=0,   E₀ = 2mₑ/net(e⁺)         ≈ 2.27 MeV

Usage:
    cd folio-assistant/computations
    python3 polarized-pair-production.py
"""

import json
import math
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import Q as q0, Q_INV, HA, E_CROSS, HBAR_Q
from experimental_constants import M_E_MEV

# ── Git SHA ──────────────────────────────────────────────────────
try:
    SHA = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=str(Path(__file__).resolve().parent.parent.parent),
    ).decode().strip()
except Exception:
    SHA = "unknown"

# ── Load e⁺ NF from pair-production witness ─────────────────────
_pp_path = Path(__file__).parent / "pair-production-nf.witness.json"
with _pp_path.open() as _f:
    _pp = json.load(_f)

net_eminus = _pp["nf_eminus"]["_net"]   # always 1.0 (trefoil = σ₀σ₁σ₀, already NF)
net_eplus  = _pp["nf_eplus"]["_net"]    # ≈ 0.4511

# ── Beta-decay energy scale ──────────────────────────────────────
_esc_path = Path(__file__).parent / "beta-decay-energy-scale.witness.json"
with _esc_path.open() as _f:
    _esc = json.load(_f)
E0_beta = _esc["energy_scales"]["E0_from_net_MeV"]

# ── Core symbolic formula ────────────────────────────────────────
def photon_nf(phi1: float, phi2: float) -> dict:
    """
    Return the NF decomposition of γ(φ₁)·γ(φ₂) as a dict {basis_word: coefficient}.

    Basis words: '𝟏', 'σ₀', 'σ₁', 'L₊', 'L₋'
    """
    S   = phi1 * phi2 + (1 - phi1) * (1 - phi2)   # same-mode diagonal
    Cp  = phi1 * (1 - phi2)                         # cross: σ₀σ₁
    Cm  = (1 - phi1) * phi2                         # cross: σ₁σ₀
    return {
        "𝟏":  S,
        "σ₀": phi1 * phi2 * HA,
        "σ₁": (1 - phi1) * (1 - phi2) * HA,
        "L₊": Cp,
        "L₋": Cm,
    }

def net_gamma2(phi1: float, phi2: float) -> float:
    """Net NF coefficient of γ(φ₁)·γ(φ₂).  Exact: 1 + S·HA."""
    S = phi1 * phi2 + (1 - phi1) * (1 - phi2)
    return 1.0 + S * HA

def delta_pair(phi1: float, phi2: float) -> float:
    """Pair-production threshold difference Δ = net(e⁻) + net(e⁺) − net(γγ)."""
    return net_eminus + net_eplus - net_gamma2(phi1, phi2)

def E0_pair(phi1: float, phi2: float) -> float:
    """E₀ calibrated from pair-production at polarizations (φ₁, φ₂)."""
    return 2.0 * M_E_MEV / delta_pair(phi1, phi2)

# ── Print header ─────────────────────────────────────────────────
print("=" * 72)
print("POLARIZED PAIR PRODUCTION: γ(φ₁)·γ(φ₂) → e⁻ + e⁺")
print("=" * 72)
print()
print("Photon representation:   γ(φ) = φ·σ₀ + (1−φ)·σ₁")
print("φ=1 ↔ pure mode A (σ₀)     φ=0 ↔ pure mode B (σ₁)")
print()
print(f"q₀ = {q0:.12f}")
print(f"HA = q−q⁻¹ = {HA:.12f}")
print()

# ── Symbolic NF formula ───────────────────────────────────────────
print("── Closed-form NF (exact, symbolic in HA) ──────────────────")
print()
print("NF(γ(φ₁)·γ(φ₂)) = S·𝟏  +  φ₁φ₂·HA·σ₀  +  (1−φ₁)(1−φ₂)·HA·σ₁")
print("                       +  C₊·L₊  +  C₋·L₋")
print()
print("where:")
print("  S  = φ₁φ₂ + (1−φ₁)(1−φ₂)   [same-mode amplitude]")
print("  C₊ = φ₁(1−φ₂)               [cross: γ₁=σ₀, γ₂=σ₁  → L₊]")
print("  C₋ = (1−φ₁)φ₂               [cross: γ₁=σ₁, γ₂=σ₀  → L₋]")
print()
print("  S + C₊ + C₋ = 1             [amplitude partition]")
print()
print("  net(γγ) = S·(1+HA) + C₊ + C₋")
print("          = S·HA + (S + C₊ + C₋)")
print("          = 1 + S·HA           ← EXACT closed form")
print()
print(f"  At q₀: net ranges from 1+HA = {1+HA:.6f} (same mode, S=1)")
print(f"                         to  1 = {1.0:.6f} (distinct modes, S=0)")
print()

# ── e⁻, e⁺ NF ───────────────────────────────────────────────────
print("── Electron / Positron NF (from pair-production-nf.witness.json) ──")
print()
print(f"  NF(e⁻) = σ₀σ₁σ₀  (trefoil, already NF)")
print(f"    net(e⁻) = {net_eminus:.10f}")
print()
print("  NF(e⁺) = σ₀⁻¹σ₁⁻¹σ₀⁻¹  (mirror trefoil, expanded via σᵢ⁻¹=σᵢ−HA)")
print(f"    net(e⁺) = {net_eplus:.10f}")
print()
print("  NF(e⁺) term-by-term:")
for k, v in _pp["nf_eplus"].items():
    if k != "_net":
        print(f"    {v['particle']:4s} ({v['word']:10s}): {v['at_q0']:+.12f}")
print()

# ── Special cases ────────────────────────────────────────────────
print("── Special cases ────────────────────────────────────────────")
print()
cases = [
    (1.0, 1.0, "same-mode A  (σ₀²):  current calculation"),
    (0.0, 0.0, "same-mode B  (σ₁²):  by σ₀↔σ₁ symmetry"),
    (1.0, 0.0, "distinct A→B (L₊=σ₀σ₁)"),
    (0.0, 1.0, "distinct B→A (L₋=σ₁σ₀)"),
    (0.5, 0.5, "equal mix    (φ₁=φ₂=½)"),
    (1.0, 0.5, "half-polarized (φ₁=1, φ₂=½)"),
    (0.5, 0.0, "half-polarized (φ₁=½, φ₂=0)"),
]

header = f"  {'case':<38} {'S':>6} {'net(γγ)':>10} {'Δ(pair)':>10} {'E₀(MeV)':>10}"
print(header)
print("  " + "─" * (len(header) - 2))

case_data = []
for phi1, phi2, label in cases:
    S   = phi1 * phi2 + (1 - phi1) * (1 - phi2)
    ng  = net_gamma2(phi1, phi2)
    D   = delta_pair(phi1, phi2)
    E0  = E0_pair(phi1, phi2)
    nf  = photon_nf(phi1, phi2)
    print(f"  {label:<38} {S:>6.3f} {ng:>10.6f} {D:>10.6f} {E0:>10.4f}")
    case_data.append({
        "phi1": phi1, "phi2": phi2, "label": label,
        "S": S, "net_gamma2": ng, "delta_pair": D,
        "E0_pair_MeV": E0,
        "nf_terms": nf,
    })

print()
print(f"  Beta-decay E₀ (reference):                          {E0_beta:>10.4f} MeV")
print()

# ── General formula for E₀(S) ───────────────────────────────────
print("── General E₀(S) formula ────────────────────────────────────")
print()
print("  E₀(φ₁,φ₂) = 2mₑ / (net(e⁺) − S·HA)")
print()
print("  where S = φ₁φ₂ + (1−φ₁)(1−φ₂)")
print()
print(f"  net(e⁺) = {net_eplus:.8f}")
print(f"  HA      = {HA:.8f}")
print()
print(f"  S=1 (same mode):     E₀ = 2mₑ / (net(e⁺)−HA)")
E0_same = 2 * M_E_MEV / (net_eplus - HA)
print(f"                           = {2*M_E_MEV:.7f} / {net_eplus-HA:.8f} = {E0_same:.5f} MeV")
print()
print(f"  S=0 (distinct mode): E₀ = 2mₑ / net(e⁺)")
E0_distinct = 2 * M_E_MEV / net_eplus
print(f"                           = {2*M_E_MEV:.7f} / {net_eplus:.8f} = {E0_distinct:.5f} MeV")
print()
print(f"  Ratio E₀(same) / E₀(distinct) = {E0_same/E0_distinct:.6f}")
print(f"  Ratio E₀(beta) / E₀(same)     = {E0_beta/E0_same:.6f}")
print(f"  Ratio E₀(beta) / E₀(distinct) = {E0_beta/E0_distinct:.6f}")
print()

# ── Physical interpretation ───────────────────────────────────────
print("── Physical interpretation ──────────────────────────────────")
print()
print("  The same-mode photon state γγ = σ₀² carries an 'extra' Hopf")
print("  link contribution (HA·σ₀) that partially annihilates the")
print("  positron's vacuum debt.  The pair threshold is LOWER for")
print("  same-mode photons because the two-photon vacuum is 'richer'.")
print()
print("  Distinct-mode photons (L₊ or L₋) carry no reducible structure")
print("  — they are already a Hopf link themselves.  The pair threshold")
print("  is HIGHER because the photon field has no self-crossing budget.")
print()
print("  The physical photon is neither pure mode A nor pure mode B.")
print("  Setting S to match the observed ratio:")
E0_obs = E0_beta
S_target = (net_eplus - 2*M_E_MEV/E0_obs) / HA
print(f"    E₀(beta)  = {E0_obs:.5f} MeV  →  S* = (net(e⁺) − 2mₑ/E₀) / HA")
print(f"    S* = ({net_eplus:.6f} − {2*M_E_MEV/E0_obs:.6f}) / {HA:.6f}")
print(f"    S* = {S_target:.6f}")
print()
if 0 <= S_target <= 1:
    phi_sym = (1 - math.sqrt(1 - 2*(1-S_target))) / 2 if S_target < 0.5 else None
    print(f"  S* ∈ [0,1] ✓  — corresponds to a partial polarization overlap.")
else:
    print(f"  S* = {S_target:.6f} outside [0,1] — the beta-decay E₀ is not")
    print("  achievable from pair production calibration alone.")
print()

# ── Normalization by setting φ₁=0, φ₂=observed ──────────────────
print("── Normalization: φ₁=0, φ₂=φ_obs ───────────────────────────")
print()
print("  If we set φ₁=0 (γ₁ purely mode B = σ₁) and vary φ₂:")
print()
print(f"  {'φ₂':>6} {'S':>8} {'net(γγ)':>10} {'Δ(pair)':>10} {'E₀(MeV)':>10}")
print("  " + "─" * 50)
phi1_fixed = 0.0
for phi2 in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    S = phi1_fixed * phi2 + (1 - phi1_fixed) * (1 - phi2)
    ng = net_gamma2(phi1_fixed, phi2)
    D = delta_pair(phi1_fixed, phi2)
    E0_v = E0_pair(phi1_fixed, phi2)
    print(f"  {phi2:>6.2f} {S:>8.4f} {ng:>10.6f} {D:>10.6f} {E0_v:>10.4f}")
print()

# ── Write witness ────────────────────────────────────────────────
output = {
    "name": "polarized-pair-production",
    "description": (
        "Gröbner--Shirshov NF for γ(φ₁)·γ(φ₂) → e⁻ + e⁺ with distinct polarization modes. "
        "Each photon γ(φ) = φ·σ₀ + (1−φ)·σ₁.  NF is exact and closed-form: "
        "net(γγ) = 1 + S·HA where S = φ₁φ₂ + (1−φ₁)(1−φ₂)."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "git_sha": SHA,
    "parameters": {
        "q0": q0,
        "HA": HA,
        "net_eminus": net_eminus,
        "net_eplus": net_eplus,
        "m_e_MeV": M_E_MEV,
        "threshold_2me_MeV": 2.0 * M_E_MEV,
        "E0_beta_MeV": E0_beta,
    },
    "symbolic_nf": {
        "formula": "NF(γ(φ₁)·γ(φ₂)) = S·𝟏 + φ₁φ₂·HA·σ₀ + (1-φ₁)(1-φ₂)·HA·σ₁ + C₊·L₊ + C₋·L₋",
        "net_formula": "net(γγ) = 1 + S·HA",
        "delta_pair_formula": "Δ(pair) = net(e⁺) - S·HA",
        "E0_formula": "E₀(φ₁,φ₂) = 2mₑ / (net(e⁺) - S·HA)",
        "S_definition": "S = φ₁φ₂ + (1-φ₁)(1-φ₂)  [same-mode amplitude, S∈[0,1]]",
        "amplitude_partition": "S + C₊ + C₋ = 1",
    },
    "E0_limits": {
        "same_mode_S1": {"S": 1.0, "E0_MeV": E0_same, "label": "same mode (σ₀² or σ₁²)"},
        "distinct_S0":  {"S": 0.0, "E0_MeV": E0_distinct, "label": "distinct modes (L₊ or L₋)"},
        "beta_decay_ref": {"E0_MeV": E0_beta, "S_equivalent": S_target, "label": "beta decay calibration"},
    },
    "cases": case_data,
}

out_path = Path(__file__).parent / "polarized-pair-production.witness.json"
with out_path.open("w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"✓ Witness written to {out_path}")
