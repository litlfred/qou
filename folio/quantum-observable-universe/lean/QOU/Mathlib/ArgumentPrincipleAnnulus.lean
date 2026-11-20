import QOU.Mathlib.ArgumentPrinciple

/-!
# QOU.Mathlib.ArgumentPrincipleAnnulus — the argument principle on an annulus

Step 2 of the annulus route to Liouville's third theorem (bean `qou-z4jb`).
`argument_principle_annulus` counts zeros minus poles, with integer orders, of a
function meromorphic on the closed annulus `r ≤ ‖z‖ ≤ R` as the difference of
the outer and inner circle integrals of `f'/f`, divided by `2πi`.

It generalises two things already in the corpus: the disc version
`QOU.Mathlib.ArgumentPrinciple.argument_principle` (same factorisation proof),
and the `ℕ`-multiplicity annulus lemmas in `QOU.QBeta.C1ConnectionPoles`, which
handle zeros only. Poles are needed for elliptic functions. Two small supporting
facts are proved here: the closed annulus is connected, and every point of a
boundary circle is an accumulation point of the annulus. Sorry-free.
-/

open Filter Topology Complex Metric

namespace QOU.Mathlib.ArgumentPrincipleAnnulus

/-- The closed annulus `r ≤ ‖z‖ ≤ R` (centre `0`). -/
def closedAnnulus (r R : ℝ) : Set ℂ := closedBall (0 : ℂ) R \ ball (0 : ℂ) r

theorem mem_closedAnnulus {r R : ℝ} {z : ℂ} :
    z ∈ closedAnnulus r R ↔ r ≤ ‖z‖ ∧ ‖z‖ ≤ R := by
  simp [closedAnnulus, mem_closedBall, mem_ball, dist_zero_right, and_comm]

theorem isCompact_closedAnnulus (r R : ℝ) : IsCompact (closedAnnulus r R) :=
  (isCompact_closedBall _ _).diff isOpen_ball

/-- The closed annulus is the image of `[r, R] × ℝ` under `(s, θ) ↦ s·e^{iθ}`,
hence connected. -/
theorem isConnected_closedAnnulus {r R : ℝ} (hr : 0 < r) (hrR : r ≤ R) :
    IsConnected (closedAnnulus r R) := by
  have hc : IsConnected (Set.Icc r R ×ˢ (Set.univ : Set ℝ)) :=
    (isConnected_Icc hrR).prod isConnected_univ
  have himg : (fun p : ℝ × ℝ => (p.1 : ℂ) * exp (p.2 * I)) ''
      (Set.Icc r R ×ˢ Set.univ) = closedAnnulus r R := by
    ext z
    constructor
    · rintro ⟨⟨s, θ⟩, ⟨⟨hs1, hs2⟩, -⟩, rfl⟩
      rw [mem_closedAnnulus, norm_mul, norm_exp_ofReal_mul_I, mul_one, Complex.norm_real,
        Real.norm_eq_abs, abs_of_pos (lt_of_lt_of_le hr hs1)]
      exact ⟨hs1, hs2⟩
    · intro hz
      rw [mem_closedAnnulus] at hz
      exact ⟨⟨‖z‖, arg z⟩, ⟨hz, trivial⟩, by simp⟩
  rw [← himg]
  exact hc.image _ (by fun_prop)

/-- Every point of a circle of positive radius is an accumulation point of any
set containing that circle (rotate it by a small angle). -/
theorem accPt_of_sphere_subset {ρ : ℝ} (hρ : 0 < ρ) {K : Set ℂ}
    (hK : sphere (0 : ℂ) ρ ⊆ K) {z : ℂ} (hz : ‖z‖ = ρ) : AccPt z (𝓟 K) := by
  rw [accPt_iff_frequently]
  have hz0 : z ≠ 0 := by
    intro h; rw [h, norm_zero] at hz; linarith
  set φ : ℝ → ℂ := fun θ => z * exp (θ * I) with hφ
  have hT : Tendsto φ (𝓝[≠] (0 : ℝ)) (𝓝 z) := by
    have : Continuous φ := by fun_prop
    have h0 : φ 0 = z := by simp [hφ]
    exact (h0 ▸ this.tendsto 0).mono_left nhdsWithin_le_nhds
  apply hT.frequently
  apply Eventually.frequently
  have hball : ∀ᶠ θ in 𝓝[≠] (0 : ℝ), θ ∈ Set.Ioo (-1 : ℝ) 1 :=
    nhdsWithin_le_nhds (Ioo_mem_nhds (by norm_num) (by norm_num))
  filter_upwards [hball, self_mem_nhdsWithin] with θ hθ hθ0
  refine ⟨?_, hK ?_⟩
  · intro h
    have h1 : exp (θ * I) = 1 := by
      have := congrArg (fun w => w / z) h
      simpa [hφ, hz0] using this
    obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.mp h1
    have hre : θ = n * (2 * Real.pi) := by
      have := congrArg Complex.im hn
      simpa using this
    have hn0 : n = 0 := by
      have hpi : (2 : ℝ) ≤ Real.pi := Real.two_le_pi
      rcases lt_trichotomy n 0 with h | h | h
      · have : (n : ℝ) ≤ -1 := by exact_mod_cast Int.le_sub_one_of_lt h
        nlinarith [hθ.1]
      · exact h
      · have : (1 : ℝ) ≤ n := by exact_mod_cast h
        nlinarith [hθ.2]
    exact hθ0 (by rw [hre, hn0]; simp)
  · rw [mem_sphere, dist_zero_right, hφ, norm_mul, norm_exp_ofReal_mul_I, mul_one, hz]

open QOU.Mathlib.ArgumentPrinciple in
/-- **The argument principle on an annulus, with integer orders.** For `f`
meromorphic on the closed annulus `K = {r ≤ ‖z‖ ≤ R}`, analytic and nonvanishing
on `K` off a finite set `S` of points strictly inside, with `S` exactly the
interior points where the divisor is nonzero,

`(2πi)⁻¹ (∮_{|z|=R} f'/f − ∮_{|z|=r} f'/f) = Σ_{w∈S} ord_w f`.

Same proof as the disc version `QOU.Mathlib.ArgumentPrinciple.argument_principle`:
global factorisation `f = (∏_{u∈S} (·-u)^{ord_u f})·g` on `K`
(`MeromorphicOn.extract_zeros_poles`); on each boundary circle
`f'/f = Σ ord_u (z-u)⁻¹ + g'/g`; every `u ∈ S` lies inside the outer circle
(each term gives `2πi`) and outside the inner one (each term gives `0`); and the
two integrals of `g'/g` agree by the annulus Cauchy theorem. -/
theorem argument_principle_annulus {f : ℂ → ℂ} {r R : ℝ} (hr : 0 < r) (hrR : r < R)
    (hf : MeromorphicOn f (closedAnnulus r R))
    (S : Finset ℂ)
    (hfU : AnalyticOnNhd ℂ f (closedAnnulus r R \ (S : Set ℂ)))
    (hfne : ∀ z ∈ closedAnnulus r R, z ∉ S → f z ≠ 0)
    (hS : (S : Set ℂ) = {z | (r < ‖z‖ ∧ ‖z‖ < R) ∧
        (MeromorphicOn.divisor f (closedAnnulus r R)) z ≠ 0}) :
    (2 * (Real.pi : ℂ) * Complex.I)⁻¹ *
        ((∮ z in C(0, R), logDeriv f z) - ∮ z in C(0, r), logDeriv f z)
      = ((∑ w ∈ S, (MeromorphicOn.divisor f (closedAnnulus r R)) w : ℤ) : ℂ) := by
  classical
  set U : Set ℂ := closedAnnulus r R with hUdef
  set D : ℂ → ℤ := fun z => (MeromorphicOn.divisor f U) z with hDdef
  have hR : 0 < R := lt_trans hr hrR
  have hSin : ∀ w ∈ S, r < ‖w‖ ∧ ‖w‖ < R := by
    intro w hw
    have : w ∈ {z | (r < ‖z‖ ∧ ‖z‖ < R) ∧ (MeromorphicOn.divisor f U) z ≠ 0} :=
      hS ▸ Finset.mem_coe.mpr hw
    exact this.1
  have hUcompact : IsCompact U := isCompact_closedAnnulus r R
  have hUconn : IsConnected U := isConnected_closedAnnulus hr hrR.le
  -- points on the two boundary circles
  have hsphR : ∀ z, ‖z‖ = R → z ∈ U ∧ z ∉ S := by
    intro z hz
    refine ⟨mem_closedAnnulus.mpr ⟨by linarith, hz.le⟩, fun h => ?_⟩
    have := (hSin z h).2; linarith
  have hsphr : ∀ z, ‖z‖ = r → z ∈ U ∧ z ∉ S := by
    intro z hz
    refine ⟨mem_closedAnnulus.mpr ⟨hz.ge, by linarith⟩, fun h => ?_⟩
    have := (hSin z h).1; linarith
  have hD0 : ∀ z ∈ U, z ∉ S → D z = 0 := by
    intro z hzU hznS
    have haz : AnalyticAt ℂ f z := hfU z ⟨hzU, by simpa using hznS⟩
    have hne : f z ≠ 0 := hfne z hzU hznS
    have hord : meromorphicOrderAt f z = 0 := by
      rw [haz.meromorphicOrderAt_eq, analyticOrderAt_eq_zero.mpr (Or.inr hne)]; rfl
    show (MeromorphicOn.divisor f U) z = 0
    rw [hf.divisor_apply hzU, hord]; rfl
  have horder_ne : ∀ u : U, meromorphicOrderAt f (u : ℂ) ≠ ⊤ := by
    have hz0 : ‖((R : ℝ) : ℂ)‖ = R := by
      rw [Complex.norm_real, Real.norm_eq_abs, abs_of_pos hR]
    obtain ⟨hz0U, hz0nS⟩ := hsphR _ hz0
    have hz0order : meromorphicOrderAt f ((R : ℝ) : ℂ) ≠ ⊤ := by
      have haz : AnalyticAt ℂ f ((R : ℝ) : ℂ) := hfU _ ⟨hz0U, by simpa using hz0nS⟩
      have hne : f ((R : ℝ) : ℂ) ≠ 0 := hfne _ hz0U hz0nS
      rw [haz.meromorphicOrderAt_eq, analyticOrderAt_eq_zero.mpr (Or.inr hne)]
      simp
    exact (hf.exists_meromorphicOrderAt_ne_top_iff_forall hUconn).mp ⟨⟨_, hz0U⟩, hz0order⟩
  have hDsupp_fin : (MeromorphicOn.divisor f U).support.Finite :=
    (MeromorphicOn.divisor f U).finiteSupport hUcompact
  obtain ⟨g, hg_an, hg_ne, hfeq⟩ := hf.extract_zeros_poles horder_ne hDsupp_fin
  have hg_ne_cb : ∀ z ∈ U, g z ≠ 0 := fun z hz => hg_ne ⟨z, hz⟩
  have hmulsub : Function.mulSupport (fun u => (fun x : ℂ => x - u) ^ (D u)) ⊆ (S : Set ℂ) := by
    intro u hu
    by_contra hnS
    apply hu
    have hDu : D u = 0 := by
      by_cases hUu : u ∈ U
      · exact hD0 u hUu hnS
      · exact (MeromorphicOn.divisor f U).apply_eq_zero_of_notMem hUu
    show (fun x : ℂ => x - u) ^ (D u) = 1
    rw [hDu]; funext x; simp
  set P : ℂ → ℂ := fun z => ∏ u ∈ S, (z - u) ^ (D u) with hPdef
  set F : ℂ → ℂ := fun z => P z * g z with hFdef
  have hFeq : f =ᶠ[Filter.codiscreteWithin U] F := by
    have hRHS : ((∏ᶠ (u : ℂ), (fun x : ℂ => x - u) ^ (D u)) • g) = F := by
      funext z
      rw [Pi.smul_apply', smul_eq_mul, finprod_eq_prod_of_mulSupport_subset _ hmulsub,
        Finset.prod_apply]
      rfl
    rw [← hRHS]; exact hfeq
  -- on either boundary circle, `logDeriv f` is the pole sum plus `logDeriv g`
  have hEq : ∀ ρ, 0 < ρ → (∀ z, ‖z‖ = ρ → z ∈ U ∧ z ∉ S) →
      Set.EqOn (logDeriv f)
        (fun z => (∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹) + logDeriv g z) (sphere 0 ρ) := by
    intro ρ hρ hsph z hz
    have hzn : ‖z‖ = ρ := by simpa using hz
    obtain ⟨hzU, hznS⟩ := hsph z hzn
    have hzu : ∀ u ∈ S, z ≠ u := fun u hu h => hznS (h ▸ hu)
    have hgz : g z ≠ 0 := hg_ne_cb z hzU
    have hgdiff : DifferentiableAt ℂ g z := (hg_an z hzU).differentiableAt
    have hPeq : P = ∏ u ∈ S, (fun z : ℂ => (z - u) ^ (D u)) := by
      funext w; rw [hPdef, Finset.prod_apply]
    have hPdiff : DifferentiableAt ℂ P z := by
      rw [hPeq]
      exact DifferentiableAt.finset_prod
        (fun u hu => (differentiableAt_id.sub_const u).zpow (Or.inl (sub_ne_zero.2 (hzu u hu))))
    have hFana : AnalyticAt ℂ F z := by
      have hPana : AnalyticAt ℂ P z := by
        rw [hPeq]
        exact Finset.analyticAt_prod _
          (fun u hu => (analyticAt_id.sub analyticAt_const).zpow (sub_ne_zero.2 (hzu u hu)))
      exact hPana.mul (hg_an z hzU)
    have hfmero : MeromorphicAt f z := hf z hzU
    have hFmero : MeromorphicAt F z := hFana.meromorphicAt
    have hsub : sphere (0 : ℂ) ρ ⊆ U := fun w hw => (hsph w (by simpa using hw)).1
    have hacc : AccPt z (Filter.principal U) := accPt_of_sphere_subset hρ hsub hzn
    have hne1 : f =ᶠ[nhdsWithin z {z}ᶜ] F :=
      hfmero.eventuallyEq_nhdsNE_of_eventuallyEq_codiscreteWithin hFmero hzU hacc hFeq
    have hval : f z = F z := by
      have hfcont : ContinuousAt f z :=
        (hfU z ⟨hzU, by simpa using hznS⟩).continuousAt
      have h1 : Filter.Tendsto f (nhdsWithin z {z}ᶜ) (nhds (f z)) := hfcont.continuousWithinAt
      have h2 : Filter.Tendsto F (nhdsWithin z {z}ᶜ) (nhds (F z)) :=
        hFana.continuousAt.continuousWithinAt
      exact tendsto_nhds_unique h1 (h2.congr' hne1.symm)
    have hnhds : f =ᶠ[nhds z] F := eventuallyEq_nhds_of_eventuallyEq_nhdsNE hne1 hval
    have hstep : logDeriv f z = logDeriv F z := by
      unfold logDeriv
      rw [Pi.div_apply, Pi.div_apply, hnhds.deriv_eq, hnhds.eq_of_nhds]
    rw [hstep]
    have hPz : P z ≠ 0 := by
      rw [hPdef]
      exact Finset.prod_ne_zero_iff.mpr (fun u hu => zpow_ne_zero _ (sub_ne_zero.2 (hzu u hu)))
    have hsplit : logDeriv F z = logDeriv P z + logDeriv g z := by
      rw [hFdef]; exact logDeriv_mul z hPz hgz hPdiff hgdiff
    rw [hsplit]
    have hlogP : logDeriv P z = ∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹ := by
      rw [hPdef]
      rw [logDeriv_prod S (fun u z => (z - u) ^ (D u)) z
        (fun u hu => zpow_ne_zero _ (sub_ne_zero.2 (hzu u hu)))
        (fun u hu => (differentiableAt_id.sub_const u).zpow (Or.inl (sub_ne_zero.2 (hzu u hu))))]
      refine Finset.sum_congr rfl (fun u hu => ?_)
      have hd : DifferentiableAt ℂ (fun x : ℂ => x - u) z := differentiableAt_id.sub_const u
      rw [logDeriv_fun_zpow hd (D u)]
      have hlz : logDeriv (fun x : ℂ => x - u) z = (z - u)⁻¹ := by
        have hd : deriv (fun x : ℂ => x - u) z = 1 := ((hasDerivAt_id z).sub_const u).deriv
        rw [logDeriv_apply, hd]; simp
      rw [hlz]
    rw [hlogP]
  -- integrability
  have hlogA : AnalyticOnNhd ℂ (logDeriv g) U := (hg_an.deriv).div hg_an hg_ne_cb
  have hsphU : ∀ ρ, (∀ z, ‖z‖ = ρ → z ∈ U ∧ z ∉ S) → sphere (0 : ℂ) ρ ⊆ U :=
    fun ρ h w hw => (h w (by simpa using hw)).1
  have hIntLog : ∀ ρ, 0 ≤ ρ → (∀ z, ‖z‖ = ρ → z ∈ U ∧ z ∉ S) →
      CircleIntegrable (logDeriv g) 0 ρ :=
    fun ρ hρ h => ContinuousOn.circleIntegrable hρ (hlogA.continuousOn.mono (hsphU ρ h))
  have hSballR : ∀ u ∈ S, u ∈ ball (0 : ℂ) R := by
    intro u hu; simpa using (hSin u hu).2
  have hIntSumR : CircleIntegrable (fun z => ∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹) 0 R :=
    circleIntegrable_sum_simple_poles hR.le S (fun u => (D u : ℂ)) hSballR
  -- the pole sum is analytic on the inner closed disc
  have hpoleAn : ∀ z ∈ closedBall (0 : ℂ) r,
      AnalyticAt ℂ (fun z => ∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹) z := by
    intro z hz
    have hzr : ‖z‖ ≤ r := by simpa using hz
    have hzu : ∀ u ∈ S, z - u ≠ 0 := by
      intro u hu h
      have := (hSin u hu).1
      rw [sub_eq_zero.mp h] at hzr; linarith
    have : (fun z => ∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹)
        = ∑ u ∈ S, (fun z => (D u : ℂ) * (z - u)⁻¹) := by
      funext w; rw [Finset.sum_apply]
    rw [this]
    exact Finset.analyticAt_sum _
      (fun u hu => analyticAt_const.mul ((analyticAt_id.sub analyticAt_const).inv (hzu u hu)))
  have hIntSumr : CircleIntegrable (fun z => ∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹) 0 r :=
    ContinuousOn.circleIntegrable hr.le
      (fun z hz => (hpoleAn z (sphere_subset_closedBall hz)).continuousAt.continuousWithinAt)
  have hInner0 : (∮ z in C(0, r), ∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹) = 0 :=
    Complex.circleIntegral_eq_zero_of_differentiable_on_off_countable hr.le
      Set.countable_empty
      (fun z hz => (hpoleAn z hz).continuousAt.continuousWithinAt)
      (fun z hz => (hpoleAn z (ball_subset_closedBall hz.1)).differentiableAt)
  have hCauchy : (∮ z in C(0, R), logDeriv g z) = ∮ z in C(0, r), logDeriv g z :=
    Complex.circleIntegral_eq_of_differentiable_on_annulus_off_countable hr hrR.le
      Set.countable_empty hlogA.continuousOn
      (fun z hz => (hlogA z ⟨ball_subset_closedBall hz.1.1,
        fun h => hz.1.2 (ball_subset_closedBall h)⟩).differentiableAt)
  rw [circleIntegral.integral_congr hR.le (hEq R hR hsphR),
    circleIntegral.integral_congr hr.le (hEq r hr hsphr),
    circleIntegral.integral_add hIntSumR (hIntLog R hR.le hsphR),
    circleIntegral.integral_add hIntSumr (hIntLog r hr.le hsphr),
    circleIntegral_sum_simple_poles hR.le S (fun u => (D u : ℂ)) hSballR,
    hInner0, hCauchy, zero_add, add_sub_cancel_right, ← Finset.sum_mul,
    mul_comm (∑ u ∈ S, (D u : ℂ)) (2 * (Real.pi : ℂ) * Complex.I), ← mul_assoc,
    inv_mul_cancel₀ two_pi_I_ne_zero', one_mul, ← Int.cast_sum]

end QOU.Mathlib.ArgumentPrincipleAnnulus
