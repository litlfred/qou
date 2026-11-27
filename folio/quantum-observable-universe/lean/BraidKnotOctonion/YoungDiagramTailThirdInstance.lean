import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.IntervalCases

/-!
# QOU.BraidsAndKnots.YoungDiagramTailThirdInstance — the depth-2 hook covariance: sign of its closed form

`ν_v(n) = Cov_Planch(N_v, ω₃)` is the hook spectrum of the covariance kernel, where `N_v` counts
the cells of hook length `v` and `ω₃ = Σ_□ c² − C(n,2)` (`YoungDiagramKernelPincer.nuV`). The
depth-1 tail `ν_{n−1}(n)` has a proved closed form (`YoungDiagramTailSecondInstance`). This file
treats the next one, the depth-2 tail `ν_{n−2}(n)`.

**The closed form (derived by hand; exact-arithmetic verified, NOT formalized here).** For `n ≥ 4`,

  `ν_{n−2}(n) = (n−2)(n−5)·Q(n)·C(2n−8, n−4) / (6(n−3)·n!)`,
  `Q(n) = n⁶ − 25n⁵ + 235n⁴ − 1067n³ + 2528n² − 3112n + 1680`.

Derivation (audit `docs/audits/2026-11-27-covariance-kernel-depth-two-tail.md`): the carriers of
a hook `n−2` are the shapes `(n−k, 3, 1^{k−3})`, their conjugates, and the boundary shapes
`(n), (n−1,1), (n−2,2)` with conjugates. All of them are the terms `k = 0, …, n` of one sum with

  `f_k = (n−k−2)(k−1)(k−2)·C(n,k) / (2(n−2))`,

because the boundary shapes are exactly the terms `k = 0, n, n−1` (the terms `k = 1, 2, n−2`
vanish). So `ν_{n−2}(n) = (2/n!)·Σ_k f_k²·ω₃(k)`, and Vandermonde in the falling-factorial basis
collapses it. The identity is checked exactly with `Fraction` against the brute-force hook
spectrum for every `n = 4…26`. Formalizing the carrier classification and the collapse, as was done
at depth 1, is open (bean `qou-swk4`).

**What this file proves (sorry-free).** The sign of the closed form: it is positive for every
`n ≥ 10`, and the full sign pattern for `n ≥ 4` is `−, 0, +, −, −, −, +, +, …` (`n = 4, 5, 6, …`).
The key step is that `Q(m + 10)` has only positive coefficients. So the depth-2 tail has sign
onset `n₂ = 10`, against `n₁ = 8` at depth 1.

Base ring: a generic ordered field (§7c), with no `ℝ`.
-/

namespace QOU.BraidsAndKnots.YoungDiagramTailThirdInstance

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The sextic factor `Q` of the depth-2 tail. -/
def depthTwoSexticFactor (x : R) : R :=
  x ^ 6 - 25 * x ^ 5 + 235 * x ^ 4 - 1067 * x ^ 3 + 2528 * x ^ 2 - 3112 * x + 1680

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- `Q(m + 10)` has only positive coefficients. -/
theorem depthTwoSexticFactor_shift (m : R) :
    depthTwoSexticFactor (m + 10) =
      m ^ 6 + 35 * m ^ 5 + 485 * m ^ 4 + 3333 * m ^ 3 + 11518 * m ^ 2 + 17348 * m + 6360 := by
  unfold depthTwoSexticFactor; ring

theorem depthTwoSexticFactor_pos_of_ge_ten {x : R} (hx : 10 ≤ x) :
    0 < depthTwoSexticFactor x := by
  have h := depthTwoSexticFactor_shift (x - 10)
  rw [sub_add_cancel] at h
  rw [h]
  have hm : 0 ≤ x - 10 := by linarith
  positivity

/-- The closed form of the depth-2 tail `ν_{n−2}(n)`, for `n ≥ 4`. -/
def nuDepthTwoClosedForm (n : ℕ) : R :=
  ((n : R) - 2) * ((n : R) - 5) * depthTwoSexticFactor (n : R) * ((2 * n - 8).choose (n - 4) : R)
    / (6 * ((n : R) - 3) * (n.factorial : R))

/-- **Eventual positivity.** The depth-2 tail closed form is positive for every `n ≥ 10`. -/
theorem nuDepthTwo_pos_of_ge_ten (n : ℕ) (hn : 10 ≤ n) :
    0 < (nuDepthTwoClosedForm n : R) := by
  unfold nuDepthTwoClosedForm
  have hnR : (10 : R) ≤ n := by exact_mod_cast hn
  have h1 : (0 : R) < (n : R) - 2 := by linarith
  have h2 : (0 : R) < (n : R) - 5 := by linarith
  have h3 : (0 : R) < (n : R) - 3 := by linarith
  have hQ := depthTwoSexticFactor_pos_of_ge_ten hnR
  have hc : (0 : R) < ((2 * n - 8).choose (n - 4) : R) := by
    exact_mod_cast Nat.choose_pos (by omega)
  have hf : (0 : R) < (n.factorial : R) := by exact_mod_cast Nat.factorial_pos n
  positivity

/-- The values at `n = 4, …, 9`, which agree with the brute-force hook spectrum. -/
theorem nuDepthTwo_small_values :
    (nuDepthTwoClosedForm 4 : R) = -2 / 3 ∧ (nuDepthTwoClosedForm 5 : R) = 0 ∧
    (nuDepthTwoClosedForm 6 : R) = 2 / 3 ∧ (nuDepthTwoClosedForm 7 : R) = -5 / 6 ∧
    (nuDepthTwoClosedForm 8 : R) = -139 / 60 ∧ (nuDepthTwoClosedForm 9 : R) = -343 / 270 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    simp [nuDepthTwoClosedForm, depthTwoSexticFactor, Nat.choose, Nat.factorial] <;> norm_num

/-- **Sign pattern.** For `n ≥ 4` the depth-2 tail is positive iff `n = 6` or `n ≥ 10`. -/
theorem nuDepthTwo_pos_iff (n : ℕ) (hn : 4 ≤ n) :
    0 < (nuDepthTwoClosedForm n : R) ↔ n = 6 ∨ 10 ≤ n := by
  obtain ⟨h4, h5, h6, h7, h8, h9⟩ := (nuDepthTwo_small_values (R := R))
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    obtain ⟨hne, hlt⟩ := hc
    interval_cases n
    · rw [h4] at h; norm_num at h
    · rw [h5] at h; exact lt_irrefl _ h
    · exact hne rfl
    · rw [h7] at h; norm_num at h
    · rw [h8] at h; norm_num at h
    · rw [h9] at h; norm_num at h
  · rintro (rfl | h)
    · rw [h6]; norm_num
    · exact nuDepthTwo_pos_of_ge_ten n h

/-- The depth-2 tail vanishes, for `n ≥ 4`, exactly at `n = 5`. -/
theorem nuDepthTwo_eq_zero_iff (n : ℕ) (hn : 4 ≤ n) :
    (nuDepthTwoClosedForm n : R) = 0 ↔ n = 5 := by
  obtain ⟨h4, h5, h6, h7, h8, h9⟩ := (nuDepthTwo_small_values (R := R))
  constructor
  · intro h
    by_contra hc
    rcases Nat.lt_or_ge n 10 with hlt | hge
    · interval_cases n
      · rw [h4] at h; norm_num at h
      · exact hc rfl
      · rw [h6] at h; norm_num at h
      · rw [h7] at h; norm_num at h
      · rw [h8] at h; norm_num at h
      · rw [h9] at h; norm_num at h
    · exact (nuDepthTwo_pos_of_ge_ten (R := R) n hge).ne' h
  · rintro rfl; exact h5

end QOU.BraidsAndKnots.YoungDiagramTailThirdInstance
