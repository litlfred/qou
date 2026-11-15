import QOU.Hecke.PermLength

/-!
# The `w ↔ w·sᵢ` pairing, and its length dichotomy

`QOU.BraidKnot.HeckeCellular` builds the Murphy element `x_λ = Σ_{w ∈ S_λ} T_w`
only in the **rank-one** case `S_λ = ⟨sᵢ⟩`, and says why:

> the eigenvector property is proved by pairing each `w` with `w sᵢ` — one of the
> two has length going up, the other down … **that pairing argument over
> `Equiv.Perm (Fin (n+1))` is the open work**. The `T_w` basis it needs is now
> available, so the blocker is the combinatorics, not the algebra.

This file supplies that combinatorics.

## What is here

* `length_swap_dichotomy` — for every `w` and every simple reflection `sᵢ`,
  **exactly one** of `ℓ(w·sᵢ) = ℓ(w) + 1` and `ℓ(w) = ℓ(w·sᵢ) + 1` holds.  This
  is the fact the two `rsFun` branches are selected by.
* `mulSwap` — right multiplication by `sᵢ`, as an **involution** of
  `Perm (Fin (n+1))` with no fixed points, so it pairs the group up.
* `mulSwap_pairs` on a `Finset` closed under it: the set splits into the
  length-ascending half and its image, which is what turns
  `Σ_{w ∈ S} T_w` into a sum over pairs.

Nothing here mentions the Hecke algebra: it is a statement about permutations
and Coxeter length, which is exactly why it was the blocker.
-/

open Equiv Finset

namespace QOU.Hecke.ParabolicPairing

open QOU.Hecke.SymmetricCoxeter QOU.Hecke.Inversions

variable {n : ℕ}

/-- Right multiplication by the simple reflection `sᵢ`. -/
def mulSwap (i : Fin n) (w : Perm (Fin (n + 1))) : Perm (Fin (n + 1)) :=
  w * Equiv.swap i.castSucc i.succ

/-- `mulSwap i` is an involution. -/
@[simp] theorem mulSwap_mulSwap (i : Fin n) (w : Perm (Fin (n + 1))) :
    mulSwap i (mulSwap i w) = w := by
  simp [mulSwap, mul_assoc, Equiv.swap_mul_self]

theorem mulSwap_involutive (i : Fin n) : Function.Involutive (mulSwap (n := n) i) :=
  mulSwap_mulSwap i

theorem mulSwap_injective (i : Fin n) : Function.Injective (mulSwap (n := n) i) :=
  (mulSwap_involutive i).injective

/-- The two values `sᵢ` exchanges, read off through `w`. -/
theorem mulSwap_apply_castSucc (i : Fin n) (w : Perm (Fin (n + 1))) :
    mulSwap i w i.castSucc = w i.succ := by
  simp [mulSwap, Equiv.Perm.mul_apply, Equiv.swap_apply_left]

theorem mulSwap_apply_succ (i : Fin n) (w : Perm (Fin (n + 1))) :
    mulSwap i w i.succ = w i.castSucc := by
  simp [mulSwap, Equiv.Perm.mul_apply, Equiv.swap_apply_right]

/-- **`mulSwap` has no fixed point**: `w ≠ w·sᵢ`, so the pairing is genuine. -/
theorem mulSwap_ne (i : Fin n) (w : Perm (Fin (n + 1))) : mulSwap i w ≠ w := by
  intro h
  have h1 : mulSwap i w i.castSucc = w i.castSucc := by rw [h]
  rw [mulSwap_apply_castSucc] at h1
  have : i.succ = i.castSucc := w.injective h1
  exact absurd this (by simp [Fin.ext_iff, Fin.val_succ, Fin.coe_castSucc])

/-! ### The dichotomy -/

/-- **Exactly one of `w` and `w·sᵢ` is longer, and by exactly one.**

This is the fact the Murphy-element pairing argument turns on: for each `w`, one
of the two `rsFun` branches applies to `w` and the other to `w·sᵢ`. -/
theorem length_swap_dichotomy (i : Fin n) (w : Perm (Fin (n + 1))) :
    ((permCoxeterSystem n).length (mulSwap i w) = (permCoxeterSystem n).length w + 1
      ∧ ¬ ((permCoxeterSystem n).length w = (permCoxeterSystem n).length (mulSwap i w) + 1))
    ∨ ((permCoxeterSystem n).length w = (permCoxeterSystem n).length (mulSwap i w) + 1
      ∧ ¬ ((permCoxeterSystem n).length (mulSwap i w)
            = (permCoxeterSystem n).length w + 1)) := by
  by_cases hlt : w i.castSucc < w i.succ
  · refine Or.inl ⟨(length_mul_swap_eq_succ_iff w i).2 hlt, ?_⟩
    have := (length_mul_swap_eq_succ_iff w i).2 hlt
    show ¬ _
    rw [mulSwap] at *
    omega
  · -- the other direction: apply the same criterion to `w·sᵢ`
    have hne : w i.castSucc ≠ w i.succ := fun h =>
      absurd (w.injective h) (by simp [Fin.ext_iff, Fin.val_succ, Fin.coe_castSucc])
    have hgt : w i.succ < w i.castSucc := lt_of_le_of_ne (not_lt.1 hlt) (Ne.symm hne)
    have hstep : (permCoxeterSystem n).length (mulSwap i (mulSwap i w))
        = (permCoxeterSystem n).length (mulSwap i w) + 1 := by
      refine (length_mul_swap_eq_succ_iff (mulSwap i w) i).2 ?_
      rw [mulSwap_apply_castSucc, mulSwap_apply_succ]
      exact hgt
    rw [mulSwap_mulSwap] at hstep
    exact Or.inr ⟨hstep, by omega⟩

/-- The dichotomy as a plain disjunction, when only the lengths are wanted. -/
theorem length_swap_cases (i : Fin n) (w : Perm (Fin (n + 1))) :
    (permCoxeterSystem n).length (mulSwap i w) = (permCoxeterSystem n).length w + 1
      ∨ (permCoxeterSystem n).length w = (permCoxeterSystem n).length (mulSwap i w) + 1 := by
  rcases length_swap_dichotomy i w with ⟨h, _⟩ | ⟨h, _⟩
  · exact Or.inl h
  · exact Or.inr h

/-- The two are never the same length — a corollary worth having on its own, since
it is what makes "one goes up, the other down" a genuine split. -/
theorem length_swap_ne (i : Fin n) (w : Perm (Fin (n + 1))) :
    (permCoxeterSystem n).length (mulSwap i w) ≠ (permCoxeterSystem n).length w := by
  rcases length_swap_cases i w with h | h <;> omega

/-! ### Pairing a closed `Finset`

A Young subgroup containing `sᵢ` is closed under `mulSwap i`.  On such a set the
involution is a fixed-point-free pairing, which is what lets a sum over the set be
reorganised into a sum over pairs. -/

/-- On a set closed under `mulSwap i`, the map is a bijection of the set onto
itself. -/
theorem mulSwap_bij {S : Finset (Perm (Fin (n + 1)))} {i : Fin n}
    (hS : ∀ w ∈ S, mulSwap i w ∈ S) :
    ∀ w ∈ S, ∃! v, v ∈ S ∧ mulSwap i v = w := by
  intro w hw
  refine ⟨mulSwap i w, ⟨hS w hw, mulSwap_mulSwap i w⟩, ?_⟩
  rintro v ⟨-, rfl⟩
  rw [mulSwap_mulSwap]

/-- **The ascending half determines the set.**  Every element of a closed `S` is
either length-ascending under `mulSwap i` or the image of one that is — the split
the Murphy pairing sums over. -/
theorem mem_ascending_or_image {S : Finset (Perm (Fin (n + 1)))} {i : Fin n}
    (hS : ∀ w ∈ S, mulSwap i w ∈ S) (w : Perm (Fin (n + 1))) (hw : w ∈ S) :
    ((permCoxeterSystem n).length (mulSwap i w) = (permCoxeterSystem n).length w + 1)
      ∨ (∃ v ∈ S, mulSwap i v = w
          ∧ (permCoxeterSystem n).length (mulSwap i v)
              = (permCoxeterSystem n).length v + 1) := by
  rcases length_swap_cases i w with h | h
  · exact Or.inl h
  · refine Or.inr ⟨mulSwap i w, hS w hw, mulSwap_mulSwap i w, ?_⟩
    rw [mulSwap_mulSwap]
    omega

/-! ### For a subgroup, closure is free

The `hS` hypothesis above is an assumption about an arbitrary `Finset`.  For the
case it exists to serve it is not an assumption at all: a Young subgroup
containing `sᵢ` is closed under right multiplication by `sᵢ` because it is a
**subgroup**.  So the pairing applies to `x_λ`'s index set with nothing to
check. -/

/-- A subgroup containing `sᵢ` is closed under `mulSwap i` — by `mul_mem`, and
nothing else. -/
theorem mulSwap_mem {H : Subgroup (Perm (Fin (n + 1)))} {i : Fin n}
    (hi : Equiv.swap i.castSucc i.succ ∈ H) {w : Perm (Fin (n + 1))} (hw : w ∈ H) :
    mulSwap i w ∈ H := H.mul_mem hw hi

/-- The same, phrased with the simple reflection `s n i` of the Coxeter system,
which is how a Young subgroup is presented. -/
theorem mulSwap_mem' {H : Subgroup (Perm (Fin (n + 1)))} {i : Fin n}
    (hi : QOU.Hecke.SymmetricCoxeter.s n i ∈ H) {w : Perm (Fin (n + 1))} (hw : w ∈ H) :
    mulSwap i w ∈ H :=
  mulSwap_mem (by rwa [← QOU.Hecke.Inversions.s_eq_swap]) hw

/-- **The pairing, on a subgroup.**  Every element is length-ascending under
`mulSwap i` or the image of one that is — with no closure hypothesis, since a
subgroup containing `sᵢ` supplies it. -/
theorem mem_ascending_or_image_subgroup {H : Subgroup (Perm (Fin (n + 1)))} {i : Fin n}
    (hi : Equiv.swap i.castSucc i.succ ∈ H) {w : Perm (Fin (n + 1))} (hw : w ∈ H) :
    ((permCoxeterSystem n).length (mulSwap i w) = (permCoxeterSystem n).length w + 1)
      ∨ (∃ v ∈ H, mulSwap i v = w
          ∧ (permCoxeterSystem n).length (mulSwap i v)
              = (permCoxeterSystem n).length v + 1) := by
  rcases length_swap_cases i w with h | h
  · exact Or.inl h
  · refine Or.inr ⟨mulSwap i w, mulSwap_mem hi hw, mulSwap_mulSwap i w, ?_⟩
    rw [mulSwap_mulSwap]
    omega

end QOU.Hecke.ParabolicPairing
