/-!
# QOU.Mathlib.PermutationEnumeration — `Fin n! ≃ Equiv.Perm (Fin n)`

For the QOU substrate's per-σ_i action tables on `H_4`, `H_5`,
`H_6`, we need a concrete enumeration of the basis elements of
`H_n(q)` indexed by `Fin n.factorial`.  Since `H_n(q)` has basis
`{T_w : w ∈ S_n}` and `|S_n| = n!`, this amounts to a bijection
`Fin n.factorial ≃ Equiv.Perm (Fin n)`.

Mathlib supplies `Fintype.card_perm : Fintype.card (Equiv.Perm α)
= (Fintype.card α).factorial` and `Fintype.equivFinOfCardEq` to
build the bijection.

This file packages the result as
`permutationEnumeration : Fin n.factorial ≃ Equiv.Perm (Fin n)`,
ready for use in encoding the H_n basis.

**File status**: small upstream-shaped helper using
existing Mathlib infrastructure.
-/

import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Perm

namespace QOU.Mathlib.PermutationEnumeration

/-- The cardinality of `Equiv.Perm (Fin n)` equals `n!`. -/
theorem card_perm_fin (n : ℕ) :
    Fintype.card (Equiv.Perm (Fin n)) = n.factorial := by
  rw [Fintype.card_perm, Fintype.card_fin]

/-- **Permutation enumeration**: a bijection
    `Fin n.factorial ≃ Equiv.Perm (Fin n)`.

    Construction: `Equiv.Perm (Fin n)` is finite of cardinality
    `n!` (via `Fintype.card_perm` + `Fintype.card_fin`).
    Use Mathlib's `Fintype.equivFinOfCardEq` to convert. -/
noncomputable def permutationEnumeration (n : ℕ) :
    Fin n.factorial ≃ Equiv.Perm (Fin n) :=
  (Fintype.equivFinOfCardEq (card_perm_fin n)).symm

/-- **Sanity**: at `n = 0`, `|Perm (Fin 0)| = 1`. -/
theorem permutationCount_n_zero :
    Fintype.card (Equiv.Perm (Fin 0)) = 1 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 2`, `|Perm (Fin 2)| = 2`. -/
theorem permutationCount_n_two :
    Fintype.card (Equiv.Perm (Fin 2)) = 2 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 3`, `|Perm (Fin 3)| = 6`. -/
theorem permutationCount_n_three :
    Fintype.card (Equiv.Perm (Fin 3)) = 6 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 4`, `|Perm (Fin 4)| = 24`. -/
theorem permutationCount_n_four :
    Fintype.card (Equiv.Perm (Fin 4)) = 24 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 5`, `|Perm (Fin 5)| = 120`. -/
theorem permutationCount_n_five :
    Fintype.card (Equiv.Perm (Fin 5)) = 120 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-- At `n = 6`, `|Perm (Fin 6)| = 720`. -/
theorem permutationCount_n_six :
    Fintype.card (Equiv.Perm (Fin 6)) = 720 := by
  rw [Fintype.card_perm, Fintype.card_fin]; rfl

/-! ### Concrete simple transpositions σ_i ∈ S_n

    The Hecke generator `σ_i` lifts from the simple
    transposition `s_i ∈ S_n` swapping `i` and `i+1`.
    Mathlib's `Equiv.swap` supplies these directly. -/

/-- Simple transposition `σ_i ∈ S_n`: swap positions `i` and
    `i+1` (with `i+1 < n`). -/
def simpleTransposition {n : ℕ} (i : Fin n) (h : i.val + 1 < n) :
    Equiv.Perm (Fin n) :=
  Equiv.swap i ⟨i.val + 1, h⟩

/-- σ_1 in S_3: swap positions 1 and 2. -/
def sigma1_in_S3 : Equiv.Perm (Fin 3) :=
  simpleTransposition (n := 3) ⟨0, by decide⟩ (by decide)

/-- σ_2 in S_3: swap positions 2 and 3. -/
def sigma2_in_S3 : Equiv.Perm (Fin 3) :=
  simpleTransposition (n := 3) ⟨1, by decide⟩ (by decide)

/-- σ_1 in S_4: swap positions 1 and 2. -/
def sigma1_in_S4 : Equiv.Perm (Fin 4) :=
  simpleTransposition (n := 4) ⟨0, by decide⟩ (by decide)

/-- σ_2 in S_4: swap positions 2 and 3. -/
def sigma2_in_S4 : Equiv.Perm (Fin 4) :=
  simpleTransposition (n := 4) ⟨1, by decide⟩ (by decide)

/-- σ_3 in S_4: swap positions 3 and 4. -/
def sigma3_in_S4 : Equiv.Perm (Fin 4) :=
  simpleTransposition (n := 4) ⟨2, by decide⟩ (by decide)

/-- Each simple transposition has order 2 (i.e., is its own
    inverse).  This is `Equiv.swap_self` applied twice. -/
theorem simpleTransposition_sq {n : ℕ} (i : Fin n) (h : i.val + 1 < n) :
    (simpleTransposition i h) * (simpleTransposition i h) = 1 := by
  unfold simpleTransposition
  exact Equiv.swap_mul_self i ⟨i.val + 1, h⟩

end QOU.Mathlib.PermutationEnumeration
