import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# QOU.Core.QGaussianMoments — q-Gaussian moments as weighted Dyck paths in ℤ[q]

Bean `qou-e1uf` (item 6 of epic `qou-dk7p`, the q-CLT), strangler step 1.
Owner ruling 2026-11-27: the q-CLT's limit object is stated combinatorially, as
an element of `ℤ[q]` at each finite degree, and no measure, characteristic
function or topology enters the algebraic side.

The `n`-th moment of the q-Gaussian (Bożejko–Speicher; the `t = 1` case of
Blitvić's `(q,t)`-Gaussian) is the sum, over pair partitions of `[n]`, of
`q ^ (crossings)` (Touchard–Riordan). Equivalently, by Flajolet's continued-fraction
correspondence for the `q`-Hermite recurrence `x Hₙ = Hₙ₊₁ + [n]_q Hₙ₋₁`, it is
the weighted count of Dyck paths of length `n` in which a down-step from height
`h` carries weight `[h]_q = 1 + q + ⋯ + q^(h-1)`. This file takes the path form as
the definition: it is a two-line recursion over `ℕ` with values in `ℤ[q]`,
so every statement is a polynomial identity at finite `n`.

* `qGaussMoment n := dyck n 0`.
* Odd moments vanish (`qGaussMoment_odd`).
* `m₂ = 1`, `m₄ = 2 + q`, `m₆ = 5 + 6q + 3q² + q³` (`qGaussMoment_two`, …).
* At `q = 0` (free case) `m₄ = 2`, the Catalan number `C₂`: exactly the
  non-crossing pairings, matching `QOU.MassTheory.FreeCumulants`. At `q = 1`
  (classical case) `m₄ = 3 = 3!!` and `m₆ = 15 = 5!!`: all pairings.

No empirical value and no limit enters this file.
-/

namespace QOU.Core.QGaussianMoments

open Polynomial

/-- The `q`-integer `[n]_q = 1 + q + ⋯ + q^(n-1)` in `ℤ[q]`. -/
noncomputable def qInt : ℕ → ℤ[X]
  | 0 => 0
  | n + 1 => qInt n + X ^ n

/-- Weighted Dyck paths: `dyck n h` is the total weight of paths with `n`
steps left, starting at height `h` and ending at height `0`. An up-step has
weight `1`; a down-step from height `h + 1` has weight `[h + 1]_q`. -/
noncomputable def dyck : ℕ → ℕ → ℤ[X]
  | 0, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, 0 => dyck n 1
  | n + 1, h + 1 => dyck n (h + 2) + qInt (h + 1) * dyck n h

/-- The `n`-th q-Gaussian moment, an element of `ℤ[q]`. -/
noncomputable def qGaussMoment (n : ℕ) : ℤ[X] := dyck n 0

/-- A path whose length and starting height have opposite parity has weight
zero. -/
theorem dyck_parity : ∀ n h : ℕ, (n + h) % 2 = 1 → dyck n h = 0
  | 0, 0, hp => by simp at hp
  | 0, _ + 1, _ => rfl
  | n + 1, 0, hp => by
      simp only [dyck]
      exact dyck_parity n 1 (by omega)
  | n + 1, h + 1, hp => by
      simp only [dyck]
      rw [dyck_parity n (h + 2) (by omega), dyck_parity n h (by omega)]
      ring

/-- **Odd q-Gaussian moments vanish.** -/
theorem qGaussMoment_odd (k : ℕ) : qGaussMoment (2 * k + 1) = 0 :=
  dyck_parity _ _ (by omega)

theorem qInt_one : qInt 1 = 1 := by simp [qInt]
theorem qInt_two : qInt 2 = 1 + X := by simp [qInt]
theorem qInt_three : qInt 3 = 1 + X + X ^ 2 := by simp [qInt]

theorem qGaussMoment_zero : qGaussMoment 0 = 1 := rfl

theorem qGaussMoment_two : qGaussMoment 2 = 1 := by
  simp [qGaussMoment, dyck, qInt]

/-- `m₄ = 2 + q`: two non-crossing pairings and one crossing pairing. -/
theorem qGaussMoment_four : qGaussMoment 4 = 2 + X := by
  simp [qGaussMoment, dyck, qInt]; ring

/-- `m₆ = 5 + 6q + 3q² + q³`: the crossing distribution of the 15 pairings
of six points. -/
theorem qGaussMoment_six : qGaussMoment 6 = 5 + 6 * X + 3 * X ^ 2 + X ^ 3 := by
  simp [qGaussMoment, dyck, qInt]; ring

/-- Free case `q = 0`: `m₄ = 2 = C₂`, the non-crossing pairings only. -/
theorem qGaussMoment_four_eval_zero : (qGaussMoment 4).eval 0 = 2 := by
  rw [qGaussMoment_four]; simp

/-- Free case `q = 0`: `m₆ = 5 = C₃`. -/
theorem qGaussMoment_six_eval_zero : (qGaussMoment 6).eval 0 = 5 := by
  rw [qGaussMoment_six]; simp

/-- Classical case `q = 1`: `m₄ = 3 = 3!!`, all pairings. -/
theorem qGaussMoment_four_eval_one : (qGaussMoment 4).eval 1 = 3 := by
  rw [qGaussMoment_four]; simp

/-- Classical case `q = 1`: `m₆ = 15 = 5!!`. -/
theorem qGaussMoment_six_eval_one : (qGaussMoment 6).eval 1 = 15 := by
  rw [qGaussMoment_six]; simp

end QOU.Core.QGaussianMoments
