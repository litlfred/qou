import Mathlib.Analysis.Complex.RemovableSingularity
import Mathlib.Analysis.Complex.Liouville
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace QOU.Archimedean.BlochRigidity

open Complex Filter Topology

/-- **Proposition D3b (vanishing, pure complex analysis).** A function holomorphic on `ℂ ∖ {0,1}`,
symmetric under `z ↦ 1 - z`, with `F(1/z)·z = -F(z)`, and with `|F(z)| ≤ C/√|z|` near `0`,
vanishes. The growth bound removes the singularity at `0`, the symmetry removes the one at `1`,
the inversion law gives linear growth at `∞`, and Liouville finishes. -/
theorem eq_zero_of_symm_growth {F : ℂ → ℂ}
    (hd : DifferentiableOn ℂ F {0, 1}ᶜ)
    (hsym : ∀ z, z ≠ 0 → z ≠ 1 → F (1 - z) = F z)
    (hinv : ∀ z, z ≠ 0 → z ≠ 1 → F z⁻¹ * z = -F z)
    {r C : ℝ} (hr : 0 < r)
    (hC : ∀ z : ℂ, z ≠ 0 → ‖z‖ ≤ r → ‖F z‖ * Real.sqrt ‖z‖ ≤ C) :
    ∀ z, z ≠ 0 → z ≠ 1 → F z = 0 := by
  have hU : IsOpen ({0, 1}ᶜ : Set ℂ) := (Set.toFinite _).isClosed.isOpen_compl
  have hmem : ∀ {z : ℂ}, z ∈ ({0, 1}ᶜ : Set ℂ) ↔ z ≠ 0 ∧ z ≠ 1 := by simp
  have hdat : ∀ z, z ≠ 0 → z ≠ 1 → DifferentiableAt ℂ F z := fun z h0 h1 =>
    (hd z (hmem.2 ⟨h0, h1⟩)).differentiableAt (hU.mem_nhds (hmem.2 ⟨h0, h1⟩))
  -- step 1: `g z = z F z` is holomorphic on `{1}ᶜ`
  set g : ℂ → ℂ := fun z => z * F z with hgdef
  have h1o : ({1}ᶜ : Set ℂ) ∈ 𝓝 (0 : ℂ) :=
    isOpen_compl_singleton.mem_nhds (by norm_num)
  have hgc : ContinuousAt g 0 := by
    have hlim : Tendsto g (𝓝 0) (𝓝 0) := by
      refine squeeze_zero_norm' (a := fun z : ℂ => max C 0 * Real.sqrt ‖z‖) ?_ ?_
      · filter_upwards [Metric.closedBall_mem_nhds (0 : ℂ) hr] with z hz
        rw [Metric.mem_closedBall, dist_zero_right] at hz
        by_cases h0 : z = 0
        · simp [hgdef, h0]
        have hs : ‖z‖ = Real.sqrt ‖z‖ * Real.sqrt ‖z‖ :=
          (Real.mul_self_sqrt (norm_nonneg _)).symm
        calc ‖g z‖ = Real.sqrt ‖z‖ * (‖F z‖ * Real.sqrt ‖z‖) := by
                simp only [hgdef, norm_mul]; linear_combination ‖F z‖ * hs
          _ ≤ Real.sqrt ‖z‖ * max C 0 :=
                mul_le_mul_of_nonneg_left ((hC z h0 hz).trans (le_max_left _ _))
                  (Real.sqrt_nonneg _)
          _ = max C 0 * Real.sqrt ‖z‖ := by ring
      · have : Tendsto (fun z : ℂ => max C 0 * Real.sqrt ‖z‖) (𝓝 0)
            (𝓝 (max C 0 * Real.sqrt ‖(0 : ℂ)‖)) :=
          (continuous_const.mul (Real.continuous_sqrt.comp continuous_norm)).tendsto 0
        simpa using this
    simpa [ContinuousAt, hgdef] using hlim
  have hgd : DifferentiableOn ℂ g {1}ᶜ := by
    refine (differentiableOn_compl_singleton_and_continuousAt_iff h1o).1 ⟨?_, hgc⟩
    intro z hz
    simp only [Set.mem_diff, Set.mem_compl_iff, Set.mem_singleton_iff] at hz
    exact (differentiableAt_id.mul (hdat z hz.2 hz.1)).differentiableWithinAt
  -- step 2: `F₂ = dslope g 0` agrees with `F` off `0` and is holomorphic on `{1}ᶜ`
  set F2 : ℂ → ℂ := dslope g 0 with hF2
  have hF2d : DifferentiableOn ℂ F2 {1}ᶜ := (differentiableOn_dslope h1o).2 hgd
  have hF2eq : ∀ z, z ≠ 0 → F2 z = F z := by
    intro z hz
    rw [hF2, dslope_of_ne _ hz, slope_def_field]
    simp only [hgdef, zero_mul, sub_zero]
    field_simp
  have hF2c0 : ContinuousAt F2 0 := (hF2d.differentiableAt h1o).continuousAt
  -- step 3: remove the singularity at `1` by the symmetry
  set F3 : ℂ → ℂ := Function.update F2 1 (F2 0) with hF3
  have hF3eq : ∀ z, z ≠ 0 → z ≠ 1 → F3 z = F z := by
    intro z h0 h1; rw [hF3, Function.update_of_ne h1, hF2eq z h0]
  have hF3c1 : ContinuousAt F3 1 := by
    rw [hF3, continuousAt_update_same]
    have ht : Tendsto (fun z : ℂ => F2 (1 - z)) (𝓝[≠] 1) (𝓝 (F2 0)) := by
      have h0 : Tendsto (fun z : ℂ => 1 - z) (𝓝 1) (𝓝 0) := by
        have := ((continuous_sub_left (1 : ℂ)).tendsto (1 : ℂ))
        simpa using this
      exact (hF2c0.tendsto.comp h0).mono_left nhdsWithin_le_nhds
    refine ht.congr' ?_
    have hn : ∀ᶠ z in 𝓝[≠] (1 : ℂ), z ≠ 0 :=
      nhdsWithin_le_nhds ((isOpen_compl_singleton.mem_nhds (by norm_num : (1 : ℂ) ≠ 0)))
    filter_upwards [hn, self_mem_nhdsWithin] with z hz0 hz1
    have hz1' : z ≠ 1 := hz1
    have h10 : 1 - z ≠ 0 := sub_ne_zero.2 (Ne.symm hz1')
    rw [hF2eq _ h10, hF2eq _ hz0]
    exact hsym z hz0 hz1'
  have hF3d : Differentiable ℂ F3 := by
    have hu : (Set.univ : Set ℂ) ∈ 𝓝 (1 : ℂ) := Filter.univ_mem
    have hds : DifferentiableOn ℂ F3 (Set.univ \ {1}) := by
      intro z hz
      simp only [Set.mem_diff, Set.mem_univ, Set.mem_singleton_iff, true_and] at hz
      have hev : F3 =ᶠ[𝓝 z] F2 := by
        filter_upwards [isOpen_compl_singleton.mem_nhds hz] with w hw
        exact Function.update_of_ne hw _ _
      exact ((hF2d.differentiableAt (isOpen_compl_singleton.mem_nhds hz)).congr_of_eventuallyEq
        hev).differentiableWithinAt
    have := (differentiableOn_compl_singleton_and_continuousAt_iff (f := F3) hu).1 ⟨hds, hF3c1⟩
    exact fun z => (this z (Set.mem_univ z)).differentiableAt Filter.univ_mem
  -- step 4: `G z = F₃ z + z F₃(0)` is bounded, by the inversion law at `∞`
  have hF30 : F3 0 = F2 0 := Function.update_of_ne (by norm_num) _ _
  have hF31 : F3 1 = F2 0 := Function.update_self _ _ _
  obtain ⟨c, hc⟩ := ((hF3d 0).isBigO_sub).bound
  obtain ⟨ε, hε, hball⟩ := Metric.eventually_nhds_iff.1 hc
  set R : ℝ := max 2 (2 / ε) with hR
  set G : ℂ → ℂ := fun z => F3 z + z * F3 0 with hG
  have hGd : Differentiable ℂ G := hF3d.add (differentiable_id.mul (differentiable_const _))
  obtain ⟨B, hB⟩ := (isCompact_closedBall (0 : ℂ) R).exists_bound_of_continuousOn
    hGd.continuous.continuousOn
  have hbd : ∀ z, ‖G z‖ ≤ max B c := by
    intro z
    by_cases hz : ‖z‖ ≤ R
    · exact (hB z (by simpa using hz)).trans (le_max_left _ _)
    push_neg at hz
    have h2 : 2 < ‖z‖ := lt_of_le_of_lt (le_max_left _ _) hz
    have hzε : 2 / ε < ‖z‖ := lt_of_le_of_lt (le_max_right _ _) hz
    have hzpos : 0 < ‖z‖ := by linarith
    have hz0 : z ≠ 0 := norm_pos_iff.1 hzpos
    have hz1 : z ≠ 1 := by intro h; rw [h, norm_one] at h2; linarith
    have hi0 : z⁻¹ ≠ 0 := inv_ne_zero hz0
    have hi1 : z⁻¹ ≠ 1 := by
      intro h; have : z = 1 := by rw [← inv_inv z, h, inv_one]
      exact hz1 this
    have hni : ‖z⁻¹‖ = ‖z‖⁻¹ := norm_inv z
    have hiε : dist z⁻¹ 0 < ε := by
      rw [dist_zero_right, hni]
      rw [div_lt_iff₀ hε] at hzε
      rw [inv_lt_comm₀ hzpos hε]
      calc ε⁻¹ < 2 * ε⁻¹ := by have := inv_pos.2 hε; linarith
        _ = 2 / ε := by ring
        _ < ‖z‖ := by rw [div_lt_iff₀ hε]; linarith
    have hFz : F3 z = -z * F3 z⁻¹ := by
      have h := hinv z⁻¹ hi0 hi1
      rw [inv_inv] at h
      rw [hF3eq z hz0 hz1, hF3eq z⁻¹ hi0 hi1]
      field_simp at h ⊢
      linear_combination h
    have hGz : G z = -z * (F3 z⁻¹ - F3 0) := by simp only [hG, hFz]; ring
    have hb := hball hiε
    simp only [sub_zero] at hb
    calc ‖G z‖ = ‖z‖ * ‖F3 z⁻¹ - F3 0‖ := by rw [hGz, norm_mul, norm_neg]
      _ ≤ ‖z‖ * (c * ‖z⁻¹‖) := mul_le_mul_of_nonneg_left hb (norm_nonneg _)
      _ = c := by rw [hni]; field_simp
      _ ≤ max B c := le_max_right _ _
  have hbdd : Bornology.IsBounded (Set.range G) :=
    isBounded_iff_forall_norm_le.2 ⟨max B c, by rintro _ ⟨z, rfl⟩; exact hbd z⟩
  -- step 5: Liouville
  have hconst : ∀ z, G z = G 0 := fun z => hGd.apply_eq_apply_of_bounded hbdd z 0
  have hz0' : F3 0 = 0 := by
    have h := hconst 1
    simp only [hG, hF31, hF30, one_mul, zero_mul, add_zero] at h
    rw [hF30]; linear_combination h
  intro z h0 h1
  have h := hconst z
  simp only [hG, hz0', mul_zero, add_zero] at h
  rw [← hF3eq z h0 h1, h]

end QOU.Archimedean.BlochRigidity
