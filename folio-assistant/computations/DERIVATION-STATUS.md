# BW Mass Formula: Derivation Status

## The Full Chain

```
Wedderburn weight w_λ = dim_q(λ)²/[n]_q!
  → per-generator eigenvalue product Π (c·λ_channel + d)
    → sum over generators Φ = Σ_i ln|V̂_i|
      → q-integer product [n₁]_q·[n₂]_q·...
        → BW coefficient × m_e
```

where [n]_q = Σ_{k=0}^{n-1} q^{n-1-2k} counts n crossings at alternating depths.

## Term-by-Term Derivation Status

### H₃(q): 3 partitions → 6 terms — FULLY DERIVED

| # | Term | Coefficient | Partition | Derivation | Lean |
|---|------|-------------|-----------|------------|------|
| 1 | Volume | 2[2]_q[7]_q·m_e | [3] sym | ✅ From sym eigenvalue chain: q^{n_pp}·(q⁻¹)^{n_nn}·([2]_q/2)^{n_pn} | ⬜ |
| 2 | Surface | 2[4]_q²·m_e | [3] sym | ✅ Boundary correction to volume (missing neighbors ∝ A^{2/3}) | ⬜ |
| 3 | Coulomb | (q-q⁻¹)[6]_q·m_e | [2,1] std | ✅ pp pairs / nuclear radius, [6]_q from B₃ crossing count | ⬜ |
| 4 | Asymmetry | 3[2]_q[7]_q·m_e | [2,1] std | ✅ nn-pp pair imbalance, same q-integers as volume ×3/2 | ⬜ |
| 5 | Pairing | [3]_q[7]_q·m_e | [2,1] std | ✅ Chebyshev sign alternation of (σ⁻¹)^Z | ⬜ |
| 6 | Exchange | [3]_q/[2]_q·m_e | [1³] alt | ✅ Surface pp screening: dim_q(std₃)/dim_q(std₂) | ⬜ |

### H₄(q): +2 partitions → +2 terms — PARTIALLY DERIVED

| # | Term | Coefficient | Partition | Derivation | Lean |
|---|------|-------------|-----------|------------|------|
| 7 | Shell | [2]_q²[3]_q·m_e | [3,1] hook₁ | ✅ Torus knot coherence at magic closures | ⬜ |
| 8 | Hook | \|β₄\|·\|ln λ_hook\|·m_e | [2,2] hook₂ | ⚠️ β₄ = -½w_{[2,2]}(4) derived, but |ln λ| factor is ad hoc | ⬜ |

### H₅(q): +3 channels → +3 terms — SCALINGS DERIVED, COEFFICIENTS OPEN

| # | Term | Coefficient | Partition | Derivation | Lean |
|---|------|-------------|-----------|------------|------|
| 9 | Wigner | ~68.9 MeV ❌ | [3,1,1] self-conj | ⚠️ Scaling T(T+1)/A derived from isospin Casimir. Coefficient NOT derived. χ_{[3,1,1]}(σ_k)=0 means it activates only on pair products. | ⬜ |
| 10 | Form factor | HA·[5]_q·m_e ✅ | [3,2]+[2,2,1] | ✅ Matches fit within 1.2%. Scaling Z²/A = charge density². | ⬜ |
| 11 | pn correlation | ~3.06 MeV ❌ | [4,1]+[2,1,1,1] | ⚠️ Scaling Z·N/A^{4/3} = pn surface density. Coefficient NOT derived. | ⬜ |

## Scaling Derivations (all from braid graph combinatorics)

| Scaling | Braid graph meaning | Status |
|---------|---------------------|--------|
| A | total crossing pairs A(A-1)/2 normalized | ✅ Derived |
| A^{2/3} | missing surface pairs (boundary nucleons) | ✅ Derived |
| Z(Z-1)/A^{1/3} | pp pairs / nuclear radius | ✅ Derived |
| (N-Z)²/(4A) | nn-pp pair imbalance | ✅ Derived |
| ±1/√A | pair parity (Chebyshev alternation) | ✅ Derived |
| Z^{4/3}/A^{1/3} | surface pp pairs | ✅ Derived |
| f_magic/A^{2/3} | coherent pairs at filled shells | ✅ Derived |
| (1-f)·A^{1/3} | incoherent inter-shell pairs | ✅ Derived |
| T(T+1)/A | isospin Casimir (from [3,1,1] pair character) | ✅ Derived |
| Z²/A | charge density² (proton form factor) | ✅ Derived |
| Z·N/A^{4/3} | pn surface density | ✅ Derived |

## Open Questions (Non-Derivable Items)

### CRITICAL (blocks derivation of coefficients)

1. **Term 9 coefficient**: χ_{[3,1,1]}(σ_k) = 0 but χ_{[3,1,1]}(σ_i·σ_j) ≠ 0.
   Need to compute the PAIR character and show it gives T(T+1) scaling
   with coefficient derivable from w_{[3,1,1]} × pair eigenvalue products.
   **Status**: Identified mechanism (pair character), not yet computed.

2. **Term 11 coefficient**: Same issue — need pair/multi-crossing character
   for the [4,1]+[2,1,1,1] channel.
   **Status**: Not yet attempted.

3. **Term 8 coefficient**: The |ln λ_hook| factor in δ_hook is ad hoc.
   Should be derivable from the hook eigenvalue chain product.
   **Status**: Partially identified (λ_hook = [2]_q - 2), multiplicative
   structure not proven.

### IMPORTANT (affects accuracy but not structure)

4. **Magic number origin**: Why {2, 8, 20, 28, 50, 82, 126} specifically?
   The shell correction uses these as input. They should be derivable from
   torus knot embedding on the genus-4 Bring's surface.
   **Status**: Documented in prop:nuclear-shell-intruder, not fully proven.

5. **Shell width σ = [2]_q**: Derived as "quantum dimension of the pairing
   representation H₂(q)". Needs formal proof that this is the correct
   Gaussian width for the shell proximity function.
   **Status**: Asserted, not proven.

6. **Energy scale E₀ = 4.155 MeV**: Calibrated from n→p decay (E₀ = Q_β/|Δnet|).
   This is a single calibration point, not a derivation. Can it be derived
   from the algebra without using Q_β as input?
   **Status**: Open. Possible route: E₀ = m_e × (crossing factor from B₃).

### NICE TO HAVE (completeness)

7. **1/α discrepancy**: 136.82 vs 137.04 (0.155% gap, 185000σ from δq).
   The formula α = q⁻¹/([9]_q·[10]_q) is derived from force carrier
   identification (T_{2,9} strong, T_{3,5} weak). But the 0.155% residual
   may indicate a correction from higher-order knot operators.
   **Status**: Not investigated.

8. **Neutrino mass**: L₋ channel with V̂ ≈ z² gives m_ν/m_e ≈ 2 (wrong by 10⁶).
   The vacuum drag formula m_ν = m_e × ℏ_q^n gives keV range (still too high).
   **Status**: Unresolved.

9. **Molecular binding precision**: H-H vertex volume method gives 4.48 eV (0.1% match)
   but C-H, C-C, O-H give ~80% errors. The NF multiplication method is better
   for H-H (+63%) but worse for others.
   **Status**: Needs systematic investigation of bond operator choice.

## Key Insight: χ_{[3,1,1]}(σ_k) = 0

The self-conjugate partition [3,1,1] has **zero character on all single generators**.
This was verified computationally (6 standard Young tableaux, axial distances cancel).

This means:
- The [3,1,1] partition contributes ONLY through multi-crossing correlations
- Its BW coefficient accumulates from pair products σ_i·σ_j, not single σ_k
- This is why it encodes the ISOSPIN quantum number T(T+1) — isospin is a
  correlation between proton and neutron crossings, not a property of individual crossings
- The coefficient should be derivable from: w_{[3,1,1]} × Σ_{pairs} χ(σ_i·σ_j)

Computing χ_{[3,1,1]}(σ_i·σ_j) requires the 6×6 representation matrices
of [3,1,1] at each generator, then multiplying pairs and taking traces.
This is computationally straightforward but hasn't been done yet.
DERIVATION-STATUS.md
