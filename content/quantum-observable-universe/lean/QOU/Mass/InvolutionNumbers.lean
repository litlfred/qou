import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Perm

/-!
# Involution (telephone) numbers — the `q = 1` shadow of `S(n) = ∑_{λ⊢n} dim_q(λ)`

The binding `q`-deformation period `S(n) = ∑_{λ ⊢ n} dim_q(λ)` (see
`mass-theory/cyclotomic-boundary-at-keystone`) has `q = 1` value
`S(n)|_{q=1} = ∑_{λ ⊢ n} f^λ = I(n)`, the **involution / telephone numbers**
(OEIS A000085: `1, 1, 2, 4, 10, 26, 76, …`), by the Frobenius–Schur identity
(RSK: involutions `↔` standard Young tableaux). `I(n)` is the number of
self-inverse permutations of `n` elements and satisfies

  `I(n) = I(n-1) + (n-1)·I(n-2)`

(split an involution of `{1,…,n}` on the image of `n`: fixed — `I(n-1)`; or
swapped with one of the `n-1` others — `(n-1)·I(n-2)`).

This file is the first F1 brick: it **defines** `involutionNumber` by that
recurrence and **machine-verifies** (`decide`) that it equals the actual count
of involutions `{σ ∈ Sₙ : σ² = 1}` for `n = 0..5`, grounding the `q = 1` shadow.
The general-`n` count recurrence — the fixed-point / transposition bijection
`card(inv Sₙ₊₂) = card(inv Sₙ₊₁) + (n+1)·card(inv Sₙ)` — is the next brick (a
genuine `Equiv.Perm (Fin _)` bijection; documented, not `sorry`'d). The full F1
target (the `q`-lift `S(n)` and its cyclotomic-boundary recurrence) sits above
this on the Mathlib-absent `q`-hook-length / RSK machinery.
-/

namespace QOU.Mass

/-- The involution / telephone numbers `A000085`, defined by the two-term
recurrence `I(n) = I(n-1) + (n-1)·I(n-2)` (`I(0) = I(1) = 1`). At `q = 1` this is
`∑_{λ ⊢ n} dim_q(λ)|_{q=1} = ∑_{λ ⊢ n} f^λ`. -/
def involutionNumber : ℕ → ℕ
  | 0 => 1
  | 1 => 1
  | (n + 2) => involutionNumber (n + 1) + (n + 1) * involutionNumber n

@[simp] theorem involutionNumber_zero : involutionNumber 0 = 1 := rfl
@[simp] theorem involutionNumber_one : involutionNumber 1 = 1 := rfl

/-- The defining two-term recurrence, as a rewrite lemma. -/
theorem involutionNumber_succ_succ (n : ℕ) :
    involutionNumber (n + 2) = involutionNumber (n + 1) + (n + 1) * involutionNumber n := rfl

/-- First values: `1, 1, 2, 4, 10, 26` (A000085). -/
theorem involutionNumber_values :
    involutionNumber 2 = 2 ∧ involutionNumber 3 = 4 ∧ involutionNumber 4 = 10 ∧
      involutionNumber 5 = 26 := by
  refine ⟨rfl, rfl, rfl, rfl⟩

/-! ## The count identity, machine-verified for `n = 0..5`

`involutionNumber n` equals the number of self-inverse permutations of `Fin n`
(`{σ : Equiv.Perm (Fin n) // σ * σ = 1}`), i.e. `∑_{λ ⊢ n} f^λ` by RSK. Verified
by `decide` over the finite permutation group for `n ≤ 5`. -/

theorem card_involutions_zero :
    Fintype.card {σ : Equiv.Perm (Fin 0) // σ * σ = 1} = involutionNumber 0 := by decide
theorem card_involutions_one :
    Fintype.card {σ : Equiv.Perm (Fin 1) // σ * σ = 1} = involutionNumber 1 := by decide
theorem card_involutions_two :
    Fintype.card {σ : Equiv.Perm (Fin 2) // σ * σ = 1} = involutionNumber 2 := by decide
theorem card_involutions_three :
    Fintype.card {σ : Equiv.Perm (Fin 3) // σ * σ = 1} = involutionNumber 3 := by decide
theorem card_involutions_four :
    Fintype.card {σ : Equiv.Perm (Fin 4) // σ * σ = 1} = involutionNumber 4 := by decide
theorem card_involutions_five :
    Fintype.card {σ : Equiv.Perm (Fin 5) // σ * σ = 1} = involutionNumber 5 := by decide

end QOU.Mass
