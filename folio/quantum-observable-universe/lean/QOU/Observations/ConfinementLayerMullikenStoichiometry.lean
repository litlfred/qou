/-
Copyright (c) 2026 Quantum Observable Universe Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization
-/
import ToricConicOpt.ConfinementLayerTower
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases

/-!
# Multi-Layer Confinement Composition, Fenchel–Legendre Mulliken Subdifferentials & Smith/Birch Stoichiometry

Extends `ToricConicOpt.ConfinementLayerTower` (`qou-5lct`) inside the canonical
`QOU.Observations` chapter subgraph with non-duplicative algebraic, variational, and
integer-lattice theorems stated purely over generic commutative rings (`[CommRing K]`)
and strict ordered commutative rings (`[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]`)
with zero field binders or division tactics (§7c, `qou-8318`):

## Main Declarations

1. **Multi-Step `promoteLayer` Composition & Five-Layer Adiabatic Telescoping:**
   - `compositeMotifs`, `expandMotifs_comp`, `promoteLayer_two_step_charge_and_kernel`:
     Associativity of `expandMotifs` across consecutive layer promotions `L₀ ⇝ L₁ ⇝ L₂` and
     transitivity of conserved-charge and Diophantine-kernel lifting.
   - `five_layer_adiabatic_telescoping_product`:
     Division-free telescoping identity `Δ₄ = Δ₀ * (η₀ * η₁ * η₂ * η₃)` for `Δ_{k+1} = Δ_k * η_k`
     and strict scale hierarchy `0 < Δ₄ < Δ₃ < Δ₂ < Δ₁ < Δ₀` with `0 < η₀ * η₁ * η₂ * η₃ < 1`
     whenever `0 < Δ₀` and each adiabatic factor lies in `(0, 1)`.

2. **Layer-3 Fenchel–Legendre Subdifferential, Charge-Transfer Minimizer & Shell-Closure Kink:**
   - `twoMullikenElectronegativity` & `fenchel_subgradient_interval_iff_mulliken_hardness`:
     Discrete Fenchel–Legendre subgradients `μ` of `E(N)` on `{N - 1, N, N + 1}` coincide
     with `[-I(N), -A_ea(N)] = [shadowSlopeMinus E N, shadowSlopePlus E N]`; doubled subgradients
     exist iff `0 ≤ parrPearsonHardness E N`, with `-twoMullikenElectronegativity E N` at exact
     symmetric distance `parrPearsonHardness E N` from `2 * shadowSlopeMinus E N` and
     `2 * shadowSlopePlus E N`.
   - `twoChargeTransferQuad` & `parr_pearson_charge_transfer_minimizer`:
     Division-free completing-the-square identity
     `(η_A + η_B) * (2 ΔE(δN)) + (χ_A - χ_B)² = ((η_A + η_B) * δN + (χ_A - χ_B))²`,
     unconditional Sanderson–Parr lower bound `-(χ_A - χ_B)² ≤ (η_A + η_B) * (2 ΔE(δN))`,
     and exact global optimality at any stationary transfer `(η_A + η_B) * δN* = χ_B - χ_A`.
   - `two_shell_piecewise_hardness_kink`:
     Piecewise-linear two-shell orbital envelope exhibiting `η_PP(C₁) = ε₁ - ε₂` and
     `2 χ_M(C₁) = ε₁ + ε₂` at shell closure `N = C₁` (`2, 10, 18, 36`) versus `η_PP(N) = 0`
     and `2 χ_M(N) = 2 * ε₂` inside an unscreened open shell `C₁ + 1 ≤ N`.

3. **Layer-4 Unimodular `SNF(A_CHO) = diag(1, 1, 2)` & Birch Toric Hessian Convexity:**
   - `cho_smith_normal_form_diag_1_1_2`:
     Explicit unimodular `GL₃(ℤ)` and `GL₇(ℤ)` factorizations certifying
     `U * A_CHO * V = diag(1, 1, 2)` (capturing the prime-`2` hydrogen parity invariant factor).
   - `birch_hessian_quad_form_sum_sq_and_pos`:
     Exact weighted sum-of-squares decomposition of the Birch Legendre Hessian
     `ξᵀ (A diag(x) Aᵀ) ξ = ∑_j x_j (Aᵀ ξ)_j²` and strict positivity for `x > 0`, `Aᵀ ξ ≠ 0`.

## References
- [mulliken1934] R. S. Mulliken, *J. Chem. Phys.* 2 (1934), 782–793
- [perdew-parr-levy-balduz1982] J. P. Perdew, R. G. Parr, M. Levy, J. L. Balduz, *Phys. Rev. Lett.* 49 (1982), 1691
- [parr-pearson1983] R. G. Parr, R. G. Pearson, *J. Am. Chem. Soc.* 105 (1983), 7512–7516
- [deloera-hemmecke-koeppe2013] J. A. De Loera, R. Hemmecke, M. Köppe, *Algebraic and Geometric Ideas in the Theory of Discrete Optimization* (2013)
- [birch1963] M. W. Birch, *J. Roy. Statist. Soc. Ser. B* 25 (1963), 220–233
-/

set_option autoImplicit false

namespace QOU.Observations.ConfinementLayerMullikenStoichiometry

open scoped BigOperators
open QOU.MathlibInfra.ConfinementLayerTower

/-! ## 1. Multi-Step `promoteLayer` Composition & Five-Layer Adiabatic Telescoping -/

section TowerComposition

/-- Composite motif-expansion table sending a Layer-`(k+2)` column `β : Fin m₂` directly to its
constituent Layer-`k` multiplicities `∑ α, motifs₁₂ β α * motifs₀₁ α j`. -/
def compositeMotifs {m₀ m₁ m₂ : ℕ}
    (motifs₀₁ : Fin m₁ → (Fin m₀ → ℕ))
    (motifs₁₂ : Fin m₂ → (Fin m₁ → ℕ)) : Fin m₂ → (Fin m₀ → ℕ) :=
  fun β j => ∑ α : Fin m₁, motifs₁₂ β α * motifs₀₁ α j

/-- Associativity of `expandMotifs` across two consecutive promotions `L₀ ⇝ L₁ ⇝ L₂`. -/
theorem expandMotifs_comp {m₀ m₁ m₂ : ℕ}
    (motifs₀₁ : Fin m₁ → (Fin m₀ → ℕ))
    (motifs₁₂ : Fin m₂ → (Fin m₁ → ℕ))
    (v : Fin m₂ → ℤ) :
    expandMotifs motifs₀₁ (expandMotifs motifs₁₂ v) =
      expandMotifs (compositeMotifs motifs₀₁ motifs₁₂) v := by
  funext j
  simp only [expandMotifs, compositeMotifs, Nat.cast_sum, Nat.cast_mul]
  calc
    (∑ α : Fin m₁, (∑ β : Fin m₂, v β * (motifs₁₂ β α : ℤ)) * (motifs₀₁ α j : ℤ))
        = ∑ α : Fin m₁, ∑ β : Fin m₂, v β * ((motifs₁₂ β α : ℤ) * (motifs₀₁ α j : ℤ)) := by
          refine Finset.sum_congr rfl ?_
          intro α _
          rw [Finset.sum_mul]
          refine Finset.sum_congr rfl ?_
          intro β _
          ring
    _ = ∑ β : Fin m₂, ∑ α : Fin m₁, v β * ((motifs₁₂ β α : ℤ) * (motifs₀₁ α j : ℤ)) :=
          Finset.sum_comm
    _ = ∑ β : Fin m₂, v β * ∑ α : Fin m₁, (motifs₁₂ β α : ℤ) * (motifs₀₁ α j : ℤ) := by
          refine Finset.sum_congr rfl ?_
          intro β _
          rw [← Finset.mul_sum]

/-- Transitive conserved-charge and integer-kernel lifting across two consecutive
`promoteLayer` steps `L₀ ⇝ L₁ ⇝ L₂`. -/
theorem promoteLayer_two_step_charge_and_kernel {d m₀ m₁ m₂ : ℕ} {K : Type*} [CommRing K]
    (L₀ : ConfinementLayer d m₀ K)
    (motifs₀₁ : Fin m₁ → (Fin m₀ → ℕ)) (δc₀₁ : Fin m₁ → K) (adm₁ : (Fin m₁ → ℕ) → Prop)
    (motifs₁₂ : Fin m₂ → (Fin m₁ → ℕ)) (δc₁₂ : Fin m₂ → K) (adm₂ : (Fin m₂ → ℕ) → Prop)
    (v : Fin m₂ → ℤ) :
    let L₁ := promoteLayer L₀ motifs₀₁ δc₀₁ adm₁
    let L₂ := promoteLayer L₁ motifs₁₂ δc₁₂ adm₂
    Matrix.mulVec L₂.A v = Matrix.mulVec L₀.A (expandMotifs (compositeMotifs motifs₀₁ motifs₁₂) v) ∧
      (Matrix.mulVec L₂.A v = 0 →
        Matrix.mulVec L₀.A (expandMotifs (compositeMotifs motifs₀₁ motifs₁₂) v) = 0) := by
  dsimp only
  have h12 := promoteLayer_charge_conservation (promoteLayer L₀ motifs₀₁ δc₀₁ adm₁) motifs₁₂ δc₁₂ adm₂ v
  have h01 := promoteLayer_charge_conservation L₀ motifs₀₁ δc₀₁ adm₁ (expandMotifs motifs₁₂ v)
  have hchain :
      Matrix.mulVec (promoteLayer (promoteLayer L₀ motifs₀₁ δc₀₁ adm₁) motifs₁₂ δc₁₂ adm₂).A v =
        Matrix.mulVec L₀.A (expandMotifs (compositeMotifs motifs₀₁ motifs₁₂) v) := by
    rw [h12, h01, expandMotifs_comp]
  exact ⟨hchain, fun hv => by rw [← hchain, hv]⟩

/-- Division-free five-layer telescoping scale identity and strict hierarchy over any strict
ordered commutative ring: when `0 < Δ₀` and each adjacent factor `η_k` (`k = 0..3`) satisfies
`0 < η_k < 1` with `Δ_{k+1} = Δ_k * η_k`, then `Δ₄ = Δ₀ * (η₀ * η₁ * η₂ * η₃)`,
`0 < Δ₄ < Δ₃ < Δ₂ < Δ₁ < Δ₀`, and `0 < η₀ * η₁ * η₂ * η₃ < 1`. -/
theorem five_layer_adiabatic_telescoping_product
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (Δ₀ Δ₁ Δ₂ Δ₃ Δ₄ η₀ η₁ η₂ η₃ : K)
    (hΔ₀ : 0 < Δ₀)
    (hη₀_pos : 0 < η₀) (hη₀_lt : η₀ < 1) (h₀ : Δ₁ = Δ₀ * η₀)
    (hη₁_pos : 0 < η₁) (hη₁_lt : η₁ < 1) (h₁ : Δ₂ = Δ₁ * η₁)
    (hη₂_pos : 0 < η₂) (hη₂_lt : η₂ < 1) (h₂ : Δ₃ = Δ₂ * η₂)
    (hη₃_pos : 0 < η₃) (hη₃_lt : η₃ < 1) (h₃ : Δ₄ = Δ₃ * η₃) :
    Δ₄ = Δ₀ * (η₀ * η₁ * η₂ * η₃) ∧
      (0 < Δ₄ ∧ Δ₄ < Δ₃ ∧ Δ₃ < Δ₂ ∧ Δ₂ < Δ₁ ∧ Δ₁ < Δ₀) ∧
      (0 < η₀ * η₁ * η₂ * η₃ ∧ η₀ * η₁ * η₂ * η₃ < 1) := by
  have htel : Δ₄ = Δ₀ * (η₀ * η₁ * η₂ * η₃) := by
    rw [h₃, h₂, h₁, h₀]
    ring
  have hΔ₁ : 0 < Δ₁ := by rw [h₀]; exact mul_pos hΔ₀ hη₀_pos
  have hΔ₂ : 0 < Δ₂ := by rw [h₁]; exact mul_pos hΔ₁ hη₁_pos
  have hΔ₃ : 0 < Δ₃ := by rw [h₂]; exact mul_pos hΔ₂ hη₂_pos
  have hΔ₄ : 0 < Δ₄ := by rw [h₃]; exact mul_pos hΔ₃ hη₃_pos
  have hlt₀ : Δ₁ < Δ₀ := by
    calc Δ₁ = Δ₀ * η₀ := h₀
      _ < Δ₀ * 1 := mul_lt_mul_of_pos_left hη₀_lt hΔ₀
      _ = Δ₀ := mul_one Δ₀
  have hlt₁ : Δ₂ < Δ₁ := by
    calc Δ₂ = Δ₁ * η₁ := h₁
      _ < Δ₁ * 1 := mul_lt_mul_of_pos_left hη₁_lt hΔ₁
      _ = Δ₁ := mul_one Δ₁
  have hlt₂ : Δ₃ < Δ₂ := by
    calc Δ₃ = Δ₂ * η₂ := h₂
      _ < Δ₂ * 1 := mul_lt_mul_of_pos_left hη₂_lt hΔ₂
      _ = Δ₂ := mul_one Δ₂
  have hlt₃ : Δ₄ < Δ₃ := by
    calc Δ₄ = Δ₃ * η₃ := h₃
      _ < Δ₃ * 1 := mul_lt_mul_of_pos_left hη₃_lt hΔ₃
      _ = Δ₃ := mul_one Δ₃
  have hp01_pos : 0 < η₀ * η₁ := mul_pos hη₀_pos hη₁_pos
  have hp012_pos : 0 < η₀ * η₁ * η₂ := mul_pos hp01_pos hη₂_pos
  have hprod_pos : 0 < η₀ * η₁ * η₂ * η₃ := mul_pos hp012_pos hη₃_pos
  have hp01_lt : η₀ * η₁ < 1 := by
    calc η₀ * η₁ < 1 * η₁ := mul_lt_mul_of_pos_right hη₀_lt hη₁_pos
      _ = η₁ := one_mul η₁
      _ < 1 := hη₁_lt
  have hp012_lt : η₀ * η₁ * η₂ < 1 := by
    calc η₀ * η₁ * η₂ < 1 * η₂ := mul_lt_mul_of_pos_right hp01_lt hη₂_pos
      _ = η₂ := one_mul η₂
      _ < 1 := hη₂_lt
  have hprod_lt : η₀ * η₁ * η₂ * η₃ < 1 := by
    calc η₀ * η₁ * η₂ * η₃ < 1 * η₃ := mul_lt_mul_of_pos_right hp012_lt hη₃_pos
      _ = η₃ := one_mul η₃
      _ < 1 := hη₃_lt
  exact ⟨htel, ⟨hΔ₄, hlt₃, hlt₂, hlt₁, hlt₀⟩, ⟨hprod_pos, hprod_lt⟩⟩

end TowerComposition

/-! ## 2. Layer-3 Fenchel–Legendre Subdifferential, Charge Transfer & Shell-Closure Kink -/

section LayerThreeMullikenHardness

/-- Division-free doubled Mulliken electronegativity
`2 χ_M(N) := I(N) + A_ea(N) = E(N - 1) - E(N + 1)` over any commutative ring `K` (§7c). -/
def twoMullikenElectronegativity {K : Type*} [CommRing K] (E : ℕ → K) (N : ℕ) : K :=
  ionizationEnergy E N + electronAffinity E N

/-- Exact division-free discrete Fenchel–Legendre subdifferential characterization of Mulliken
electronegativity and Parr–Pearson chemical hardness over any strict ordered commutative ring:
1. `μ` satisfies `E(N) + μ ≤ E(N + 1)` and `E(N) - μ ≤ E(N - 1)` iff
   `shadowSlopeMinus E N ≤ μ ∧ μ ≤ shadowSlopePlus E N`,
2. Doubled subgradients `two_μ` (`2 E(N) + two_μ ≤ 2 E(N + 1)` and `2 E(N) - two_μ ≤ 2 E(N - 1)`)
   exist iff `0 ≤ parrPearsonHardness E N`,
3. Whenever `0 ≤ parrPearsonHardness E N`, `-twoMullikenElectronegativity E N` satisfies the
   doubled subgradient bounds and lies at equal distance `parrPearsonHardness E N` from both
   `2 * shadowSlopeMinus E N` and `2 * shadowSlopePlus E N`. -/
theorem fenchel_subgradient_interval_iff_mulliken_hardness
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (E : ℕ → K) (N : ℕ) :
    (∀ μ : K,
      (E N + μ ≤ E (N + 1) ∧ E N - μ ≤ E (N - 1)) ↔
        (shadowSlopeMinus E N ≤ μ ∧ μ ≤ shadowSlopePlus E N)) ∧
    ((∃ two_μ : K,
      2 * E N + two_μ ≤ 2 * E (N + 1) ∧ 2 * E N - two_μ ≤ 2 * E (N - 1)) ↔
      0 ≤ parrPearsonHardness E N) ∧
    (0 ≤ parrPearsonHardness E N →
      (2 * E N + (-twoMullikenElectronegativity E N) ≤ 2 * E (N + 1) ∧
        2 * E N - (-twoMullikenElectronegativity E N) ≤ 2 * E (N - 1)) ∧
      2 * shadowSlopePlus E N - (-twoMullikenElectronegativity E N) =
        parrPearsonHardness E N ∧
      (-twoMullikenElectronegativity E N) - 2 * shadowSlopeMinus E N =
        parrPearsonHardness E N) := by
  have hiff : ∀ μ : K,
      (E N + μ ≤ E (N + 1) ∧ E N - μ ≤ E (N - 1)) ↔
        (shadowSlopeMinus E N ≤ μ ∧ μ ≤ shadowSlopePlus E N) := by
    intro μ
    simp only [shadowSlopeMinus, shadowSlopePlus]
    constructor
    · rintro ⟨hp, hm⟩
      exact ⟨by linarith, by linarith⟩
    · rintro ⟨hm, hp⟩
      exact ⟨by linarith, by linarith⟩
  have hmid_hi :
      2 * shadowSlopePlus E N - (-twoMullikenElectronegativity E N) =
        parrPearsonHardness E N := by
    simp only [shadowSlopePlus, twoMullikenElectronegativity, parrPearsonHardness,
      ionizationEnergy, electronAffinity]
    ring
  have hmid_lo :
      (-twoMullikenElectronegativity E N) - 2 * shadowSlopeMinus E N =
        parrPearsonHardness E N := by
    simp only [shadowSlopeMinus, twoMullikenElectronegativity, parrPearsonHardness,
      ionizationEnergy, electronAffinity]
    ring
  have hmem_of_nonneg : 0 ≤ parrPearsonHardness E N →
      2 * E N + (-twoMullikenElectronegativity E N) ≤ 2 * E (N + 1) ∧
        2 * E N - (-twoMullikenElectronegativity E N) ≤ 2 * E (N - 1) := by
    intro hpp
    have hp_id :
        2 * E (N + 1) - (2 * E N + (-twoMullikenElectronegativity E N)) =
          parrPearsonHardness E N := by
      simp only [twoMullikenElectronegativity, parrPearsonHardness,
        ionizationEnergy, electronAffinity]
      ring
    have hm_id :
        2 * E (N - 1) - (2 * E N - (-twoMullikenElectronegativity E N)) =
          parrPearsonHardness E N := by
      simp only [twoMullikenElectronegativity, parrPearsonHardness,
        ionizationEnergy, electronAffinity]
      ring
    exact ⟨by linarith, by linarith⟩
  refine ⟨hiff, ?_, fun hpp => ⟨hmem_of_nonneg hpp, hmid_hi, hmid_lo⟩⟩
  constructor
  · rintro ⟨two_μ, hp, hm⟩
    rw [parr_pearson_hardness_eq_second_diff]
    linarith
  · intro hpp
    exact ⟨-twoMullikenElectronegativity E N, hmem_of_nonneg hpp⟩

/-- Division-free doubled Parr–Pearson two-species charge-transfer energy
`2 ΔE(δN) := 2 (χ_A - χ_B) δN + (η_A + η_B) δN²` over any commutative ring `K` (§7c). -/
def twoChargeTransferQuad {K : Type*} [CommRing K] (χ_A χ_B η_A η_B δN : K) : K :=
  2 * (χ_A - χ_B) * δN + (η_A + η_B) * δN ^ 2

/-- Division-free completing-the-square global minimizer and Sanderson–Parr stabilization energy
for two-species charge transfer over any strict ordered commutative ring when `0 < η_A + η_B`:
1. `(η_A + η_B) * twoChargeTransferQuad(δN) + (χ_A - χ_B)² = ((η_A + η_B) * δN + (χ_A - χ_B))²`,
2. Unconditional lower bound `-(χ_A - χ_B)² ≤ (η_A + η_B) * twoChargeTransferQuad(δN)`,
3. For any stationary transfer `(η_A + η_B) * δN* = χ_B - χ_A`,
   `(η_A + η_B) * twoChargeTransferQuad(δN*) = -(χ_A - χ_B)²`, `twoChargeTransferQuad(δN*) ≤ 0`,
   and `twoChargeTransferQuad(δN) - twoChargeTransferQuad(δN*) = (η_A + η_B) * (δN - δN*)² ≥ 0`. -/
theorem parr_pearson_charge_transfer_minimizer
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (χ_A χ_B η_A η_B : K) (hη : 0 < η_A + η_B) :
    (∀ δN : K,
      (η_A + η_B) * twoChargeTransferQuad χ_A χ_B η_A η_B δN + (χ_A - χ_B) ^ 2 =
        ((η_A + η_B) * δN + (χ_A - χ_B)) ^ 2) ∧
    (∀ δN : K,
      -(χ_A - χ_B) ^ 2 ≤ (η_A + η_B) * twoChargeTransferQuad χ_A χ_B η_A η_B δN) ∧
    (∀ δN_star : K, (η_A + η_B) * δN_star = χ_B - χ_A →
      (η_A + η_B) * twoChargeTransferQuad χ_A χ_B η_A η_B δN_star = -(χ_A - χ_B) ^ 2 ∧
      twoChargeTransferQuad χ_A χ_B η_A η_B δN_star ≤ 0 ∧
      (∀ δN : K,
        twoChargeTransferQuad χ_A χ_B η_A η_B δN -
            twoChargeTransferQuad χ_A χ_B η_A η_B δN_star =
          (η_A + η_B) * (δN - δN_star) ^ 2) ∧
      (∀ δN : K,
        twoChargeTransferQuad χ_A χ_B η_A η_B δN_star ≤
          twoChargeTransferQuad χ_A χ_B η_A η_B δN)) := by
  have hcs : ∀ δN : K,
      (η_A + η_B) * twoChargeTransferQuad χ_A χ_B η_A η_B δN + (χ_A - χ_B) ^ 2 =
        ((η_A + η_B) * δN + (χ_A - χ_B)) ^ 2 := by
    intro δN
    unfold twoChargeTransferQuad
    ring
  have hlb : ∀ δN : K,
      -(χ_A - χ_B) ^ 2 ≤ (η_A + η_B) * twoChargeTransferQuad χ_A χ_B η_A η_B δN := by
    intro δN
    have hid := hcs δN
    have hnn : 0 ≤ ((η_A + η_B) * δN + (χ_A - χ_B)) ^ 2 := sq_nonneg _
    linarith
  refine ⟨hcs, hlb, ?_⟩
  intro δN_star hstar
  have hval :
      (η_A + η_B) * twoChargeTransferQuad χ_A χ_B η_A η_B δN_star = -(χ_A - χ_B) ^ 2 := by
    have hid := hcs δN_star
    rw [hstar] at hid
    have hzero : ((χ_B - χ_A) + (χ_A - χ_B)) ^ 2 = 0 := by ring
    linarith
  have hnonpos : twoChargeTransferQuad χ_A χ_B η_A η_B δN_star ≤ 0 := by
    by_contra hpos
    push_neg at hpos
    have hmpos : 0 < (η_A + η_B) * twoChargeTransferQuad χ_A χ_B η_A η_B δN_star :=
      mul_pos hη hpos
    have hsqnn : 0 ≤ (χ_A - χ_B) ^ 2 := sq_nonneg (χ_A - χ_B)
    linarith
  have hdiff_sq : ∀ δN : K,
      twoChargeTransferQuad χ_A χ_B η_A η_B δN -
          twoChargeTransferQuad χ_A χ_B η_A η_B δN_star =
        (η_A + η_B) * (δN - δN_star) ^ 2 := by
    intro δN
    have hpoly :
        (twoChargeTransferQuad χ_A χ_B η_A η_B δN -
            twoChargeTransferQuad χ_A χ_B η_A η_B δN_star) -
          (η_A + η_B) * (δN - δN_star) ^ 2 =
        2 * ((η_A + η_B) * δN_star - (χ_B - χ_A)) * (δN - δN_star) := by
      unfold twoChargeTransferQuad
      ring
    have hvan : (η_A + η_B) * δN_star - (χ_B - χ_A) = 0 := sub_eq_zero.mpr hstar
    rw [hvan, mul_zero, zero_mul] at hpoly
    exact sub_eq_zero.mp hpoly
  refine ⟨hval, hnonpos, hdiff_sq, ?_⟩
  intro δN
  have hd := hdiff_sq δN
  have hnn : 0 ≤ (η_A + η_B) * (δN - δN_star) ^ 2 :=
    mul_nonneg (le_of_lt hη) (sq_nonneg (δN - δN_star))
  linarith

/-- Piecewise-linear two-shell atomic ground-state energy envelope with inner shell closure `C₁`,
inner orbital binding energy `ε₁`, and outer orbital binding energy `ε₂`. -/
def twoShellEnergy {K : Type*} [CommRing K] (E_core : K) (C₁ : ℕ) (ε₁ ε₂ : K) (N : ℕ) : K :=
  if N ≤ C₁ then
    E_core - (N : K) * ε₁
  else
    E_core - (C₁ : K) * ε₁ - ((N - C₁ : ℕ) : K) * ε₂

/-- Division-free noble-gas shell-closure kink theorem (`1 ≤ C₁`) over any `[CommRing K]`:
at the exact shell boundary `N = C₁` (`C₁ ∈ {2, 10, 18, 36}`), hardness jumps to `ε₁ - ε₂` and
doubled Mulliken electronegativity equals `ε₁ + ε₂`, whereas strictly inside the next unscreened
shell (`C₁ + 1 ≤ N`), hardness vanishes (`parrPearsonHardness = 0`) and doubled Mulliken
electronegativity equals `2 * ε₂`. -/
theorem two_shell_piecewise_hardness_kink {K : Type*} [CommRing K]
    (E_core : K) {C₁ : ℕ} (hC₁ : 1 ≤ C₁) (ε₁ ε₂ : K) :
    let E := twoShellEnergy E_core C₁ ε₁ ε₂
    ionizationEnergy E C₁ = ε₁ ∧
      electronAffinity E C₁ = ε₂ ∧
      parrPearsonHardness E C₁ = ε₁ - ε₂ ∧
      twoMullikenElectronegativity E C₁ = ε₁ + ε₂ ∧
      (∀ N : ℕ, C₁ + 1 ≤ N →
        parrPearsonHardness E N = 0 ∧ twoMullikenElectronegativity E N = 2 * ε₂) := by
  have hprev_le : C₁ - 1 ≤ C₁ := Nat.sub_le C₁ 1
  have hsucc_not_le : ¬ C₁ + 1 ≤ C₁ := by omega
  have hsub_cast : ((C₁ - 1 : ℕ) : K) = (C₁ : K) - 1 := by
    rw [Nat.cast_sub hC₁, Nat.cast_one]
  have hion : ionizationEnergy (twoShellEnergy E_core C₁ ε₁ ε₂) C₁ = ε₁ := by
    simp only [ionizationEnergy, twoShellEnergy, hprev_le, le_refl, ↓reduceIte, hsub_cast]
    ring
  have haff : electronAffinity (twoShellEnergy E_core C₁ ε₁ ε₂) C₁ = ε₂ := by
    have hdiff1 : C₁ + 1 - C₁ = 1 := by omega
    simp only [electronAffinity, twoShellEnergy, le_refl, hsucc_not_le, ↓reduceIte, hdiff1,
      Nat.cast_one]
    ring
  have hpp : parrPearsonHardness (twoShellEnergy E_core C₁ ε₁ ε₂) C₁ = ε₁ - ε₂ := by
    unfold parrPearsonHardness
    rw [hion, haff]
  have hmull : twoMullikenElectronegativity (twoShellEnergy E_core C₁ ε₁ ε₂) C₁ = ε₁ + ε₂ := by
    unfold twoMullikenElectronegativity
    rw [hion, haff]
  refine ⟨hion, haff, hpp, hmull, ?_⟩
  intro N hN
  have hN_not_le : ¬ N ≤ C₁ := by omega
  have hN1_not_le : ¬ N + 1 ≤ C₁ := by omega
  have hNp1_sub : ((N + 1 - C₁ : ℕ) : K) = ((N - C₁ : ℕ) : K) + 1 := by
    have heq : N + 1 - C₁ = (N - C₁) + 1 := by omega
    rw [heq, Nat.cast_add, Nat.cast_one]
  have hionN : ionizationEnergy (twoShellEnergy E_core C₁ ε₁ ε₂) N = ε₂ := by
    by_cases hcase : N - 1 ≤ C₁
    · have hNeq : N = C₁ + 1 := by omega
      subst hNeq
      have h1 : C₁ + 1 - 1 = C₁ := by omega
      have h2' : C₁ + 1 - C₁ = 1 := by omega
      simp only [ionizationEnergy, twoShellEnergy, h1, le_refl, hsucc_not_le, ↓reduceIte,
        h2', Nat.cast_one]
      ring
    · have hNm1_sub : ((N - 1 - C₁ : ℕ) : K) = ((N - C₁ : ℕ) : K) - 1 := by
        have hpos : 1 ≤ N - C₁ := by omega
        have heq : N - 1 - C₁ = (N - C₁) - 1 := by omega
        rw [heq, Nat.cast_sub hpos, Nat.cast_one]
      simp only [ionizationEnergy, twoShellEnergy, hcase, hN_not_le, ↓reduceIte, hNm1_sub]
      ring
  have haffN : electronAffinity (twoShellEnergy E_core C₁ ε₁ ε₂) N = ε₂ := by
    simp only [electronAffinity, twoShellEnergy, hN_not_le, hN1_not_le, ↓reduceIte, hNp1_sub]
    ring
  refine ⟨?_, ?_⟩
  · unfold parrPearsonHardness
    rw [hionN, haffN, sub_self]
  · unfold twoMullikenElectronegativity
    rw [hionN, haffN]
    ring

end LayerThreeMullikenHardness

/-! ## 3. Layer-4 Unimodular `SNF(A_CHO) = diag(1, 1, 2)` & Birch Toric Hessian Convexity -/

section LayerFourSmithAndBirch

/-- Left unimodular `GL₃(ℤ)` factor for the Smith normal form of `A_CHO`. -/
def choSmithU : Matrix (Fin 3) (Fin 3) ℤ :=
  ![![1, 0, 0],
    ![0, 0, 1],
    ![0, -1, 2]]

/-- Explicit integer inverse of `choSmithU` in `GL₃(ℤ)`. -/
def choSmithUInv : Matrix (Fin 3) (Fin 3) ℤ :=
  ![![1, 0, 0],
    ![0, 2, -1],
    ![0, 1, 0]]

/-- Right unimodular `GL₇(ℤ)` factor for the Smith normal form of `A_CHO`. -/
def choSmithV : Matrix (Fin 7) (Fin 7) ℤ :=
  ![![1, -1, 0, 2, 1, 1, -1],
    ![0, 1, -1, 0, 0, -1, -2],
    ![0, 0, 0, 1, 0, 0, 0],
    ![0, 1, 0, -2, -2, -1, 0],
    ![0, 0, 0, 0, 1, 0, 0],
    ![0, 0, 0, 0, 0, 1, 0],
    ![0, 0, 0, 0, 0, 0, 1]]

/-- Explicit integer inverse of `choSmithV` in `GL₇(ℤ)`. -/
def choSmithVInv : Matrix (Fin 7) (Fin 7) ℤ :=
  ![![1, 0, 0, 1, 1, 0, 1],
    ![0, 0, 2, 1, 2, 1, 0],
    ![0, -1, 2, 1, 2, 0, -2],
    ![0, 0, 1, 0, 0, 0, 0],
    ![0, 0, 0, 0, 1, 0, 0],
    ![0, 0, 0, 0, 0, 1, 0],
    ![0, 0, 0, 0, 0, 0, 1]]

/-- Canonical Smith normal form matrix `diag(1, 1, 2)` of `A_CHO` in `ℤ^{3 × 7}`. -/
def choSmithDiag : Matrix (Fin 3) (Fin 7) ℤ :=
  ![![1, 0, 0, 0, 0, 0, 0],
    ![0, 1, 0, 0, 0, 0, 0],
    ![0, 0, 2, 0, 0, 0, 0]]

/-- Unimodular Smith normal form certificate for the `3 × 7` C–H–O stoichiometry matrix `A_CHO`:
`choSmithU ∈ GL₃(ℤ)` and `choSmithV ∈ GL₇(ℤ)` satisfy `U * U⁻¹ = 1`, `U⁻¹ * U = 1`,
`V * V⁻¹ = 1`, `V⁻¹ * V = 1`, and `U * A_CHO * V = diag(1, 1, 2)`. -/
theorem cho_smith_normal_form_diag_1_1_2 :
    choSmithU * choSmithUInv = 1 ∧
      choSmithUInv * choSmithU = 1 ∧
      choSmithV * choSmithVInv = 1 ∧
      choSmithVInv * choSmithV = 1 ∧
      choSmithU * A_CHO * choSmithV = choSmithDiag := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;> decide
  · ext i j; fin_cases i <;> fin_cases j <;> decide
  · ext i j; fin_cases i <;> fin_cases j <;> decide
  · ext i j; fin_cases i <;> fin_cases j <;> decide
  · ext i j; fin_cases i <;> fin_cases j <;> decide

/-- Birch mass-action Legendre Hessian quadratic form `ξᵀ (A diag(x) Aᵀ) ξ`. -/
def birchHessianQuad {E M : ℕ} {K : Type*} [CommRing K]
    (A : Matrix (Fin E) (Fin M) ℤ) (x : Fin M → K) (ξ : Fin E → K) : K :=
  ∑ e₁ : Fin E, ∑ e₂ : Fin E,
    ξ e₁ * (∑ j : Fin M, (A e₁ j : K) * (A e₂ j : K) * x j) * ξ e₂

/-- Exact weighted sum-of-squares decomposition and strict positive-definiteness of the Birch
toric Legendre Hessian quadratic form over any strict ordered commutative ring:
1. `birchHessianQuad A x ξ = ∑_j x_j * (∑_e A_{e,j} ξ_e)²`,
2. For positive concentrations `x_j > 0` (`∀ j`) and any direction `ξ` with `(Aᵀ ξ)_{j₀} ≠ 0`,
   `0 < birchHessianQuad A x ξ`. -/
theorem birch_hessian_quad_form_sum_sq_and_pos
    {E M : ℕ} {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (A : Matrix (Fin E) (Fin M) ℤ) (x : Fin M → K) (ξ : Fin E → K) :
    birchHessianQuad A x ξ =
        (∑ j : Fin M, x j * (∑ e : Fin E, (A e j : K) * ξ e) ^ 2) ∧
      ((∀ j : Fin M, 0 < x j) →
        (∃ j₀ : Fin M, (∑ e : Fin E, (A e j₀ : K) * ξ e) ≠ 0) →
          0 < birchHessianQuad A x ξ) := by
  have hsos :
      birchHessianQuad A x ξ =
        ∑ j : Fin M, x j * (∑ e : Fin E, (A e j : K) * ξ e) ^ 2 := by
    unfold birchHessianQuad
    have hstep1 :
        (∑ e₁ : Fin E, ∑ e₂ : Fin E,
            ξ e₁ * (∑ j : Fin M, (A e₁ j : K) * (A e₂ j : K) * x j) * ξ e₂) =
          ∑ e₁ : Fin E, ∑ e₂ : Fin E, ∑ j : Fin M,
            x j * (((A e₁ j : K) * ξ e₁) * ((A e₂ j : K) * ξ e₂)) := by
      refine Finset.sum_congr rfl ?_
      intro e₁ _
      refine Finset.sum_congr rfl ?_
      intro e₂ _
      rw [Finset.mul_sum, Finset.sum_mul]
      refine Finset.sum_congr rfl ?_
      intro j _
      ring
    rw [hstep1]
    have hswap1 :
        (∑ e₁ : Fin E, ∑ e₂ : Fin E, ∑ j : Fin M,
            x j * (((A e₁ j : K) * ξ e₁) * ((A e₂ j : K) * ξ e₂))) =
          ∑ j : Fin M, ∑ e₁ : Fin E, ∑ e₂ : Fin E,
            x j * (((A e₁ j : K) * ξ e₁) * ((A e₂ j : K) * ξ e₂)) := by
      calc
        (∑ e₁ : Fin E, ∑ e₂ : Fin E, ∑ j : Fin M,
            x j * (((A e₁ j : K) * ξ e₁) * ((A e₂ j : K) * ξ e₂)))
            = ∑ e₁ : Fin E, ∑ j : Fin M, ∑ e₂ : Fin E,
                x j * (((A e₁ j : K) * ξ e₁) * ((A e₂ j : K) * ξ e₂)) := by
              refine Finset.sum_congr rfl ?_
              intro e₁ _
              exact Finset.sum_comm
        _ = ∑ j : Fin M, ∑ e₁ : Fin E, ∑ e₂ : Fin E,
              x j * (((A e₁ j : K) * ξ e₁) * ((A e₂ j : K) * ξ e₂)) := Finset.sum_comm
    rw [hswap1]
    refine Finset.sum_congr rfl ?_
    intro j _
    calc
      (∑ e₁ : Fin E, ∑ e₂ : Fin E,
          x j * (((A e₁ j : K) * ξ e₁) * ((A e₂ j : K) * ξ e₂)))
          = x j * ∑ e₁ : Fin E, ∑ e₂ : Fin E,
              ((A e₁ j : K) * ξ e₁) * ((A e₂ j : K) * ξ e₂) := by
            rw [Finset.mul_sum]
            refine Finset.sum_congr rfl ?_
            intro e₁ _
            rw [Finset.mul_sum]
      _ = x j * ((∑ e₁ : Fin E, (A e₁ j : K) * ξ e₁) *
            (∑ e₂ : Fin E, (A e₂ j : K) * ξ e₂)) := by
            congr 1
            rw [Finset.sum_mul]
            refine Finset.sum_congr rfl ?_
            intro e₁ _
            rw [Finset.mul_sum]
      _ = x j * (∑ e : Fin E, (A e j : K) * ξ e) ^ 2 := by
            ring
  refine ⟨hsos, ?_⟩
  rintro hx ⟨j₀, hj₀⟩
  rw [hsos]
  have hterm_pos : 0 < x j₀ * (∑ e : Fin E, (A e j₀ : K) * ξ e) ^ 2 :=
    mul_pos (hx j₀) (sq_pos_of_ne_zero hj₀)
  have hterm_nonneg : ∀ j ∈ (Finset.univ : Finset (Fin M)),
      0 ≤ x j * (∑ e : Fin E, (A e j : K) * ξ e) ^ 2 :=
    fun j _ => mul_nonneg (le_of_lt (hx j)) (sq_nonneg _)
  exact lt_of_lt_of_le hterm_pos
    (Finset.single_le_sum hterm_nonneg (Finset.mem_univ j₀))

end LayerFourSmithAndBirch

end QOU.Observations.ConfinementLayerMullikenStoichiometry
