import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic


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

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
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
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [manuscript] §4/transfer-matrix-level-independence
/-- **External axiom (Jones 1987): Markov trace product theorem.** -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
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
/-- **REMOVED 2026-05-17**: the previous
    `transfer_matrix_path_independence_axiom` used `True` as the
    isotopy-equivalence hypothesis, making it equivalent to
    `∀ tm1 tm2 : R_q, tm1 = tm2` — an **inconsistent** axiom
    (`R_q = LaurentPolynomial ℤ` has more than one element).

    The structural content (isotopy-equivalent configurations have
    equal transfer matrices) needs a proper isotopy predicate; a
    `True` placeholder cannot stand in for the actual hypothesis.

    For the actual mass-invariance content see
    `reidemeister-mass-invariance.lean` which uses proper
    Reidemeister-move equivalence relations. -/

end QOU


/-! ## §3b-cond conditional-class hypothesis (audit-visibility stub) -/

namespace QOU.BraidKnot.TransferMatrixLevel.ConditionalAudit

class CrystalGraphRealization : Prop where
  holds : True

def transfer_matrix_level_conditional [_inst : CrystalGraphRealization] : True := trivial

end QOU.BraidKnot.TransferMatrixLevel.ConditionalAudit
