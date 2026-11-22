import Mathlib.Tactic
import Mathlib.GroupTheory.Perm.Cycle.Type

/-!
# The genus-4 torus knots' algebraic fibres are not Bring's curve

The two saturating torus knots `T(3,5)` and `T(2,9)` are links of the singularities
`y³ = x⁵` and `y² = x⁹`. Their Milnor fibres compactify to the smooth genus-4 curves
`X₃,₅ : y³ = x⁵ + 1` and `X₂,₉ : y² = x⁹ + 1`. On these curves
`(x, y) ↦ (ζ₅x, ζ₃y)` has order 15 and `(x, y) ↦ (ζ₉x, y)` has order 9.

The corpus records `Aut(Σ₄) ≅ S₅` (`def:brings-surface`). Bring's curve `Σ₄` therefore has
no automorphism of order 9 or 15 (the two lemmas below). So neither compactified fibre is
isomorphic to `Σ₄`. The genus-4 match between these knots and Bring's surface is
topological only. It does not come from an identification of curves.

Scope: the order-9 and order-15 automorphisms and the genus of `X₃,₅` and `X₂,₉` are
standard facts about superelliptic curves. They are cited here, not proved.
-/

namespace QOU.AlphaEM.Saturation

-- Ref: [leitner2026] Ch. Bring's surface, def:brings-surface (Aut Σ₄ ≅ S₅)
open Equiv in
/-- Every cycle length of a permutation of `Fin 5` lies in `[2, 5]` and divides its order. -/
theorem cycle_len_facts (σ : Perm (Fin 5)) {a : ℕ} (ha : a ∈ σ.cycleType) :
    2 ≤ a ∧ a ≤ 5 ∧ a ∣ orderOf σ := by
  refine ⟨Perm.two_le_of_mem_cycleType ha, ?_, ?_⟩
  · calc a ≤ σ.cycleType.sum := Multiset.le_sum_of_mem ha
      _ = σ.support.card := Perm.sum_cycleType σ
      _ ≤ 5 := by simpa using Finset.card_le_univ σ.support
  · rw [← Perm.lcm_cycleType]; exact Multiset.dvd_lcm ha

open Equiv in
/-- **`S₅` has no element of order 9.** -/
theorem perm5_no_order_9 (σ : Perm (Fin 5)) : orderOf σ ≠ 9 := by
  intro h
  have hall : ∀ a ∈ σ.cycleType, a ∣ 3 := by
    intro a ha
    obtain ⟨h2, h5, hd⟩ := cycle_len_facts σ ha
    rw [h] at hd
    interval_cases a <;> simp_all
  have : orderOf σ ∣ 3 := by rw [← Perm.lcm_cycleType]; exact Multiset.lcm_dvd.2 hall
  rw [h] at this; norm_num at this

open Equiv in
/-- **`S₅` has no element of order 15.** -/
theorem perm5_no_order_15 (σ : Perm (Fin 5)) : orderOf σ ≠ 15 := by
  intro h
  have hlen : ∀ a ∈ σ.cycleType, a = 3 ∨ a = 5 := by
    intro a ha
    obtain ⟨h2, h5, hd⟩ := cycle_len_facts σ ha
    rw [h] at hd
    interval_cases a <;> simp_all
  have h3 : 3 ∈ σ.cycleType := by
    by_contra h3
    have hall : ∀ a ∈ σ.cycleType, a ∣ 5 := by
      intro a ha
      rcases hlen a ha with rfl | rfl
      · exact absurd ha h3
      · exact dvd_rfl
    have : orderOf σ ∣ 5 := by rw [← Perm.lcm_cycleType]; exact Multiset.lcm_dvd.2 hall
    rw [h] at this; norm_num at this
  have h5 : 5 ∈ σ.cycleType := by
    by_contra h5
    have hall : ∀ a ∈ σ.cycleType, a ∣ 3 := by
      intro a ha
      rcases hlen a ha with rfl | rfl
      · exact dvd_rfl
      · exact absurd ha h5
    have : orderOf σ ∣ 3 := by rw [← Perm.lcm_cycleType]; exact Multiset.lcm_dvd.2 hall
    rw [h] at this; norm_num at this
  obtain ⟨t, ht⟩ := Multiset.exists_cons_of_mem h3
  have h5t : 5 ∈ t := by
    rw [ht, Multiset.mem_cons] at h5
    rcases h5 with h | h
    · norm_num at h
    · exact h
  obtain ⟨u, hu⟩ := Multiset.exists_cons_of_mem h5t
  have hsum : σ.cycleType.sum = 8 + u.sum := by
    rw [ht, hu]; simp; ring
  have hle : σ.cycleType.sum ≤ 5 := by
    rw [Perm.sum_cycleType]; simpa using Finset.card_le_univ σ.support
  omega

end QOU.AlphaEM.Saturation
