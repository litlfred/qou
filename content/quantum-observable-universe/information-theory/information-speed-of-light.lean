import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring


/-!
# QOU.Information.speedOfLight — Speed of light as Lieb–Robinson velocity

The speed of light c_q := 1/(q - 1) is the ratio of the spatial coupling
weight to the temporal coupling weight of the q-connection.

LaTeX label: `def:information-speed-of-light`

## References
- [manuscript] §9/information-speed-of-light
-/

namespace QOU.Information

/-- **Speed of light** at substrate parameter q.

    c_q := 1 / (q - 1)

    The ratio of spatial to temporal information transfer within
    a light cone: spatial coupling weight q⁻¹ divided by temporal
    coupling weight ℏ_q = 1 - q⁻¹. -/
-- Ref: [manuscript] §9/information-speed-of-light
noncomputable def speedOfLight {k : Type*} [Field k] (q : k) (hq : q ≠ 1) : k :=
  1 / (q - 1)

/-- The speed of light equals the ratio q⁻¹ / ℏ_q. -/
-- Ref: [manuscript] §9/information-speed-of-light
theorem speedOfLight_eq_ratio {k : Type*} [Field k] (q : k)
    (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    speedOfLight q hq1 = q⁻¹ / (1 - q⁻¹) := by
  -- Ref: [manuscript] §9/information-speed-of-light
  -- 1/(q-1) = q⁻¹ · q/(q-1) = q⁻¹/((q-1)/q) = q⁻¹/(1 - q⁻¹).
  unfold speedOfLight
  have hq_sub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have hsub_inv : 1 - q⁻¹ ≠ 0 := by
    rw [sub_ne_zero]
    intro h
    apply hq_sub
    -- from 1 = q⁻¹ we get q = 1, so q - 1 = 0
    have : q * 1 = q * q⁻¹ := by rw [h]
    rw [mul_one, mul_inv_cancel₀ hq0] at this
    rw [this]; ring
  field_simp [hq0, hq_sub, hsub_inv]

end QOU.Information
