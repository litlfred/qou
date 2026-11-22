import Mathlib.Tactic
import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.GroupTheory.SpecificGroups.Cyclic

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

/-! ## No `S₅`-equivariant home for the genus-4 fibre surfaces

Three group-theoretic facts used in audit §20. With two cited topological facts they rule
out any `S₅`-equivariant embedding of a genus-4, one-boundary fibre surface into Bring's
surface:

* `perm5_not_isCyclic`: `S₅` is not cyclic. A finite group of holomorphic automorphisms
  fixing a point of a Riemann surface is cyclic (it acts faithfully on the tangent line).
* `perm5_no_order_18`: the `T(2,9)` monodromy has order 18, and `S₅` has no such element.
* `no_overgroup_of_perm5`: a finite group of order at most 120 that contains `S₅` has no
  element of order 15 or 18. With Kerckhoff's Nielsen realisation and the bound
  `|Aut| ≤ 120` in genus 4, this excludes the `T(3,5)` and `T(2,9)` monodromies from any
  finite group of mapping classes containing an `S₅`.
-/

open Equiv in
/-- **`S₅` is not cyclic.** Two transpositions sharing a point do not commute. -/
theorem perm5_not_isCyclic : ¬ IsCyclic (Perm (Fin 5)) := by
  intro h
  obtain ⟨g, hg⟩ := IsCyclic.exists_generator (α := Perm (Fin 5))
  have key : ∀ a b : Perm (Fin 5), a * b = b * a := by
    intro a b
    obtain ⟨m, rfl⟩ := Subgroup.mem_zpowers_iff.1 (hg a)
    obtain ⟨n, rfl⟩ := Subgroup.mem_zpowers_iff.1 (hg b)
    exact (Commute.zpow_zpow_self g m n).eq
  exact absurd (key (swap (0 : Fin 5) 1) (swap 1 2)) (by decide)

open Equiv in
/-- **`S₅` has no element of order 18.** Its square would have order 9. -/
theorem perm5_no_order_18 (σ : Perm (Fin 5)) : orderOf σ ≠ 18 := by
  intro h
  have h9 : orderOf (σ ^ 2) = 9 := by
    rw [orderOf_pow_of_dvd (by norm_num) (by rw [h]; norm_num), h]
  exact perm5_no_order_9 _ h9

open Equiv in
/-- **No small overgroup of `S₅` has an element of order 15 or 18.** If `S₅` injects into a
finite group `G` with `|G| ≤ 120`, the injection is onto, so every element of `G` has an
order already realised in `S₅`. -/
theorem no_overgroup_of_perm5 {G : Type*} [Group G] [Finite G] (hG : Nat.card G ≤ 120)
    (φ : Perm (Fin 5) →* G) (hφ : Function.Injective φ) (g : G) :
    orderOf g ≠ 15 ∧ orderOf g ≠ 18 := by
  have hcard : Nat.card (Perm (Fin 5)) = 120 := by
    rw [Nat.card_eq_fintype_card, Fintype.card_perm, Fintype.card_fin]; rfl
  obtain ⟨σ, rfl⟩ := (hφ.bijective_of_nat_card_le (by omega)).2 g
  rw [orderOf_injective φ hφ σ]
  exact ⟨perm5_no_order_15 σ, perm5_no_order_18 σ⟩

end QOU.AlphaEM.Saturation
