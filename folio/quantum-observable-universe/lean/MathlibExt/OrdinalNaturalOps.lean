/-
Copyright (c) 2022 Violeta Hernández Palacios. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Violeta Hernández Palacios
-/
import Mathlib.SetTheory.Ordinal.Family
import Mathlib.Tactic.Abel

/-!
# Natural addition on ordinals (port of the removed `Mathlib.SetTheory.Ordinal.NaturalOps`)

Mathlib removed `Mathlib.SetTheory.Ordinal.NaturalOps` after deprecating it on 2025-08-06; the
material now lives in the combinatorial-games repository (`CombinatorialGames.NatOrdinal`),
which is not a dependency here. QOU's surreal-birthday bounds (`QOU.Observations.*`) use the
Hessenberg natural sum `Ordinal.nadd` and a handful of its lemmas, so this file carries the
natural-addition part of that module verbatim from Mathlib commit f897ebc (the v4.24 pin),
under its original Apache 2.0 licence and authorship. Only the deprecated `blsub` lemma and the unused
`add_le_nadd` are left out, and `nadd_nat`'s proof is re-spelled for renamed successor lemmas; natural multiplication and the `NatOrdinal` type synonym are not
used here and are not ported.
-/

universe u v

open Function Order Set

noncomputable section

namespace Ordinal

variable {a b c : Ordinal.{u}}


/-- Natural addition on ordinals `a ♯ b`, also known as the Hessenberg sum, is recursively defined
as the least ordinal greater than `a' ♯ b` and `a ♯ b'` for all `a' < a` and `b' < b`. In contrast
to normal ordinal addition, it is commutative.

Natural addition can equivalently be characterized as the ordinal resulting from adding up
corresponding coefficients in the Cantor normal forms of `a` and `b`. -/
noncomputable def nadd (a b : Ordinal.{u}) : Ordinal.{u} :=
  max (⨆ x : Iio a, succ (nadd x.1 b)) (⨆ x : Iio b, succ (nadd a x.1))
termination_by (a, b)
decreasing_by all_goals cases x; decreasing_tactic

@[inherit_doc]
scoped[NaturalOps] infixl:65 " ♯ " => Ordinal.nadd

open NaturalOps

/-! ### Natural addition -/

theorem lt_nadd_iff : a < b ♯ c ↔ (∃ b' < b, a ≤ b' ♯ c) ∨ ∃ c' < c, a ≤ b ♯ c' := by
  rw [nadd]
  simp [Ordinal.lt_iSup_iff]

theorem nadd_le_iff : b ♯ c ≤ a ↔ (∀ b' < b, b' ♯ c < a) ∧ ∀ c' < c, b ♯ c' < a := by
  rw [← not_lt, lt_nadd_iff]
  simp

theorem nadd_lt_nadd_left (h : b < c) (a) : a ♯ b < a ♯ c :=
  lt_nadd_iff.2 (Or.inr ⟨b, h, le_rfl⟩)

theorem nadd_lt_nadd_right (h : b < c) (a) : b ♯ a < c ♯ a :=
  lt_nadd_iff.2 (Or.inl ⟨b, h, le_rfl⟩)

theorem nadd_le_nadd_left (h : b ≤ c) (a) : a ♯ b ≤ a ♯ c := by
  rcases lt_or_eq_of_le h with (h | rfl)
  · exact (nadd_lt_nadd_left h a).le
  · exact le_rfl

theorem nadd_le_nadd_right (h : b ≤ c) (a) : b ♯ a ≤ c ♯ a := by
  rcases lt_or_eq_of_le h with (h | rfl)
  · exact (nadd_lt_nadd_right h a).le
  · exact le_rfl

variable (a b)

theorem nadd_comm (a b) : a ♯ b = b ♯ a := by
  rw [nadd, nadd, max_comm]
  congr <;> ext x <;> cases x <;> apply congr_arg _ (nadd_comm _ _)
termination_by (a, b)

private theorem iSup_nadd_of_monotone {a b} (f : Ordinal.{u} → Ordinal.{u}) (h : Monotone f) :
    ⨆ x : Iio (a ♯ b), f x = max (⨆ a' : Iio a, f (a'.1 ♯ b)) (⨆ b' : Iio b, f (a ♯ b'.1)) := by
  apply (max_le _ _).antisymm'
  · rw [Ordinal.iSup_le_iff]
    rintro ⟨i, hi⟩
    obtain ⟨x, hx, hi⟩ | ⟨x, hx, hi⟩ := lt_nadd_iff.1 hi
    · exact le_max_of_le_left ((h hi).trans <| Ordinal.le_iSup (fun x : Iio a ↦ _) ⟨x, hx⟩)
    · exact le_max_of_le_right ((h hi).trans <| Ordinal.le_iSup (fun x : Iio b ↦ _) ⟨x, hx⟩)
  all_goals
    apply csSup_le_csSup' bddAbove_of_small
    rintro _ ⟨⟨c, hc⟩, rfl⟩
    refine mem_range_self (⟨_, ?_⟩ : Iio _)
    apply_rules [nadd_lt_nadd_left, nadd_lt_nadd_right]


theorem nadd_assoc (a b c) : a ♯ b ♯ c = a ♯ (b ♯ c) := by
  unfold nadd
  rw [iSup_nadd_of_monotone fun a' ↦ succ (a' ♯ c), iSup_nadd_of_monotone fun b' ↦ succ (a ♯ b'),
    max_assoc]
  · congr <;> ext x <;> cases x <;> apply congr_arg _ (nadd_assoc _ _ _)
  · exact succ_mono.comp fun x y h ↦ nadd_le_nadd_left h _
  · exact succ_mono.comp fun x y h ↦ nadd_le_nadd_right h _
termination_by (a, b, c)

@[simp]
theorem nadd_zero (a : Ordinal) : a ♯ 0 = a := by
  rw [nadd, ciSup_of_empty fun _ : Iio 0 ↦ _, sup_bot_eq]
  convert iSup_succ a
  rename_i x
  cases x
  exact nadd_zero _
termination_by a

@[simp]
theorem zero_nadd : 0 ♯ a = a := by rw [nadd_comm, nadd_zero]

@[simp]
theorem nadd_one (a : Ordinal) : a ♯ 1 = succ a := by
  rw [nadd, ciSup_unique (s := fun _ : Iio 1 ↦ _), Iio_one_default_eq, nadd_zero,
    max_eq_right_iff, Ordinal.iSup_le_iff]
  rintro ⟨i, hi⟩
  rwa [nadd_one, succ_le_succ_iff, succ_le_iff]
termination_by a

@[simp]
theorem one_nadd : 1 ♯ a = succ a := by rw [nadd_comm, nadd_one]

theorem nadd_succ : a ♯ succ b = succ (a ♯ b) := by rw [← nadd_one (a ♯ b), nadd_assoc, nadd_one]

theorem succ_nadd : succ a ♯ b = succ (a ♯ b) := by rw [← one_nadd (a ♯ b), ← nadd_assoc, one_nadd]

@[simp]
theorem nadd_nat (n : ℕ) : a ♯ n = a + n := by
  induction n with
  | zero => simp
  | succ n hn =>
    rw [Nat.cast_succ, ← Order.succ_eq_add_one, nadd_succ, hn, Order.succ_eq_add_one,
      Order.succ_eq_add_one, add_assoc]

@[simp]
theorem nat_nadd (n : ℕ) : ↑n ♯ a = a + n := by rw [nadd_comm, nadd_nat]

theorem le_nadd_self {a b} : a ≤ b ♯ a := by simpa using nadd_le_nadd_right (zero_le (a := b)) a

theorem le_nadd_left {a b c} (h : a ≤ c) : a ≤ b ♯ c :=
  le_nadd_self.trans (nadd_le_nadd_left h b)

theorem le_self_nadd {a b} : a ≤ a ♯ b := by simpa using nadd_le_nadd_left (zero_le (a := b)) a

theorem le_nadd_right {a b c} (h : a ≤ b) : a ≤ b ♯ c :=
  le_self_nadd.trans (nadd_le_nadd_right h c)

end Ordinal
