import Mathlib.Algebra.CharZero.Defs
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# QOU.QBeta.PhibSaddleA1Formal — the saddle 2-loop `A₁ = 1/3 + (17s/108)·i`, over any char-0 field

The 2-loop coefficient of a saddle expansion with derivatives `V₂, V₃, V₄` is

    A₁ = V₄/(8·V₂²) − 5·V₃²/(24·V₂³).

For the potential `V(z) = Li₂(z) − Li₂(1/z)` at `z* = e^{iπ/3}` the three derivatives lie in
`ℚ(√3, i)`. This file treats `√3` and `i` as **ring symbols**: `s` and `i` in an arbitrary field of
characteristic zero with `s² = 3` and `i² = −1`. With

    V₂ = 3/2 − (s/2)·i,   V₃ = 2 + 3s·i,   V₄ = −39/2 + (3s/2)·i,

the coefficient is exactly `A₁ = 1/3 + (17s/108)·i`. No ordering, no square root and no complex
numbers are used. `V₃ ≠ 0` follows from `s² = 3`, `i² = −1` and characteristic zero alone, since
`V₃ = 0` would force `9·s²·i² = 4`, that is `−27 = 4`.

The evaluation at `s = √3 ∈ ℝ`, `i = I ∈ ℂ` lives behind the transcendental boundary in
`QOU.Transcendental.Nuclear.PhibSaddleA1Exact`, which keeps the original names.
-/

namespace QOU.QBeta.PhibSaddleA1Formal

variable {K : Type*} [Field K] [CharZero K]

/-- The saddle derivatives as elements of `ℚ(s, i)`. -/
def V2 (s i : K) : K := 3 / 2 - (s / 2) * i
def V3 (s i : K) : K := 2 + (3 * s) * i
def V4 (s i : K) : K := -39 / 2 + (3 * s / 2) * i

/-- The exact 2-loop coefficient. -/
def A1 (s i : K) : K := 1 / 3 + (17 * s / 108) * i

/-- **Division-free core identity:** `3·V₄·V₂ − 5·V₃² = 24·V₂³·A₁`, using only `s² = 3` and
`i² = −1`. -/
theorem a1_core_identity {s i : K} (h : s ^ 2 = 3) (hI : i ^ 2 = -1) :
    3 * V4 s i * V2 s i - 5 * V3 s i ^ 2 = 24 * V2 s i ^ 3 * A1 s i := by
  simp only [V2, V3, V4, A1]
  linear_combination
    (13 * s * i / 4 + 17 * s ^ 2 / 36 + 539 / 12) * h
    + (17 * i ^ 2 * s ^ 4 / 36 - 13 * i * s ^ 3 / 4
        - 17 * s ^ 4 / 36 - 87 * s ^ 2 / 2) * hI

/-- `V₃ ≠ 0`: otherwise `3s·i = −2`, so `9·s²·i² = 4`, i.e. `−27 = 4`. -/
theorem V3_ne_zero {s i : K} (h : s ^ 2 = 3) (hI : i ^ 2 = -1) : V3 s i ≠ 0 := by
  intro h0
  have e : 3 * s * i = -2 := by simp only [V3] at h0; linear_combination h0
  have e2 : (3 * s * i) ^ 2 = 4 := by rw [e]; norm_num
  have : (31 : K) = 0 := by
    have : (3 * s * i) ^ 2 = 9 * s ^ 2 * i ^ 2 := by ring
    rw [this, h, hI] at e2
    linear_combination -e2
  exact (by norm_num : (31 : K) ≠ 0) this

/-- `V₂ ≠ 0`: if `V₂ = 0` the core identity forces `V₃² = 0`. -/
theorem V2_ne_zero {s i : K} (h : s ^ 2 = 3) (hI : i ^ 2 = -1) : V2 s i ≠ 0 := by
  intro h0
  have core := a1_core_identity h hI
  rw [h0] at core
  have hV3sq : V3 s i ^ 2 = 0 := by linear_combination (-(1 : K) / 5) * core
  exact V3_ne_zero h hI (pow_eq_zero_iff (by norm_num) |>.mp hV3sq)

/-- **The 2-loop coefficient is exactly `1/3 + (17s/108)·i`.** -/
theorem A1_eq {s i : K} (h : s ^ 2 = 3) (hI : i ^ 2 = -1) :
    V4 s i / (8 * V2 s i ^ 2) - 5 * V3 s i ^ 2 / (24 * V2 s i ^ 3) = A1 s i := by
  have hV2 : V2 s i ≠ 0 := V2_ne_zero h hI
  have core := a1_core_identity h hI
  field_simp
  linear_combination (8 : K) * core

end QOU.QBeta.PhibSaddleA1Formal
