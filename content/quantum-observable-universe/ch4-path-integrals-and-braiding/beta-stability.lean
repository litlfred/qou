/-!
# QOU.Braiding.beta_stability — Beta-stability line from ∂L_bind/∂p = 0

LaTeX label: `prop:beta-stability`

## References
- [manuscript] §4/beta-stability
-/

import Mathlib.Data.Real.Basic

namespace QOU.Braiding

/-- Beta-stability line: p*(A) = A / (2 + a_C·A^{2/3}/(2·a_A)). -/
-- Ref: [manuscript] §4/beta-stability
noncomputable def beta_stability_line (A : ℝ) (a_C a_A : ℝ) : ℝ :=
  A / (2 + a_C * A^(2/3 : ℝ) / (2 * a_A))

/-- At q = 1, a_C = 0 and all nuclei are symmetric (p = A/2). -/
-- Ref: [manuscript] §4/beta-stability
theorem beta_stability_classical (A : ℝ) (a_A : ℝ) (hA : A ≠ 0) :
    beta_stability_line A 0 a_A = A / 2 := by
  simp [beta_stability_line]
  ring

end QOU.Braiding
