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

/-- Witness that two `SubstrateParameter` instances arise from the
    same underlying QOU. Opaque placeholder until the full
    `QuantumObservableUniverse` structure is axiomatized in Lean
    (currently a paper-side claim per Ch 2). The witness packages:
    a shared braiding $c_{V,V}$, a shared Hecke relation, and a
    shared positive-definite dagger structure — i.e. the data that,
    in the narrative, pins the substrate parameter uniquely. -/
opaque SameQouOrigin {M : Type*} (sp₁ sp₂ : SubstrateParameter M) : Prop

/-- Uniqueness of the substrate parameter (conditional on shared QOU
    origin).

Given two substrate parameters for the same base $M$ that arise from
the same underlying QOU (encoded by `SameQouOrigin`), their
underlying field values coincide pointwise. The proof follows from:
(1) intrinsic spectral decomposition of the braiding $c_{V,V}$
    (the splitting $V \otimes V = S^2 V \oplus \Lambda^2 V$ is
    canonical, so the eigenvalue pair $\{\lambda_+, \lambda_-\}$
    is intrinsic);
(2) the Hecke relation pinning the unordered pair as
    $\{q, -q^{-1}\}$;
(3) positivity of the induced dagger selecting the positive
    representative.

The `SameQouOrigin` hypothesis stands in for the as-yet-unformalized
QOU structure: once Ch 2's axioms are in scope as a Lean type, the
hypothesis becomes derivable from any pair of QOU instances on $M$
and the theorem upgrades to unconditional uniqueness.

Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
     §XIV — braid group representations from R-matrices, combined
     with the positivity constraint from the QOU dagger structure.
-/
theorem unique {M : Type*}
    (sp₁ sp₂ : SubstrateParameter M)
    (h_same_qou : SameQouOrigin sp₁ sp₂) :
    sp₁.field = sp₂.field := by
  sorry -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2

end SubstrateParameter
end QOU
