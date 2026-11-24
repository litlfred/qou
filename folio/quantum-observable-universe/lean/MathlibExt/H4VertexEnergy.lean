/-
Full four-strand vertex energy in `H₄(q)` (prereg Addendum 18, audit §29).

Three quark strands and one lepton strand, in that tensor order, on the weight-zero space of
`V^{⊗4}` (basis `uudd, udud, uddu, duud, dudu, dduu`, indices 0–5). The Jimbo generators are
written out below and their Hecke and braid relations are proved here.

The Young-channel state weights `W(s) = Σ_λ q^{c(λ)} (P_λ)_{ss}` were computed in exact `ℚ(q)`
arithmetic (sympy, `P_λ` as Lagrange polynomials in the full twist); they are **not** proved in
Lean. Their summed values on the initial and final sets enter below as the definitions
`wInit`, `wFinal`, and the statements here are about those rational functions.

No empirical number enters any statement.
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.QBeta.H4VertexEnergy

open Matrix

section Generic

variable {R : Type*} [Field R]

/-- `Ř` on strands 1,2. `h` stands for `q - q⁻¹`. -/
def s1 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![q, 0, 0, 0, 0, 0; 0, 0, 0, 1, 0, 0; 0, 0, 0, 0, 1, 0;
     0, 1, 0, h, 0, 0; 0, 0, 1, 0, h, 0; 0, 0, 0, 0, 0, q]

/-- `Ř` on strands 2,3. -/
def s2 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![0, 1, 0, 0, 0, 0; 1, h, 0, 0, 0, 0; 0, 0, q, 0, 0, 0;
     0, 0, 0, q, 0, 0; 0, 0, 0, 0, 0, 1; 0, 0, 0, 0, 1, h]

/-- `Ř` on strands 3,4 (the quark–lepton pair of §28). -/
def s3 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![q, 0, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0; 0, 1, h, 0, 0, 0;
     0, 0, 0, 0, 1, 0; 0, 0, 0, 1, h, 0; 0, 0, 0, 0, 0, q]

variable (q h : R) (hH : q ^ 2 = h * q + 1)
include hH

theorem hecke1 : s1 q h * s1 q h = h • s1 q h + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s1, Matrix.mul_apply, Fin.sum_univ_succ] <;>
    first | ring1 | linear_combination hH

theorem hecke2 : s2 q h * s2 q h = h • s2 q h + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s2, Matrix.mul_apply, Fin.sum_univ_succ] <;>
    first | ring1 | linear_combination hH

theorem hecke3 : s3 q h * s3 q h = h • s3 q h + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s3, Matrix.mul_apply, Fin.sum_univ_succ] <;>
    first | ring1 | linear_combination hH

/-- Product matrix `m12` (multiplied out). -/
def m12 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![0, q, 0, 0, 0, 0;
     0, 0, 0, q, 0, 0;
     0, 0, 0, 0, 0, 1;
     1, h, 0, h*q, 0, 0;
     0, 0, q, 0, 0, h;
     0, 0, 0, 0, q, h*q]

/-- Product matrix `m121` (multiplied out). -/
def m121 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![0, 0, 0, q, 0, 0;
     0, q, 0, h*q, 0, 0;
     0, 0, 0, 0, 0, q;
     q, h*q, 0, h^2*q + h, 0, 0;
     0, 0, 0, 0, q, h*q;
     0, 0, q, 0, h*q, h*q^2]

/-- Product matrix `m21` (multiplied out). -/
def m21 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![0, 0, 0, 1, 0, 0;
     q, 0, 0, h, 0, 0;
     0, 0, 0, 0, q, 0;
     0, q, 0, h*q, 0, 0;
     0, 0, 0, 0, 0, q;
     0, 0, 1, 0, h, h*q]

/-- Product matrix `m212` (multiplied out). -/
def m212 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![0, 0, 0, q, 0, 0;
     0, q, 0, h*q, 0, 0;
     0, 0, 0, 0, 0, q;
     q, h*q, 0, h*q^2, 0, 0;
     0, 0, 0, 0, q, h*q;
     0, 0, q, 0, h*q, h^2*q + h]

/-- Product matrix `m23` (multiplied out). -/
def m23 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![0, 0, 1, 0, 0, 0;
     q, 0, h, 0, 0, 0;
     0, q, h*q, 0, 0, 0;
     0, 0, 0, 0, q, 0;
     0, 0, 0, 0, 0, q;
     0, 0, 0, 1, h, h*q]

/-- Product matrix `m232` (multiplied out). -/
def m232 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![0, 0, q, 0, 0, 0;
     0, q, h*q, 0, 0, 0;
     q, h*q, h*q^2, 0, 0, 0;
     0, 0, 0, 0, 0, q;
     0, 0, 0, 0, q, h*q;
     0, 0, 0, q, h*q, h^2*q + h]

/-- Product matrix `m32` (multiplied out). -/
def m32 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![0, q, 0, 0, 0, 0;
     0, 0, q, 0, 0, 0;
     1, h, h*q, 0, 0, 0;
     0, 0, 0, 0, 0, 1;
     0, 0, 0, q, 0, h;
     0, 0, 0, 0, q, h*q]

/-- Product matrix `m323` (multiplied out). -/
def m323 (q h : R) : Matrix (Fin 6) (Fin 6) R :=
  !![0, 0, q, 0, 0, 0;
     0, q, h*q, 0, 0, 0;
     q, h*q, h^2*q + h, 0, 0, 0;
     0, 0, 0, 0, 0, q;
     0, 0, 0, 0, q, h*q;
     0, 0, 0, q, h*q, h*q^2]

omit hH in
theorem mul12 : s1 q h * s2 q h = m12 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s1, s2, m12, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring

omit hH in
theorem mul121 : m12 q h * s1 q h = m121 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [m12, s1, m121, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring

omit hH in
theorem mul21 : s2 q h * s1 q h = m21 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s2, s1, m21, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring

omit hH in
theorem mul212 : m21 q h * s2 q h = m212 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [m21, s2, m212, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring

omit hH in
theorem mul23 : s2 q h * s3 q h = m23 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s2, s3, m23, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring

omit hH in
theorem mul232 : m23 q h * s2 q h = m232 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [m23, s2, m232, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring

omit hH in
theorem mul32 : s3 q h * s2 q h = m32 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s3, s2, m32, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring

omit hH in
theorem mul323 : m32 q h * s3 q h = m323 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [m32, s3, m323, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring

theorem m121_eq_m212 : m121 q h = m212 q h := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [m121, m212] <;>
    first | ring1 | linear_combination hH | linear_combination (-1 : R) * hH | linear_combination h * hH | linear_combination (-h) * hH

theorem m232_eq_m323 : m232 q h = m323 q h := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [m232, m323] <;>
    first | ring1 | linear_combination hH | linear_combination (-1 : R) * hH | linear_combination h * hH | linear_combination (-h) * hH

theorem braid12 : s1 q h * s2 q h * s1 q h = s2 q h * s1 q h * s2 q h := by
  rw [mul12, mul121, mul21, mul212, m121_eq_m212 q h hH]

theorem braid23 : s2 q h * s3 q h * s2 q h = s3 q h * s2 q h * s3 q h := by
  rw [mul23, mul232, mul32, mul323, m232_eq_m323 q h hH]


omit hH in
theorem comm13 : s1 q h * s3 q h = s3 q h * s1 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s1, s3, Matrix.mul_apply, Fin.sum_univ_succ] <;> ring

end Generic

section Real

/-- Summed Young-channel weight of the initial set `{uddu, dudu, dduu}` (lepton `ν`).
Exact `ℚ(q)` computation, not proved here. -/
noncomputable def wInit (q : ℝ) : ℝ :=
  (q ^ 12 + q ^ 10 + 2 * q ^ 8 + 5 * q ^ 4 + q ^ 2 + 2) / ((q ^ 2 + 1) * (q ^ 4 + 1))

/-- Summed Young-channel weight of the final set `{uudd, udud, duud}` (lepton `e`). -/
noncomputable def wFinal (q : ℝ) : ℝ :=
  2 * q ^ 2 * (q ^ 6 + 3 * q ^ 4 + 2) / ((q ^ 2 + 1) * (q ^ 4 + 1))

/-- Claim 1 at the level of the two sets: they sum to `q⁶ + 3q² + 2`, the trace of
`Σ_λ q^{c(λ)} P_λ` over multiplicities `1, 3, 2`. -/
theorem init_add_final (q : ℝ) : wInit q + wFinal q = q ^ 6 + 3 * q ^ 2 + 2 := by
  unfold wInit wFinal
  have : (q ^ 2 + 1) * (q ^ 4 + 1) ≠ 0 := by positivity
  field_simp; ring

/-- The difference factors through `(q² - 1)²`: the split is second order in `h`. -/
theorem init_sub_final (q : ℝ) :
    wInit q - wFinal q =
      (q ^ 2 - 1) ^ 2 * (q ^ 8 + 3 * q ^ 6 + 5 * q ^ 4 + q ^ 2 + 2) /
        ((q ^ 2 + 1) * (q ^ 4 + 1)) := by
  unfold wInit wFinal
  have : (q ^ 2 + 1) * (q ^ 4 + 1) ≠ 0 := by positivity
  field_simp; ring

theorem wFinal_pos (q : ℝ) (hq : 0 < q) : 0 < wFinal q := by unfold wFinal; positivity

/-- The ratio exceeds 1 for `q > 1`, so the du-type → ud-type vertex energy is positive. -/
theorem one_lt_ratio (q : ℝ) (hq : 1 < q) : 1 < wInit q / wFinal q := by
  have hq0 : 0 < q := by linarith
  rw [one_lt_div (wFinal_pos q hq0)]
  have hd := init_sub_final q
  have : 0 < (q ^ 2 - 1) ^ 2 * (q ^ 8 + 3 * q ^ 6 + 5 * q ^ 4 + q ^ 2 + 2) /
      ((q ^ 2 + 1) * (q ^ 4 + 1)) := by
    have : 0 < q ^ 2 - 1 := by nlinarith
    positivity
  linarith

/-- Bound: `ln(W_init/W_final) ≤ W_init/W_final - 1`, and the right side is
`(q² - 1)²(q⁸ + 3q⁶ + 5q⁴ + q² + 2) / (2q²(q⁶ + 3q⁴ + 2))`. -/
theorem log_ratio_le (q : ℝ) (hq : 0 < q) :
    Real.log (wInit q / wFinal q) ≤
      (q ^ 2 - 1) ^ 2 * (q ^ 8 + 3 * q ^ 6 + 5 * q ^ 4 + q ^ 2 + 2) /
        (2 * q ^ 2 * (q ^ 6 + 3 * q ^ 4 + 2)) := by
  have hf := wFinal_pos q hq
  have hpos : 0 < wInit q / wFinal q := by
    have : 0 < wInit q := by unfold wInit; positivity
    positivity
  have h1 := Real.log_le_sub_one_of_pos hpos
  have : wInit q / wFinal q - 1 =
      (q ^ 2 - 1) ^ 2 * (q ^ 8 + 3 * q ^ 6 + 5 * q ^ 4 + q ^ 2 + 2) /
        (2 * q ^ 2 * (q ^ 6 + 3 * q ^ 4 + 2)) := by
    unfold wInit wFinal
    have : (q ^ 2 + 1) * (q ^ 4 + 1) ≠ 0 := by positivity
    have : q ^ 6 + 3 * q ^ 4 + 2 ≠ 0 := by positivity
    field_simp; ring
  linarith

/-- Below the cell on `1 < q`, `q² ≤ 2` (which contains the substrate range):
`ln(W_init/W_final) < 2 ln q`. (It fails for large `q`; the polynomial below changes sign
near `q ≈ 1.579`.) -/
theorem log_ratio_lt_cell (q : ℝ) (hq : 1 < q) (hq2 : q ^ 2 ≤ 2) :
    Real.log (wInit q / wFinal q) < 2 * Real.log q := by
  have hq0 : 0 < q := by linarith
  rw [show 2 * Real.log q = Real.log (q ^ 2) by rw [Real.log_pow]; norm_num]
  have hf := wFinal_pos q hq0
  have hi : 0 < wInit q := by unfold wInit; positivity
  apply Real.log_lt_log (by positivity)
  rw [div_lt_iff₀ hf]
  have hD : 0 < (q ^ 2 + 1) * (q ^ 4 + 1) := by positivity
  have key : q ^ 2 * wFinal q - wInit q =
      (q ^ 2 - 1) * (q ^ 2 + 1) * (-(q ^ 8 - q ^ 6 - 3 * q ^ 4 - q ^ 2 - 2)) /
        ((q ^ 2 + 1) * (q ^ 4 + 1)) := by
    unfold wInit wFinal; field_simp; ring
  have hx1 : 1 < q ^ 2 := by nlinarith
  have hg : 0 < -(q ^ 8 - q ^ 6 - 3 * q ^ 4 - q ^ 2 - 2) := by
    have e8 : q ^ 8 = (q ^ 2) ^ 4 := by ring
    have e6 : q ^ 6 = (q ^ 2) ^ 3 := by ring
    have e4 : q ^ 4 = (q ^ 2) ^ 2 := by ring
    rw [e8, e6, e4]
    set x := q ^ 2
    have hx0 : 0 < x := by linarith
    have h1 : 0 ≤ (2 - x) * x ^ 3 := mul_nonneg (sub_nonneg.mpr hq2) (pow_pos hx0 3).le
    have h2 : 0 ≤ x ^ 2 * (3 - x) := mul_nonneg (sq_nonneg x) (by linarith)
    nlinarith [h1, h2]
  have : 0 < q ^ 2 * wFinal q - wInit q := by
    rw [key]; have : 0 < q ^ 2 - 1 := by linarith
    positivity
  linarith

end Real

end QOU.QBeta.H4VertexEnergy
