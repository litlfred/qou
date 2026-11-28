/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Ring.Subring.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# The per-loop measure under Form B (bean `qou-l4t2`, owner ruling 2026-11-28)

Owner ruling (PR #9911): photon vertices on a fermion loop join by the signed bar-odd
rule, so each extra vertex pair contributes the scalar `−h²`, `h = q − q⁻¹`, at any
positions (`EmPhotonJoinRules.barOdd_eq`). The owner also picked the one-factor
measure for Form B (decision card, 2026-11-28).

Form B's ladder is `Π(α) = H α Σ_{k ≥ 0} (−h² α)^k` with `H = s μ₁`, `s = [2]_q`.
Its `L`-loop coefficient is `c_L = s μ₁ (−h²)^(L−1)`.

## Results

1. `formB_coeff_succ`: `c_{L+1} = −h² c_L`. The step from one loop order to the next
   is `−h²`, an element of `ℤ[q, q⁻¹]`. No measure weight enters it.
2. `formB_coeff_of_recursion`: any ladder with `c₁ = s μ₁` and the Form B step is
   `c_L = s μ₁ (−h²)^(L−1)`. Nothing is chosen beyond `μ₁`.
3. `formB_measure_const`: writing `c_L = θ_L μ_L` with the Form B graph values
   `θ_L = s (−h²)^(L−1)`, and `θ_L` cancellable, forces `μ_L = μ₁` at every order.
   So the per-loop measure under Form B is `1` from the second loop on. The only
   measure input is the one-loop weight `μ₁`.
4. `formB_coeff_mem`: every coefficient is in `S·μ₁` for any subring `S` that contains
   `s` and `h`. It is linear in `μ₁`, so no power of `μ₁` and no new period appears.
5. `formB_eq_product_iff`: at two loops the one-factor and product measures agree
   iff `s h² μ₁ (μ₁ − 1) = 0`. In a domain with `s h² ≠ 0` that means `μ₁ ∈ {0, 1}`.

What this does not derive: the value `μ₁ = 1/(π b₁) = 1/(8π)`. That is still the
phase-4 identification (audit 2026-07-18, Clauses A and B). No measured value and no
transcendental constant enter this file.
-/

set_option autoImplicit false

namespace QOU.MassTheory
namespace EmFormBLoopMeasure

variable {K : Type*} [CommRing K]

/-- Form B ladder coefficient at loop order `L + 1`: `s μ₁ (−h²)^L`. -/
def formBCoeff (s h μ₁ : K) (L : ℕ) : K := s * μ₁ * (-h ^ 2) ^ L

/-- Form B graph value at loop order `L + 1`: `s (−h²)^L`. -/
def formBGraph (s h : K) (L : ℕ) : K := s * (-h ^ 2) ^ L

theorem formB_coeff_zero (s h μ₁ : K) : formBCoeff s h μ₁ 0 = s * μ₁ := by
  simp [formBCoeff]

/-- **The per-loop step is `−h²`.** -/
theorem formB_coeff_succ (s h μ₁ : K) (L : ℕ) :
    formBCoeff s h μ₁ (L + 1) = -h ^ 2 * formBCoeff s h μ₁ L := by
  unfold formBCoeff; ring

/-- **Uniqueness.** A ladder with one-loop coefficient `s μ₁` and the Form B step is the
Form B ladder. -/
theorem formB_coeff_of_recursion (s h μ₁ : K) (c : ℕ → K) (h0 : c 0 = s * μ₁)
    (hs : ∀ L, c (L + 1) = -h ^ 2 * c L) : ∀ L, c L = formBCoeff s h μ₁ L := by
  intro L
  induction L with
  | zero => rw [h0, formB_coeff_zero]
  | succ n ih => rw [hs n, ih, formB_coeff_succ]

/-- **The measure is constant.** If `c_L = θ_L μ_L` with the Form B graph values and each
`θ_L` is cancellable, then `μ_L = μ₁` at every order. -/
theorem formB_measure_const (s h μ₁ : K) (μ : ℕ → K)
    (hcan : ∀ L, IsLeftRegular (formBGraph s h L))
    (hc : ∀ L, formBGraph s h L * μ L = formBCoeff s h μ₁ L) : ∀ L, μ L = μ₁ := by
  intro L
  apply hcan L
  simp only
  rw [hc L]; unfold formBGraph formBCoeff; ring

/-- **Linear in `μ₁`.** Every Form B coefficient is `x μ₁` with `x ∈ S`. -/
theorem formB_coeff_mem (S : Subring K) (s h μ₁ : K) (hs : s ∈ S) (hh : h ∈ S) (L : ℕ) :
    ∃ x ∈ S, formBCoeff s h μ₁ L = x * μ₁ :=
  ⟨s * (-h ^ 2) ^ L, S.mul_mem hs (S.pow_mem (S.neg_mem (S.pow_mem hh 2)) L), by
    unfold formBCoeff; ring⟩

/-- **One factor vs product at two loops.** `s (−h²) μ₁ = s (−h²) μ₁²` iff
`s h² μ₁ (μ₁ − 1) = 0`. -/
theorem formB_eq_product_iff (s h μ₁ : K) :
    formBGraph s h 1 * μ₁ = formBGraph s h 1 * μ₁ ^ 2 ↔
      s * h ^ 2 * μ₁ * (μ₁ - 1) = 0 := by
  unfold formBGraph
  constructor
  · intro e; linear_combination e
  · intro e; linear_combination e

end EmFormBLoopMeasure
end QOU.MassTheory
