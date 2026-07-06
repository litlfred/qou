# Batch 4 Triage of Lean Stubs

This analysis catalogs exactly 10 new files containing sorry stubs in `/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/`.

## Selected Stubs

### 1. Archimedean/eos_borromean_cfl.lean
- **Relative Path**: `Archimedean/eos_borromean_cfl.lean`
- **Declaration**:
  ```lean
  theorem eos_borromean_cfl [ctx : EosBorromeanCflContext] :
      (ctx.ε_B = ctx.M_B * ctx.n_B +
        (3 / 5) * (ctx.hbar_q ^ 2 * (3 * Real.pi ^ 2) ^ ((2 : ℝ) / 3) /
          (2 * ctx.M_B)) * ctx.n_B ^ ((5 : ℝ) / 3) ∧
       ctx.P_B = (ctx.hbar_q ^ 2 * (3 * Real.pi ^ 2) ^ ((2 : ℝ) / 3) /
          (5 * ctx.M_B)) * ctx.n_B ^ ((5 : ℝ) / 3)) ∧
      ctx.P_D = (ctx.hbar_q ^ 2 * (3 * Real.pi ^ 2) ^ ((2 : ℝ) / 3) /
        (5 * ctx.M_D)) * (3 * ctx.n_B) ^ ((5 : ℝ) / 3) +
        3 * ctx.Δ_CFL ^ 2 * ctx.μ_q ^ 2 / Real.pi ^ 2 ∧
      ctx.P_D / ctx.P_B = (ctx.M_B / ctx.M_D) * (3 : ℝ) ^ ((5 : ℝ) / 3) +
        3 * ctx.Δ_CFL ^ 2 * ctx.μ_q ^ 2 / (Real.pi ^ 2 * ctx.P_B) :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `claim_i_borromean_eos : ε_B = M_B * n_B + (3 / 5) * (hbar_q ^ 2 * (3 * Real.pi ^ 2) ^ ((2 : ℝ) / 3) / (2 * M_B)) * n_B ^ ((5 : ℝ) / 3) ∧ P_B = (hbar_q ^ 2 * (3 * Real.pi ^ 2) ^ ((2 : ℝ) / 3) / (5 * M_B)) * n_B ^ ((5 : ℝ) / 3)`
  - `claim_ii_cfl_eos : P_D = (hbar_q ^ 2 * (3 * Real.pi ^ 2) ^ ((2 : ℝ) / 3) / (5 * M_D)) * (3 * n_B) ^ ((5 : ℝ) / 3) + 3 * Δ_CFL ^ 2 * μ_q ^ 2 / Real.pi ^ 2`
  - `claim_iii_stiffness_ratio : P_D / P_B = (M_B / M_D) * (3 : ℝ) ^ ((5 : ℝ) / 3) + 3 * Δ_CFL ^ 2 * μ_q ^ 2 / (Real.pi ^ 2 * P_B)`

### 2. Archimedean/genus_filtration_ideal.lean
- **Relative Path**: `Archimedean/genus_filtration_ideal.lean`
- **Declaration**:
  ```lean
  theorem genus_filtration_ideal [ctx : GenusFiltrationIdealContext] :
      ctx.genus = 4 ∧
      ctx.EvalMatrixRank = 5 ∧
      ctx.ideal_exponent = 5 ∧
      (∀ p : ℕ, 11 ≤ p → Nat.Prime p → Odd p → ctx.kills_T_2p p) :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `claim_i_genus_eq_four : genus = 4`
  - `claim_i_completeness_rank_five : EvalMatrixRank = 5`
  - `claim_ii_ideal_eq_u5 : ideal_exponent = 5`
  - `claim_iii_kills_higher_torus_knots : ∀ p : ℕ, 11 ≤ p → Nat.Prime p → Odd p → kills_T_2p p`

### 3. Archimedean/genus_maximal_descent.lean
- **Relative Path**: `Archimedean/genus_maximal_descent.lean`
- **Declaration**:
  ```lean
  theorem genus_maximal_descent [ctx : GenusMaximalDescentContext] :
      ctx.genus = 4 ∧ ctx.aut_order ≤ 84 * (ctx.genus - 1) :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `claim_i_genus_eq_four : genus = 4`
  - `claim_ii_hurwitz_bound : aut_order ≤ 84 * (genus - 1)`

### 4. Archimedean/gram_weighted_qvalue.lean
- **Relative Path**: `Archimedean/gram_weighted_qvalue.lean`
- **Declaration**:
  ```lean
  theorem gram_weighted_qvalue [ctx : GramWeightedQvalueContext] :
      ctx.Q
        = (Finset.univ.sum (fun k : Fin ctx.N => ctx.w k * ctx.Δ k))
          * (ctx.N : ℝ) * ctx.m_e :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `claim_i_qvalue_formula : Q = (Finset.univ.sum (fun k : Fin N => w k * Δ k)) * (N : ℝ) * m_e`
  - `claim_ii_weights_sum_to_one : Finset.univ.sum (fun k : Fin N => w k) = 1`
  - `claim_iii_weights_nonneg : ∀ k : Fin N, 0 ≤ w k`

### 5. ArchimedeanUniverse/brings_euler_characteristic.lean
- **Relative Path**: `ArchimedeanUniverse/brings_euler_characteristic.lean`
- **Declaration**:
  ```lean
  theorem brings_euler_characteristic [ctx : BringsEulerCharacteristicContext] :
      ctx.g = 4 ∧ ctx.chi_A = 2 - 2 * (ctx.g : ℤ) ∧ ctx.chi_A = -6 :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `claim_brings_euler_characteristic : g = 4 ∧ chi_A = 2 - 2 * (g : ℤ) ∧ chi_A = -6`

### 6. ArchimedeanUniverse/brings_riemann_hurwitz.lean
- **Relative Path**: `ArchimedeanUniverse/brings_riemann_hurwitz.lean`
- **Declaration**:
  ```lean
  theorem brings_riemann_hurwitz [ctx : BringsRiemannHurwitzContext] :
      ctx.deg = 4 ∧ ctx.R_tot = 14 ∧ ctx.n_branch = 6 :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `claim_brings_riemann_hurwitz : deg = 4 ∧ R_tot = 14 ∧ n_branch = 6`

### 7. BraidKnot/geom_yekutieli_alignment.lean
- **Relative Path**: `BraidKnot/geom_yekutieli_alignment.lean`
- **Declaration**:
  There are two `sorry` containing declarations in this file. The primary theorem is:
  ```lean
  theorem geom_yekutieli_per_block_alignment {R : Type*} [CommRing R]
      [ctx : GeomYekutieliAlignmentContext R] :
      ctx.boundaryHolonomy = ctx.trM ∧
        ctx.massFactor = ctx.Geom * ctx.trM :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `geom_identity : Geom = Vol_q * hbar_q_inv ^ 2 + CS_q * hbar_q ^ 2`
  - `hyperbolic_implies_cs_zero : is_hyperbolic → CS_q = 0`
  - `torus_implies_vol_zero : is_torus → Vol_q = 0`
  - `trivial_implies_both_zero : is_trivial → Vol_q = 0 ∧ CS_q = 0`
  - `claim_iv_holonomy_equals_trM : boundaryHolonomy = trM`
  - `mass_factor_def : massFactor = Geom * boundaryHolonomy`

### 8. CategoricalReeb/ofWeightDecomposition.lean
- **Relative Path**: `CategoricalReeb/ofWeightDecomposition.lean`
- **Declaration**:
  ```lean
  theorem ofWeightDecomposition [ctx : OfWeightDecompositionContext] :
      ∀ x : ctx.CategoricalObj, ctx.Θ_A (ctx.ξ x) = 1 :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `claim_ofWeightDecomposition : ∀ x : CategoricalObj, Θ_A (ξ x) = 1`

### 9. CommutativeQOU/u1EquivariantReduction.lean
- **Relative Path**: `CommutativeQOU/u1EquivariantReduction.lean`
- **Declaration**:
  ```lean
  theorem u1EquivariantReduction [ctx : U1EquivariantReductionContext] :
      ctx.n_fixed_poles = 2 ∧ ctx.orbit_interval_length = Real.pi :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `claim_u1EquivariantReduction : n_fixed_poles = 2 ∧ orbit_interval_length = Real.pi`

### 10. FluidDynamics/discrete_vortex_spectrum.lean
- **Relative Path**: `FluidDynamics/discrete_vortex_spectrum.lean`
- **Declaration**:
  ```lean
  theorem discrete_vortex_spectrum [ctx : DiscreteVortexSpectrumContext] :
      (∀ k : ℕ, 1 ≤ k →
        ctx.λ k = (ctx.q_int k) ^ 2 * ctx.hbar_q / ctx.L_q ^ 2) ∧
      (∀ n : ℕ, ctx.E_level n =
        (ctx.hbar_q / (2 * ctx.I_q)) * (ctx.q_int n) * (ctx.q_int (n + 1))) ∧
      (∀ n n' : ℕ, (n + 1 = n' ∨ n' + 1 = n) →
        ctx.ΔE_trans n n' = ctx.E_level n' - ctx.E_level n) ∧
      (ctx.q = 1 → ∀ k : ℕ, ctx.q_int k = (k : ℝ)) :=
    sorry
  ```
- **Available Context Properties / Claims**:
  - `impl_discrete_eigenvalues : vortex_spectrum_discrete → ∀ k : ℕ, 1 ≤ k → λ k = (q_int k) ^ 2 * hbar_q / L_q ^ 2`
  - `impl_spin_levels : vortex_spectrum_discrete → ∀ n : ℕ, E_level n = (hbar_q / (2 * I_q)) * (q_int n) * (q_int (n + 1))`
  - `impl_ladder_transitions : vortex_spectrum_discrete → ∀ n n' : ℕ, (n + 1 = n' ∨ n' + 1 = n) → ΔE_trans n n' = E_level n' - E_level n`
  - `impl_classical_kelvin_limit : vortex_spectrum_discrete → (q = 1 → ∀ k : ℕ, q_int k = (k : ℝ))`
  - `spectrum_active : vortex_spectrum_discrete`
