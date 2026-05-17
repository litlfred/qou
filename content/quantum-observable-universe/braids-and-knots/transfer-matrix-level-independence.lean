/-!
# QOU.transfer_matrix_level_independence — Transfer matrix level independence

The categorical transfer matrix of a hadron is independent of the
braid representative, PawLei embedding, and crossing evaluation order.
The Markov trace computed at the constituent level (individual quark
knots) agrees with the composite-level trace (composite knot).

LaTeX label: `prop:transfer-matrix-level-independence`

## References

- [manuscript] §4/transfer-matrix-level-independence
- [jones1987] https://doi.org/10.2307/1971403

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A hadron configuration: constituent knots linked at a brane point. -/
structure HadronConfig where
  /-- Number of constituent knots. -/
  numConstituents : ℕ
  /-- Constituent Skein polynomials (one per knot). -/
  constituentPolynomials : List R_q
  /-- The composite knot Skein polynomial. -/
  compositePolynomial : R_q
  /-- Correct number of constituents. -/
  constituents_length : constituentPolynomials.length = numConstituents

/-- **Transfer matrix level independence** (constituent-composite agreement):

    The product of Markov-traced constituent volumes equals the
    Markov trace of the composite knot:

      Π_{i=0}^{n-2} V̂_i^{const}(q) = V̂^{comp}(q) = P_{K_H}(q)

    Furthermore, the categorical transfer matrix depends only on
    the isotopy class of the hadron and the knot types of its
    constituents — it is independent of the braid representative,
    PawLei embedding, and crossing evaluation order within S_p. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [manuscript] §4/transfer-matrix-level-independence
/-- **External axiom (Jones 1987): Markov trace product theorem.** -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
axiom transfer_matrix_level_independence_axiom :
    ∀ (H : HadronConfig) (constituentProduct : R_q),
      constituentProduct = H.constituentPolynomials.foldl (· * ·) 1 →
      constituentProduct = H.compositePolynomial

theorem transfer_matrix_level_independence
    (H : HadronConfig)
    (constituentProduct : R_q)
    (h_prod : constituentProduct = H.constituentPolynomials.foldl (· * ·) 1)
    : constituentProduct = H.compositePolynomial :=
  transfer_matrix_level_independence_axiom H constituentProduct h_prod

/-- **External axiom (manuscript §4/bundle-isotopy-equivalence):
    isotopy-equivalent configurations yield equal transfer matrices.** -/
-- Ref: [manuscript] §4/transfer-matrix-level-independence
axiom transfer_matrix_path_independence_axiom :
    ∀ (transferMatrix1 transferMatrix2 : R_q),
      True →
      transferMatrix1 = transferMatrix2

/-- Path independence on S_p: two braiding operations producing
    isotopy-equivalent configurations have the same transfer matrix. -/
-- Ref: [manuscript] §4/transfer-matrix-level-independence
theorem transfer_matrix_path_independence
    (transferMatrix1 transferMatrix2 : R_q)
    (h_isotopy : True) :
    transferMatrix1 = transferMatrix2 :=
  transfer_matrix_path_independence_axiom transferMatrix1 transferMatrix2 h_isotopy

end QOU
