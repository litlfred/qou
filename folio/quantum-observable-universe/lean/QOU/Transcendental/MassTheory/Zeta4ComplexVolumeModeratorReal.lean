/-
  `Complex.cosh` / `Complex.sinh` form of the `ζ₄` moderator, split out of
  `QOU.MassTheory.Zeta4ComplexVolumeModerator`: the rotation `η ↦ η + iπ/2`
  is the `exp` label of multiplication by `ζ₄` on `G_m`.  Same namespace,
  original names kept.
-/
import QOU.MassTheory.Zeta4ComplexVolumeModerator
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU.Mass.Zeta4ComplexVolumeModerator

/-! ## The smooth moderator — the `ζ₄` rotation `η ↦ η + iπ/2` exchanges cosh ↔ i·sinh -/

/-- **`Re 𝔙 ↦ i·Im-channel`.** The `ζ₄ = i` rotation `η ↦ η + iπ/2` sends `cosh η` to `i·sinh η`:
the bar-even (binding) channel rotates into `i ×` the bar-odd (Q_β) channel — the
`Re 𝔙 ↔ i·Im 𝔙` coupling of the complex volume `𝔙 = Vol + i·CS`. -/
theorem cosh_zeta4_rotation (z : ℂ) :
    Complex.cosh (z + (↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I * Complex.sinh z := by
  rw [Complex.cosh_add]
  have h0 : Complex.cosh ((↑(Real.pi / 2) : ℂ) * Complex.I) = 0 := by
    rw [Complex.cosh_mul_I, ← Complex.ofReal_cos, Real.cos_pi_div_two, Complex.ofReal_zero]
  have h1 : Complex.sinh ((↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I := by
    rw [Complex.sinh_mul_I, ← Complex.ofReal_sin, Real.sin_pi_div_two, Complex.ofReal_one,
      one_mul]
  rw [h0, h1]; ring

/-- **`Im 𝔙 ↦ i·Re-channel`.** The companion: the same rotation sends `sinh η` to `i·cosh η`. -/
theorem sinh_zeta4_rotation (z : ℂ) :
    Complex.sinh (z + (↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I * Complex.cosh z := by
  rw [Complex.sinh_add]
  have h0 : Complex.cosh ((↑(Real.pi / 2) : ℂ) * Complex.I) = 0 := by
    rw [Complex.cosh_mul_I, ← Complex.ofReal_cos, Real.cos_pi_div_two, Complex.ofReal_zero]
  have h1 : Complex.sinh ((↑(Real.pi / 2) : ℂ) * Complex.I) = Complex.I := by
    rw [Complex.sinh_mul_I, ← Complex.ofReal_sin, Real.sin_pi_div_two, Complex.ofReal_one,
      one_mul]
  rw [h0, h1]; ring

/-- Subtracting the rotated hyperbolic sine term from the shifted hyperbolic cosine cancels to zero (`qou-f8rr`). -/
theorem cosh_zeta4_rotation_sub_eq_zero (z : ℂ) :
    Complex.cosh (z + (↑(Real.pi / 2) : ℂ) * Complex.I) - Complex.I * Complex.sinh z = 0 := by
  rw [cosh_zeta4_rotation z, sub_self]

end QOU.Mass.Zeta4ComplexVolumeModerator
