import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Complex.HasPrimitives
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

/-! ## Cauchy for the parallelogram — proved, not axiomatised

This was an `axiom`, and the comment above it read:

> **BLOCKED**: Proving Cauchy-Goursat for parallelograms from scratch in Lean 4 is currently
> infeasible.  Mathlib only has `integral_boundary_rect_eq_zero_of_differentiable_on_off_countable`
> which applies strictly to axis-aligned rectangles.  We cannot use an affine transformation to pull
> back a generic parallelogram to an axis-aligned rectangle because such a transformation is
> ℝ-linear, not ℂ-linear …  the standard proof involves decomposing the parallelogram into two
> triangles and proving Goursat's lemma for triangles.  However, Mathlib currently completely lacks
> integrals over triangles and Goursat's lemma for simplices.

**Every sentence of that is true and the conclusion does not follow**, because it answers a harder
question than the one the statement asks.  Goursat is what you need to prove Cauchy *from scratch*
for a merely-differentiable function.  The 2026-08-24 soundness fix had already added
`Differentiable ℂ f` — **entire** — and an entire function has a primitive.  With a primitive the
contour integral is a telescoping sum and the shape of the contour is irrelevant: no triangles, no
Goursat, no rectangles, no affine pullback.

Concretely, if `F' = f` then each edge integrates by the fundamental theorem of calculus,

  ∫₀¹ ω · f(a + tω) dt = F(a + ω) − F(a),

and the four edges of the parallelogram telescope:

  [F(z₀+ω₁) − F(z₀)] + [F(z₀+ω₁+ω₂) − F(z₀+ω₁)]
    − [F(z₀+ω₂+ω₁) − F(z₀+ω₂)] − [F(z₀+ω₂) − F(z₀)] = 0.

The primitive comes from Mathlib's `DifferentiableOn.isExactOn_ball` (Morera for a disk,
`Mathlib/Analysis/Complex/HasPrimitives.lean`), applied on any ball large enough to contain the four
edges — `‖z₀‖ + ‖ω₁‖ + ‖ω₂‖ + 1` does.

The one thing genuinely given up is sharpness, and it was given up in 2026-08-24 rather than here:
Cauchy needs only differentiability on a neighbourhood of the closed parallelogram, and `Differentiable`
is strictly stronger.  Sharpening the hypothesis still wants Goursat, so that half of the comment
above stands and is left open.
-/

/-- Every point of the segment `t ↦ a + t·ω`, `t ∈ [0,1]`, lies in the ball of radius
`‖a‖ + ‖ω‖ + ε` about the origin. -/
theorem segment_mem_ball {a ω : ℂ} {R : ℝ} (hR : ‖a‖ + ‖ω‖ < R) {t : ℝ}
    (ht : t ∈ Set.uIcc (0 : ℝ) 1) : a + (t : ℂ) * ω ∈ Metric.ball (0 : ℂ) R := by
  rw [Set.uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)] at ht
  have ht0 : |t| ≤ 1 := by rw [abs_le]; constructor <;> [linarith [ht.1]; linarith [ht.2]]
  have : ‖a + (t : ℂ) * ω‖ ≤ ‖a‖ + ‖ω‖ := by
    refine (norm_add_le _ _).trans ?_
    have : ‖(t : ℂ) * ω‖ ≤ ‖ω‖ := by
      rw [norm_mul, Complex.norm_real, Real.norm_eq_abs]
      nlinarith [norm_nonneg ω, abs_nonneg t]
    linarith
  simpa [Metric.mem_ball, dist_eq_norm] using lt_of_le_of_lt this hR

/-- **One edge integrates to a difference of primitive values.**

`∫₀¹ ω · f(a + tω) dt = F(a + ω) − F(a)` whenever `F` is a primitive of `f` on a ball containing
the segment.  The chain rule supplies `HasDerivAt (fun s : ℝ => F (a + s·ω)) (ω · f (a + tω)) t`;
the fundamental theorem of calculus does the rest. -/
theorem edge_integral_eq_sub {f F : ℂ → ℂ} {a ω : ℂ} {R : ℝ}
    (hF : ∀ z ∈ Metric.ball (0 : ℂ) R, HasDerivAt F (f z) z)
    (hf : Continuous f) (hR : ‖a‖ + ‖ω‖ < R) :
    (∫ t in (0:ℝ)..1, ω * f (a + (t : ℂ) * ω)) = F (a + ω) - F a := by
  have hderiv : ∀ t ∈ Set.uIcc (0:ℝ) 1,
      HasDerivAt (fun s : ℝ => F (a + (s : ℂ) * ω)) (ω * f (a + (t : ℂ) * ω)) t := by
    intro t ht
    have hu : HasDerivAt (fun s : ℝ => a + (s : ℂ) * ω) ω t := by
      simpa using ((Complex.ofRealCLM.hasDerivAt (x := t)).mul_const ω).const_add a
    have := (hF _ (segment_mem_ball hR ht)).scomp t hu
    simpa [mul_comm] using this
  have hint : IntervalIntegrable (fun t : ℝ => ω * f (a + (t : ℂ) * ω)) volume 0 1 :=
    (Continuous.intervalIntegrable (by fun_prop) 0 1)
  have := intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint
  simpa using this

/-- **Cauchy's theorem for the fundamental parallelogram (PROVED).**

The contour integral of an entire function around the boundary of the parallelogram with base point
`z₀` and periods `ω₁, ω₂` vanishes.  See the section header for why this needs no Goursat. -/
theorem parallelogramIntegral_eq_zero_of_differentiable (f : ℂ → ℂ) (ω₁ ω₂ z₀ : ℂ)
    (hf : Differentiable ℂ f) :
    parallelogramIntegral f ω₁ ω₂ z₀ = 0 := by
  set R : ℝ := ‖z₀‖ + ‖ω₁‖ + ‖ω₂‖ + 1 with hRdef
  obtain ⟨F, hF⟩ : Complex.IsExactOn f (Metric.ball (0 : ℂ) R) :=
    (hf.differentiableOn).isExactOn_ball
  have hfc : Continuous f := hf.continuous
  have n₁ := norm_nonneg ω₁
  have n₂ := norm_nonneg ω₂
  have n₀ := norm_nonneg z₀
  -- the four edges, each a difference of primitive values
  have e₁ := edge_integral_eq_sub (f := f) (F := F) (a := z₀) (ω := ω₁) hF hfc (by rw [hRdef]; linarith)
  have e₂ := edge_integral_eq_sub (f := f) (F := F) (a := z₀ + ω₁) (ω := ω₂) hF hfc
    (by rw [hRdef]; have := norm_add_le z₀ ω₁; linarith)
  have e₃ := edge_integral_eq_sub (f := f) (F := F) (a := z₀ + ω₂) (ω := ω₁) hF hfc
    (by rw [hRdef]; have := norm_add_le z₀ ω₂; linarith)
  have e₄ := edge_integral_eq_sub (f := f) (F := F) (a := z₀) (ω := ω₂) hF hfc (by rw [hRdef]; linarith)
  rw [parallelogramIntegral, e₁, e₂, e₃, e₄]
  have h : z₀ + ω₁ + ω₂ = z₀ + ω₂ + ω₁ := by ring
  rw [h]
  ring

-- MATHLIB GAP: Bare pole integral
-- Bare pole integral over the boundary of the parallelogram.
--
-- GENUINELY BLOCKED, and for a different reason than the theorem above. Measured
-- against the pinned Mathlib v4.24.0: `windingNumber` occurs NOWHERE, and there is no
-- residue theorem (the only `residue` hits are p-adic and local-field ring
-- homomorphisms, an unrelated sense of the word). So both classical routes to this
-- statement are absent upstream, not merely inconvenient.
--
-- THE TWO AXIOMS IN THIS FILE WERE NEVER THE SAME DIFFICULTY, and the shared
-- "BLOCKED: Goursat is infeasible" reasoning was right about this one and wrong about
-- the other. Cauchy for an ENTIRE function needs only a primitive, which
-- `DifferentiableOn.isExactOn_ball` supplies, after which the four edges telescope and
-- the contour's shape is irrelevant — that is now
-- `parallelogramIntegral_eq_zero_of_differentiable`, proved above. The integrand here
-- is `(z - w)⁻¹`, which has a POLE, so no primitive exists on any region containing the
-- contour and the telescoping argument has nothing to stand on. The difference is the
-- pole, not the parallelogram.
--
-- What the old text got right: contour deformation onto a small circle about `w` needs
-- homotopy invariance for polygonal paths, which Mathlib lacks. What it got wrong: the
-- clause "requires the Cauchy-Goursat theorem for parallelograms (which is blocked
-- above)" — that theorem is no longer blocked and no longer above; it is proved. The
-- holomorphic-part step it was invoked for is therefore available; it is the deformation
-- that is not.
--
-- The corpus does carry `QOU.Mathlib.ArgumentPrinciple` for the disc, so the honest
-- statement of the remaining gap is the TRANSFER from disc to parallelogram, and that
-- transfer is exactly the missing homotopy invariance.
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
