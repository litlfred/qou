import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.YekutieliTriple — Yekutieli triple mapping

The Yekutieli triple at level n consists of objects (local
trivialisations), 1-morphisms (transition automorphisms), and
2-morphisms (deformation parameters in the band).

Note: The structure `YekutielijTriple` is already defined in
cosimplicial-crossed-groupoid.lean. This file provides the mapping
version used in the definition block.

## References

- [yekutieli2010] Central Extensions of Gerbes, §3
- [leitner2026] §3

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The Yekutieli triple mapping: assigns a triple (x, g, a) to each
    level n and intersection Uᵢ ∩ Uⱼ of the brane tower.

    LaTeX: `\label{def:yekutieli-triple}` -/
-- Ref: [yekutieli2010] §3, [leitner2026] §3
structure YekutieliTripleMapping (M : Type*) where
  /-- Level in the brane tower. -/
  level : ℕ
  /-- Objects: local trivialisations. -/
  objects : M → M
  /-- 1-morphisms: transition automorphisms gᵢⱼ. -/
  transitions : M → R_q
  /-- 2-morphisms: deformation parameters aᵢⱼ in the band. -/
  deformations : M → R_q
  /-- The 2-morphisms are invertible (in 𝒪_M×). -/
  deformations_ne_zero : ∀ p : M, deformations p ≠ 0

end

end QOU
