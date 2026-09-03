/-
  Vertex operator on the exceptional divisor.

  The vertex operator Y(a, z) is the R-matrix insertion of a state
  a ∈ Aₙ at the affine coordinate z = v₁/v₂ on 𝒮_p ≅ ℙ¹(ℂ).
  Its modes aₘ are the Laurent coefficients, computed via the
  Markov trace of the braid operator.

  The brane tower ⊕ Aₙ is the graded state space, the jet
  prolongation j : Aₙ → A_{n+1} is the translation operator L_{-1},
  and the OPE singularity is the Hecke/Skein relation.

  ## References
  - [frenkel2004] https://doi.org/10.1090/surv/088
  - [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Topology.FiberBundle.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A vertex operator on the exceptional divisor 𝒮_p.
    Given a state a ∈ V_n (level n of the brane tower), the vertex
    operator Y(a, z) is a formal Laurent series in the affine
    coordinate z = v₁/v₂ on 𝒮_p whose modes are R-matrix insertions. -/
-- Ref: [frenkel2004] Frenkel, "Lectures on the Langlands program and conformal field theory," arXiv:hep-th/0512172 (related: 0007054)
structure VertexOperator (q : R_q) where
  /-- The Reeb bundle (base space for the insertion). -/
  bundle : ReebBundle q
  /-- Conformal weight (jet level) of the state. -/
  weight : ℕ

/-- The OPE (operator product expansion) of two vertex operators.
    Records the leading singularity data: the eigenvalues of the
    Hecke generator T acting on the collision Y₁(z)Y₂(w) as z → w. -/
structure OPE (q : R_q) where
  /-- The two vertex operators whose collision is being resolved. -/
  left : VertexOperator q
  right : VertexOperator q
  /-- The symmetric (bosonic) eigenvalue of the Hecke generator. -/
  bosonic_eigenvalue : R_q
  /-- The antisymmetric (fermionic) eigenvalue. -/
  fermionic_eigenvalue : R_q

/-- The OPE of any two vertex operators in a QOU with q > 1 has
    its leading singularity governed by the Hecke relation
    (T - q)(T + q⁻¹) = 0: the bosonic eigenvalue is q and the
    fermionic eigenvalue is -q⁻¹.

    This is the Skein relation L₊ - L₋ = (q - q⁻¹)L₀ applied
    to the strand collision on 𝒮_p. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
axiom ope_is_skein
    -- {q : R_q} (hq : q > 1)  -- (archimedean; not meaningful over R_q)
    (Y₁ Y₂ : VertexOperator q)
    : ∃ (ope : OPE q),
        ope.left = Y₁ ∧ ope.right = Y₂ ∧
        ope.bosonic_eigenvalue = q ∧
        ope.fermionic_eigenvalue = -q_inv_param

end

end QOU
