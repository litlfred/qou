import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# The π identities of the B2 lift interface (transcendental boundary)

Split out of `MathlibExt.TauRhoHodgeLiftInterface` under the owner ruling of
2026-11-27 (bean `qou-dk7p`): every transcendental result lives in
`QOU/Transcendental/`. The interface file keeps the algebraic class and its
conditional theorems; the two identities that carry a genuine `Real.pi` live
here.

* `half_a0_eq_inv_8pi` — `½ · (1/(4π)) = 1/(8π)`;
* `gauss_bonnet_bring_eq_inv_8pi` — `|χ|/(4·Area) = 1/(8π)` on Bring
  (`χ = −6`, `Area = 12π`).

Nothing wires `1/(8π)` to production; see the interface file's honesty note.
-/

namespace QOU.Archimedean.TauRhoHodgeLiftInterface

/-- The measure identity with a genuine π: `½ · a₀ = 1/(8π)`. -/
theorem half_a0_eq_inv_8pi :
    (1 / 2 : ℝ) * (1 / (4 * Real.pi)) = 1 / (8 * Real.pi) := by
  have h := Real.pi_ne_zero
  field_simp
  ring

/-- The Gauss–Bonnet placement on Bring (`χ = −6`, `Area = 12π`):
`|χ| / (4·Area) = 1/(8π)` — the merged GB identity's Bring instance, with the
π carried honestly. -/
theorem gauss_bonnet_bring_eq_inv_8pi :
    |(-6 : ℝ)| / (4 * (12 * Real.pi)) = 1 / (8 * Real.pi) := by
  have h := Real.pi_ne_zero
  rw [abs_of_nonpos (by norm_num : (-6 : ℝ) ≤ 0)]
  field_simp
  ring

end QOU.Archimedean.TauRhoHodgeLiftInterface
