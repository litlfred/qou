import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts

open Complex
open MeasureTheory

noncomputable section

/-- The contour integral of `f` over the boundary of the fundamental parallelogram
with base point `z₀` and periods `ω₁, ω₂`. -/
def parallelogramIntegral (f : ℂ → ℂ) (ω₁ ω₂ z₀ : ℂ) : ℂ :=
  (∫ t in (0:ℝ)..1, ω₁ * f (z₀ + t * ω₁)) +
  (∫ t in (0:ℝ)..1, ω₂ * f (z₀ + ω₁ + t * ω₂)) -
  (∫ t in (0:ℝ)..1, ω₁ * f (z₀ + ω₂ + t * ω₁)) -
  (∫ t in (0:ℝ)..1, ω₂ * f (z₀ + t * ω₂))

-- MATHLIB GAP: Cauchy-Goursat for parallelograms
-- If f is analytic on and inside the parallelogram, the integral vanishes.
-- BLOCKED: Proving Cauchy-Goursat for parallelograms from scratch in Lean 4 is currently infeasible.
-- Mathlib only has `integral_boundary_rect_eq_zero_of_differentiable_on_off_countable` which applies
-- strictly to axis-aligned rectangles (`Mathlib.Analysis.Complex.CauchyIntegral`).
-- We cannot use an affine transformation to pull back a generic parallelogram to an axis-aligned
-- rectangle because such a transformation is ℝ-linear, not ℂ-linear, and therefore does not
-- preserve complex differentiability (it would violate the Cauchy-Riemann equations).
-- The standard proof involves decomposing the parallelogram into two triangles and proving Goursat's
-- lemma for triangles (subdividing into 4 smaller triangles and bounding the integral). However,
-- Mathlib currently completely lacks integrals over triangles and Goursat's lemma for simplices.
--
-- SOUNDNESS FIX 2026-08-24. This axiom was stated WITHOUT any hypothesis on `f`:
--
--     axiom … (f : ℂ → ℂ) (ω₁ ω₂ z₀ : ℂ) : parallelogramIntegral f ω₁ ω₂ z₀ = 0
--
-- The name says `_of_differentiable` and the comment above says "If f is analytic",
-- but neither reached the statement, so it asserted that the contour integral of
-- EVERY function vanishes. Instantiated at `fun z => (z - w)⁻¹` it contradicts the
-- pole axiom below, and `False` was derivable (verified against this module, not a
-- reproduction: docs/audits/2026-08-24-parallelogram-axioms-inconsistent.lean).
--
-- `Differentiable ℂ f` (entire) is the SOUND repair, not the sharp one: Cauchy's
-- theorem needs only differentiability on a neighbourhood of the closed
-- parallelogram. Entire is strictly stronger, so the axiom is weaker than it could
-- be — correct but less useful. Sharpening it to a neighbourhood hypothesis is the
-- eventual target and is left open deliberately rather than guessed at.
axiom parallelogramIntegral_eq_zero_of_differentiable (f : ℂ → ℂ) (ω₁ ω₂ z₀ : ℂ)
    (hf : Differentiable ℂ f) :
  parallelogramIntegral f ω₁ ω₂ z₀ = 0

-- MATHLIB GAP: Bare pole integral
-- Bare pole integral over the boundary of the parallelogram
-- BLOCKED: Proving this requires the argument principle or the residue theorem for parallelograms.
-- While we have `QOU.Mathlib.ArgumentPrinciple` for the disc, extending it to the parallelogram
-- requires the Cauchy-Goursat theorem for parallelograms (which is blocked above) to show that
-- the integral of the holomorphic part `g(z)` vanishes. Furthermore, we would need to continuously
-- deform the parallelogram contour into a small circle around the pole `w`, which requires
-- homotopy invariance of contour integrals (also missing for generic polygonal paths in Mathlib).
--
-- SOUNDNESS FIX 2026-08-24. This axiom was stated WITHOUT hypotheses on `ω₁ ω₂ w`:
--
--     axiom … (ω₁ ω₂ z₀ w : ℂ) : parallelogramIntegral (fun z => (z - w)⁻¹) … = 2πi
--
-- and was inconsistent BY ITSELF, independently of the axiom above. Every term of
-- `parallelogramIntegral` carries a literal `ω₁` or `ω₂` factor, so at the
-- DEGENERATE parallelogram `ω₁ = ω₂ = 0` the left side is identically `0`, giving
-- `0 = 2πi`. Verified, exit 0.
--
-- It was also false for `w` OUTSIDE the parallelogram, where the true value is `0`,
-- and the sign depends on orientation. Three hypotheses, all of them standard:
--
--   * `horient : 0 < (ω₂ / ω₁).im` — the periods are positively oriented. This also
--     rules out the degenerate case (it forces `ω₁ ≠ 0` and `ω₂ / ω₁ ∉ ℝ`), and it
--     fixes the SIGN: without it the residue is `±2πi`.
--   * `w` is strictly interior, written in the period coordinates `a, b ∈ (0,1)`.
--
-- The residue theorem then gives `2πi` with multiplicity one, since a strictly
-- interior `w` is enclosed exactly once.
axiom parallelogramIntegral_inv_sub_eq_two_pi_i (ω₁ ω₂ z₀ w : ℂ)
    (horient : 0 < (ω₂ / ω₁).im)
    (a b : ℝ) (ha₀ : 0 < a) (ha₁ : a < 1) (hb₀ : 0 < b) (hb₁ : b < 1)
    (hw : w = z₀ + (a : ℂ) * ω₁ + (b : ℂ) * ω₂) :
  parallelogramIntegral (fun z => (z - w)⁻¹) ω₁ ω₂ z₀ = 2 * Real.pi * I

end
