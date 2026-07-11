import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

/-!
# QOU.QBeta.Qsqrt3SaddleArithmetic

**The even-channel resurgence action's arithmetic home is ℚ(√3).**

The 4₁ (figure-eight) Kashaev sum `Σ_k exp(2 Σ_{j≤k} log(2 sin(πj/N)))` localises,
in the `N → ∞` volume-conjecture limit, at the saddle `x* = 5/6` (the maximum of
`G(x) = ∫₀ˣ log(2 sin πs) ds`, where `G'(x*) = log(2 sin(5π/6)) = log 1 = 0`). The
perturbative expansion around that saddle is built from the Taylor derivatives of
`log(2 sin πx)` at `x*`, and **those derivatives are exact elements of
`ℚ(√3)·π^k`** — the arithmetic reflection of the classical fact that the invariant
trace field of 4₁ is `ℚ(√−3)` (`ℚ(√3) = ℚ(√−3)` up to `i`; the Eisenstein /
hexagonal field).

This file certifies that arithmetic, sorry-free:

* `sin_saddle` / `grad_saddle_zero` — `x* = 5/6` is a critical point.
* `cot_saddle` / `hessian_eq` — the Hessian `G''(x*) = π·cot(5π/6) = −√3·π ∈ ℚ(√3)·π`.
* `laplaceB1_at_saddle` — the leading saddle-Laplace coefficient
  `b₁ = g₄/(8 g₂²) + 5 g₃²/(24 |g₂|³)` evaluated at the exact **exponent** Taylor
  data `g_k = 2·G^{(k)}(x*)` (the sum is `exp(2N·G)`, so the Laplace exponent is
  `2G`), i.e. `(g₂, g₃, g₄) = (−2√3π, −8π², −16√3π³)`, equals
  **`√3·π/54 ∈ ℚ(√3)·π`** — an exact arithmetic object, replacing the
  entropy-blocked numerical PSLQ of #3571.

## Honest scope (anti-laundering): arithmetic *home*, NOT a closed action value

`b₁` is the **naive integral-Laplace** coefficient. It does **not** equal the
*observable* action coefficient `c₁ ≈ 0.554` (numerically fitted in #3571):
`b₁ = √3π/54 ≈ 0.101` (`laplaceB1_at_saddle`), a rational multiple of `√3·π`
(`laplaceB1_saddle_mem_qsqrt3`). The observable needs the full state-integral
normalisation (the `N^{3/2}` power, Euler–Maclaurin sum-vs-integral and boundary
terms) absent from this naive saddle — that is the research-grade part, and the
observable's *exact* form is unknown, so no `b₁ = c₁` claim is made. (A numeric
`b₁ < ½ < c₁` inequality would need π-bounds from `…Trigonometric.Bounds`, which
is outside this file's cached dependency surface; the value-gap is recorded here
rather than lemma-ised.) This file proves the `ℚ(√3)` arithmetic home of the even
channel; it launders **no** action value.

Even-channel counterpart of the odd-channel `HopfCubicOddCarrier` (KC20, the
bar-odd carrier over the prime-19 cubic field). Companion audit
`docs/audits/2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md` (#3571).

-- Ref: [manuscript] the 4₁ trace field ℚ(√−3); Kashaev saddle at x*=5/6
-/

namespace QOU.QBeta.Qsqrt3Saddle

open Real

/-- At the saddle `x* = 5/6`, `2·sin(5π/6) = 1` (so `G'(x*) = log 1 = 0`). -/
theorem sin_saddle : 2 * Real.sin (5 * π / 6) = 1 := by
  have h : (5 : ℝ) * π / 6 = π - π / 6 := by ring
  rw [h, Real.sin_pi_sub, Real.sin_pi_div_six]
  norm_num

/-- `sin(5π/6) = 1/2`. -/
theorem sin_saddle' : Real.sin (5 * π / 6) = 1 / 2 := by
  have := sin_saddle; linarith

/-- `cos(5π/6) = −√3/2`. -/
theorem cos_saddle : Real.cos (5 * π / 6) = -(Real.sqrt 3 / 2) := by
  have h : (5 : ℝ) * π / 6 = π - π / 6 := by ring
  rw [h, Real.cos_pi_sub, Real.cos_pi_div_six]

/-- **Critical point:** `G'(x*) = log(2 sin(5π/6)) = 0`. -/
theorem grad_saddle_zero : Real.log (2 * Real.sin (5 * π / 6)) = 0 := by
  rw [sin_saddle, Real.log_one]

/-- `cot(5π/6) = −√3` — the arithmetic that puts the Hessian in `ℚ(√3)`. -/
theorem cot_saddle : Real.cos (5 * π / 6) / Real.sin (5 * π / 6) = -Real.sqrt 3 := by
  rw [cos_saddle, sin_saddle']; ring

/-- **The Hessian `G''(x*) = π·cot(5π/6) = −√3·π ∈ ℚ(√3)·π`.** -/
theorem hessian_eq :
    π * (Real.cos (5 * π / 6) / Real.sin (5 * π / 6)) = -Real.sqrt 3 * π := by
  rw [cot_saddle]; ring

/-- The leading saddle-Laplace `1/N` coefficient as a function of the first three
    saddle Taylor data `(g₂, g₃, g₄)` (with `g₂ < 0`, so `|g₂| = −g₂`):
    `b₁ = g₄/(8 g₂²) + 5 g₃²/(24 (−g₂)³)`. -/
noncomputable def laplaceB1 (g2 g3 g4 : ℝ) : ℝ :=
  g4 / (8 * g2 ^ 2) + 5 * g3 ^ 2 / (24 * (-g2) ^ 3)

/-- **`b₁ = √3·π/54 ∈ ℚ(√3)·π`** at the exact 4₁ exponent (`2G`) saddle data
    `(g₂, g₃, g₄) = (−2√3π, −8π², −16√3π³)`. Exact arithmetic object (the numerical
    PSLQ of #3571 was entropy-blocked; this is the exact value). -/
theorem laplaceB1_at_saddle (hπ : π ≠ 0) :
    laplaceB1 (-2 * Real.sqrt 3 * π) (-8 * π ^ 2) (-16 * Real.sqrt 3 * π ^ 3)
      = Real.sqrt 3 * π / 54 := by
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hr : (0 : ℝ) < Real.sqrt 3 := by positivity
  have hr' : Real.sqrt 3 ≠ 0 := ne_of_gt hr
  have e2 : (-2 * Real.sqrt 3 * π) ^ 2 = 12 * π ^ 2 := by
    linear_combination 4 * π ^ 2 * h3
  have e3 : (-(-2 * Real.sqrt 3 * π)) ^ 3 = 24 * Real.sqrt 3 * π ^ 3 := by
    linear_combination 8 * Real.sqrt 3 * π ^ 3 * h3
  unfold laplaceB1
  rw [e2, e3]
  field_simp
  linear_combination (-552960 : ℝ) * h3

/-- **The naive saddle `b₁` is a rational multiple of `√3·π` — i.e. it lives in
    `ℚ(√3)·π`** (`b₁ = (1/54)·√3π`). This is the exact arithmetic *home* of the
    even channel; it is NOT the observable action coefficient `c₁` (see the module
    docstring's honest-scope note). -/
theorem laplaceB1_saddle_mem_qsqrt3 (hπ : π ≠ 0) :
    ∃ r : ℚ, laplaceB1 (-2 * Real.sqrt 3 * π) (-8 * π ^ 2) (-16 * Real.sqrt 3 * π ^ 3)
      = (r : ℝ) * (Real.sqrt 3 * π) := by
  refine ⟨1 / 54, ?_⟩
  rw [laplaceB1_at_saddle hπ]
  push_cast
  ring

end QOU.QBeta.Qsqrt3Saddle
