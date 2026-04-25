import QOU.SubstrateParameter

/-!
# Uniqueness of the substrate parameter

The substrate parameter `q ∈ End(𝟙)` of a QOU is uniquely
determined by the braiding spectrum and the positivity of the
induced dagger.

LaTeX: `\label{thm:substrate-parameter-unique}`

**Ground ring**: `R_q = ℤ[q, q⁻¹]`. The uniqueness statement is
that any two `SubstrateParameter` records for the same base QOU
agree on their underlying field of $q$-values.
-/

namespace QOU
namespace SubstrateParameter

/-- Uniqueness of the substrate parameter.

Given two substrate parameters for the same base $M$ of a QOU,
their underlying field values coincide pointwise. The proof
follows from:
(1) intrinsic spectral decomposition of the braiding $c_{V,V}$
    (the splitting $V \otimes V = S^2 V \oplus \Lambda^2 V$ is
    canonical, so the eigenvalue pair $\{\lambda_+, \lambda_-\}$
    is intrinsic);
(2) the Hecke relation pinning the unordered pair as
    $\{q, -q^{-1}\}$;
(3) positivity of the induced dagger selecting the positive
    representative.

Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
     §XIV — braid group representations from R-matrices, combined
     with the positivity constraint from the QOU dagger structure.
-/
theorem unique {M : Type*}
    (sp₁ sp₂ : SubstrateParameter M) :
    sp₁.field = sp₂.field := by
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  sorry

end SubstrateParameter
end QOU
