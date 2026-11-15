/-
  The Lobachevsky volume behaves like an entropic barrier at a face of the
  angle polytope.

  `Λ′(t) = −log(2 sin t)` blows up to `+∞` as `t → 0⁺`, and the curvature
  `−Λ″(t) = cot t` is squeezed against `1/t`: it is below `1/t` on `(0, π/2)`
  and `t · cot t → 1`.  `1/t` is the second derivative of the entropy
  `t log t`, so near a face `−Σ Λ(θᵢ)` has the Hessian of the entropic
  barrier `Σ θᵢ log θᵢ`.  This makes Rivin's volume ascent an entropy-regularised
  interior-point path on the angle LP — an analogy at the level of Hessians,
  not an identity with any particular central path.

  Archimedean (ℝ): real analysis of the real Lobachevsky function.

  -- Ref: [rivin1994] Euclidean structures on simplicial surfaces and hyperbolic volume
-/
import QOU.Knot.RivinConcavity

open Filter Topology Real

namespace QOU.Archimedean.LobBarrier

/-- `2 sin t → 0⁺` as `t → 0⁺`. -/
theorem tendsto_two_sin_nhdsGT :
    Tendsto (fun t : ℝ => 2 * Real.sin t) (𝓝[>] 0) (𝓝[>] 0) := by
  apply tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within
  · have h : Tendsto (fun t : ℝ => 2 * Real.sin t) (𝓝 0) (𝓝 (2 * Real.sin 0)) :=
      ((continuous_const.mul continuous_sin).tendsto 0)
    simpa using h.mono_left nhdsWithin_le_nhds
  · filter_upwards [Ioo_mem_nhdsGT Real.pi_pos] with t ht
    exact mul_pos two_pos (Real.sin_pos_of_pos_of_lt_pi ht.1 ht.2)

/-- **`−log(2 sin t) → +∞` as `t → 0⁺`.** -/
theorem tendsto_neg_log_two_sin_atTop :
    Tendsto (fun t : ℝ => -Real.log (2 * Real.sin t)) (𝓝[>] 0) atTop :=
  tendsto_neg_atBot_atTop.comp (Real.tendsto_log_nhdsGT_zero.comp tendsto_two_sin_nhdsGT)

/-- **The barrier property: `Λ′(t) → +∞` as `t → 0⁺`.**  The volume gradient
pushes every angle away from `0`, so the ascent never reaches a face from
inside. -/
theorem tendsto_deriv_Lob_atTop :
    Tendsto (deriv QOU.Archimedean.Lob) (𝓝[>] 0) atTop := by
  refine tendsto_neg_log_two_sin_atTop.congr' ?_
  filter_upwards [Ioo_mem_nhdsGT Real.pi_pos] with t ht
  exact ((QOU.Knot.Rivin.hasDerivAt_Lob ht.1 ht.2).deriv).symm

/-- `sin t / t → 1` as `t → 0⁺`. -/
theorem tendsto_sin_div_self :
    Tendsto (fun t : ℝ => Real.sin t / t) (𝓝[>] 0) (𝓝 1) := by
  have h := (Real.hasDerivAt_sin 0).tendsto_slope_zero
  simp only [zero_add, Real.sin_zero, sub_zero, Real.cos_zero, smul_eq_mul] at h
  have h' := h.mono_left (nhdsWithin_mono _ (fun t (ht : (0:ℝ) < t) => ht.ne'))
  refine h'.congr' (Eventually.of_forall fun t => ?_)
  simp [div_eq_inv_mul]

/-- **`t · cot t → 1` as `t → 0⁺`**: the curvature `−Λ″ = cot` is
asymptotic to `1/t`. -/
theorem tendsto_mul_cot :
    Tendsto (fun t : ℝ => t * Real.cot t) (𝓝[>] 0) (𝓝 1) := by
  have hinv : Tendsto (fun t : ℝ => (Real.sin t / t)⁻¹) (𝓝[>] 0) (𝓝 1) := by
    simpa using tendsto_sin_div_self.inv₀ one_ne_zero
  have hcos : Tendsto Real.cos (𝓝[>] (0:ℝ)) (𝓝 1) := by
    simpa using (Real.continuous_cos.tendsto 0).mono_left nhdsWithin_le_nhds
  have := hcos.mul hinv
  simp only [mul_one] at this
  refine this.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with t (ht : (0:ℝ) < t)
  rw [Real.cot_eq_cos_div_sin]
  field_simp

/-- **`cot t < 1/t` on `(0, π/2)`**, from `t < tan t`. -/
theorem cot_lt_inv {t : ℝ} (h0 : 0 < t) (h1 : t < π / 2) :
    Real.cot t < 1 / t := by
  have htan : t < Real.tan t := Real.lt_tan h0 h1
  have hpos : 0 < Real.tan t := h0.trans htan
  have hcot : Real.cot t = 1 / Real.tan t := by
    rw [Real.cot_eq_cos_div_sin, Real.tan_eq_sin_div_cos, one_div_div]
  rw [hcot]
  exact one_div_lt_one_div_of_lt h0 htan

/-- **The Hessian comparison.**  On `(0, π/2)` the curvature `−Λ″(t) = cot t`
is positive and strictly below `1/t`, the curvature of the entropy `t log t`. -/
theorem neg_deriv2_Lob_mem {t : ℝ} (h0 : 0 < t) (h1 : t < π / 2) :
    0 < -deriv (deriv QOU.Archimedean.Lob) t
      ∧ -deriv (deriv QOU.Archimedean.Lob) t < 1 / t := by
  have hπ : t < π := by linarith [Real.pi_pos]
  rw [QOU.Knot.Rivin.deriv_deriv_Lob h0 hπ, neg_neg]
  refine ⟨?_, cot_lt_inv h0 h1⟩
  rw [Real.cot_eq_cos_div_sin]
  exact div_pos (Real.cos_pos_of_mem_Ioo ⟨by linarith, h1⟩)
    (Real.sin_pos_of_pos_of_lt_pi h0 hπ)

end QOU.Archimedean.LobBarrier
