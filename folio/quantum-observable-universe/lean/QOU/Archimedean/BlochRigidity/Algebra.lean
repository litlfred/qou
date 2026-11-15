import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

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

/-- **The two-term relation is algebraic.** Over any field, with values in any additive group:
inversion oddness and the five-term relation give `3 • (φ t + φ (1 - t)) = 0` for `t ≠ 0, 1, 2`
with `t² - t + 1 ≠ 0`. The proof sums the four five-term instances
`(t, (1-t)⁻¹)`, `(t, t/(t-1))`, `(t, (t-1)/t)`, `(1-t, (1-t)⁻¹)`. These instances were found by a
linear-algebra search over five-term instances with Möbius-related arguments. -/
theorem two_term {φ : F → A}
    (hinv : ∀ z : F, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z)
    (h5 : ∀ x y : F, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    {t : F} (ht0 : t ≠ 0) (ht1 : t ≠ 1) (ht2 : t ≠ 2) (ht6 : t ^ 2 - t + 1 ≠ 0) :
    3 • (φ t + φ (1 - t)) = 0 := by
  have a1 : 1 - t ≠ 0 := sub_ne_zero.2 (Ne.symm ht1)
  have a2 : t - 1 ≠ 0 := sub_ne_zero.2 ht1
  have a3 : t - 1 ≠ 1 := fun h => ht2 (by linear_combination h)
  have a4 : t * (1 - t) ≠ 0 := mul_ne_zero ht0 a1
  have a5 : t * (1 - t) ≠ 1 := fun h => ht6 (by linear_combination -h)
  have a6 : (t - 1) ^ 2 ≠ 0 := pow_ne_zero 2 a2
  have a7 : (t - 1) ^ 2 ≠ 1 := fun h => ht2 (by
    have : t * (t - 2) = 0 := by linear_combination h
    rcases mul_eq_zero.1 this with h' | h'
    · exact absurd h' ht0
    · linear_combination h')
  have a8 : (t - 1) / t ≠ 0 := div_ne_zero a2 ht0
  have a9 : (t - 1) / t ≠ 1 := by
    rw [Ne, div_eq_one_iff_eq ht0]; intro h; have : (-1 : F) = 0 := by linear_combination h
    exact one_ne_zero (neg_eq_zero.1 this)
  have b1 : (1 - t)⁻¹ ≠ 0 := inv_ne_zero a1
  have b2 : (1 - t)⁻¹ ≠ 1 := by rw [Ne, inv_eq_one]; intro h; exact ht0 (by linear_combination -h)
  have b3 : ((t - 1) / t)⁻¹ ≠ 0 := inv_ne_zero a8
  have b4 : ((t - 1) / t)⁻¹ ≠ 1 := by rw [Ne, inv_eq_one]; exact a9
  -- the four five-term instances
  have e1 := h5 t (1 - t)⁻¹ ht0 ht1 b1 b2 (by
    intro h; apply a5; field_simp at h; linear_combination h)
  have e2 := h5 t ((t - 1) / t)⁻¹ ht0 ht1 b3 b4 (by
    intro h; apply ht2; field_simp at h; linear_combination h)
  have e3 := h5 t ((t - 1) / t) ht0 ht1 a8 a9 (by
    intro h; apply ht6; field_simp at h; linear_combination h)
  have e4 := h5 (1 - t) (1 - t)⁻¹ a1 (fun h => ht0 (by linear_combination -h)) b1 b2 (by
    intro h; apply a7; field_simp at h; linear_combination h)
  have d1 : 1 - (1 - t)⁻¹ = -t / (1 - t) := by field_simp; ring
  have d2 : 1 - ((t - 1) / t)⁻¹ = -1 / (t - 1) := by rw [inv_div]; field_simp; ring
  have d3 : 1 - (t - 1) / t = 1 / t := by field_simp; ring
  rw [show (1 - t)⁻¹ / t = (t * (1 - t))⁻¹ by field_simp,
    show (1 - t⁻¹) / (1 - ((1 - t)⁻¹)⁻¹) = (t - 1) / t ^ 2 by rw [inv_inv, sub_sub_cancel]; field_simp,
    show (1 - t) / (1 - (1 - t)⁻¹) = -((t - 1) ^ 2 / t) by rw [d1]; field_simp; ring] at e1
  rw [show ((t - 1) / t)⁻¹ / t = (t - 1)⁻¹ by field_simp,
    show (1 - t⁻¹) / (1 - ((t - 1) / t)⁻¹⁻¹) = t - 1 by field_simp; ring,
    show (1 - t) / (1 - ((t - 1) / t)⁻¹) = (t - 1) ^ 2 by field_simp; ring] at e2
  rw [show (t - 1) / t / t = (t - 1) / t ^ 2 by field_simp,
    show (1 - t⁻¹) / (1 - ((t - 1) / t)⁻¹) = -((t - 1) ^ 2 / t) by rw [d2]; field_simp,
    show (1 - t) / (1 - (t - 1) / t) = t * (1 - t) by rw [d3]; field_simp] at e3
  rw [show (1 - t)⁻¹ / (1 - t) = ((t - 1) ^ 2)⁻¹ by field_simp; ring,
    show (1 - (1 - t)⁻¹) / (1 - ((1 - t)⁻¹)⁻¹) = (t - 1)⁻¹ by rw [d1, inv_inv, sub_sub_cancel]; field_simp; ring,
    show (1 - (1 - t)) / (1 - (1 - t)⁻¹) = t - 1 by rw [d1, sub_sub_cancel]; field_simp; ring] at e4
  rw [hinv _ a1 (fun h => ht0 (by linear_combination -h)), hinv _ a4 a5] at e1
  rw [hinv _ a8 a9] at e2
  rw [hinv _ a1 (fun h => ht0 (by linear_combination -h)), hinv _ a6 a7] at e4
  have h := congrArg₂ (· + ·) (congrArg₂ (· + ·) e1 e2) (congrArg₂ (· + ·) e3 e4)
  simp only [add_zero] at h
  rw [← h]
  abel

/-- **The mixed-derivative identity is the cocycle identity (generic field).** Differentiating
the five-term relation once in `y` and once in `x̄` gives a three-term identity in the values
`p, r, s` of the second-derivative coefficient `β` at `a = y/x`, `ab`, `b = (1-x)/(1-y)`. Here `X, Y`
stand for the conjugates of `x, y`. That identity is the nonzero multiple
`x(Y-1) / (y(X-1)(X-Y)(x-y))` of the cocycle identity for `ρ = β·N`, `N(z) = z Z (1-z)(1-Z)`.
Pure field algebra. -/
theorem cocycle_of_mixed {x y X Y p r s : F}
    (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy1 : y ≠ 1) (hxy : x ≠ y)
    (hX0 : X ≠ 0) (hX1 : X ≠ 1) (hY1 : Y ≠ 1) (hXY : X ≠ Y)
    (H : p * (-Y / X ^ 2) * (1 / x)
        - r * (-Y / (X ^ 2 * (1 - Y))) * ((1 - x) / (x * (1 - y) ^ 2))
        + s * (-1 / (1 - Y)) * ((1 - x) / (1 - y) ^ 2) = 0) :
    r * ((y / x * ((1 - x) / (1 - y))) * (Y / X * ((1 - X) / (1 - Y)))
          * (1 - y / x * ((1 - x) / (1 - y))) * (1 - Y / X * ((1 - X) / (1 - Y))))
      = p * ((y / x) * (Y / X) * (1 - y / x) * (1 - Y / X)) * ((1 - X) / (1 - Y))
        + y / x * (s * (((1 - x) / (1 - y)) * ((1 - X) / (1 - Y))
            * (1 - (1 - x) / (1 - y)) * (1 - (1 - X) / (1 - Y)))) := by
  have h1x : 1 - x ≠ 0 := sub_ne_zero.2 (Ne.symm hx1)
  have h1y : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  have h1X : 1 - X ≠ 0 := sub_ne_zero.2 (Ne.symm hX1)
  have h1Y : 1 - Y ≠ 0 := sub_ne_zero.2 (Ne.symm hY1)
  have hY1' : Y - 1 ≠ 0 := sub_ne_zero.2 hY1
  have hxy' : x - y ≠ 0 := sub_ne_zero.2 hxy
  have hXY' : X - Y ≠ 0 := sub_ne_zero.2 hXY
  have key : r * ((y / x * ((1 - x) / (1 - y))) * (Y / X * ((1 - X) / (1 - Y)))
          * (1 - y / x * ((1 - x) / (1 - y))) * (1 - Y / X * ((1 - X) / (1 - Y))))
      - (p * ((y / x) * (Y / X) * (1 - y / x) * (1 - Y / X)) * ((1 - X) / (1 - Y))
        + y / x * (s * (((1 - x) / (1 - y)) * ((1 - X) / (1 - Y))
            * (1 - (1 - x) / (1 - y)) * (1 - (1 - X) / (1 - Y)))))
      = (y * (X - 1) * (X - Y) * (x - y) / (x * (Y - 1))) *
        (p * (-Y / X ^ 2) * (1 / x)
        - r * (-Y / (X ^ 2 * (1 - Y))) * ((1 - x) / (x * (1 - y) ^ 2))
        + s * (-1 / (1 - Y)) * ((1 - x) / (1 - y) ^ 2)) := by
    field_simp
    ring
  rw [H, mul_zero, sub_eq_zero] at key
  exact key

end QOU.Archimedean.BlochRigidity
