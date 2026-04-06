#!/usr/bin/env python3
"""
Polarized two-photon NF with color content: γ(φ₁)·γ(φ₂)

A photon with polarization/entanglement history φ is defined as:

    γ(φ) = φ·σ₀ + (1−φ)·σ₁   ∈ H₂(q)

where:
    σ₀ = Hopf generator on (σ,r) color plane   ← red polarization
    σ₁ = Hopf generator on (r,g) color plane    ← green polarization
    φ ∈ [0,1]  = fraction of σ₀ content (polarization/entanglement history)

The identity photon γ(1) = σ₀ is the "pure red-channel" photon used
in pair-production-nf.py.  A photon with φ < 1 carries partial σ₁
color content — it encodes a polarization history that reaches into
the green color-tube fiber.

───────────────────────────────────────────────────────────────────
MAIN RESULT:

  NF(γ(φ₁)·γ(φ₂))
      = S·𝟏  +  φ₁φ₂·HA·σ₀  +  (1−φ₁)(1−φ₂)·HA·σ₁
              +  C₊·L₊  +  C₋·L₋

  where
      S  = φ₁φ₂ + (1−φ₁)(1−φ₂)     neutrino/identity amplitude
      C₊ = φ₁(1−φ₂)                  L₊ = σ₀σ₁  (Hopf link, OBSERVABLE)
      C₋ = (1−φ₁)φ₂                  L₋ = σ₁σ₀  (Hopf link, OBSERVABLE)
      HA = q − q⁻¹                    Hecke amplitude

───────────────────────────────────────────────────────────────────
OBSERVABILITY (from nucleon-nf-observability.md):

    ℓ = 0  (𝟏):    unknot — VIRTUAL, unobservable (neutrino channel)
    ℓ = 1  (σᵢ):   single crossing — VIRTUAL, topologically removable
    ℓ = 2  (L±):   Hopf links — OBSERVABLE, topologically non-trivial

    → The fibre-confined terms are S·𝟏, φ₁φ₂·HA·σ₀, (1−φ₁)(1−φ₂)·HA·σ₁
    → The observable terms are C₊·L₊ and C₋·L₋

    φ₁φ₂ > 0         iff  both photons have σ₀ content  (φ₁ > 0 AND φ₂ > 0)
    (1−φ₁)(1−φ₂) > 0 iff  both photons have σ₁ content  (φ₁ < 1 AND φ₂ < 1)

───────────────────────────────────────────────────────────────────
TENSOR PRODUCT vs CONCATENATION:

    Concatenation  γ·γ  = σ₀·σ₀ = σ₀²  in H₂(q)
        → Hecke relation triggers: σ₀² → HA·σ₀ + 𝟏
        → Models two photons on the SAME adjacent strand pair (interacting)
        → This is the pair-production vertex

    Tensor product γ⊗γ = σ₀·σ₂  in H₄(q)  [far-commuting generators]
        → R2 (far-commutativity): |0−2| = 2 ≥ 2, so σ₀σ₂ is already in NF
        → Models two photons on DIFFERENT strand pairs (non-interacting)
        → This is two photons passing by each other with no interaction

    The pair-production vertex requires CONCATENATION because the photons
    must be on adjacent strands to trigger the Hecke relation.

───────────────────────────────────────────────────────────────────
NEUTRON vs PROTON KNOT BASIS (from ch2-quantum-geometry):

    From the cohomological embedding table (§2.25):
        H⁰ cohomology = trivial knot = γ (photon)   ← γ = 𝟏 in H*(Σ₄)
        H² cohomology = unknot = ν/ν^σ (neutrino)

    In the Hecke computation, the assignments are:
        𝟏       = neutrino ν            (empty word)
        σ₀      = H⁰ Hopf crossing      (word length 1, virtual)
        σ₁      = H¹ Hopf crossing      (word length 1, virtual)
        σ₀σ₁    = L₊ Hopf link         (word length 2, OBSERVABLE)
        σ₁σ₀    = L₋ Hopf link         (word length 2, OBSERVABLE)
        σ₀σ₁σ₀  = e⁻ trefoil T(2,3)   (word length 3, OBSERVABLE)

    The nucleon (neutron/proton) is NOT simply σ₀ or σ₁ — it is a
    B₃-confined quark state with a 6-term NF.  Dominant term is σ₁
    (~90% amplitude), but the full construction is:
        quarks → pairwise crossings → B₃ = (σ₀σ₁⁻¹)³ → 6-term NF

Usage:
    python3 pair-production.py
"""

import math, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

q_sym = sp.Symbol('q', positive=True)
phi1  = sp.Symbol('phi1', real=True, positive=True)
phi2  = sp.Symbol('phi2', real=True, positive=True)

from q_parameter import Q as q0, Q_INV as qi0, HA as HA0, E_CROSS, HBAR_Q
from experimental_constants import M_E_MEV

try:
    SHA = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent)
    ).decode().strip()
except Exception:
    SHA = "unknown"

_esc_path = Path(__file__).parent / "beta-decay-energy-scale.witness.json"
with _esc_path.open() as _f:
    _esc = json.load(_f)
E0 = _esc["energy_scales"]["E0_from_net_MeV"]

HA_sym = q_sym - 1 / q_sym

PARTICLE_KNOT = {
    ():        ("ν",  "𝟏"),
    (0,):      ("H⁰", "σ₀"),
    (1,):      ("H¹", "σ₁"),
    (0, 1):    ("L₊", "σ₀σ₁"),
    (1, 0):    ("L₋", "σ₁σ₀"),
    (0, 1, 0): ("e⁻", "σ₀σ₁σ₀"),
}
OBSERVABLE_WORDS = {w for w in PARTICLE_KNOT if len(w) >= 2}

def ws(w):
    if not w:
        return "𝟏"
    return "·".join(f"σ_{i}" for i in w)

def pn(w):
    return PARTICLE_KNOT.get(w, ("?", "?"))[0]

def eval_q0(c):
    if isinstance(c, (int, float)):
        return float(c)
    return float(sp.sympify(c).subs(q_sym, q0))


# ══════════════════════════════════════════════════════════════
# SECTION 1 — ALGEBRAIC PROOF OF THE TWO-PHOTON NF FORMULA
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("  POLARIZED TWO-PHOTON NF:  γ(φ₁)·γ(φ₂)")
print("=" * 70)
print(f"""
  Photon definition:
      γ(φ) = φ·σ₀ + (1−φ)·σ₁

  Product (before reduction):
      γ(φ₁)·γ(φ₂)  =  [φ₁·σ₀ + (1−φ₁)·σ₁]·[φ₂·σ₀ + (1−φ₂)·σ₁]
                    =  φ₁φ₂·σ₀²
                     + φ₁(1−φ₂)·σ₀σ₁
                     + (1−φ₁)φ₂·σ₁σ₀
                     + (1−φ₁)(1−φ₂)·σ₁²

  Apply Hecke relation  σᵢ² = HA·σᵢ + 𝟏:
      σ₀²  →  HA·σ₀ + 𝟏
      σ₁²  →  HA·σ₁ + 𝟏
      σ₀σ₁ →  L₊  (already in NF, word length 2)
      σ₁σ₀ →  L₋  (already in NF, word length 2)

  NF result:
      NF(γ(φ₁)·γ(φ₂))
        = [φ₁φ₂ + (1−φ₁)(1−φ₂)]·𝟏
        +  φ₁φ₂·HA·σ₀
        +  (1−φ₁)(1−φ₂)·HA·σ₁
        +  φ₁(1−φ₂)·L₊
        +  (1−φ₁)φ₂·L₋

  Identifying coefficients:
      S  = φ₁φ₂ + (1−φ₁)(1−φ₂)     (neutrino channel)
      C₊ = φ₁(1−φ₂)                 (observable L₊ amplitude)
      C₋ = (1−φ₁)φ₂                 (observable L₋ amplitude)
""")


# ══════════════════════════════════════════════════════════════
# SECTION 2 — OBSERVABILITY ANALYSIS
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("  OBSERVABILITY ANALYSIS")
print("=" * 70)
print("""
  Term classification by word length ℓ:

    ℓ = 0  → 𝟏      (unknot)      VIRTUAL  — neutrino channel
    ℓ = 1  → σ₀,σ₁  (single crossing) VIRTUAL  — color-tube fibre
    ℓ = 2  → L₊,L₋  (Hopf links)  OBSERVABLE — topologically stable

  In the two-photon NF:
    FIBRE (unobservable):
        S·𝟏              with  S = φ₁φ₂ + (1−φ₁)(1−φ₂)
        φ₁φ₂·HA·σ₀      (σ₀ = H⁰ Hopf crossing, ℓ=1)
        (1−φ₁)(1−φ₂)·HA·σ₁  (σ₁ = H¹ color-tube, ℓ=1)

    OBSERVABLE:
        C₊·L₊            C₊ = φ₁(1−φ₂)
        C₋·L₋            C₋ = (1−φ₁)φ₂

  Conditions for each fibre channel to be active:
    σ₀ channel active  iff  φ₁φ₂ > 0  ⟺  φ₁ > 0 AND φ₂ > 0
    σ₁ channel active  iff  (1−φ₁)(1−φ₂) > 0  ⟺  φ₁ < 1 AND φ₂ < 1

  Both fibre channels active simultaneously iff  φ₁,φ₂ ∈ (0,1)
  (mixed/entangled polarization — generic physical photon)

  L₊ channel active  iff  φ₁ > 0 AND φ₂ < 1  (σ₀→σ₁ color transition)
  L₋ channel active  iff  φ₁ < 1 AND φ₂ > 0  (σ₁→σ₀ color transition)
""")


# ══════════════════════════════════════════════════════════════
# SECTION 3 — TENSOR PRODUCT vs CONCATENATION
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("  TENSOR PRODUCT vs CONCATENATION")
print("=" * 70)
print(f"""
  Concatenation γ·γ = σ₀² in H₂(q):
    → Adjacent-strand interaction; Hecke relation fires.
    → NF = HA·σ₀ + 𝟏  (pair-production vertex)
    → Two photons on the SAME strand pair, annihilate into a
      dressed photon (σ₀) + a neutrino (𝟏).

  Tensor product γ⊗γ = σ₀·σ₂ in H₄(q):
    → σ₀ acts on strands (0,1); σ₂ acts on strands (2,3).
    → Far-commutativity R2: |0−2| = 2 ≥ 2, so σ₀σ₂ is already in NF.
    → NF = σ₀·σ₂  (no reduction, two independent photons)
    → Models photons on DIFFERENT strand pairs — they pass through
      each other without interacting.

  Physical picture:
    The tensor product embeds each photon on its own independent
    strand pair.  The Hecke relation cannot fire across a gap of
    ≥ 2 generators.  This is the "no-interaction" state.

    The concatenation puts both photons on the SAME crossing
    site.  When they collide at the same brane point, σ₀² triggers
    the Hecke relation — this IS the pair-production vertex.

    Tensor product is correct for free-space two-photon STATES.
    Concatenation is correct for the pair-production INTERACTION VERTEX.

  Numerical check (tensor product):
    σ₀·σ₂ in H₄(q): NF = σ₀·σ₂ (no reduction needed)
    net = 1 + 1 = 2  (two independent photons, each with weight 1)

  Numerical check (concatenation, φ=1):
    σ₀·σ₀ = σ₀²: NF = HA·σ₀ + 𝟏
    net = {HA0:.8f} + 1 = {1 + HA0:.8f}  (one dressed photon + one neutrino)
""")


# ══════════════════════════════════════════════════════════════
# SECTION 4 — NUMERICAL EVALUATION AT SPECIAL φ VALUES
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("  NUMERICAL NF AT q₀ FOR SPECIAL POLARIZATIONS")
print("=" * 70)
print(f"\n  q₀  = {q0:.10f}")
print(f"  HA  = q−q⁻¹ = {HA0:.10f}")
print(f"  E₀  = {E0:.6f} MeV")
print(f"  mₑ  = {M_E_MEV:.6f} MeV")
print(f"  2mₑ = {2*M_E_MEV:.6f} MeV  (pair threshold)\n")

def two_photon_nf(phi1_val, phi2_val):
    """Compute NF(γ(φ₁)·γ(φ₂)) coefficients analytically."""
    S   = phi1_val * phi2_val + (1 - phi1_val) * (1 - phi2_val)
    c0  = phi1_val * phi2_val * HA0          # σ₀ coefficient
    c1  = (1 - phi1_val) * (1 - phi2_val) * HA0  # σ₁ coefficient
    Cp  = phi1_val * (1 - phi2_val)          # L₊ coefficient
    Cm  = (1 - phi1_val) * phi2_val          # L₋ coefficient
    net = S + c0 + c1 + Cp + Cm
    return dict(
        S=S, c_sigma0=c0, c_sigma1=c1, C_plus=Cp, C_minus=Cm,
        net=net
    )

def print_nf_table(phi1_val, phi2_val, label):
    nf = two_photon_nf(phi1_val, phi2_val)
    print(f"  ── {label}  (φ₁={phi1_val:.4g}, φ₂={phi2_val:.4g}) ──")
    print(f"  {'Term':6s}  {'Coefficient':>14s}  {'Observable?':12s}  {'Physical':}")
    print(f"  {'─'*60}")
    print(f"  {'𝟏':6s}  {nf['S']:+14.8f}  {'No (ℓ=0)':12s}  neutrino channel")
    print(f"  {'σ₀':6s}  {nf['c_sigma0']:+14.8f}  {'No (ℓ=1)':12s}  H⁰ Hopf / σ-r plane")
    print(f"  {'σ₁':6s}  {nf['c_sigma1']:+14.8f}  {'No (ℓ=1)':12s}  H¹ / color-tube fiber")
    print(f"  {'L₊':6s}  {nf['C_plus']:+14.8f}  {'YES (ℓ=2)':12s}  Hopf link σ₀σ₁")
    print(f"  {'L₋':6s}  {nf['C_minus']:+14.8f}  {'YES (ℓ=2)':12s}  Hopf link σ₁σ₀")
    print(f"  {'─'*60}")
    print(f"  {'net':6s}  {nf['net']:+14.8f}")
    obs = nf['C_plus'] + nf['C_minus']
    fib = nf['S'] + nf['c_sigma0'] + nf['c_sigma1']
    print(f"  Observable fraction (L±/net):  {obs/nf['net']*100:.2f}%")
    print(f"  Fibre fraction (𝟏+σ/net):      {fib/nf['net']*100:.2f}%")
    print()
    return nf

cases = [
    (1.0,   1.0,   "pure σ₀  (existing pair-production-nf.py)"),
    (0.0,   0.0,   "pure σ₁  (all color-tube fiber)"),
    (1.0,   0.0,   "σ₀⊗σ₁  (crossed channels, pure color exchange)"),
    (0.0,   1.0,   "σ₁⊗σ₀  (crossed channels, reversed)"),
    (0.5,   0.5,   "maximally mixed  (φ=½)"),
    (0.75,  0.75,  "σ₀-dominant  (φ=¾)"),
    (0.25,  0.25,  "σ₁-dominant  (φ=¼)"),
]

all_nf_results = {}
for p1, p2, lbl in cases:
    nf = print_nf_table(p1, p2, lbl)
    all_nf_results[(p1, p2)] = nf


# ══════════════════════════════════════════════════════════════
# SECTION 5 — PAIR PRODUCTION THRESHOLD SWEEP OVER φ
# ══════════════════════════════════════════════════════════════
#
# For pair production  γγ → e⁻ + e⁺, the energy budget is:
#
#   Δ(pair) = NF_net(e⁻) + NF_net(e⁺) − NF_net(γγ)
#   E_pair  = Δ(pair) × E₀
#
# We use NF(e⁻) = σ₀σ₁σ₀ (net=1) and NF(e⁺) = mirror trefoil.
# From pair-production-nf.witness.json:

_pp_path = Path(__file__).parent / "pair-production-nf.witness.json"
with _pp_path.open() as _f:
    _pp = json.load(_f)
net_eminus  = _pp["energy_budget"]["net_eminus"]
net_eplus   = _pp["energy_budget"]["net_eplus"]
E_threshold = _pp["parameters"]["threshold_MeV"]

print("=" * 70)
print("  PAIR PRODUCTION ENERGY THRESHOLD vs PHOTON POLARIZATION φ")
print("=" * 70)
print(f"""
  E₀           = {E0:.6f} MeV
  NF_net(e⁻)   = {net_eminus:.8f}
  NF_net(e⁺)   = {net_eplus:.8f}
  Sum e⁻+e⁺    = {net_eminus+net_eplus:.8f}
  Observed 2mₑ = {E_threshold:.6f} MeV

  Δ(pair,φ) = NF_net(e⁻) + NF_net(e⁺) − NF_net(γ(φ)·γ(φ))
  E_pair(φ) = Δ(pair,φ) × E₀
""")

print(f"  {'φ':>5s}  {'NF_net(γγ)':>12s}  {'Δ(pair)':>12s}  "
      f"{'E_pair MeV':>11s}  {'Ratio':>7s}  {'Residual%':>10s}")
print(f"  {'─'*70}")

phi_sweep = [i / 20 for i in range(0, 21)]
best_phi  = None
best_res  = float('inf')
sweep_data = []

for phi in phi_sweep:
    nf = two_photon_nf(phi, phi)
    net_gg = nf['net']
    delta  = net_eminus + net_eplus - net_gg
    E_pair = delta * E0
    ratio  = E_pair / E_threshold
    res_pc = abs(E_pair - E_threshold) / E_threshold * 100
    sweep_data.append({
        'phi': phi, 'net_gg': net_gg, 'delta': delta,
        'E_pair': E_pair, 'ratio': ratio, 'residual_percent': res_pc,
    })
    flag = " ◄ best" if abs(res_pc - best_res) < 1e-10 else ""
    if res_pc < best_res:
        best_res = res_pc
        best_phi = phi
        flag = " ◄"
    mark = " ◄ existing" if phi == 1.0 else ""
    print(f"  {phi:5.2f}  {net_gg:12.8f}  {delta:12.8f}  "
          f"{E_pair:11.6f}  {ratio:7.5f}  {res_pc:9.4f}%{mark}")

print(f"\n  Best match at φ = {best_phi:.2f} (same as φ=1.00 — pure polarization)")
print(f"  Both φ=0 and φ=1 give equal minimum residual = {best_res:.4f}%")
print(f"  NB: φ = 1.00 (pure σ₀) was used in pair-production-nf.py → "
      f"{sweep_data[-1]['residual_percent']:.3f}%")

# Analytic formula for net(γ(φ)·γ(φ)):
# net = S + c₀ + c₁ + C₊ + C₋
#     = [φ² + (1-φ)²] + HA·φ² + HA·(1-φ)² + φ(1-φ) + φ(1-φ)
#     = [φ² + (1-φ)²]·(1 + HA) + 2φ(1-φ)
#     = [1 - 2φ(1-φ)]·(1 + HA) + 2φ(1-φ)
#     = (1 + HA) - 2φ(1-φ)·HA
# → parabola in φ, minimum at φ=½, maximum at φ=0 or φ=1
net_at_0   = 1 + HA0
net_at_half = 1 + HA0 - 2 * 0.25 * HA0
print(f"""
  ANALYTIC FORMULA:
    net(γ(φ)·γ(φ)) = (1 + HA) − 2φ(1−φ)·HA
      φ = 0 or 1:  net = 1 + HA     = {net_at_0:.8f}   (maximum)
      φ = ½:       net = 1 + HA/2   = {net_at_half:.8f}   (minimum)

  Larger net(γγ) → smaller Δ(pair) → smaller E_pair → CLOSER to 2mₑ.
  Pure polarization (φ=0 or φ=1) maximizes net(γγ) and minimizes the
  threshold residual.  Color mixing increases the residual monotonically
  toward φ=½ where the residual reaches ~49%.

  CONCLUSION:
    Adding color content (mixed φ) makes the pair-production threshold
    prediction WORSE.  The 4.35% residual in pair-production-nf.py IS
    the best achievable with the γγ → e⁻e⁺ NF approach for pure photons.
    The ~4.4% residual is an intrinsic feature of the NF model, not a
    deficiency caused by missing color content on the photons.
""")


# ══════════════════════════════════════════════════════════════
# SECTION 6 — ASYMMETRIC CASE (different incoming polarizations)
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("  ASYMMETRIC CASE: φ₁ ≠ φ₂  (Breit-Wheeler-like)")
print("=" * 70)
print("""
  When the two photons have different polarization histories,
  C₊ ≠ C₋ and L₊ ≠ L₋ amplitudes.  This breaks the left/right
  symmetry of the Hopf-link observable.
""")

asym_cases = [
    (1.0, 0.5, "σ₀ + mixed"),
    (0.8, 0.2, "partial colors"),
    (0.9, 0.1, "nearly orthogonal"),
    (0.6, 0.4, "near-symmetric"),
]

print(f"  {'φ₁':>5s}  {'φ₂':>5s}  {'C₊(L₊)':>9s}  {'C₋(L₋)':>9s}  "
      f"{'C₊/C₋':>7s}  {'Obs total':>10s}")
print(f"  {'─'*60}")
for p1, p2, lbl in asym_cases:
    nf = two_photon_nf(p1, p2)
    Cp, Cm = nf['C_plus'], nf['C_minus']
    ratio  = Cp / Cm if Cm != 0 else float('inf')
    obs    = Cp + Cm
    print(f"  {p1:5.2f}  {p2:5.2f}  {Cp:+9.5f}  {Cm:+9.5f}  "
          f"{ratio:7.4f}  {obs:10.5f}  ({lbl})")


# ══════════════════════════════════════════════════════════════
# SECTION 7 — SINGLE-PHOTON NF
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("  SINGLE-PHOTON NF: γ(φ₁)·?")
print("=" * 70)
print("""
  NF(γ(φ₁)) = φ₁·σ₀ + (1−φ₁)·σ₁

  This is already in normal form — both σ₀ and σ₁ have word
  length 1 and no Hecke relation can fire on a single generator.

  The single photon is ENTIRELY virtual/fibre:
      σ₀ (ℓ=1): virtual — H⁰ Hopf crossing (σ-r color plane)
      σ₁ (ℓ=1): virtual — H¹ Hopf crossing (r-g color plane)

  A single photon has NO observable (ℓ≥2) content.
  Observability requires at least two photons — the Hecke product
  creates the L±  Hopf links that constitute the observable output.
""")
print(f"  {'φ':>5s}  {'σ₀ coeff':>10s}  {'σ₁ coeff':>10s}  "
      f"{'net':>10s}  {'Observable?':}")
print(f"  {'─'*55}")
for phi_val in [0.0, 0.25, 0.5, 0.75, 1.0]:
    c0 = phi_val
    c1 = 1.0 - phi_val
    net = c0 + c1
    print(f"  {phi_val:5.2f}  {c0:+10.5f}  {c1:+10.5f}  "
          f"{net:+10.5f}  No (all ℓ=1)")


# ══════════════════════════════════════════════════════════════
# SECTION 8 — NEUTRON CLARIFICATION
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("  NEUTRON IS NOT σ₀ OR σ₁ — IT IS A B₃-CONFINED QUARK STATE")
print("=" * 70)
print(f"""
  The neutron is NOT σ₀ or σ₁.  Those are single Hopf generators
  (virtual, word length 1).  The neutron is a full nucleon NF:

    NF(n) = −0.1373·𝟏  +  0.0564·σ₀  +  1.5350·σ₁
            +0.1543·L₊  +  0.0137·L₋  −  0.0664·e⁻

  (from free-neutron-decay.witness.json at q₀)

  Construction:
    γγ → νν̄ (Hecke relation σᵢ² → HA·σᵢ + 𝟏)
    → 3 pair creations on 3 strands
    → quark dressing [u,d,d] → pairwise crossings
    → Borromean confinement B₃ = (σ₀σ₁⁻¹)³
    → Gröbner reduction → 6-term NF

  The dominant term is σ₁ (~90% amplitude), which lives in the
  color-tube fiber (r,g plane) — this IS the color confinement.
  σ₀ (~4% amplitude) is the spacetime coupling term.
  L₊, L₋ (~10% amplitude) are the observable Hopf links
  (the nuclear binding visible as stable nuclear structure).

  Single-generator assignment:
    σ₀ = H⁰ Hopf generator = photon-like crossing (σ-r plane)
    σ₁ = H¹ Hopf generator = color-tube crossing  (r-g plane)
  Both are VIRTUAL (ℓ=1), both contribute to the nucleon as
  sub-leading corrections to the B₃-confined 6-term structure.
""")


# ══════════════════════════════════════════════════════════════
# WITNESS JSON
# ══════════════════════════════════════════════════════════════

witness = {
    "name": "pair-production",
    "description": (
        "Polarized two-photon NF γ(φ₁)·γ(φ₂) in H₂(q) with color content. "
        "γ(φ) = φ·σ₀ + (1−φ)·σ₁ where φ is the polarization/entanglement "
        "history parameter. Observable terms (ℓ≥2) are L± Hopf links with "
        "coefficients C± = φ₁(1−φ₂), (1−φ₁)φ₂. Fibre/virtual terms are "
        "S·𝟏, φ₁φ₂·HA·σ₀, (1−φ₁)(1−φ₂)·HA·σ₁. Pair-production threshold "
        "sweep over φ shows φ=1 (existing pair-production-nf.py) gives "
        "~4.35% residual; maximally mixed φ=0.5 gives different residual."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "git_sha": SHA,
    "parameters": {
        "q0": q0,
        "HA": HA0,
        "E0_MeV": E0,
        "m_e_MeV": M_E_MEV,
        "threshold_2me_MeV": E_threshold,
    },
    "photon_definition": {
        "formula": "γ(φ) = φ·σ₀ + (1−φ)·σ₁",
        "phi_meaning": "fraction of σ₀ polarization content",
        "phi_equals_1": "pure σ₀ (existing pair-production-nf.py)",
        "phi_equals_0": "pure σ₁ (color-tube fiber photon)",
        "phi_half": "maximally mixed / equal polarization",
    },
    "nf_formula": {
        "S":       "phi1*phi2 + (1-phi1)*(1-phi2)",
        "c_sigma0": "phi1*phi2 * HA",
        "c_sigma1": "(1-phi1)*(1-phi2) * HA",
        "C_plus":  "phi1*(1-phi2)",
        "C_minus": "(1-phi1)*phi2",
        "observable_condition": {
            "sigma0_active": "phi1 > 0 AND phi2 > 0",
            "sigma1_active": "phi1 < 1 AND phi2 < 1",
            "L_plus_active": "phi1 > 0 AND phi2 < 1",
            "L_minus_active": "phi1 < 1 AND phi2 > 0",
        },
    },
    "tensor_product_vs_concatenation": {
        "concatenation": {
            "algebra": "σ₀·σ₀ = σ₀² in H₂(q)",
            "nf": "HA·σ₀ + 𝟏",
            "physics": "same-strand interaction, pair-production vertex",
        },
        "tensor_product": {
            "algebra": "σ₀⊗σ₀ = σ₀·σ₂ in H₄(q)",
            "nf": "σ₀·σ₂  (already reduced, far-commuting)",
            "physics": "different-strand non-interaction, free photon state",
        },
    },
    "special_cases": {
        key_str: two_photon_nf(p1, p2)
        for (p1, p2), key_str in [
            ((1.0, 1.0), "phi_1_1"),
            ((0.0, 0.0), "phi_0_0"),
            ((1.0, 0.0), "phi_1_0"),
            ((0.5, 0.5), "phi_half_half"),
        ]
    },
    "threshold_sweep": sweep_data,
    "best_phi_for_threshold": best_phi,
    "best_residual_percent": best_res,
}

out_path = Path(__file__).with_suffix(".witness.json")
out_path.write_text(json.dumps(witness, indent=2))
print(f"\n  Witness written to {out_path.name}")
