/-
# UT(Σ₄) is canonically oriented and chiral; conjugation is a strict contactomorphism

Owner, 2026-10-12: option 1 ("bar involution = conjugation") only if it can be derived (bean
`qou-jfx8`). `BringConjugationChirality.lean` showed that on `UT(Σ₄)` (where the corpus puts the
Reeb flow) the natural lift of complex conjugation `ι` preserves orientation, so it cannot be
the `σ ↔ σ⁻¹` swap there. This file states what DOES fix the chirality on `UT(Σ₄)`.

## 1. The geodesic flow fixes the orientation

On the upper half-plane with unit tangent vectors `(x, y, θ)`, the Liouville (contact) form
of the geodesic flow is `α = (cos θ dx + sin θ dy)/y`, whose Reeb field is the geodesic
spray. Then

    α ∧ dα = −(1/y²) dx ∧ dy ∧ dθ,

nowhere zero (`contact_volume_coeff`). So `α ∧ dα` is a canonical volume form on `UT(Σ₄)`
(it descends, being `PSL₂ℝ`-invariant), and it orients `UT(Σ₄)` with **no choice made**. Note the
sign: it is the *opposite* of the orientation `dx ∧ dy ∧ dθ` built from the complex
orientation of the base and the counter-clockwise fibre. This matches
`BringConeLinkEulerNumber.lean`, which identifies the cone's link with `UT(Σ₄)`
"orientation reversed". (Matching signs of two conventions is recorded, not proved here.)

## 2. Conjugation preserves the contact form itself

In the upper half-plane, conjugation is `z ↦ −z̄`, i.e. `(x, y) ↦ (−x, y)`, and its differential
sends `θ ↦ π − θ`. The pullback of `α` is `α` (`iota_pullback_alpha`), so `ι` lifts to a
**strict contactomorphism**, commuting with the Reeb (geodesic) flow, with Jacobian
determinant `+1` (`iota_lift_det`). More generally `α` is built from the metric alone
(`α_v(ξ) = ⟨v, dπ ξ⟩`), so the lift of EVERY isometry, orientation-reversing ones included,
preserves it; the lemma checks the reflection `z ↦ −z̄` as the instance. Conjugation is a symmetry of the whole Reeb structure; it
cannot carry chirality.

## 3. UT(Σ₄) has no fibre-preserving orientation reversal

Reversing orientation negates the Seifert Euler number. The link has Euler number `−6 ≠ 0`
(`bring_link_euler`), so `e ≠ −e` (`bring_link_chiral`). Hence no orientation-reversing,
fibre-preserving self-map exists. (For Seifert spaces with `SL̃₂` geometry every
self-homeomorphism is isotopic to a fibre-preserving one; that is a citation, not proved here.)
**UT(Σ₄) is a chiral 3-manifold.**

## What this derives, and the one bit left

On an oriented 3-manifold, the skein/Hecke relation at `q` with orientation `o` is the relation
at `q⁻¹` with orientation `−o`, and links go to mirrors: the only symmetry is the JOINT one
(orientation reversal, `q ↦ q⁻¹`). On `UT(Σ₄)` the orientation is canonical (§1) and cannot be
reversed (§3), and conjugation does not touch it (§2). So once `q₀ > 1` is fixed (CAL-2), the
preference between `σ` and `σ⁻¹` is determined. What remains is a single **global** sign
convention, "a positive crossing is positive for `α ∧ dα`", not a per-collision choice. That bit
is equivalent to `q₀ > 1` versus `q₀ < 1`, which the framework has already spent. It is a
convention to record, not a parameter to fit.

The per-collision `ChiralityMatching` class (`letterSign_conj`) has the wrong shape for
`UT(Σ₄)`: chirality there is global, not a property of where on `Σ₄` a collision sits.

§7c: over `ℝ` (trigonometry, orientation signs) and `ℤ` (Euler numbers).

-- Ref: [manuscript] lem:bring-cone-reeb-quaternionic-twist; bean qou-rydq; bean qou-jfx8.
   Geodesic flow as Reeb flow of the Liouville form: standard (Geiges, *An Introduction to
   Contact Topology*, §1.5). Skein modules under orientation reversal: arXiv:1610.04728.
   Seifert manifolds, Euler number and orientation: Scott, *The geometries of 3-manifolds*
   (1983), §3.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import QOU.Brings.BringConeLinkEulerNumber

namespace QOU.Brings.UTContactChirality

open Real

/-- **`α ∧ dα` is nowhere zero.** With `α = (cos θ dx + sin θ dy)/y`, the coefficient of
`dx ∧ dy ∧ dθ` in `α ∧ dα` is `a_x·(∂_y a_θ − ∂_θ a_y) − a_y·(∂_x a_θ − ∂_θ a_x)`, with
`∂_θ a_y = cos θ / y`, `∂_θ a_x = −sin θ / y` and `a_θ = 0`; it equals `−1/y²`. (The partial
derivatives are entered by hand; `ut_contact_orientation_probe.py` checks them symbolically.) -/
theorem contact_volume_coeff (y θ : ℝ) (hy : y ≠ 0) :
    (cos θ / y) * (0 - cos θ / y) - (sin θ / y) * (0 - -(sin θ / y)) = -1 / y ^ 2 := by
  have h := sin_sq_add_cos_sq θ
  field_simp
  linear_combination -h

theorem contact_volume_ne_zero (y θ : ℝ) (hy : y ≠ 0) :
    (cos θ / y) * (0 - cos θ / y) - (sin θ / y) * (0 - -(sin θ / y)) ≠ 0 := by
  rw [contact_volume_coeff y θ hy]
  exact div_ne_zero (by norm_num) (pow_ne_zero 2 hy)

/-- **Conjugation preserves `α`.** Under `(x, y, θ) ↦ (−x, y, π − θ)`, the `dx` coefficient
`cos θ / y` pulls back to `cos (π − θ)·(−1)/y` and the `dy` coefficient `sin θ / y` to
`sin (π − θ)/y`; both are unchanged. -/
theorem iota_pullback_alpha (y θ : ℝ) :
    cos (π - θ) * (-1) / y = cos θ / y ∧ sin (π - θ) / y = sin θ / y := by
  refine ⟨?_, by rw [sin_pi_sub]⟩
  rw [cos_pi_sub]; ring

/-- The lift `(x, y, θ) ↦ (−x, y, π − θ)` has Jacobian `diag(−1, 1, −1)`, determinant `+1`. -/
theorem iota_lift_det : ((-1 : ℤ) * 1 * (-1)) = 1 := by norm_num

/-- **Orientation reversal negates the Euler number; a nonzero Euler number forbids a
fibre-preserving orientation reversal.** -/
theorem euler_chiral (e : ℤ) (he : e ≠ 0) : e ≠ -e := by
  intro h; omega

/-- **`UT(Σ₄)` is chiral**: Euler number `−6`, so `e ≠ −e`. -/
theorem bring_link_chiral :
    linkEulerNumber (canonicalDegree 4) ≠ -linkEulerNumber (canonicalDegree 4) := by
  rw [bring_link_euler]; norm_num

end QOU.Brings.UTContactChirality
