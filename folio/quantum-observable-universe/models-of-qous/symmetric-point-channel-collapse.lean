import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Algebra.Group.Invertible.Defs
import Mathlib.Tactic.Ring

namespace QOU

/-- **Channel sum at the symmetric point (division-free core).**  For an
involutive unit (`s² = 1`, the `q = 1` specialisation of the Hecke
relation) in any commutative ring, the inverse coincides with the element
and the unaveraged channel sum is `2s`.  No inverse of `2`, no field:
this is the multiplicative-relation ("R[h]") form of `(s + s⁻¹)/2 = s`
per §7c. -/
-- Ref: [leitner2026] models-of-qous/symmetric-point-channel-collapse.md
theorem symmetric_point_channel_sum {R : Type*} [CommRing R] (s : Rˣ)
    (hs : (s : R) ^ 2 = 1) :
    ((s⁻¹ : Rˣ) : R) = (s : R) ∧
      (s : R) + ((s⁻¹ : Rˣ) : R) = 2 * (s : R) := by
  -- s² = 1 ⇒ s·s = 1 ⇒ s⁻¹ = s⁻¹·(s·s) = (s⁻¹·s)·s = s.
  have hss : (s : R) * (s : R) = 1 := by rw [← pow_two]; exact hs
  have hinv : ((s⁻¹ : Rˣ) : R) = (s : R) := by
    calc ((s⁻¹ : Rˣ) : R)
        = ((s⁻¹ : Rˣ) : R) * ((s : R) * (s : R)) := by rw [hss, mul_one]
      _ = (((s⁻¹ : Rˣ) : R) * (s : R)) * (s : R) := by ring
      _ = (s : R) := by rw [Units.inv_mul, one_mul]
  exact ⟨hinv, by rw [hinv]; ring⟩

/-- **Channel collapse at the symmetric point.**  For an involutive unit
(`s² = 1`) in a commutative ring in which `2` is invertible, the inverse
coincides with the element and the averaged channel `(s + s⁻¹)/2`
collapses onto it.  This is the algebraic core of the `q = 1`
degeneration of the inter-nucleon channel assignments `σ`, `σ⁻¹`,
`(σ + σ⁻¹)/2`.

Base ring (§7c): `[CommRing R]` with `s : Rˣ` and `[Invertible (2 : R)]`
in place of the former `[Field R]` with `s ≠ 0` implicit and `(2 : R) ≠ 0`
— an element with `s² = 1` *is* a unit, and the only division used is by
`2`.  A field of characteristic `≠ 2` is the special case
(`invertibleOfNonzero`); `ℤ[1/2][q^{±1}]` is another. -/
-- Ref: [leitner2026] models-of-qous/symmetric-point-channel-collapse.md
theorem symmetric_point_channel_collapse {R : Type*} [CommRing R]
    [Invertible (2 : R)] (s : Rˣ) (hs : (s : R) ^ 2 = 1) :
    ((s⁻¹ : Rˣ) : R) = (s : R) ∧
      ⅟(2 : R) * ((s : R) + ((s⁻¹ : Rˣ) : R)) = (s : R) := by
  obtain ⟨hinv, hsum⟩ := symmetric_point_channel_sum s hs
  refine ⟨hinv, ?_⟩
  rw [hsum, ← mul_assoc, invOf_mul_self, one_mul]

end QOU
