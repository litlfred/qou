#!/usr/bin/env python3
"""
Pair production: NF(γ₁ · γ₂) with 3-term polarized photon model.

From §2.25 Knot basis for H*(Σ₄):

    H⁰ = point (trivial knot) = γ (photon)   ← the identity 𝟙 in H*(Σ₄)

A photon with color content (polarization) is:

    γ₁ = 𝟙 + φ₀·σ₀ + φ₁·σ₁   ∈ H₃(q)    (first photon)
    γ₂ = 𝟙 + ψ₀·σ₀ + ψ₁·σ₁   ∈ H₃(q)    (second photon)

The identity (𝟙) IS the photon; σ₀ and σ₁ are its color dressing.
γ̃ ("tilde") is just a second photon with its own color content,
NOT a conjugate.

───────────────────────────────────────────────────────────────────
KNOT-PARTICLE TABLE (§2.25):

  H⁰   → 𝟙  (point, trivial knot)     = γ (photon)
  H²   → τ(1,0) (unknot)               = ν (neutrino)
  H¹·⁰ → τ(2,3) (trefoil)             = e⁻/e⁺; on divisor: u/d
  H¹·⁰ → τ(2,5) (cinquefoil)          = μ; on divisor: gen-2 quarks
  H¹·⁰ → τ(2,7) (septafoil)           = τ-lepton; gen-3 quarks
  H¹·⁰ → τ(3,5)                        = Weak force (β-decay vertex)
  H⁰·¹ → τ(2,9) = τ(2,3²)             = Strong binding (gluon)
  H⁰·¹ → τ(3,4) = τ(3,2²)             = Hopf² binding (color)
  H⁰·¹ → 4₁ (figure-eight)             = Higgs boson (mass mechanism)

───────────────────────────────────────────────────────────────────
MAIN RESULT:

  NF(γ₁ · γ₂) = NF[(𝟙 + φ₀σ₀ + φ₁σ₁) · (𝟙 + ψ₀σ₀ + ψ₁σ₁)]

  Expanding all 9 terms and applying Hecke σᵢ² = HA·σᵢ + 𝟙:

  ┌────────────────────────────────────────────────────────────────┐
  │  NF(γ₁·γ₂) = (1 + φ₀ψ₀ + φ₁ψ₁)·𝟙                          │
  │             + (φ₀ + ψ₀ + φ₀ψ₀·HA)·σ₀                        │
  │             + (φ₁ + ψ₁ + φ₁ψ₁·HA)·σ₁                        │
  │             + φ₀ψ₁·L₊                                         │
  │             + φ₁ψ₀·L₋                                         │
  └────────────────────────────────────────────────────────────────┘

  The L± Hopf links are the cross-color terms: φ₀ψ₁ and φ₁ψ₀.
  These are OBSERVABLE (ℓ=2).  They arise from color MIXING
  between the two photons — one photon's σ₀ meets the other's σ₁.

Usage:
    python3 pair-production.py
"""

import math, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401

q_sym = sp.Symbol('q', positive=True)

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
    ():        ("ν",  "𝟏",      "unknot (0₁)"),
    (0,):      ("σ₀", "σ₀",     "virtual (ℓ=1)"),
    (1,):      ("σ₁", "σ₁",     "virtual (ℓ=1)"),
    (0, 1):    ("L₊", "σ₀σ₁",   "Hopf link"),
    (1, 0):    ("L₋", "σ₁σ₀",   "Hopf link"),
    (0, 1, 0): ("e⁻", "σ₀σ₁σ₀", "trefoil (3₁)"),
}
OBSERVABLE_WORDS = {w for w in PARTICLE_KNOT if len(w) >= 2}

def ws(w):
    if not w:
        return "𝟏"
    return "·".join(f"σ_{i}" for i in w)

def pn(w):
    return PARTICLE_KNOT.get(w, ("?", "?", "?"))[0]

def eval_q0(c):
    if isinstance(c, (int, float)):
        return float(c)
    return float(sp.sympify(c).subs(q_sym, q0))


# ══════════════════════════════════════════════════════════════
# SECTION 1 — THREE-TERM PHOTON MODEL
# ══════════════════════════════════════════════════════════════

print("=" * 72)
print("  THREE-TERM PHOTON:  γ = 𝟙 + φ₀·σ₀ + φ₁·σ₁")
print("=" * 72)
print("""
  From §2.25:  H⁰ = trivial knot = photon γ.
  The identity 𝟙 IS the photon in H*(Σ₄).

  Color content (polarization) adds σ₀ and σ₁ dressing:

      γ₁ = 𝟙 + φ₀·σ₀ + φ₁·σ₁       (first photon with color)
      γ₂ = 𝟙 + ψ₀·σ₀ + ψ₁·σ₁       (second photon with color)

  where φ₀, φ₁, ψ₀, ψ₁ ∈ ℝ are independent polarization amplitudes.
  γ̃ is just a second photon — NOT a conjugate.

  Key difference from old model:
      OLD: γ(φ) = φ·σ₀ + (1−φ)·σ₁     (no identity, constrained)
      NEW: γ     = 𝟙 + φ₀·σ₀ + φ₁·σ₁  (identity IS the photon)
""")


# ══════════════════════════════════════════════════════════════
# SECTION 2 — ALGEBRAIC DERIVATION OF NF(γ₁ · γ₂)
# ══════════════════════════════════════════════════════════════

print("=" * 72)
print("  ALGEBRAIC DERIVATION: NF(γ₁ · γ₂)")
print("=" * 72)
print(f"""
  γ₁·γ₂ = (𝟙 + φ₀σ₀ + φ₁σ₁)(𝟙 + ψ₀σ₀ + ψ₁σ₁)

  Expanding all 9 terms:

    𝟙·𝟙          =  𝟙
    𝟙·ψ₀σ₀       =  ψ₀·σ₀
    𝟙·ψ₁σ₁       =  ψ₁·σ₁
    φ₀σ₀·𝟙       =  φ₀·σ₀
    φ₀σ₀·ψ₀σ₀    =  φ₀ψ₀·σ₀²
    φ₀σ₀·ψ₁σ₁    =  φ₀ψ₁·σ₀σ₁       = φ₀ψ₁·L₊
    φ₁σ₁·𝟙       =  φ₁·σ₁
    φ₁σ₁·ψ₀σ₀    =  φ₁ψ₀·σ₁σ₀       = φ₁ψ₀·L₋
    φ₁σ₁·ψ₁σ₁    =  φ₁ψ₁·σ₁²

  Collecting before Hecke reduction:

    𝟙:   1
    σ₀:  φ₀ + ψ₀
    σ₁:  φ₁ + ψ₁
    σ₀²: φ₀ψ₀
    σ₁²: φ₁ψ₁
    L₊:  φ₀ψ₁
    L₋:  φ₁ψ₀

  Apply Hecke relation  σᵢ² = HA·σᵢ + 𝟙  where HA = q − q⁻¹:

    φ₀ψ₀·σ₀²  →  φ₀ψ₀·HA·σ₀ + φ₀ψ₀·𝟙
    φ₁ψ₁·σ₁²  →  φ₁ψ₁·HA·σ₁ + φ₁ψ₁·𝟙

  Final NF:
  ┌────────────────────────────────────────────────────────────────┐
  │  NF(γ₁·γ₂) = (1 + φ₀ψ₀ + φ₁ψ₁)·𝟙                          │
  │             + (φ₀ + ψ₀ + φ₀ψ₀·HA)·σ₀                        │
  │             + (φ₁ + ψ₁ + φ₁ψ₁·HA)·σ₁                        │
  │             + φ₀ψ₁·L₊                                         │
  │             + φ₁ψ₀·L₋                                         │
  └────────────────────────────────────────────────────────────────┘

  Net = (1 + φ₀ψ₀ + φ₁ψ₁)
      + (φ₀ + ψ₀ + φ₀ψ₀·HA)
      + (φ₁ + ψ₁ + φ₁ψ₁·HA)
      + φ₀ψ₁ + φ₁ψ₀

      = 1 + (φ₀ + ψ₀) + (φ₁ + ψ₁)
        + φ₀ψ₀(1 + HA) + φ₁ψ₁(1 + HA) + φ₀ψ₁ + φ₁ψ₀

      = (1 + φ₀ + φ₁)(1 + ψ₀ + ψ₁) + (φ₀ψ₀ + φ₁ψ₁)·HA

  HA = q − q⁻¹ = {HA0:.10f}
""")


# ══════════════════════════════════════════════════════════════
# SECTION 3 — VERIFICATION WITH hecke_symbolic.py
# ══════════════════════════════════════════════════════════════

print("=" * 72)
print("  MACHINE VERIFICATION via hecke_symbolic.py")
print("=" * 72)

from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement,
    q as qs, HA as HA_s
)

div = SymbolicHeckeDivision()

phi0_s = sp.Symbol('phi0', real=True)
phi1_s = sp.Symbol('phi1', real=True)
psi0_s = sp.Symbol('psi0', real=True)
psi1_s = sp.Symbol('psi1', real=True)

# Build γ₁ = 𝟙 + φ₀·σ₀ + φ₁·σ₁
gamma1 = SymbolicHeckeElement({
    (): sp.Integer(1),
    (0,): phi0_s,
    (1,): phi1_s,
})

# Build γ₂ = 𝟙 + ψ₀·σ₀ + ψ₁·σ₁
gamma2 = SymbolicHeckeElement({
    (): sp.Integer(1),
    (0,): psi0_s,
    (1,): psi1_s,
})

# Multiply γ₁ · γ₂ (unreduced)
product = gamma1 * gamma2

print(f"\n  γ₁ = 𝟙 + φ₀·σ₀ + φ₁·σ₁")
print(f"  γ₂ = 𝟙 + ψ₀·σ₀ + ψ₁·σ₁")
print(f"\n  Unreduced product γ₁·γ₂  ({len(product.terms)} terms):")
for w in sorted(product.terms, key=lambda w: (len(w), w)):
    c = sp.expand(product.terms[w])
    print(f"    {c}  ·  {ws(w)}")

# Gröbner--Shirshov-reduce
reduced, stats = div.reduce(product)
print(f"\n  After Gröbner--Shirshov reduction ({stats}):")
print(f"  NF(γ₁·γ₂)  ({len(reduced.terms)} terms):")
for w in sorted(reduced.terms, key=lambda w: (len(w), w)):
    c = sp.expand(reduced.terms[w])
    print(f"    {c}  ·  {ws(w)}   [{pn(w)}]")

# Verify symbolic match with hand derivation
print(f"\n  ── Symbolic coefficient verification ──")
expected = {
    ():     1 + phi0_s * psi0_s + phi1_s * psi1_s,
    (0,):   phi0_s + psi0_s + phi0_s * psi0_s * HA_s,
    (1,):   phi1_s + psi1_s + phi1_s * psi1_s * HA_s,
    (0, 1): phi0_s * psi1_s,
    (1, 0): phi1_s * psi0_s,
}
all_match = True
for w, exp_c in expected.items():
    got_c = reduced.terms.get(w, sp.Integer(0))
    diff = sp.expand(got_c - exp_c)
    match = diff == 0
    all_match = all_match and match
    sym = "✓" if match else "✗"
    print(f"    {ws(w):8s}: expected {sp.expand(exp_c)},  got {sp.expand(got_c)}  {sym}")

print(f"\n  All coefficients match hand derivation: {'YES ✓' if all_match else 'NO ✗'}")


# ══════════════════════════════════════════════════════════════
# SECTION 4 — NUMERICAL EVALUATION AT q₀
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  NUMERICAL NF(γ₁·γ₂) AT q₀")
print("=" * 72)
print(f"\n  q₀  = {q0:.10f}")
print(f"  HA  = q−q⁻¹ = {HA0:.10f}")
print(f"  E₀  = {E0:.6f} MeV")
print(f"  mₑ  = {M_E_MEV:.6f} MeV")
print(f"  2mₑ = {2*M_E_MEV:.6f} MeV  (pair threshold)\n")

def pair_nf(phi0_val, phi1_val, psi0_val, psi1_val):
    """Compute NF(γ₁·γ₂) coefficients at q₀."""
    c_id = 1 + phi0_val * psi0_val + phi1_val * psi1_val
    c_s0 = phi0_val + psi0_val + phi0_val * psi0_val * HA0
    c_s1 = phi1_val + psi1_val + phi1_val * psi1_val * HA0
    c_Lp = phi0_val * psi1_val
    c_Lm = phi1_val * psi0_val
    net  = c_id + c_s0 + c_s1 + c_Lp + c_Lm
    return dict(
        c_identity=c_id, c_sigma0=c_s0, c_sigma1=c_s1,
        C_plus=c_Lp, C_minus=c_Lm, net=net,
    )

def print_pair_table(phi0_val, phi1_val, psi0_val, psi1_val, label):
    nf = pair_nf(phi0_val, phi1_val, psi0_val, psi1_val)
    print(f"  ── {label} ──")
    print(f"     γ₁ = 𝟙 + {phi0_val}·σ₀ + {phi1_val}·σ₁")
    print(f"     γ₂ = 𝟙 + {psi0_val}·σ₀ + {psi1_val}·σ₁")
    print(f"  {'Term':6s}  {'Coefficient':>14s}  {'Observable?':12s}  {'Physical':}")
    print(f"  {'─'*64}")
    print(f"  {'𝟏':6s}  {nf['c_identity']:+14.8f}  {'No (ℓ=0)':12s}  vacuum/neutrino")
    print(f"  {'σ₀':6s}  {nf['c_sigma0']:+14.8f}  {'No (ℓ=1)':12s}  σ₀ virtual dressing")
    print(f"  {'σ₁':6s}  {nf['c_sigma1']:+14.8f}  {'No (ℓ=1)':12s}  σ₁ color-tube fiber")
    print(f"  {'L₊':6s}  {nf['C_plus']:+14.8f}  {'YES (ℓ=2)':12s}  Hopf link (cross-color)")
    print(f"  {'L₋':6s}  {nf['C_minus']:+14.8f}  {'YES (ℓ=2)':12s}  Hopf link (cross-color)")
    print(f"  {'─'*64}")
    print(f"  {'net':6s}  {nf['net']:+14.8f}")
    obs = abs(nf['C_plus']) + abs(nf['C_minus'])
    if abs(nf['net']) > 1e-15:
        print(f"  |Observable| fraction (|L±|/|net|):  {obs/abs(nf['net'])*100:.2f}%")
    print()
    return nf

# ── Same-color cases (φ = ψ): both photons have identical color ──
print("  ═══ SAME COLOR ON BOTH PHOTONS (φ = ψ) ═══\n")
same_cases = [
    (0.0, 0.0, 0.0, 0.0, "bare: γ₁ = γ₂ = 𝟙 (no color)"),
    (1.0, 0.0, 1.0, 0.0, "pure σ₀: φ₀=ψ₀=1"),
    (0.0, 1.0, 0.0, 1.0, "pure σ₁: φ₁=ψ₁=1"),
    (1.0, 1.0, 1.0, 1.0, "full color: φ₀=φ₁=ψ₀=ψ₁=1"),
    (0.5, 0.5, 0.5, 0.5, "half color: all = ½"),
    (0.3, 0.3, 0.3, 0.3, "mild color: all = 0.3"),
]

all_nf_results = {}
for p0, p1, q0v, q1v, lbl in same_cases:
    nf = print_pair_table(p0, p1, q0v, q1v, lbl)
    all_nf_results[(p0, p1, q0v, q1v)] = nf

# ── Cross-color cases (φ ≠ ψ) ──
print("  ═══ CROSS-COLOR (φ ≠ ψ) ═══\n")
cross_cases = [
    (1.0, 0.0, 0.0, 1.0, "orthogonal: γ₁ has σ₀, γ₂ has σ₁"),
    (0.0, 1.0, 1.0, 0.0, "orthogonal: γ₁ has σ₁, γ₂ has σ₀"),
    (1.0, 0.5, 0.5, 1.0, "asymmetric cross-color"),
    (0.7, 0.3, 0.3, 0.7, "rotated cross-color"),
    (1.0, 1.0, 0.0, 0.0, "one colored, one bare"),
]

for p0, p1, q0v, q1v, lbl in cross_cases:
    nf = print_pair_table(p0, p1, q0v, q1v, lbl)
    all_nf_results[(p0, p1, q0v, q1v)] = nf


# ══════════════════════════════════════════════════════════════
# SECTION 5 — OBSERVABLE L± CONTENT: CROSS-COLOR MIXING
# ══════════════════════════════════════════════════════════════

print("=" * 72)
print("  OBSERVABLE CONTENT: L₊ = φ₀ψ₁, L₋ = φ₁ψ₀ (cross-color)")
print("=" * 72)
print(f"""
  The observable (pair-produced) content is:

    C(L₊) = φ₀·ψ₁     (σ₀ of γ₁ meets σ₁ of γ₂)
    C(L₋) = φ₁·ψ₀     (σ₁ of γ₁ meets σ₀ of γ₂)

  Key: L± requires CROSS-COLOR mixing between the two photons.
  If both photons have only σ₀ color (φ₁=ψ₁=0), then L₊=L₋=0.
  The σ₀²→HA·σ₀+𝟙 self-energy is entirely virtual (ℓ=1 and ℓ=0).

  For observable pair production:
    L₊ > 0 requires: φ₀ > 0 AND ψ₁ > 0
    L₋ > 0 requires: φ₁ > 0 AND ψ₀ > 0

  Maximum L₊ + L₋ for same-color photons (φ=ψ, φ₀=φ₁):
    L₊ + L₋ = 2φ₀φ₁     (maximized at φ₀ = φ₁)

  Orthogonal photons (φ₀=1,φ₁=0; ψ₀=0,ψ₁=1):
    L₊ = 1·1 = 1,  L₋ = 0·0 = 0    (pure asymmetric pair)
""")

print(f"  {'φ₀':>4s} {'φ₁':>4s} {'ψ₀':>4s} {'ψ₁':>4s}  "
      f"{'L₊':>8s}  {'L₋':>8s}  {'|L±|':>8s}  {'𝟙':>8s}  {'net':>10s}")
print(f"  {'─'*70}")

sweep_data = []
sweep_configs = [
    # same-color sweep
    (0.0, 0.0, 0.0, 0.0),
    (0.2, 0.2, 0.2, 0.2),
    (0.4, 0.4, 0.4, 0.4),
    (0.5, 0.5, 0.5, 0.5),
    (0.6, 0.6, 0.6, 0.6),
    (0.8, 0.8, 0.8, 0.8),
    (1.0, 1.0, 1.0, 1.0),
    # orthogonal
    (1.0, 0.0, 0.0, 1.0),
    (0.0, 1.0, 1.0, 0.0),
    # mixed
    (0.5, 0.5, 1.0, 0.0),
    (1.0, 0.0, 0.5, 0.5),
]

for p0, p1, q0v, q1v in sweep_configs:
    nf = pair_nf(p0, p1, q0v, q1v)
    obs = abs(nf['C_plus']) + abs(nf['C_minus'])
    sweep_data.append({
        'phi0': p0, 'phi1': p1, 'psi0': q0v, 'psi1': q1v,
        'c_identity': nf['c_identity'],
        'c_sigma0': nf['c_sigma0'], 'c_sigma1': nf['c_sigma1'],
        'C_plus': nf['C_plus'], 'C_minus': nf['C_minus'],
        'net': nf['net'], 'obs_total': obs,
    })
    print(f"  {p0:4.1f} {p1:4.1f} {q0v:4.1f} {q1v:4.1f}  "
          f"{nf['C_plus']:+8.4f}  {nf['C_minus']:+8.4f}  "
          f"{obs:8.4f}  {nf['c_identity']:+8.4f}  {nf['net']:+10.6f}")


# ══════════════════════════════════════════════════════════════
# SECTION 6 — PAIR PRODUCTION ENERGY BUDGET
# ══════════════════════════════════════════════════════════════

_pp_path = Path(__file__).parent / "pair-production-nf.witness.json"
with _pp_path.open() as _f:
    _pp = json.load(_f)
net_eminus  = _pp["energy_budget"]["net_eminus"]
net_eplus   = _pp["energy_budget"]["net_eplus"]
E_threshold = _pp["parameters"]["threshold_MeV"]

print("\n" + "=" * 72)
print("  PAIR PRODUCTION ENERGY: γ₁·γ₂ → e⁻e⁺")
print("=" * 72)
print(f"""
  E₀           = {E0:.6f} MeV
  NF_net(e⁻)   = {net_eminus:.8f}
  NF_net(e⁺)   = {net_eplus:.8f}
  Sum e⁻+e⁺    = {net_eminus + net_eplus:.8f}
  Observed 2mₑ = {E_threshold:.6f} MeV

  Energy budget:
    Δ(pair) = NF_net(e⁻) + NF_net(e⁺) − NF_net(γ₁·γ₂)
    E_pair  = Δ(pair) × E₀
""")

print(f"  {'φ₀':>4s} {'φ₁':>4s} {'ψ₀':>4s} {'ψ₁':>4s}  "
      f"{'net(γγ)':>12s}  {'Δ(pair)':>10s}  "
      f"{'E_pair':>10s}  {'Residual%':>10s}")
print(f"  {'─'*70}")

energy_sweep = []
for p0, p1, q0v, q1v in sweep_configs:
    nf = pair_nf(p0, p1, q0v, q1v)
    net_gg = nf['net']
    delta = net_eminus + net_eplus - net_gg
    E_pair = delta * E0
    res_pc = abs(E_pair - E_threshold) / E_threshold * 100 if E_threshold > 0 else 0
    energy_sweep.append({
        'phi0': p0, 'phi1': p1, 'psi0': q0v, 'psi1': q1v,
        'net_gg': net_gg, 'delta': delta,
        'E_pair': E_pair, 'residual_percent': res_pc,
    })
    print(f"  {p0:4.1f} {p1:4.1f} {q0v:4.1f} {q1v:4.1f}  "
          f"{net_gg:+12.6f}  {delta:+10.6f}  "
          f"{E_pair:10.4f}  {res_pc:9.4f}%")


# ══════════════════════════════════════════════════════════════
# SECTION 7 — FACTORED NET FORMULA
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  ALGEBRAIC STRUCTURE")
print("=" * 72)
print(f"""
  Define the "color norms":
    N₁ = 1 + φ₀ + φ₁    (total weight of γ₁)
    N₂ = 1 + ψ₀ + ψ₁    (total weight of γ₂)

  And the "Hecke self-energy":
    H_self = (φ₀ψ₀ + φ₁ψ₁)·HA    (from σᵢ² → HA·σᵢ + 𝟙)

  Then:
    net(γ₁·γ₂) = N₁·N₂ + H_self
               = (1+φ₀+φ₁)(1+ψ₀+ψ₁) + (φ₀ψ₀+φ₁ψ₁)·HA

  The product N₁·N₂ is the "classical" part (if σᵢ were numbers).
  The Hecke correction H_self is from quantum self-interaction σᵢ².

  For identical photons (φ=ψ):
    net = (1+φ₀+φ₁)² + (φ₀²+φ₁²)·HA
""")

# Numerical verification
print(f"  Numerical verification at q₀:")
test_configs = [
    (0.0, 0.0, 0.0, 0.0),
    (0.5, 0.5, 0.5, 0.5),
    (1.0, 1.0, 1.0, 1.0),
    (1.0, 0.0, 0.0, 1.0),
    (0.3, 0.7, 0.7, 0.3),
]
for p0, p1, q0v, q1v in test_configs:
    N1 = 1 + p0 + p1
    N2 = 1 + q0v + q1v
    H_self = (p0 * q0v + p1 * q1v) * HA0
    net_formula = N1 * N2 + H_self
    net_direct = pair_nf(p0, p1, q0v, q1v)['net']
    match = abs(net_formula - net_direct) < 1e-12
    print(f"    φ=({p0},{p1}), ψ=({q0v},{q1v}): "
          f"N₁N₂+H = {net_formula:+.8f}, direct = {net_direct:+.8f}  "
          f"{'✓' if match else '✗'}")


# ══════════════════════════════════════════════════════════════
# SECTION 8 — COMPARISON WITH OLD MODEL
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  COMPARISON: NEW (3-TERM) vs OLD (2-TERM) PHOTON MODEL")
print("=" * 72)
print(f"""
  OLD model:  γ(φ) = φ·σ₀ + (1−φ)·σ₁
    • No identity component — photon IS a crossing
    • Two photon product → difference of squares structure

  NEW model:  γ = 𝟙 + φ₀·σ₀ + φ₁·σ₁
    • Identity 𝟙 IS the photon (matching §2.25: H⁰ = point = γ)
    • Color content is additive dressing on top of identity
    • Two photon product → SUM structure:
        (𝟙 + X₁)(𝟙 + X₂) = 𝟙 + X₁ + X₂ + X₁X₂

  The new model correctly captures:
    1. Bare photon (all φ,ψ=0): γ₁·γ₂ = 𝟙 (vacuum, no pair production)
    2. L₊ = φ₀ψ₁: one photon's σ₀ crossing the other's σ₁ → OBSERVABLE
    3. L₋ = φ₁ψ₀: reverse cross-color → OBSERVABLE
    4. Same-color self-energy φ₀ψ₀·σ₀² → HA·σ₀ + 𝟙 is virtual
    5. net always ≥ 1 (photon identity persists as vacuum floor)
""")


# ══════════════════════════════════════════════════════════════
# WITNESS JSON
# ══════════════════════════════════════════════════════════════

witness = {
    "name": "pair-production",
    "description": (
        "Three-term polarized photon pair production: "
        "γ₁ = 𝟙 + φ₀·σ₀ + φ₁·σ₁, γ₂ = 𝟙 + ψ₀·σ₀ + ψ₁·σ₁. "
        "NF(γ₁·γ₂) = (1+φ₀ψ₀+φ₁ψ₁)·𝟙 + (φ₀+ψ₀+φ₀ψ₀·HA)·σ₀ "
        "+ (φ₁+ψ₁+φ₁ψ₁·HA)·σ₁ + φ₀ψ₁·L₊ + φ₁ψ₀·L₋. "
        "Observable L± Hopf links are cross-color terms. "
        "Net = (1+φ₀+φ₁)(1+ψ₀+ψ₁) + (φ₀ψ₀+φ₁ψ₁)·HA."
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
        "formula_gamma1": "γ₁ = 𝟙 + φ₀·σ₀ + φ₁·σ₁",
        "formula_gamma2": "γ₂ = 𝟙 + ψ₀·σ₀ + ψ₁·σ₁",
        "identity_is_photon": "𝟙 = H⁰ = trivial knot = photon (§2.25)",
        "color_content": "φᵢ·σᵢ and ψᵢ·σᵢ are independent polarization dressing",
        "tilde_meaning": "γ̃ is just a second photon, not a conjugate",
    },
    "nf_formula": {
        "c_identity": "1 + φ₀ψ₀ + φ₁ψ₁",
        "c_sigma0": "φ₀ + ψ₀ + φ₀ψ₀·HA",
        "c_sigma1": "φ₁ + ψ₁ + φ₁ψ₁·HA",
        "C_plus": "φ₀·ψ₁ (cross-color: σ₀ of γ₁ meets σ₁ of γ₂)",
        "C_minus": "φ₁·ψ₀ (cross-color: σ₁ of γ₁ meets σ₀ of γ₂)",
        "net": "(1+φ₀+φ₁)(1+ψ₀+ψ₁) + (φ₀ψ₀+φ₁ψ₁)·HA",
    },
    "observability": {
        "L_plus": "observable (ℓ=2), coefficient φ₀ψ₁",
        "L_minus": "observable (ℓ=2), coefficient φ₁ψ₀",
        "sigma_terms": "virtual (ℓ=1), fibre-confined",
        "identity": "vacuum/neutrino channel (ℓ=0)",
        "pair_production_requires": "cross-color mixing between the two photons",
    },
    "symbolic_verification": all_match,
    "special_cases": {
        f"phi({p0},{p1})_psi({q0v},{q1v})": pair_nf(p0, p1, q0v, q1v)
        for p0, p1, q0v, q1v in [
            (0.0, 0.0, 0.0, 0.0),
            (1.0, 0.0, 1.0, 0.0),
            (0.0, 1.0, 0.0, 1.0),
            (1.0, 1.0, 1.0, 1.0),
            (1.0, 0.0, 0.0, 1.0),
            (0.5, 0.5, 0.5, 0.5),
        ]
    },
    "sweep_data": sweep_data,
    "energy_sweep": energy_sweep,
}

out_path = Path(__file__).with_suffix(".witness.json")
out_path.write_text(json.dumps(witness, indent=2))
print(f"\n  Witness written to {out_path.name}")
