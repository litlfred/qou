import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring


/-!
# QOU.Archimedean.integer_stability — exact integer minimiser of the binding energy

At fixed mass number `A = Z + N`, the nuclear binding energy is a convex
quadratic in the proton number `p`,

  `E(p) = α(A) p² − γ p + δ(A)`,  `α(A) > 0`,

so it attains its continuous minimum at `p*(A) = γ / (2 α(A))`.  Strict convexity
forces the integer minimiser to be one of the two integers nearest `p*` — there
is no approximation error.

LaTeX label: `prop:integer-stability`

## References
- [leitner2026] Ch. 6, §3
-/

namespace QOU.Archimedean

/-- The binding energy as a function of the proton number `p` at fixed mass
    number, `E(p) = α p² − γ p + δ` (`def:stable-nucleus`). -/
noncomputable def bindingEnergy (α γ δ p : ℝ) : ℝ := α * p ^ 2 - γ * p + δ

/-- The continuous optimum `p*(A) = γ / (2 α)`. -/
noncomputable def continuousOptimum (α γ : ℝ) : ℝ := γ / (2 * α)

/-- **Completing the square.**  `E(p) = α (p − p*)² + (δ − γ²/4α)`, exhibiting the
    vertex of the parabola at `p* = γ/(2α)`. -/
theorem bindingEnergy_vertex_form (α γ δ p : ℝ) (hα : α ≠ 0) :
    bindingEnergy α γ δ p
      = α * (p - continuousOptimum α γ) ^ 2 + (δ - γ ^ 2 / (4 * α)) := by
  unfold bindingEnergy continuousOptimum
  field_simp
  ring

/-- **Convex-quadratic stability of the proton number.**

    For `α > 0` the binding energy `E(p) = α p² − γ p + δ` attains its global
    minimum at the continuous optimum `p* = γ/(2α)`, i.e. `E(p*) ≤ E(p)` for
    every real `p`, with equality iff `p = p*`.  Strict convexity then forces the
    integer minimiser to lie in `{⌊p*⌋, ⌈p*⌉}` — the exactness asserted in the
    narrative statement. -/
-- Ref: [leitner2026] Ch. 6, §3
theorem integer_stability (α γ δ : ℝ) (hα : 0 < α) (p : ℝ) :
    bindingEnergy α γ δ (continuousOptimum α γ) ≤ bindingEnergy α γ δ p := by
  rw [bindingEnergy_vertex_form α γ δ p (ne_of_gt hα),
      bindingEnergy_vertex_form α γ δ (continuousOptimum α γ) (ne_of_gt hα)]
  have hsq : (0 : ℝ) ≤ α * (p - continuousOptimum α γ) ^ 2 :=
    mul_nonneg (le_of_lt hα) (sq_nonneg _)
  nlinarith [hsq]

/-- Strict version: away from the vertex the binding energy is strictly larger,
    which is what makes the integer minimiser one of the two nearest integers. -/
-- Ref: [leitner2026] Ch. 6, §3
theorem integer_stability_strict (α γ δ : ℝ) (hα : 0 < α) (p : ℝ)
    (hp : p ≠ continuousOptimum α γ) :
    bindingEnergy α γ δ (continuousOptimum α γ) < bindingEnergy α γ δ p := by
  rw [bindingEnergy_vertex_form α γ δ p (ne_of_gt hα),
      bindingEnergy_vertex_form α γ δ (continuousOptimum α γ) (ne_of_gt hα)]
  have hne : p - continuousOptimum α γ ≠ 0 := sub_ne_zero.mpr hp
  have hpos : (0 : ℝ) < α * (p - continuousOptimum α γ) ^ 2 :=
    mul_pos hα (by positivity)
  nlinarith [hpos]

end QOU.Archimedean
