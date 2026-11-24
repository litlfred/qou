import QOU.Nuclear.WeightSpaceNucleon
import BraidKnotOctonion.FibreDimensionForcesTL
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# The weight-space trace of β_Bor and the convention-D Markov trace (owner "1y")

Proves the claims made alongside `WeightSpaceNucleon`, and relates the weight-space trace `T` to
the convention-D Markov trace.

* `chi3_bor`: on the trivial representation (`σ ↦ q`, `σ⁻¹ ↦ q⁻¹`) β_Bor = (σ₀σ₁⁻¹)³ acts as `1`.
  This is the trace on the weight spaces `m = ±3` (`uuu`, `ddd`).
* `hecke_r21a/b`, `braid_r21`: a 2-dimensional representation `ρ₍₂,₁₎` of `H₃(q)`.
* `T_eq_chi3_add_chi21`: `T = χ₍₃₎(β_Bor) + χ₍₂,₁₎(β_Bor)` with `χ₍₃₎(β_Bor) = 1`.
* `T_at_one`: `T = 3` at `q = 1`. `T_pos`: `T > 0` for `1 ≤ q`, `q² ≤ 2`.
* `qtrace_one`, `qtrace_sigma`: the K-weighted sum over all four weight spaces divided by `[2]³`
  is `1` on the identity and `z_D = q²/[2]` on `σ₁`.
* `qtrace_bor_weights`: on β_Bor that sum is `y₃·χ₍₃₎ + y₂₁·χ₍₂,₁₎` with
  `y₃ = 1 − 2/[2]²`, `y₂₁ = 1/[2]²`, `y₁₃ = 0`.
* `qtrace_weights_D_moments`: those weights solve the corpus's Markov moment equations with
  `z = z_D` (normalisation, `σ`, `σ²`).
* `D_moments_force_weights`: any weights solving those equations with `z = z_D` are exactly these
  (via `QOU.BraidsAndKnots.threeRow_eq_zero_of_jones_ocneanu`).

So the convention-D Markov trace of β_Bor is the normalised K-weighted sum of the weight-space traces,
`τ_D(β_Bor) = (q³ + q⁻³ + [2]·T)/[2]³`. No measured value appears here.
-/

namespace QOU.QBeta.WeightSpaceMarkov

open Matrix QOU.QBeta.WeightSpaceNucleon

section Generic

variable {R : Type*} [Field R]

/-- Trivial representation: β_Bor ↦ (q·(q − h))³, which is `1` when `h = q − q⁻¹`. -/
theorem chi3_bor (q : R) (hq : q ≠ 0) : (q * (q - (q - q⁻¹))) ^ 3 = 1 := by
  field_simp; ring

/-- `ρ₍₂,₁₎(σ₀)`. -/
def r21a (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 1; 0, -q⁻¹]
/-- `ρ₍₂,₁₎(σ₁)`. -/
def r21b (q : R) : Matrix (Fin 2) (Fin 2) R := !![-q⁻¹, 0; 1, q]

theorem hecke_r21a (q : R) (hq : q ≠ 0) :
    r21a q * r21a q = (q - q⁻¹) • r21a q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [r21a, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem hecke_r21b (q : R) (hq : q ≠ 0) :
    r21b q * r21b q = (q - q⁻¹) • r21b q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [r21b, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem braid_r21 (q : R) (hq : q ≠ 0) :
    r21a q * r21b q * r21a q = r21b q * r21a q * r21b q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [r21a, r21b, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- `σ₀σ₁⁻¹` in `ρ₍₂,₁₎`, multiplied out (`σ₁⁻¹ = σ₁ − h`). -/
def r21step (q : R) : Matrix (Fin 2) (Fin 2) R := !![1 - q ^ 2, q⁻¹; -q⁻¹, -q⁻¹ ^ 2]

theorem r21step_eq (q : R) (hq : q ≠ 0) :
    r21a q * (r21b q - (q - q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) R)) = r21step q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [r21a, r21b, r21step, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- `T = χ₍₃₎(β_Bor) + χ₍₂,₁₎(β_Bor)`, with `χ₍₃₎(β_Bor) = 1`. -/
theorem T_eq_chi3_add_chi21 (q : R) (hq : q ≠ 0) :
    trace ((sPlus0 q (q - q⁻¹) * (sPlus1 q (q - q⁻¹)
        - (q - q⁻¹) • (1 : Matrix (Fin 3) (Fin 3) R))) ^ 3)
      = 1 + trace ((r21a q * (r21b q - (q - q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) R))) ^ 3) := by
  rw [trace_plus_closed q hq, r21step_eq q hq, pow_three]
  simp only [r21step, Matrix.mul_fin_two, Matrix.trace_fin_two, Matrix.of_apply,
    Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.empty_val',
    Matrix.cons_val_fin_one, Matrix.head_cons, Matrix.head_fin_const]
  field_simp
  ring

/-- Polynomial form of `T`. -/
def Tpoly (q : R) : R := -(q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6

theorem T_at_one : Tpoly (1 : R) = 3 := by unfold Tpoly; norm_num

/-- K-weighted sum over the weight spaces `m = 3, 1, −1, −3`, divided by `[2]³`. -/
def qtrace (q t3 t1 tm1 tm3 : R) : R :=
  (q ^ 3 * t3 + q * t1 + q⁻¹ * tm1 + q⁻¹ ^ 3 * tm3) / (q + q⁻¹) ^ 3

/-- Identity: weight-space dimensions `1, 3, 3, 1`. -/
theorem qtrace_one (q : R) (hq : q ≠ 0) (hs : q + q⁻¹ ≠ 0) : qtrace q 1 3 3 1 = 1 := by
  unfold qtrace
  rw [div_eq_one_iff_eq (pow_ne_zero 3 hs)]
  field_simp
  ring

/-- `σ₁`: traces `q` on `uuu`, `tr sPlus1 = h + q`, `tr sMinus1 = h + q`, `q` on `ddd`. -/
theorem qtrace_sigma (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    qtrace q q (trace (sPlus1 q (q - q⁻¹))) (trace (sMinus1 q (q - q⁻¹))) q
      = q ^ 2 / (q + q⁻¹) := by
  have hs : q + q⁻¹ ≠ 0 := by
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this]; exact div_ne_zero hq2 hq
  simp only [qtrace, sPlus1, sMinus1, Matrix.trace_fin_three, Matrix.of_apply,
    Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_cons, Matrix.head_fin_const,
    Matrix.tail_cons]
  field_simp
  ring

/-- Convention-D weights. -/
def y3 (q : R) : R := 1 - 2 / (q + q⁻¹) ^ 2
def y21 (q : R) : R := 1 / (q + q⁻¹) ^ 2

/-- On β_Bor (traces `1, T, T, 1`): the K-weighted sum is `y₃·1 + y₂₁·(T − 1)`. -/
theorem qtrace_bor_weights (q T : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    qtrace q 1 T T 1 = y3 q * 1 + y21 q * (T - 1) := by
  have e : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  unfold qtrace y3 y21
  rw [e]
  field_simp
  ring

/-- The weights `(y₃, y₂₁, 0)` solve the Markov moment equations at `z = z_D`. -/
theorem qtrace_weights_D_moments (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    y3 q + 2 * y21 q + 0 = 1 ∧
    q * y3 q + (q - q⁻¹) * y21 q + (-q⁻¹) * 0 = q ^ 2 / (q + q⁻¹) ∧
    q ^ 2 * y3 q + (-1) * y21 q + q⁻¹ ^ 2 * 0 = (q ^ 2 / (q + q⁻¹)) ^ 2 := by
  have e : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  unfold y3 y21
  rw [e]
  refine ⟨by field_simp; ring, by field_simp; ring, by field_simp; ring⟩

/-- Any weights solving the moment equations at `z = z_D` are `(y₃, y₂₁, 0)`. -/
theorem D_moments_force_weights (q a b c : R) (hq : q ≠ 0) (hs : q + q⁻¹ ≠ 0)
    (h3 : (q + q⁻¹) ^ 2 - 1 ≠ 0)
    (hnorm : a + 2 * b + c = 1)
    (hsigma : q * a + (q - q⁻¹) * b + (-q⁻¹) * c = q ^ 2 / (q + q⁻¹))
    (hss : q ^ 2 * a + (-1) * b + q⁻¹ ^ 2 * c = (q ^ 2 / (q + q⁻¹)) ^ 2) :
    a = y3 q ∧ b = y21 q ∧ c = 0 := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have hzD : q ^ 2 / (q + q⁻¹) * (q + q⁻¹) = q ^ 2 := div_mul_cancel₀ _ hs
  have hc : c = 0 := QOU.BraidsAndKnots.threeRow_eq_zero_of_jones_ocneanu q q⁻¹
    (q ^ 2 / (q + q⁻¹)) a b c hqi hnorm hsigma hss hzD hs h3
  subst hc
  have hb : b = y21 q := by
    unfold y21
    have h1 : (q + q⁻¹) * b = q - q ^ 2 / (q + q⁻¹) := by linear_combination q * hnorm - hsigma
    have h2 : q - q ^ 2 / (q + q⁻¹) = 1 / (q + q⁻¹) := by
      rw [eq_div_iff hs, sub_mul, div_mul_cancel₀ _ hs]
      linear_combination hqi
    rw [h2] at h1
    rw [eq_div_iff (pow_ne_zero 2 hs)]
    have : (q + q⁻¹) * ((q + q⁻¹) * b) = (q + q⁻¹) * (1 / (q + q⁻¹)) := by rw [h1]
    rw [mul_one_div_cancel hs] at this
    linear_combination this
  refine ⟨?_, hb, rfl⟩
  unfold y3
  rw [hb] at hnorm
  unfold y21 at hnorm
  linear_combination hnorm

end Generic

section Real

/-- `T > 0` for `1 ≤ q` and `q² ≤ 2`. -/
theorem T_pos (q : ℝ) (h1 : 1 ≤ q) (h2 : q ^ 2 ≤ 2) : 0 < Tpoly q := by
  unfold Tpoly
  have hq6 : 0 < q ^ 6 := by positivity
  rw [neg_div, neg_pos, div_neg_iff]
  right
  refine ⟨?_, hq6⟩
  set x := q ^ 2 with hx
  have hx1 : 1 ≤ x := by nlinarith
  have e : q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1
      = x ^ 6 - 3 * x ^ 5 + 3 * x ^ 4 - 5 * x ^ 3 + 3 * x ^ 2 - 3 * x + 1 := by rw [hx]; ring
  rw [e]
  nlinarith [mul_nonneg (sub_nonneg.2 hx1) (sub_nonneg.2 h2), pow_le_pow_left₀ (by linarith) h2 2,
    sq_nonneg (x - 1), sq_nonneg (x ^ 2 - 2), mul_nonneg (by linarith : (0:ℝ) ≤ x) (sub_nonneg.2 hx1)]

end Real

end QOU.QBeta.WeightSpaceMarkov
