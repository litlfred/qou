import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination

/-!
# Twisted invariants of linear sections vanish (pure algebra)

The last step of Bloch–Suslin rigidity, after the analytic extension step: a section
`F(z) = a + b z` of `O(1)` on `ℙ¹` that is anti-invariant under inversion with the twist
`z · F(z⁻¹) = -F(z)` and invariant under `z ↦ 1 - z` is zero. Holds over any field with an
element other than `0` and `1`.
-/

namespace QOU.Archimedean.BlochRigidity

theorem linear_section_eq_zero {K : Type*} [Field K] {a b : K}
    (hinv : ∀ z : K, z ≠ 0 → z * (a + b * z⁻¹) = -(a + b * z))
    (hsym : ∀ z : K, a + b * (1 - z) = a + b * z)
    (hK : ∃ z : K, z ≠ 0 ∧ z ≠ 1) : a = 0 ∧ b = 0 := by
  have hb : b = 0 := by have := hsym 0; simpa using this
  subst hb
  obtain ⟨z, hz0, hz1⟩ := hK
  have h1 := hinv 1 one_ne_zero
  have hz := hinv z hz0
  simp only [zero_mul, add_zero, one_mul] at h1 hz
  refine ⟨?_, rfl⟩
  have : (z - 1) * a = 0 := by linear_combination hz - h1
  rcases mul_eq_zero.1 this with h | h
  · exact absurd (sub_eq_zero.1 h) hz1
  · exact h

end QOU.Archimedean.BlochRigidity
