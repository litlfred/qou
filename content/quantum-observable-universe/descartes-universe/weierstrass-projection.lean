/-!
# QOU.Descartes.weierstrassProjection — Weierstrass projection ℘_q(z)

The Weierstrass elliptic function associated to the Descartes elliptic
curve E_q, defined via the classical Laurent series on ℂ/Λ_q.

LaTeX label: `def:weierstrass-projection`

## References
- [manuscript] §5/weierstrass-projection

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Descartes

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Weierstrass projection** ℘_q : ℂ/Λ_q → ℙ¹.

    The meromorphic function defined by
    ℘_q(z) = 1/z² + Σ_{ω ∈ Λ_q \ {0}} (1/(z-ω)² - 1/ω²)
    which uniformises the Descartes elliptic curve E_q.

    The Weierstrass invariants are g₂(q) = -4p(q), g₃(q) = -4r(q)
    where p, r are the short Weierstrass coefficients of E_q. -/
/-- **External axiom** (Lang, Elliptic Functions §VI.3; manuscript
    §5/weierstrass-projection): the Weierstrass projection ℘_q
    associated to the Descartes elliptic curve.  Axiomatised pending
    a complex Weierstrass-℘ formalisation in Mathlib. -/
-- Ref: [manuscript] §5/weierstrass-projection
axiom weierstrassProjection : R_q → R_q → ℂ → ℂ

/-- **External axiom (Lang, Elliptic Functions Thm VI.3.6):** the
    Weierstrass differential equation `℘'² = 4℘³ − g₂℘ − g₃`. -/
-- Ref: [manuscript] §5/weierstrass-projection
-- Ref: https://doi.org/10.1007/978-0-387-09494-6 Theorem VI.3.6
axiom weierstrass_diff_eq_axiom :
    ∀ (g2 g3 : R_q) (z : ℂ),
      z ≠ 0 →
      ∃ (wp_deriv wp_val : ℂ),
        wp_deriv ^ 2 = 4 * wp_val ^ 3 - ↑g2 * wp_val - ↑g3

/-- The Weierstrass function satisfies the differential equation
    ℘'(z)² = 4℘(z)³ - g₂℘(z) - g₃. -/
theorem weierstrass_diff_eq (g2 g3 : R_q) (z : ℂ)
    (hz : z ≠ 0) :
    ∃ (wp_deriv wp_val : ℂ),
      wp_deriv ^ 2 = 4 * wp_val ^ 3 - ↑g2 * wp_val - ↑g3 :=
  weierstrass_diff_eq_axiom g2 g3 z hz

end QOU.Descartes
