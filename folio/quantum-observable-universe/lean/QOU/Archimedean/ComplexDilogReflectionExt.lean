/-
# The complex Euler reflection identity on the full doubly-slit plane

    Li₂ z + Li₂ (1 − z) = π²/6 − log z · log (1 − z)
        for every  z ∈ ℂ ∖ ((−∞, 0] ∪ [1, ∞))

with `Li₂ = cLiTwoExt` (the integral continuation, analytic on `ℂ ∖ [1,∞)` by
`QOU.MathlibExt.analyticOnNhd_cLiTwoExt`) and `log` Mathlib's principal branch.

`QOU.Archimedean.cLiTwo_reflection` proves the identity only on `ball(½, ½)`,
where all four terms are given by series. This file continues it to the largest
domain on which the principal-branch statement is meaningful: `z` and `1 − z`
must both avoid `[1,∞)` (the `Li₂` cut) and both avoid `(−∞,0]` (the `log` cut);
the two pairs of conditions coincide, giving

    reflDomain = {z | z.im ≠ 0 ∨ (0 < z.re ∧ z.re < 1)}
              = slitPlane ∩ (1 − ·)⁻¹' slitPlane.

Proof: identity theorem. Both sides are analytic on `reflDomain`, which is open
and star-convex about `½` (hence preconnected), and they agree on the
neighbourhood `ball(½,½)` of `½`.

Sorry-free, no axioms beyond the standard three. Beans `qou-ph1k`, `qou-gkco`.

-- Ref: [manuscript] beans qou-ph1k, qou-gkco, qou-clx8
-/
import QOU.Archimedean.ComplexDilogBridge
import QOU.MathlibExt.ComplexDilogarithmUnique
import QOU.MathlibExt.ComplexRogersDilog

namespace QOU.Archimedean

open Complex QOU.MathlibExt Set

/-- The domain of the principal-branch reflection identity: `ℂ` minus both
real rays `(−∞,0]` and `[1,∞)`. -/
def reflDomain : Set ℂ := {z : ℂ | z.im ≠ 0 ∨ (0 < z.re ∧ z.re < 1)}

theorem mem_slitPlane_of_mem_reflDomain {z : ℂ} (hz : z ∈ reflDomain) :
    z ∈ slitPlane := by
  rw [mem_slitPlane_iff]
  rcases hz with h | h
  · exact Or.inr h
  · exact Or.inl h.1

theorem one_sub_mem_slitPlane_of_mem_reflDomain {z : ℂ} (hz : z ∈ reflDomain) :
    1 - z ∈ slitPlane := by
  rw [mem_slitPlane_iff]
  rcases hz with h | h
  · refine Or.inr ?_
    simpa using h
  · refine Or.inl ?_
    simp only [sub_re, one_re]
    linarith [h.2]

/-- `reflDomain = slitPlane ∩ (1 − ·)⁻¹' slitPlane`. -/
theorem reflDomain_eq :
    reflDomain = slitPlane ∩ (fun z : ℂ => 1 - z) ⁻¹' slitPlane := by
  ext z
  refine ⟨fun hz => ⟨mem_slitPlane_of_mem_reflDomain hz,
    one_sub_mem_slitPlane_of_mem_reflDomain hz⟩, ?_⟩
  rintro ⟨h1, h2⟩
  rw [mem_slitPlane_iff] at h1
  rw [mem_preimage, mem_slitPlane_iff] at h2
  simp only [sub_re, one_re, sub_im, one_im, zero_sub, ne_eq, neg_eq_zero] at h2
  rcases h1 with h1 | h1
  · rcases h2 with h2 | h2
    · exact Or.inr ⟨h1, by linarith⟩
    · exact Or.inl h2
  · exact Or.inl h1

theorem isOpen_reflDomain : IsOpen reflDomain := by
  rw [reflDomain_eq]
  exact isOpen_slitPlane.inter
    (isOpen_slitPlane.preimage (continuous_const.sub continuous_id))

theorem mem_notCut_of_mem_reflDomain {z : ℂ} (hz : z ∈ reflDomain) : z ∈ notCut := by
  rw [notCut_eq_preimage_slitPlane]
  exact one_sub_mem_slitPlane_of_mem_reflDomain hz

theorem one_sub_mem_notCut_of_mem_reflDomain {z : ℂ} (hz : z ∈ reflDomain) :
    1 - z ∈ notCut := by
  rw [notCut_eq_preimage_slitPlane]
  show 1 - (1 - z) ∈ slitPlane
  rw [sub_sub_cancel]
  exact mem_slitPlane_of_mem_reflDomain hz

/-- **`reflDomain` is the Rogers domain.** Both are `ℂ` with the two real cuts
`(−∞,0]` and `[1,∞)` removed: `reflDomain_eq` writes this set as
`slitPlane ∩ (1 − ·)⁻¹' slitPlane`, and `one_sub_mem_slitPlane_iff` identifies the
second factor with `notCut`. -/
theorem reflDomain_eq_rogersDomain : reflDomain = rogersDomain := by
  rw [reflDomain_eq]
  ext z
  simp only [Set.mem_inter_iff, Set.mem_preimage, rogersDomain]
  rw [one_sub_mem_slitPlane_iff]

theorem half_mem_reflDomain : (1 / 2 : ℂ) ∈ reflDomain :=
  Or.inr ⟨by norm_num, by norm_num⟩

/-- **`reflDomain` is star-convex about `½`.** A segment from `½` to a non-real
point is non-real except at `½`; a segment from `½` to a point of `(0,1)` stays
in `(0,1)`. -/
theorem starConvex_half_reflDomain : StarConvex ℝ (1 / 2 : ℂ) reflDomain := by
  intro w hw a b ha hb hab
  simp only [Complex.real_smul]
  have him' : ((a : ℂ) * (1 / 2) + (b : ℂ) * w).im = b * w.im := by simp
  have hre' : ((a : ℂ) * (1 / 2) + (b : ℂ) * w).re = a * (1 / 2) + b * w.re := by simp
  rcases hw with him | hre
  · rcases eq_or_lt_of_le hb with hb0 | hbpos
    · refine Or.inr ?_
      rw [hre', ← hb0]
      have ha1 : a = 1 := by linarith
      rw [ha1]
      constructor <;> norm_num
    · refine Or.inl ?_
      rw [him']
      exact mul_ne_zero (ne_of_gt hbpos) him
  · refine Or.inr ?_
    rw [hre']
    obtain ⟨h0, h1⟩ := hre
    have hbw : b * w.re ≤ b := by nlinarith
    have hbw0 : 0 ≤ b * w.re := mul_nonneg hb h0.le
    rcases eq_or_lt_of_le ha with ha0 | hapos
    · have hb1 : b = 1 := by linarith
      rw [← ha0, hb1]
      constructor <;> linarith
    · constructor <;> nlinarith

theorem isPreconnected_reflDomain : IsPreconnected reflDomain :=
  (starConvex_half_reflDomain.isPathConnected half_mem_reflDomain).isConnected.isPreconnected

theorem ball_half_subset_reflDomain :
    Metric.ball (1 / 2 : ℂ) (1 / 2) ⊆ reflDomain := by
  intro z hz
  rw [reflDomain_eq]
  exact ⟨mem_slitPlane_of_mem_ball_half hz,
    mem_slitPlane_of_mem_ball_half (one_sub_mem_ball_half hz)⟩

/-- Left-hand side plus the `log` product: analytic on `reflDomain`. -/
theorem analyticOnNhd_reflCombo :
    AnalyticOnNhd ℂ
      (fun z => cLiTwoExt z + cLiTwoExt (1 - z) + Complex.log z * Complex.log (1 - z))
      reflDomain := fun z hz =>
  ((analyticOnNhd_cLiTwoExt z (mem_notCut_of_mem_reflDomain hz)).add
      ((analyticOnNhd_cLiTwoExt (1 - z) (one_sub_mem_notCut_of_mem_reflDomain hz)).comp
        (analyticAt_const.sub analyticAt_id))).add
    ((analyticAt_clog (mem_slitPlane_of_mem_reflDomain hz)).mul
      (AnalyticAt.clog (analyticAt_const.sub analyticAt_id)
        (one_sub_mem_slitPlane_of_mem_reflDomain hz)))

/-- **The complex Euler reflection identity, on all of `ℂ ∖ ((−∞,0] ∪ [1,∞))`.**

    Li₂ z + Li₂ (1 − z) = π²/6 − log z · log (1 − z)

with `Li₂ = cLiTwoExt` and principal `log`. Continued from `ball(½,½)`
(`cLiTwo_reflection`) by the identity theorem. -/
theorem cLiTwoExt_reflection {z : ℂ} (hz : z ∈ reflDomain) :
    cLiTwoExt z + cLiTwoExt (1 - z)
      = (Real.pi : ℂ) ^ 2 / 6 - Complex.log z * Complex.log (1 - z) := by
  have hev : ∀ᶠ w in nhds (1 / 2 : ℂ),
      (fun w => cLiTwoExt w + cLiTwoExt (1 - w) + Complex.log w * Complex.log (1 - w)) w
        = (fun _ => (Real.pi : ℂ) ^ 2 / 6) w := by
    filter_upwards [Metric.ball_mem_nhds (1 / 2 : ℂ) (by norm_num : (0 : ℝ) < 1 / 2)]
      with w hw
    have h1 := cLiTwoExt_eq_cLiTwo (norm_lt_one_of_mem_ball_half hw)
    have h2 := cLiTwoExt_eq_cLiTwo (norm_lt_one_of_mem_ball_half (one_sub_mem_ball_half hw))
    have hr := cLiTwo_reflection hw
    simp only [h1, h2]
    linear_combination hr
  have heq := analyticOnNhd_reflCombo.eqOn_of_preconnected_of_frequently_eq
    (fun _ _ => analyticAt_const) isPreconnected_reflDomain half_mem_reflDomain
    (hev.filter_mono nhdsWithin_le_nhds).frequently hz
  beta_reduce at heq
  linear_combination heq

/-- Non-vacuity: the domain contains the 5₂ saddle root region — any non-real
point, e.g. `i`. -/
theorem I_mem_reflDomain : Complex.I ∈ reflDomain := Or.inl (by simp)

end QOU.Archimedean
