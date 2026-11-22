import QOU.KZ.KZComplex
import Mathlib.Analysis.Analytic.IsolatedZeros
import Mathlib.Analysis.Complex.CauchyIntegral

/-!
# Half-monodromy of the KZ equation

Step 1 of `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md` (hexagon groundwork).

* `eventuallyEq_of_gauge` — **uniqueness at a puncture.** Two holomorphic germs `K`, `H` at `0`
  with `K 0 = H 0` that both solve `z F' + F A = M(z) F` (with `M` continuous, `M 0 = A`)
  agree near `0`, provided `X ↦ kX − (AX − XA)` is injective for every `k ≥ 1`.  Proof: the
  difference is `z^n g(z)` with `g 0 ≠ 0`; dividing by `z^n` and letting `z → 0` gives
  `n g(0) − [A, g(0)] = 0`.
* `rho`, `hasDerivAt_comp_rho` — the Möbius map `ρ(v) = 1 − 1/v` (order three, cycling
  `0 → ∞ → 1 → 0`) pulls a solution of `KZ(X, Y)` back to a solution of `KZ(−X − Y, X)`.
* `log_neg_div` — `log(−z/(1−z)) = log z − iπ − log(1−z)` for `Im z > 0`.
* `half_monodromy` — with `C = −A − B`, the solution of `KZ(C, A)` normalised at `1`, read
  at `1/(1 − z) = ρ(ρ(z))`, equals `G₀^{AB}(z) e^{−iπA}` on
  `T = {Im z > 0, |z| < 1, Re z < 1/2}`.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1
-/

namespace QOU.KZ.KZHalfMonodromy
open Set Filter Topology QOU.KZ.FuchsianFormal QOU.KZ.FuchsianAnalytic QOU.KZ.KZComplex
variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

theorem eventuallyEq_of_gauge {A : R}
    (hinj : ∀ k : ℕ, 0 < k → Function.Injective (indicial A k))
    {M K H : ℂ → R} (hK : AnalyticAt ℂ K 0) (hH : AnalyticAt ℂ H 0)
    (hM : ContinuousAt M 0) (hM0 : M 0 = A)
    (hKe : ∀ᶠ z in 𝓝 0, z • deriv K z + K z * A = M z * K z)
    (hHe : ∀ᶠ z in 𝓝 0, z • deriv H z + H z * A = M z * H z)
    (h0 : K 0 = H 0) : K =ᶠ[𝓝 0] H := by
  set W : ℂ → R := fun z => K z - H z with hWdef
  have hW : AnalyticAt ℂ W 0 := hK.sub hH
  by_contra hne
  have hne' : ¬ (∀ᶠ z in 𝓝 (0:ℂ), W z = 0) := by
    intro h; apply hne; filter_upwards [h] with z hz; exact sub_eq_zero.mp hz
  obtain ⟨n, g, hg, hg0, hWg⟩ := hW.exists_eventuallyEq_pow_smul_nonzero_iff.mpr hne'
  have hW0 : W 0 = 0 := by simp [hWdef, h0]
  -- n ≥ 1
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := by
    rcases n with _ | m
    · exact absurd (by simpa [hW0] using hWg.self_of_nhds) (Ne.symm hg0)
    · exact ⟨m, rfl⟩
  -- W satisfies the gauge equation near 0
  have hWe : ∀ᶠ z in 𝓝 (0:ℂ), z • deriv W z + W z * A = M z * W z := by
    filter_upwards [hKe, hHe, hK.eventually_analyticAt, hH.eventually_analyticAt]
      with z h1 h2 h3 h4
    have : deriv W z = deriv K z - deriv H z :=
      deriv_sub h3.differentiableAt h4.differentiableAt
    rw [this]
    show z • (deriv K z - deriv H z) + (K z - H z) * A = M z * (K z - H z)
    rw [smul_sub, sub_mul, mul_sub, ← h1, ← h2]; abel
  -- derivative of W through the factorisation
  have hdW : ∀ᶠ z in 𝓝 (0:ℂ),
      deriv W z = z ^ (m + 1) • deriv g z + (((m + 1 : ℕ) : ℂ) * z ^ m) • g z := by
    have hev : ∀ᶠ z in 𝓝 (0:ℂ), W =ᶠ[𝓝 z] fun y => (y - 0) ^ (m + 1) • g y :=
      hWg.eventually_nhds
    filter_upwards [hev, hg.eventually_analyticAt] with z hz hgz
    rw [hz.deriv_eq]
    have := ((hasDerivAt_pow (m + 1) z).smul hgz.differentiableAt.hasDerivAt)
    simp only [sub_zero]
    convert this.deriv using 2
  -- the reduced equation, off 0
  set E : ℂ → R := fun z =>
    ((m + 1 : ℕ) : ℂ) • g z + z • deriv g z + g z * A - M z * g z with hEdef
  have hE : ∀ᶠ z in 𝓝[≠] (0:ℂ), E z = 0 := by
    have h := (hWe.and (hdW.and hWg))
    filter_upwards [nhdsWithin_le_nhds h, self_mem_nhdsWithin] with z ⟨he, hd, hwg⟩ hz
    have hz' : z ≠ 0 := hz
    rw [hd, hwg] at he
    simp only [sub_zero] at he
    have key : z ^ (m + 1) • E z = 0 := by
      have e2 := sub_eq_zero.mpr he
      rw [← e2]
      simp only [hEdef, smul_sub, smul_add, smul_smul, smul_mul_assoc, mul_smul_comm]
      rw [show z ^ (m + 1) * ((m + 1 : ℕ) : ℂ) = z * (((m + 1 : ℕ) : ℂ) * z ^ m) by ring,
        show z ^ (m + 1) * z = z * z ^ (m + 1) by ring]
      abel
    exact (smul_eq_zero.mp key).resolve_left (pow_ne_zero _ hz')
  have hEc : ContinuousAt E 0 := by
    have hg' : ContinuousAt (deriv g) 0 := hg.deriv.continuousAt
    exact ((continuousAt_const.smul hg.continuousAt).add
      (continuousAt_id.smul hg')).add (hg.continuousAt.mul continuousAt_const) |>.sub
      (hM.mul hg.continuousAt)
  have hE0 : E 0 = 0 := by
    have t1 : Tendsto E (𝓝[≠] (0:ℂ)) (𝓝 (E 0)) := hEc.tendsto.mono_left nhdsWithin_le_nhds
    have t2 : Tendsto E (𝓝[≠] (0:ℂ)) (𝓝 0) := tendsto_const_nhds.congr' (hE.mono fun _ h => h.symm)
    exact tendsto_nhds_unique t1 t2
  apply hg0
  apply hinj (m + 1) (Nat.succ_pos m)
  rw [show indicial A (m + 1) 0 = 0 by simp [indicial, ad]]
  rw [← hE0]
  simp only [hEdef, indicial, ad, hM0, zero_smul]
  rw [Nat.cast_smul_eq_nsmul, nsmul_eq_mul]
  abel


/-- The order-three Möbius map `ρ(v) = 1 − 1/v`, permuting `0 → ∞ → 1 → 0`. -/
noncomputable def rho (v : ℂ) : ℂ := 1 - v⁻¹

theorem hasDerivAt_rho {v : ℂ} (hv : v ≠ 0) : HasDerivAt rho ((v ^ 2)⁻¹) v := by
  have := (hasDerivAt_inv hv).const_sub 1
  simpa [rho] using this

omit [CompleteSpace R] in
theorem kzΩ_rho (X Y : R) {v : ℂ} (hv0 : v ≠ 0) (hv1 : v ≠ 1) :
    (v ^ 2)⁻¹ • kzΩ X Y (rho v) = kzΩ (-X - Y) X v := by
  have h1 : v - 1 ≠ 0 := sub_ne_zero.mpr hv1
  have e1 : (v ^ 2)⁻¹ * (rho v)⁻¹ = -v⁻¹ + (v - 1)⁻¹ := by
    simp only [rho]; field_simp; ring
  have e2 : (v ^ 2)⁻¹ * (rho v - 1)⁻¹ = -v⁻¹ := by
    simp only [rho]; field_simp; ring
  simp only [kzΩ, smul_add, smul_smul, e1, e2, smul_sub, add_smul, neg_smul, smul_neg]
  abel

omit [CompleteSpace R] in
/-- Pull-back of a KZ solution along `ρ`: `KZ(X,Y)` becomes `KZ(−X−Y, X)`. -/
theorem hasDerivAt_comp_rho {X Y : R} {G : ℂ → R} {v : ℂ} (hv0 : v ≠ 0) (hv1 : v ≠ 1)
    (h : HasDerivAt G (kzΩ X Y (rho v) * G (rho v)) (rho v)) :
    HasDerivAt (fun u => G (rho u)) (kzΩ (-X - Y) X v * G (rho v)) v := by
  have := h.scomp v (hasDerivAt_rho hv0)
  rw [← kzΩ_rho X Y hv0 hv1, smul_mul_assoc]
  exact this

theorem rho_ne_zero {v : ℂ} (hv1 : v ≠ 1) : rho v ≠ 0 := by
  intro h; apply hv1
  have : v⁻¹ = 1 := by simp only [rho] at h; linear_combination -h
  simpa using congrArg (·⁻¹) this

theorem rho_ne_one (v : ℂ) (hv0 : v ≠ 0) : rho v ≠ 1 := by
  simp [rho, hv0]

theorem one_sub_rho_rho {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    1 - rho (rho z) = -z / (1 - z) := by
  have h1 : 1 - z ≠ 0 := sub_ne_zero.mpr (Ne.symm hz1)
  have h2 : z - 1 ≠ 0 := sub_ne_zero.mpr hz1
  simp only [rho]; field_simp; ring

/-- **Logarithm of `−z/(1−z)`** in the upper half plane. -/
theorem log_neg_div {z : ℂ} (hz : 0 < z.im) :
    Complex.log (-z / (1 - z)) = Complex.log z - Real.pi * Complex.I - Complex.log (1 - z) := by
  have hz0 : z ≠ 0 := fun h => by simp [h] at hz
  have hz1 : 1 - z ≠ 0 := fun h => by
    have : z = 1 := by linear_combination -h
    simp [this] at hz
  set w := Complex.log z - Real.pi * Complex.I - Complex.log (1 - z)
  have hexp : Complex.exp w = -z / (1 - z) := by
    simp only [w, Complex.exp_sub, Complex.exp_log hz0, Complex.exp_log hz1,
      Complex.exp_pi_mul_I]
    ring
  have ha0 : 0 ≤ Complex.arg z := Complex.arg_nonneg_iff.mpr hz.le
  have haπ : Complex.arg z < Real.pi := Complex.arg_lt_pi_iff.mpr (Or.inr hz.ne')
  have hb : Complex.arg (1 - z) < 0 := Complex.arg_neg_iff.mpr (by simp; exact hz)
  have hb' : -Real.pi < Complex.arg (1 - z) := Complex.neg_pi_lt_arg _
  have him : w.im = Complex.arg z - Real.pi - Complex.arg (1 - z) := by
    simp [w, Complex.log_im]
  rw [← hexp, Complex.log_exp] <;> rw [him] <;> linarith


theorem cpowA_neg_div (A : R) {z : ℂ} (hz : 0 < z.im) :
    cpowA A (-z / (1 - z)) =
      cpowA (-A) (1 - z) * (cpowA A z * NormedSpace.exp ℂ ((-(Real.pi * Complex.I)) • A)) := by
  have hc : ∀ a b : ℂ, Commute (a • A) (b • A) := fun a b =>
    ((Commute.refl A).smul_left a).smul_right b
  unfold cpowA
  rw [← NormedSpace.exp_add_of_commute (hc _ _), ← NormedSpace.exp_add_of_commute]
  · rw [log_neg_div hz]; congr 1
    simp only [smul_neg, sub_smul, neg_smul]; abel
  · rw [smul_neg, ← neg_smul]; exact (hc _ _).add_right (hc _ _)

omit [CompleteSpace R] in
theorem cseries_zero (H : ℕ → R) : cseries H 0 = H 0 := by
  unfold cseries
  rw [tsum_eq_single 0]
  · simp
  · intro k hk; simp [zero_pow hk]

/-- The region `T = {Im z > 0, |z| < 1, Re z < 1/2}` where the half-monodromy is computed. -/
def T : Set ℂ := {z | 0 < z.im} ∩ Metric.ball 0 1 ∩ {z | z.re < 1 / 2}

theorem convex_T : Convex ℝ T :=
  ((convex_halfSpace_gt Complex.imLm.isLinear 0).inter (convex_ball 0 1)).inter
    (convex_halfSpace_lt Complex.reLm.isLinear (1 / 2))

theorem ne_zero_of_im_pos {z : ℂ} (hz : 0 < z.im) : z ≠ 0 := fun h => by simp [h] at hz

theorem ne_one_of_im_pos {z : ℂ} (hz : 0 < z.im) : z ≠ 1 := fun h => by simp [h] at hz

theorem im_neg_div {z : ℂ} : (-z / (1 - z)).im = -z.im / Complex.normSq (1 - z) := by
  rw [Complex.div_im]; simp; ring

theorem norm_neg_div_lt_one {z : ℂ} (hz : z.re < 1 / 2) : ‖-z / (1 - z)‖ < 1 := by
  have h1 : 0 < ‖1 - z‖ := norm_pos_iff.mpr fun h => by
    have : z = 1 := by linear_combination -h
    simp [this] at hz; norm_num at hz
  rw [norm_div, norm_neg, div_lt_one h1, ← sq_lt_sq₀ (norm_nonneg _) (norm_nonneg _),
    Complex.sq_norm, Complex.sq_norm, Complex.normSq_apply, Complex.normSq_apply]
  simp; nlinarith

theorem rho_rho_mem_D₁ {z : ℂ} (hz : z ∈ T) : rho (rho z) ∈ D₁ := by
  obtain ⟨⟨him, -⟩, hre⟩ := hz
  have hz0 := ne_zero_of_im_pos him
  have hz1 := ne_one_of_im_pos him
  refine ⟨?_, ?_⟩
  · show ‖1 - rho (rho z)‖ < 1
    rw [one_sub_rho_rho hz0 hz1]; exact norm_neg_div_lt_one hre
  · show 1 - rho (rho z) ∈ Complex.slitPlane
    rw [one_sub_rho_rho hz0 hz1, Complex.mem_slitPlane_iff]
    right; rw [im_neg_div]
    have : 0 < Complex.normSq (1 - z) := Complex.normSq_pos.mpr (sub_ne_zero.mpr (Ne.symm hz1))
    have him' : 0 < z.im := him
    exact (div_neg_of_neg_of_pos (by linarith) this).ne

/-- `G₁^{CA}(1/(1−z))`, pulled back twice along `ρ`, solves `KZ(A, B)` on `T`. -/
theorem isKZSolOn_pullback (A B : R) (H : ℕ → R) (h0 : H 0 = 1)
    (hH : IsFormalGauge (kzM0 A (-A - B)) H) :
    IsKZSolOn A B (fun z => G₁ A H (rho (rho z))) T := by
  intro z hz
  have him := hz.1.1
  have hz0 := ne_zero_of_im_pos him
  have hz1 := ne_one_of_im_pos him
  have h1 := isKZSolOn_G₁ (-A - B) A H h0 hH _ (rho_rho_mem_D₁ hz)
  have h2 := hasDerivAt_comp_rho (rho_ne_zero hz1) (rho_ne_one z hz0) h1
  have h3 := hasDerivAt_comp_rho (G := fun u => G₁ A H (rho u)) hz0 hz1 h2
  have e1 : -(-(-A - B) - A) - (-A - B) = A := by abel
  have e2 : -(-A - B) - A = B := by abel
  rw [e1, e2] at h3
  exact h3

/-- **Half-monodromy.** Pulling the solution of `KZ(C, A)` normalised at `1` (with
`C = −A − B`) back along `z ↦ 1/(1 − z)` gives the solution of `KZ(A, B)` normalised at `0`,
times `e^{−iπA}`, throughout the region `T`. -/
theorem half_monodromy (A B : R)
    (hinj : ∀ k : ℕ, 0 < k → Function.Injective (indicial A k))
    (H₀ H : ℕ → R) (h₀ : H₀ 0 = 1) (hH₀ : IsFormalGauge (kzM0 A B) H₀)
    (h0 : H 0 = 1) (hH : IsFormalGauge (kzM0 A (-A - B)) H) :
    EqOn (fun z => G₁ A H (rho (rho z)))
      (fun z => G₀ A H₀ z * NormedSpace.exp ℂ ((-(Real.pi * Complex.I)) • A)) T := by
  set E := NormedSpace.exp ℂ ((-(Real.pi * Complex.I)) • A) with hE
  set K : ℂ → R := fun z => cseries H (-z / (1 - z)) * cpowA (-A) (1 - z) with hK
  set M : ℂ → R := fun z => A + (z * (z - 1)⁻¹) • B with hM
  have hbH := boundedOn_kz_solution A (-A - B) H h0 hH
  have hbH₀ := boundedOn_kz_solution A B H₀ h₀ hH₀
  have hXK : ∀ z, 0 < z.im → G₁ A H (rho (rho z)) = K z * (cpowA A z * E) := by
    intro z hz
    simp only [G₁, one_sub_rho_rho (ne_zero_of_im_pos hz) (ne_one_of_im_pos hz),
      cpowA_neg_div A hz, hK, mul_assoc]
    rfl
  have hball : ∀ z ∈ Metric.ball (0 : ℂ) (1 / 2), z.re < 1 / 2 ∧ z ≠ 1 ∧ 1 - z ≠ 0 := by
    intro z hz
    have hz' : ‖z‖ < 1 / 2 := by simpa using hz
    have hre : z.re < 1 / 2 := (Complex.re_le_norm z).trans_lt hz'
    have h1 : z ≠ 1 := fun h => by simp [h] at hre; norm_num at hre
    exact ⟨hre, h1, sub_ne_zero.mpr (Ne.symm h1)⟩
  -- `K` is holomorphic on the disc of radius `1/2`
  have hKdiff : DifferentiableOn ℂ K (Metric.ball 0 (1 / 2)) := by
    intro z hz
    obtain ⟨hre, -, h1⟩ := hball z hz
    have hφ : DifferentiableAt ℂ (fun z : ℂ => -z / (1 - z)) z :=
      differentiableAt_id.neg.div ((differentiableAt_const (1 : ℂ)).sub differentiableAt_id) h1
    have hc := (hasDerivAt_cseries hbH (norm_neg_div_lt_one hre)).differentiableAt
    have hslit : 1 - z ∈ Complex.slitPlane :=
      Complex.mem_slitPlane_iff.mpr (Or.inl (by simp; linarith))
    have hp := (hasDerivAt_cpowA (-A) hslit).differentiableAt
    exact ((hc.comp z hφ).mul (hp.comp z ((differentiableAt_const (1 : ℂ)).sub differentiableAt_id)))
      |>.differentiableWithinAt
  have hKan : AnalyticOnNhd ℂ K (Metric.ball 0 (1 / 2)) :=
    hKdiff.analyticOnNhd Metric.isOpen_ball
  set F : ℂ → R := fun z => z • deriv K z + K z * A - M z * K z with hF
  have hFan : AnalyticOnNhd ℂ F (Metric.ball 0 (1 / 2)) := by
    apply DifferentiableOn.analyticOnNhd _ Metric.isOpen_ball
    have hdK := hKan.deriv.differentiableOn
    have hMd : DifferentiableOn ℂ M (Metric.ball 0 (1 / 2)) := by
      intro z hz
      have : z - 1 ≠ 0 := sub_ne_zero.mpr (hball z hz).2.1
      exact ((differentiableAt_const A).add ((differentiableAt_id.mul
        ((differentiableAt_id.sub (differentiableAt_const (1 : ℂ))).inv this)).smul_const B))
        |>.differentiableWithinAt
    exact ((differentiableOn_id.smul hdK).add (hKdiff.mul_const A)).sub (hMd.mul hKdiff)
  -- the gauge equation holds on the upper half of that disc …
  have hFzero : ∀ z ∈ Metric.ball (0 : ℂ) (1 / 2), 0 < z.im → F z = 0 := by
    intro z hzB hz
    have hz0 := ne_zero_of_im_pos hz
    obtain ⟨hre, -, -⟩ := hball z hzB
    have hzT : z ∈ T :=
      ⟨⟨hz, Metric.ball_subset_ball (by norm_num) hzB⟩, hre⟩
    have hX := isKZSolOn_pullback A B H h0 hH z hzT
    have hev : (fun u => K u * (cpowA A u * E)) =ᶠ[𝓝 z]
        fun u => G₁ A H (rho (rho u)) := by
      filter_upwards [(isOpen_lt continuous_const Complex.continuous_im).mem_nhds hz]
        with u hu
      exact (hXK u hu).symm
    have hX' := hX.congr_of_eventuallyEq hev
    beta_reduce at hX'
    rw [hXK z hz] at hX'
    have hslit : z ∈ Complex.slitPlane := Complex.mem_slitPlane_iff.mpr (Or.inr hz.ne')
    have hP := (hasDerivAt_cpowA A hslit).mul_const E
    have hKd := (hKan z hzB).differentiableAt.hasDerivAt
    have hu := (hKd.mul hP).unique hX'
    have hunit : IsUnit (cpowA A z * E) := (isUnit_cpowA A z).mul (NormedSpace.isUnit_exp ℂ _)
    have hzΩ : z • kzΩ A B z = M z := by
      simp only [kzΩ, hM, smul_add, smul_smul, mul_inv_cancel₀ hz0, one_smul]
    rw [← hunit.mul_left_eq_zero]
    calc F z * (cpowA A z * E)
        = z • (deriv K z * (cpowA A z * E) + K z * (z⁻¹ • (A * cpowA A z) * E))
            - M z * (K z * (cpowA A z * E)) := by
          simp only [hF, sub_mul, add_mul, smul_add, smul_mul_assoc, mul_smul_comm, smul_smul,
            mul_inv_cancel₀ hz0, one_smul, mul_assoc]
      _ = 0 := by rw [hu, ← smul_mul_assoc, hzΩ, sub_self]
  -- … hence on the whole disc, by the identity theorem
  have hFB : EqOn F 0 (Metric.ball 0 (1 / 2)) := by
    have hz₀ : Complex.I / 4 ∈ Metric.ball (0 : ℂ) (1 / 2) := by
      simp; norm_num
    refine hFan.eqOn_zero_of_preconnected_of_eventuallyEq_zero
      (convex_ball 0 _).isPreconnected hz₀ ?_
    have hopen : IsOpen (Metric.ball (0 : ℂ) (1 / 2) ∩ {z | 0 < z.im}) :=
      Metric.isOpen_ball.inter (isOpen_lt continuous_const Complex.continuous_im)
    filter_upwards [hopen.mem_nhds ⟨hz₀, by simp⟩] with z hz
    exact hFzero z hz.1 hz.2
  have hKe : ∀ᶠ z in 𝓝 (0 : ℂ), z • deriv K z + K z * A = M z * K z := by
    filter_upwards [Metric.ball_mem_nhds (0 : ℂ) (by norm_num : (0 : ℝ) < 1 / 2)] with z hz
    exact sub_eq_zero.mp (hFB hz)
  -- the series `H₀` satisfies the same equation
  have hSd : ∀ z : ℂ, ‖z‖ < 1 →
      HasDerivAt (cseries H₀) (∑' n : ℕ, ((n : ℂ) * z ^ (n - 1)) • H₀ n) z :=
    fun z hz => hasDerivAt_cseries hbH₀ hz
  have hHe : ∀ᶠ z in 𝓝 (0 : ℂ),
      z • deriv (cseries H₀) z + cseries H₀ z * A = M z * cseries H₀ z := by
    filter_upwards [Metric.ball_mem_nhds (0 : ℂ) one_pos] with z hz
    have hz' : ‖z‖ < 1 := by simpa using hz
    rw [(hSd z hz').deriv, smul_deriv_cseries]
    have g := gauge_cseries (boundedOn_kzM0 A B) hbH₀ hH₀ hz'
    rw [show kzM0 A B 0 = A by simp [kzM0], cseries_kzM0 A B hz'] at g
    rw [g]
    congr 1
    simp only [hM]
    rw [sub_eq_add_neg, ← neg_smul, show (1 : ℂ) - z = -(z - 1) by ring, div_neg, neg_neg,
      div_eq_mul_inv]
  have hSan : AnalyticAt ℂ (cseries H₀) 0 := by
    have : DifferentiableOn ℂ (cseries H₀) (Metric.ball 0 1) := fun z hz =>
      (hSd z (by simpa using hz)).differentiableAt.differentiableWithinAt
    exact this.analyticOnNhd Metric.isOpen_ball 0 (Metric.mem_ball_self one_pos)
  have hMc : ContinuousAt M 0 := by
    have : ContinuousAt (fun z : ℂ => z * (z - 1)⁻¹) 0 :=
      continuousAt_id.mul ((continuousAt_id.sub continuousAt_const).inv₀ (by norm_num))
    exact continuousAt_const.add (this.smul continuousAt_const)
  have hM0 : M 0 = A := by simp [hM]
  have hK0 : K 0 = cseries H₀ 0 := by
    simp [hK, cseries_zero, cpowA, h0, h₀]
  have hKS := eventuallyEq_of_gauge hinj (hKan 0 (Metric.mem_ball_self (by norm_num))) hSan
    hMc hM0 hKe hHe hK0
  -- a common point in `T`
  obtain ⟨ε, hε, hεb⟩ := Metric.mem_nhds_iff.mp hKS
  set δ : ℝ := min ε (1 / 4) / 2 with hδdef
  have hδ : 0 < δ := by positivity
  have hδε : δ < ε := by
    have := min_le_left ε (1 / 4); simp only [hδdef]; linarith
  have hδ4 : δ < 1 / 4 := by
    have := min_le_right ε (1 / 4); simp only [hδdef]; linarith
  set c : ℂ := (δ : ℂ) * Complex.I with hc
  have hcn : ‖c‖ = δ := by simp [hc, abs_of_pos hδ]
  have hcim : 0 < c.im := by simp [hc, hδ]
  have hcT : c ∈ T := by
    refine ⟨⟨hcim, ?_⟩, ?_⟩
    · show ‖c - 0‖ < 1; rw [sub_zero, hcn]; linarith
    · show c.re < 1 / 2; simp [hc]
  have hKc : K c = cseries H₀ c := hεb (by
    show ‖c - 0‖ < ε; rw [sub_zero, hcn]; exact hδε)
  refine eqOn_of_convex convex_T ?_ (isKZSolOn_pullback A B H h0 hH) ?_ hcT ?_
  · intro z hz
    have hz0 := ne_zero_of_im_pos hz.1.1
    have hz1 := ne_one_of_im_pos hz.1.1
    exact (((continuousAt_id.inv₀ hz0).smul continuousAt_const).add
      (((continuousAt_id.sub continuousAt_const).inv₀ (sub_ne_zero.mpr hz1)).smul
        continuousAt_const)).continuousWithinAt
  · intro z hz
    have hslit : z ∈ Complex.slitPlane := Complex.mem_slitPlane_iff.mpr (Or.inr hz.1.1.ne')
    exact (isKZSolOn_G₀ A B H₀ h₀ hH₀).mul_const E z ⟨by simpa using hz.1.2, hslit⟩
  · show G₁ A H (rho (rho c)) = G₀ A H₀ c * E
    rw [hXK c hcim, hKc]; simp only [G₀, mul_assoc]

end QOU.KZ.KZHalfMonodromy
