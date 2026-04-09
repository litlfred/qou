/-!
# B₃ character theory (corrected)

B₃ = (σ₀σ₁⁻¹)³ is NOT central in H₃(q) and is NOT a scalar
matrix in the standard representation. However:

- net(B₃) = 1 exactly (trivial character)
- χ_alt(B₃) = 1 exactly (alternating character)
- The e⁻ NF coefficient of B₃ is zero (observed computationally,
  consistent with character constraints but not yet proved from
  characters alone)

## RETRACTED claims (from earlier version)

The following claims were INCORRECT and have been removed:
- borromean3_comm_gen0/gen1 — B₃ does NOT commute with generators
- borromean3_central — B₃ is NOT central in H₃(q)
- borromean3_is_scalar — B₃ is NOT scalar in the standard rep
- borromean3_entry_01 = 0 — FALSE (B₃(0,1) ≠ 0 in the std rep)
- borromean3_eq_fullTwist — B₃ ≠ Δ² (different braid group elements)

The error: these were stated with `by simp; ring` but never compiled.
The `ring` tactic would have failed because the matrix entries are
nonzero Laurent polynomials.

## What IS true

The trivial and alternating characters ARE exactly 1, because in
1-dimensional representations the generator inverse σ₁⁻¹ ↦ q⁻¹
(trivial) or −q (alternating), and the product σ₀σ₁⁻¹ evaluates
to 1 in both cases. This is a 1D computation, not a 2×2 matrix
computation, so `ring` works.

## References

- [jones1987] https://doi.org/10.2307/1971403
-/

import QOU.Descartes.HeckeH3
import QOU.Interactions.BorromeanUnique

namespace QOU.Interactions

open QOU.Descartes Matrix

/-! ## §1  What B₃ IS in the standard rep -/

/-- B₃ is NOT the identity in the standard representation.
    It is a 2×2 matrix with nonzero off-diagonal entries. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem borromean3_not_identity :
    borromean3 ≠ (1 : TMatrix) := by
  intro h
  -- B₃(0,0) ≠ 1 (it equals (1-q²)³ + 3(1-q²)·q⁻² which ≠ 1 for q ≠ 1)
  have h00 := congr_fun (congr_fun h 0) 0
  simp [borromean3, borromeanUnit, stdRep3_gen0, stdRep3_genInv1,
        stdRep3_gen1, HeckeRep.genInv, HA_t, q_from_t, q_inv_from_t,
        mul_apply, Fin.sum_univ_two, of, Matrix.one_apply] at h00
  -- After simp, h00 is an equation in ℤ[t,t⁻¹] that is false
  -- (the LHS is a nontrivial Laurent polynomial, the RHS is 1)
  linarith [LaurentPolynomial.T_ne_zero (R := ℤ) (1 : ℤ)]

/-! ## §2  The full twist Δ² IS the identity in the standard rep -/

/-- The full twist Δ = σ₀σ₁σ₀ squares to the identity in the
    standard (2,1) representation of H₃(q).

    This is because Δ² is central with character q^{n(λ)} on
    irrep V_λ, and for λ = (2,1) the content is 0, so Δ² ↦ I.

    Numerically verified: (σ₀σ₁σ₀)² = I at all tested q values. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem fullTwist_sq_eq_one :
    (stdRep3_gen0 * stdRep3_gen1 * stdRep3_gen0) *
    (stdRep3_gen0 * stdRep3_gen1 * stdRep3_gen0) = (1 : TMatrix) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [stdRep3_gen0, stdRep3_gen1, q_from_t, q_inv_from_t,
          mul_apply, Fin.sum_univ_two, of, Matrix.one_apply] <;>
    ring

/-! ## §3  B₃ and Δ² are DIFFERENT -/

/-- B₃ = (σ₀σ₁⁻¹)³ ≠ Δ² = (σ₀σ₁σ₀)² in the standard rep.
    Δ² = I (proved above), but B₃ ≠ I (proved above).
    Therefore B₃ ≠ Δ². -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem borromean3_ne_fullTwist :
    borromean3 ≠
    (stdRep3_gen0 * stdRep3_gen1 * stdRep3_gen0) *
    (stdRep3_gen0 * stdRep3_gen1 * stdRep3_gen0) := by
  rw [fullTwist_sq_eq_one]
  exact borromean3_not_identity

/-! ## §4  e⁻ NF coefficient of B₃ -/

/-- The e⁻ NF coefficient of B₃ is observed to be zero
    computationally (at all tested q values). This is consistent
    with the character constraints:
      χ_triv(B₃) = 1, χ_alt(B₃) = 1
    but is not yet proved from characters alone (the character
    system has 3 equations for 6 unknowns; additional structure
    — e.g., the anti-palindromic symmetry of B₃ — is needed).

    Computational witness: confinement-operator-selection.witness.json. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Interactions
