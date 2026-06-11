import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

namespace QOU

/-- **Channel collapse at the symmetric point.**  For an involutive
element (`s ^ 2 = 1`, the `q = 1` specialisation of the Hecke
relation) in a field of characteristic ≠ 2, the inverse coincides
with the element and the averaged channel `(s + s⁻¹)/2` collapses
onto it.  This is the algebraic core of the `q = 1` degeneration of
the inter-nucleon channel assignments `σ`, `σ⁻¹`, `(σ + σ⁻¹)/2`. -/
theorem symmetric_point_channel_collapse {R : Type*} [Field R]
    (s : R) (hs : s ^ 2 = 1) (h2 : (2 : R) ≠ 0) :
    s⁻¹ = s ∧ (s + s⁻¹) / 2 = s := by
  -- Ref: [manuscript] models-of-qous/symmetric-point-channel-collapse.md
  sorry

end QOU
