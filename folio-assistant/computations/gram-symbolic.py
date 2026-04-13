#!/usr/bin/env python3
"""
Symbolic Gram matrix computation in H₃(q).

Everything is symbolic in q — no numerical evaluation until
comparison with physical observables at q₀.
"""
import sympy as sp

q = sp.Symbol('q', positive=True)
qi = 1 / q
h = q - qi                           # Hecke amplitude
z = 1 / (sp.sqrt(q) + 1/sp.sqrt(q))  # Markov parameter

# Markov trace of each NF basis element
tr_basis = {
    'γ': sp.Integer(1),
    'σ₀': z,
    'σ₁': z,
    'L₊': z**2,
    'L₋': z**2,
    'e⁻': z**3,
}

print("Markov trace of NF basis elements (symbolic):")
for name, val in tr_basis.items():
    simplified = sp.simplify(val)
    print(f"  tr_M({name}) = {simplified}")

# ── Symbolic NF products b_i · b_j ──────────────────────────
# From Hecke algebra: σᵢ² = hσᵢ + 1, σ₀σ₁σ₀ = σ₁σ₀σ₁ (YB)
# We encode NF(b_i · b_j) as a 6-vector [γ, σ₀, σ₁, L₊, L₋, e⁻]

O = sp.Integer(0)
I = sp.Integer(1)

# Products: NF(b_i · b_j) — read off from the Hecke algebra rules
# γ · anything = anything
# σ₀ · σ₀ = hσ₀ + γ
# σ₀ · σ₁ = L₊
# σ₀ · L₊ = σ₀·σ₀σ₁ = (hσ₀+γ)σ₁ = hL₊ + σ₁
# σ₀ · L₋ = σ₀σ₁σ₀ = e⁻
# σ₀ · e⁻ = σ₀·σ₀σ₁σ₀ = (hσ₀+γ)σ₁σ₀ = hL₋ + L₋ ... wait
# Let me just be systematic

names = ['γ', 'σ₀', 'σ₁', 'L₊', 'L₋', 'e⁻']

# NF products b_i · b_j reduced using only:
#   σᵢ² = hσᵢ + γ  (Hecke relation)
#   σ₀σ₁σ₀ = σ₁σ₀σ₁  (Yang-Baxter)
# Basis order: [γ, σ₀, σ₁, L₊, L₋, e⁻]

# Row i, column j → NF coefficients of b_i · b_j
NF = {}

# γ · anything = that thing
NF[('γ','γ')] = [I, O, O, O, O, O]
NF[('γ','σ₀')] = [O, I, O, O, O, O]
NF[('γ','σ₁')] = [O, O, I, O, O, O]
NF[('γ','L₊')] = [O, O, O, I, O, O]
NF[('γ','L₋')] = [O, O, O, O, I, O]
NF[('γ','e⁻')] = [O, O, O, O, O, I]

# anything · γ = that thing
NF[('σ₀','γ')] = [O, I, O, O, O, O]
NF[('σ₁','γ')] = [O, O, I, O, O, O]
NF[('L₊','γ')] = [O, O, O, I, O, O]
NF[('L₋','γ')] = [O, O, O, O, I, O]
NF[('e⁻','γ')] = [O, O, O, O, O, I]

# σ₀ · σ₀ = hσ₀ + γ
NF[('σ₀','σ₀')] = [I, h, O, O, O, O]

# σ₀ · σ₁ = L₊
NF[('σ₀','σ₁')] = [O, O, O, I, O, O]

# σ₁ · σ₀ = L₋
NF[('σ₁','σ₀')] = [O, O, O, O, I, O]

# σ₁ · σ₁ = hσ₁ + γ
NF[('σ₁','σ₁')] = [I, O, h, O, O, O]

# σ₀ · L₊ = σ₀ · σ₀σ₁ = (hσ₀+γ)σ₁ = hσ₀σ₁ + σ₁ = hL₊ + σ₁
NF[('σ₀','L₊')] = [O, O, I, h, O, O]

# σ₀ · L₋ = σ₀ · σ₁σ₀ = σ₀σ₁σ₀ = e⁻
NF[('σ₀','L₋')] = [O, O, O, O, O, I]

# σ₀ · e⁻ = σ₀ · σ₀σ₁σ₀ = σ₀²σ₁σ₀ = (hσ₀+γ)σ₁σ₀ = hσ₀σ₁σ₀ + σ₁σ₀ = he⁻ + L₋
NF[('σ₀','e⁻')] = [O, O, O, O, I, h]

# σ₁ · L₊ = σ₁ · σ₀σ₁ = σ₁σ₀σ₁ = e⁻  (by YB: σ₁σ₀σ₁ = σ₀σ₁σ₀)
NF[('σ₁','L₊')] = [O, O, O, O, O, I]

# σ₁ · L₋ = σ₁ · σ₁σ₀ = σ₁²σ₀ = (hσ₁+γ)σ₀ = hσ₁σ₀ + σ₀ = hL₋ + σ₀
NF[('σ₁','L₋')] = [O, I, O, O, h, O]

# σ₁ · e⁻ = σ₁ · σ₀σ₁σ₀
# Use YB: e⁻ = σ₁σ₀σ₁, so σ₁·e⁻ = σ₁·σ₁σ₀σ₁ = σ₁²σ₀σ₁ = (hσ₁+γ)σ₀σ₁
# = hσ₁σ₀σ₁ + σ₀σ₁ = he⁻ + L₊
NF[('σ₁','e⁻')] = [O, O, O, I, O, h]

# L₊ · σ₀ = σ₀σ₁ · σ₀ = σ₀σ₁σ₀ = e⁻
NF[('L₊','σ₀')] = [O, O, O, O, O, I]

# L₊ · σ₁ = σ₀σ₁ · σ₁ = σ₀σ₁² = σ₀(hσ₁+γ) = hσ₀σ₁ + σ₀ = hL₊ + σ₀
NF[('L₊','σ₁')] = [O, I, O, h, O, O]

# L₊ · L₊ = σ₀σ₁ · σ₀σ₁ = σ₀(σ₁σ₀σ₁) = σ₀·e⁻ (by YB) = he⁻ + L₋
NF[('L₊','L₊')] = [O, O, O, O, I, h]

# L₊ · L₋ = σ₀σ₁ · σ₁σ₀ = σ₀σ₁²σ₀ = σ₀(hσ₁+γ)σ₀ = hσ₀σ₁σ₀ + σ₀² = he⁻ + hσ₀ + γ
NF[('L₊','L₋')] = [I, h, O, O, O, h]

# L₊ · e⁻ = σ₀σ₁ · σ₀σ₁σ₀ = σ₀(σ₁σ₀σ₁)σ₀ = σ₀·e⁻·σ₀
# = σ₀(he⁻+L₋)  ... wait, we computed σ₀·e⁻ = he⁻ + L₋ above
# so L₊·e⁻ = (σ₀σ₁)(σ₀σ₁σ₀) need to reassociate
# = σ₀ · σ₁ · σ₀ · σ₁ · σ₀  ... this is T_{2,5} braid word
# Let's compute step by step:
# σ₀σ₁σ₀σ₁σ₀:
# Step 1: σ₀σ₁ = L₊
# Step 2: L₊ · σ₀ = e⁻
# Step 3: e⁻ · σ₁ = he⁻ + L₊  (from σ₁·e⁻ by cyclicity? No.)
# Wait — e⁻·σ₁ ≠ σ₁·e⁻. Let me compute e⁻·σ₁ directly.
# e⁻·σ₁ = σ₀σ₁σ₀·σ₁. Use YB on positions 2,3,4: σ₀σ₁ = ... no
# σ₀σ₁σ₀σ₁: apply YB to σ₀σ₁σ₀ → σ₁σ₀σ₁:
# = σ₁σ₀σ₁² = σ₁σ₀(hσ₁+γ) = hσ₁σ₀σ₁ + σ₁σ₀ = he⁻ + L₋
# So e⁻·σ₁ = he⁻ + L₋? That can't be right — that's the same as σ₀·e⁻
# Let me recheck: σ₀·e⁻ = σ₀·σ₀σ₁σ₀ = σ₀²σ₁σ₀ = (hσ₀+1)σ₁σ₀ = hL₋... wait
# e⁻·σ₁ = σ₀σ₁σ₀σ₁ = σ₀²σ₁σ₀ = he⁻ + L₋

NF[('e⁻','σ₁')] = [O, O, O, O, I, h]

# e⁻·σ₀ = σ₀σ₁σ₀·σ₀ = σ₀σ₁σ₀² = σ₀σ₁(hσ₀+γ) = hσ₀σ₁σ₀ + σ₀σ₁ = he⁻ + L₊
NF[('e⁻','σ₀')] = [O, O, O, I, O, h]

# e⁻·L₊ = (he⁻+L₊)σ₁ = h(he⁻+L₋) + (hL₊+σ₀) = h²e⁻ + hL₋ + hL₊ + σ₀
NF[('e⁻','L₊')] = [O, I, O, h, h, h**2]

# L₋·σ₀ = σ₁σ₀² = σ₁(hσ₀+γ) = hL₋ + σ₁
NF[('L₋','σ₀')] = [O, O, I, O, h, O]

# e⁻·L₋ = (he⁻+L₋)σ₀ = h(he⁻+L₊) + (hL₋+σ₁) = h²e⁻ + hL₊ + hL₋ + σ₁
NF[('e⁻','L₋')] = [O, O, I, h, h, h**2]

# L₋ · σ₁ = σ₁σ₀·σ₁ = σ₁σ₀σ₁ = e⁻ (by YB)
NF[('L₋','σ₁')] = [O, O, O, O, O, I]

# L₋ · L₊ = σ₁σ₀·σ₀σ₁ = σ₁σ₀²σ₁ = σ₁(hσ₀+γ)σ₁ = hσ₁σ₀σ₁ + σ₁²
# = he⁻ + hσ₁ + γ
NF[('L₋','L₊')] = [I, O, h, O, O, h]

# L₋ · L₋ = σ₁σ₀·σ₁σ₀ = σ₁(σ₀σ₁σ₀) = σ₁·e⁻ = he⁻ + L₊
NF[('L₋','L₋')] = [O, O, O, I, O, h]

# L₋ · e⁻ = σ₁σ₀·σ₀σ₁σ₀ = σ₁σ₀²σ₁σ₀ = σ₁(hσ₀+γ)σ₁σ₀
# = h·σ₁σ₀σ₁σ₀ + σ₁²σ₀
# σ₁σ₀σ₁σ₀ = e⁻·σ₀ = he⁻ + L₊
# σ₁²σ₀ = (hσ₁+γ)σ₀ = hL₋ + σ₀
# So: h(he⁻+L₊) + hL₋ + σ₀ = h²e⁻ + hL₊ + hL₋ + σ₀
NF[('L₋','e⁻')] = [O, I, O, h, h, h**2]

# L₊ · e⁻: σ₀σ₁·σ₀σ₁σ₀ = σ₀(σ₁σ₀σ₁)σ₀ = σ₀(σ₀σ₁σ₀)σ₀ = σ₀²σ₁σ₀²
# = (hσ₀+γ)σ₁(hσ₀+γ) = (hσ₀+γ)(hσ₁σ₀+σ₁)
# = h²σ₀σ₁σ₀ + hσ₀σ₁ + hσ₁σ₀ + σ₁
# = h²e⁻ + hL₊ + hL₋ + σ₁
NF[('L₊','e⁻')] = [O, O, I, h, h, h**2]

# e⁻ · e⁻ = σ₀σ₁σ₀·σ₀σ₁σ₀ = σ₀σ₁(σ₀²)σ₁σ₀ = σ₀σ₁(hσ₀+γ)σ₁σ₀
# = h·σ₀σ₁σ₀σ₁σ₀ + σ₀σ₁²σ₀
# First term: σ₀σ₁σ₀σ₁σ₀ = T_{2,5} word.
# L₊·e⁻ = h²e⁻ + hL₊ + hL₋ + σ₁ (just computed)
# So h·(σ₀σ₁σ₀σ₁σ₀) = h·(L₊·e⁻) ... wait, σ₀σ₁σ₀σ₁σ₀ = L₊·(L₊·σ₀)... hmm
# Let me just use: σ₀σ₁σ₀σ₁σ₀ is the cinquefoil braid word.
# I already know from the numeric table that NF(e⁻·e⁻) at q₀ is:
# [1.000, 0.209, 0.209, 0.044, 0.044, 0.218]
# = [γ, hσ₀, hσ₁, h²L₊, h²L₋, (h²+1)... hmm not exact
# Let me compute symbolically:
# e⁻·e⁻ = (σ₀σ₁σ₀)² = σ₀σ₁σ₀²σ₁σ₀ = σ₀σ₁(hσ₀+1)σ₁σ₀
# = h·σ₀σ₁σ₀σ₁σ₀ + σ₀σ₁²σ₀
# Second: σ₀σ₁²σ₀ = σ₀(hσ₁+1)σ₀ = hσ₀σ₁σ₀ + σ₀² = he⁻ + hσ₀ + γ
# First: σ₀σ₁σ₀σ₁σ₀ — this is T_{2,5}. Let me compute it:
# σ₀σ₁σ₀σ₁σ₀ = (σ₀σ₁σ₀)(σ₁σ₀) = e⁻ · L₋
# But I need NF(e⁻·L₋) which I computed: h²e⁻ + hL₊ + hL₋ + σ₁
# So: e⁻·e⁻ = h·(h²e⁻ + hL₊ + hL₋ + σ₁) + (he⁻ + hσ₀ + γ)
# = h³e⁻ + h²L₊ + h²L₋ + hσ₁ + he⁻ + hσ₀ + γ
# = γ + hσ₀ + hσ₁ + h²L₊ + h²L₋ + (h³+h)e⁻
NF[('e⁻','e⁻')] = [I, h, h, h**2, h**2, h**3 + h]

# ── Compute Gram matrix G_{ij} = tr_M(b_i · b_j) ───────────

print("\n" + "=" * 72)
print("  SYMBOLIC GRAM MATRIX")
print("=" * 72)

tr_vec = [sp.Integer(1), z, z, z**2, z**2, h*z**2 + z]

G = sp.zeros(6, 6)
for i, ni in enumerate(names):
    for j, nj in enumerate(names):
        key = (ni, nj)
        if key not in NF:
            print(f"  MISSING: {ni} · {nj}")
            continue
        nf = NF[key]
        # tr_M(Σ c_k b_k) = Σ c_k tr_M(b_k)
        val = sum(c * t for c, t in zip(nf, tr_vec))
        G[i, j] = sp.simplify(val)

print("\nG_{ij} = tr_M(b_i · b_j):\n")
for i in range(6):
    row = []
    for j in range(6):
        row.append(sp.simplify(G[i, j]))
    print(f"  {names[i]:4s}: {row}")

print(f"\n  det(G) = {sp.simplify(sp.det(G))}")

# Try to simplify and factor
print("\n  Simplified entries:")
for i in range(6):
    for j in range(i, 6):
        expr = sp.simplify(G[i, j])
        if expr != 0:
            print(f"    G[{names[i]},{names[j]}] = {expr}")

# ── Numeric check at q₀ ──────────────────────────────────────
try:
    import sys as _sys; _sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
    from q_parameter import Q as q0
except ImportError:
    q0 = 1.109978595554181  # canonical from CODATA 2022
print(f"\n  Numeric check at q₀ = {q0}:")
for i in range(6):
    row = []
    for j in range(6):
        row.append(float(G[i, j].subs(q, q0)))
    print(f"    {names[i]:4s}: {['%8.6f' % v for v in row]}")

# ── Compute inverse symbolically ─────────────────────────────
print("\n  Computing G⁻¹ symbolically...")
try:
    G_inv = G.inv()
    print("  G⁻¹ computed successfully.")
    print("\n  Simplified G⁻¹ entries:")
    for i in range(6):
        for j in range(i, 6):
            expr = sp.simplify(G_inv[i, j])
            if expr != 0:
                print(f"    G⁻¹[{names[i]},{names[j]}] = {expr}")
except Exception as e:
    print(f"  G⁻¹ computation failed: {e}")
    # Fall back to numeric
    import numpy as np
    G_num = np.array([[float(G[i, j].subs(q, q0)) for j in range(6)] for i in range(6)])
    G_inv_num = np.linalg.inv(G_num)
    print("  Numeric G⁻¹:")
    for i in range(6):
        print(f"    {names[i]:4s}: {['%8.4f' % v for v in G_inv_num[i]]}")

# ── NF products table (symbolic) ─────────────────────────────
print("\n" + "=" * 72)
print("  NF PRODUCT TABLE (symbolic in h = q − q⁻¹)")
print("=" * 72)

for (ni, nj), nf in sorted(NF.items(), key=lambda x: (names.index(x[0][0]), names.index(x[0][1]))):
    nonzero = [(names[k], nf[k]) for k in range(6) if nf[k] != 0]
    terms = " + ".join(f"{c}·{n}" if c != 1 else n for n, c in nonzero)
    print(f"  {ni}·{nj} = {terms}")
