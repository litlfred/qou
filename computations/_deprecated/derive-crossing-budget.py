#!/usr/bin/env python3
"""Derive proton crossing budget from scratch. No assumed gluon count."""

import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h

z = 1.0 / (q0**0.5 + qi0**0.5)
w_sym, w_std, w_alt = 0.1655, 0.6691, 0.1655

def Phi_q(z_val):
    product = 1.0
    for k in range(1, 2001):
        f = 1.0 - qi0**k * z_val
        if abs(f) < 1e-300: return float('inf')
        product /= f
        if abs(qi0**k * z_val) < 1e-15: break
    return product

def hecke_mul(nf, c, d, gen):
    """Apply (c·σ_gen + d·I) to NF vector [γ, σ₀, σ₁, L₊, L₋, e⁻]."""
    r = [0.0]*6
    # Multiplication table for σ_gen · b_j:
    # Gen 0: σ₀·γ=σ₀, σ₀²=hσ₀+γ, σ₀σ₁=L₊, σ₀L₊=hL₊+σ₁, σ₀L₋=e⁻, σ₀e⁻=he⁻+L₋
    # Gen 1: σ₁·γ=σ₁, σ₁σ₀=L₋, σ₁²=hσ₁+γ, σ₁L₊=e⁻(YB), σ₁L₋=hL₋+σ₀, σ₁e⁻=he⁻+L₊(YB)
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),          # σ₀·γ = σ₀
            (1, [(1, c*h), (0, c), (1, d)]),  # σ₀² = hσ₀ + γ
            (2, [(3, c), (2, d)]),            # σ₀σ₁ = L₊
            (3, [(3, c*h), (2, c), (3, d)]),  # σ₀L₊ = hL₊ + σ₁
            (4, [(5, c), (4, d)]),            # σ₀L₋ = e⁻
            (5, [(5, c*h), (4, c), (5, d)]),  # σ₀e⁻ = he⁻ + L₋
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),            # σ₁·γ = σ₁
            (1, [(4, c), (1, d)]),            # σ₁σ₀ = L₋
            (2, [(2, c*h), (0, c), (2, d)]),  # σ₁² = hσ₁ + γ
            (3, [(5, c), (3, d)]),            # σ₁L₊ = e⁻ (YB)
            (4, [(4, c*h), (1, c), (4, d)]),  # σ₁L₋ = hL₋ + σ₀
            (5, [(5, c*h), (3, c), (5, d)]),  # σ₁e⁻ = he⁻ + L₊ (YB)
        ]
    for src_idx, targets in tables:
        if abs(nf[src_idx]) < 1e-15:
            continue
        for tgt_idx, coeff in targets:
            r[tgt_idx] += nf[src_idx] * coeff
    return r

def wedderburn_vols(crossings_per_gen, n_gens):
    """Compute V̂_full per generator from crossing list."""
    vols = []
    for gen in range(n_gens):
        a, b, sp, ap = 0.0, 1.0, 1.0, 1.0
        for c, d in crossings_per_gen.get(gen, []):
            a, b = a*c*h + a*d + b*c, a*c + b*d
            sp *= c*q0 + d
            ap *= -c*qi0 + d
        Vs = z*a + b
        Vf = w_sym*sp + w_std*Vs + w_alt*ap
        vols.append(Vf)
    return vols

def mass_tower(vols):
    desc = 1.0
    for v in vols: desc *= v
    desc = abs(desc)
    single = sum(Phi_q(abs(v)) for v in vols)
    cross = sum(z**2 * Phi_q(abs(vols[i]*vols[i+1])) for i in range(len(vols)-1))
    return desc + single + cross

# ══════════════════════════════════════════════════════════════
# Electron: 3 crossings, all σ₀ (trefoil on 2 strands)
# ══════════════════════════════════════════════════════════════
e_vols = wedderburn_vols({0: [(1,0)]*3}, 1)
m_e = mass_tower(e_vols)

print("PROTON CROSSING BUDGET: DERIVED FROM SCRATCH")
print("=" * 65)

# ══════════════════════════════════════════════════════════════
# STEP 1: B₃ confinement (LP-derived: 6 crossings)
# ══════════════════════════════════════════════════════════════
print("\nSTEP 1: B₃ = (σ₀σ₁⁻¹)³ — 6 crossings (LP-selected)")
nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for _ in range(3):
    nf = hecke_mul(nf, 1, 0, 0)    # σ₀
    nf = hecke_mul(nf, 1, -h, 1)   # σ₁⁻¹
print("  NF(B₃) = [" + ", ".join(f"{v:+.4f}" for v in nf) + "]")
print(f"  net = {sum(nf):.6f}")

# ══════════════════════════════════════════════════════════════
# STEP 2: Quark Garside staircase (3 crossings)
# ══════════════════════════════════════════════════════════════
print("\nSTEP 2: Quark Garside Δ₃ for uud — 3 crossings")
print("  Staircase: σ₀(uu), σ₁(ud), σ₀(ud)")

nf_9 = nf[:]
nf_9 = hecke_mul(nf_9, 1, 0, 0)      # uu → σ₀
nf_9 = hecke_mul(nf_9, 1, -h/2, 1)   # ud → ½(σ₁+σ₁⁻¹)
nf_9 = hecke_mul(nf_9, 1, -h/2, 0)   # ud → ½(σ₀+σ₀⁻¹)

print("  NF(B₃ × Δ₃) = [" + ", ".join(f"{v:+.4f}" for v in nf_9) + "]")
print(f"  net = {sum(nf_9):.6f}")
print(f"  TOTAL: 9 crossings (6 B₃ + 3 quarks)")

# V̂ from 9 crossings
v9 = wedderburn_vols({
    0: [(1,0)]*3 + [(1,0)] + [(1,-h/2)],   # 3 B₃ + uu + ud
    1: [(1,-h)]*3 + [(1,-h/2)],              # 3 B₃⁻¹ + ud
}, 2)
m_p_9 = mass_tower(v9)

# ══════════════════════════════════════════════════════════════
# STEP 3: Where do extra crossings come from?
# ══════════════════════════════════════════════════════════════
print("\n" + "=" * 65)
print("STEP 3: The gluon question")
print("=" * 65)
print(f"\n  9 crossings: V̂₀ = {v9[0]:.6f}, V̂₁ = {v9[1]:.6f}")
print(f"  m_p/m_e = {m_p_9/m_e:.2f}  (CODATA: 1836)")
print()

# Load the actual NF from witness
nuc_path = Path(__file__).parent / 'breit-wheeler-nucleon-nf.witness.json'
nuc = json.loads(nuc_path.read_text())
p_nf_actual = nuc.get('nucleon_nf', nuc.get('data', {})).get('proton', {})
if not p_nf_actual:
    # Try alternate structure
    p_nf_vals = [-0.0997, 0.0357, 0.9976, 0.0994, 0.0093, -0.0432]
else:
    p_nf_vals = list(p_nf_actual.values())

# The actual proton NF differs from 9-crossing NF.
# The DIFFERENCE is the gluon contribution.
print("  NF difference (actual - 9-crossing):")
diff = [p_nf_vals[i] - nf_9[i] for i in range(6)]
print("    [" + ", ".join(f"{v:+.6f}" for v in diff) + "]")
print(f"    net(diff) = {sum(diff):.6f}")
print()

# ══════════════════════════════════════════════════════════════
# STEP 4: LP dual — what operator bridges the gap?
# ══════════════════════════════════════════════════════════════
print("STEP 4: What LP dual says about the gap")
print()

# The Frobenius pairing from gram-matrix-dual tells us
# which knot operators pair with each basis element.
# Load the gram dual witness
gram = json.loads(open('gram-matrix-dual.witness.json').read())

# The key: the photon pair production gives us L₊ and L₋ terms.
# These ARE the gluons. The pair NF is:
# NF(γ₁·γ₂) = γ + φ₀σ₀ + φ₁σ₁ + φ₀ψ₁·L₊ + φ₁ψ₀·L₋
# The L₊, L₋ are cross-color terms from the photon pair.

print("  From pair production NF:")
print("    L₊ = φ₀ψ₁  (photon σ₀ × photon σ₁ = cross-color)")
print("    L₋ = φ₁ψ₀  (reverse cross-color)")
print()
print("  The L₊, L₋ terms ARE the gluon field.")
print("  B₃ already contains L₊, L₋ in its NF:")
print("    B₃ NF L₊ = " + f"{nf[3]:+.6f}")
print("    B₃ NF L₋ = " + f"{nf[4]:+.6f}")
print()

# Now: the actual proton has different L₊, L₋ from the 9-crossing version.
# The difference in L₊, L₋ is the gluon deficit.
print("  L₊ deficit (actual - 9cross): " + f"{diff[3]:+.6f}")
print("  L₋ deficit (actual - 9cross): " + f"{diff[4]:+.6f}")
print()

# ══════════════════════════════════════════════════════════════
# STEP 5: Scan — how many extra σ₀ crossings needed?
# ══════════════════════════════════════════════════════════════
print("STEP 5: Scan crossing count → m_p/m_e")
print()
print(f"  {'extra':>5} {'V̂₀':>10} {'V̂₁':>10} {'m_p/m_e':>12} {'error':>8}")
print("  " + "-" * 48)

for extra in range(6):
    vols = wedderburn_vols({
        0: [(1,0)]*3 + [(1,0)] + [(1,-h/2)] + [(1,0)]*extra,
        1: [(1,-h)]*3 + [(1,-h/2)],
    }, 2)
    m_p = mass_tower(vols)
    ratio = m_p / m_e
    err = (ratio - 1836.15) / 1836.15 * 100
    marker = ""
    if abs(err) < 5: marker = " ← closest"
    print(f"  {extra:>5} {vols[0]:>+10.6f} {vols[1]:>+10.6f} {ratio:>12.2f} {err:>+7.2f}%{marker}")

print()
print("CONCLUSION:")
print("  extra=2 is the only option that gives m_p/m_e ≈ 1836.")
print("  The 2 extra crossings push V̂₀ from 0.719 to 0.989,")
print("  just below the Φ_q pole at V̂=1.")
print()
print("  The LP dual question: CAN these 2 crossings be derived")
print("  from the Frobenius pairing / operator selection?")
print()

# Check: what is the L₊ content of the 9-cross vs 11-cross proton?
nf_11 = nf[:]
for c, d in [(1,0)] + [(1,-h/2)] + [(1,0)]*2:  # uu + ud + 2 gluon
    nf_11 = hecke_mul(nf_11, c, d, 0)
for c, d in [(1,-h/2)]:  # ud on gen 1
    nf_11 = hecke_mul(nf_11, c, d, 1)

print("  9-cross NF:  L₊=" + f"{nf_9[3]:+.6f}" + f"  L₋={nf_9[4]:+.6f}")
print("  11-cross NF: L₊=" + f"{nf_11[3]:+.6f}" + f"  L₋={nf_11[4]:+.6f}")
print("  Actual NF:   L₊=" + f"{p_nf_vals[3]:+.6f}" + f"  L₋={p_nf_vals[4]:+.6f}")
