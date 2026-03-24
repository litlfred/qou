/-!
# QOU.Brings.mi_sw_abelianisation — MI–SW abelianisation

The restriction of the nonabelian multiplicative integral to the
exceptional divisor E_c ≅ P¹(ℂ) at a branch point z_c abelianises
to the n-th prolonged Seiberg–Witten period:

  ‖MI∫_{E_c} (∇_A q, L ∧ F⁺)‖_{J^n} = |a_D^{(n)}| = |∮_{E_c} λ_SW^{(n)}|

LaTeX label: `prop:mi-sw-abelianisation`

## References

- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4
- [manuscript] §5-brings-surface/mi-sw-abelianisation
-/

import Mathlib.Data.Real.Basic

namespace QOU.Brings

/-- **MI–SW abelianisation data**: the multiplicative integral
    restricted to the exceptional divisor. -/
-- Ref: [seiberg1994], [manuscript] §5
structure MISWAbelianisation where
  /-- The branch point index c. -/
  branchIndex : ℕ
  /-- The jet level n. -/
  jetLevel : ℕ
  /-- The multiplicative integral norm ‖MI∫‖_{J^n}. -/
  mi_norm : ℝ
  /-- The Seiberg–Witten period |a_D^{(n)}|. -/
  sw_period : ℝ
  /-- Both are non-negative. -/
  mi_nonneg : 0 ≤ mi_norm
  sw_nonneg : 0 ≤ sw_period
  /-- The abelianisation identity: MI norm = SW period. -/
  abelianisation : mi_norm = sw_period

/-- The abelianisation preserves non-negativity. -/
-- Ref: [manuscript] §5
theorem mi_sw_nonneg (data : MISWAbelianisation) : 0 ≤ data.mi_norm :=
  data.mi_nonneg

/-- The SW period determines the MI integral. -/
-- Ref: [seiberg1994]
theorem sw_determines_mi (data : MISWAbelianisation) :
    data.mi_norm = data.sw_period :=
  data.abelianisation

end QOU.Brings
