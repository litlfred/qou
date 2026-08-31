import Mathlib.Tactic

/-!
# An affine crossing count needs a large negative intercept, and the measured one has none

`QOU.Mass.CountChannelCarrierLocus` reduced `qou-brng`'s remaining question to one test: a carrier
must break `μ_t = 3·μ_p`, where `μ = ½(n₊+n₋)` is the count multiplicity. This file runs that test
against the corpus's **measured** crossing counts and turns the result into a constraint on the
whole affine family.

## The measured model

`QOU.MassTheory.CrossingCountAffine` records, from `level3_em_channel_parity_probe.py` across
**12 nuclei to `A = 39`**,

    n₊ = 5A − 1 + 2Z,    n₋ = 5A − 1 − 2Z,

so the count multiplicity is `μ(A) = ½(n₊+n₋) = 5A − 1` — charge-free, and *exactly* the
multiplicity `QOU.Mass.BrunnianBindingChannel.countChannel` carries. It is not a guess; it is what
the canonical atomic braids measure.

**It passes the acceptance test and then fails on sign.** `μ(3) = 14` and `3·μ(2) = 27`, so the
three-to-one relation is broken and the `b₃ = 0` locus is escaped — but

    b₃/b₂ = μ(3)/μ(2) − 3 = 14/9 − 3 = −13/9 = −1.444…

against a measured `+0.6411239316`. Wrong sign (`measuredModel_b3_neg`).

## The general constraint

For any affine `μ(A) = α·A + β` the cumulant is exact and linear
(`b3_affine_eq`): `b₃ = μ(3) − 3·μ(2) = −(3α + 2β)`. So with a positive two-body binding
`b₂ = μ(2) = 2α + β > 0`,

    b₃ > 0   ⟺   2β < −3α        (`b3_pos_iff_of_b2_pos`)

and combining the two, the intercept is pinned to a window
(`b3_pos_forces_intercept_window`):

    −2α < β < −³⁄₂ α.

**The measured model sits far outside it**: `β/α = −1/5 = −0.2`, where the window is
`(−2, −1.5)` and the value reproducing the measured `b₃/b₂` is `−1.6214` — off by a factor
**8.11**. The gap is not in the *form* of the derived model, which is affine and could work; it is
in one ratio, and the required value is known to six figures.

## Why this is worth stating as a window rather than a miss

The intercept must be **large and negative** — of order `−1.6·α`, comparable to twice the slope.
An affine count with a small intercept (`β = −1` against `α = 5`) cannot produce a positive
three-body cumulant *whatever* the slope, because `b₃/b₂` depends on `β/α` alone
(`b3_ratio_depends_only_on_intercept_ratio`). So the search is one-dimensional, and the target is
a number rather than a shape.

## Scope

Scope-**(a)** on the conjunction {affine count multiplicity, the measured `5A − 1`}. It excludes
neither the count channel nor affine models in general — `window_is_inhabited` exhibits an affine
model with `b₃ > 0`. What is measured is that the corpus's own crossing counts miss the required
intercept ratio by 8.11×.

Ground ring: generic `{R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]` where an
ordering is needed (§7c); the exact identities are ring-only.

Beans `qou-brng`, `qou-6vu3`.
-/

namespace QOU.Mass.AffineCountMultiplicityWindow

variable {R : Type*} [Field R]

/-- An affine count multiplicity `μ(A) = α·A + β`. -/
def mu (α β A : R) : R := α * A + β

/-- The two-body binding in count-multiplicity units: `b₂ = μ(2)`. -/
def b2 (α β : R) : R := mu α β 2

/-- The connected three-body cumulant: `b₃ = μ(3) − 3·μ(2)`. -/
def b3 (α β : R) : R := mu α β 3 - 3 * mu α β 2

/-- **The cumulant of an affine multiplicity is exact and linear**: `b₃ = −(3α + 2β)`. The `A`
dependence cancels entirely — only the slope and intercept survive. -/
theorem b3_affine_eq (α β : R) : b3 α β = -(3 * α + 2 * β) := by
  unfold b3 mu; ring

/-- `b₂ = 2α + β`. -/
theorem b2_eq (α β : R) : b2 α β = 2 * α + β := by
  unfold b2 mu; ring

/-- **The measured model's cumulant is `−13`.** With `μ(A) = 5A − 1`
(`QOU.MassTheory.CrossingCountAffine`, 12 nuclei to `A = 39`), `b₃ = −(15 − 2) = −13`. -/
theorem measuredModel_b3 : b3 (5 : R) (-1) = -13 := by
  rw [b3_affine_eq]; ring

/-- **And its two-body value is `9`**, so `b₃/b₂ = −13/9`, against a measured `+0.6411239316`. -/
theorem measuredModel_b2 : b2 (5 : R) (-1) = 9 := by
  rw [b2_eq]; ring

/-- **The measured model breaks the degenerate locus** — `μ(3) = 14 ≠ 27 = 3·μ(2)` — so it passes
`CountChannelCarrierLocus.carrier_must_break_three_to_one`. The failure below is a sign failure,
not the pair-local degeneracy. -/
theorem measuredModel_breaks_three_to_one :
    mu (5 : ℚ) (-1) 3 ≠ 3 * mu (5 : ℚ) (-1) 2 := by
  unfold mu; norm_num

/-- **The ratio depends only on the intercept-to-slope ratio.** Writing `β = r·α` with `α ≠ 0`,
`b₃/b₂ = −(3 + 2r)/(2 + r)` — the slope cancels. So the search for a carrier reproducing `b₃` is
one-dimensional. -/
theorem b3_ratio_depends_only_on_intercept_ratio {α r : R} (hα : α ≠ 0)
    (hb : 2 + r ≠ 0) :
    b3 α (r * α) / b2 α (r * α) = -(3 + 2 * r) / (2 + r) := by
  rw [b3_affine_eq, b2_eq]
  field_simp

/-! ### The window, over an ordered field -/

section Ordered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **A positive three-body cumulant is exactly a bound on the intercept**: `b₃ > 0` iff
`2β < −3α`, with no further hypothesis. -/
theorem b3_pos_iff {α β : R} :
    0 < b3 α β ↔ 2 * β < -(3 * α) := by
  rw [b3_affine_eq]
  constructor <;> intro h <;> linarith

/-- **So the intercept is pinned to a window.** A positive two-body binding together with a
positive three-body cumulant forces `−2α < β < −³⁄₂·α`: the intercept must be large and negative,
comparable to twice the slope. (The window is non-empty exactly when `α > 0`, which is not needed
for the implication itself.) -/
theorem b3_pos_forces_intercept_window {α β : R} (h2 : 0 < b2 α β)
    (h3 : 0 < b3 α β) : -(2 * α) < β ∧ 2 * β < -(3 * α) := by
  rw [b2_eq] at h2
  rw [b3_affine_eq] at h3
  exact ⟨by linarith, by linarith⟩

/-- **The measured model is outside the window.** `α = 5`, `β = −1`: the two-body binding is
positive but `2β = −2` is not below `−3α = −15`, so the three-body cumulant is negative. -/
theorem measuredModel_outside_window : ¬ (2 * (-1 : ℚ) < -(3 * 5)) := by norm_num

/-- **The measured model's cumulant is strictly negative**, so its `b₃` has the wrong sign against
the measured `+1.4262225 MeV`. -/
theorem measuredModel_b3_neg : b3 (5 : ℚ) (-1) < 0 := by
  rw [measuredModel_b3]; norm_num

/-- **Non-vacuity: the window is inhabited.** An affine multiplicity with a large negative
intercept does give a positive three-body cumulant — here `α = 5`, `β = −8`, so `μ(2) = 2`,
`μ(3) = 7` and `b₃ = 1 > 0`. So the affine family is not excluded; the measured intercept is what
fails. -/
theorem window_is_inhabited : 0 < b3 (5 : ℚ) (-8) ∧ 0 < b2 (5 : ℚ) (-8) := by
  rw [b3_affine_eq, b2_eq]; norm_num

end Ordered

end QOU.Mass.AffineCountMultiplicityWindow
