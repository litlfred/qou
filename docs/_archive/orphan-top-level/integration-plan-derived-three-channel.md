# Integration Plan: Derived Atom Construction → Three-Channel Hecke Engine

## Status: WAITING — blocked on `claude/refine-atom-construction-ay72P`

## Goal

Replace the 5 fitted Bethe-Weizsacker coefficients and CODATA-imported
constituent masses in `atom_mass_full_hecke.py` with categorically
derived quantities from the refine-atom-construction branch. Keep our
three-channel Wedderburn decomposition (sym/std/alt) as a new analytical
lens on the derived NF elements.

---

## What to replace

| Current (fitted/imported) | Replace with (derived) | Source on refine branch |
|--------------------------|----------------------|----------------------|
| m_p = 938.272 MeV (CODATA) | net(𝔭) × energy_scale from nucleon NF | `four-term-pair-nucleon.md`, `breit-wheeler-nucleon-nf.py` |
| m_n = 939.565 MeV (CODATA) | net(𝔫) × energy_scale from nucleon NF | same |
| λ_V = 15.56 MeV (fitted) | NF reduction cost from typed Garside | `typed-garside-element.md`, `he4-full-word.py` |
| λ_S = 17.23 MeV (fitted) | Surface deficit in Garside NF | `torus-knot-shell-binding.md` |
| λ_C = 0.697 MeV (fitted) | Crossing asymmetry from pp eigenvalue excess | `gram-weighted-qvalue.md` |
| a_A = 23.29 MeV (fitted) | Pauli asymmetry from alternating channel | `gram-weight-eigenstructure.md` |
| δ_pair = 12/√A (fitted) | Cooper Hopf loop from NF pairing terms | TBD (may stay semi-empirical initially) |

## What to keep

- **Three-channel Wedderburn traces** (sym/std/alt) — new finding
- **Fibre/horizontal/mixed decomposition** — orthogonal to NF approach
- **Exact rational arithmetic** (QRatFull class)
- **Ground-state ordering search**

## Integration steps

### Step 1: Import nucleon NFs from refine branch

Pull the proton/neutron NF coefficients from
`four-term-photon-to-atoms.py` and express them in our QRatFull
framework. The key data:

```python
# Proton NF (from γγ → B₃ → typed crossings)
PROTON_NF = {
    'γ': -0.100, 'σ₀': +0.036, 'σ₁': +0.998,
    'L₊': +0.099, 'L₋': +0.009, 'e⁻': -0.043,
}  # net ≈ +0.999

# Neutron NF (from γγ → B₃ → typed crossings)  
NEUTRON_NF = {
    'γ': -0.202, 'σ₀': +0.048, 'σ₁': +1.009,
    'L₊': -0.010, 'L₋': +0.009, 'e⁻': -0.044,
}  # net ≈ +0.811
```

Then compute three-channel traces of the NF elements directly
(project onto sym/std/alt eigenspaces of the Wedderburn decomposition).

### Step 2: Replace Bethe-Weizsacker with typed Garside NF

For each nucleus (Z, N):
1. Build typed Garside element 𝒢(t₀,...,t_{A-1}) in H_A(q)
2. Compute Gröbner-Shirshov NF (inductive reduction)
3. Extract binding from NF reduction cost:
   - B(Z,N) ∝ ||𝒢_par||₁ (L¹ norm of parent NF)
4. For Q-values: use Gram-weighted formula from `gram-weighted-qvalue.md`:
   - Q = (Σ w_k^G · Δ_k) × N × m_e

This requires either:
- (a) Porting `he4-full-word.py` logic into our engine, or
- (b) Using the Rust hecke-engine (`tools/hecke-engine/`) for NF computation
  and feeding results into our Python three-channel analysis

Option (b) is better for A > 10 (Rust handles large NFs efficiently).

### Step 3: Three-channel decomposition of Garside element

**New contribution**: Project the typed Garside element onto
irreducible representations via character theory:

```
tr_sym(𝒢) = Σ_w c_w · q^{ℓ(w)}      (symmetric character)
tr_alt(𝒢) = Σ_w c_w · (-q⁻¹)^{ℓ(w)}  (alternating character)
tr_std(𝒢) = Σ_w c_w · χ_std(w)        (standard character)
```

This gives us the three-channel decomposition of the **derived**
nuclear element, not just the transfer-matrix-chain approximation.

### Step 4: Mass from derived NF + three-channel trace

The final atomic mass becomes:

```
M(Z,N) = Z · m_p^{derived} + N · m_n^{derived} + Z · m_e
         - B^{Garside}(Z,N)
```

where:
- m_p^{derived} = |tr_M(𝔭_NF)| × κ (energy scale from q)
- m_n^{derived} = |tr_M(𝔫_NF)| × κ
- B^{Garside} = f(||𝒢||₁, Gram weights)

And the three-channel decomposition tells us how much of the
mass lives in each irreducible sector.

---

## Dependencies from refine branch

### Files to merge/use:
- `computations/four-term-photon-to-atoms.py` — nucleon derivation
- `computations/he4-full-word.py` — full H_A(q) word analysis
- `computations/confinement-lp.py` — B₃ proof
- `computations/confinement-operator-selection.py` — exhaustive search
- `tools/hecke-engine/src/main.rs` — Rust NF engine for A > 10
- Content blocks: `derived-atom.md`, `four-term-pair-nucleon.md`,
  `torus-knot-shell-binding.md`, `gram-weighted-qvalue.md`

### Key data to extract:
- Nucleon NF coefficients (proton, neutron) — 6 floats each
- B₃ confinement operator NF — 6 floats
- Gram matrix eigenstructure for H_A(q) at each A
- Torus knot shell boundary coefficients (Chebyshev recurrence)

---

## Verification plan

1. **Hydrogen**: m_p^{derived} should match CODATA to ~0.1%
2. **Helium-4**: B^{Garside}(2,2) should give ~28.3 MeV (AME2020: 28.296)
3. **Three-channel consistency**: tr_full from Garside projection should
   match tr_full from transfer-matrix chain (current approach) for small A
4. **Channel suppression**: Verify standard channel still exponentially
   suppressed in the Garside-derived traces
5. **All 10 atoms**: Deviations from AME2020 should be ≤ current (~6 MeV)
   and ideally better (no fitted coefficients)
