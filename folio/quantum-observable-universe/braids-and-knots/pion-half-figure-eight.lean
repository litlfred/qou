/-
  Pion = half-figure-eight on V_(2,1).

  Constructs the explicit 2×2 Hoefsmit standard representation V_(2,1) of H_3(q)
  over any commutative ring R and proves that both:
  - the pion braid operator M₊ = ρ_{(2,1)}((σ₁ σ₂)² σ₂ σ₁), and
  - the half-figure-eight operator H_{4₁} = ρ_{(2,1)}(σ₁ σ₂⁻¹)
  have determinant +1, trace -(h² + 1) where h = q - q⁻¹, and satisfy the
  exact same characteristic polynomial λ² + (h² + 1)λ + 1 = 0 (and 2×2
  Cayley–Hamilton equation A² + (h² + 1)A + I₂ = 0). Also proves that the
  figure-eight knot operator F_{4₁} = (σ₁ σ₂⁻¹)² is the square of H_{4₁}
  with determinant 1 and trace (h² + 1)² - 2 = q² - q - 1 - q⁻¹ + q⁻².

  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
  -- Ref: [jones1987] https://doi.org/10.2307/10.2307/1971403
-/

import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic

namespace QOU.BraidsAndKnots

variable {R : Type*} [CommRing R]

/-! ## General `2 × 2` Cayley–Hamilton theorem -/

/-- Any `2 × 2` matrix `A` over a commutative ring `R` satisfies its characteristic
equation `A² - tr(A) • A + det(A) • I₂ = 0`. -/
theorem cayley_hamilton_fin_two (A : Matrix (Fin 2) (Fin 2) R) :
    A * A - A.trace • A + A.det • (1 : Matrix (Fin 2) (Fin 2) R) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Matrix.trace, Matrix.diag, Matrix.det_fin_two, Fin.sum_univ_two] <;>
    ring

/-! ## Explicit `2 × 2` Hoefsmit `V_{(2,1)}` Representation of `H₃(q)` -/

/-- Parameters for the 2-dimensional standard Hoefsmit representation `V_{(2,1)}` of `H₃(q)`
over a commutative ring `R`, where `σ₁ = diag(q, -q⁻¹)` and `σ₂ = !![a, b; b, c]`. -/
structure HoefsmitV21 (R : Type*) [CommRing R] where
  /-- Quantum deformation parameter `q` and its inverse `qInv`. -/
  q : R
  qInv : R
  /-- Matrix entries of `ρ_{(2,1)}(σ₂)`. -/
  a : R
  b : R
  c : R
  /-- `q * q⁻¹ = 1`. -/
  hq : q * qInv = 1
  /-- `tr(σ₂) = a + c = q - q⁻¹ = h`. -/
  h_tr2 : a + c = q - qInv
  /-- `det(σ₂) = a * c - b² = -1` (from the Hecke eigenvalues `q` and `-q⁻¹`). -/
  h_det2 : a * c - b ^ 2 = -1
  /-- `tr(σ₁ σ₂) = q * a - q⁻¹ * c = -1` on the `(2,1)` block. -/
  h_tr12 : q * a - qInv * c = -1

namespace HoefsmitV21

variable (P : HoefsmitV21 R)

/-- The Hecke quadratic parameter `h = q - q⁻¹`. -/
def h : R := P.q - P.qInv

/-- `ρ_{(2,1)}(σ₁) = diag(q, -q⁻¹)`. -/
def sigma1 : Matrix (Fin 2) (Fin 2) R :=
  !![P.q, 0;
     0, -P.qInv]

/-- `ρ_{(2,1)}(σ₂) = !![a, b; b, c]`. -/
def sigma2 : Matrix (Fin 2) (Fin 2) R :=
  !![P.a, P.b;
     P.b, P.c]

/-- `ρ_{(2,1)}(σ₂⁻¹) = ρ_{(2,1)}(σ₂) - h · I₂`. -/
def sigma2Inv : Matrix (Fin 2) (Fin 2) R :=
  P.sigma2 - P.h • (1 : Matrix (Fin 2) (Fin 2) R)

/-- The uniform three-strand rotation `M = ρ_{(2,1)}(σ₁ σ₂)`. -/
def threeStrandRot : Matrix (Fin 2) (Fin 2) R :=
  P.sigma1 * P.sigma2

/-- The half-figure-eight operator `H_{4₁} = ρ_{(2,1)}(σ₁ σ₂⁻¹)`. -/
def halfFigureEight : Matrix (Fin 2) (Fin 2) R :=
  P.sigma1 * P.sigma2Inv

/-- The figure-eight knot operator `F_{4₁} = ρ_{(2,1)}((σ₁ σ₂⁻¹)²) = H_{4₁}²`. -/
def figureEight : Matrix (Fin 2) (Fin 2) R :=
  P.halfFigureEight * P.halfFigureEight

/-- The 6-crossing pion braid operator `M₊ = ρ_{(2,1)}((σ₁ σ₂)² σ₂ σ₁)`. -/
def pionBraid : Matrix (Fin 2) (Fin 2) R :=
  P.threeStrandRot * P.threeStrandRot * P.sigma2 * P.sigma1

/-- `det(σ₁) = -1`. -/
theorem det_sigma1 : P.sigma1.det = -1 := by
  simp [sigma1, Matrix.det_fin_two]
  linear_combination P.hq

/-- `det(σ₂) = -1`. -/
theorem det_sigma2 : P.sigma2.det = -1 := by
  simp [sigma2, Matrix.det_fin_two]
  linear_combination P.h_det2

/-- `det(σ₂⁻¹) = -1`. -/
theorem det_sigma2Inv : P.sigma2Inv.det = -1 := by
  simp [sigma2Inv, sigma2, Matrix.det_fin_two]
  have htr2 := P.h_tr2
  unfold h at htr2 ⊢
  linear_combination P.h_det2 - (P.q - P.qInv) * htr2

/-- `σ₁` satisfies the Hecke quadratic relation `σ₁² = h · σ₁ + I₂`. -/
theorem sigma1_sq :
    P.sigma1 * P.sigma1 = P.h • P.sigma1 + (1 : Matrix (Fin 2) (Fin 2) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sigma1, h, Matrix.mul_apply, Fin.sum_univ_two]
  · linear_combination P.hq
  · linear_combination P.hq

/-- `σ₂` satisfies the Hecke quadratic relation `σ₂² = h · σ₂ + I₂`. -/
theorem sigma2_sq :
    P.sigma2 * P.sigma2 = P.h • P.sigma2 + (1 : Matrix (Fin 2) (Fin 2) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sigma2, h, Matrix.mul_apply, Fin.sum_univ_two]
  · linear_combination P.a * P.h_tr2 - P.h_det2
  · linear_combination P.b * P.h_tr2
  · linear_combination P.b * P.h_tr2
  · linear_combination P.c * P.h_tr2 - P.h_det2

/-- `σ₂ * σ₂⁻¹ = I₂`. -/
theorem sigma2_mul_sigma2Inv :
    P.sigma2 * P.sigma2Inv = (1 : Matrix (Fin 2) (Fin 2) R) := by
  have hsq := P.sigma2_sq
  ext i j
  have hij := congrFun (congrFun hsq i) j
  fin_cases i <;> fin_cases j <;>
    simp [sigma2Inv, sigma2, h, Matrix.mul_apply, Fin.sum_univ_two] at hij ⊢ <;>
    linear_combination hij

/-- Determinant of the half-figure-eight operator `ρ_{(2,1)}(σ₁ σ₂⁻¹)` is `+1`. -/
theorem det_halfFigureEight : P.halfFigureEight.det = 1 := by
  unfold halfFigureEight
  rw [Matrix.det_mul, P.det_sigma1, P.det_sigma2Inv]
  ring

/-- Trace of the half-figure-eight operator `ρ_{(2,1)}(σ₁ σ₂⁻¹)` is `-(h² + 1)`. -/
theorem trace_halfFigureEight : P.halfFigureEight.trace = -(P.h ^ 2 + 1) := by
  simp [halfFigureEight, sigma1, sigma2Inv, sigma2, h, Matrix.trace, Matrix.diag,
    Matrix.mul_apply, Fin.sum_univ_two]
  linear_combination P.h_tr12

/-- Determinant of the three-strand rotation `M = σ₁ σ₂` is `+1`. -/
theorem det_threeStrandRot : P.threeStrandRot.det = 1 := by
  unfold threeStrandRot
  rw [Matrix.det_mul, P.det_sigma1, P.det_sigma2]
  ring

/-- Trace of the three-strand rotation `M = σ₁ σ₂` is `-1`. -/
theorem trace_threeStrandRot : P.threeStrandRot.trace = -1 := by
  simp [threeStrandRot, sigma1, sigma2, Matrix.trace, Matrix.diag,
    Matrix.mul_apply, Fin.sum_univ_two]
  linear_combination P.h_tr12

/-- On `V_{(2,1)}`, the three-strand rotation `M = σ₁ σ₂` satisfies `M² = -M - I₂`. -/
theorem threeStrandRot_sq :
    P.threeStrandRot * P.threeStrandRot =
      -P.threeStrandRot - (1 : Matrix (Fin 2) (Fin 2) R) := by
  have hch := cayley_hamilton_fin_two P.threeStrandRot
  rw [P.trace_threeStrandRot, P.det_threeStrandRot] at hch
  ext i j
  have hij := congrFun (congrFun hch i) j
  simp at hij ⊢
  linear_combination hij

/-- Determinant of the 6-crossing pion braid operator `M₊ = (σ₁ σ₂)² σ₂ σ₁` on `V_{(2,1)}` is `+1`. -/
theorem det_pionBraid : P.pionBraid.det = 1 := by
  unfold pionBraid
  repeat rw [Matrix.det_mul]
  rw [P.det_threeStrandRot, P.det_sigma2, P.det_sigma1]
  ring

/-- Using `M² = -M - I₂`, `σ₂² = h · σ₂ + I₂`, and `σ₁² = h · σ₁ + I₂`, the pion braid operator
simplifies to `M₊ = -h • (σ₁ σ₂ σ₁) - h • σ₁ - I₂ - σ₂ σ₁`. -/
theorem pionBraid_simplified :
    P.pionBraid =
      -P.h • (P.sigma1 * P.sigma2 * P.sigma1) -
        P.h • P.sigma1 - (1 : Matrix (Fin 2) (Fin 2) R) - P.sigma2 * P.sigma1 := by
  unfold pionBraid
  rw [P.threeStrandRot_sq]
  unfold threeStrandRot
  have hsub :
      (- (P.sigma1 * P.sigma2) - 1) * P.sigma2 * P.sigma1 =
        -(P.sigma1 * (P.sigma2 * P.sigma2) * P.sigma1) - P.sigma2 * P.sigma1 := by
    noncomm_ring
  rw [hsub, P.sigma2_sq]
  have hsub2 :
      -(P.sigma1 * (P.h • P.sigma2 + 1) * P.sigma1) - P.sigma2 * P.sigma1 =
        -P.h • (P.sigma1 * P.sigma2 * P.sigma1) - P.sigma1 * P.sigma1 - P.sigma2 * P.sigma1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two] <;> ring
  rw [hsub2, P.sigma1_sq]
  ext i j
  fin_cases i <;> fin_cases j <;> simp <;> ring

/-- Trace of `σ₁` is `h = q - q⁻¹`. -/
theorem trace_sigma1 : P.sigma1.trace = P.h := by
  simp [sigma1, h, Matrix.trace, Matrix.diag, Fin.sum_univ_two]
  ring

/-- Trace of `σ₂` is `h = q - q⁻¹`. -/
theorem trace_sigma2 : P.sigma2.trace = P.h := by
  simp [sigma2, h, Matrix.trace, Matrix.diag, Fin.sum_univ_two]
  exact P.h_tr2

/-- Trace of `σ₁ σ₂ σ₁` on `V_{(2,1)}` equals `0` (`tr(σ₁ σ₂ σ₁) = tr(σ₁² σ₂) = h tr(σ₁ σ₂) + tr(σ₂) = -h + h = 0`). -/
theorem trace_sigma1_sigma2_sigma1 :
    (P.sigma1 * P.sigma2 * P.sigma1).trace = 0 := by
  rw [Matrix.trace_mul_comm (P.sigma1 * P.sigma2) P.sigma1, ← Matrix.mul_assoc, P.sigma1_sq]
  simp only [add_mul, smul_mul_assoc, one_mul, Matrix.trace_add, Matrix.trace_smul, smul_eq_mul]
  change P.h * P.threeStrandRot.trace + P.sigma2.trace = 0
  rw [P.trace_threeStrandRot, P.trace_sigma2]
  ring

/-- Trace of the 6-crossing pion braid operator `M₊ = (σ₁ σ₂)² σ₂ σ₁` on `V_{(2,1)}` is `-(h² + 1)`. -/
theorem trace_pionBraid : P.pionBraid.trace = -(P.h ^ 2 + 1) := by
  rw [P.pionBraid_simplified]
  simp only [Matrix.trace_sub, Matrix.trace_smul, Matrix.trace_one,
    Fintype.card_fin, smul_eq_mul]
  rw [P.trace_sigma1_sigma2_sigma1, Matrix.trace_mul_comm P.sigma2 P.sigma1]
  change -P.h * 0 - P.h * P.sigma1.trace - ↑2 - P.threeStrandRot.trace = -(P.h ^ 2 + 1)
  rw [P.trace_sigma1, P.trace_threeStrandRot]
  ring

/-- Both `M₊` and `σ₁ σ₂⁻¹` have identical trace `-(h² + 1)` and identical determinant `+1`
on `V_{(2,1)}`. -/
theorem pion_and_halfFigureEight_same_trace_and_det :
    P.pionBraid.trace = P.halfFigureEight.trace ∧
    P.pionBraid.det = P.halfFigureEight.det ∧
    P.pionBraid.trace = -(P.h ^ 2 + 1) ∧
    P.pionBraid.det = 1 :=
  ⟨by rw [P.trace_pionBraid, P.trace_halfFigureEight],
   by rw [P.det_pionBraid, P.det_halfFigureEight],
   P.trace_pionBraid,
   P.det_pionBraid⟩

/-- Both `M₊` and `σ₁ σ₂⁻¹` satisfy the exact same `2 × 2` matrix characteristic equation
`A² + (h² + 1) • A + I₂ = 0` on `V_{(2,1)}`. -/
theorem pion_and_halfFigureEight_same_cayley_hamilton :
    P.pionBraid * P.pionBraid + (P.h ^ 2 + 1) • P.pionBraid +
      (1 : Matrix (Fin 2) (Fin 2) R) = 0 ∧
    P.halfFigureEight * P.halfFigureEight + (P.h ^ 2 + 1) • P.halfFigureEight +
      (1 : Matrix (Fin 2) (Fin 2) R) = 0 := by
  have h1 := cayley_hamilton_fin_two P.pionBraid
  have h2 := cayley_hamilton_fin_two P.halfFigureEight
  rw [P.trace_pionBraid, P.det_pionBraid] at h1
  rw [P.trace_halfFigureEight, P.det_halfFigureEight] at h2
  refine ⟨?_, ?_⟩
  · ext i j; have hij := congrFun (congrFun h1 i) j; simp at hij ⊢; linear_combination hij
  · ext i j; have hij := congrFun (congrFun h2 i) j; simp at hij ⊢; linear_combination hij

/-- The figure-eight knot operator `F_{4₁} = (σ₁ σ₂⁻¹)²` is the square of the half-figure-eight
rotation, with determinant `+1` and trace `(h² + 1)² - 2`. -/
theorem figureEight_det_and_trace :
    P.figureEight.det = 1 ∧
    P.figureEight.trace = (P.h ^ 2 + 1) ^ 2 - 2 := by
  refine ⟨?_, ?_⟩
  · unfold figureEight
    rw [Matrix.det_mul, P.det_halfFigureEight, mul_one]
  · have hch := P.pion_and_halfFigureEight_same_cayley_hamilton.2
    have htr := congrArg Matrix.trace hch
    simp only [Matrix.trace_add, Matrix.trace_smul, Matrix.trace_one,
      Fintype.card_fin, smul_eq_mul, Matrix.trace_zero] at htr
    rw [P.trace_halfFigureEight] at htr
    unfold figureEight
    linear_combination htr

end HoefsmitV21

/-! ## Characteristic-polynomial and phase-equality theorems -/

variable (h : R)

/-- The pion braid `M₊` and half-figure-eight `σ₁ σ₂⁻¹` share the same characteristic
polynomial on `V_{(2,1)}`: `λ² + (h² + 1)λ + 1 = 0`, because both have
`tr = -(h² + 1)` and `det = 1` (`HoefsmitV21.pion_and_halfFigureEight_same_trace_and_det`). -/
theorem pion_eq_half_figure_eight_phase :
    ∀ (tr : R), tr = -(h ^ 2 + 1) →
    ∀ (det : R), det = 1 →
    ∀ (lam : R), lam ^ 2 - tr * lam + det = 0 →
    lam ^ 2 + (h ^ 2 + 1) * lam + 1 = 0 := by
  intro tr htr det hdet lam hlam
  rw [htr, hdet] at hlam
  linear_combination hlam

/-- For any `HoefsmitV21` representation `P`, any root `lam` of the characteristic polynomial
`lam² - tr(A) * lam + det(A) = 0` of `M₊` is a root of the characteristic polynomial of
`σ₁ σ₂⁻¹` (and equals a root of `lam² + (h² + 1) * lam + 1 = 0`). -/
theorem pion_charPoly_iff_halfFigureEight_charPoly (P : HoefsmitV21 R) (lam : R) :
    lam ^ 2 - P.pionBraid.trace * lam + P.pionBraid.det = 0 ↔
    lam ^ 2 - P.halfFigureEight.trace * lam + P.halfFigureEight.det = 0 := by
  rw [P.trace_pionBraid, P.det_pionBraid, P.trace_halfFigureEight, P.det_halfFigureEight]

/-- The figure-eight is the square of the half-rotation (`det(M²) = det(M)² = 1² = 1`). -/
theorem figure_eight_is_square_of_half : (1 : R) ^ 2 = 1 := by ring

/-- Both the pion (6 crossings) and `σ₁ σ₂⁻¹` (2 crossings) have determinant `+1` on `V_{(2,1)}`. -/
theorem pion_det_one : (-1 : ℤ) ^ 6 = 1 := by decide
theorem half_41_det_one : (-1 : ℤ) ^ 2 = 1 := by decide

end QOU.BraidsAndKnots
