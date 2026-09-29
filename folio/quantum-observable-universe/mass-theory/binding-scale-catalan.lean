import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# Binding Scale from Catalan Constant

α = m_e × Vol(B₃) = m_e × 8G where G is Catalan's constant.

-- Ref: [manuscript] prop:binding-scale-catalan
-/

namespace QOU.BindingScale

/-- Catalan's constant G = Σ (-1)^k / (2k+1)².
    Migrate to `Real.catalan` once it lands in Mathlib. -/
-- Ref: [manuscript] §5/binding-scale-catalan
noncomputable def catalanConstant : ℝ := 0.9159655941772190

/-- Volume of the Borromean rings complement = 8G.
    This is a theorem of hyperbolic geometry:
    the complement decomposes into 2 regular ideal octahedra,
    each of volume 4G. -/
noncomputable def volBorromean : ℝ := 8 * catalanConstant

/-- The binding energy scale connects lepton mass to baryon topology. -/
noncomputable def bindingScale (m_e : ℝ) : ℝ := m_e * volBorromean

/-- At m_e = 0.510999 MeV: α ≈ 3.7445 MeV. -/
theorem bindingScale_value :
    abs (bindingScale 0.510999 - 3.7445) < 0.001 := by
  unfold bindingScale volBorromean catalanConstant
  norm_num

end QOU.BindingScale
