import Mathlib.RingTheory.AdjoinRoot
import Mathlib.RingTheory.PowerBasis

/-!
# QOU.Hecke.H2AlgebraDimension — `H_2(q)` is a 2-dimensional K-algebra

Brick `qou-lrz1` at `n = 2`: the concrete Iwahori–Hecke algebra
`H_2(q) = K[σ]/(σ² - (q-1)σ - q)` is realised as
`AdjoinRoot (X² - (q-1)X - q)`, and this file proves — sorry-free over a
field — that it is a **finite-dimensional K-algebra of dimension `2 = 2!`**,
with the power basis `{1, σ}`.

This is the `n = 2` case of the general `dim H_n(q) = n!` claim (brick
`qou-lrz1`), the prerequisite for the `T_w`-basis Gram determinant
`det(Gram) = [n]_q!` (brick `qou-twwf`).  The dimension and the
`FiniteDimensional` instance are exactly the hypotheses the end-to-end
semisimplicity hook `QOU.MathlibExt.isSemisimpleRing_of_gram_det_eq_qFactorial`
requires of the carrier algebra.
-/

namespace QOU.Hecke

open Polynomial

variable {K : Type*} [Field K]

/-- The **`H_2(q)` Hecke quadratic** `X² - (q-1)X - q`.  Its root is the
    Hecke generator `σ` (`σ² = (q-1)σ + q`); the quotient
    `K[X]/(h2Poly)` is the Iwahori–Hecke algebra `H_2(q)`. -/
noncomputable def h2Poly (q : K) : K[X] := X ^ 2 - C (q - 1) * X - C q

/-- **`h2Poly` is monic (sorry-free).** -/
theorem h2Poly_monic (q : K) : (h2Poly q).Monic := by
  unfold h2Poly; monicity!

/-- **`h2Poly` has degree 2 (sorry-free).** -/
theorem h2Poly_natDegree (q : K) : (h2Poly q).natDegree = 2 := by
  unfold h2Poly; compute_degree!

/-- **`h2Poly ≠ 0` (sorry-free).** -/
theorem h2Poly_ne_zero (q : K) : h2Poly q ≠ 0 := (h2Poly_monic q).ne_zero

/-- The **power basis `{1, σ}` of `H_2(q) = AdjoinRoot (h2Poly q)`**
    (sorry-free), of dimension `2`. -/
noncomputable def h2PowerBasis (q : K) : PowerBasis K (AdjoinRoot (h2Poly q)) :=
  AdjoinRoot.powerBasis' (h2Poly_monic q)

/-- **The power basis has dimension 2 (sorry-free).** -/
@[simp] theorem h2PowerBasis_dim (q : K) : (h2PowerBasis q).dim = 2 := by
  rw [h2PowerBasis, AdjoinRoot.powerBasis'_dim, h2Poly_natDegree]

/-- **`H_2(q)` is finite-dimensional over `K` (sorry-free).**  The
    instance the semisimplicity hooks require of the carrier. -/
instance h2_finiteDimensional (q : K) :
    FiniteDimensional K (AdjoinRoot (h2Poly q)) :=
  (h2PowerBasis q).finite

/-- **`dim_K H_2(q) = 2 = 2!` (sorry-free).**  The `n = 2` instance of
    `dim H_n(q) = n!` (brick `qou-lrz1`): the Iwahori–Hecke algebra
    `H_2(q) = K[σ]/(σ²-(q-1)σ-q)` is `2`-dimensional, spanned by the
    `T_w` basis `{T_e, T_{s}} = {1, σ}` indexed by `S_2 = {e, s}`. -/
theorem h2_finrank (q : K) :
    Module.finrank K (AdjoinRoot (h2Poly q)) = 2 := by
  rw [(h2PowerBasis q).finrank, h2PowerBasis_dim]

end QOU.Hecke
