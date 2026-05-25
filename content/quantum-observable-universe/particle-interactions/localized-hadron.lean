/-!
# QOU.LocalizedHadron — Hadron placed at a categorical point

A localized hadron is a hadron placed at a categorical point p of the
projective line ℙ(V), via a morphism 𝟙 → Sym^n(𝒦_p) ⊗ ℒ_p^bind.

## References

- [manuscript] §3 Lifting and Descent

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import QOU.KnotTheory

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A localized hadron: a hadron placed at a specific categorical point.

    LaTeX: `\label{def:localized-hadron}` -/
-- Ref: [manuscript] §3, Definition: Localized hadron
structure LocalizedHadron extends Hadron where
  /-- The categorical point (base point in the projective line). -/
  point_theta : R_q
  point_phi : R_q
  /-- Binding link data. -/
  binding : HadronBinding

end QOU
