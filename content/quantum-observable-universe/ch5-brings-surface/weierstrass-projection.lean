/-!
# QOU.Descartes.weierstrassProjection — Weierstrass projection ℘_q(z)

The Weierstrass elliptic function associated to the Descartes elliptic
curve E_q, defined via the classical Laurent series on ℂ/Λ_q.

LaTeX label: `def:weierstrass-projection`

## References
- [manuscript] §5/weierstrass-projection
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- **Weierstrass projection** ℘_q : ℂ/Λ_q → ℙ¹.

    The meromorphic function defined by
    ℘_q(z) = 1/z² + Σ_{ω ∈ Λ_q \ {0}} (1/(z-ω)² - 1/ω²)
    which uniformises the Descartes elliptic curve E_q.

    The Weierstrass invariants are g₂(q) = -4p(q), g₃(q) = -4r(q)
    where p, r are the short Weierstrass coefficients of E_q. -/
-- Ref: [manuscript] §5/weierstrass-projection
noncomputable def weierstrassProjection
    (g2 g3 : ℝ) (z : ℂ) : ℂ :=
  -- Ref: [manuscript] §5/weierstrass-projection
  sorry

/-- The Weierstrass function satisfies the differential equation
    ℘'(z)² = 4℘(z)³ - g₂℘(z) - g₃.

    Stated as: for all z not in the lattice Λ_q, the squared
    derivative of ℘_q at z equals the cubic polynomial evaluated
    at ℘_q(z). -/
-- Ref: [manuscript] §5/weierstrass-projection
-- Ref: [manuscript] https://doi.org/10.1007/978-0-387-09494-6
theorem weierstrass_diff_eq (g2 g3 : ℝ) (z : ℂ)
    (hz : z ≠ 0) :
    ∃ (wp_deriv wp_val : ℂ),
      wp_deriv ^ 2 = 4 * wp_val ^ 3 - ↑g2 * wp_val - ↑g3 := by
  -- Ref: [manuscript] https://doi.org/10.1007/978-0-387-09494-6  Theorem VI.3.6
  sorry

end QOU.Descartes
