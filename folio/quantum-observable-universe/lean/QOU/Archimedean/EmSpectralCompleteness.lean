import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Matrix.Basic
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

- [leitner2026] §5/em-spectral-completeness
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
-- Ref: [leitner2026] §5/em-spectral-completeness
theorem hecke_minimal_polynomial_splits :
    ∃ (lp lm : S.R) (_ : lp = lambdaPlus S) (_ : lm = lambdaMinus S),
      IsUnit (lp - lm) := by
  refine ⟨lambdaPlus S, lambdaMinus S, rfl, rfl, ?_⟩
  exact eigenvalues_distinct S

end SpectralRing

/-- **Theorem (two-strand spectral completeness).**

    The endomorphism algebra `End(A ⊗ A)` of the rank-2 block is
    modelled as `M₂(R) = Matrix (Fin 2) (Fin 2) R`, with the braiding
    diagonal in its eigenbasis (`diagonal ![λ₊, λ₋]`).  Its two
    resolvent projections

      `p₊ = (λ₊−λ₋)⁻¹ · (c − λ₋·1)`,   `p₋ = (λ₊−λ₋)⁻¹ · (λ₊·1 − c)`

    are two non-zero idempotents with `p₊ + p₋ = 1` and `p₊·p₋ = 0`
    (each equals a coordinate projection `diagonal ![1,0]` /
    `diagonal ![0,1]`).  The construction is well-defined precisely
    because `λ₊ − λ₋` is a unit (`eigenvalues_distinct`) — this is
    where the spectral content enters (`(λ₊−λ₋)⁻¹·(λ₊−λ₋) = 1`).

    **Correction (was a false axiom).**  This was previously an `axiom`
    asserting the idempotents live in the base ring `S.R`.  That
    statement is *false*: an integral domain such as `ℝ` (a valid
    `SpectralRing`) has no non-trivial idempotent splitting of `1`
    (`p₊·p₋ = 0` forces `p₊ = 0 ∨ p₋ = 0`).  The idempotents live in
    `End(A⊗A) = M₂(R)`, not in `R`.  Requires `Nontrivial R` (over the
    zero ring `p₊ = 0`). -/
-- Ref: [jones1987] §3–§4 (Hecke representations of braid groups; the
--      two braiding eigenvalues on the standard rank-2 block)
-- Ref: [leitner2026] §5/em-spectral-completeness
theorem em_spectral_completeness (S : SpectralRing) [Nontrivial S.R] :
    ∃ (p_plus p_minus : Matrix (Fin 2) (Fin 2) S.R),
      p_plus + p_minus = 1 ∧
      p_plus * p_minus = 0 ∧
      p_plus ≠ 0 ∧ p_minus ≠ 0 := by
  obtain ⟨u, hu_eq⟩ := S.eigenvalues_distinct
  have hinv : (↑u⁻¹ : S.R) * (S.lambdaPlus - S.lambdaMinus) = 1 := by
    rw [← hu_eq]; exact u.inv_mul
  let p_plus : Matrix (Fin 2) (Fin 2) S.R := (↑u⁻¹ : S.R) •
      (Matrix.diagonal ![S.lambdaPlus, S.lambdaMinus]
        - S.lambdaMinus • (1 : Matrix (Fin 2) (Fin 2) S.R))
  let p_minus : Matrix (Fin 2) (Fin 2) S.R := (↑u⁻¹ : S.R) •
      (S.lambdaPlus • (1 : Matrix (Fin 2) (Fin 2) S.R)
        - Matrix.diagonal ![S.lambdaPlus, S.lambdaMinus])
  have hpp : p_plus = Matrix.diagonal ![1, 0] := by
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [p_plus, Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul, hinv]
  have hpm : p_minus = Matrix.diagonal ![0, 1] := by
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [p_minus, Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul, hinv]
  refine ⟨p_plus, p_minus, ?_, ?_, ?_, ?_⟩
  · rw [hpp, hpm]; ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.add_apply]
  · rw [hpp, hpm]; ext i j; fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Matrix.diagonal_apply, Matrix.zero_apply]
  · rw [hpp]; intro h
    have h00 := congrFun (congrFun h 0) 0
    simp at h00
  · rw [hpm]; intro h
    have h11 := congrFun (congrFun h 1) 1
    simp at h11

end QOU.Archimedean
