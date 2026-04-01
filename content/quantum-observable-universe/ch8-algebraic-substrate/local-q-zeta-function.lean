/-!
# QOU.AlgebraicSubstrate.LocalQZetaFunction

The local q-zeta function of Bring's curve, encoding point counts
over finite extensions via the characteristic polynomial of Frobenius.

LaTeX label: `def:local-q-zeta-function`
-/

set_option autoImplicit false

import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic

open Polynomial Complex

namespace QOU.AlgebraicSubstrate

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
  q : ℝ
  /-- Positivity of q. -/
  q_pos : q > 0
  /-- The 8 fundamental Frobenius eigenvalues α₁, …, α₈. -/
  eigenvalues : Fin 8 → ℂ
  /-- The characteristic polynomial P(t) = ∏ᵢ (1 - αᵢ t). -/
  charPoly : ℂ[X]
  /-- P has degree 2g = 8. -/
  charPoly_degree : charPoly.natDegree = 2 * bringsGenus
  /-- P factors as ∏ᵢ (1 - αᵢ t). -/
  -- Ref: [manuscript] Chapter 8, Section 4
  charPoly_roots :
    charPoly = ∏ i : Fin 8, (X - C (eigenvalues i))

end QOU.AlgebraicSubstrate
