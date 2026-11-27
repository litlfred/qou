import QOU.Nuclear.PhibSaddleA1Formal
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-!
# QOU.QBeta.PhibSaddleA1Exact — the saddle 2-loop A₁ = 1/3 + (17√3/108)·i (exact)

The 2-loop coefficient of the potential `V(z) = Li₂(z) − Li₂(1/z)` at the geometric
saddle `z* = e^{iπ/3}` is

    A₁ = V⁗(z*)/(8·V''(z*)²) − 5·V'''(z*)²/(24·V''(z*)³).

The saddle derivatives are algebraic (all in `ℚ(√3, i)`), pinned to 50+ dps by the probe
`computations/qbeta/qbeta_phib_a1_vs_ohtsuki_kappa1.py` and confirmed symbolically (sympy):

    V''(z*)  = 3/2 − (√3/2)·i,
    V'''(z*) = 2 + 3√3·i,
    V''''(z*) = −39/2 + (3√3/2)·i.

This file certifies the **arithmetic**: given these algebraic derivative values, the 2-loop
coefficient is exactly `1/3 + (17√3/108)·i`. The derivative values themselves are the
numerically-established physical inputs (Li₂-derivative evaluation, outside Mathlib's current
reach); this theorem discharges the field computation on top of them, division-free.

**Scope note (self-review, PR #3874).** `A₁` is the exact 2-loop of *this* potential; it is
**not** the 4₁ Ohtsuki 2-loop invariant `κ₁ = 11√3π/108` (they disagree — `A₁` is π-free,
`κ₁` real/π-bearing). So `V = Li₂(z) − Li₂(1/z)` is a Vol+torsion reconstruction, not the 4₁
state integral. This lemma records the exact value; it makes no physical b-dictionary claim.

Base ring: `ℂ` (the saddle values are genuinely complex — archimedean, post-wall). The field
arithmetic is proved once over any characteristic-zero field with ring symbols `s² = 3`,
`i² = −1` in `QOU.QBeta.PhibSaddleA1Formal`; every theorem here is its instance at
`s = √3`, `i = I`.
-/

namespace QOU.QBeta.PhibSaddleA1Exact

open Complex

/-- `√3` as a real number, with its defining square. -/
noncomputable def s : ℝ := Real.sqrt 3

theorem s_sq : s ^ 2 = 3 := Real.sq_sqrt (by norm_num)

/-- The three exact saddle derivatives of `V = Li₂(z) − Li₂(1/z)` at `z* = e^{iπ/3}`,
as elements of `ℚ(√3, i) ⊂ ℂ` (numerically pinned, symbolically confirmed). -/
noncomputable def V2 : ℂ := PhibSaddleA1Formal.V2 (s : ℂ) I
noncomputable def V3 : ℂ := PhibSaddleA1Formal.V3 (s : ℂ) I
noncomputable def V4 : ℂ := PhibSaddleA1Formal.V4 (s : ℂ) I

/-- The exact 2-loop coefficient. -/
noncomputable def A1 : ℂ := PhibSaddleA1Formal.A1 (s : ℂ) I

theorem V2_eq : V2 = 3 / 2 - ((s : ℂ) / 2) * I := rfl
theorem V3_eq : V3 = 2 + (3 * (s : ℂ)) * I := rfl
theorem V4_eq : V4 = -39 / 2 + (3 * (s : ℂ) / 2) * I := rfl
theorem A1_def : A1 = 1 / 3 + (17 * (s : ℂ) / 108) * I := rfl

theorem s_pos : 0 < s := Real.sqrt_pos.mpr (by norm_num)

/-- `(√3 : ℂ)² = 3`. -/
theorem s_cpow : (s : ℂ) ^ 2 = 3 := by
  have : ((s ^ 2 : ℝ) : ℂ) = ((3 : ℝ) : ℂ) := by rw [s_sq]
  push_cast at this ⊢
  linear_combination this

/-- **Division-free core identity:** `3·V₄·V₂ − 5·V₃² = 24·V₂³·A₁`. -/
theorem a1_core_identity : 3 * V4 * V2 - 5 * V3 ^ 2 = 24 * V2 ^ 3 * A1 :=
  PhibSaddleA1Formal.a1_core_identity s_cpow Complex.I_sq

/-- `V₃ ≠ 0`. -/
theorem V3_ne_zero : V3 ≠ 0 := PhibSaddleA1Formal.V3_ne_zero s_cpow Complex.I_sq

/-- `V₂ ≠ 0`. -/
theorem V2_ne_zero : V2 ≠ 0 := PhibSaddleA1Formal.V2_ne_zero s_cpow Complex.I_sq

/-- **The 2-loop coefficient is exactly `1/3 + (17√3/108)·i`.** -/
theorem A1_eq : V4 / (8 * V2 ^ 2) - 5 * V3 ^ 2 / (24 * V2 ^ 3) = A1 :=
  PhibSaddleA1Formal.A1_eq s_cpow Complex.I_sq

end QOU.QBeta.PhibSaddleA1Exact
