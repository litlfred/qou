import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic

/-!
# QOU.AlgebraicSubstrate.LocalQZetaFunction

The local q-zeta function of Bring's curve, encoding point counts
over finite extensions via the characteristic polynomial of Frobenius.

LaTeX label: `def:local-q-zeta-function`

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

set_option autoImplicit false


open Polynomial Complex

namespace QOU.AlgebraicSubstrate

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The genus of Bring's curve. -/
def bringsGenus : ℕ := 4

/-- **Local q-zeta function** of Bring's curve.

    Encodes the generating function for point counts over finite
    extensions of F_q.  The characteristic polynomial P(t) has degree
    2g = 8, with roots α₁, …, α₈ — the fundamental Frobenius
    eigenvalues.

    LaTeX: `\label{def:local-q-zeta-function}`
    Ref: [manuscript] Chapter 8, Section 4 -/
structure LocalQZetaFunction where
  /-- The substrate parameter q. -/
  q : R_q
  /-- Positivity of q. -/
  -- q_pos : q > 0  -- (archimedean; not meaningful over R_q)
  /-- The 8 fundamental Frobenius eigenvalues α₁, …, α₈. -/
  eigenvalues : Fin 8 → ℂ
  /-- The *reversed* characteristic polynomial P̃(X) = ∏ᵢ (X - αᵢ).
      Related to the standard form P(t) = ∏ᵢ (1 - αᵢ t) by
      P(t) = t^{2g} · P̃(1/t), so the roots of P̃ are the eigenvalues
      αᵢ themselves (not their reciprocals). We use this convention
      to match Lean's polynomial root factorization. -/
  charPoly : ℂ[X]
  /-- P̃ has degree 2g = 8. -/
  charPoly_degree : charPoly.natDegree = 2 * bringsGenus
  /-- P̃ factors as ∏ᵢ (X - αᵢ). -/
  charPoly_roots :
    charPoly = ∏ i : Fin 8, (X - C (eigenvalues i))

end QOU.AlgebraicSubstrate
