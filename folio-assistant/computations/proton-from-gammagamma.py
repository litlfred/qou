#!/usr/bin/env python3
"""
Full proton derivation from γγ via LP dual and operator selection.

Step by step:
1. γγ pair production → NF (what comes out?)
2. Frobenius dual → which knot operators act?
3. e⁻ and e⁺ from T_{2,3} operator selection
4. Quarks from pair production
5. Three quarks + B₃ (LP-selected confinement) → proton
6. LP dual tells us what's MISSING (the gluon question)
"""

import json, sys, math
import numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h

z = 1.0 / (q0**0.5 + qi0**0.5)
NAMES = ['γ', 'σ₀', 'σ₁', 'L₊', 'L₋', 'e⁻']

def mul(nf, c, d, gen):
    r = [0.0]*6
    if gen == 0:
        rules = [(0,[(1,c),(0,d)]), (1,[(1,c*h),(0,c),(1,d)]), (2,[(3,c),(2,d)]),
                 (3,[(3,c*h),(2,c),(3,d)]), (4,[(5,c),(4,d)]), (5,[(5,c*h),(4,c),(5,d)])]
    else:
        rules = [(0,[(2,c),(0,d)]), (1,[(4,c),(1,d)]), (2,[(2,c*h),(0,c),(2,d)]),
                 (3,[(5,c),(3,d)]), (4,[(4,c*h),(1,c),(4,d)]), (5,[(5,c*h),(3,c),(5,d)])]
    for src, targets in rules:
        if abs(nf[src]) < 1e-15: continue
        for tgt, coeff in targets:
            r[tgt] += nf[src] * coeff
    return r

def show(label, nf):
    parts = [f"{v:+.4f}·{NAMES[i]}" for i, v in enumerate(nf) if abs(v) > 1e-6]
    print(f"  {label}")
    print(f"    NF = {' '.join(parts)}")
    print(f"    net = {sum(nf):.6f}, tr_M = {tr(nf):.6f}")

def tr(nf):
    w = [1.0, z, z, z**2, z**2, z**3]
    return sum(nf[i]*w[i] for i in range(6))

# Corrected Gram matrix (tr_M(e⁻) = z³)
G = np.array([
    [1.000000, 0.499320, 0.499320, 0.249321, 0.249321, 0.124491],
    [0.499320, 1.104388, 0.249321, 0.551443, 0.124491, 0.275347],
    [0.499320, 0.249321, 1.104388, 0.124491, 0.551443, 0.275347],
    [0.249321, 0.124491, 0.551443, 0.275347, 1.130414, 0.609008],
    [0.249321, 0.551443, 0.124491, 1.130414, 0.275347, 0.609008],
    [0.124491, 0.275347, 0.275347, 0.609008, 0.609008, 1.257733],
])
G_inv = np.linalg.inv(G)

def dual(nf):
    return list(G_inv @ np.array(nf))

def pair(a, b):
    return float(np.array(a) @ G @ np.array(b))

def knot_nf(name):
    nf = [1,0,0,0,0,0]
    if name == "T_{2,3}":
        nf = mul(mul(mul(nf,1,0,0),1,0,1),1,0,0)
    elif name == "T_{2,2}":
        nf = mul(mul(nf,1,0,0),1,0,0)
    elif name == "T_{2,1}":
        nf = mul(nf,1,0,0)
    elif name == "B₃":
        for _ in range(3):
            nf = mul(nf,1,0,0); nf = mul(nf,1,-h,1)
    return nf

print("=" * 70)
print("  PROTON FROM γγ: STEP BY STEP")
print("=" * 70)

# ─── 1. γγ PAIR PRODUCTION ─────────────────────────────────
print("\n─── 1. γγ PAIR PRODUCTION ───")
print("  Photon: γ = 𝟙 (identity in H₃(q))")
print("  Two bare photons: γ₁·γ₂ = 𝟙·𝟙 = 𝟙")
show("γγ bare", [1,0,0,0,0,0])

phi = 0.0487
nf_gg = [1 + 2*phi**2, phi*(2 + phi*h), phi*(2 + phi*h), phi**2, phi**2, 0]
show("γγ colored (φ=0.049)", nf_gg)
print()
print("  The colored pair has σ₀, σ₁ (virtual crossings)")
print("  and L₊, L₋ (Hopf links = gluon channels).")
print("  NO e⁻ component yet — need T_{2,3} to produce it.")

# ─── 2. OPERATOR SELECTION VIA FROBENIUS DUAL ──────────────
print("\n─── 2. OPERATOR SELECTION ───")
print("  For each particle K, compute K∨ = G⁻¹·K,")
print("  then ⟨K∨, T⟩_F gives the operator pairing.\n")

particles = {
    "γ (photon)":   [1,0,0,0,0,0],
    "e⁻ (electron)": [0,0,0,0,0,1],
    "L₊ (gluon+)":  [0,0,0,1,0,0],
    "B₃ (confined)": knot_nf("B₃"),
}
operators = ["identity", "T_{2,1}", "T_{2,2}", "T_{2,3}", "B₃"]

print(f"  {'Particle':<16}", end="")
for op in operators:
    print(f" {op:>10}", end="")
print()
print("  " + "-" * 68)

for pname, pnf in particles.items():
    d = dual(pnf)
    print(f"  {pname:<16}", end="")
    for op in operators:
        p = pair(d, knot_nf(op))
        print(f" {p:>+10.4f}", end="")
    print()

# ─── 3. T_{2,3} → e⁻ AND e⁺ ──────────────────────────────
print("\n─── 3. T_{2,3} PRODUCES e⁻ AND e⁺ ───")

nf_e = [0,0,0,0,0,1]  # electron = σ₀σ₁σ₀
nf_ep = [1,0,0,0,0,0]
nf_ep = mul(mul(mul(nf_ep, 1, -h, 0), 1, -h, 1), 1, -h, 0)

show("e⁻ (trefoil T_{2,3})", nf_e)
show("e⁺ (mirror trefoil)", nf_ep)

# Annihilation check
nf_ann = mul(mul(mul(nf_e[:], 1, -h, 0), 1, -h, 1), 1, -h, 0)
show("e⁻ · e⁺⁻¹ (annihilation)", nf_ann)

# ─── 4. QUARKS ────────────────────────────────────────────
print("\n─── 4. QUARKS (from pair production vertex) ───")
print("  u = positive crossing eigenvalue (+q)")
print("  d = negative crossing eigenvalue (-q⁻¹)")
print("  These are NOT standalone particles — they exist")
print("  only inside the Borromean environment.\n")

# ─── 5. B₃ CONFINEMENT ────────────────────────────────────
print("─── 5. B₃ CONFINEMENT (LP-selected) ───")
nf_B3 = knot_nf("B₃")
show("B₃ = (σ₀σ₁⁻¹)³", nf_B3)

Gb = G @ np.array(nf_B3)
print("  Frobenius Gx ≥ 0:", "YES ✓" if all(Gb >= -1e-10) else "NO ✗")
print()

# ─── 6. B₃ × QUARKS → PROTON (9 crossings) ────────────
print("─── 6. B₃ × QUARK GARSIDE → PROTON ───")
print("  Garside staircase Δ₃ for uud: 3 pairwise crossings")
print("    Level 0: σ₀(u₁-u₂) → positive")
print("    Level 1: σ₁(u₂-d₃) → mixed, σ₀(u₁-d₃) → mixed\n")

nf_p9 = nf_B3[:]
nf_p9 = mul(nf_p9, 1, 0, 0)        # uu
nf_p9 = mul(nf_p9, 1, -h/2, 1)     # ud gen 1
nf_p9 = mul(nf_p9, 1, -h/2, 0)     # ud gen 0
show("Proton (9 cross: 6 B₃ + 3 quarks)", nf_p9)

# ─── 7. LP DUAL: WHAT DOES THE PROTON DEMAND? ─────────
print("\n─── 7. LP DUAL: PROTON DEMAND ANALYSIS ───")
dual_p9 = dual(nf_p9)
print("  Frobenius dual of 9-crossing proton:")
for i in range(6):
    tag = "DEMAND" if dual_p9[i] < -0.01 else "supply" if dual_p9[i] > 0.01 else ""
    print(f"    {NAMES[i]}: {dual_p9[i]:>+.4f}  {tag}")

print("\n  Operator pairings (what operators does proton demand?):")
for op in operators:
    p = pair(dual_p9, knot_nf(op))
    if abs(p) > 0.001:
        tag = "← demands this!" if p < -0.01 else ""
        print(f"    ⟨p∨, {op:10s}⟩ = {p:+.6f}  {tag}")

# ─── 8. WHAT IF WE ADD MORE CROSSINGS? ────────────────
print("\n─── 8. EFFECT OF ADDITIONAL σ₀ CROSSINGS ───")
print("  If the proton DEMANDS additional content, each extra")
print("  σ₀ crossing fills that demand. How many are needed?\n")

w_sym, w_std, w_alt = 0.1655, 0.6691, 0.1655

def Phi_q(z_val):
    product = 1.0
    for k in range(1, 2001):
        f = 1.0 - qi0**k * z_val
        if abs(f) < 1e-300: return float('inf')
        product /= f
        if abs(qi0**k * z_val) < 1e-15: break
    return product

def mass_ratio(extra_gen0):
    # Gen 0 volumes
    a0, b0, sp0, ap0 = 0.0, 1.0, 1.0, 1.0
    for c, d in [(1,0)]*3 + [(1,0)] + [(1,-h/2)] + [(1,0)]*extra_gen0:
        a0, b0 = a0*c*h + a0*d + b0*c, a0*c + b0*d
        sp0 *= c*q0+d; ap0 *= -c*qi0+d
    V0 = w_sym*sp0 + w_std*(z*a0+b0) + w_alt*ap0

    a1, b1, sp1, ap1 = 0.0, 1.0, 1.0, 1.0
    for c, d in [(1,-h)]*3 + [(1,-h/2)]:
        a1, b1 = a1*c*h + a1*d + b1*c, a1*c + b1*d
        sp1 *= c*q0+d; ap1 *= -c*qi0+d
    V1 = w_sym*sp1 + w_std*(z*a1+b1) + w_alt*ap1

    Ve = 0.5939
    m_e = abs(Ve) + Phi_q(abs(Ve))
    m_p = abs(V0*V1) + Phi_q(abs(V0)) + Phi_q(abs(V1)) + z**2*Phi_q(abs(V0*V1))
    return m_p/m_e, V0, V1

# Also try extra crossings on gen 1
print(f"  {'extra_g0':>8} {'extra_g1':>8} {'V̂₀':>10} {'V̂₁':>10} {'m_p/m_e':>12} {'error':>8}")
print("  " + "-" * 60)

for eg0 in range(4):
    for eg1 in [0]:
        # Compute with extra on gen 0
        a0, b0, sp0, ap0 = 0.0, 1.0, 1.0, 1.0
        for c, d in [(1,0)]*3 + [(1,0)] + [(1,-h/2)] + [(1,0)]*eg0:
            a0, b0 = a0*c*h+a0*d+b0*c, a0*c+b0*d
            sp0 *= c*q0+d; ap0 *= -c*qi0+d
        V0 = w_sym*sp0+w_std*(z*a0+b0)+w_alt*ap0

        a1, b1, sp1, ap1 = 0.0, 1.0, 1.0, 1.0
        for c, d in [(1,-h)]*3 + [(1,-h/2)] + [(1,0)]*eg1:
            a1, b1 = a1*c*h+a1*d+b1*c, a1*c+b1*d
            sp1 *= c*q0+d; ap1 *= -c*qi0+d
        V1 = w_sym*sp1+w_std*(z*a1+b1)+w_alt*ap1

        Ve = 0.5939
        m_e = abs(Ve) + Phi_q(abs(Ve))
        if abs(V0) >= q0 or abs(V1) >= q0:
            print(f"  {eg0:>8} {eg1:>8} {V0:>+10.4f} {V1:>+10.4f} {'DIVERGES':>12} {'':>8}")
            continue
        m_p = abs(V0*V1) + Phi_q(abs(V0)) + Phi_q(abs(V1)) + z**2*Phi_q(abs(V0*V1))
        ratio = m_p/m_e
        err = (ratio-1836.15)/1836.15*100
        marker = " ←" if abs(err) < 5 else ""
        print(f"  {eg0:>8} {eg1:>8} {V0:>+10.6f} {V1:>+10.6f} {ratio:>12.2f} {err:>+7.2f}%{marker}")

print()
print("CONCLUSION:")
print("  With 9 crossings (B₃ + quarks only): V̂₀ = 0.719, m_p/m_e = 684")
print("  With 11 crossings (+2 on gen 0):     V̂₀ = 0.989, m_p/m_e = 1873")
print()
print("  The 2 extra crossings are the GLUON FIELD.")
print("  They must be DERIVED, not assumed.")
print("  The LP dual demand analysis above shows what the proton needs.")
