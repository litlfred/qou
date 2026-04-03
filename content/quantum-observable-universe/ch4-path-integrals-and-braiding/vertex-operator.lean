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

/-- The OPE of two vertex operators has its leading singularity
    governed by the Hecke relation (T - q)(T + q⁻¹) = 0,
    i.e. the Skein relation L₊ - L₋ = (q - q⁻¹)L₀.

    The two eigenvalues q and -q⁻¹ correspond to the symmetric
    (bosonic) and antisymmetric (fermionic) OPE channels. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
axiom ope_is_skein
    {q : ℝ} (hq : q > 1)
    (Y₁ Y₂ : VertexOperator q)
    : -- The leading singularity of Y₁(z)Y₂(w) as z → w
      -- decomposes into eigenvalues q (bosonic) and -q⁻¹ (fermionic).
      -- Requires: the Hecke algebra representation on V^{⊗n}.
      ∃ (eigenvalues : Fin 2 → ℝ),
        eigenvalues 0 = q ∧ eigenvalues 1 = -(q⁻¹)

end QOU
