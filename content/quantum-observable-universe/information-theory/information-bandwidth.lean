import Mathlib.Algebra.Field.Basic


/-!
# QOU.Information.informationBandwidth — Information bandwidth per Planck time

The information bandwidth 𝔅(q) := q·η_q / (q - 1)² is the
Bremermann-analog bit budget of the substrate: the maximum number of
distinguishable q-bits one Planck step carries across the light-cone
boundary.  It is the product of the speed of light c_q = 1/(q - 1),
the iteration count n_R(q) = 1/ℏ_q, and the operational entropy η_q.

LaTeX label: `def:information-bandwidth`

## References
- [manuscript] §9/information-bandwidth
-/

namespace QOU.Information

/-- **Information bandwidth** per Planck time at substrate parameter q.

    𝔅(q) := q · η_q / (q - 1)²

    The product of the speed of light c_q = 1/(q - 1), the iteration
    count n_R(q) = 1/ℏ_q, and the operational entropy η_q per fibre. -/
-- Ref: [manuscript] §9/information-bandwidth
noncomputable def informationBandwidth {k : Type*} [Field k]
    (q η : k) : k :=
  q * η / (q - 1) ^ 2

/-- The information bandwidth factors as c_q · n_R · η, with
    c_q = 1/(q - 1) the speed of light and n_R = 1/ℏ_q = q/(q-1). -/
-- Ref: [manuscript] §9/information-bandwidth
theorem informationBandwidth_eq_factored {k : Type*} [Field k]
    (q η : k) (hq0 : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    informationBandwidth q η = (1 / (q - 1)) * (q / (q - 1)) * η := by
  -- Ref: [manuscript] §9/information-bandwidth
  unfold informationBandwidth
  field_simp
  ring

end QOU.Information
