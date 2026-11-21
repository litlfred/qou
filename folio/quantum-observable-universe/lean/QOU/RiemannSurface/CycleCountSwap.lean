import QOU.RiemannSurface.CombinatorialMapEuler
import Mathlib.Logic.Equiv.Fintype
import Mathlib.Data.Fintype.Card

/-!
# `QOU.RiemannSurface.CycleCountSwap` — a transposition changes the cycle count by ±1

Bean `qou-m3tr` (Bring milestone M3, step 2), parent `qou-qhcr`.

For a permutation `π` of a finite set and `a ≠ b`, write `c(π)` for the number of cycles of `π`,
fixed points included (`numCycles`). Then

* `numCycles_mul_swap_of_sameCycle`: if `a`, `b` lie in one cycle of `π`, the product
  `π * swap a b` has **one more** cycle (the cycle splits);
* `numCycles_mul_swap_of_not_sameCycle`: otherwise it has **one fewer** (the two cycles merge).

This is the lemma the genus inequality `c(σ) + c(α) + c(σα) ≤ |D| + 2` for connected maps
needs (proof plan in bean `qou-m3tr`). Mathlib has no version of it.

## Proof

`ρ = π * swap a b` agrees with `π` off `T = {a, b}`. A cycle of `π` that avoids `T` is iterated
identically by `ρ`, so it is a cycle of `ρ` and conversely (`sameCycle_iff_of_avoids`); hence
both permutations have the same number `N` of cycles avoiding `T`. The cycles meeting `T` number
`M ∈ {1, 2}`, with `M = 1` exactly when `a` and `b` share a cycle. So `c = N + M` on both sides
and `|c(ρ) − c(π)| ≤ 1`. The sign homomorphism (`sign_eq_neg_one_pow`) forces `c(ρ) + c(π)`
odd, which excludes `0` and fixes the sign of the change.
-/

namespace QOU.RiemannSurface.CycleCountSwap

open Equiv Equiv.Perm
open QOU.RiemannSurface.CombinatorialMapEuler

set_option linter.unusedSectionVars false

variable {D : Type*} [Fintype D] [DecidableEq D]

/-- The cycle of `x` under `π` avoids `a` and `b`. -/
def Avoids (π : Perm D) (a b x : D) : Prop := ¬ π.SameCycle x a ∧ ¬ π.SameCycle x b

/-- `ρ` agrees with `π` off `{a, b}`. -/
def Agree (π ρ : Perm D) (a b : D) : Prop := ∀ x, x ≠ a → x ≠ b → ρ x = π x

theorem agree_mul_swap (π : Perm D) (a b : D) : Agree π (π * swap a b) a b := by
  intro x ha hb; simp [Perm.mul_apply, swap_apply_of_ne_of_ne ha hb]

theorem agree_symm_mul_swap (π : Perm D) (a b : D) : Agree (π * swap a b) π a b := by
  intro x ha hb; simp [Perm.mul_apply, swap_apply_of_ne_of_ne ha hb]

theorem pow_ne_of_avoids {π : Perm D} {a b x : D} (h : Avoids π a b x) (j : ℕ) :
    (π ^ j) x ≠ a ∧ (π ^ j) x ≠ b := by
  refine ⟨fun hj => h.1 ⟨(j : ℤ), by rw [zpow_natCast, hj]⟩,
    fun hj => h.2 ⟨(j : ℤ), by rw [zpow_natCast, hj]⟩⟩

theorem pow_eq_of_avoids {π ρ : Perm D} {a b x : D} (hag : Agree π ρ a b)
    (h : Avoids π a b x) (j : ℕ) : (ρ ^ j) x = (π ^ j) x := by
  induction j with
  | zero => rfl
  | succ j ih =>
    rw [pow_succ', pow_succ', Perm.mul_apply, Perm.mul_apply, ih]
    exact hag _ (pow_ne_of_avoids h j).1 (pow_ne_of_avoids h j).2

/-- On a cycle avoiding `{a, b}`, `π` and `ρ` have the same cycle relation. -/
theorem sameCycle_iff_of_avoids {π ρ : Perm D} {a b x : D} (hag : Agree π ρ a b)
    (h : Avoids π a b x) (y : D) : π.SameCycle x y ↔ ρ.SameCycle x y := by
  constructor
  · intro hxy
    obtain ⟨n, -, hn⟩ := hxy.exists_pow_eq'
    exact ⟨(n : ℤ), by rw [zpow_natCast, pow_eq_of_avoids hag h n, hn]⟩
  · intro hxy
    obtain ⟨n, -, hn⟩ := hxy.exists_pow_eq'
    exact ⟨(n : ℤ), by rw [zpow_natCast, ← pow_eq_of_avoids hag h n, hn]⟩

theorem avoids_of_avoids {π ρ : Perm D} {a b x : D} (hag : Agree π ρ a b)
    (h : Avoids π a b x) : Avoids ρ a b x :=
  ⟨fun h' => h.1 ((sameCycle_iff_of_avoids hag h a).2 h'),
   fun h' => h.2 ((sameCycle_iff_of_avoids hag h b).2 h')⟩

/-! ### Splitting the cycles into those meeting `{a, b}` and the rest -/

/-- A cycle meets `{a, b}`. -/
def Meets (π : Perm D) (a b : D) : Quotient (SameCycle.setoid π) → Prop :=
  Quotient.lift (fun x => π.SameCycle x a ∨ π.SameCycle x b) fun x y (hxy : π.SameCycle x y) =>
    propext ⟨fun h => h.imp (fun h' => hxy.symm.trans h') (fun h' => hxy.symm.trans h'),
      fun h => h.imp (fun h' => hxy.trans h') (fun h' => hxy.trans h')⟩

/-- The restricted cycle relation on darts whose `π`-cycle avoids `{a, b}`. -/
def avoidSetoid (π : Perm D) (a b : D) : Setoid {x // Avoids π a b x} :=
  Setoid.comap Subtype.val (SameCycle.setoid π)

/-- Cycles of `π` avoiding `{a, b}` = classes of the restricted relation. -/
def avoidEquivSelf (π : Perm D) (a b : D) :
    {q // ¬ Meets π a b q} ≃ Quotient (avoidSetoid π a b) :=
  Equiv.subtypeQuotientEquivQuotientSubtype (Avoids π a b) (fun q => ¬ Meets π a b q)
    (fun x => by simp [Meets, Avoids, not_or]) (fun _ _ => Iff.rfl)

/-- Cycles of `ρ` avoiding `{a, b}` = the same classes, when `ρ` agrees with `π` off `{a, b}`. -/
def avoidEquivOther {π ρ : Perm D} {a b : D} (hag : Agree π ρ a b) (hag' : Agree ρ π a b) :
    {q // ¬ Meets ρ a b q} ≃ Quotient (avoidSetoid π a b) :=
  Equiv.subtypeQuotientEquivQuotientSubtype (Avoids π a b) (fun q => ¬ Meets ρ a b q)
    (fun x => by
      show Avoids π a b x ↔ ¬ (ρ.SameCycle x a ∨ ρ.SameCycle x b)
      rw [not_or]
      exact ⟨fun h => avoids_of_avoids hag h, fun h => avoids_of_avoids hag' h⟩)
    (fun x y => by
      show π.SameCycle x.1 y.1 ↔ ρ.SameCycle x.1 y.1
      exact sameCycle_iff_of_avoids hag x.2 y.1)

theorem numCycles_eq (π : Perm D) (a b : D) :
    numCycles π = Nat.card {q // Meets π a b q} + Nat.card {q // ¬ Meets π a b q} := by
  classical
  unfold numCycles
  rw [← Nat.card_sum]
  exact Nat.card_congr (Equiv.sumCompl _).symm

/-- The cycles meeting `{a, b}` are the classes of `a` and of `b`. -/
theorem meets_iff (π : Perm D) (a b : D) (q : Quotient (SameCycle.setoid π)) :
    Meets π a b q ↔ q = Quotient.mk _ a ∨ q = Quotient.mk _ b := by
  induction q using Quotient.inductionOn with
  | h x =>
    show (π.SameCycle x a ∨ π.SameCycle x b) ↔ _
    rw [Quotient.eq, Quotient.eq]
    rfl

theorem card_meets_le (π : Perm D) (a b : D) : Nat.card {q // Meets π a b q} ≤ 2 := by
  have hs : Function.Surjective
      (fun i : Bool => (⟨Quotient.mk _ (if i then a else b), by
        rw [meets_iff]; cases i <;> simp⟩ : {q // Meets π a b q})) := by
    rintro ⟨q, hq⟩
    rcases (meets_iff π a b q).1 hq with rfl | rfl
    · exact ⟨true, rfl⟩
    · exact ⟨false, rfl⟩
  simpa using Nat.card_le_card_of_surjective _ hs

theorem card_meets_pos (π : Perm D) (a b : D) : 1 ≤ Nat.card {q // Meets π a b q} :=
  Nat.one_le_iff_ne_zero.2 (Nat.card_ne_zero.2
    ⟨⟨⟨Quotient.mk _ a, (meets_iff π a b _).2 (Or.inl rfl)⟩⟩, inferInstance⟩)

theorem card_meets_of_sameCycle {π : Perm D} {a b : D} (h : π.SameCycle a b) :
    Nat.card {q // Meets π a b q} = 1 := by
  have hab : (Quotient.mk (SameCycle.setoid π) a) = Quotient.mk _ b := Quotient.sound h
  rw [Nat.card_eq_one_iff_exists]
  refine ⟨⟨Quotient.mk _ a, (meets_iff π a b _).2 (Or.inl rfl)⟩, ?_⟩
  rintro ⟨q, hq⟩
  apply Subtype.ext
  rcases (meets_iff π a b q).1 hq with rfl | rfl
  · rfl
  · exact hab.symm

theorem card_meets_of_not_sameCycle {π : Perm D} {a b : D} (h : ¬ π.SameCycle a b) :
    Nat.card {q // Meets π a b q} = 2 := by
  have hi : Function.Injective
      (fun i : Bool => (⟨Quotient.mk _ (if i then a else b), by
        rw [meets_iff]; cases i <;> simp⟩ : {q // Meets π a b q})) := by
    intro i j hij
    have hq := congrArg Subtype.val hij
    cases i <;> cases j
    · rfl
    · exact absurd (Quotient.exact hq).symm h
    · exact absurd (Quotient.exact hq) h
    · rfl
  have h2 := Nat.card_le_card_of_injective _ hi
  have := card_meets_le π a b
  simp at h2
  omega

/-! ### Parity from the sign -/

theorem odd_add_numCycles_mul_swap (π : Perm D) {a b : D} (hab : a ≠ b) :
    (numCycles (π * swap a b) + numCycles π) % 2 = 1 := by
  have hs := sign_mul π (swap a b)
  rw [sign_swap hab, sign_eq_neg_one_pow, sign_eq_neg_one_pow] at hs
  have h1 : ((-1 : ℤˣ)) ^ (Fintype.card D + numCycles (π * swap a b) +
      (Fintype.card D + numCycles π)) = -1 := by
    rw [pow_add, hs]
    rcases Int.units_eq_one_or ((-1 : ℤˣ) ^ (Fintype.card D + numCycles π)) with h | h <;>
      rw [h] <;> decide
  have hne : ¬ Even (Fintype.card D + numCycles (π * swap a b) +
      (Fintype.card D + numCycles π)) := by
    intro he
    rw [he.neg_one_pow] at h1
    exact absurd h1 (by decide)
  rw [Nat.not_even_iff] at hne
  omega

/-! ### The ±1 law -/

theorem numCycles_mul_swap_of_sameCycle (π : Perm D) {a b : D} (hab : a ≠ b)
    (h : π.SameCycle a b) : numCycles (π * swap a b) = numCycles π + 1 := by
  have hN : Nat.card {q // ¬ Meets (π * swap a b) a b q} = Nat.card {q // ¬ Meets π a b q} :=
    Nat.card_congr ((avoidEquivOther (agree_mul_swap π a b)
      (agree_symm_mul_swap π a b)).trans (avoidEquivSelf π a b).symm)
  have hρ := numCycles_eq (π * swap a b) a b
  have hπ := numCycles_eq π a b
  have hMπ := card_meets_of_sameCycle h
  have hle := card_meets_le (π * swap a b) a b
  have hpos := card_meets_pos (π * swap a b) a b
  have hodd := odd_add_numCycles_mul_swap π hab
  omega

theorem numCycles_mul_swap_of_not_sameCycle (π : Perm D) {a b : D}
    (h : ¬ π.SameCycle a b) : numCycles (π * swap a b) + 1 = numCycles π := by
  have hab : a ≠ b := fun e => h (e ▸ SameCycle.refl _ _)
  have hN : Nat.card {q // ¬ Meets (π * swap a b) a b q} = Nat.card {q // ¬ Meets π a b q} :=
    Nat.card_congr ((avoidEquivOther (agree_mul_swap π a b)
      (agree_symm_mul_swap π a b)).trans (avoidEquivSelf π a b).symm)
  have hρ := numCycles_eq (π * swap a b) a b
  have hπ := numCycles_eq π a b
  have hMπ := card_meets_of_not_sameCycle h
  have hle := card_meets_le (π * swap a b) a b
  have hpos := card_meets_pos (π * swap a b) a b
  have hodd := odd_add_numCycles_mul_swap π hab
  omega

end QOU.RiemannSurface.CycleCountSwap
