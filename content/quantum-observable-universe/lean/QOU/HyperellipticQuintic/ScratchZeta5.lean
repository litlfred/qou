import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Complex

namespace QOU.HyperellipticQuintic

noncomputable def zeta5 : ℂ := Complex.exp (2 * Real.pi * Complex.I / 5)

def HyperellipticQuintic (p : ℂ × ℂ) : Prop :=
  p.2 ^ 2 = p.1 ^ 5 - 1

class Zeta5MonodromyContext where
  X_5 : Type
  tr_M_beta : ℂ
  Phi : ℂ
  residue_eval : ℂ
  DeltaTheta : ℝ
  
  claim_monodromy_phase :
    residue_eval = Phi * tr_M_beta ∧
    Complex.arg residue_eval = DeltaTheta

noncomputable def gauss_sum_5 : ℂ :=
  zeta5^0 + zeta5^1 + zeta5^4 + zeta5^9 + zeta5^16

lemma zeta5_pow_five : zeta5 ^ 5 = 1 := by
  dsimp [zeta5]
  rw [← Complex.exp_nat_mul]
  have h_exp : (5 : ℕ) * (2 * ↑Real.pi * Complex.I / 5) = 2 * ↑Real.pi * Complex.I := by push_cast; ring
  rw [h_exp, Complex.exp_two_pi_mul_I]

lemma zeta5_reductions : zeta5 ^ 9 = zeta5 ^ 4 ∧ zeta5 ^ 16 = zeta5 := by
  have h1 : zeta5 ^ 9 = zeta5 ^ 5 * zeta5 ^ 4 := by ring
  have h2 : zeta5 ^ 16 = (zeta5 ^ 5) ^ 3 * zeta5 := by ring
  rw [h1, h2, zeta5_pow_five]
  constructor <;> ring

lemma gauss_sum_5_reduced : gauss_sum_5 = 1 + 2 * zeta5 + 2 * zeta5^4 := by
  dsimp [gauss_sum_5]
  rw [zeta5_reductions.1, zeta5_reductions.2]
  ring

lemma zeta5_add_inv : zeta5 + zeta5^4 = 2 * (Real.cos (2 * Real.pi / 5) : ℂ) := by
  have h_nz : zeta5 ≠ 0 := by
    intro h
    have h_pow : zeta5 ^ 5 = 0 := by rw [h]; ring
    rw [zeta5_pow_five] at h_pow
    exact one_ne_zero h_pow
  have h_inv : zeta5 ^ 4 = zeta5⁻¹ := by
    calc zeta5 ^ 4 = zeta5 ^ 4 * (zeta5 * zeta5⁻¹) := by rw [mul_inv_cancel₀ h_nz, mul_one]
      _ = (zeta5 ^ 4 * zeta5) * zeta5⁻¹ := by ring
      _ = zeta5 ^ 5 * zeta5⁻¹ := by ring_nf
      _ = 1 * zeta5⁻¹ := by rw [zeta5_pow_five]
      _ = zeta5⁻¹ := by ring
  rw [h_inv, zeta5]
  have h_arg : 2 * Real.pi * Complex.I / 5 = (2 * Real.pi / 5 : ℝ) * Complex.I := by
    push_cast; ring
  rw [h_arg, ← Complex.exp_neg]
  have h_arg_neg : -((2 * Real.pi / 5 : ℝ) * Complex.I) = (-(2 * Real.pi / 5 : ℝ)) * Complex.I := by ring
  rw [h_arg_neg, Complex.exp_mul_I, Complex.exp_mul_I]
  rw [Complex.cos_neg, Complex.sin_neg]
  push_cast
  ring

lemma cos_two_pi_fifths : Real.cos (2 * Real.pi / 5) = (Real.sqrt 5 - 1) / 4 := by
  have h_double : 2 * Real.pi / 5 = 2 * (Real.pi / 5) := by ring
  rw [h_double, Real.cos_two_mul, Real.cos_pi_div_five]
  have : (((1 + Real.sqrt 5) / 4) ^ 2) = (1 + 2 * Real.sqrt 5 + 5) / 16 := by
    calc (((1 + Real.sqrt 5) / 4) ^ 2) = (1 + Real.sqrt 5) ^ 2 / 16 := by ring
      _ = (1 + 2 * Real.sqrt 5 + (Real.sqrt 5) ^ 2) / 16 := by ring
      _ = (1 + 2 * Real.sqrt 5 + 5) / 16 := by rw [Real.sq_sqrt (by positivity)]
  rw [this]
  ring

lemma gauss_sum_5_eval : gauss_sum_5 = (Real.sqrt 5 : ℂ) := by
  rw [gauss_sum_5_reduced]
  have : 1 + 2 * zeta5 + 2 * zeta5 ^ 4 = 1 + 2 * (zeta5 + zeta5 ^ 4) := by ring
  rw [this, zeta5_add_inv, cos_two_pi_fifths]
  push_cast
  ring

lemma gauss_sum_5_abs : norm gauss_sum_5 = Real.sqrt 5 := by
  rw [gauss_sum_5_eval]
  exact Complex.norm_of_nonneg (Real.sqrt_nonneg 5)

theorem zeta5_residue_monodromy_phase [ctx : Zeta5MonodromyContext] :
  ctx.residue_eval = ctx.Phi * ctx.tr_M_beta ∧
  norm gauss_sum_5 = Real.sqrt 5 ∧
  Complex.arg ctx.residue_eval = ctx.DeltaTheta :=
  ⟨ctx.claim_monodromy_phase.1, gauss_sum_5_abs, ctx.claim_monodromy_phase.2⟩

#print axioms gauss_sum_5_abs
#print axioms zeta5_residue_monodromy_phase

end QOU.HyperellipticQuintic
