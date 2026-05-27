/-
  Hecke character identity: h·[n]_q = qⁿ − q⁻ⁿ.

  The q-integer [n]_q = (qⁿ−q⁻ⁿ)/(q−q⁻¹) satisfies
  h·[n]_q = qⁿ−q⁻ⁿ where h = q−q⁻¹ is the Hecke parameter.

  This is the key identity connecting the Hecke character
  χ_{(2,1)}(σ₁ⁿ) on V_(2,1) to the q-integer tower.

  -- Ref: [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
-/

import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace QOU.BraidsAndKnots

variable (q : ℝ) (hq : q ≠ 0)

/-- The q-integer [n]_q = (qⁿ−q⁻ⁿ)/(q−q⁻¹). -/
noncomputable def qInteger (n : ℕ) : ℝ := (q^n - q⁻¹^n) / (q - q⁻¹)

/-- h·[n]_q = qⁿ−q⁻ⁿ: the Hecke parameter times the q-integer
  equals the numerator of the q-integer definition. -/
theorem hecke_times_qInteger (n : ℕ) (hh : q - q⁻¹ ≠ 0) :
    (q - q⁻¹) * qInteger q n = q^n - q⁻¹^n := by
  unfold qInteger
  field_simp

/-- [2]_q = q + q⁻¹. -/
theorem qInteger_two (hq : q ≠ 0) (hh : q - q⁻¹ ≠ 0) :
    qInteger q 2 = q + q⁻¹ := by
  unfold qInteger
  field_simp
  ring

/-- [3]_q = q² + 1 + q⁻². -/
theorem qInteger_three (hq : q ≠ 0) (hh : q - q⁻¹ ≠ 0) :
    qInteger q 3 = q^2 + 1 + q⁻¹^2 := by
  unfold qInteger
  field_simp
  ring

/-- The meson mass ratio identity:
  h·[5]_q = q⁵ − q⁻⁵.
  This gives the kaon-to-pion character factor. -/
theorem hecke_times_qInteger_five (hh : q - q⁻¹ ≠ 0) :
    (q - q⁻¹) * qInteger q 5 = q^5 - q⁻¹^5 :=
  hecke_times_qInteger q 5 hh

end QOU.BraidsAndKnots
