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
-/

import Mathlib.Topology.FiberBundle.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU

/-- A vertex operator on the exceptional divisor 𝒮_p.
    Given a state a ∈ V_n (level n of the brane tower), the vertex
    operator Y(a, z) is a formal Laurent series in the affine
    coordinate z = v₁/v₂ on 𝒮_p whose modes are R-matrix insertions. -/
-- Ref: [frenkel2004] https://doi.org/10.1090/surv/088
structure VertexOperator (q : ℝ) where
  /-- The Reeb bundle (base space for the insertion). -/
  bundle : ReebBundle q
  /-- Conformal weight (jet level) of the state. -/
  weight : ℕ

/-- The OPE (operator product expansion) of two vertex operators.
    Records the leading singularity data: the eigenvalues of the
    Hecke generator T acting on the collision Y₁(z)Y₂(w) as z → w. -/
structure OPE (q : ℝ) where
  /-- The two vertex operators whose collision is being resolved. -/
  left : VertexOperator q
  right : VertexOperator q
  /-- The symmetric (bosonic) eigenvalue of the Hecke generator. -/
  bosonic_eigenvalue : ℝ
  /-- The antisymmetric (fermionic) eigenvalue. -/
  fermionic_eigenvalue : ℝ

/-- The OPE of any two vertex operators in a QOU with q > 1 has
    its leading singularity governed by the Hecke relation
    (T - q)(T + q⁻¹) = 0: the bosonic eigenvalue is q and the
    fermionic eigenvalue is -q⁻¹.

    This is the Skein relation L₊ - L₋ = (q - q⁻¹)L₀ applied
    to the strand collision on 𝒮_p. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
axiom ope_is_skein
    {q : ℝ} (hq : q > 1)
    (Y₁ Y₂ : VertexOperator q)
    : ∃ (ope : OPE q),
        ope.left = Y₁ ∧ ope.right = Y₂ ∧
        ope.bosonic_eigenvalue = q ∧
        ope.fermionic_eigenvalue = -(q⁻¹)

end QOU
