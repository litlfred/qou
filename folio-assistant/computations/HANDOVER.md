# Session Handover

## PRIMARY TASK: Derive figure-eight BW coefficients

The 11-term BW mass formula uses coefficients from the **Borromean braid B₃ = (σ₀σ₁⁻¹)³**. These work for A≥4 nuclei (0.025% MAE) but fail for A=3 (³H at 0.19%).

The nuclear knot classification (`prop:nuclear-knot-classification`) shows A=3 nuclei are **figure-eight-like** (Vol(4₁) = 2.030), not Borromean (Vol(B₃) = 7.328).

**The task**: derive the BW coefficient chain for **4₁ = σ₀σ₁⁻¹σ₀⁻¹σ₁** (4 crossings) from scratch. Same method as Borromean: Wedderburn → eigenvalue products → q-integer identification. The figure-eight has different crossing structure → different q-integer indices.

### Approaches tried and failed

- Uniform Vol(K)/Vol(B₃) scaling of all BW terms → breaks volume-surface balance
- Scale only descended terms (volume, pairing, Wigner) by Vol ratio → 0.17% MAE (worse)
- Frobenius-Schur indicator for pairing → always positive (wrong object)
- Hopf CS chirality for pairing → correct for ee/oo, breaks eo nuclei

### The correct approach

Each nuclear knot type needs its OWN coefficient set derived from its braid word:
- **Borromean B₃** (A≥4): current 11 terms, 0.025% MAE ✓
- **Figure-eight 4₁** (A=3): NEW coefficients needed
- **Satellite** (A=2): deuteron — the exact NF trace gives B=2.225 MeV (0.6 keV accuracy)
- **Unknot** (A=1): trivial, B=0

## CONTEXT: Read these propositions first

**Priority order** (read these to understand the framework):

1. `def:mass-identity` — the foundational categorical mass definition
   - Path: `lifting-and-descent/mass-identity.md`
   - 𝔪(ϱ) = ‖tr((∫_A ⊗ id) ∘ Δ ∘ ϱ)‖

2. `thm:topological-mass` — the topological decomposition
   - Path: `braids-and-knots/topological-mass.md`
   - Descent involution splits mass into base holonomy + divisors

3. `prop:topological-mass-formula` — the archimedean specialization
   - Path: `braids-and-knots/topological-mass-formula.md`
   - 𝔪(K) = Vol(K)/ℏ_q² for hyperbolic knots

4. `thm:wedderburn-mass-formula` — the three-invariant formula
   - Path: `braids-and-knots/wedderburn-mass-formula.md`
   - M = M_free + α(Φ₁ - 2[3]Φ₂ + h²Φ₃)

5. `prop:q-integer-mass-formula` — the 7-term BW with q-integer coefficients
   - Path: `particle-interactions/q-integer-mass-formula.md`
   - All coefficients as [n]_q products × m_e

6. `prop:bw-categorical-descent` — BW = descent decomposition
   - Path: `particle-interactions/bw-categorical-descent.md`
   - Descended (Casimirs) + Transient (divisors)

7. `prop:wedderburn-trace-identity` — Σ dim_q(λ)² = [n]_q!
   - Path: `braids-and-knots/wedderburn-trace-identity.md`
   - WHY the Wigner coefficient = [5]_q!

8. `prop:hook-weight-derivation` — β₄ from [2,2] partition
   - Path: `braids-and-knots/hook-weight-derivation.md`
   - Hook invisible at pair level, needs triple character

9. `prop:nuclear-knot-classification` — **NEW from this session**
   - Path: `braids-and-knots/nuclear-knot-classification.md`
   - A=3 → figure-eight, A≥4 → Borromean

10. `prop:em-coupling-chern-simons` — **NEW from this session**
    - Path: `descartes-universe/em-coupling-chern-simons.md`
    - 1/α with CS + Gram κ = 137.035944 (399 ppb)

11. `prop:em-coupling-projection` — the three-layer α derivation
    - Path: `descartes-universe/em-coupling-projection.md`
    - α = q⁻¹/([9]·[10]) from R-matrix eigenvalue

12. `def:categorical-proton`, `def:categorical-neutron` — nucleon definitions
    - Path: `descartes-universe/categorical-proton.md`, `categorical-neutron.md`
    - B₃(u,u,d) and B₃(u,d,d) with typed crossings

## CURRENT RESULTS

### Masses (11-term BW, zero fitted parameters)

```
MAE = 0.025% across 48 isotopes (H through U)
Best:  ⁵¹V at 0.0007% (0.3 MeV)
Worst: ³He at 0.25% (6.9 MeV) ← needs figure-eight coefficients
```

### Fine structure constant

```
1/α = q·[9]·[10] × (1 + c₁ + c₁²·κ) = 137.035944
CODATA: 137.035999
Error: 399 ppb (0.00004%)
```

### Key formulas in hecke_core.py

- `binding_energy_bw(Z, N, k=5)` — 11-term BW formula
- `binding_energy_derived(Z, N)` — exact NF trace (works for D)
- `binding_energy_physical(Z, N)` — BW + QED + q-torsion
- `classify_nuclear_knot(Z, N)` — returns (α_scale, knot_name, is_hyperbolic)
- `build_atom_nf(Z, N)` — full NF of nuclear braid in H₃(q)
- `build_nucleon_nf(quarks)` — single nucleon NF
- `ALPHA_EM_INV_DERIVED` — the CS+Gram corrected 1/α

### Character engine (hecke_characters.py)

- `build_seminormal_matrices(shape)` — exact rep matrices for any partition
- `compute_mass_at_level(Z, N, k)` — character computation at level k
- Verified k=5 through k=11, all Hecke relations pass

### Key constants

```
q₀ = 1.109978595554181
ℏ_q = 0.099082
Vol(4₁) = 2.029883 (figure-eight, defines q₀)
Vol(B₃) = 7.327725 = 8G (Borromean, binding scale for A≥4)
α = m_e × Vol(B₃) = 3.7445 MeV (Borromean binding scale)
```

## OPEN QUESTIONS (ranked)

1. **Figure-eight BW coefficients** — PRIMARY TASK
2. **Content blocks** — 8 propositions need .ts+.md+.lean (partially done)
3. **Magic numbers** — {2,8,20,28,50,82,126} from Bring's surface
4. **Energy scale E₀** — calibrated, not independently derived
5. **Neutrino mass** — wrong by 10⁶
6. **Molecular binding** — H-H works, others don't
7. **1/α remaining 399 ppb** — J³ correction (Massey products?)

## BRANCH

`claude/update-computations-math-Skr0C`
