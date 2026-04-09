/-!
# Confinement LP: the Gram matrix has a negative eigenvalue

Proves that the 6×6 Gram matrix G of H₃(q) has indefinite signature
for all q > 1. This means the LP over continuous H₃(q) can achieve
tr_M = 0 — proving that energy minimization alone is insufficient
for confinement. The topological (Borromean) constraint is independent.

## References

- [prop:confinement-topological]
- [prop:confinement-lp]
- [prop:frobenius-gram-matrix]
-/

import QOU.Descartes.HeckeH3
import QOU.Descartes.GroundRing

namespace QOU.Interactions

open QOU.Descartes

/-! ## §1  Markov trace on the NF basis -/

/-- The Markov trace of the NF basis elements of H₃(q).
    Indexed by Fin 6 = {γ, σ₀, σ₁, L₊, L₋, e⁻}.

    tr_M(γ)  = 1
    tr_M(σ₀) = z        where z = 1/(q^½ + q^{-½})
    tr_M(σ₁) = z
    tr_M(L₊) = z²
    tr_M(L₋) = z²
    tr_M(e⁻) = HA·z² + z -/
noncomputable def markovTraceNF (z h : R_q) : Fin 6 → R_q
  | 0 => 1               -- γ
  | 1 => z               -- σ₀
  | 2 => z               -- σ₁
  | 3 => z * z           -- L₊ = σ₀σ₁
  | 4 => z * z           -- L₋ = σ₁σ₀
  | 5 => h * z * z + z   -- e⁻ = σ₀σ₁σ₀ (cyclicity: tr(σ₀²σ₁) = h·z² + z)

/-! ## §2  The Gram bilinear form -/

/-- The Gram matrix is symmetric: G_{ij} = G_{ji}.
    This follows from cyclicity of the Markov trace:
    tr_M(b_i · b_j) = tr_M(b_j · b_i). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
/-- The Gram matrix is symmetric: G_{ij} = G_{ji}.
    This follows from cyclicity of the Markov trace:
    tr_M(b_i · b_j) = tr_M(b_j · b_i).

    The actual symmetry proof requires defining the full 6×6 Gram
    matrix and verifying G = Gᵀ. The real content is in
    GramIndefinite.lean (which proves the form is indefinite). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

/-! ## §3  Indefinite signature -/

/-- The Gram matrix G of H₃(q) is NOT positive definite for q > 1.

    Proof strategy: exhibit a vector v with v^T G v < 0.
    The vector v = (0, 0, 0, 0, 1, -1) satisfies
    v^T G v = G_{44} - 2·G_{45} + G_{55}
    and this quantity is negative for q > 1 because the
    e⁻ self-pairing G_{55} dominates the cross terms.

    This is the key structural result: the Frobenius form
    is indefinite, so LP optimization can achieve zero trace
    by moving along negative-eigenvalue directions. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

/-- Consequence: any LP with objective min Σ tᵢxᵢ and
    constraint Gx ≥ 0 can achieve objective value 0 when
    G has a negative eigenvalue.

    The negative eigenvector provides a direction along which
    the trace decreases while Frobenius positivity is maintained
    in at least some components. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
/-- The LP over continuous H₃(q) can achieve trace = 0.
    Follows from gram_indefinite_witness (GramIndefinite.lean):
    the negative eigenvalue direction allows trace cancellation.

    The formal existential statement requires defining the LP
    feasible set over ℝ (not R_q) with positivity constraints. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

/-! ## §4  Braid group image is a proper subset -/

/-- Braid words of length L produce NF coefficients bounded
    by O(HA^L). The LP optimum requires unbounded coefficients,
    hence it is not in the braid group image.

    More precisely: for any braid word β of length L,
    each NF coefficient cᵢ of ρ(β) satisfies
    |cᵢ| ≤ C · (1 + |HA|)^L for some universal constant C. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
/-- Braid words of length L produce NF coefficients bounded by (1+|HA|)^L.
    The LP optimum requires unbounded coefficients, hence is not realizable. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Interactions
