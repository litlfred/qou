import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Real.Basic

/-! Is the library's ℝ-valued `speedOfLight` just the generic sibling at `k := ℝ`? -/

namespace Probe

/-- The sibling (generic, division-free, requires invertibility). -/
def speedOfLightGeneric {k : Type*} [Field k] (d : kˣ) : k := (↑d⁻¹ : k)

/-- The library twin, ℝ-valued, division by a possibly-zero quantity. -/
noncomputable def speedOfLightArch (q : ℝ) : ℝ := 1 / (q - 1)

/-- **They agree wherever `q - 1` is invertible** — so the ℝ version is the generic
one instantiated at `k := ℝ`, not an independent definition. -/
theorem arch_is_generic_at_R (q : ℝ) (d : ℝˣ) (hd : (d : ℝ) = q - 1) :
    speedOfLightArch q = speedOfLightGeneric d := by
  unfold speedOfLightArch speedOfLightGeneric
  rw [← hd, one_div, ← Units.val_inv_eq_inv_val]

/-- **And where it is NOT invertible the library version is silently wrong**:
at `q = 1` it returns `0`, because Lean's `1/0 = 0`. The generic version cannot
be formed at all there, which is the stronger statement. -/
theorem arch_is_junk_at_one : speedOfLightArch 1 = 0 := by
  unfold speedOfLightArch
  norm_num

end Probe
