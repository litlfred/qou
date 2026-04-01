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
    ℘'(z)² = 4℘(z)³ - g₂℘(z) - g₃. -/
-- Ref: [manuscript] §5/weierstrass-projection
theorem weierstrass_diff_eq (g2 g3 : ℝ) (z : ℂ) :
    True := by  -- placeholder for the differential equation statement
  -- Ref: [manuscript] §5/weierstrass-projection
  sorry

end QOU.Descartes
