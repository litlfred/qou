import Mathlib.GroupTheory.Perm.Basic
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Sigma
import Mathlib.Algebra.Group.End

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

This file **defines** `involutionNumber` by that recurrence and **proves**
(`card_involutions_eq_involutionNumber`) that it equals the actual count of
involutions `{σ ∈ Sₙ : σ² = 1}` for **all** `n`, grounding the `q = 1` shadow.
The proof is a clean bijective argument: strong (two-step) induction on `n`,
reduced to the count recurrence
`card(inv Sₙ₊₂) = card(inv Sₙ₊₁) + (n+1)·card(inv Sₙ)`, which is proved by
splitting an involution `σ` on `p := σ 0` (fixed-point vs transposition) via the
point-restriction bijection `involSubtypeEquiv`. Sorry-free (axioms:
`propext, Classical.choice, Quot.sound`).

The full F1 target (the `q`-lift `S(n)` and its cyclotomic-boundary recurrence)
sits above this on the Mathlib-absent `q`-hook-length / RSK machinery.
-/

namespace QOU.Mass

open Equiv

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

/-! ## The general count identity `card(involutions of Fin n) = involutionNumber n`

We prove the identity for **all** `n` by two-step induction, the inductive step
being the count recurrence
`card(inv Fin (n+2)) = card(inv Fin (n+1)) + (n+1)·card(inv Fin n)`. -/

section Count

variable {α : Type*} [DecidableEq α]

/-- `swap a b * σ` is again an involution when `σ` is and `swap (σ a) (σ b) = swap a b`
(i.e. `σ` either swaps or fixes the pair `a, b`). -/
private theorem swap_mul_involutive {σ : Perm α} {a b : α}
    (hσ : σ * σ = 1) (hab : Equiv.swap (σ a) (σ b) = Equiv.swap a b) :
    (Equiv.swap a b * σ) * (Equiv.swap a b * σ) = 1 := by
  apply Equiv.ext
  intro y
  simp only [Equiv.Perm.mul_apply, Equiv.Perm.one_apply]
  rw [σ.injective.map_swap a b (σ y), hab, Equiv.swap_apply_self,
    ← Equiv.Perm.mul_apply, hσ, Equiv.Perm.one_apply]

/-- Point-restriction bijection: involutions of `α` fixing the complement of `pr`
correspond bijectively to involutions of the subtype `pr`. -/
private def involSubtypeEquiv (pr : α → Prop) [DecidablePred pr] :
    {τ : Perm (Subtype pr) // τ * τ = 1} ≃
      {σ : Perm α // σ * σ = 1 ∧ ∀ a, ¬ pr a → σ a = a} :=
  ((Equiv.Perm.subtypeEquivSubtypePerm pr).subtypeEquiv
      (p := fun τ => τ * τ = 1)
      (q := fun g : {f : Perm α // ∀ a, ¬ pr a → f a = a} => (g : Perm α) * (g : Perm α) = 1)
      (fun τ => by
        simp only [Equiv.Perm.subtypeEquivSubtypePerm_apply_coe]
        constructor
        · intro h; rw [← map_mul, h, map_one]
        · intro h
          exact Equiv.Perm.ofSubtype_injective (by rw [map_mul, map_one]; exact h))).trans
    ((Equiv.subtypeSubtypeEquivSubtypeInter (fun σ => ∀ a, ¬ pr a → σ a = a)
      (fun σ : Perm α => σ * σ = 1)).trans
      (Equiv.subtypeEquivRight (fun _ => and_comm)))

end Count

/-- Number of involutions of `Fin n`. -/
private def numInv (n : ℕ) : ℕ := Fintype.card {σ : Equiv.Perm (Fin n) // σ * σ = 1}

/-- Transport the involution count along a bijection to `Fin n`. -/
private theorem card_invol_eq_numInv {α : Type*} [DecidableEq α] [Fintype α] (n : ℕ)
    (e : α ≃ Fin n) :
    Fintype.card {σ : Equiv.Perm α // σ * σ = 1} = numInv n := by
  apply Fintype.card_congr
  have hmul : ∀ σ τ : Equiv.Perm α, e.permCongr (σ * τ) = e.permCongr σ * e.permCongr τ := by
    intro σ τ; ext x; simp [Equiv.permCongr_apply, Equiv.Perm.mul_apply]
  have hone : e.permCongr (1 : Equiv.Perm α) = 1 := by ext x; simp [Equiv.permCongr_apply]
  refine e.permCongr.subtypeEquiv (fun σ => ?_)
  constructor
  · intro h; rw [← hmul, h, hone]
  · intro h
    apply e.permCongr.injective
    rw [hmul σ σ, hone]
    exact h

/-- Involutions of `Fin (m+1)` fixing `0` are counted by `numInv m`. -/
private theorem card_fix0 (m : ℕ) :
    Fintype.card {σ : Equiv.Perm (Fin (m + 1)) // σ * σ = 1 ∧ σ 0 = 0} = numInv m := by
  have e : {a : Fin (m + 1) // a ≠ 0} ≃ Fin m := Fintype.equivFinOfCardEq (by
    rw [Fintype.card_subtype_compl, Fintype.card_subtype_eq]; simp)
  have hiff : ∀ σ : Equiv.Perm (Fin (m + 1)),
      (σ * σ = 1 ∧ σ 0 = 0) ↔ (σ * σ = 1 ∧ ∀ a, ¬ (a ≠ 0) → σ a = a) := fun σ =>
    and_congr_right fun _ =>
      ⟨fun h a ha => by rw [not_ne_iff.mp ha]; exact h, fun h => h 0 (by simp)⟩
  rw [Fintype.card_congr (Equiv.subtypeEquivRight hiff),
    ← Fintype.card_congr (involSubtypeEquiv (fun a : Fin (m + 1) => a ≠ 0)),
    card_invol_eq_numInv m e]

/-- Involutions of `Fin (n+2)` fixing both `0` and `p ≠ 0` are counted by `numInv n`. -/
private theorem card_fix2 (n : ℕ) (p : Fin (n + 2)) (hp : p ≠ 0) :
    Fintype.card {σ : Equiv.Perm (Fin (n + 2)) // σ * σ = 1 ∧ σ 0 = 0 ∧ σ p = p} = numInv n := by
  have hcard : Fintype.card {a : Fin (n + 2) // a ≠ 0 ∧ a ≠ p} = n := by
    have hfilter : (Finset.univ.filter (fun a : Fin (n + 2) => a ≠ 0 ∧ a ≠ p))
        = Finset.univ \ {0, p} := by
      ext a
      simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_sdiff,
        Finset.mem_insert, Finset.mem_singleton, not_or]
    rw [Fintype.card_subtype, hfilter, Finset.card_univ_diff, Fintype.card_fin,
      Finset.card_pair (Ne.symm hp)]
    omega
  have e : {a : Fin (n + 2) // a ≠ 0 ∧ a ≠ p} ≃ Fin n := Fintype.equivFinOfCardEq hcard
  have hiff : ∀ σ : Equiv.Perm (Fin (n + 2)),
      (σ * σ = 1 ∧ σ 0 = 0 ∧ σ p = p) ↔ (σ * σ = 1 ∧ ∀ a, ¬ (a ≠ 0 ∧ a ≠ p) → σ a = a) := fun σ =>
    and_congr_right fun _ =>
      ⟨fun h a ha => by
          rcases not_and_or.mp ha with h' | h'
          · rw [not_not.mp h']; exact h.1
          · rw [not_not.mp h']; exact h.2,
       fun h => ⟨h 0 (by simp), h p (by simp)⟩⟩
  rw [Fintype.card_congr (Equiv.subtypeEquivRight hiff),
    ← Fintype.card_congr (involSubtypeEquiv (fun a : Fin (n + 2) => a ≠ 0 ∧ a ≠ p)),
    card_invol_eq_numInv n e]

/-- The fiber `{σ involution : σ 0 = p}` (for `p ≠ 0`) is equivalent, via multiplication
by the transposition `swap 0 p`, to involutions fixing both `0` and `p`. -/
private def fiberNeEquiv (n : ℕ) (p : Fin (n + 2)) :
    {σ : {σ : Equiv.Perm (Fin (n + 2)) // σ * σ = 1} // (σ : Equiv.Perm (Fin (n + 2))) 0 = p}
      ≃ {σ : Equiv.Perm (Fin (n + 2)) // σ * σ = 1 ∧ σ 0 = 0 ∧ σ p = p} where
  toFun := fun ⟨⟨σ, hσ⟩, h0⟩ =>
    ⟨Equiv.swap 0 p * σ, by
      have hσp : σ p = 0 := by
        have : σ (σ 0) = 0 := by rw [← Equiv.Perm.mul_apply, hσ, Equiv.Perm.one_apply]
        rwa [h0] at this
      refine ⟨swap_mul_involutive hσ (by rw [h0, hσp]; exact Equiv.swap_comm p 0), ?_, ?_⟩
      · rw [Equiv.Perm.mul_apply, h0, Equiv.swap_apply_right]
      · rw [Equiv.Perm.mul_apply, hσp, Equiv.swap_apply_left]⟩
  invFun := fun ⟨σ, hσ, hσ0, hσp⟩ =>
    ⟨⟨Equiv.swap 0 p * σ, swap_mul_involutive hσ (by rw [hσ0, hσp])⟩, by
      rw [Equiv.Perm.mul_apply, hσ0, Equiv.swap_apply_left]⟩
  left_inv := fun ⟨⟨σ, hσ⟩, h0⟩ => by
    apply Subtype.ext
    apply Subtype.ext
    show Equiv.swap 0 p * (Equiv.swap 0 p * σ) = σ
    rw [← mul_assoc, Equiv.swap_mul_self, one_mul]
  right_inv := fun ⟨σ, hσ, hσ0, hσp⟩ => by
    apply Subtype.ext
    show Equiv.swap 0 p * (Equiv.swap 0 p * σ) = σ
    rw [← mul_assoc, Equiv.swap_mul_self, one_mul]

/-- The count of `σ 0 = p` involutions of `Fin (n+2)`, for `p ≠ 0`, is `numInv n`. -/
private theorem card_fiber_ne (n : ℕ) (p : Fin (n + 2)) (hp : p ≠ 0) :
    Fintype.card {σ : {σ : Equiv.Perm (Fin (n + 2)) // σ * σ = 1} //
      (σ : Equiv.Perm (Fin (n + 2))) 0 = p} = numInv n := by
  rw [Fintype.card_congr (fiberNeEquiv n p), card_fix2 n p hp]

/-- The count of `σ 0 = 0` involutions of `Fin (n+2)` is `numInv (n+1)`. -/
private theorem card_fiber_zero (n : ℕ) :
    Fintype.card {σ : {σ : Equiv.Perm (Fin (n + 2)) // σ * σ = 1} //
      (σ : Equiv.Perm (Fin (n + 2))) 0 = 0} = numInv (n + 1) := by
  rw [Fintype.card_congr (Equiv.subtypeSubtypeEquivSubtypeInter
        (fun σ : Equiv.Perm (Fin (n + 2)) => σ * σ = 1) (fun σ => σ 0 = 0)),
    card_fix0 (n + 1)]

/-- The count recurrence: `numInv (n+2) = numInv (n+1) + (n+1) * numInv n`,
obtained by fibering an involution of `Fin (n+2)` over its value `σ 0`. -/
private theorem numInv_succ_succ (n : ℕ) :
    numInv (n + 2) = numInv (n + 1) + (n + 1) * numInv n := by
  have hL : numInv (n + 2) = ∑ p : Fin (n + 2),
      Fintype.card {σ : {σ : Equiv.Perm (Fin (n + 2)) // σ * σ = 1} //
        (σ : Equiv.Perm (Fin (n + 2))) 0 = p} := by
    rw [numInv, ← Fintype.card_sigma]
    exact Fintype.card_congr (Equiv.sigmaFiberEquiv _).symm
  rw [hL, ← Finset.add_sum_erase _ _ (Finset.mem_univ (0 : Fin (n + 2)))]
  congr 1
  · exact card_fiber_zero n
  · have hbody : ∀ p ∈ Finset.univ.erase (0 : Fin (n + 2)),
        Fintype.card {σ : {σ : Equiv.Perm (Fin (n + 2)) // σ * σ = 1} //
          (σ : Equiv.Perm (Fin (n + 2))) 0 = p} = numInv n :=
      fun p hp => card_fiber_ne n p (Finset.ne_of_mem_erase hp)
    rw [Finset.sum_congr rfl hbody, Finset.sum_const, smul_eq_mul]
    congr 1
    rw [Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ, Fintype.card_fin]
    omega

private theorem numInv_eq_involutionNumber (n : ℕ) : numInv n = involutionNumber n := by
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    match n with
    | 0 => decide
    | 1 => decide
    | (m + 2) =>
      rw [numInv_succ_succ, involutionNumber, ih (m + 1) (by omega), ih m (by omega)]

/-- **General count identity.** The number of involutions (self-inverse permutations)
of `Fin n` equals `involutionNumber n`, for every `n`. Equivalently, `involutionNumber`
counts `∑_{λ ⊢ n} f^λ` by the Frobenius–Schur / RSK correspondence. -/
theorem card_involutions_eq_involutionNumber (n : ℕ) :
    Fintype.card {σ : Equiv.Perm (Fin n) // σ * σ = 1} = involutionNumber n :=
  numInv_eq_involutionNumber n

/-! ## Small-`n` corollaries (`n = 0..5`, A000085 `1,1,2,4,10,26`)

These now follow from the general identity above (previously verified independently by
`decide`); together with `involutionNumber_values` they pin the numeric counts. -/

theorem card_involutions_zero :
    Fintype.card {σ : Equiv.Perm (Fin 0) // σ * σ = 1} = involutionNumber 0 :=
  card_involutions_eq_involutionNumber 0
theorem card_involutions_one :
    Fintype.card {σ : Equiv.Perm (Fin 1) // σ * σ = 1} = involutionNumber 1 :=
  card_involutions_eq_involutionNumber 1
theorem card_involutions_two :
    Fintype.card {σ : Equiv.Perm (Fin 2) // σ * σ = 1} = involutionNumber 2 :=
  card_involutions_eq_involutionNumber 2
theorem card_involutions_three :
    Fintype.card {σ : Equiv.Perm (Fin 3) // σ * σ = 1} = involutionNumber 3 :=
  card_involutions_eq_involutionNumber 3
theorem card_involutions_four :
    Fintype.card {σ : Equiv.Perm (Fin 4) // σ * σ = 1} = involutionNumber 4 :=
  card_involutions_eq_involutionNumber 4
theorem card_involutions_five :
    Fintype.card {σ : Equiv.Perm (Fin 5) // σ * σ = 1} = involutionNumber 5 :=
  card_involutions_eq_involutionNumber 5

end QOU.Mass
