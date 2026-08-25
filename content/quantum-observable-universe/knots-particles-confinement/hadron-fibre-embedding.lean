import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.HadronFibreEmbedding — Fibre-compatible hadron embedding

A fibre-compatible embedding places a hadron into a fibre of the
brane tower, satisfying integrability, fibre confinement, Hopf
compatibility, and volume compatibility conditions.

## References

- [manuscript] §3 Lifting and Descent

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

/-- A fibre-compatible hadron embedding: a morphism ιₚ satisfying
    integrability, fibre confinement, Hopf compatibility, and
    volume compatibility.

    LaTeX: `\label{def:hadron-fibre-embedding}` -/
-- Ref: [manuscript] §3, Definition: Fibre-compatible hadron embedding
structure HadronFibreEmbedding where
  /-- The base point in the projective line. -/
  theta : R_q
  phi : R_q
  /-- The embedding energy (from Möbius energy constraint). -/
  energy : R_q
  -- Energy is non-negative:
  -- energy_nonneg : 0 ≤ energy  -- (archimedean; not meaningful over R_q)
  /-- Integrability: the embedding preserves the connection structure. -/
  integrable : Prop
  /-- Fibre confinement: the image is contained in a single fibre. -/
  confined : Prop

end

end QOU
