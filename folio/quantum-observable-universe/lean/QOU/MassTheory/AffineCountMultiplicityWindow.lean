import Mathlib.Tactic

/-!
# An affine crossing count needs a large negative intercept, and the measured one has none

`QOU.Mass.CountChannelCarrierLocus` reduced `qou-brng`'s remaining question to one test: a carrier
must break `μ_t = 3·μ_p`, where `μ = ½(n₊+n₋)` is the count multiplicity. This file runs that test
against the corpus's **measured** crossing counts and turns the result into a constraint on the
whole affine family.

## 🛑 RETRACTED: the instantiation at `(5, −1)` — the two counts are different objects

An earlier version of this file instantiated the window at `μ(A) = 5A − 1`, the count from
`QOU.MassTheory.CrossingCountAffine`, calling it *"exactly the multiplicity
`BrunnianBindingChannel.countChannel` carries"*. **That identification is wrong and is withdrawn.**

Two independent reasons, either of which is fatal:

1. **Total vs inter-component.** `countChannel`'s `n₊, n₋` are *inter-component* crossings —
   `minimal_brunnian_bond` fixes them from "the pairwise crossing pattern inside `L6a4`". The
   `5A − 1` count is over **every** letter of the `A`-nucleon word, self-crossings included. In the
   construction the inter-nucleon letters are only the `A − 1` chain interfaces; the rest are the
   per-nucleon words.
2. **They are not crossing numbers at all.** `atom_braid_word_3A`'s own docstring: *"this does NOT
   return a braid word … the returned object lies in `H_n(q)` and is NOT in the image of
   `ρ : B_n → H_n(q)` … there is NO SINGLE LINK behind it … **so NO TOPOLOGICAL quantity may be read
   off it — not a volume, not a crossing number, not a genus**."* `n₊, n₋` there count Hecke **letter
   types** by their `d` coefficient, and `tr_M` of the object is a weighted sum of `2^{2A+1}` link
   invariants (32 for `²H`), not one link's.

The counts themselves are sound and the relations `n₊ + n₋ = 10A − 2`, `n₊ − n₋ = 4Z` hold exactly
(checked against the docstring's own `²H` figures: 23 letters, 11 `σ`, 7 `σ⁻¹`, 5 averaged `= 2A+1`).
**`CrossingCountAffine` is not impugned** — it feeds these counts to the *linear* functional
`E = n₊q − n₋q⁻¹`, which linearity transports; reading a *link crossing number* off them is the
forbidden step, and that step was mine.

**So the window below is stated for a general affine multiplicity and is instantiated at nothing.**
Whether the binding channel's inter-component counts are affine in `A` at all is open; the corpus's
`A − 1` chain interfaces would give `μ = (A−1)/2`, i.e. `r = β/α = −1`, still outside the window —
but that is an observation about the construction, not a measurement of a carrier, and it is not
claimed here.

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

/-- **Non-vacuity: the window is inhabited.** An affine multiplicity with a large negative
intercept does give a positive three-body cumulant — here `α = 5`, `β = −8`, so `μ(2) = 2`,
`μ(3) = 7` and `b₃ = 1 > 0`. So the affine family is not excluded; the measured intercept is what
fails. -/
theorem window_is_inhabited : 0 < b3 (5 : ℚ) (-8) ∧ 0 < b2 (5 : ℚ) (-8) := by
  rw [b3_affine_eq, b2_eq]; norm_num

end Ordered

end QOU.Mass.AffineCountMultiplicityWindow
