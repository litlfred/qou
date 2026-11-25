import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-!
# Signature of the traced Reeb–horizontal Dirac square (bean `qou-2k68`, route 2b)

Route 2b asks whether the relativistic worldline Lagrangian `-m c √(c² - v²)` of
`QOU.Core.CategoricalHamiltonianLegendre` can be derived from the categorical Lagrangian rather
than postulated. A square-root Lagrangian arises from a quadratic Lagrangian by eliminating an
einbein, and that needs an **indefinite** (Lorentzian) quadratic form in the Reeb rate `ω` and
the horizontal rate `u`:

    Q(ω, u) = τ((ω X + u Y)²),   X = Reeb contraction, Y = horizontal connection.

This file decides the signature from the adjointness of `X` and `Y` with respect to a positive
trace (the convention-D Markov weights are non-negative, so `τ = Σ_λ y_λ tr_λ` is positive on
real seminormal blocks):

* `traceSq_nonneg_of_symm` and `weightedTraceSq_nonneg`: if `X` and `Y` are both symmetric, then
  `Q ≥ 0` for all `(ω, u)`. The form is positive semidefinite and has **no light cone**, so the
  worldline square root cannot come from it.
* `trace_mul_eq_zero_of_skew_symm`, `trace_sq_nonpos_of_skew` and
  `traceSq_eq_of_skew_symm`: if `X` is skew-symmetric (like a time derivative) and `Y` is
  symmetric, the cross term vanishes and `Q = ω² τ(X²) + u² τ(Y²)` with `τ(X²) ≤ 0 ≤ τ(Y²)`.
  This form is indefinite, and its null cone is `u² τ(Y²) = ω² (-τ(X²))`.
* `einbein_stationary_value`: for a timelike `Q = s² > 0`, the einbein Lagrangian
  `-Q/(2e) - e m²/2` at its stationary point `e = s/m` equals `-m s`. This is the mechanism that
  produces the square root.

Consequence, recorded in `qou-2k68`: deriving the worldline needs the corpus to fix the
adjointness of the Reeb contraction `ι_ξ∇`. It does not do so today (`CategoricalDiracOperator`
leaves `reeb` an arbitrary endomorphism). Even then the cone speed would be the trace-norm ratio
`√(-τ(X²)/τ(Y²))`, not the weight ratio `c_q = q⁻¹/ℏ_q` alone, and the einbein mass `m` remains a
separate input.

Ground ring: an ordered field `K` (the signature statements need an order; no square roots).
-/

namespace QOU.Core.ReebWorldlineSignature

open Matrix BigOperators

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
variable {n : Type*} [Fintype n]

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- `tr(Z Z) = Σ_{i,j} Z_ij Z_ji`. -/
lemma trace_mul_self_eq (Z : Matrix n n K) :
    (Z * Z).trace = ∑ i, ∑ j, Z i j * Z j i := by
  simp [Matrix.trace, Matrix.mul_apply]

/-- For a symmetric matrix, `tr(Z²) ≥ 0`. -/
theorem trace_sq_nonneg_of_symm {Z : Matrix n n K} (hZ : Zᵀ = Z) : 0 ≤ (Z * Z).trace := by
  rw [trace_mul_self_eq]
  refine Finset.sum_nonneg (fun i _ => Finset.sum_nonneg (fun j _ => ?_))
  have h : Z j i = Z i j := by
    have := congrFun (congrFun hZ i) j
    simpa [Matrix.transpose_apply] using this
  rw [h]
  exact mul_self_nonneg _

/-- **No light cone from two symmetric generators.** If the Reeb contraction `X` and the
horizontal connection `Y` are symmetric, `tr((ωX + uY)²) ≥ 0` for every `(ω, u)`. -/
theorem traceSq_nonneg_of_symm {X Y : Matrix n n K} (hX : Xᵀ = X) (hY : Yᵀ = Y) (ω u : K) :
    0 ≤ ((ω • X + u • Y) * (ω • X + u • Y)).trace := by
  apply trace_sq_nonneg_of_symm
  rw [Matrix.transpose_add, Matrix.transpose_smul, Matrix.transpose_smul, hX, hY]

/-- The same statement for a positive weighted trace `Σ_λ y_λ tr_λ` over a family of blocks with
`y_λ ≥ 0` (the convention-D Markov weights). -/
theorem weightedTraceSq_nonneg {ι : Type*} (s : Finset ι) (y : ι → K) (hy : ∀ l ∈ s, 0 ≤ y l)
    (X Y : ι → Matrix n n K) (hX : ∀ l, (X l)ᵀ = X l) (hY : ∀ l, (Y l)ᵀ = Y l) (ω u : K) :
    0 ≤ ∑ l ∈ s, y l * ((ω • X l + u • Y l) * (ω • X l + u • Y l)).trace :=
  Finset.sum_nonneg (fun l hl => mul_nonneg (hy l hl) (traceSq_nonneg_of_symm (hX l) (hY l) ω u))

/-- For `X` skew-symmetric and `Y` symmetric, `tr(X Y) = 0`. -/
theorem trace_mul_eq_zero_of_skew_symm {X Y : Matrix n n K} (hX : Xᵀ = -X) (hY : Yᵀ = Y) :
    (X * Y).trace = 0 := by
  have h1 : (X * Y).trace = (Y * X).trace := Matrix.trace_mul_comm X Y
  have h2 : (X * Y).trace = ((X * Y)ᵀ).trace := (Matrix.trace_transpose _).symm
  rw [Matrix.transpose_mul, hX, hY, Matrix.mul_neg, Matrix.trace_neg] at h2
  linarith

/-- For a skew-symmetric matrix, `tr(X²) ≤ 0`. -/
theorem trace_sq_nonpos_of_skew {X : Matrix n n K} (hX : Xᵀ = -X) : (X * X).trace ≤ 0 := by
  rw [trace_mul_self_eq]
  have key : ∀ i j, X i j * X j i = -(X i j * X i j) := by
    intro i j
    have := congrFun (congrFun hX i) j
    simp only [Matrix.transpose_apply, Matrix.neg_apply] at this
    rw [this]; ring
  simp only [key, Finset.sum_neg_distrib]
  exact neg_nonpos.mpr (Finset.sum_nonneg (fun i _ => Finset.sum_nonneg
    (fun j _ => mul_self_nonneg _)))

/-- **Indefinite form from a skew Reeb contraction.** With `X` skew and `Y` symmetric,
`tr((ωX + uY)²) = ω² tr(X²) + u² tr(Y²)`, the cross term vanishing. -/
theorem traceSq_eq_of_skew_symm {X Y : Matrix n n K} (hX : Xᵀ = -X) (hY : Yᵀ = Y) (ω u : K) :
    ((ω • X + u • Y) * (ω • X + u • Y)).trace =
      ω ^ 2 * (X * X).trace + u ^ 2 * (Y * Y).trace := by
  have hxy := trace_mul_eq_zero_of_skew_symm hX hY
  have hyx : (Y * X).trace = 0 := by rw [Matrix.trace_mul_comm]; exact hxy
  simp only [Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.trace_add, Matrix.trace_smul, smul_eq_mul, hxy, hyx]
  ring

/-- The null cone of the indefinite form: `Q(ω, u) = 0 ↔ u² tr(Y²) = ω² (-tr(X²))`. -/
theorem traceSq_null_iff {X Y : Matrix n n K} (hX : Xᵀ = -X) (hY : Yᵀ = Y) (ω u : K) :
    ((ω • X + u • Y) * (ω • X + u • Y)).trace = 0 ↔
      u ^ 2 * (Y * Y).trace = ω ^ 2 * (-(X * X).trace) := by
  rw [traceSq_eq_of_skew_symm hX hY]
  constructor <;> intro h <;> linarith

/-- **Einbein elimination.** For `Q = s²` with `s > 0` and `m > 0`, the einbein Lagrangian
`L(e) = -Q/(2e) - e m²/2` is stationary at `e = s/m` (`dL/de = Q/(2e²) - m²/2 = 0`), and its value
there is `-m s`: the square-root worldline Lagrangian. -/
theorem einbein_stationary_value {Q s m : K} (hs : 0 < s) (hm : 0 < m) (hQ : Q = s * s) :
    Q / (2 * (s / m) ^ 2) - m ^ 2 / 2 = 0 ∧
      -Q / (2 * (s / m)) - (s / m) * m ^ 2 / 2 = -m * s := by
  have hs0 : s ≠ 0 := ne_of_gt hs
  have hm0 : m ≠ 0 := ne_of_gt hm
  subst hQ
  constructor
  · field_simp; ring
  · field_simp; ring

end QOU.Core.ReebWorldlineSignature
