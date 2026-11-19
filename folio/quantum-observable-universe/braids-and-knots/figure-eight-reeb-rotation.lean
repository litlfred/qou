/-
  The figure-eight knot operator acts unitarily on V_(2,1).

  M_{4₁} = (σ₁σ₂⁻¹)² is constructed explicitly as a 2×2 real matrix from the
  smooth Hoefsmit seminormal generators σ₁, σ₂ on V_(2,1) for all real q > 0.
  We prove the Hecke quadratic relations, the 3-strand braid relation
  σ₁σ₂σ₁ = σ₂σ₁σ₂, the two-sided inverse σ₂⁻¹, det(M_{4₁}) = 1, the exact
  Laurent trace formula tr(M_{4₁}) = q⁴ - 2q² + 1 - 2q⁻² + q⁻⁴, and the full
  three-regime golden-ratio eigenvalue trichotomy on q > 0.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kashaev1997] https://doi.org/10.1007/s100529801020
  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
-/

import Mathlib.Analysis.Complex.Norm
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic
import QOU.BraidsAndKnots.unit_modulus_of_det_one_small_trace

namespace QOU.BraidsAndKnots

open Matrix

/-! ## §1. Golden Ratio `φ = (1 + √5)/2` and Quadratic Factorizations -/

/-- The golden ratio `φ = (1 + √5)/2`. -/
noncomputable def goldenPhi : ℝ := (1 + Real.sqrt 5) / 2

theorem sqrt_five_pos : 0 < Real.sqrt 5 :=
  Real.sqrt_pos.mpr (by norm_num)

theorem sqrt_five_sq : Real.sqrt 5 ^ 2 = 5 :=
  Real.sq_sqrt (by norm_num)

theorem goldenPhi_pos : 0 < goldenPhi := by
  unfold goldenPhi
  linarith [sqrt_five_pos]

theorem goldenPhi_gt_one : 1 < goldenPhi := by
  unfold goldenPhi
  have h : 2 < Real.sqrt 5 := by
    have h4 : (2 : ℝ) = Real.sqrt 4 := by norm_num
    rw [h4]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  linarith

/-- The defining golden quadratic identity `φ² = φ + 1`. -/
theorem goldenPhi_sq : goldenPhi ^ 2 = goldenPhi + 1 := by
  unfold goldenPhi
  nlinarith [sqrt_five_sq]

/-- The reciprocal golden ratio `φ⁻¹ = (√5 - 1)/2 = φ - 1`. -/
theorem goldenPhi_inv_eq : goldenPhi⁻¹ = goldenPhi - 1 := by
  have hsq : goldenPhi * (goldenPhi - 1) = 1 := by
    linear_combination goldenPhi_sq
  exact inv_eq_of_mul_eq_one_right hsq

theorem goldenPhi_inv_pos : 0 < goldenPhi⁻¹ :=
  inv_pos.mpr goldenPhi_pos

theorem goldenPhi_inv_lt_one : goldenPhi⁻¹ < 1 := by
  rw [goldenPhi_inv_eq]
  unfold goldenPhi
  have h : Real.sqrt 5 < 3 := by
    have h9 : (3 : ℝ) = Real.sqrt 9 := by norm_num
    rw [h9]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  linarith

theorem goldenPhi_inv_lt_goldenPhi : goldenPhi⁻¹ < goldenPhi :=
  lt_trans goldenPhi_inv_lt_one goldenPhi_gt_one

/-- Exact root factorization of `q² - q - 1 = (q - φ)(q + φ⁻¹)`. -/
theorem quad_sub_q_sub_one_factor (q : ℝ) :
    q ^ 2 - q - 1 = (q - goldenPhi) * (q + goldenPhi⁻¹) := by
  rw [goldenPhi_inv_eq]
  linear_combination goldenPhi_sq

/-- Exact root factorization of `q² + q - 1 = (q - φ⁻¹)(q + φ)`. -/
theorem quad_add_q_sub_one_factor (q : ℝ) :
    q ^ 2 + q - 1 = (q - goldenPhi⁻¹) * (q + goldenPhi) := by
  rw [goldenPhi_inv_eq]
  linear_combination goldenPhi_sq

/-! ## §2. Explicit Smooth Hoefsmit Matrices on `V_(2,1)` (`H₃(q)`) -/

/-- Smooth diagonal entry `a(q) = -q⁻² / (q + q⁻¹)` of `σ₂` on `V_(2,1)`.
    Because `(1 - q⁴) · a(q) = q - q⁻¹`, this agrees with `(q - q⁻¹)/(1 - q⁴)` for all
    `q⁴ ≠ 1` and resolves the `0/0` removable singularity at `q = 1`. -/
noncomputable def hoefsmitA (q : ℝ) : ℝ :=
  -(q⁻¹ ^ 2) / (q + q⁻¹)

/-- Smooth diagonal entry `c(q) = q² / (q + q⁻¹)` of `σ₂` on `V_(2,1)`.
    Because `(1 - q⁻⁴) · c(q) = q - q⁻¹`, this agrees with `(q - q⁻¹)/(1 - q⁻⁴)` for all
    `q⁴ ≠ 1` and resolves the `0/0` removable singularity at `q = 1`. -/
noncomputable def hoefsmitC (q : ℝ) : ℝ :=
  (q ^ 2) / (q + q⁻¹)

/-- Smooth off-diagonal binding amplitude `b(q) = √(q² + 1 + q⁻²) / (q + q⁻¹)`
    of `σ₂` on `V_(2,1)`. -/
noncomputable def hoefsmitB (q : ℝ) : ℝ :=
  Real.sqrt (q ^ 2 + 1 + q⁻¹ ^ 2) / (q + q⁻¹)

theorem q_add_inv_pos {q : ℝ} (hq : 0 < q) : 0 < q + q⁻¹ :=
  add_pos hq (inv_pos.mpr hq)

theorem q_add_inv_ne_zero {q : ℝ} (hq : 0 < q) : q + q⁻¹ ≠ 0 :=
  ne_of_gt (q_add_inv_pos hq)

theorem q_sq_add_one_add_inv_sq_pos (q : ℝ) : 0 < q ^ 2 + 1 + q⁻¹ ^ 2 := by
  positivity

/-- Removable-singularity identity for `a(q)`: `(1 - q⁴) · a(q) = q - q⁻¹`,
    so `a(q) = (q - q⁻¹)/(1 - q⁴)` whenever `q⁴ ≠ 1`, while remaining smooth at `q = 1`. -/
theorem hoefsmitA_mul_one_sub_q4 {q : ℝ} (hq : 0 < q) :
    (1 - q ^ 4) * hoefsmitA q = q - q⁻¹ := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero hq
  unfold hoefsmitA
  field_simp
  ring

/-- Removable-singularity identity for `c(q)`: `(1 - q⁻⁴) · c(q) = q - q⁻¹`,
    so `c(q) = (q - q⁻¹)/(1 - q⁻⁴)` whenever `q⁻⁴ ≠ 1`, while remaining smooth at `q = 1`. -/
theorem hoefsmitC_mul_one_sub_q_inv4 {q : ℝ} (hq : 0 < q) :
    (1 - q⁻¹ ^ 4) * hoefsmitC q = q - q⁻¹ := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero hq
  unfold hoefsmitC
  field_simp
  ring

/-- Seminormal trace identity: `a(q) + c(q) = q - q⁻¹`. -/
theorem hoefsmitA_add_C {q : ℝ} (hq : 0 < q) :
    hoefsmitA q + hoefsmitC q = q - q⁻¹ := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero hq
  unfold hoefsmitA hoefsmitC
  field_simp
  ring

/-- Seminormal diagonal product: `a(q) · c(q) = -1 / (q + q⁻¹)²`. -/
theorem hoefsmitA_mul_C {q : ℝ} (hq : 0 < q) :
    hoefsmitA q * hoefsmitC q = -1 / (q + q⁻¹) ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero hq
  unfold hoefsmitA hoefsmitC
  field_simp

/-- Squared binding amplitude: `b(q)² = (q² + 1 + q⁻²) / (q + q⁻¹)² = [3]_q / [2]_q²`. -/
theorem hoefsmitB_sq (q : ℝ) :
    hoefsmitB q ^ 2 = (q ^ 2 + 1 + q⁻¹ ^ 2) / (q + q⁻¹) ^ 2 := by
  unfold hoefsmitB
  rw [div_pow, Real.sq_sqrt (le_of_lt (q_sq_add_one_add_inv_sq_pos q))]

/-- Seminormal determinant identity: `a(q) · c(q) - b(q)² = -1`. -/
theorem hoefsmitA_mul_C_sub_B_sq {q : ℝ} (hq : 0 < q) :
    hoefsmitA q * hoefsmitC q - hoefsmitB q ^ 2 = -1 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero hq
  rw [hoefsmitA_mul_C hq, hoefsmitB_sq]
  field_simp
  ring

/-- Key polynomial identity for `b(q)²`: `b(q)² = 1 + a(q) · c(q)`. -/
theorem hoefsmitB_sq_eq_one_add_AC {q : ℝ} (hq : 0 < q) :
    hoefsmitB q ^ 2 = 1 + hoefsmitA q * hoefsmitC q := by
  linarith [hoefsmitA_mul_C_sub_B_sq hq]

/-- First Hoefsmit generator `σ₁ = diag(q, -q⁻¹)` on `V_(2,1)`. -/
noncomputable def hoefsmitSigma1 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![q, 0; 0, -q⁻¹]

/-- Second Hoefsmit generator `σ₂ = !![a(q), b(q); b(q), c(q)]` on `V_(2,1)`. -/
noncomputable def hoefsmitSigma2 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![hoefsmitA q, hoefsmitB q; hoefsmitB q, hoefsmitC q]

/-- Explicit inverse `σ₂⁻¹ = σ₂ - (q - q⁻¹) · I₂ = !![-c(q), b(q); b(q), -a(q)]` on `V_(2,1)`. -/
noncomputable def hoefsmitSigma2Inv (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![-hoefsmitC q, hoefsmitB q; hoefsmitB q, -hoefsmitA q]

/-- **Hecke quadratic relation for `σ₁`:**
    `σ₁² = (q - q⁻¹) • σ₁ + 1`. -/
theorem hoefsmitSigma1_sq {q : ℝ} (hq : 0 < q) :
    hoefsmitSigma1 q * hoefsmitSigma1 q = (q - q⁻¹) • hoefsmitSigma1 q + 1 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [hoefsmitSigma1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **Hecke quadratic relation for `σ₂`:**
    `σ₂² = (q - q⁻¹) • σ₂ + 1`. -/
theorem hoefsmitSigma2_sq {q : ℝ} (hq : 0 < q) :
    hoefsmitSigma2 q * hoefsmitSigma2 q = (q - q⁻¹) • hoefsmitSigma2 q + 1 := by
  have htr := hoefsmitA_add_C hq
  have hdet := hoefsmitB_sq_eq_one_add_AC hq
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [hoefsmitSigma2, Matrix.mul_apply, Fin.sum_univ_two]
  · linear_combination hdet + hoefsmitA q * htr
  · linear_combination hoefsmitB q * htr
  · linear_combination hoefsmitB q * htr
  · linear_combination hdet + hoefsmitC q * htr

/-- **Two-sided inverse relation for `σ₂`:**
    `σ₂ * σ₂⁻¹ = 1` and `σ₂⁻¹ * σ₂ = 1`. -/
theorem hoefsmitSigma2_mul_inv {q : ℝ} (hq : 0 < q) :
    hoefsmitSigma2 q * hoefsmitSigma2Inv q = 1 ∧
    hoefsmitSigma2Inv q * hoefsmitSigma2 q = 1 := by
  have hdet := hoefsmitB_sq_eq_one_add_AC hq
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [hoefsmitSigma2, hoefsmitSigma2Inv, Matrix.mul_apply, Fin.sum_univ_two] <;>
      linarith
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [hoefsmitSigma2, hoefsmitSigma2Inv, Matrix.mul_apply, Fin.sum_univ_two] <;>
      linarith

/-- **3-strand Braid relation for the Hoefsmit matrices on `V_(2,1)`:**
    `σ₁ σ₂ σ₁ = σ₂ σ₁ σ₂` for all real `q > 0`. -/
theorem hoefsmit_braid_relation {q : ℝ} (hq : 0 < q) :
    hoefsmitSigma1 q * hoefsmitSigma2 q * hoefsmitSigma1 q =
    hoefsmitSigma2 q * hoefsmitSigma1 q * hoefsmitSigma2 q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero hq
  have hb2 := hoefsmitB_sq q
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [hoefsmitSigma1, hoefsmitSigma2, Matrix.mul_apply, Fin.sum_univ_two]
  · -- (0, 0): q² a = q a² - q⁻¹ b²
    have h : q * hoefsmitA q ^ 2 - q⁻¹ * (hoefsmitB q ^ 2) = q ^ 2 * hoefsmitA q := by
      rw [hb2]
      unfold hoefsmitA
      field_simp
      ring
    linarith
  · -- (0, 1): -b = q a b - q⁻¹ b c
    have h : q * hoefsmitA q - q⁻¹ * hoefsmitC q = -1 := by
      unfold hoefsmitA hoefsmitC
      field_simp
      ring
    have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0
    linear_combination -hoefsmitB q * h - hoefsmitB q * hqq
  · -- (1, 0): -b = q a b - q⁻¹ b c
    have h : q * hoefsmitA q - q⁻¹ * hoefsmitC q = -1 := by
      unfold hoefsmitA hoefsmitC
      field_simp
      ring
    have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0
    linear_combination -hoefsmitB q * h - hoefsmitB q * hqq
  · -- (1, 1): q⁻² c = q b² - q⁻¹ c²
    have h : q * (hoefsmitB q ^ 2) - q⁻¹ * hoefsmitC q ^ 2 = q⁻¹ ^ 2 * hoefsmitC q := by
      rw [hb2]
      unfold hoefsmitC
      field_simp
      ring
    linarith

/-! ## §3. The Figure-Eight Knot Operator `M_{4₁} = (σ₁ σ₂⁻¹)²` on `V_(2,1)` -/

/-- Single crossing block `A(q) = σ₁ σ₂⁻¹` of the figure-eight braid word `(σ₁ σ₂⁻¹)²`. -/
noncomputable def figureEightHalfOp (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  hoefsmitSigma1 q * hoefsmitSigma2Inv q

/-- **The figure-eight knot operator `M_{4₁}(q) = (σ₁ σ₂⁻¹)²` on `V_(2,1)`.** -/
noncomputable def figureEightOp (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  figureEightHalfOp q * figureEightHalfOp q

/-- Determinant of `σ₁`: `det(σ₁) = -1`. -/
theorem det_hoefsmitSigma1 {q : ℝ} (hq : 0 < q) :
    (hoefsmitSigma1 q).det = -1 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  simp [hoefsmitSigma1, Matrix.det_fin_two]
  field_simp

/-- Determinant of `σ₂`: `det(σ₂) = -1`. -/
theorem det_hoefsmitSigma2 {q : ℝ} (hq : 0 < q) :
    (hoefsmitSigma2 q).det = -1 := by
  have hdet := hoefsmitA_mul_C_sub_B_sq hq
  simp [hoefsmitSigma2, Matrix.det_fin_two]
  linarith

/-- Determinant of `σ₂⁻¹`: `det(σ₂⁻¹) = -1`. -/
theorem det_hoefsmitSigma2Inv {q : ℝ} (hq : 0 < q) :
    (hoefsmitSigma2Inv q).det = -1 := by
  have hdet := hoefsmitA_mul_C_sub_B_sq hq
  simp [hoefsmitSigma2Inv, Matrix.det_fin_two]
  linarith

/-- Determinant of `A(q) = σ₁ σ₂⁻¹`: `det(σ₁ σ₂⁻¹) = 1`. -/
theorem det_figureEightHalfOp {q : ℝ} (hq : 0 < q) :
    (figureEightHalfOp q).det = 1 := by
  unfold figureEightHalfOp
  rw [Matrix.det_mul, det_hoefsmitSigma1 hq, det_hoefsmitSigma2Inv hq]
  ring

/-- **Determinant of the figure-eight knot operator:** `det(M_{4₁}(q)) = 1` for all `q > 0`. -/
theorem det_figureEightOp {q : ℝ} (hq : 0 < q) :
    (figureEightOp q).det = 1 := by
  unfold figureEightOp
  rw [Matrix.det_mul, det_figureEightHalfOp hq]
  ring

/-- The legacy arithmetic identity `(-1)⁴ = 1`. -/
theorem figure_eight_det_one : (-1 : ℝ)^4 = 1 := by norm_num

/-- Trace of the half-word `A(q) = σ₁ σ₂⁻¹`: `tr(σ₁ σ₂⁻¹) = 1 - q² - q⁻²`. -/
theorem trace_figureEightHalfOp {q : ℝ} (hq : 0 < q) :
    (figureEightHalfOp q).trace = 1 - q ^ 2 - q⁻¹ ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero hq
  simp [figureEightHalfOp, hoefsmitSigma1, hoefsmitSigma2Inv,
    Matrix.trace, Fin.sum_univ_two, hoefsmitA, hoefsmitC]
  field_simp
  ring

/-- Closed-form trace of `M_{4₁} = (σ₁σ₂⁻¹)²` on `V_(2,1)` as a Laurent polynomial in `q`. -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
noncomputable def figureEightTrace (q : ℝ) : ℝ :=
  q ^ 4 - 2 * q ^ 2 + 1 - 2 * q ^ (-2 : ℤ) + q ^ (-4 : ℤ)

/-- **Exact Trace Theorem:** The matrix trace `(figureEightOp q).trace` of
    `M_{4₁}(q) = (σ₁ σ₂⁻¹)²` on `V_(2,1)` equals `figureEightTrace q = q⁴ - 2q² + 1 - 2q⁻² + q⁻⁴`
    for every `q > 0`. -/
theorem trace_figureEightOp_eq {q : ℝ} (hq : 0 < q) :
    (figureEightOp q).trace = figureEightTrace q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero hq
  have hb2 := hoefsmitB_sq q
  -- By 2×2 Cayley-Hamilton, tr(A²) = tr(A)² - 2 det(A)
  have hCH : (figureEightOp q).trace =
      (figureEightHalfOp q).trace ^ 2 - 2 * (figureEightHalfOp q).det := by
    simp [figureEightOp, Matrix.trace, Matrix.det_fin_two, Fin.sum_univ_two, Matrix.mul_apply]
    ring
  rw [hCH, trace_figureEightHalfOp hq, det_figureEightHalfOp hq, figureEightTrace]
  have hz2 : q ^ (-2 : ℤ) = q⁻¹ ^ 2 := by
    change (q ^ (2 : ℕ))⁻¹ = q⁻¹ ^ 2
    rw [inv_pow]
  have hz4 : q ^ (-4 : ℤ) = q⁻¹ ^ 4 := by
    change (q ^ (4 : ℕ))⁻¹ = q⁻¹ ^ 4
    rw [inv_pow]
  rw [hz2, hz4]
  field_simp
  ring

/-- **Classical trace value:** `tr M_{4₁}|_{q=1} = -1`. -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_one : figureEightTrace 1 = -1 := by
  simp only [figureEightTrace, one_pow, one_zpow]; norm_num

/-- **`tr M + 2` is a perfect square:** `tr M_{4₁}(q) + 2 = (q² - 1 + q⁻²)²`. -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_add_two {q : ℝ} (hq : q ≠ 0) :
    figureEightTrace q + 2 = (q ^ 2 - 1 + q ^ (-2 : ℤ)) ^ 2 := by
  rw [figureEightTrace]; field_simp; ring

/-- Strict lower bound `tr M_{4₁}(q) > -2` for all real `q ≠ 0`:
    since `q² - 1 + q⁻² = ((q² - 1/2)² + 3/4) / q² > 0`, the square never vanishes on `ℝ`. -/
theorem figureEightTrace_gt_neg_two {q : ℝ} (hq : q ≠ 0) :
    -2 < figureEightTrace q := by
  have hsq := figureEightTrace_add_two hq
  have hbase : 0 < q ^ 2 - 1 + q ^ (-2 : ℤ) := by
    have hz2 : q ^ (-2 : ℤ) = (q ^ 2)⁻¹ := by rfl
    rw [hz2]
    have hq2 : 0 < q ^ 2 := sq_pos_of_ne_zero hq
    have hnum : 0 < (q ^ 2 - 1 / 2) ^ 2 + 3 / 4 := by positivity
    have hid : q ^ 2 - 1 + (q ^ 2)⁻¹ = ((q ^ 2 - 1 / 2) ^ 2 + 3 / 4) / q ^ 2 := by
      field_simp; ring
    rw [hid]
    exact div_pos hnum hq2
  have hsq_pos : 0 < (q ^ 2 - 1 + q ^ (-2 : ℤ)) ^ 2 := sq_pos_of_pos hbase
  linarith

/-- `tr M_{4₁}(q) ≥ -2` on the real axis. -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_ge_neg_two {q : ℝ} (hq : q ≠ 0) :
    -2 ≤ figureEightTrace q :=
  le_of_lt (figureEightTrace_gt_neg_two hq)

/-- **`tr M - 2` factors into the two golden factors and the two cyclotomic factors.** -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_sub_two_factored {q : ℝ} (hq : q ≠ 0) :
    figureEightTrace q - 2 =
      (q ^ 2 - q - 1) * ((q ^ 2 + q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1))
        / q ^ 4 := by
  rw [figureEightTrace]; field_simp; ring

/-- **`θ = 0` at the golden ratio:** if `q² = q + 1`, then `tr M_{4₁}(q) = 2`. -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_golden {q : ℝ} (h : q ^ 2 = q + 1) (hq : q ≠ 0) :
    figureEightTrace q = 2 := by
  have hz : q ^ 2 - q - 1 = 0 := by rw [h]; ring
  have hfac := figureEightTrace_sub_two_factored hq
  rw [hz, zero_mul, zero_div] at hfac
  linarith

/-! ## §4. Sign Analysis of `tr(M_{4₁}) - 2` Across the Three Golden Regimes -/

theorem cyclotomic_factors_pos (q : ℝ) :
    0 < (q ^ 2 - q + 1) * (q ^ 2 + q + 1) := by
  have h1 : 0 < q ^ 2 - q + 1 := by
    have : q ^ 2 - q + 1 = (q - 1 / 2) ^ 2 + 3 / 4 := by ring
    rw [this]; positivity
  have h2 : 0 < q ^ 2 + q + 1 := by
    have : q ^ 2 + q + 1 = (q + 1 / 2) ^ 2 + 3 / 4 := by ring
    rw [this]; positivity
  exact mul_pos h1 h2

/-- **Regime 1 (Interior of the golden interval `φ⁻¹ < q < φ`):**
    `(figureEightOp q).trace` satisfies `|(figureEightOp q).trace| < 2`
    (equivalently `(figureEightOp q).trace ^ 2 < 4`). -/
theorem figureEightOp_trace_lt_two_of_golden_interval {q : ℝ}
    (hq_low : goldenPhi⁻¹ < q) (hq_high : q < goldenPhi) :
    |(figureEightOp q).trace| < 2 := by
  have hq : 0 < q := lt_trans goldenPhi_inv_pos hq_low
  have hq0 : q ≠ 0 := ne_of_gt hq
  rw [trace_figureEightOp_eq hq, abs_lt]
  refine ⟨figureEightTrace_gt_neg_two hq0, ?_⟩
  have hfac := figureEightTrace_sub_two_factored hq0
  have hf1 : q ^ 2 - q - 1 < 0 := by
    rw [quad_sub_q_sub_one_factor]
    exact mul_neg_of_neg_of_pos (sub_neg.mpr hq_high) (add_pos hq goldenPhi_inv_pos)
  have hf2 : 0 < q ^ 2 + q - 1 := by
    rw [quad_add_q_sub_one_factor]
    exact mul_pos (sub_pos.mpr hq_low) (add_pos hq goldenPhi_pos)
  have hcyc := cyclotomic_factors_pos q
  have hpos_right : 0 < (q ^ 2 + q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) := by
    have : (q ^ 2 + q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) =
        (q ^ 2 + q - 1) * ((q ^ 2 - q + 1) * (q ^ 2 + q + 1)) := by ring
    rw [this]
    exact mul_pos hf2 hcyc
  have hnum_neg :
      (q ^ 2 - q - 1) * ((q ^ 2 + q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1)) < 0 :=
    mul_neg_of_neg_of_pos hf1 hpos_right
  have hq4 : 0 < q ^ 4 := by positivity
  have hdiv_neg := div_neg_of_neg_of_pos hnum_neg hq4
  linarith

/-- **Regime 2 (Golden endpoints `q = φ⁻¹` or `q = φ`):**
    `(figureEightOp q).trace = 2`. -/
theorem figureEightOp_trace_eq_two_of_golden_endpoint {q : ℝ}
    (h : q = goldenPhi⁻¹ ∨ q = goldenPhi) :
    (figureEightOp q).trace = 2 := by
  have hq : 0 < q := by
    rcases h with rfl | rfl
    · exact goldenPhi_inv_pos
    · exact goldenPhi_pos
  have hq0 : q ≠ 0 := ne_of_gt hq
  rw [trace_figureEightOp_eq hq]
  have hfac := figureEightTrace_sub_two_factored hq0
  rcases h with rfl | rfl
  · have hf2 : (goldenPhi⁻¹) ^ 2 + goldenPhi⁻¹ - 1 = 0 := by
      rw [quad_add_q_sub_one_factor, sub_self, zero_mul]
    rw [hf2, zero_mul, zero_mul, mul_zero, zero_div] at hfac
    linarith
  · have hf1 : goldenPhi ^ 2 - goldenPhi - 1 = 0 := by
      rw [quad_sub_q_sub_one_factor, sub_self, zero_mul]
    rw [hf1, zero_mul, zero_div] at hfac
    linarith

/-- **Regime 3 (Exterior `0 < q < φ⁻¹` or `q > φ`):**
    `2 < (figureEightOp q).trace`. -/
theorem figureEightOp_trace_gt_two_of_exterior {q : ℝ}
    (h : (0 < q ∧ q < goldenPhi⁻¹) ∨ goldenPhi < q) :
    2 < (figureEightOp q).trace := by
  have hq : 0 < q := by
    rcases h with ⟨hq0, _⟩ | hq_hi
    · exact hq0
    · exact lt_trans goldenPhi_pos hq_hi
  have hq0 : q ≠ 0 := ne_of_gt hq
  rw [trace_figureEightOp_eq hq]
  have hfac := figureEightTrace_sub_two_factored hq0
  have hcyc := cyclotomic_factors_pos q
  have hprod_pos : 0 < (q ^ 2 - q - 1) * (q ^ 2 + q - 1) := by
    rcases h with ⟨_, hlt⟩ | hgt
    · have hf1 : q ^ 2 - q - 1 < 0 := by
        rw [quad_sub_q_sub_one_factor]
        exact mul_neg_of_neg_of_pos
          (sub_neg.mpr (lt_trans hlt goldenPhi_inv_lt_goldenPhi))
          (add_pos hq goldenPhi_inv_pos)
      have hf2 : q ^ 2 + q - 1 < 0 := by
        rw [quad_add_q_sub_one_factor]
        exact mul_neg_of_neg_of_pos (sub_neg.mpr hlt) (add_pos hq goldenPhi_pos)
      exact mul_pos_of_neg_of_neg hf1 hf2
    · have hf1 : 0 < q ^ 2 - q - 1 := by
        rw [quad_sub_q_sub_one_factor]
        exact mul_pos (sub_pos.mpr hgt) (add_pos hq goldenPhi_inv_pos)
      have hf2 : 0 < q ^ 2 + q - 1 := by
        rw [quad_add_q_sub_one_factor]
        exact mul_pos
          (sub_pos.mpr (lt_trans goldenPhi_inv_lt_goldenPhi hgt))
          (add_pos hq goldenPhi_pos)
      exact mul_pos hf1 hf2
  have hnum_pos :
      0 < (q ^ 2 - q - 1) * ((q ^ 2 + q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1)) := by
    have : (q ^ 2 - q - 1) * ((q ^ 2 + q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1)) =
        ((q ^ 2 - q - 1) * (q ^ 2 + q - 1)) * ((q ^ 2 - q + 1) * (q ^ 2 + q + 1)) := by ring
    rw [this]
    exact mul_pos hprod_pos hcyc
  have hq4 : 0 < q ^ 4 := by positivity
  have hdiv_pos := div_pos hnum_pos hq4
  linarith

/-! ## §5. Characteristic Equation of `figureEightOp q` & Complete Golden Trichotomy -/

/-- A complex number `λ ∈ ℂ` is an eigenvalue (characteristic root) of a real `2 × 2` matrix `M`
    when `λ² - tr(M) λ + det(M) = 0`. -/
def IsCharRoot2x2 (M : Matrix (Fin 2) (Fin 2) ℝ) (lam : ℂ) : Prop :=
  lam ^ 2 - (M.trace : ℂ) * lam + (M.det : ℂ) = 0

/-- For `M_{4₁}(q)` (`q > 0`), `IsCharRoot2x2 (figureEightOp q) lam` reduces to
    `lam² - ((figureEightOp q).trace : ℂ) * lam + 1 = 0`. -/
theorem isCharRoot_figureEightOp_iff {q : ℝ} (hq : 0 < q) (lam : ℂ) :
    IsCharRoot2x2 (figureEightOp q) lam ↔
      lam ^ 2 - ((figureEightOp q).trace : ℂ) * lam + 1 = 0 := by
  unfold IsCharRoot2x2
  rw [det_figureEightOp hq, Complex.ofReal_one]

/-- **Legacy signature preserved:** Any root of `λ² - t λ + 1 = 0` with `t² < 4` has `‖λ‖ = 1`. -/
-- Ref: [jones1987] Jones, Hecke algebra representations of braid groups (1987)
-- Ref: [kashaev1997]
theorem figure_eight_unitary_on_standard
    (t : ℝ) (ht : t ^ 2 < 4) (lam : ℂ)
    (hroot : lam ^ 2 - (t : ℂ) * lam + 1 = 0) :
    ‖lam‖ = 1 :=
  unit_modulus_of_det_one_small_trace t ht lam hroot

/-- **Complete Three-Regime Golden Trichotomy for the Figure-Eight Knot Operator `M_{4₁}(q)`
    on `V_(2,1)` (`prop:figure-eight-reeb-rotation`):**

    1. **Golden interval (`φ⁻¹ < q < φ`):** every eigenvalue `λ` of `figureEightOp q`
       has unit modulus `‖λ‖ = 1` (with `|(figureEightOp q).trace| < 2`).
    2. **Golden endpoints (`q = φ⁻¹` or `q = φ`):** `(figureEightOp q).trace = 2` and
       every eigenvalue `λ` of `figureEightOp q` equals `1`.
    3. **Exterior (`0 < q < φ⁻¹` or `q > φ`):** `2 < (figureEightOp q).trace`, and every
       eigenvalue `λ` of `figureEightOp q` is strictly real (`λ.im = 0`) and not of unit
       modulus (`‖λ‖ ≠ 1`). -/
theorem figure_eight_golden_trichotomy :
    (-- (1) Interior: φ⁻¹ < q < φ ⇒ |tr(M_{4₁})| < 2 and ‖λ‖ = 1
     ∀ (q : ℝ), goldenPhi⁻¹ < q → q < goldenPhi →
       |(figureEightOp q).trace| < 2 ∧
       ∀ (lam : ℂ), IsCharRoot2x2 (figureEightOp q) lam → ‖lam‖ = 1) ∧
    (-- (2) Endpoints: q ∈ {φ⁻¹, φ} ⇒ tr(M_{4₁}) = 2 and λ = 1
     ∀ (q : ℝ), (q = goldenPhi⁻¹ ∨ q = goldenPhi) →
       (figureEightOp q).trace = 2 ∧
       ∀ (lam : ℂ), IsCharRoot2x2 (figureEightOp q) lam → lam = 1) ∧
    (-- (3) Exterior: (0 < q < φ⁻¹ ∨ φ < q) ⇒ tr(M_{4₁}) > 2, λ.im = 0, and ‖λ‖ ≠ 1
     ∀ (q : ℝ), ((0 < q ∧ q < goldenPhi⁻¹) ∨ goldenPhi < q) →
       2 < (figureEightOp q).trace ∧
       ∀ (lam : ℂ), IsCharRoot2x2 (figureEightOp q) lam →
         lam.im = 0 ∧ ‖lam‖ ≠ 1) := by
  refine ⟨?_, ?_, ?_⟩
  · -- (1) Golden interval
    intro q hlow hhigh
    have hq : 0 < q := lt_trans goldenPhi_inv_pos hlow
    have htr : |(figureEightOp q).trace| < 2 :=
      figureEightOp_trace_lt_two_of_golden_interval hlow hhigh
    refine ⟨htr, ?_⟩
    intro lam hroot
    rw [isCharRoot_figureEightOp_iff hq] at hroot
    have hsq : (figureEightOp q).trace ^ 2 < 4 := by
      have : |(figureEightOp q).trace| ^ 2 < (2 : ℝ) ^ 2 :=
        sq_lt_sq.mpr (by simpa [abs_of_pos (by norm_num : (0 : ℝ) < 2)] using htr)
      rw [sq_abs] at this
      linarith
    exact figure_eight_unitary_on_standard (figureEightOp q).trace hsq lam hroot
  · -- (2) Golden endpoints
    intro q hend
    have hq : 0 < q := by
      rcases hend with rfl | rfl
      · exact goldenPhi_inv_pos
      · exact goldenPhi_pos
    have htr : (figureEightOp q).trace = 2 :=
      figureEightOp_trace_eq_two_of_golden_endpoint hend
    refine ⟨htr, ?_⟩
    intro lam hroot
    rw [isCharRoot_figureEightOp_iff hq, htr] at hroot
    have hsq : (lam - 1) ^ 2 = 0 := by
      calc (lam - 1) ^ 2 = lam ^ 2 - ((2 : ℝ) : ℂ) * lam + 1 := by push_cast; ring
        _ = 0 := hroot
    exact sub_eq_zero.mp (sq_eq_zero_iff.mp hsq)
  · -- (3) Exterior
    intro q hext
    have hq : 0 < q := by
      rcases hext with ⟨hq0, _⟩ | hq_hi
      · exact hq0
      · exact lt_trans goldenPhi_pos hq_hi
    have htr : 2 < (figureEightOp q).trace :=
      figureEightOp_trace_gt_two_of_exterior hext
    refine ⟨htr, ?_⟩
    intro lam hroot
    rw [isCharRoot_figureEightOp_iff hq] at hroot
    set t := (figureEightOp q).trace
    set a := lam.re
    set b := lam.im
    rw [Complex.ext_iff] at hroot
    obtain ⟨hr, hi⟩ := hroot
    simp only [pow_two, Complex.add_re, Complex.sub_re, Complex.mul_re,
      Complex.one_re, Complex.zero_re, Complex.ofReal_re, Complex.ofReal_im,
      Complex.mul_im, Complex.add_im, Complex.sub_im, Complex.one_im,
      Complex.zero_im] at hr hi
    have hre : a ^ 2 - b ^ 2 - t * a + 1 = 0 := by linear_combination hr
    have him : b * (2 * a - t) = 0 := by linear_combination hi
    -- Show b = 0: if 2a = t, then a² + b² = 1, so a² ≤ 1, contradicting 4a² = t² > 4.
    have hb0 : b = 0 := by
      rcases mul_eq_zero.mp him with hb | ha
      · exact hb
      · exfalso
        have hb2 : b ^ 2 = 1 - a ^ 2 := by linear_combination -hre + a * ha
        have ha2_le : a ^ 2 ≤ 1 := by nlinarith [sq_nonneg b, hb2]
        have ht2_gt : 4 < t ^ 2 := by nlinarith [htr]
        have h4a2 : 4 * a ^ 2 = t ^ 2 := by
          have : 2 * a = t := by linarith
          nlinarith
        linarith
    refine ⟨hb0, ?_⟩
    intro hnorm
    have hns : Complex.normSq lam = 1 := by
      have h1 : ‖lam‖ ^ 2 = 1 := by rw [hnorm]; norm_num
      rw [← Complex.sq_norm]; exact h1
    have ha2 : a ^ 2 = 1 := by
      have hsq : Complex.normSq lam = a ^ 2 + b ^ 2 := by
        rw [Complex.normSq_apply]; ring
      nlinarith [hns, hsq, hb0]
    -- Substitute b = 0 and a² = 1 into hre: 2 - t * a = 0, so t * a = 2, hence t² = (t*a)² = 4
    have hta : t * a = 2 := by linear_combination -hre + ha2 - b * hb0
    have ht2 : t ^ 2 = 4 := by
      calc t ^ 2 = t ^ 2 * a ^ 2 := by rw [ha2, mul_one]
        _ = (t * a) ^ 2 := by ring
        _ = 4 := by rw [hta]; norm_num
    nlinarith [htr, ht2]

end QOU.BraidsAndKnots
