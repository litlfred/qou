import QOU.QBeta.ThetaRealityBound

/-!
# QOU.QBeta.AfreeThetaConstraint — the one falsifiable statement the channel carries,
and the shape of candidate that cannot be tested against it

`ThetaRealityBound` showed that the T4 checks are worth less than they read: the
diagonal crossing is an identity in `A`, and reality is a one-sided bound. Read
together with the circularity note that leaves the channel

  `S_K = A · κ · (ln²q₀ − ϑ_K²)`

looking contentless — two anchor equations in three unknowns `(A, ϑ₁, ϑ₂)`.

It is not contentless. **Underdetermined is not contentless.** This file proves
the two facts that matter for the search:

* `afree_invariant` — eliminating `A` between the two anchors leaves
  `(ln²q₀ − ϑ₁²) · S₂ = (ln²q₀ − ϑ₂²) · S₁`, a relation containing **no** `A`
  and **no** `κ`. Any route supplying both `ϑ` values is testable against it
  with nothing inherited from the `A`-conditioned corpus values.
* `A_determined_of_theta` — a route that lands on that relation **determines**
  `A = S/(κ(ln²q₀ − ϑ²))`, rather than importing it from the literature.

and then the negative design result:

* `ratio_attained` — for **every** target ratio `y > 1` there is an explicit,
  admissible `A` realising `ϑ₂² = y · ϑ₁²`, with `ϑ₁² > 0`. Hence a route that
  supplies only the **ratio** of the two `ϑ` is **unfalsifiable**: it cannot
  fail, it can only *name* an `A`. Only a route supplying both `ϑ` values
  **absolutely** over-determines the system and can produce a failing residual.

The counting behind the last point: two equations, three unknowns; one extra
scalar closes the system exactly (no residual), two over-determine it by one.

Nothing here derives `A_ω` or proposes a value of `ϑ`; these are structural
facts about what the channel can and cannot be asked.

-- Ref: [manuscript] docs/scope/2026-08-01-theta-independent-routes.md
-- Ref: [manuscript] docs/scope/2026-08-01-t4-anchor-circularity.md
-/

namespace QOU.QBeta.AfreeThetaConstraint

open QOU.QBeta.ThetaRealityBound

/-- Reading the channel backwards: `ln²q₀ − ϑ² = S/(Aκ)`. -/
theorem lnq_sq_sub_thetaSq (A κ lnq S : ℝ) :
    lnq ^ 2 - thetaSq A κ lnq S = S / (A * κ) := by
  unfold thetaSq; ring

/-- **The `A`-free invariant.** Eliminating `A` (and `κ`) between the two anchor
equations leaves a relation between the two `ϑ` and the two measured `S` alone.

This is the falsifiable content of the channel: a curve in the `(ϑ₁, ϑ₂)` plane
that any independent determination must land on, with no conditioning on `A`. -/
theorem afree_invariant {A κ lnq S₁ S₂ : ℝ} (hA : A ≠ 0) (hκ : κ ≠ 0) :
    (lnq ^ 2 - thetaSq A κ lnq S₁) * S₂
      = (lnq ^ 2 - thetaSq A κ lnq S₂) * S₁ := by
  rw [lnq_sq_sub_thetaSq, lnq_sq_sub_thetaSq]
  field_simp

/-- The same relation in quotient form, when the second leak is nonzero. -/
theorem afree_invariant_div {A κ lnq S₁ S₂ : ℝ} (hA : A ≠ 0) (hκ : κ ≠ 0)
    (hS₂ : S₂ ≠ 0) (h₂ : lnq ^ 2 - thetaSq A κ lnq S₂ ≠ 0) :
    (lnq ^ 2 - thetaSq A κ lnq S₁) / (lnq ^ 2 - thetaSq A κ lnq S₂)
      = S₁ / S₂ := by
  rw [div_eq_div_iff h₂ hS₂]
  exact (afree_invariant hA hκ).trans (mul_comm _ _)

/-- **A route landing on the curve determines `A`.** Given a `ϑ` obtained
independently — not by inverting the channel — the channel returns `A`
rather than consuming it. This is what would make an independent leg a
*determination* of `A_ω` instead of a literature import. -/
theorem A_determined_of_theta {A κ lnq S : ℝ} (hA : A ≠ 0) (hκ : κ ≠ 0)
    (h : lnq ^ 2 - thetaSq A κ lnq S ≠ 0) :
    A = S / (κ * (lnq ^ 2 - thetaSq A κ lnq S)) := by
  rw [lnq_sq_sub_thetaSq] at h ⊢
  have hS : S ≠ 0 := by
    intro hs; apply h; rw [hs]; simp
  field_simp

/-- The channel evaluated at the `A` that realises a prescribed ratio.
Factored out so `ratio_attained` can use it at both leaks. -/
private theorem thetaSq_at_ratio_A {κ lnq S₁ S₂ y : ℝ} (hκ : κ ≠ 0)
    (hden : y * S₁ - S₂ ≠ 0) (S : ℝ) :
    thetaSq ((y * S₁ - S₂) / (κ * lnq ^ 2 * (y - 1))) κ lnq S
      = lnq ^ 2 * (y * S₁ - S₂ - S * (y - 1)) / (y * S₁ - S₂) := by
  unfold thetaSq
  field_simp

/-- **Every ratio is attainable — the unfalsifiability of ratio-shaped
candidates.**

Given a positive leak `S₁ > 0`, a negative leak `S₂ < 0`, and *any* target
ratio `y > 1`, the explicit value

  `A = (y·S₁ − S₂) / (κ · ln²q₀ · (y − 1))`

is positive and satisfies `ϑ₂² = y · ϑ₁²` with `ϑ₁² > 0` — i.e. it is an
admissible point of the family, with both `ϑ` real.

Consequence: a route supplying only the **ratio** `ϑ₂/ϑ₁` can never be
refuted by the channel. Whatever ratio it produces, some `A` realises it
exactly, with zero residual. Such a route does not test `A_ω`; it merely
renames it. A genuine test requires **both** `ϑ` absolutely. -/
theorem ratio_attained {κ lnq S₁ S₂ y : ℝ} (hκ : 0 < κ) (hlnq : 0 < lnq ^ 2)
    (hS₁ : 0 < S₁) (hS₂ : S₂ < 0) (hy : 1 < y) :
    ∃ A : ℝ, 0 < A ∧ 0 < thetaSq A κ lnq S₁ ∧
      thetaSq A κ lnq S₂ = y * thetaSq A κ lnq S₁ := by
  -- the denominator `y·S₁ − S₂` is positive: `y > 1 > 0`, `S₁ > 0`, `S₂ < 0`
  have hden : 0 < y * S₁ - S₂ := by nlinarith
  have hy1 : 0 < y - 1 := by linarith
  have h12 : 0 < S₁ - S₂ := by linarith
  have key := fun S : ℝ =>
    thetaSq_at_ratio_A (κ := κ) (lnq := lnq) (S₁ := S₁) (S₂ := S₂) (y := y)
      (ne_of_gt hκ) (ne_of_gt hden) S
  refine ⟨(y * S₁ - S₂) / (κ * lnq ^ 2 * (y - 1)),
    div_pos hden (mul_pos (mul_pos hκ hlnq) hy1), ?_, ?_⟩
  · -- `ϑ₁² = ln²q₀·(S₁ − S₂)/(y·S₁ − S₂) > 0`
    rw [key S₁, show y * S₁ - S₂ - S₁ * (y - 1) = S₁ - S₂ by ring]
    exact div_pos (mul_pos hlnq h12) hden
  · rw [key S₁, key S₂]
    field_simp
    ring

/-- Restated as the design constraint: the channel places **no** restriction on
the ratio of the two `ϑ`. Every value above 1 occurs. -/
theorem ratio_unconstrained {κ lnq S₁ S₂ : ℝ} (hκ : 0 < κ) (hlnq : 0 < lnq ^ 2)
    (hS₁ : 0 < S₁) (hS₂ : S₂ < 0) :
    ∀ y : ℝ, 1 < y → ∃ A : ℝ, 0 < A ∧ 0 < thetaSq A κ lnq S₁ ∧
      thetaSq A κ lnq S₂ = y * thetaSq A κ lnq S₁ :=
  fun _ hy => ratio_attained hκ hlnq hS₁ hS₂ hy

end QOU.QBeta.AfreeThetaConstraint
