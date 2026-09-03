import QOU.Hecke.PermLength

/-!
# When is Coxeter length additive?

`QOU.Hecke.PermLength` proves that the Coxeter length of a permutation is its
inversion count (`length_eq_invCount`).  This file turns that into an exact
criterion for when length is **additive** along a product.

Mathlib has subadditivity (`CoxeterSystem.length_mul_le`) but no equality
criterion, so `length_mul_eq_add_iff` below fills a genuine gap.

## The counting identity

Write `Inv w` for the inversion set.  For a pair `p = (a, b)` with `a < b` put

* `A` — "`v` inverts `p`", i.e. `v b < v a`;
* `B` — "`u * v` inverts `p`", i.e. `u (v b) < u (v a)`.

Sorting the pair `(v a, v b)` gives a bijection `vPair v` of the strictly
ordered pairs, and the point of the whole file is that

  `vPair v p ∈ Inv u  ↔  A xor B`.

Counting the four classes `A ∧ B`, `A ∧ ¬B`, `¬A ∧ B`, `¬A ∧ ¬B` then gives

  `ℓ(u) + ℓ(v) = ℓ(u * v) + 2 · #{p ∈ Inv v : p ∉ Inv (u * v)}`,

so length is additive exactly when `u` undoes none of `v`'s inversions —
that is, exactly when `Inv v ⊆ Inv (u * v)`.
-/

open Equiv Finset

namespace QOU.Hecke.Inversions

open QOU.Hecke.SymmetricCoxeter

variable {m n : ℕ}

/-! ### The strictly ordered pairs -/

/-- The pairs `(a, b)` with `a < b`: the index set every inversion set sits in. -/
def pairsLt (m : ℕ) : Finset (Fin m × Fin m) :=
  Finset.univ.filter (fun p => p.1 < p.2)

@[simp] theorem mem_pairsLt {p : Fin m × Fin m} : p ∈ pairsLt m ↔ p.1 < p.2 := by
  simp [pairsLt]

theorem invSet_subset_pairsLt (w : Perm (Fin m)) : invSet w ⊆ pairsLt m :=
  fun _ hp => mem_pairsLt.2 (mem_invSet.1 hp).1

/-- Filtering the ordered pairs by membership in an inversion set is a no-op. -/
theorem filter_mem_invSet (w : Perm (Fin m)) :
    (pairsLt m).filter (fun p => p ∈ invSet w) = invSet w := by
  ext p
  simp only [mem_filter, mem_pairsLt]
  exact ⟨fun h => h.2, fun h => ⟨(mem_invSet.1 h).1, h⟩⟩

/-! ### The induced map on pairs -/

/-- Sort a pair into increasing order. -/
def sortPair (p : Fin m × Fin m) : Fin m × Fin m :=
  if p.1 < p.2 then p else (p.2, p.1)

/-- The map induced on unordered pairs by a permutation: apply `v`, then re-sort. -/
def vPair (v : Perm (Fin m)) (p : Fin m × Fin m) : Fin m × Fin m :=
  sortPair (v p.1, v p.2)

theorem vPair_mem_pairsLt (v : Perm (Fin m)) {p : Fin m × Fin m} (h : p.1 < p.2) :
    vPair v p ∈ pairsLt m := by
  have hne : v p.1 ≠ v p.2 := fun hh => (ne_of_lt h) (v.injective hh)
  unfold vPair sortPair
  by_cases hlt : v p.1 < v p.2
  · simp [hlt]
  · have : v p.2 < v p.1 := (not_lt.1 hlt).lt_of_ne (Ne.symm hne)
    simpa [hlt] using this

/-- `vPair v` is undone by `vPair v⁻¹` on strictly ordered pairs. -/
theorem vPair_inv_vPair (v : Perm (Fin m)) {p : Fin m × Fin m} (h : p.1 < p.2) :
    vPair v⁻¹ (vPair v p) = p := by
  unfold vPair sortPair
  by_cases hlt : v p.1 < v p.2
  · simp [hlt, h]
  · simp [hlt, not_lt.2 (le_of_lt h)]

/-- **The key membership criterion.**  `u` inverts the sorted image of `p` under
`v` exactly when precisely one of `v`, `u * v` inverts `p`. -/
theorem vPair_mem_invSet_iff (u v : Perm (Fin m)) {p : Fin m × Fin m} (hp : p.1 < p.2) :
    vPair v p ∈ invSet u ↔
      ((p ∈ invSet v ∧ p ∉ invSet (u * v)) ∨ (p ∉ invSet v ∧ p ∈ invSet (u * v))) := by
  have hne : v p.1 ≠ v p.2 := fun hh => (ne_of_lt hp) (v.injective hh)
  have hune : u (v p.1) ≠ u (v p.2) := fun hh => hne (u.injective hh)
  have hA : p ∈ invSet v ↔ v p.2 < v p.1 := by simp [mem_invSet, hp]
  have hB : p ∈ invSet (u * v) ↔ u (v p.2) < u (v p.1) := by
    simp [mem_invSet, hp, Equiv.Perm.mul_apply]
  rw [hA, hB]
  by_cases hlt : v p.1 < v p.2
  · have hpair : vPair v p = (v p.1, v p.2) := by simp [vPair, sortPair, hlt]
    rw [hpair]
    simp only [mem_invSet]
    constructor
    · intro h
      exact Or.inr ⟨asymm hlt, h.2⟩
    · rintro (h | h)
      · exact absurd hlt (asymm h.1)
      · exact ⟨hlt, h.2⟩
  · have hA' : v p.2 < v p.1 := (not_lt.1 hlt).lt_of_ne (Ne.symm hne)
    have hpair : vPair v p = (v p.2, v p.1) := by simp [vPair, sortPair, hlt]
    rw [hpair]
    simp only [mem_invSet]
    constructor
    · intro h
      exact Or.inl ⟨hA', asymm h.2⟩
    · rintro (h | h)
      · exact ⟨hA', (not_lt.1 h.2).lt_of_ne hune⟩
      · exact absurd hA' h.1

/-! ### The counting identity -/

/-- The inversion count of `u` counts the pairs inverted by exactly one of
`v` and `u * v`. -/
theorem invCount_eq_card_symmDiff (u v : Perm (Fin (n + 1))) :
    invCount u
      = ((pairsLt (n + 1)).filter
          (fun p => (p ∈ invSet v ∧ p ∉ invSet (u * v))
                  ∨ (p ∉ invSet v ∧ p ∈ invSet (u * v)))).card := by
  classical
  refine Finset.card_bij' (fun q _ => vPair v⁻¹ q) (fun p _ => vPair v p) ?_ ?_ ?_ ?_
  · intro q hq
    have hq' : q.1 < q.2 := (mem_invSet.1 hq).1
    have hmem : vPair v⁻¹ q ∈ pairsLt (n + 1) := vPair_mem_pairsLt _ hq'
    refine mem_filter.2 ⟨hmem, ?_⟩
    have hback : vPair v (vPair v⁻¹ q) = q := by
      have := vPair_inv_vPair v⁻¹ hq'
      simpa using this
    exact (vPair_mem_invSet_iff u v (mem_pairsLt.1 hmem)).1 (by rw [hback]; exact hq)
  · intro p hp
    have hp' : p.1 < p.2 := mem_pairsLt.1 (mem_filter.1 hp).1
    exact (vPair_mem_invSet_iff u v hp').2 (mem_filter.1 hp).2
  · intro q hq
    have hq' : q.1 < q.2 := (mem_invSet.1 hq).1
    have := vPair_inv_vPair v⁻¹ hq'
    simpa using this
  · intro p hp
    exact vPair_inv_vPair v (mem_pairsLt.1 (mem_filter.1 hp).1)

/-- **The length-additivity defect.**  `ℓ(u) + ℓ(v)` exceeds `ℓ(u * v)` by twice
the number of `v`-inversions that `u` undoes. -/
theorem invCount_add_invCount (u v : Perm (Fin (n + 1))) :
    invCount u + invCount v
      = invCount (u * v) + 2 * ((invSet v).filter (fun p => p ∉ invSet (u * v))).card := by
  classical
  set D₁ := (invSet v).filter (fun p => p ∉ invSet (u * v)) with hD₁
  set D₂ := (invSet (u * v)).filter (fun p => p ∉ invSet v) with hD₂
  have hS : (pairsLt (n + 1)).filter
      (fun p => (p ∈ invSet v ∧ p ∉ invSet (u * v))
              ∨ (p ∉ invSet v ∧ p ∈ invSet (u * v))) = D₁ ∪ D₂ := by
    ext p
    simp only [hD₁, hD₂, mem_union, mem_filter, mem_pairsLt]
    constructor
    · rintro ⟨-, h | h⟩
      · exact Or.inl ⟨h.1, h.2⟩
      · exact Or.inr ⟨h.2, h.1⟩
    · rintro (h | h)
      · exact ⟨(mem_invSet.1 h.1).1, Or.inl ⟨h.1, h.2⟩⟩
      · exact ⟨(mem_invSet.1 h.1).1, Or.inr ⟨h.2, h.1⟩⟩
  have hdisj : Disjoint D₁ D₂ := by
    rw [hD₁, hD₂, Finset.disjoint_left]
    intro p hp hq
    exact (mem_filter.1 hp).2 (mem_filter.1 hq).1
  have hu : invCount u = D₁.card + D₂.card := by
    rw [invCount_eq_card_symmDiff u v, hS, card_union_of_disjoint hdisj]
  have h1 : ((invSet v).filter (fun p => p ∈ invSet (u * v))).card + D₁.card = invCount v := by
    rw [hD₁]
    exact filter_card_add_filter_neg_card_eq_card _
  have h2 : ((invSet (u * v)).filter (fun p => p ∈ invSet v)).card + D₂.card
      = invCount (u * v) := by
    rw [hD₂]
    exact filter_card_add_filter_neg_card_eq_card _
  have h3 : ((invSet v).filter (fun p => p ∈ invSet (u * v))).card
      = ((invSet (u * v)).filter (fun p => p ∈ invSet v)).card := by
    rw [filter_mem_eq_inter, filter_mem_eq_inter, Finset.inter_comm]
  omega

/-! ### The criterion -/

/-- **Length is additive exactly when no inversion is undone.**

`ℓ(u * v) = ℓ(u) + ℓ(v)` holds iff every pair inverted by `v` is still
inverted by `u * v`. -/
theorem length_mul_eq_add_iff (u v : Perm (Fin (n + 1))) :
    (permCoxeterSystem n).length (u * v)
        = (permCoxeterSystem n).length u
          + (permCoxeterSystem n).length v
      ↔ invSet v ⊆ invSet (u * v) := by
  classical
  rw [length_eq_invCount, length_eq_invCount, length_eq_invCount]
  have key := invCount_add_invCount u v
  constructor
  · intro h
    have hzero : ((invSet v).filter (fun p => p ∉ invSet (u * v))).card = 0 := by omega
    intro p hp
    by_contra hcon
    have : p ∈ (invSet v).filter (fun p => p ∉ invSet (u * v)) := mem_filter.2 ⟨hp, hcon⟩
    rw [card_eq_zero] at hzero
    simp [hzero] at this
  · intro h
    have hempty : (invSet v).filter (fun p => p ∉ invSet (u * v)) = ∅ := by
      rw [filter_eq_empty_iff]
      intro p hp
      exact not_not.2 (h hp)
    rw [hempty] at key
    simpa using key.symm

/-! ### Non-vacuity

The criterion is an honest `iff`: both sides genuinely occur.  `s₀ * s₀ = 1`
collapses, so additivity fails and the subset criterion is false; `s₀ * s₁` is
reduced, so it holds. -/

section NonVacuity

open Equiv

/-- `s₀ * s₀ = 1`: `u` undoes `v`'s inversion, so additivity fails. -/
example : ¬ (invSet (swap (0 : Fin 3) 1) ⊆ invSet (swap (0 : Fin 3) 1 * swap (0 : Fin 3) 1)) := by
  decide

/-- `s₀ * s₁` is reduced: no inversion is undone, so additivity holds. -/
example : invSet (swap (1 : Fin 3) 2) ⊆ invSet (swap (0 : Fin 3) 1 * swap (1 : Fin 3) 2) := by
  decide

/-- The defect in the collapsing case is genuinely `2`, matching
`invCount_add_invCount`. -/
example : invCount (swap (0 : Fin 3) 1) + invCount (swap (0 : Fin 3) 1)
    = invCount (swap (0 : Fin 3) 1 * swap (0 : Fin 3) 1) + 2 := by decide

end NonVacuity

end QOU.Hecke.Inversions
