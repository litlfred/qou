import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.FieldSimp

/-!
# Bloch–Suslin rigidity: the algebraic layer

This file holds the parts of the rigidity argument for the Bloch–Wigner function that
are pure algebra. They are stated over an arbitrary field `F`, with values in an
arbitrary additive group `A`. No topology, order or analysis is used.

The analytic steps live in separate files and are named as separate propositions:

* `Regularity.lean`: a continuous five-term solution is `C^∞`.

## Why the analysis cannot be removed

The hypotheses "inversion-odd, conjugation-odd and five-term" are `ℚ`-linear. Every
additive map from the minus part of the pre-Bloch group `𝒫(ℂ)` to `ℝ` satisfies them,
and `B(ℂ) ⊗ ℚ ≅ K₃^ind(ℂ) ⊗ ℚ` has infinite `ℚ`-rank (Borel, Suslin). So a statement of
the form "every solution is a multiple of `D`" needs some regularity hypothesis, and the
proof must contain an analytic step.
-/

namespace QOU.Archimedean.BlochRigidity

variable {F : Type*} [Field F]

theorem one_sub_inv_ne_zero {x : F} (hx1 : x ≠ 1) : 1 - x⁻¹ ≠ 0 := by
  rw [sub_ne_zero]; intro h; apply hx1; rw [eq_comm, inv_eq_one] at h; exact h

/-- The two "flipped" five-term arguments `(1 - y⁻¹)/(1 - x⁻¹)` and `(1 - y)/(1 - x)` avoid
`0` and `1` whenever `x, y ≠ 1` and `x ≠ y`. -/
theorem flip_args {x y : F} (hx1 : x ≠ 1) (hy1 : y ≠ 1) (hxy : x ≠ y) :
    ((1 - y⁻¹) / (1 - x⁻¹) ≠ 0 ∧ (1 - y⁻¹) / (1 - x⁻¹) ≠ 1) ∧
    ((1 - y) / (1 - x) ≠ 0 ∧ (1 - y) / (1 - x) ≠ 1) := by
  have hx' := one_sub_inv_ne_zero hx1
  have hy' := one_sub_inv_ne_zero hy1
  have hx'' : 1 - x ≠ 0 := sub_ne_zero.2 (Ne.symm hx1)
  have hy'' : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  refine ⟨⟨div_ne_zero hy' hx', ?_⟩, ⟨div_ne_zero hy'' hx'', ?_⟩⟩
  · rw [Ne, div_eq_one_iff_eq hx', sub_right_inj, inv_inj]; exact Ne.symm hxy
  · rw [Ne, div_eq_one_iff_eq hx'', sub_right_inj]; exact Ne.symm hxy

variable {A : Type*} [AddCommGroup A]

/-- **The rearranged five-term relation.** Over any field, with values in any additive
group: if `φ` is inversion-odd on `F ∖ {0,1}` and satisfies Suslin's five-term relation,
then
`φ x = φ y - φ (y/x) - φ ((1 - y⁻¹)/(1 - x⁻¹)) + φ ((1 - y)/(1 - x))`.
The variable `x` now occurs only in denominators. This is the identity the regularity
argument integrates against a bump function in `y`. -/
theorem five_term_rearranged {φ : F → A}
    (hinv : ∀ z : F, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z)
    (h5 : ∀ x y : F, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    {x y : F} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy0 : y ≠ 0) (hy1 : y ≠ 1) (hxy : x ≠ y) :
    φ x = φ y - φ (y / x) - φ ((1 - y⁻¹) / (1 - x⁻¹)) + φ ((1 - y) / (1 - x)) := by
  obtain ⟨⟨ha0, ha1⟩, ⟨hb0, hb1⟩⟩ := flip_args hx1 hy1 hxy
  have e := h5 x y hx0 hx1 hy0 hy1 hxy
  have ea := hinv _ ha0 ha1
  have eb := hinv _ hb0 hb1
  rw [inv_div] at ea eb
  rw [ea, eb] at e
  calc φ x = φ x - (φ x - φ y + φ (y / x) - -φ ((1 - y⁻¹) / (1 - x⁻¹))
        + -φ ((1 - y) / (1 - x))) := by rw [e, sub_zero]
    _ = _ := by abel

end QOU.Archimedean.BlochRigidity
