#!/usr/bin/env python3
"""
Colored photon pair production: energy alignment at q₀.

Starting from the remark rem:knot-basis-color-content, we treat
each photon as γ = 𝟙 + φ₀·σ₀ + φ₁·σ₁ with INDEPENDENT formal
color weights φ₀, φ₁, ψ₀, ψ₁ ∈ R.

This script:
  1. Derives the NF(γ₁·γ₂) symbolically with all 4 weights independent
  2. Computes the energy budget:  E_pair = Δ(pair) × E₀
     where Δ(pair) is the net coefficient change from γγ → e⁻e⁺
  3. Solves for which color weights make E_pair = 2mₑ exactly at q₀
  4. Verifies the algebra with hecke_symbolic.py

Usage:
    python3 colored-pair-energy-alignment.py
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

# Load E₀ from beta-decay-energy-scale witness
_esc_path = Path(__file__).parent / "beta-decay-energy-scale.witness.json"
with _esc_path.open() as _f:
    _esc = json.load(_f)
E0 = _esc["energy_scales"]["E0_from_net_MeV"]

# Load e⁻/e⁺ NF data
_pp_path = Path(__file__).parent / "pair-production-nf.witness.json"
with _pp_path.open() as _f:
    _pp = json.load(_f)
net_eminus = _pp["energy_budget"]["net_eminus"]
net_eplus  = _pp["energy_budget"]["net_eplus"]
E_threshold = _pp["parameters"]["threshold_MeV"]

print("=" * 72)
print("  COLORED PHOTON PAIR PRODUCTION — ENERGY ALIGNMENT AT q₀")
print("=" * 72)
print(f"""
  Parameters:
    q₀      = {q0:.10f}
    HA      = q − q⁻¹ = {HA0:.10f}
    E₀      = {E0:.6f} MeV
    mₑ      = {M_E_MEV:.6f} MeV
    2mₑ     = {2*M_E_MEV:.6f} MeV (pair threshold)
    net(e⁻) = {net_eminus:.8f}
    net(e⁺) = {net_eplus:.8f}
""")

# ══════════════════════════════════════════════════════════════
# SECTION 1 — SYMBOLIC NF WITH FORMAL VARIABLES
# ══════════════════════════════════════════════════════════════

phi0 = sp.Symbol('phi0', real=True)
phi1 = sp.Symbol('phi1', real=True)
psi0 = sp.Symbol('psi0', real=True)
psi1 = sp.Symbol('psi1', real=True)
h = sp.Symbol('h', positive=True)  # h = q - q⁻¹

# NF coefficients from the remark derivation
c_id = 1 + phi0*psi0 + phi1*psi1
c_s0 = phi0 + psi0 + phi0*psi0*h
c_s1 = phi1 + psi1 + phi1*psi1*h
c_Lp = phi0*psi1
c_Lm = phi1*psi0

# Net
net_gg = sp.expand(c_id + c_s0 + c_s1 + c_Lp + c_Lm)
net_factored = sp.expand((1+phi0+phi1)*(1+psi0+psi1) + (phi0*psi0+phi1*psi1)*h)

# Verify factored form
assert sp.expand(net_gg - net_factored) == 0, "Net formula mismatch!"
print("  ✓ NF formula verified symbolically (net = N₁·N₂ + H_self)")

# ══════════════════════════════════════════════════════════════
# SECTION 2 — MACHINE VERIFICATION
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  MACHINE VERIFICATION via hecke_symbolic.py")
print("=" * 72)

from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement,
    q as qs, HA as HA_s
)

div = SymbolicHeckeDivision()

gamma1 = SymbolicHeckeElement({
    (): sp.Integer(1),
    (0,): phi0,
    (1,): phi1,
})

gamma2 = SymbolicHeckeElement({
    (): sp.Integer(1),
    (0,): psi0,
    (1,): psi1,
})

product = gamma1 * gamma2
reduced, stats = div.reduce(product)

print(f"\n  NF(γ₁·γ₂) reduced ({stats}):")
expected = {
    ():     1 + phi0*psi0 + phi1*psi1,
    (0,):   phi0 + psi0 + phi0*psi0*HA_s,
    (1,):   phi1 + psi1 + phi1*psi1*HA_s,
    (0, 1): phi0*psi1,
    (1, 0): phi1*psi0,
}
all_match = True
for w, exp_c in expected.items():
    got_c = reduced.terms.get(w, sp.Integer(0))
    diff = sp.expand(got_c - exp_c)
    match = diff == 0
    all_match = all_match and match
    sym = "✓" if match else "✗"
    wlbl = "𝟏" if not w else "·".join(f"σ_{i}" for i in w)
    print(f"    {wlbl:10s}: {sym}")

print(f"\n  All coefficients match: {'YES ✓' if all_match else 'NO ✗'}")

# ══════════════════════════════════════════════════════════════
# SECTION 3 — ENERGY BUDGET: SOLVE FOR COLOR WEIGHTS
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  ENERGY BUDGET: γ₁·γ₂ → e⁻e⁺")
print("=" * 72)

# Energy balance:
#   E_pair = [net(e⁻) + net(e⁺) - net(γ₁·γ₂)] × E₀
#   Target: E_pair = 2mₑ
#
# Therefore:
#   net(γ₁·γ₂) = net(e⁻) + net(e⁺) - 2mₑ/E₀

target_delta = 2 * M_E_MEV / E0
net_ee = net_eminus + net_eplus
net_gg_target = net_ee - target_delta

print(f"""
  Energy balance equation:
    E_pair = [net(e⁻) + net(e⁺) − net(γ₁·γ₂)] × E₀ = 2mₑ

  Solving for net(γ₁·γ₂):
    net(γ₁·γ₂) = net(e⁻) + net(e⁺) − 2mₑ/E₀
                = {net_eminus:.8f} + {net_eplus:.8f} − {target_delta:.8f}
                = {net_gg_target:.8f}

  The net formula is:
    net(γ₁·γ₂) = (1+φ₀+φ₁)(1+ψ₀+ψ₁) + (φ₀ψ₀+φ₁ψ₁)·HA
""")

# ── Symmetric case: identical photons, φ=ψ, both colors equal ──
# If φ₀ = φ₁ = ψ₀ = ψ₁ = t:
#   net = (1+2t)² + 2t²·HA
# Solve: (1+2t)² + 2t²·HA = net_gg_target

t = sp.Symbol('t', positive=True)
net_sym = (1 + 2*t)**2 + 2*t**2 * HA0
eqn = sp.Eq(net_sym, net_gg_target)
t_sols = sp.solve(eqn, t)
t_real_positive = [s for s in t_sols if sp.im(s) == 0 and float(s) > 0]

print(f"  ── Symmetric case: φ₀ = φ₁ = ψ₀ = ψ₁ = t ──")
print(f"     (1+2t)² + 2t²·HA = {net_gg_target:.8f}")
if t_real_positive:
    t_val = float(t_real_positive[0])
    print(f"     Solution: t = {t_val:.10f}")
    # Verify
    net_check = (1 + 2*t_val)**2 + 2*t_val**2 * HA0
    print(f"     Verification: net = {net_check:.8f} (target: {net_gg_target:.8f})")
    E_check = (net_ee - net_check) * E0
    print(f"     E_pair = {E_check:.6f} MeV (target: {2*M_E_MEV:.6f} MeV)")
    print(f"     Residual: {abs(E_check - 2*M_E_MEV):.8f} MeV")
else:
    print(f"     No real positive solution — net target may be < 1 (below vacuum)")

# ── General symmetric: φ₀ = ψ₀ = a, φ₁ = ψ₁ = b (2-parameter) ──
a, b = sp.symbols('a b', real=True, positive=True)
net_2param = (1 + a + b)**2 + (a**2 + b**2) * HA0
eqn_2param = sp.Eq(net_2param, net_gg_target)

print(f"\n  ── 2-parameter symmetric: φ₀ = ψ₀ = a, φ₁ = ψ₁ = b ──")
print(f"     (1+a+b)² + (a²+b²)·HA = {net_gg_target:.8f}")
print(f"     This defines a curve in (a,b) space.\n")

# Sample the curve by fixing b and solving for a
print(f"     {'b':>6s}  {'a':>12s}  {'net':>12s}  {'E_pair (MeV)':>12s}  {'L₊ = ab':>10s}  {'L₋ = ba':>10s}")
print(f"     {'─'*70}")

sample_results = []
for b_val in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]:
    net_b = (1 + a + b_val)**2 + (a**2 + b_val**2) * HA0
    a_sols = sp.solve(sp.Eq(net_b, net_gg_target), a)
    a_real_pos = [float(s) for s in a_sols if sp.im(s) == 0 and float(s) > 0]
    if a_real_pos:
        a_val = a_real_pos[0]
        net_v = (1 + a_val + b_val)**2 + (a_val**2 + b_val**2) * HA0
        E_v = (net_ee - net_v) * E0
        Lp = a_val * b_val
        Lm = b_val * a_val  # symmetric: Lp = Lm
        sample_results.append({
            'a': a_val, 'b': b_val, 'net': net_v, 'E_pair': E_v,
            'L_plus': Lp, 'L_minus': Lm
        })
        print(f"     {b_val:6.3f}  {a_val:12.8f}  {net_v:12.8f}  "
              f"{E_v:12.6f}  {Lp:10.6f}  {Lm:10.6f}")

# ══════════════════════════════════════════════════════════════
# SECTION 4 — ORTHOGONAL POLARIZATION: ONE-PARAMETER FAMILY
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  ORTHOGONAL POLARIZATION: φ₀ = ψ₁ = s, φ₁ = ψ₀ = 0")
print("=" * 72)

s = sp.Symbol('s', positive=True)

# γ₁ = 𝟙 + s·σ₀, γ₂ = 𝟙 + s·σ₁
# net = (1+s)(1+s) + 0 = (1+s)²  (no Hecke self-energy: φ₀ψ₀=0, φ₁ψ₁=0)
net_ortho = (1 + s)**2

print(f"""
  Orthogonal photons:  γ₁ = 𝟙 + s·σ₀, γ₂ = 𝟙 + s·σ₁
  
  NF(γ₁·γ₂) = 1·𝟙 + s·σ₀ + s·σ₁ + s²·L₊
  
  net = (1+s)² = 1 + 2s + s²
  L₊ = s², L₋ = 0  (pure asymmetric pair)
  
  No Hecke self-energy: φ₀ψ₀ = 0, φ₁ψ₁ = 0
  
  Solving (1+s)² = {net_gg_target:.8f}:
""")

s_sols = sp.solve(sp.Eq(net_ortho, net_gg_target), s)
s_real_pos = [float(sol) for sol in s_sols if sp.im(sol) == 0 and float(sol) > 0]
if s_real_pos:
    s_val = s_real_pos[0]
    print(f"     s = {s_val:.10f}")
    net_check_ortho = (1 + s_val)**2
    E_check_ortho = (net_ee - net_check_ortho) * E0
    print(f"     net(γ₁·γ₂) = {net_check_ortho:.8f}")
    print(f"     E_pair = {E_check_ortho:.6f} MeV")
    print(f"     2mₑ    = {2*M_E_MEV:.6f} MeV")
    print(f"     Residual: {abs(E_check_ortho - 2*M_E_MEV):.8f} MeV")
    print(f"     L₊ = s² = {s_val**2:.8f} (observable Hopf link content)")
else:
    print(f"     No real positive solution (net target < 1?)")
    if net_gg_target < 1:
        print(f"     Indeed net_target = {net_gg_target:.8f} < 1")
        print(f"     This means E(e⁻+e⁺) > E(γγ) for bare photons,")
        print(f"     but the threshold condition requires net(γγ) < net(ee).")

# ══════════════════════════════════════════════════════════════
# SECTION 5 — ENERGY DEFICIT ANALYSIS
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  ENERGY ANALYSIS: BARE vs COLORED PHOTONS")
print("=" * 72)

# Bare photons: γ₁ = γ₂ = 𝟙, net = 1
# Energy: E_pair(bare) = (net_ee - 1) × E₀
E_bare = (net_ee - 1) * E0

# Required color energy to reach 2mₑ:
# 2mₑ = E_pair = (net_ee - net_gg) × E₀
# net_gg = net_ee - 2mₑ/E₀
# Color contribution = net_gg - 1 (excess over bare)

color_contrib = net_gg_target - 1
color_energy = -color_contrib * E0  # negative because higher net_gg = less pair energy

print(f"""
  Bare photon pair: γ₁ = γ₂ = 𝟙
    net(𝟙·𝟙) = 1.0
    E_pair(bare) = ({net_ee:.6f} − 1.0) × {E0:.4f} = {E_bare:.6f} MeV
    Observed 2mₑ = {2*M_E_MEV:.6f} MeV
    Deficit: {E_bare - 2*M_E_MEV:.6f} MeV

  The bare pair energy ({E_bare:.4f} MeV) is {"above" if E_bare > 2*M_E_MEV else "below"} threshold ({2*M_E_MEV:.4f} MeV).
""")

if E_bare > 2*M_E_MEV:
    print(f"  Bare photon pair already exceeds 2mₑ by {E_bare - 2*M_E_MEV:.6f} MeV.")
    print(f"  Color dressing ABSORBS energy: colored photons have higher net,")
    print(f"  so E_pair = (net_ee − net_gg)×E₀ is SMALLER for colored photons.")
    print(f"  Color weights must be chosen so the excess is exactly absorbed.")
    print(f"  Required net(γγ) = {net_gg_target:.8f}")
    print(f"  Color contribution to net: {color_contrib:+.8f}")
elif E_bare < 2*M_E_MEV:
    print(f"  Bare photon pair is below 2mₑ by {2*M_E_MEV - E_bare:.6f} MeV.")
    print(f"  Color content must supply the deficit.")
    print(f"  Required net(γγ) = {net_gg_target:.8f}")
    if net_gg_target < 1:
        print(f"  BUT net(γγ) < 1 is impossible (identity always present)!")
        print(f"  This means the 3-term photon model requires a DIFFERENT")
        print(f"  energy scale or the pair production process involves")
        print(f"  additional algebra (e.g. Borromean confinement).")

# ══════════════════════════════════════════════════════════════
# SECTION 6 — RATIO ANALYSIS: E_pair / 2mₑ vs color weight
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  RATIO: E_pair(φ) / 2mₑ FOR SYMMETRIC PHOTONS")
print("=" * 72)

print(f"\n  φ₀=φ₁=ψ₀=ψ₁=t,  net = (1+2t)² + 2t²·HA")
print(f"\n  {'t':>6s}  {'net(γγ)':>12s}  {'E_pair (MeV)':>12s}  {'E/2mₑ':>8s}  {'L₊+L₋':>8s}")
print(f"  {'─'*56}")

ratio_data = []
for t_test in [0.0, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.7, 1.0]:
    net_t = (1 + 2*t_test)**2 + 2*t_test**2 * HA0
    E_t = (net_ee - net_t) * E0
    ratio = E_t / (2 * M_E_MEV) if 2*M_E_MEV > 0 else 0
    obs = 2 * t_test**2  # L₊ + L₋ for symmetric case
    ratio_data.append({
        't': t_test, 'net': net_t, 'E_pair': E_t,
        'ratio': ratio, 'obs_content': obs,
    })
    print(f"  {t_test:6.3f}  {net_t:12.6f}  {E_t:+12.6f}  {ratio:8.4f}  {obs:8.4f}")

# ══════════════════════════════════════════════════════════════
# WITNESS
# ══════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════
# P2.5 — SYMBOLIC POLYNOMIAL-IN-q FORM
# ══════════════════════════════════════════════════════════════
#
# The energy alignment above evaluates with HA = q₀ - 1/q₀ as a
# numerical constant, but the NF coefficients are themselves
# polynomials in (q, q⁻¹) once the symbolic h is replaced by
# h(q) = q - 1/q.  Capture the symmetric one-parameter family
# (φ₀ = φ₁ = ψ₀ = ψ₁ = t) — the smallest non-trivial case — as
# polynomials in q for the witness JSON, alongside the symbolic
# NF coefficients with formal color weights.

h_q = q_sym - 1 / q_sym

# Per-coefficient polynomials in q (symbolic colors substituted with the
# symmetric t parameter; t kept symbolic):
t_sym = sp.Symbol('t', positive=True)
sym_subs = {phi0: t_sym, phi1: t_sym, psi0: t_sym, psi1: t_sym, h: h_q}
c_id_q   = sp.simplify(c_id.subs(sym_subs))
c_s0_q   = sp.simplify(c_s0.subs(sym_subs))
c_s1_q   = sp.simplify(c_s1.subs(sym_subs))
c_Lp_q   = sp.simplify(c_Lp.subs(sym_subs))
c_Lm_q   = sp.simplify(c_Lm.subs(sym_subs))
net_q    = sp.simplify(net_factored.subs(sym_subs))

symbolic_q_form = {
    "engine": "sympy",
    "q_symbol": "q (sp.Symbol('q', positive=True))",
    "h_symbol_definition": "h = q - 1/q  (HA = [2]_q in Kashiwara normalisation)",
    "color_parametrization": (
        "symmetric one-parameter family φ₀ = φ₁ = ψ₀ = ψ₁ = t "
        "(smallest non-trivial colored case)"
    ),
    "nf_coefficients_polynomial_q": {
        "c_identity":   str(c_id_q),
        "c_sigma0":     str(c_s0_q),
        "c_sigma1":     str(c_s1_q),
        "C_plus":       str(c_Lp_q),
        "C_minus":      str(c_Lm_q),
        "net":          str(net_q),
    },
    "nf_coefficients_general_symbolic": {
        "c_identity": "1 + φ₀ψ₀ + φ₁ψ₁",
        "c_sigma0":   "φ₀ + ψ₀ + φ₀ψ₀·h",
        "c_sigma1":   "φ₁ + ψ₁ + φ₁ψ₁·h",
        "C_plus":     "φ₀·ψ₁",
        "C_minus":    "φ₁·ψ₀",
        "net":        "(1 + φ₀ + φ₁)(1 + ψ₀ + ψ₁) + (φ₀ψ₀ + φ₁ψ₁)·h",
    },
    "note": (
        "NF(γ₁·γ₂) coefficients in the symmetric symbolic family, "
        "expressed as Laurent polynomials in q ∈ ℚ(q).  The "
        "specialisation h ↦ q₀ - 1/q₀ recovers the numerical HA used "
        "in the energy budget; this section exposes the algebraic "
        "form that lives upstream of the q = q₀ specialisation."
    ),
}

witness = {
    "name": "colored-pair-energy-alignment",
    "description": (
        "Energy alignment analysis for colored photon pair production "
        "γ₁·γ₂ → e⁻e⁺. Photons γ = 𝟙 + φ₀σ₀ + φ₁σ₁ with independent "
        "formal color weights. Checks whether energy budget "
        "Δ(pair)×E₀ = 2mₑ is achievable."
    ),
    "symbolic_q_form": symbolic_q_form,
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "git_sha": SHA,
    "parameters": {
        "q0": q0,
        "HA": HA0,
        "E0_MeV": E0,
        "m_e_MeV": M_E_MEV,
        "threshold_2me_MeV": 2 * M_E_MEV,
    },
    "energy_balance": {
        "net_eminus": net_eminus,
        "net_eplus": net_eplus,
        "net_ee_sum": net_ee,
        "target_delta_2me_over_E0": target_delta,
        "net_gg_target": net_gg_target,
        "bare_photon_E_pair_MeV": E_bare,
        "bare_vs_threshold": "above" if E_bare > 2*M_E_MEV else "below",
    },
    "nf_formula": {
        "c_identity": "1 + φ₀ψ₀ + φ₁ψ₁",
        "c_sigma0": "φ₀ + ψ₀ + φ₀ψ₀·HA",
        "c_sigma1": "φ₁ + ψ₁ + φ₁ψ₁·HA",
        "C_plus": "φ₀·ψ₁",
        "C_minus": "φ₁·ψ₀",
        "net": "(1+φ₀+φ₁)(1+ψ₀+ψ₁) + (φ₀ψ₀+φ₁ψ₁)·HA",
    },
    "symbolic_verification": all_match,
    "ratio_sweep": ratio_data,
    "sample_curve": sample_results,
}

out_path = Path(__file__).with_suffix(".witness.json")
out_path.write_text(json.dumps(witness, indent=2))
print(f"\n  Witness written to {out_path.name}")
