import QOU.Knot.WhiteheadMajorantRate
import QOU.Knot.WhiteheadWindowTaylor

/-!
# Whitehead tail decay (vdV Lemma 2b, quantitative) — bean qou-vy77

Quadratic decay of the van der Veen functional
`g(u,v) = clausen u + 2 clausen v − 2 clausen(u+v)` away from its saddle
`(π, π/2)`, by two one-dimensional monotone-split bricks.
-/

namespace QOU.Knot.WhiteheadInner

open Real QOU.Knot.FigureEightVolume

/-- Jordan, in the form used here: `(2/π) t ≤ sin t` on `[0, π/2]`. -/
theorem jordan {t : ℝ} (h0 : 0 ≤ t) (h1 : t ≤ π / 2) : 2 / π * t ≤ Real.sin t :=
  Real.mul_le_sin h0 h1

/-- The `v`-derivative of `g` is a log-sine ratio, and it is controlled linearly:
for `a = v/2 ≥ a* = π/2 − s/2`, `log(sin(a+s)/sin a) ≤ −(2/π) sin s (a − a*)`. -/
theorem log_ratio_le {a s : ℝ} (hs0 : 0 ≤ s) (hsπ : s ≤ π)
    (ha1 : π / 2 - s / 2 ≤ a) (ha2 : a < π - s) :
    Real.log (2 * Real.sin (a + s)) - Real.log (2 * Real.sin a)
      ≤ -(2 / π * Real.sin s * (a - (π / 2 - s / 2))) := by
  have hpi := Real.pi_pos
  have hsa : 0 < Real.sin a := Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hsas : 0 < Real.sin (a + s) := Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hsa1 : Real.sin a ≤ 1 := Real.sin_le_one a
  have hss : 0 ≤ Real.sin s := Real.sin_nonneg_of_nonneg_of_le_pi hs0 hsπ
  have hsh : 0 ≤ Real.sin (s / 2) := Real.sin_nonneg_of_nonneg_of_le_pi (by linarith) (by linarith)
  have hch : Real.cos (s / 2) ≤ 1 := Real.cos_le_one _
  have hss2 : Real.sin s ≤ 2 * Real.sin (s / 2) := by
    have h2 := Real.sin_two_mul (s / 2)
    rw [show 2 * (s / 2) = s by ring] at h2
    rw [h2]
    nlinarith
  -- sum to product
  have hdiff : Real.sin (a + s) - Real.sin a = 2 * Real.sin (s / 2) * Real.cos (a + s / 2) := by
    rw [Real.sin_sub_sin]
    rw [show (a + s - a) / 2 = s / 2 by ring, show (a + s + a) / 2 = a + s / 2 by ring]
  have hcos : Real.cos (a + s / 2) = -Real.sin (a - (π / 2 - s / 2)) := by
    rw [show a + s / 2 = (a - (π / 2 - s / 2)) + π / 2 by ring, Real.cos_add_pi_div_two]
  have hJ := jordan (t := a - (π / 2 - s / 2)) (by linarith) (by linarith)
  set d := a - (π / 2 - s / 2) with hd
  have hd0 : 0 ≤ d := by linarith
  have hnum : Real.sin (a + s) - Real.sin a ≤ -(Real.sin s * (2 / π * d)) := by
    rw [hdiff, hcos]
    have h1 : 0 ≤ 2 / π * d := by positivity
    nlinarith [mul_le_mul_of_nonneg_left hJ hsh, mul_le_mul_of_nonneg_right hss2 h1]
  rw [← Real.log_div (by positivity) (by positivity)]
  have hratio : 2 * Real.sin (a + s) / (2 * Real.sin a) = Real.sin (a + s) / Real.sin a := by
    field_simp
  rw [hratio]
  refine le_trans (Real.log_le_sub_one_of_pos (by positivity)) ?_
  rw [div_sub_one hsa.ne', div_le_iff₀ hsa]
  have hP : 0 ≤ Real.sin s * (2 / π * d) := by positivity
  nlinarith

/-- The mirror bound for `a ≤ a*`. -/
theorem log_ratio_ge {a s : ℝ} (hs0 : 0 ≤ s) (hsπ : s ≤ π)
    (ha1 : 0 < a) (ha2 : a ≤ π / 2 - s / 2) :
    2 / π * Real.sin s * ((π / 2 - s / 2) - a)
      ≤ Real.log (2 * Real.sin (a + s)) - Real.log (2 * Real.sin a) := by
  have hpi := Real.pi_pos
  have hsa : 0 < Real.sin a := Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hsas : 0 < Real.sin (a + s) := Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hsas1 : Real.sin (a + s) ≤ 1 := Real.sin_le_one _
  have hss : 0 ≤ Real.sin s := Real.sin_nonneg_of_nonneg_of_le_pi hs0 hsπ
  have hsh : 0 ≤ Real.sin (s / 2) := Real.sin_nonneg_of_nonneg_of_le_pi (by linarith) (by linarith)
  have hch : Real.cos (s / 2) ≤ 1 := Real.cos_le_one _
  have hss2 : Real.sin s ≤ 2 * Real.sin (s / 2) := by
    have h2 := Real.sin_two_mul (s / 2)
    rw [show 2 * (s / 2) = s by ring] at h2
    rw [h2]
    nlinarith
  have hdiff : Real.sin (a + s) - Real.sin a = 2 * Real.sin (s / 2) * Real.cos (a + s / 2) := by
    rw [Real.sin_sub_sin]
    rw [show (a + s - a) / 2 = s / 2 by ring, show (a + s + a) / 2 = a + s / 2 by ring]
  have hcos : Real.cos (a + s / 2) = Real.sin ((π / 2 - s / 2) - a) := by
    rw [← Real.cos_pi_div_two_sub]; congr 1; ring
  have hJ := jordan (t := (π / 2 - s / 2) - a) (by linarith) (by linarith)
  set d := (π / 2 - s / 2) - a with hd
  have hd0 : 0 ≤ d := by linarith
  have hnum : Real.sin s * (2 / π * d) ≤ Real.sin (a + s) - Real.sin a := by
    rw [hdiff, hcos]
    have h1 : 0 ≤ 2 / π * d := by positivity
    nlinarith [mul_le_mul_of_nonneg_left hJ hsh, mul_le_mul_of_nonneg_right hss2 h1]
  rw [← Real.log_div (by positivity) (by positivity)]
  have hratio : 2 * Real.sin (a + s) / (2 * Real.sin a) = Real.sin (a + s) / Real.sin a := by
    field_simp
  rw [hratio]
  -- log x ≥ 1 − 1/x
  have hlog : 1 - Real.sin a / Real.sin (a + s) ≤ Real.log (Real.sin (a + s) / Real.sin a) := by
    have h := Real.log_le_sub_one_of_pos (x := Real.sin a / Real.sin (a + s)) (by positivity)
    rw [Real.log_div hsa.ne' hsas.ne'] at h
    rw [Real.log_div hsas.ne' hsa.ne']
    linarith
  refine le_trans ?_ hlog
  rw [show 1 - Real.sin a / Real.sin (a + s) = (Real.sin (a + s) - Real.sin a) / Real.sin (a + s) by
    field_simp]
  rw [le_div_iff₀ hsas]
  have hP : 0 ≤ Real.sin s * (2 / π * d) := by positivity
  have : 2 / π * Real.sin s * d = Real.sin s * (2 / π * d) := by ring
  nlinarith

/-- **`v`-decay brick (vdV Lemma 2b, inner direction).**  For fixed `u ∈ [0, 2π]`,
`g(u, v) + (sin(u/2)/π)·(v − v*)² ≤ g(u, v*)` with `v* = π − u/2`. -/
theorem functional2_v_decay {u v : ℝ} (hu0 : 0 ≤ u) (hu : u ≤ 2 * π) (hv0 : 0 ≤ v)
    (huv : u + v ≤ 2 * π) :
    whiteheadFunctional2 u v + Real.sin (u / 2) / π * (v - (π - u / 2)) ^ 2
      ≤ whiteheadFunctional2 u (π - u / 2) := by
  have hpi := Real.pi_pos
  set c := Real.sin (u / 2) / π with hc
  set vs := π - u / 2 with hvs
  set φ : ℝ → ℝ := fun w => whiteheadFunctional2 u w + c * (w - vs) ^ 2 with hφ
  set φ' : ℝ → ℝ := fun w =>
    2 * (Real.log (2 * Real.sin ((u + w) / 2)) - Real.log (2 * Real.sin (w / 2)))
      + c * (2 * (w - vs)) with hφ'
  have hcont : Continuous φ := by
    simp only [hφ, whiteheadFunctional2]
    have := QOU.Knot.continuous_clausen
    fun_prop
  have hderiv : ∀ w ∈ Set.Ioo 0 (2 * π - u), HasDerivAt φ (φ' w) w := by
    intro w hw
    obtain ⟨hw0, hw1⟩ := hw
    have h1 := QOU.Knot.hasDerivAt_clausen (θ := w) hw0 (by linarith)
    have h2 := (QOU.Knot.hasDerivAt_clausen (θ := u + w) (by linarith) (by linarith)).comp w
      ((hasDerivAt_id w).const_add u)
    have h3 : HasDerivAt (fun w : ℝ => c * (w - vs) ^ 2) (c * (2 * (w - vs))) w := by
      have := ((hasDerivAt_id w).sub_const vs).pow 2
      simpa using this.const_mul c
    have hsum := ((h1.const_mul 2).const_add (clausen u)).sub (h2.const_mul 2) |>.add h3
    convert hsum using 1
    simp only [hφ']
    ring
  have hφ'_def : ∀ w, φ' w = 2 * (Real.log (2 * Real.sin (w / 2 + u / 2))
      - Real.log (2 * Real.sin (w / 2))) + c * (2 * (w - vs)) := by
    intro w; simp only [hφ']; ring_nf
  have hvs0 : 0 ≤ vs := by simp only [hvs]; linarith
  have hvs1 : vs ≤ 2 * π - u := by simp only [hvs]; linarith
  rcases le_total v vs with hle | hge
  · -- monotone on [0, vs]
    have hmono : MonotoneOn φ (Set.Icc 0 vs) := by
      refine monotoneOn_of_deriv_nonneg (convex_Icc 0 vs) hcont.continuousOn ?_ ?_
      · rw [interior_Icc]; intro w hw
        exact (hderiv w ⟨hw.1, by linarith [hw.2]⟩).differentiableAt.differentiableWithinAt
      · rw [interior_Icc]; intro w hw
        rw [(hderiv w ⟨hw.1, by linarith [hw.2]⟩).deriv, hφ'_def]
        have hl := log_ratio_ge (a := w / 2) (s := u / 2) (by linarith) (by linarith)
          (by linarith [hw.1]) (by simp only [hvs] at hw; linarith [hw.2])
        have : c * (2 * (w - vs)) = -(2 / π * Real.sin (u / 2) * (π / 2 - u / 2 / 2 - w / 2)) * 2 := by
          simp only [hc, hvs]; field_simp; try ring
        rw [this]
        linarith
    have := hmono ⟨hv0, hle⟩ ⟨hvs0, le_refl vs⟩ hle
    simpa [hφ] using this
  · have hanti : AntitoneOn φ (Set.Icc vs (2 * π - u)) := by
      refine antitoneOn_of_deriv_nonpos (convex_Icc _ _) hcont.continuousOn ?_ ?_
      · rw [interior_Icc]; intro w hw
        exact (hderiv w ⟨by linarith [hw.1], hw.2⟩).differentiableAt.differentiableWithinAt
      · rw [interior_Icc]; intro w hw
        rw [(hderiv w ⟨by linarith [hw.1], hw.2⟩).deriv, hφ'_def]
        have hl := log_ratio_le (a := w / 2) (s := u / 2) (by linarith) (by linarith)
          (by simp only [hvs] at hw; linarith [hw.1]) (by linarith [hw.2])
        have : c * (2 * (w - vs)) = (2 / π * Real.sin (u / 2) * (w / 2 - (π / 2 - u / 2 / 2))) * 2 := by
          simp only [hc, hvs]; field_simp; try ring
        rw [this]
        linarith
    have := hanti ⟨le_refl vs, hvs1⟩ ⟨hge, by linarith⟩ hge
    simpa [hφ] using this

theorem cos_sub_sin_eq (t : ℝ) :
    Real.cos t - Real.sin t = -(2 * Real.sin (π / 4)) * Real.sin (t - π / 4) := by
  rw [← Real.cos_pi_div_two_sub t, Real.cos_sub_cos]
  rw [show (t + (π / 2 - t)) / 2 = π / 4 by ring, show (t - (π / 2 - t)) / 2 = t - π / 4 by ring]
  ring

theorem one_le_two_sin_pi_div_four : 1 ≤ 2 * Real.sin (π / 4) := by
  rw [Real.sin_pi_div_four]
  have h : (1 : ℝ) ≤ √2 := by
    rw [show (1 : ℝ) = √1 by simp]; exact Real.sqrt_le_sqrt (by norm_num)
  linarith

/-- `log cot t ≤ −(2/π)(t − π/4)` on `[π/4, π/2)`. -/
theorem log_cot_le {t : ℝ} (h1 : π / 4 ≤ t) (h2 : t < π / 2) :
    Real.log (Real.cos t) - Real.log (Real.sin t) ≤ -(2 / π * (t - π / 4)) := by
  have hpi := Real.pi_pos
  have hs : 0 < Real.sin t := Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hc : 0 < Real.cos t := Real.cos_pos_of_mem_Ioo ⟨by linarith, h2⟩
  have hs1 : Real.sin t ≤ 1 := Real.sin_le_one t
  have hJ := jordan (t := t - π / 4) (by linarith) (by linarith)
  have hJ0 : 0 ≤ 2 / π * (t - π / 4) := by
    have : 0 ≤ t - π / 4 := by linarith
    positivity
  have h2s := one_le_two_sin_pi_div_four
  have hcs : Real.cos t - Real.sin t ≤ -(2 / π * (t - π / 4)) := by
    rw [cos_sub_sin_eq]
    nlinarith [mul_le_mul_of_nonneg_left hJ (by linarith : (0:ℝ) ≤ 2 * Real.sin (π / 4))]
  rw [← Real.log_div hc.ne' hs.ne']
  refine le_trans (Real.log_le_sub_one_of_pos (by positivity)) ?_
  rw [div_sub_one hs.ne', div_le_iff₀ hs]
  nlinarith

/-- `log cot t ≥ (2/π)(π/4 − t)` on `(0, π/4]`. -/
theorem log_cot_ge {t : ℝ} (h1 : 0 < t) (h2 : t ≤ π / 4) :
    2 / π * (π / 4 - t) ≤ Real.log (Real.cos t) - Real.log (Real.sin t) := by
  have hpi := Real.pi_pos
  have hs : 0 < Real.sin t := Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hc : 0 < Real.cos t := Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
  have hc1 : Real.cos t ≤ 1 := Real.cos_le_one t
  have hJ := jordan (t := π / 4 - t) (by linarith) (by linarith)
  have hJ0 : 0 ≤ 2 / π * (π / 4 - t) := by
    have : 0 ≤ π / 4 - t := by linarith
    positivity
  have h2s := one_le_two_sin_pi_div_four
  have hcs : 2 / π * (π / 4 - t) ≤ Real.cos t - Real.sin t := by
    rw [cos_sub_sin_eq, show t - π / 4 = -(π / 4 - t) by ring, Real.sin_neg]
    nlinarith [mul_le_mul_of_nonneg_left hJ (by linarith : (0:ℝ) ≤ 2 * Real.sin (π / 4))]
  have hlog : 1 - Real.sin t / Real.cos t ≤ Real.log (Real.cos t) - Real.log (Real.sin t) := by
    have h := Real.log_le_sub_one_of_pos (x := Real.sin t / Real.cos t) (by positivity)
    rw [Real.log_div hs.ne' hc.ne'] at h
    linarith
  refine le_trans ?_ hlog
  rw [show 1 - Real.sin t / Real.cos t = (Real.cos t - Real.sin t) / Real.cos t by field_simp,
    le_div_iff₀ hc]
  nlinarith

/-- The centre-line profile `h(u) = g(u, π − u/2)` in closed form. -/
theorem centre_profile_eq (u : ℝ) :
    whiteheadFunctional2 u (π - u / 2)
      = clausen u + 2 * clausen (π - u / 2) - 2 * clausen (π + u / 2) := by
  unfold whiteheadFunctional2
  rw [show u + (π - u / 2) = π + u / 2 by ring]

/-- **`u`-decay brick (vdV Lemma 2b, outer direction).**  On `[0, 2π]` the centre-line
profile satisfies `h(u) + (u − π)²/(4π) ≤ h(π) = 4·clausen(π/2)`. -/
theorem centre_profile_decay {u : ℝ} (hu0 : 0 ≤ u) (hu : u ≤ 2 * π) :
    whiteheadFunctional2 u (π - u / 2) + (u - π) ^ 2 / (4 * π) ≤ 4 * clausen (π / 2) := by
  have hpi := Real.pi_pos
  set ψ : ℝ → ℝ := fun w => clausen w + 2 * clausen (π - w / 2) - 2 * clausen (π + w / 2)
    + (w - π) ^ 2 / (4 * π) with hψ
  set ψ' : ℝ → ℝ := fun w => (Real.log (Real.cos (w / 4)) - Real.log (Real.sin (w / 4)))
    + (w - π) / (2 * π) with hψ'
  have hcont : Continuous ψ := by
    simp only [hψ]
    have := QOU.Knot.continuous_clausen
    fun_prop
  have hderiv : ∀ w ∈ Set.Ioo 0 (2 * π), HasDerivAt ψ (ψ' w) w := by
    intro w hw
    obtain ⟨hw0, hw1⟩ := hw
    have h1 := QOU.Knot.hasDerivAt_clausen (θ := w) hw0 hw1
    have h2 := (QOU.Knot.hasDerivAt_clausen (θ := π - w / 2) (by linarith) (by linarith)).comp w
      (((hasDerivAt_id w).div_const 2).const_sub π)
    have h3 := (QOU.Knot.hasDerivAt_clausen (θ := π + w / 2) (by linarith) (by linarith)).comp w
      (((hasDerivAt_id w).div_const 2).const_add π)
    have h4 : HasDerivAt (fun w : ℝ => (w - π) ^ 2 / (4 * π)) ((w - π) / (2 * π)) w := by
      have := (((hasDerivAt_id w).sub_const π).pow 2).div_const (4 * π)
      convert this using 1
      simp; field_simp; ring
    have hsum := ((h1.add (h2.const_mul 2)).sub (h3.const_mul 2)).add h4
    convert hsum using 1
    · -- the derivative value
      simp only [hψ']
      have hc : 0 < Real.cos (w / 4) := Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
      have hs : 0 < Real.sin (w / 4) := Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
      have e1 : Real.sin ((π - w / 2) / 2) = Real.cos (w / 4) := by
        rw [show (π - w / 2) / 2 = π / 2 - w / 4 by ring, Real.sin_pi_div_two_sub]
      have e2 : Real.sin ((π + w / 2) / 2) = Real.cos (w / 4) := by
        rw [show (π + w / 2) / 2 = w / 4 + π / 2 by ring, Real.sin_add_pi_div_two]
      have e3 : Real.sin (w / 2) = 2 * Real.sin (w / 4) * Real.cos (w / 4) := by
        rw [show w / 2 = 2 * (w / 4) by ring, Real.sin_two_mul]
      rw [e1, e2, e3]
      rw [Real.log_mul (by norm_num) hc.ne',
        show 2 * (2 * Real.sin (w / 4) * Real.cos (w / 4))
          = 4 * (Real.sin (w / 4) * Real.cos (w / 4)) by ring,
        Real.log_mul (by norm_num) (by positivity), Real.log_mul hs.ne' hc.ne',
        show (4 : ℝ) = 2 * 2 by norm_num, Real.log_mul (by norm_num) (by norm_num)]
      ring
  have hψπ : ψ π = 4 * clausen (π / 2) := by
    have h := whiteheadFunctional2_saddle
    have h' := centre_profile_eq π
    rw [show π - π / 2 = π / 2 by ring] at h'
    rw [h'] at h
    simp only [hψ, sub_self]
    rw [show (0 : ℝ) ^ 2 / (4 * π) = 0 by simp, show π - π / 2 = π / 2 by ring]
    linarith
  have hgoal : ψ u ≤ ψ π := by
    rcases le_total u π with hle | hge
    · have hmono : MonotoneOn ψ (Set.Icc 0 π) := by
        refine monotoneOn_of_deriv_nonneg (convex_Icc 0 π) hcont.continuousOn ?_ ?_
        · rw [interior_Icc]; intro w hw
          exact (hderiv w ⟨hw.1, by linarith [hw.2]⟩).differentiableAt.differentiableWithinAt
        · rw [interior_Icc]; intro w hw
          rw [(hderiv w ⟨hw.1, by linarith [hw.2]⟩).deriv]
          have := log_cot_ge (t := w / 4) (by linarith [hw.1]) (by linarith [hw.2])
          simp only [hψ']
          have e : 2 / π * (π / 4 - w / 4) = -((w - π) / (2 * π)) := by field_simp; ring
          linarith
      exact hmono ⟨hu0, hle⟩ ⟨by linarith, le_refl π⟩ hle
    · have hanti : AntitoneOn ψ (Set.Icc π (2 * π)) := by
        refine antitoneOn_of_deriv_nonpos (convex_Icc _ _) hcont.continuousOn ?_ ?_
        · rw [interior_Icc]; intro w hw
          exact (hderiv w ⟨by linarith [hw.1], hw.2⟩).differentiableAt.differentiableWithinAt
        · rw [interior_Icc]; intro w hw
          rw [(hderiv w ⟨by linarith [hw.1], hw.2⟩).deriv]
          have := log_cot_le (t := w / 4) (by linarith [hw.1]) (by linarith [hw.2])
          simp only [hψ']
          have e : 2 / π * (w / 4 - π / 4) = (w - π) / (2 * π) := by field_simp; ring
          linarith
      exact hanti ⟨le_refl π, by linarith⟩ ⟨hge, hu⟩ hge
  rw [centre_profile_eq]
  rw [← hψπ]
  simpa [hψ] using hgoal

/-- **Global quadratic decay of the van der Veen functional** (vdV Lemma 2b). -/
theorem functional2_decay {u v : ℝ} (hu0 : 0 ≤ u) (hv0 : 0 ≤ v) (huv : u + v ≤ 2 * π) :
    whiteheadFunctional2 u v + (u - π) ^ 2 / (4 * π)
        + Real.sin (u / 2) / π * (v - (π - u / 2)) ^ 2 ≤ 4 * clausen (π / 2) := by
  have h1 := functional2_v_decay hu0 (by linarith) hv0 huv
  have h2 := centre_profile_decay hu0 (by linarith)
  linarith

/-- **Grid ceiling at the functional, all grid points.**  For `n + k ≤ N − 1`,
`(2π/N) log S_{n,k} ≤ g(2nπ/N, 2kπ/N) + 10·masterErr N` (boundary rows included). -/
theorem two_pi_log_whiteheadTerm_le_functional {N n k : ℕ} (hN : 4 ≤ N) (hnk : n + k ≤ N - 1) :
    (2 * π / N) * Real.log (whiteheadTerm N n k)
      ≤ whiteheadFunctional2 (2 * ((n : ℝ) * (π / N))) (2 * ((k : ℝ) * (π / N)))
        + 10 * masterErr N := by
  have hme := masterErr_nonneg N
  rcases Nat.eq_zero_or_pos n with hn0 | hn1
  · subst hn0
    rw [whiteheadTerm_zero_left, Real.log_one, mul_zero]
    unfold whiteheadFunctional2
    simp
    linarith
  rcases Nat.eq_zero_or_pos k with hk0 | hk1
  · subst hk0
    have hdev := abs_deviation_le_masterErr (N := N) (k := n) hN (by omega) (by omega)
    rw [abs_le] at hdev
    have hlogT := log_whiteheadTerm (N := N) (M := n) (k := 0) (by omega)
    have hS0 : ∑ j ∈ Finset.Icc (1:ℕ) 0,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))) = 0 := by
      rw [Finset.Icc_eq_empty (by omega : ¬(1:ℕ) ≤ 0)]
      exact Finset.sum_empty
    have hlogT' : Real.log (whiteheadTerm N n 0)
        = ∑ j ∈ Finset.Icc 1 n, Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
      rw [hlogT, hS0]
      simp only [Nat.zero_add]
      ring
    unfold whiteheadFunctional2
    simp only [Nat.cast_zero, zero_mul, mul_zero, clausen_zero, add_zero]
    rw [hlogT']
    have : (2 * π / N) * ∑ j ∈ Finset.Icc 1 n, Real.log (2 * Real.sin ((j : ℝ) * (π / N)))
        = 2 * ((π / N) * ∑ j ∈ Finset.Icc 1 n, Real.log (2 * Real.sin ((j : ℝ) * (π / N)))) := by
      ring
    rw [this]
    linarith [hdev.2]
  · have hdev := abs_log_whiteheadTerm_deviation (N := N) (M := n) (k := k)
      hN hn1 hk1 (by omega)
    rw [abs_le] at hdev
    have hpsi : 2 * (2 * ((-clausen (2 * (((k:ℝ) + (n:ℝ)) * (π / N))) / 2)
            - (-clausen (2 * ((k:ℝ) * (π / N))) / 2))
         - (-clausen (2 * ((n:ℝ) * (π / N))) / 2))
        = whiteheadFunctional2 (2 * ((n:ℝ) * (π / N))) (2 * ((k:ℝ) * (π / N))) := by
      unfold whiteheadFunctional2
      rw [show 2 * ((n:ℝ) * (π / N)) + 2 * ((k:ℝ) * (π / N))
          = 2 * (((k:ℝ) + (n:ℝ)) * (π / N)) by ring]
      ring
    rw [← hpsi]
    have : (2 * π / N) * Real.log (whiteheadTerm N n k)
        = 2 * ((π / N) * Real.log (whiteheadTerm N n k)) := by ring
    rw [this]
    linarith [hdev.2]

/-- Lower bound at the grid point `(⌊N/2⌋, ⌊N/4⌋)`: `(2π/N) log S ≥ g(u₀,v₀) − 10·masterErr`. -/
theorem functional_le_two_pi_log_centre {N : ℕ} (hN : 4 ≤ N) :
    whiteheadFunctional2 (2 * (((N / 2 : ℕ) : ℝ) * (π / N))) (2 * (((N / 4 : ℕ) : ℝ) * (π / N)))
        - 10 * masterErr N
      ≤ (2 * π / N) * Real.log (whiteheadTerm N (N / 2) (N / 4)) := by
  have hdev := abs_log_whiteheadTerm_deviation (N := N) (M := N / 2) (k := N / 4)
    hN (by omega) (by omega) (by omega)
  rw [abs_le] at hdev
  have hpsi : 2 * (2 * ((-clausen (2 * ((((N / 4 : ℕ) : ℝ) + ((N / 2 : ℕ) : ℝ)) * (π / N))) / 2)
          - (-clausen (2 * (((N / 4 : ℕ) : ℝ) * (π / N))) / 2))
       - (-clausen (2 * (((N / 2 : ℕ) : ℝ) * (π / N))) / 2))
      = whiteheadFunctional2 (2 * (((N / 2 : ℕ) : ℝ) * (π / N)))
          (2 * (((N / 4 : ℕ) : ℝ) * (π / N))) := by
    unfold whiteheadFunctional2
    rw [show 2 * (((N / 2 : ℕ) : ℝ) * (π / N)) + 2 * (((N / 4 : ℕ) : ℝ) * (π / N))
        = 2 * ((((N / 4 : ℕ) : ℝ) + ((N / 2 : ℕ) : ℝ)) * (π / N)) by ring]
    ring
  rw [← hpsi]
  have : (2 * π / N) * Real.log (whiteheadTerm N (N / 2) (N / 4))
      = 2 * ((π / N) * Real.log (whiteheadTerm N (N / 2) (N / 4))) := by ring
  rw [this]
  linarith [hdev.1]

theorem abs_sub_le_of_hasDerivAt {f f' : ℝ → ℝ} {a b C : ℝ}
    (hd : ∀ x ∈ Set.uIcc a b, HasDerivAt f (f' x) x) (hb : ∀ x ∈ Set.uIcc a b, |f' x| ≤ C) :
    |f b - f a| ≤ C * |b - a| := by
  have h := Convex.norm_image_sub_le_of_norm_hasDerivWithin_le
    (fun x hx => (hd x hx).hasDerivWithinAt) (fun x hx => by rw [Real.norm_eq_abs]; exact hb x hx)
    (convex_uIcc a b) Set.left_mem_uIcc Set.right_mem_uIcc
  simpa [Real.norm_eq_abs] using h

theorem log_two_sin_mem {θ : ℝ} (h1 : π / 6 ≤ θ) (h2 : θ ≤ 5 * π / 6) :
    0 ≤ Real.log (2 * Real.sin θ) ∧ Real.log (2 * Real.sin θ) ≤ 1 := by
  have hs := sin_ge_half h1 h2
  have hs1 := Real.sin_le_one θ
  constructor
  · exact Real.log_nonneg (by linarith)
  · have : Real.log (2 * Real.sin θ) ≤ Real.log 2 := Real.log_le_log (by linarith) (by linarith)
    have := Real.log_lt_sub_one_of_pos (x := 2) (by norm_num) (by norm_num)
    linarith

/-- **Saddle Lipschitz brick (generic).** -/
theorem functional_near_saddle_ge {u0 v0 h : ℝ} (hh0 : 0 ≤ h) (hh12 : h ≤ π / 24)
    (hu0π : |u0 - π| ≤ 2 * h) (hv0π : |v0 - π / 2| ≤ 2 * h) :
    4 * clausen (π / 2) - 8 * h ≤ whiteheadFunctional2 u0 v0 := by
  have hpi := Real.pi_pos
  obtain ⟨hu1, hu2⟩ := abs_le.mp hu0π
  obtain ⟨hv1, hv2⟩ := abs_le.mp hv0π
  have hA : |whiteheadFunctional2 π (π / 2) - whiteheadFunctional2 π v0| ≤ 2 * |π / 2 - v0| := by
    refine abs_sub_le_of_hasDerivAt (f := fun v => whiteheadFunctional2 π v)
      (f' := fun v => 2 * -Real.log (2 * Real.sin (v / 2))
        - 2 * (-Real.log (2 * Real.sin ((π + v) / 2)) * 1)) ?_ ?_
    · intro v hv
      have hvr : π / 2 - 2 * h ≤ v ∧ v ≤ π / 2 + 2 * h := by
        rcases Set.mem_uIcc.mp hv with h' | h' <;> constructor <;> linarith [h'.1, h'.2]
      have h1 := QOU.Knot.hasDerivAt_clausen (θ := v) (by linarith) (by linarith)
      have h2 := (QOU.Knot.hasDerivAt_clausen (θ := π + v) (by linarith) (by linarith)).comp v
        ((hasDerivAt_id v).const_add π)
      have := ((h1.const_mul 2).const_add (clausen π)).sub (h2.const_mul 2)
      simpa [whiteheadFunctional2, Function.comp_def] using this
    · intro v hv
      have hvr : π / 2 - 2 * h ≤ v ∧ v ≤ π / 2 + 2 * h := by
        rcases Set.mem_uIcc.mp hv with h' | h' <;> constructor <;> linarith [h'.1, h'.2]
      have hA1 := log_two_sin_mem (θ := v / 2) (by linarith) (by linarith)
      have hA2 := log_two_sin_mem (θ := (π + v) / 2) (by linarith) (by linarith)
      rw [abs_le]; constructor <;> linarith
  have hB : |whiteheadFunctional2 π v0 - whiteheadFunctional2 u0 v0| ≤ 2 * |π - u0| := by
    refine abs_sub_le_of_hasDerivAt (f := fun u => whiteheadFunctional2 u v0)
      (f' := fun u => -Real.log (2 * Real.sin (u / 2))
        - 2 * (-Real.log (2 * Real.sin ((u + v0) / 2)) * 1)) ?_ ?_
    · intro u hu
      have hur : π - 2 * h ≤ u ∧ u ≤ π + 2 * h := by
        rcases Set.mem_uIcc.mp hu with h' | h' <;> constructor <;> linarith [h'.1, h'.2]
      have h1 := QOU.Knot.hasDerivAt_clausen (θ := u) (by linarith) (by linarith)
      have h2 := (QOU.Knot.hasDerivAt_clausen (θ := u + v0) (by linarith) (by linarith)).comp u
        ((hasDerivAt_id u).add_const v0)
      have := (h1.add_const (2 * clausen v0)).sub (h2.const_mul 2)
      simpa [whiteheadFunctional2, Function.comp_def] using this
    · intro u hu
      have hur : π - 2 * h ≤ u ∧ u ≤ π + 2 * h := by
        rcases Set.mem_uIcc.mp hu with h' | h' <;> constructor <;> linarith [h'.1, h'.2]
      have hB1 := log_two_sin_mem (θ := u / 2) (by linarith) (by linarith)
      have hB2 := log_two_sin_mem (θ := (u + v0) / 2) (by linarith) (by linarith)
      rw [abs_le]; constructor <;> linarith
  have hsad := whiteheadFunctional2_saddle
  have e1 : |π / 2 - v0| ≤ 2 * h := by rw [abs_sub_comm]; exact hv0π
  have e2 : |π - u0| ≤ 2 * h := by rw [abs_sub_comm]; exact hu0π
  have hA' := (abs_le.mp hA).2
  have hB' := (abs_le.mp hB).2
  linarith

/-- **Saddle Lipschitz brick.** `g(u₀,v₀) ≥ 4·clausen(π/2) − 8π/N` at the grid saddle. -/
theorem functional_centre_ge {N : ℕ} (hN : 24 ≤ N) :
    4 * clausen (π / 2) - 8 * (π / N)
      ≤ whiteheadFunctional2 (2 * (((N / 2 : ℕ) : ℝ) * (π / N)))
          (2 * (((N / 4 : ℕ) : ℝ) * (π / N))) := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  have hN24 : (24 : ℝ) ≤ N := by exact_mod_cast hN
  have hh12 : π / N ≤ π / 24 := by
    rw [div_le_div_iff₀ hNpos (by norm_num)]; nlinarith
  have hn0 := abs_div_two_sub_le N
  have hk0 := abs_div_four_sub_le N
  refine functional_near_saddle_ge (by positivity) hh12 ?_ ?_
  · have : 2 * (((N / 2 : ℕ) : ℝ) * (π / N)) - π = 2 * (π / N) * (((N / 2 : ℕ) : ℝ) - N / 2) := by
      field_simp; try ring
    rw [this, abs_mul, abs_of_pos (by positivity)]
    nlinarith [div_pos hpi hNpos]
  · have : 2 * (((N / 4 : ℕ) : ℝ) * (π / N)) - π / 2 = 2 * (π / N) * (((N / 4 : ℕ) : ℝ) - N / 4) := by
      field_simp; try ring
    rw [this, abs_mul, abs_of_pos (by positivity)]
    nlinarith [div_pos hpi hNpos]

end QOU.Knot.WhiteheadInner
