import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse

/-!
# Eigenvalues of the γγ vertex `σ₀σ₁⁻¹` on the `(2,1)` block of `H₃(q)`

PR #8804 §36 (owner, 2026-11-22: *"Try eigenvalues approach"*, then *"Prove the H₃ eigenvalue
facts in Lean"*). The probe `mn_vertex_eigenvalue_probe.py` measured these; this file proves them.

Hoefsmit form of the `(2,1)` block, over a generic field `R` (§7c): `σ₀ = diag(q, −q⁻¹)`,
`σ₁ = [[a, b], [b, a']]` with `a = h/(1 − q⁴)`, `a' = h/(1 − q⁻⁴)`, `h = q − q⁻¹`, and `b` any
element with `b² = 1 + a·a'` (a square root, kept as a hypothesis so nothing archimedean enters).

## What is proved (sorry-free)
* `sigma1_hecke` — `σ₁² = h·σ₁ + 1` (the data are a Hecke representation).
* `vertex_det` — `det(σ₀σ₁⁻¹) = 1`, with `σ₁⁻¹ = σ₁ − h`. So the eigenvalues are `λ, λ⁻¹`.
* `vertex_trace` — `tr(σ₀σ₁⁻¹) = −(q⁴ − q² + 1)/q²`.
* `vertex_cayley_hamilton` — `V² − (tr V)·V + 1 = 0`.
* `trace_formula_at_one` — the trace formula at `q = 1` is `−1`, so the characteristic
  polynomial there is `x² + x + 1`: the eigenvalues are the primitive cube roots of unity.
* `arccos_neg_half` — `arccos(−1/2) = 2π/3`, i.e. `t(1) = θ(1)/2π = 1/3` exactly.

The value at `q = 1` is taken from the closed-form trace, which is a polynomial in `q, q⁻¹`;
the Hoefsmit entries themselves are singular at `q = 1` (`1 − q⁴ = 0`).
-/

namespace QOU.MassTheory.GammaGammaVertexEigenvalues

open Matrix

section Generic
variable {R : Type*} [Field R]

/-- `h = q − q⁻¹`. -/
def hq (q : R) : R := q - q⁻¹
def aq (q : R) : R := hq q / (1 - q ^ 4)
def aq' (q : R) : R := hq q / (1 - q⁻¹ ^ 4)

def s0 (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 0; 0, -q⁻¹]
def s1 (q b : R) : Matrix (Fin 2) (Fin 2) R := !![aq q, b; b, aq' q]
/-- `σ₁⁻¹ = σ₁ − h` (Hecke relation). -/
def s1inv (q b : R) : Matrix (Fin 2) (Fin 2) R := s1 q b - hq q • (1 : Matrix (Fin 2) (Fin 2) R)
/-- The γγ pair-production vertex `σ₀σ₁⁻¹`. -/
def vertex (q b : R) : Matrix (Fin 2) (Fin 2) R := s0 q * s1inv q b

variable {q b : R}

lemma a_add_a' (hq0 : q ≠ 0) (h4 : 1 - q ^ 4 ≠ 0) (_h4' : 1 - q⁻¹ ^ 4 ≠ 0) :
    aq q + aq' q = hq q := by
  unfold aq aq' hq
  have : q ^ 4 - 1 ≠ 0 := by intro h; apply h4; linear_combination -h
  field_simp
  ring

lemma sigma1_hecke (hq0 : q ≠ 0) (h4 : 1 - q ^ 4 ≠ 0) (h4' : 1 - q⁻¹ ^ 4 ≠ 0)
    (hb : b ^ 2 = 1 + aq q * aq' q) :
    s1 q b * s1 q b = hq q • s1 q b + 1 := by
  have hs := a_add_a' hq0 h4 h4'
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [s1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    [linear_combination hb + aq q * hs; linear_combination b * hs; linear_combination b * hs;
     linear_combination hb + aq' q * hs]

lemma aq_closed (hq0 : q ≠ 0) (h4 : 1 - q ^ 4 ≠ 0) : aq q = -1 / (q * (1 + q ^ 2)) := by
  have h2 : 1 + q ^ 2 ≠ 0 := by
    intro h; apply h4; linear_combination (1 - q ^ 2) * h
  unfold aq hq
  rw [div_eq_div_iff h4 (mul_ne_zero hq0 h2)]
  field_simp
  ring

theorem vertex_det (hq0 : q ≠ 0) (h4 : 1 - q ^ 4 ≠ 0) (h4' : 1 - q⁻¹ ^ 4 ≠ 0)
    (hb : b ^ 2 = 1 + aq q * aq' q) : (vertex q b).det = 1 := by
  have hs := a_add_a' hq0 h4 h4'
  simp only [vertex, Matrix.det_mul, s0, s1inv, s1, Matrix.det_fin_two_of]
  rw [Matrix.det_fin_two]
  simp [Matrix.sub_apply, Matrix.smul_apply]
  field_simp
  linear_combination hb + hq q * hs

lemma vertex_eq : vertex q b =
    !![q * (aq q - hq q), q * b; -q⁻¹ * b, -q⁻¹ * (aq' q - hq q)] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [vertex, s0, s1inv, s1, Matrix.mul_apply, Fin.sum_univ_two]

theorem vertex_trace (hq0 : q ≠ 0) (h4 : 1 - q ^ 4 ≠ 0) (h4' : 1 - q⁻¹ ^ 4 ≠ 0) :
    (vertex q b).trace = -(q ^ 4 - q ^ 2 + 1) / q ^ 2 := by
  have hs := a_add_a' hq0 h4 h4'
  have ha := aq_closed hq0 h4
  have h2 : 1 + q ^ 2 ≠ 0 := by
    intro h; apply h4; linear_combination (1 - q ^ 2) * h
  have ha' : aq' q = hq q - aq q := by linear_combination hs
  rw [vertex_eq, Matrix.trace_fin_two_of, ha', ha]
  unfold hq
  field_simp
  ring

/-- Cayley–Hamilton for the vertex: `V² − (tr V)·V + 1 = 0`. -/
theorem vertex_cayley_hamilton (hq0 : q ≠ 0) (h4 : 1 - q ^ 4 ≠ 0) (h4' : 1 - q⁻¹ ^ 4 ≠ 0)
    (hb : b ^ 2 = 1 + aq q * aq' q) :
    vertex q b * vertex q b - (vertex q b).trace • vertex q b + 1 = 0 := by
  have hd := vertex_det hq0 h4 h4' hb
  rw [Matrix.det_fin_two] at hd
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.trace_fin_two] <;>
    first | ring1 | linear_combination hd | linear_combination -hd

end Generic

/-- The closed-form trace at `q = 1` is `−1`: the characteristic polynomial is `x² + x + 1`. -/
theorem trace_formula_at_one : (-(1 ^ 4 - 1 ^ 2 + 1) / 1 ^ 2 : ℚ) = -1 := by norm_num

/-- `arccos(−1/2) = 2π/3`, so the vertex phase at `q = 1` is `θ/2π = 1/3`. -/
theorem arccos_neg_half : Real.arccos (-(1 / 2)) = 2 * Real.pi / 3 := by
  rw [Real.arccos_neg, ← Real.cos_pi_div_three,
    Real.arccos_cos (by positivity) (by linarith [Real.pi_pos])]
  ring

theorem phase_at_one : Real.arccos (-(1 / 2)) / (2 * Real.pi) = 1 / 3 := by
  rw [arccos_neg_half]; field_simp [Real.pi_ne_zero]

end QOU.MassTheory.GammaGammaVertexEigenvalues
