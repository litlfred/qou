import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Order.Fin.Basic
import Mathlib.Tactic

/-!
# QOU.Hecke.Inversions — an ℕ-valued inversion count for `Perm (Fin n)`

Toward the braid half of the `T_w` basis (bean `qou-twwf`).

## Why this exists

`QOU.Hecke.TwBasis` proves the Hecke **quadratic** relation for the right
multiplication operators `Rs i`, using only Mathlib's `length_mul_simple`
dichotomy.  The **braid** relation needs to know *which* branch each length
comparison takes, and the textbook route to that (dihedral reduction through
parabolic cosets) needs machinery Mathlib does not have — measured: the whole
`Mathlib/GroupTheory/Coxeter/` directory is four files (`Basic`, `Inversion`,
`Length`, `Matrix`), with **no** strong exchange property, **no** parabolic
subgroups, and **no** minimal coset representatives.

For type `A` there is a concrete alternative: a descent is just a comparison of
two values, `ℓ(w sᵢ) > ℓ(w) ↔ w(i) < w(i+1)`.  Getting there needs
`ℓ = invCount`, and Mathlib has only `signAux` — the inversion **parity**, as a
`ℤˣ`-valued product — with no ℕ-valued count and no comparison to `ℓ`.  So the
count is built here.

## What is proved (sorry-free)

* `eq_one_of_strictMono` — a strictly monotone permutation of `Fin n` is the
  identity.  Via `StrictMono.orderIsoOfSurjective` and the subsingleton of
  `Fin n ≃o Fin n`.
* `invSet` / `invCount` — the inversion set and its cardinality.
* `invCount_one`.
* **`eq_one_of_invCount_eq_zero`** — no inversions implies the identity.  This is
  the base case of the `ℓ = invCount` induction.

## What is NOT proved yet

The step lemma `invCount (w * sᵢ) = invCount w ± 1`, with `+` exactly when
`w(i) < w(i+1)`; and hence `ℓ = invCount` and the descent characterisation.
That is the pair-matching bijection (pairs meeting `{i, i+1}` in one element
swap with each other; only the pair `(i, i+1)` flips) and it is the remaining
substantive step.  Nothing here bears on it.
-/

open Equiv Finset
namespace QOU.Hecke.Inversions

variable {n : ℕ}

/-- A strictly monotone permutation of `Fin n` is the identity. -/
theorem eq_one_of_strictMono {w : Perm (Fin n)} (h : StrictMono w) : w = 1 := by
  have hiso : (StrictMono.orderIsoOfSurjective (w : Fin n → Fin n) h w.surjective)
      = OrderIso.refl (Fin n) := Subsingleton.elim _ _
  ext a
  have h2 : w a = a := by
    simpa using congrArg (fun e : Fin n ≃o Fin n => e a) hiso
  exact congrArg Fin.val h2

/-- The inversion set of a permutation of `Fin n`. -/
def invSet (w : Perm (Fin n)) : Finset (Fin n × Fin n) :=
  Finset.univ.filter (fun p => p.1 < p.2 ∧ w p.2 < w p.1)

/-- The number of inversions. -/
def invCount (w : Perm (Fin n)) : ℕ := (invSet w).card

@[simp] theorem invCount_one : invCount (1 : Perm (Fin n)) = 0 := by
  simp only [invCount, invSet, Perm.coe_one, id_eq, card_eq_zero, filter_eq_empty_iff]
  rintro ⟨a, b⟩ -
  simp only [not_and, not_lt]
  exact fun h => le_of_lt h

/-- **A permutation with no inversions is the identity.** -/
theorem eq_one_of_invCount_eq_zero {w : Perm (Fin n)} (h : invCount w = 0) : w = 1 := by
  refine eq_one_of_strictMono (fun a b hab => ?_)
  by_contra hcon
  have hmem : (a, b) ∈ invSet w := by
    simp only [invSet, mem_filter, mem_univ, true_and]
    refine ⟨hab, lt_of_le_of_ne (not_lt.mp hcon) (fun he => ?_)⟩
    exact absurd (w.injective he) (ne_of_gt hab)
  exact absurd h (Finset.card_ne_zero_of_mem hmem)

end QOU.Hecke.Inversions
