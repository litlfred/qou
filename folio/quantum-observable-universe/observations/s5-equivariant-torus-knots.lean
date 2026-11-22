import Mathlib.Tactic
import Mathlib.GroupTheory.SpecificGroups.Cyclic
import Mathlib.GroupTheory.Perm.Cycle.Type


/-!
# QOU.TorusKnot.s5_equivariant_classification

A torus knot T_{2,s} (s ≥ 3, coprime to 2) admits an
S_5-equivariant embedding iff s ∈ {3, 5}, since the orders of
elements of S_5 are {1, 2, 3, 4, 5, 6} and the odd values ≥ 3
in this set are exactly {3, 5}.

LaTeX label: `prop:s5-equivariant-torus-knots`

**Ground ring**: `ℤ` (finite group theory).
-/

namespace QOU

open Equiv

/-- The set of element orders that occur in S_5.
    Cycle types of S_5 partitions and their LCMs:
      (1)^5 → 1, (2)(1)^3 → 2, (2)^2(1) → 2, (3)(1)^2 → 3,
      (3)(2) → 6, (4)(1) → 4, (5) → 5. -/
-- Ref: [leitner2026] Chapter 7, §Particle identification conjectures
def s5ElementOrders : Set ℕ := {1, 2, 3, 4, 5, 6}

/-- Odd element orders ≥ 3 that occur in S_5.
    By inspection of s5ElementOrders: {3, 5}. -/
-- Ref: [leitner2026] Chapter 7, §Particle identification conjectures
def s5OddOrdersGe3 : Set ℕ := {3, 5}

/-- **S_5-equivariant torus-knot classification**:
    T_{2,s} (s ≥ 3, gcd(2,s) = 1, i.e. s odd) embeds equivariantly
    into a Riemann surface with automorphism group S_5 iff
    s ∈ {3, 5}.

    The proof reduces to finding an element of order s in S_5.
    By the orders-in-S_5 table, odd orders ≥ 3 are exactly {3, 5}.

    LaTeX: `\label{prop:s5-equivariant-torus-knots}`
    Ref: [leitner2026] Chapter 7, §Particle identification conjectures -/
theorem s5_equivariant_classification (s : ℕ)
    (hs : 3 ≤ s) (hodd : Odd s) :
    (s ∈ s5OddOrdersGe3) ↔ (s = 3 ∨ s = 5) := by
  constructor
  · intro hmem
    rcases hmem with (rfl | rfl)
    · left; rfl
    · right; rfl
  · intro h
    rcases h with (rfl | rfl)
    · left; rfl
    · right; rfl

/-! ## The two tests, stated on `S₅` itself

The fibration of `T(2,s)` has monodromy of order `2s`. For odd `s` this cyclic group is
`ℤ₂ × ℤ_s`, the two rotations of the torus knot together. Two tests therefore make sense:

* the **ℤ_s test** (weaker): `S₅` has an element of order `s`. It holds iff `s ∈ {3, 5}`
  (`s5_has_order_iff`).
* the **monodromy test** (stronger): `S₅` has an element of order `2s`. It holds iff
  `s = 3` (`s5_has_order_two_mul_iff`).

Both are proved from cycle types, not from the table `s5ElementOrders`.
-/

/-- Every cycle length of a permutation of `Fin 5` lies in `[2, 5]` and divides its order. -/
theorem s5_cycle_len_facts (σ : Perm (Fin 5)) {a : ℕ} (ha : a ∈ σ.cycleType) :
    2 ≤ a ∧ a ≤ 5 ∧ a ∣ orderOf σ := by
  refine ⟨Perm.two_le_of_mem_cycleType ha, ?_, ?_⟩
  · calc a ≤ σ.cycleType.sum := Multiset.le_sum_of_mem ha
      _ = σ.support.card := Perm.sum_cycleType σ
      _ ≤ 5 := by simpa using Finset.card_le_univ σ.support
  · rw [← Perm.lcm_cycleType]; exact Multiset.dvd_lcm ha

/-- The order of every element of `S₅` divides 60. -/
theorem s5_order_dvd_sixty (σ : Perm (Fin 5)) : orderOf σ ∣ 60 := by
  rw [← Perm.lcm_cycleType]
  refine Multiset.lcm_dvd.2 fun a ha => ?_
  obtain ⟨h2, h5, -⟩ := s5_cycle_len_facts σ ha
  interval_cases a <;> norm_num

/-- If 5 divides the order of an element of `S₅`, the element is a 5-cycle. -/
theorem s5_five_dvd_order (σ : Perm (Fin 5)) (h : 5 ∣ orderOf σ) : orderOf σ = 5 := by
  by_cases h5 : 5 ∈ σ.cycleType
  · obtain ⟨t, ht⟩ := Multiset.exists_cons_of_mem h5
    have hle : σ.cycleType.sum ≤ 5 := by
      rw [Perm.sum_cycleType]; simpa using Finset.card_le_univ σ.support
    have ht0 : t = 0 := by
      by_contra hne
      obtain ⟨a, ha⟩ := Multiset.exists_mem_of_ne_zero hne
      have ha' : a ∈ σ.cycleType := by rw [ht]; exact Multiset.mem_cons_of_mem ha
      have h2 := (s5_cycle_len_facts σ ha').1
      have : a ≤ t.sum := Multiset.le_sum_of_mem ha
      rw [ht, Multiset.sum_cons] at hle
      omega
    rw [← Perm.lcm_cycleType, ht, ht0]; simp
  · exfalso
    have : orderOf σ ∣ 12 := by
      rw [← Perm.lcm_cycleType]
      refine Multiset.lcm_dvd.2 fun a ha => ?_
      obtain ⟨h2, h5', -⟩ := s5_cycle_len_facts σ ha
      interval_cases a <;> simp_all
    have := dvd_trans h this
    norm_num at this

private theorem odd_dvd_sixty {s : ℕ} (hs : 3 ≤ s) (hodd : Odd s) (h : s ∣ 60) :
    s = 3 ∨ s = 5 ∨ s = 15 := by
  have hle : s ≤ 60 := Nat.le_of_dvd (by norm_num) h
  obtain ⟨k, rfl⟩ := hodd
  have hk : k ≤ 30 := by omega
  interval_cases k <;> simp_all

/-- **ℤ_s test.** For odd `s ≥ 3`, `S₅` has an element of order `s` iff `s ∈ {3, 5}`. -/
theorem s5_has_order_iff (s : ℕ) (hs : 3 ≤ s) (hodd : Odd s) :
    (∃ σ : Perm (Fin 5), orderOf σ = s) ↔ (s = 3 ∨ s = 5) := by
  constructor
  · rintro ⟨σ, rfl⟩
    rcases odd_dvd_sixty hs hodd (s5_order_dvd_sixty σ) with h | h | h
    · exact Or.inl h
    · exact Or.inr h
    · have := s5_five_dvd_order σ (by rw [h]; norm_num); omega
  · rintro (rfl | rfl)
    · refine ⟨swap 0 1 * swap 1 2, orderOf_eq_prime (by decide) (by decide)⟩
    · haveI : Fact (Nat.Prime 5) := ⟨by norm_num⟩
      exact ⟨swap 0 1 * swap 1 2 * swap 2 3 * swap 3 4,
        orderOf_eq_prime (by decide) (by decide)⟩

/-- **Monodromy test.** For odd `s ≥ 3`, `S₅` has an element of order `2s` iff `s = 3`.
So under this test only `T(2,3)` passes; `T(2,5)` fails, since `S₅` has no element of
order 10. -/
theorem s5_has_order_two_mul_iff (s : ℕ) (hs : 3 ≤ s) (hodd : Odd s) :
    (∃ σ : Perm (Fin 5), orderOf σ = 2 * s) ↔ s = 3 := by
  constructor
  · rintro ⟨σ, hσ⟩
    have h60 := s5_order_dvd_sixty σ
    rw [hσ] at h60
    rcases odd_dvd_sixty hs hodd (dvd_trans (Dvd.intro_left 2 rfl) h60) with h | h | h
    · exact h
    · have := s5_five_dvd_order σ (by rw [hσ, h]; norm_num); omega
    · have := s5_five_dvd_order σ (by rw [hσ, h]; norm_num); omega
  · rintro rfl
    refine ⟨swap 0 1 * (swap 2 3 * swap 3 4), ?_⟩
    have h6 : (swap (0 : Fin 5) 1 * (swap 2 3 * swap 3 4)) ^ 6 = 1 := by decide
    have hd : orderOf (swap (0 : Fin 5) 1 * (swap 2 3 * swap 3 4)) ∣ 6 :=
      orderOf_dvd_of_pow_eq_one h6
    have h2 : (swap (0 : Fin 5) 1 * (swap 2 3 * swap 3 4)) ^ 2 ≠ 1 := by decide
    have h3 : (swap (0 : Fin 5) 1 * (swap 2 3 * swap 3 4)) ^ 3 ≠ 1 := by decide
    have hpos := orderOf_pos (swap (0 : Fin 5) 1 * (swap 2 3 * swap 3 4))
    have hle := Nat.le_of_dvd (by norm_num) hd
    interval_cases h : orderOf (swap (0 : Fin 5) 1 * (swap 2 3 * swap 3 4))
    · exact absurd (by rw [← pow_one (swap (0 : Fin 5) 1 * (swap 2 3 * swap 3 4)), ← h,
        pow_orderOf_eq_one]) (by decide : (swap (0 : Fin 5) 1 * (swap 2 3 * swap 3 4)) ≠ 1)
    · exact absurd (h ▸ pow_orderOf_eq_one _) h2
    · exact absurd (h ▸ pow_orderOf_eq_one _) h3
    · norm_num at hd
    · norm_num at hd
    · rfl

end QOU
