import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Complex.HasPrimitives
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts
import Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv

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

/-! ## The bare pole integral — proved by edge-wise logarithms

No residue theorem or winding number is needed (Mathlib v4.24.0 has neither). Each edge of the
parallelogram, rescaled by its own direction, is a horizontal segment `t ↦ u + t`, `t ∈ [0,1]`, off
the real axis, so the principal logarithm is a primitive of `(z - w)⁻¹` along it. -/

/-- **One edge of the pole integral.** If `u = (s - w)/ω` is off the real axis, the segment
`t ↦ u + t` stays in `slitPlane`, and `∫₀¹ ω (s + tω − w)⁻¹ dt = log (u + 1) − log u` by the
fundamental theorem of calculus. -/
theorem edge_integral_inv_sub_eq_log_sub {s ω w : ℂ} (hω : ω ≠ 0)
    (him : ((s - w) / ω).im ≠ 0) :
    (∫ t in (0:ℝ)..1, ω * (s + (t : ℂ) * ω - w)⁻¹) =
      log ((s - w) / ω + 1) - log ((s - w) / ω) := by
  set u := (s - w) / ω with hu
  have hne : ∀ t : ℝ, u + (t : ℂ) ≠ 0 := by
    intro t h
    have := congrArg Complex.im h
    simp at this
    exact him this
  have hcongr : ∀ t : ℝ, ω * (s + (t : ℂ) * ω - w)⁻¹ = (u + (t : ℂ))⁻¹ := by
    intro t
    have : s + (t : ℂ) * ω - w = (u + t) * ω := by
      rw [hu]; field_simp; ring
    rw [this, mul_inv, ← mul_assoc, mul_comm ω, mul_assoc, mul_inv_cancel₀ hω, mul_one]
  simp_rw [hcongr]
  have hderiv : ∀ t ∈ Set.uIcc (0:ℝ) 1,
      HasDerivAt (fun x : ℝ => log (u + (x : ℂ))) (u + (t : ℂ))⁻¹ t := by
    intro t _
    have h1 : HasDerivAt (fun x : ℝ => u + (x : ℂ)) 1 t := by
      simpa using (Complex.ofRealCLM.hasDerivAt (x := t)).const_add u
    have h2 : u + (t : ℂ) ∈ slitPlane := by
      rw [mem_slitPlane_iff]; right; simpa using him
    simpa [one_div] using HasDerivAt.clog_real h1 h2
  have hcont : Continuous (fun t : ℝ => (u + (t : ℂ))⁻¹) :=
    Continuous.inv₀ (by fun_prop) hne
  have := intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv (hcont.intervalIntegrable 0 1)
  simpa using this

/-- For `u` off the real axis, `Im (log (u+1) − log u) = arg ((u+1)/u)`. -/
theorem im_log_succ_sub_log {u : ℂ} (h : u.im ≠ 0) :
    (log (u + 1) - log u).im = arg ((u + 1) / u) := by
  have hu : u ≠ 0 := fun h0 => h (by simp [h0])
  have hu1 : u + 1 ≠ 0 := fun h0 => h (by have := congrArg Complex.im h0; simpa using this)
  rw [sub_im, log_im, log_im]
  have hrange : -Real.pi < arg (u + 1) - arg u ∧ arg (u + 1) - arg u ≤ Real.pi := by
    have h1im : (u + 1).im = u.im := by simp
    rcases lt_or_gt_of_ne h with hneg | hpos
    · have a1 := arg_neg_iff.mpr hneg
      have a2 := arg_neg_iff.mpr (h1im ▸ hneg)
      have b1 := neg_pi_lt_arg u
      have b2 := neg_pi_lt_arg (u + 1)
      constructor <;> linarith
    · have a1 := arg_nonneg_iff.mpr hpos.le
      have a2 := arg_nonneg_iff.mpr (h1im ▸ hpos.le)
      have b1 := arg_lt_pi_iff.mpr (Or.inr h)
      have b2 := arg_lt_pi_iff.mpr (Or.inr (h1im ▸ h))
      constructor <;> linarith
  rw [← Real.Angle.toReal_coe_eq_self_iff.mpr hrange,
    ← Real.Angle.toReal_coe_eq_self_iff.mpr ⟨neg_pi_lt_arg ((u + 1) / u), arg_le_pi _⟩,
    Real.Angle.coe_sub, arg_div_coe_angle hu1 hu]

/-- `Im ((u+1)/u) = Im (u⁻¹)`. -/
theorem im_div_succ (u : ℂ) (hu : u ≠ 0) : ((u + 1) / u).im = -u.im / normSq u := by
  rw [add_div, div_self hu, add_im, one_im, zero_add, div_eq_mul_inv, one_mul, inv_im]

/-- Below the real axis an edge term turns by an angle in `(0, π)`. -/
theorem im_log_succ_sub_log_pos {u : ℂ} (h : u.im < 0) :
    0 < (log (u + 1) - log u).im ∧ (log (u + 1) - log u).im < Real.pi := by
  have hu : u ≠ 0 := fun h0 => by simp [h0] at h
  rw [im_log_succ_sub_log h.ne]
  have hi : 0 < ((u + 1) / u).im := by
    rw [im_div_succ u hu]; exact div_pos (by linarith) (normSq_pos.mpr hu)
  refine ⟨lt_of_le_of_ne (arg_nonneg_iff.mpr hi.le) ?_, arg_lt_pi_iff.mpr (Or.inr hi.ne')⟩
  intro h0; have := (arg_eq_zero_iff.mp h0.symm).2; linarith

/-- Above the real axis an edge term turns by an angle in `(−π, 0)`. -/
theorem im_log_succ_sub_log_neg {u : ℂ} (h : 0 < u.im) :
    -Real.pi < (log (u + 1) - log u).im ∧ (log (u + 1) - log u).im < 0 := by
  have hu : u ≠ 0 := fun h0 => by simp [h0] at h
  rw [im_log_succ_sub_log h.ne']
  have hi : ((u + 1) / u).im < 0 := by
    rw [im_div_succ u hu]; exact div_neg_of_neg_of_pos (by linarith) (normSq_pos.mpr hu)
  exact ⟨neg_pi_lt_arg _, arg_neg_iff.mpr hi⟩

/-- **Bare pole integral over the parallelogram (PROVED).** For positively oriented periods
(`0 < Im (ω₂/ω₁)`) and `w` strictly interior (`a, b ∈ (0,1)` in period coordinates), the integral
of `(z - w)⁻¹` around the boundary is `2πi`.

Proof: by `edge_integral_inv_sub_eq_log_sub` the integral is a signed sum `T` of four differences
`log (u + 1) − log u`, with `u` below the real axis on the bottom and right edges and above it on
the top and left (subtracted) edges. The four quotients `(u + 1)/u` telescope, so `exp T = 1` and
`T = 2πi n`. Each signed term has imaginary part in `(0, π)`, so `Im T ∈ (0, 4π)` and `n = 1`.
The hypotheses are needed: at `ω₁ = ω₂ = 0` the integral is `0`, for exterior `w` it is `0`, and
the orientation fixes the sign.
-- Ref: [ahlfors1979] Ahlfors, Complex Analysis, 3rd ed., Ch. 4 §5 (the residue
     theorem; a simple pole strictly inside a positively-oriented simple
     closed contour contributes 2πi times its residue, here 1). Proved here directly.
-/
theorem parallelogramIntegral_inv_sub_eq_two_pi_i (ω₁ ω₂ z₀ w : ℂ)
    (horient : 0 < (ω₂ / ω₁).im)
    (a b : ℝ) (ha₀ : 0 < a) (ha₁ : a < 1) (hb₀ : 0 < b) (hb₁ : b < 1)
    (hw : w = z₀ + (a : ℂ) * ω₁ + (b : ℂ) * ω₂) :
  parallelogramIntegral (fun z => (z - w)⁻¹) ω₁ ω₂ z₀ = 2 * Real.pi * I := by
  have hω₁ : ω₁ ≠ 0 := by rintro rfl; simp at horient
  have hω₂ : ω₂ ≠ 0 := by rintro rfl; simp at horient
  set τ := ω₂ / ω₁ with hτ
  have hτ0 : τ ≠ 0 := div_ne_zero hω₂ hω₁
  -- `Im (ω₁/ω₂) < 0`
  have hσ : (ω₁ / ω₂).im < 0 := by
    have : ω₁ / ω₂ = τ⁻¹ := by rw [hτ, inv_div]
    rw [this, inv_im]
    exact div_neg_of_neg_of_pos (by linarith) (normSq_pos.mpr hτ0)
  -- the four normalised start points
  have e1 : (z₀ - w) / ω₁ = -(a : ℂ) - (b : ℂ) * τ := by
    rw [hw, hτ]; field_simp; ring
  have e2 : (z₀ + ω₁ - w) / ω₂ = ((1 - a : ℝ) : ℂ) * (ω₁ / ω₂) - (b : ℂ) := by
    rw [hw]; push_cast; field_simp; ring
  have e3 : (z₀ + ω₂ - w) / ω₁ = -(a : ℂ) + ((1 - b : ℝ) : ℂ) * τ := by
    rw [hw, hτ]; push_cast; field_simp; ring
  have e4 : (z₀ - w) / ω₂ = -(a : ℂ) * (ω₁ / ω₂) - (b : ℂ) := by
    rw [hw]; field_simp; ring
  have i1 : ((z₀ - w) / ω₁).im < 0 := by
    rw [e1]; simp; nlinarith
  have i2 : ((z₀ + ω₁ - w) / ω₂).im < 0 := by
    rw [e2]; simp only [sub_im, mul_im, ofReal_re, ofReal_im, zero_mul, add_zero]
    simp; nlinarith
  have i3 : 0 < ((z₀ + ω₂ - w) / ω₁).im := by
    rw [e3]; simp only [add_im, neg_im, mul_im, ofReal_re, ofReal_im, zero_mul, add_zero]
    simp; nlinarith
  have i4 : 0 < ((z₀ - w) / ω₂).im := by
    rw [e4]; simp; nlinarith
  -- the four edges
  have E1 := edge_integral_inv_sub_eq_log_sub (s := z₀) (ω := ω₁) (w := w) hω₁ i1.ne
  have E2 := edge_integral_inv_sub_eq_log_sub (s := z₀ + ω₁) (ω := ω₂) (w := w) hω₂ i2.ne
  have E3 := edge_integral_inv_sub_eq_log_sub (s := z₀ + ω₂) (ω := ω₁) (w := w) hω₁ i3.ne'
  have E4 := edge_integral_inv_sub_eq_log_sub (s := z₀) (ω := ω₂) (w := w) hω₂ i4.ne'
  unfold parallelogramIntegral
  simp only []
  rw [E1, E2, E3, E4]
  -- `exp` of each edge term is the ratio of consecutive vertices (relative to `w`)
  have hexp : ∀ p ω : ℂ, ω ≠ 0 → (p / ω).im ≠ 0 →
      p ≠ 0 ∧ p + ω ≠ 0 ∧ exp (log (p / ω + 1) - log (p / ω)) = (p + ω) / p := by
    intro p ω hω hi
    have hu : p / ω ≠ 0 := fun h0 => hi (by simp [h0])
    have hu1 : p / ω + 1 ≠ 0 := fun h0 => hi (by have := congrArg Complex.im h0; simpa using this)
    have hp : p ≠ 0 := fun h0 => hu (by simp [h0])
    have hpω : p + ω ≠ 0 := by
      intro h0; apply hu1; rw [div_add_one hω, h0, zero_div]
    refine ⟨hp, hpω, ?_⟩
    rw [exp_sub, exp_log hu1, exp_log hu]
    field_simp
  obtain ⟨p1, q1, x1⟩ := hexp _ _ hω₁ i1.ne
  obtain ⟨p2, q2, x2⟩ := hexp _ _ hω₂ i2.ne
  obtain ⟨p3, q3, x3⟩ := hexp _ _ hω₁ i3.ne'
  obtain ⟨p4, q4, x4⟩ := hexp _ _ hω₂ i4.ne'
  set T := log ((z₀ - w) / ω₁ + 1) - log ((z₀ - w) / ω₁) +
      (log ((z₀ + ω₁ - w) / ω₂ + 1) - log ((z₀ + ω₁ - w) / ω₂)) -
      (log ((z₀ + ω₂ - w) / ω₁ + 1) - log ((z₀ + ω₂ - w) / ω₁)) -
      (log ((z₀ - w) / ω₂ + 1) - log ((z₀ - w) / ω₂)) with hT
  have hexpT : exp T = 1 := by
    rw [hT, exp_sub, exp_sub, exp_add, x1, x2, x3, x4]
    have r2 : z₀ + ω₁ - w + ω₂ = z₀ + ω₂ - w + ω₁ := by ring
    have r1 : z₀ - w + ω₁ = z₀ + ω₁ - w := by ring
    have r4 : z₀ - w + ω₂ = z₀ + ω₂ - w := by ring
    rw [r1] at q1 ⊢; rw [r4] at q4 ⊢; rw [r2] at q2 ⊢
    field_simp
  obtain ⟨n, hn⟩ := exp_eq_one_iff.mp hexpT
  -- the imaginary part of `T` lies strictly between `0` and `4π`
  have j1 := im_log_succ_sub_log_pos i1
  have j2 := im_log_succ_sub_log_pos i2
  have j3 := im_log_succ_sub_log_neg i3
  have j4 := im_log_succ_sub_log_neg i4
  have hTim : T.im = 2 * Real.pi * n := by
    rw [hn]; simp; ring
  have hTim' : 0 < T.im ∧ T.im < 4 * Real.pi := by
    rw [hT]; simp only [add_im, sub_im] at j1 j2 j3 j4 ⊢
    constructor <;> linarith
  have hpi := Real.pi_pos
  have hn1 : n = 1 := by
    have h0 : (0 : ℝ) < n := by
      by_contra hc; push_neg at hc; nlinarith [hTim'.1]
    have h2 : (n : ℝ) < 2 := by
      by_contra hc; push_neg at hc; nlinarith [hTim'.2]
    have h0' : 0 < n := by exact_mod_cast h0
    have h2' : n < 2 := by exact_mod_cast h2
    omega
  rw [hn, hn1]; simp

end
