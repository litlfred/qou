/-
Copyright (c) 2026. All rights reserved.
-/
import QOU.Core.TarskiSign
import Mathlib.Algebra.Order.Archimedean.Basic

/-!
# The integer phase of the Gonshor walk: every `α` gets both bounds

`gonshorCut_located` (in `QOU.Core.TarskiSign`) needs a stage where the
Gonshor window of `α` has both bounds. Here that hypothesis is discharged.

Before the window has an upper bound, every sign has been `+`, so the value
after `n` signs is `n` and `α > n − 1`. Before it has a lower bound, every
sign has been `-`, so the value is `−n` and `α ≤ −(n − 1)`. In an
Archimedean ordered field neither can go on forever, and both flags, once
set, stay set. So some window has both bounds, and the Gonshor cut of every
`α` is located with no hypothesis and no axiom (`gonshorCut_located'`).

This is the integer phase of the sign expansion: the run of equal signs that
fixes the integer part of `α` before the dyadic halving starts.
-/

namespace QOU.Core.TarskiSign

open QOU.AppendixSurreals

/-- Once a lower bound is set, every later step keeps it. -/
theorem step_hasLo (st : GonshorState) (s : Sign) (h : st.hasLo = true) :
    (st.step s).hasLo = true := by
  cases s <;> unfold GonshorState.step <;> split_ifs <;> simp_all

/-- Once an upper bound is set, every later step keeps it. -/
theorem step_hasHi (st : GonshorState) (s : Sign) (h : st.hasHi = true) :
    (st.step s).hasHi = true := by
  cases s <;> unfold GonshorState.step <;> split_ifs <;> simp_all

section Phase

variable {K : Type*} [Field K] [LinearOrder K]

theorem follow_hasLo_mono (α : K) {n m : ℕ} (hnm : n ≤ m)
    (h : (follow α n).hasLo = true) : (follow α m).hasLo = true := by
  induction hnm with
  | refl => exact h
  | step _ ih => exact step_hasLo _ _ ih

theorem follow_hasHi_mono (α : K) {n m : ℕ} (hnm : n ≤ m)
    (h : (follow α n).hasHi = true) : (follow α m).hasHi = true := by
  induction hnm with
  | refl => exact h
  | step _ ih => exact step_hasHi _ _ ih

/-- With no upper bound yet, `n` signs have all been `+`: the value is `n`. -/
theorem value_of_not_hasHi (α : K) (n : ℕ) (h : (follow α n).hasHi = false) :
    (follow α n).value = n := by
  induction n with
  | zero => simp [follow, GonshorState.init]
  | succ n ih =>
    have hn : (follow α n).hasHi = false := by
      cases hH : (follow α n).hasHi
      · rfl
      · have := step_hasHi (follow α n) (signAt α (follow α n)) hH
        simp only [follow] at h; rw [h] at this; exact absurd this (by simp)
    have hv := ih hn
    simp only [follow, signAt] at h ⊢
    split_ifs at h ⊢ with hlt
    · simp [GonshorState.step, hn, hv]
    · exfalso; unfold GonshorState.step at h; split_ifs at h

/-- With no upper bound after `n + 1` signs, `α > n`. -/
theorem lt_of_not_hasHi (α : K) (n : ℕ) (h : (follow α (n + 1)).hasHi = false) :
    ((n : ℚ) : K) < α := by
  have hn : (follow α n).hasHi = false := by
    cases hH : (follow α n).hasHi
    · rfl
    · have := follow_hasHi_mono α (Nat.le_succ n) hH
      rw [h] at this; exact absurd this (by simp)
  have hv := value_of_not_hasHi α n hn
  simp only [follow, signAt] at h
  split_ifs at h with hlt
  · rwa [hv] at hlt
  · exfalso; unfold GonshorState.step at h; split_ifs at h

/-- With no lower bound yet, `n` signs have all been `-`: the value is `−n`. -/
theorem value_of_not_hasLo (α : K) (n : ℕ) (h : (follow α n).hasLo = false) :
    (follow α n).value = -n := by
  induction n with
  | zero => simp [follow, GonshorState.init]
  | succ n ih =>
    have hn : (follow α n).hasLo = false := by
      cases hL : (follow α n).hasLo
      · rfl
      · have := step_hasLo (follow α n) (signAt α (follow α n)) hL
        simp only [follow] at h; rw [h] at this; exact absurd this (by simp)
    have hv := ih hn
    simp only [follow, signAt] at h ⊢
    split_ifs at h ⊢ with hlt
    · exfalso; unfold GonshorState.step at h; split_ifs at h
    · simp [GonshorState.step, hn, hv]; ring

/-- With no lower bound after `n + 1` signs, `α ≤ −n`. -/
theorem le_of_not_hasLo (α : K) (n : ℕ) (h : (follow α (n + 1)).hasLo = false) :
    α ≤ ((-(n : ℚ) : ℚ) : K) := by
  have hn : (follow α n).hasLo = false := by
    cases hL : (follow α n).hasLo
    · rfl
    · have := follow_hasLo_mono α (Nat.le_succ n) hL
      rw [h] at this; exact absurd this (by simp)
  have hv := value_of_not_hasLo α n hn
  simp only [follow, signAt] at h
  split_ifs at h with hlt
  · exfalso; unfold GonshorState.step at h; split_ifs at h
  · rw [hv] at hlt; exact not_lt.mp hlt

end Phase

section Located

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [Archimedean K]

/-- **Integer phase.** In an Archimedean ordered field, some Gonshor window of
every `α` has both bounds. -/
theorem exists_follow_bounded (α : K) :
    ∃ n, (follow α n).hasLo = true ∧ (follow α n).hasHi = true := by
  obtain ⟨a, ha⟩ := exists_nat_ge α
  obtain ⟨b, hb⟩ := exists_nat_gt (-α)
  refine ⟨max a b + 1, ?_, ?_⟩
  · cases hL : (follow α (b + 1)).hasLo
    · have := le_of_not_hasLo α b hL
      push_cast at this; linarith
    · exact follow_hasLo_mono α (by omega) hL
  · cases hH : (follow α (a + 1)).hasHi
    · have := lt_of_not_hasHi α a hH
      push_cast at this; linarith
    · exact follow_hasHi_mono α (by omega) hH

open QOU.Core.LawvereCut in
/-- **Located, unconditionally.** In an Archimedean ordered field the Gonshor
cut of every `α` is located. No bounds hypothesis, no `[Coev E]`, no axiom. -/
theorem gonshorCut_located' (α : K) : (gonshorCut α).Located := by
  obtain ⟨n, hL, hH⟩ := exists_follow_bounded α
  exact gonshorCut_located α hL hH

end Located

end QOU.Core.TarskiSign
