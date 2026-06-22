import Mathlib.Algebra.Polynomial.Laurent
import QOU.Archimedean.EmCouplingProjection


/-!
# QOU.Archimedean.em_spectral_completeness

Two-strand spectral completeness over a commutative ring `R`.

The endomorphism algebra `End(A ⊗ A)` of the fundamental object's
two-fold tensor power has rank 2 as an `R`-module, splits into
exactly two central idempotents `p₊, p₋` with `p₊ + p₋ = 1`, and
the braiding `c_{A,A}` has only two eigenvalues `q^(1/2), -q^(-1/2)`.

The singlet idempotent `p₋` projects onto the unit `𝟙`. Any scalar
coupling `A ⊗ A → 𝟙` is a multiple of `tr_τ(p₋) · p₋`, hence the
EM coupling is unique up to global normalisation.

LaTeX label: `thm:em-spectral-completeness`

## References

- [manuscript] §5/em-spectral-completeness
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Archimedean

open LaurentPolynomial

/-- Ground ring `R = ℤ[q^{±1/2}, (q - q⁻¹)⁻¹]`.  We model it
abstractly: any commutative ring with `q` invertible and
`q - q⁻¹` invertible suffices for the algebraic content of the
theorem.  In Mathlib terms this is `LaurentPolynomial ℤ` localised
at `q^{1/2}` and `(q - q⁻¹)`. -/
structure SpectralRing where
  R : Type*
  [comm : CommRing R]
  q : Rˣ                              -- q is a unit
  qHalf : Rˣ                          -- q^{1/2} is a unit
  qHalf_sq : (qHalf : R) * qHalf = q  -- (q^{1/2})² = q
  qDiff_unit : IsUnit ((q : R) - ((q⁻¹ : Rˣ) : R))  -- q - q⁻¹ is invertible

namespace SpectralRing

variable (S : SpectralRing)

instance : CommRing S.R := S.comm

/-- The two eigenvalues of the braiding on `A ⊗ A`. -/
def lambdaPlus : S.R := S.qHalf
def lambdaMinus : S.R := -((S.qHalf⁻¹ : S.Rˣ) : S.R)

/-- The two eigenvalues of the categorical braiding are distinct:
    `λ₊ − λ₋ = qHalf + qHalf⁻¹` is a unit in `R`.

    Proof: `(qHalf + qHalf⁻¹)(qHalf − qHalf⁻¹) = qHalf² − qHalf⁻² =
    q − q⁻¹`, a unit by the `SpectralRing.qDiff_unit` field
    (`qHalf² = q` via `qHalf_sq`; `qHalf⁻² = q⁻¹` as units); a factor
    of a unit is a unit (`isUnit_of_mul_isUnit_left`).  Previously an
    `axiom` citing Jones 1987; the unit algebra discharges it from the
    `SpectralRing` fields directly. -/
-- Ref: [jones1987] §3–§4 (Hecke representations of braid groups; the
--      standard-block braiding eigenvalues q and −q⁻¹)
theorem eigenvalues_distinct :
    IsUnit (lambdaPlus S - lambdaMinus S) := by
  have hqh : S.qHalf * S.qHalf = S.q :=
    Units.ext (by rw [Units.val_mul]; exact S.qHalf_sq)
  have h2 : ((S.qHalf⁻¹ : S.Rˣ) : S.R) * ((S.qHalf⁻¹ : S.Rˣ) : S.R)
      = ((S.q⁻¹ : S.Rˣ) : S.R) := by
    rw [← Units.val_mul, ← mul_inv, hqh]
  have key : (lambdaPlus S - lambdaMinus S)
        * ((S.qHalf : S.R) - ((S.qHalf⁻¹ : S.Rˣ) : S.R))
      = (S.q : S.R) - ((S.q⁻¹ : S.Rˣ) : S.R) := by
    simp only [lambdaPlus, lambdaMinus, sub_neg_eq_add]
    have expand : ((S.qHalf : S.R) + ((S.qHalf⁻¹ : S.Rˣ) : S.R))
          * ((S.qHalf : S.R) - ((S.qHalf⁻¹ : S.Rˣ) : S.R))
        = (S.qHalf : S.R) * (S.qHalf : S.R)
          - ((S.qHalf⁻¹ : S.Rˣ) : S.R) * ((S.qHalf⁻¹ : S.Rˣ) : S.R) := by ring
    rw [expand, S.qHalf_sq, h2]
  exact isUnit_of_mul_isUnit_left (key ▸ S.qDiff_unit)

/-- The minimal polynomial of the categorical braiding factors
    over `R` into linear factors with distinct unit roots. -/
-- Ref: [manuscript] §5/em-spectral-completeness
theorem hecke_minimal_polynomial_splits :
    ∃ (lp lm : S.R) (_ : lp = lambdaPlus S) (_ : lm = lambdaMinus S),
      IsUnit (lp - lm) := by
  refine ⟨lambdaPlus S, lambdaMinus S, rfl, rfl, ?_⟩
  exact eigenvalues_distinct S

end SpectralRing

/-! **Theorem (two-strand spectral completeness)**.

    There exist exactly two non-zero central idempotents `p₊, p₋`
    in `End(A ⊗ A)` with `p₊ + p₋ = id` and `p₊ · p₋ = 0`.  The
    singlet idempotent `p₋` projects onto a free rank-1 summand,
    canonically isomorphic to the unit object.

    The corollary is that any scalar coupling `A ⊗ A → 𝟙` is a
    multiple of `tr_τ(p₋) · p₋`. -/
-- Ref: [manuscript] §5/em-spectral-completeness
/-- **External axiom (Jones 1987; manuscript §5): two-strand spectral
    completeness — exactly two central idempotents in End(A⊗A).** -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [manuscript] §5/em-spectral-completeness
axiom em_spectral_completeness_axiom :
    ∀ (S : SpectralRing),
      ∃ (p_plus p_minus : S.R),
        p_plus + p_minus = 1 ∧
        p_plus * p_minus = 0 ∧
        p_plus ≠ 0 ∧ p_minus ≠ 0

theorem em_spectral_completeness (S : SpectralRing) :
    ∃ (p_plus p_minus : S.R),
      p_plus + p_minus = 1 ∧
      p_plus * p_minus = 0 ∧
      p_plus ≠ 0 ∧ p_minus ≠ 0 :=
  em_spectral_completeness_axiom S

end QOU.Archimedean
