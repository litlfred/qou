import QOU.KZ.KZHalfMonodromy
import QOU.Mass.KZHolonomy.FlatTransport

/-!
# The hexagon relation for the KZ associator

For the 3-point KZ equation `G' = (z⁻¹ A + (z − 1)⁻¹ B) G` in a complete normed `ℂ`-algebra,
with `C = −A − B` and `A`, `B`, `C` non-resonant,

  `e^{−iπA} Φ(C,A) e^{−iπC} Φ(B,C) e^{−iπB} Φ(A,B) = 1`   (`hexagon`).

The proof compares six solutions of `KZ(A,B)` around the fixed point `e^{iπ/3}` of the
order-three rotation `ρ(z) = 1 − 1/z`: the normalised solutions at `0` and `1` of `KZ(A,B)`,
`KZ(B,C)` and `KZ(C,A)`, the last four pulled back along `ρ` and `ρ²`.  Consecutive solutions
differ by an associator (`lens_rel`) or by a half-monodromy (`half_monodromy`).  An invertible
reference solution on a disc around `e^{iπ/3}` (`exists_reference`, by radial transport)
turns these pointwise relations into relations between constants; going once around gives
`G₀ = G₀ Q`, and invertibility of `G₀` near `0` gives `Q = 1`.

-- Ref: [drinfeld1990] Leningrad Math. J. 1 (1990) 1419–1457, §2
-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1
-/
namespace QOU.KZ.KZHexagon
open Set Filter Topology QOU.KZ.FuchsianFormal QOU.KZ.KZComplex QOU.KZ.KZHalfMonodromy
  QOU.Mass.KZHolonomy
variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

/-- `v ↦ (h ↦ h • v)`, as a real-linear map into real-linear maps. -/
noncomputable def smulCLM : R →L[ℝ] ℂ →L[ℝ] R := (ContinuousLinearMap.lsmul ℝ ℂ).flip

omit [CompleteSpace R] in
theorem smulCLM_apply (v : R) (h : ℂ) : smulCLM v h = h • v := rfl

/-- **An invertible reference solution on a star-shaped domain.** If `Ω` is holomorphic on an
open domain `D` star-shaped about `c` (with continuous derivative), then `N' = Ω N` has a
solution on `D` with `N(c) = 1`, invertible at every point.  Radial transport from `c`. -/
theorem exists_reference {Ω Ω' : ℂ → R} {D : Set ℂ} {c : ℂ} (hD : IsOpen D)
    (hstar : StarConvex ℝ c D)
    (hΩ : ∀ z ∈ D, HasDerivAt Ω (Ω' z) z) (hΩ' : ContinuousOn Ω' D) :
    ∃ N : ℂ → R, (∀ z ∈ D, HasDerivAt N (Ω z * N z) z) ∧ (∀ z ∈ D, IsUnit (N z)) ∧
      N c = 1 := by
  set ω : ℂ → ℂ →L[ℝ] R := fun z => smulCLM (Ω z) with hω
  set ω' : ℂ → ℂ →L[ℝ] ℂ →L[ℝ] R := fun y => smulCLM.comp (smulCLM (Ω' y)) with hω'
  have hfl : IsFlatOn ω ω' D := by
    refine ⟨fun y hy => ?_, ?_, fun y _ a b => ?_⟩
    · have h1 := ((hΩ y hy).hasFDerivAt.restrictScalars ℝ)
      have h2 := smulCLM.hasFDerivAt.comp y h1
      convert h2 using 1
    · exact (continuous_const.clm_comp smulCLM.continuous).comp_continuousOn hΩ'
    · simp only [hω, hω', ContinuousLinearMap.comp_apply, smulCLM_apply, smul_smul,
        smul_mul_smul_comm, mul_comm a b, sub_self]
  refine ⟨radialTransport ω c, fun z hz => ?_, fun z hz => isUnit_radialTransport hstar hfl hz, ?_⟩
  · have h := hasFDerivAt_radialTransport hD hfl
      (fun t ht => seg_mem_of_starConvex hstar hz ht)
    have h2 : HasFDerivAt (radialTransport ω c)
        (ContinuousLinearMap.smulRight (1 : ℂ →L[ℂ] ℂ) (Ω z * radialTransport ω c z)) z := by
      refine hasFDerivAt_of_restrictScalars ℝ h ?_
      ext h
      simp [hω, smulCLM_apply]
    simpa using h2.hasDerivAt
  · have hX : ContinuousOn (radialX ω c c) (Icc 0 1) := by
      unfold radialX; simp only [sub_self, map_zero]; exact continuousOn_const
    have hU : IsFundSol (radialX ω c c) (fun _ => (1 : R)) := by
      refine ⟨rfl, fun t _ => ?_⟩
      unfold radialX; simp only [sub_self, map_zero, zero_mul]
      exact hasDerivWithinAt_const _ _ _
    rw [radialTransport_eq hX hU]

/-! ### Complex solutions restricted to the real segment -/

omit [CompleteSpace R] in
theorem cseries_ofReal (H : ℕ → R) (t : ℝ) : cseries H t = FuchsianAnalytic.series H t := by
  unfold cseries FuchsianAnalytic.series
  congr 1; ext k
  rw [← Complex.ofReal_pow, Complex.coe_smul]

omit [CompleteSpace R] in
theorem cpowA_ofReal (A : R) {t : ℝ} (ht : 0 < t) : cpowA A t = FuchsianAnalytic.tpow A t := by
  unfold cpowA FuchsianAnalytic.tpow
  rw [← Complex.ofReal_log ht.le, Complex.coe_smul, NormedSpace.exp_eq_exp ℝ ℂ R]

omit [CompleteSpace R] in
theorem G₀_ofReal (A : R) (H : ℕ → R) {t : ℝ} (ht : 0 < t) :
    KZComplex.G₀ A H t = AssociatorKZ.G₀ A H t := by
  simp only [KZComplex.G₀, AssociatorKZ.G₀, cseries_ofReal, cpowA_ofReal A ht]

omit [CompleteSpace R] in
theorem G₁_ofReal (B : R) (H : ℕ → R) {t : ℝ} (ht : t < 1) :
    KZComplex.G₁ B H t = AssociatorKZ.G₁ B H t := by
  have h : (1 : ℂ) - t = ((1 - t : ℝ) : ℂ) := by push_cast; ring
  simp only [KZComplex.G₁, AssociatorKZ.G₁, h, cseries_ofReal, cpowA_ofReal B (sub_pos.mpr ht)]

/-- The lens `|z| < 1, |z − 1| < 1`, where both normalised solutions live. -/
def L : Set ℂ := Metric.ball 0 1 ∩ Metric.ball 1 1

theorem re_pos_of_mem_ball_one {z : ℂ} (hz : z ∈ Metric.ball (1 : ℂ) 1) : 0 < z.re := by
  have h := (Complex.abs_re_le_norm (z - 1)).trans_lt (by simpa [dist_eq_norm] using hz)
  simp at h; linarith [(abs_lt.mp h).1]

theorem re_lt_one_of_mem_ball_zero {z : ℂ} (hz : z ∈ Metric.ball (0 : ℂ) 1) : z.re < 1 := by
  have h := (Complex.abs_re_le_norm z).trans_lt (by simpa using hz)
  linarith [(abs_lt.mp h).2]

theorem L_subset_D₀ : L ⊆ D₀ := fun z hz =>
  ⟨by simpa using hz.1, Complex.mem_slitPlane_iff.mpr (Or.inl (re_pos_of_mem_ball_one hz.2))⟩

theorem L_subset_D₁ : L ⊆ D₁ := fun z hz =>
  ⟨by simpa [dist_eq_norm, norm_sub_rev] using hz.2,
    Complex.mem_slitPlane_iff.mpr (Or.inl (by simp; linarith [re_lt_one_of_mem_ball_zero hz.1]))⟩

/-- **The associator relates the two normalised solutions on the whole lens.** -/
theorem lens_rel (A B : R) (H₀ H₁ : ℕ → R) (h₀ : H₀ 0 = 1) (hH₀ : IsFormalGauge (kzM0 A B) H₀)
    (h₁ : H₁ 0 = 1) (hH₁ : IsFormalGauge (kzM0 B A) H₁) :
    EqOn (KZComplex.G₀ A H₀)
      (fun z => KZComplex.G₁ B H₁ z * AssociatorKZ.phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁) L := by
  have hc : ((1 / 2 : ℝ) : ℂ) ∈ L := by
    refine ⟨?_, ?_⟩ <;> simp [dist_eq_norm] <;> norm_num
  refine eqOn_of_convex ((convex_ball _ _).inter (convex_ball _ _)) ?_
    (fun z hz => isKZSolOn_G₀ A B H₀ h₀ hH₀ z (L_subset_D₀ hz))
    (fun z hz => (isKZSolOn_G₁ A B H₁ h₁ hH₁).mul_const _ z (L_subset_D₁ hz)) hc ?_
  · intro z hz
    have hz0 : z ≠ 0 := fun h => by simpa [h] using re_pos_of_mem_ball_one hz.2
    have hz1 : z - 1 ≠ 0 := fun h => by
      have : z = 1 := sub_eq_zero.mp h
      simpa [this] using re_lt_one_of_mem_ball_zero hz.1
    exact (((continuousAt_id.inv₀ hz0).smul continuousAt_const).add
      (((continuousAt_id.sub continuousAt_const).inv₀ hz1).smul
        continuousAt_const)).continuousWithinAt
  · have := (AssociatorKZ.phiKZ_spec A B H₀ H₁ h₀ hH₀ h₁ hH₁).2 (1 / 2) (by norm_num)
    show KZComplex.G₀ A H₀ ((1 / 2 : ℝ) : ℂ) = KZComplex.G₁ B H₁ ((1 / 2 : ℝ) : ℂ) * _
    rw [G₀_ofReal A H₀ (by norm_num), G₁_ofReal B H₁ (by norm_num)]
    exact this

/-! ### Geometry of the Möbius rotation near `e^{iπ/3}` -/

section Geometry

theorem norm_lt_norm_of_normSq {a b : ℂ} (h : Complex.normSq a < Complex.normSq b) : ‖a‖ < ‖b‖ := by
  rw [← sq_lt_sq₀ (norm_nonneg _) (norm_nonneg _), Complex.sq_norm, Complex.sq_norm]; exact h

theorem norm_lt_one_of_normSq {a : ℂ} (h : Complex.normSq a < 1) : ‖a‖ < 1 := by
  simpa using norm_lt_norm_of_normSq (b := 1) (by simpa using h)

theorem one_lt_norm_of_normSq {a : ℂ} (h : 1 < Complex.normSq a) : 1 < ‖a‖ := by
  simpa using norm_lt_norm_of_normSq (a := 1) (by simpa using h)

theorem rho_eq {z : ℂ} (hz : z ≠ 0) : rho z = (z - 1) / z := by
  simp only [rho]; field_simp

theorem rho_rho_eq {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) : rho (rho z) = (1 - z)⁻¹ := by
  have h1 : 1 - z ≠ 0 := sub_ne_zero.mpr (Ne.symm hz1)
  have h2 : z - 1 ≠ 0 := sub_ne_zero.mpr hz1
  simp only [rho]; field_simp; ring

theorem rho_rho_rho {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) : rho (rho (rho z)) = z := by
  have h1 : 1 - z ≠ 0 := sub_ne_zero.mpr (Ne.symm hz1)
  rw [rho_rho_eq hz0 hz1]; simp only [rho, inv_inv]; ring

theorem one_sub_rho {z : ℂ} : 1 - rho z = z⁻¹ := by simp [rho]

theorem normSq_sub_one (z : ℂ) :
    Complex.normSq (z - 1) = (z.re - 1) * (z.re - 1) + z.im * z.im := by
  simp [Complex.normSq_apply]

theorem normSq_one_sub (z : ℂ) :
    Complex.normSq (1 - z) = (1 - z.re) * (1 - z.re) + z.im * z.im := by
  simp [Complex.normSq_apply]

theorem normSq_pos_of_im {z : ℂ} (hz : 0 < z.im) : 0 < Complex.normSq z :=
  Complex.normSq_pos.mpr (ne_zero_of_im_pos hz)

theorem normSq_one_sub_pos_of_im {z : ℂ} (hz : 0 < z.im) : 0 < Complex.normSq (1 - z) :=
  Complex.normSq_pos.mpr (sub_ne_zero.mpr (Ne.symm (ne_one_of_im_pos hz)))

theorem im_rho {z : ℂ} : (rho z).im = z.im / Complex.normSq z := by
  simp [rho, Complex.inv_im, neg_div]

theorem re_rho {z : ℂ} : (rho z).re = 1 - z.re / Complex.normSq z := by
  simp [rho, Complex.inv_re]

theorem norm_rho_lt_one {z : ℂ} (hz : 0 < z.im)
    (h : Complex.normSq (z - 1) < Complex.normSq z) : ‖rho z‖ < 1 := by
  rw [rho_eq (ne_zero_of_im_pos hz), norm_div,
    div_lt_one (norm_pos_iff.mpr (ne_zero_of_im_pos hz))]
  exact norm_lt_norm_of_normSq h

theorem mem_D₀_rho {z : ℂ} (hz : 0 < z.im) (h : Complex.normSq (z - 1) < Complex.normSq z) :
    rho z ∈ D₀ :=
  ⟨norm_rho_lt_one hz h, Complex.mem_slitPlane_iff.mpr
    (Or.inr (by rw [im_rho]; exact (div_pos hz (normSq_pos_of_im hz)).ne'))⟩

theorem mem_D₁_rho {z : ℂ} (hz : 0 < z.im) (h : 1 < Complex.normSq z) : rho z ∈ D₁ := by
  refine ⟨?_, ?_⟩
  · show ‖1 - rho z‖ < 1
    rw [one_sub_rho, norm_inv]; exact inv_lt_one_of_one_lt₀ (one_lt_norm_of_normSq h)
  · show 1 - rho z ∈ Complex.slitPlane
    rw [one_sub_rho, Complex.mem_slitPlane_iff]
    right; rw [Complex.inv_im]
    exact (div_neg_of_neg_of_pos (neg_neg_of_pos hz) (normSq_pos_of_im hz)).ne

theorem mem_D₀_rho2 {z : ℂ} (hz : 0 < z.im) (h : 1 < Complex.normSq (1 - z)) :
    rho (rho z) ∈ D₀ := by
  rw [rho_rho_eq (ne_zero_of_im_pos hz) (ne_one_of_im_pos hz)]
  refine ⟨?_, ?_⟩
  · show ‖(1 - z)⁻¹‖ < 1
    rw [norm_inv]; exact inv_lt_one_of_one_lt₀ (one_lt_norm_of_normSq h)
  · rw [Complex.mem_slitPlane_iff]; right; rw [Complex.inv_im]
    have : -(1 - z).im = z.im := by simp
    rw [this]; exact (div_pos hz (normSq_one_sub_pos_of_im hz)).ne'

theorem mem_D₁_rho2 {z : ℂ} (hz : 0 < z.im) (hre : z.re < 1 / 2) : rho (rho z) ∈ D₁ := by
  have hz0 := ne_zero_of_im_pos hz
  have hz1 := ne_one_of_im_pos hz
  refine ⟨?_, ?_⟩
  · show ‖1 - rho (rho z)‖ < 1
    rw [one_sub_rho_rho hz0 hz1]; exact norm_neg_div_lt_one hre
  · show 1 - rho (rho z) ∈ Complex.slitPlane
    rw [one_sub_rho_rho hz0 hz1, Complex.mem_slitPlane_iff]
    right; rw [im_neg_div]
    exact (div_neg_of_neg_of_pos (by linarith) (normSq_one_sub_pos_of_im hz)).ne

theorem mem_T_rho {z : ℂ} (hz : 0 < z.im) (h1 : Complex.normSq (z - 1) < Complex.normSq z)
    (h2 : Complex.normSq (z - 1) < 1) : rho z ∈ T := by
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · show 0 < (rho z).im
    rw [im_rho]; exact div_pos hz (normSq_pos_of_im hz)
  · simpa using norm_rho_lt_one hz h1
  · show (rho z).re < 1 / 2
    have hn := normSq_pos_of_im hz
    rw [re_rho, sub_lt_comm, lt_div_iff₀ hn]
    rw [normSq_sub_one] at h2; rw [Complex.normSq_apply]; nlinarith

theorem mem_L_rho {z : ℂ} (hz : 0 < z.im) (h1 : Complex.normSq (z - 1) < Complex.normSq z)
    (h2 : 1 < Complex.normSq z) : rho z ∈ L := by
  refine ⟨by simpa using norm_rho_lt_one hz h1, ?_⟩
  show dist (rho z) 1 < 1
  rw [dist_eq_norm, ← norm_neg, neg_sub, one_sub_rho, norm_inv]
  exact inv_lt_one_of_one_lt₀ (one_lt_norm_of_normSq h2)

theorem mem_T_rho2 {z : ℂ} (hz : 0 < z.im) (h1 : 1 < Complex.normSq (1 - z))
    (h2 : 1 < Complex.normSq z) : rho (rho z) ∈ T := by
  have hm := normSq_one_sub_pos_of_im hz
  rw [rho_rho_eq (ne_zero_of_im_pos hz) (ne_one_of_im_pos hz)]
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · show 0 < ((1 - z)⁻¹).im
    rw [Complex.inv_im]
    have : -(1 - z).im = z.im := by simp
    rw [this]; exact div_pos hz hm
  · show ‖(1 - z)⁻¹ - 0‖ < 1
    rw [sub_zero, norm_inv]; exact inv_lt_one_of_one_lt₀ (one_lt_norm_of_normSq h1)
  · show ((1 - z)⁻¹).re < 1 / 2
    rw [Complex.inv_re, div_lt_iff₀ hm]
    rw [normSq_one_sub]; rw [Complex.normSq_apply] at h2; simp; nlinarith

theorem mem_L_rho2 {z : ℂ} (hz : 0 < z.im) (h1 : 1 < Complex.normSq (1 - z))
    (h2 : Complex.normSq z < Complex.normSq (1 - z)) : rho (rho z) ∈ L := by
  have h1z : 1 - z ≠ 0 := sub_ne_zero.mpr (Ne.symm (ne_one_of_im_pos hz))
  rw [rho_rho_eq (ne_zero_of_im_pos hz) (ne_one_of_im_pos hz)]
  refine ⟨?_, ?_⟩
  · show ‖(1 - z)⁻¹ - 0‖ < 1
    rw [sub_zero, norm_inv]; exact inv_lt_one_of_one_lt₀ (one_lt_norm_of_normSq h1)
  · show dist (1 - z)⁻¹ 1 < 1
    have : (1 - z)⁻¹ - 1 = z / (1 - z) := by field_simp; ring
    rw [dist_eq_norm, this, norm_div, div_lt_one (norm_pos_iff.mpr h1z)]
    exact norm_lt_norm_of_normSq h2

end Geometry


/-! ### The hexagon -/

section Hexagon

/-- `e^{−iπX}`. -/
noncomputable def eπ (X : R) : R := NormedSpace.exp ℂ ((-(Real.pi * Complex.I)) • X)

omit [CompleteSpace R] in
theorem hasDerivAt_kzΩ (A B : R) {z : ℂ} (hz0 : z ≠ 0) (hz1 : z - 1 ≠ 0) :
    HasDerivAt (kzΩ A B) ((-(z ^ 2)⁻¹) • A + (-1 / (z - 1) ^ 2) • B) z := by
  have h1 := (hasDerivAt_inv hz0).smul_const A
  have h2 := (((hasDerivAt_id' z).sub_const (1 : ℂ)).inv hz1).smul_const B
  exact h1.add h2

omit [CompleteSpace R] in
theorem continuousAt_kzΩ' (A B : R) {z : ℂ} (hz0 : z ≠ 0) (hz1 : z - 1 ≠ 0) :
    ContinuousAt (fun w : ℂ => (-(w ^ 2)⁻¹) • A + (-1 / (w - 1) ^ 2) • B) z :=
  (((continuousAt_id.pow 2).inv₀ (pow_ne_zero 2 hz0)).neg.smul continuousAt_const).add
    ((continuousAt_const.div ((continuousAt_id.sub continuousAt_const).pow 2)
      (pow_ne_zero 2 hz1)).smul continuousAt_const)

theorem convex_lin_gt (a b c : ℝ) : Convex ℝ {z : ℂ | c < a * z.re + b * z.im} :=
  convex_halfSpace_gt (f := fun z : ℂ => a * z.re + b * z.im)
    ⟨fun x y => by simp; ring, fun r x => by simp; ring⟩ c

theorem mem_ball_of_normSq {z c : ℂ} (h : Complex.normSq (z - c) < 1) : z ∈ Metric.ball c 1 := by
  rw [Metric.mem_ball, dist_eq_norm]; exact norm_lt_one_of_normSq h

/-- The working disc around `e^{iπ/3}`, cut to the upper half-plane. -/
def Dh : Set ℂ := Metric.ball ⟨1 / 2, 9 / 10⟩ 1 ∩ {z | 0 < z.im}

theorem convex_Dh : Convex ℝ Dh :=
  (convex_ball _ _).inter (convex_halfSpace_gt Complex.imLm.isLinear 0)

theorem isOpen_Dh : IsOpen Dh :=
  Metric.isOpen_ball.inter (isOpen_lt continuous_const Complex.continuous_im)

theorem mem_Dh {z : ℂ} (h1 : Complex.normSq (z - ⟨1 / 2, 9 / 10⟩) < 1) (h2 : 0 < z.im) :
    z ∈ Dh := ⟨mem_ball_of_normSq h1, h2⟩

theorem normSq_gt_of_lin {x y : ℝ} (h : 5 < 3 * x + 4 * y) : 1 < x * x + y * y := by
  nlinarith [sq_nonneg (4 * x - 3 * y)]

/-- **The hexagon relation for the KZ associator.**  With `C = −A − B` and `A`, `B`, `C`
non-resonant, `e^{−iπA} Φ(C,A) e^{−iπC} Φ(B,C) e^{−iπB} Φ(A,B) = 1`.

Six solutions of `KZ(A,B)` (the normalised solutions at `0` and `1` of `KZ(A,B)`, `KZ(B,C)`,
`KZ(C,A)`, pulled back along the order-three rotation `z ↦ 1 − 1/z`) are compared in turn
around the fixed point `e^{iπ/3}`; consecutive ones differ by an associator or by a
half-monodromy, and going once around returns the first one. -/
theorem hexagon (A B : R)
    (hA : ∀ k : ℕ, 0 < k → Function.Injective (indicial A k))
    (hB : ∀ k : ℕ, 0 < k → Function.Injective (indicial B k))
    (hC : ∀ k : ℕ, 0 < k → Function.Injective (indicial (-A - B) k))
    (H₀ H₁ K₀ K₁ L₀ L₁ : ℕ → R)
    (h₀ : H₀ 0 = 1) (hH₀ : IsFormalGauge (kzM0 A B) H₀)
    (h₁ : H₁ 0 = 1) (hH₁ : IsFormalGauge (kzM0 B A) H₁)
    (k₀ : K₀ 0 = 1) (hK₀ : IsFormalGauge (kzM0 B (-A - B)) K₀)
    (k₁ : K₁ 0 = 1) (hK₁ : IsFormalGauge (kzM0 (-A - B) B) K₁)
    (l₀ : L₀ 0 = 1) (hL₀ : IsFormalGauge (kzM0 (-A - B) A) L₀)
    (l₁ : L₁ 0 = 1) (hL₁ : IsFormalGauge (kzM0 A (-A - B)) L₁) :
    eπ A * AssociatorKZ.phiKZ (-A - B) A L₀ L₁ l₀ hL₀ l₁ hL₁ * eπ (-A - B) *
      AssociatorKZ.phiKZ B (-A - B) K₀ K₁ k₀ hK₀ k₁ hK₁ * eπ B *
      AssociatorKZ.phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁ = 1 := by
  set C := -A - B with hCdef
  have eBC : -B - C = A := by rw [hCdef]; abel
  have eCA : -C - A = B := by rw [hCdef]; abel
  set ΦAB := AssociatorKZ.phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁
  set ΦBC := AssociatorKZ.phiKZ B C K₀ K₁ k₀ hK₀ k₁ hK₁
  set ΦCA := AssociatorKZ.phiKZ C A L₀ L₁ l₀ hL₀ l₁ hL₁
  -- the reference solution on the disc
  have hne : ∀ z ∈ Dh, z ≠ 0 ∧ z - 1 ≠ 0 := fun z hz =>
    ⟨ne_zero_of_im_pos hz.2, sub_ne_zero.mpr (ne_one_of_im_pos hz.2)⟩
  obtain ⟨N, hN, hNu, -⟩ := exists_reference (Ω := kzΩ A B)
    (Ω' := fun w : ℂ => (-(w ^ 2)⁻¹) • A + (-1 / (w - 1) ^ 2) • B) isOpen_Dh
    (convex_Dh.starConvex (mem_Dh (z := ⟨1 / 2, 9 / 10⟩) (by norm_num [Complex.normSq_apply]) (by norm_num)))
    (fun z hz => hasDerivAt_kzΩ A B (hne z hz).1 (hne z hz).2)
    (fun z hz => (continuousAt_kzΩ' A B (hne z hz).1 (hne z hz).2).continuousWithinAt)
  have hΩc : ContinuousOn (kzΩ A B) Dh := fun z hz =>
    (hasDerivAt_kzΩ A B (hne z hz).1 (hne z hz).2).continuousAt.continuousWithinAt
  have rep : ∀ (X : ℂ → R) (U : Set ℂ) (p : ℂ), Convex ℝ U → U ⊆ Dh → p ∈ U →
      (∀ z ∈ U, HasDerivAt X (kzΩ A B z * X z) z) → ∃ α : R, EqOn X (fun z => N z * α) U :=
    fun X U p hU hUD hp hX => ⟨_, eqOn_mul_of_isUnit hU (hΩc.mono hUD)
      (fun z hz => hN z (hUD hz)) hX hp (hNu p (hUD hp))⟩
  have link : ∀ {p : ℂ} {α β c x y : R}, p ∈ Dh → x = N p * α → y = N p * β → x = y * c →
      α = β * c := fun hp hx hy h =>
    (hNu _ hp).mul_left_cancel (by rw [← hx, h, hy, mul_assoc])
  -- the six convex pieces of the disc
  have cH : Convex ℝ {z : ℂ | 0 < z.im} := convex_halfSpace_gt Complex.imLm.isLinear 0
  have hQ1 : Convex ℝ (Metric.ball (0 : ℂ) 1 ∩ Dh) := (convex_ball _ _).inter convex_Dh
  have hQ2 : Convex ℝ (Metric.ball (1 : ℂ) 1 ∩ Dh) := (convex_ball _ _).inter convex_Dh
  have hQ3 : Convex ℝ ({z : ℂ | 1 / 2 < z.re} ∩ Dh) :=
    (convex_halfSpace_gt Complex.reLm.isLinear _).inter convex_Dh
  have hQ4 : Convex ℝ ({z : ℂ | 5 < 3 * z.re + 4 * z.im} ∩ Dh) :=
    (convex_lin_gt 3 4 5).inter convex_Dh
  have hQ5 : Convex ℝ ({z : ℂ | 2 < -3 * z.re + 4 * z.im} ∩ Dh) :=
    (convex_lin_gt (-3) 4 2).inter convex_Dh
  have hQ6 : Convex ℝ ({z : ℂ | z.re < 1 / 2} ∩ Dh) :=
    (convex_halfSpace_lt Complex.reLm.isLinear _).inter convex_Dh
  -- each of the six solutions solves `KZ(A, B)` on its piece
  have s1 : ∀ z ∈ Metric.ball (0 : ℂ) 1 ∩ Dh, HasDerivAt (G₀ A H₀) (kzΩ A B z * G₀ A H₀ z) z :=
    fun z hz => isKZSolOn_G₀ A B H₀ h₀ hH₀ z
      ⟨by simpa using hz.1, Complex.mem_slitPlane_iff.mpr (Or.inr hz.2.2.ne')⟩
  have s2 : ∀ z ∈ Metric.ball (1 : ℂ) 1 ∩ Dh, HasDerivAt (G₁ B H₁) (kzΩ A B z * G₁ B H₁ z) z :=
    fun z hz => isKZSolOn_G₁ A B H₁ h₁ hH₁ z
      ⟨by simpa [dist_eq_norm, norm_sub_rev] using hz.1,
        Complex.mem_slitPlane_iff.mpr (Or.inr (by simpa using hz.2.2.ne'))⟩
  have s3 : ∀ z ∈ {z : ℂ | 1 / 2 < z.re} ∩ Dh,
      HasDerivAt (fun z => G₀ B K₀ (rho z)) (kzΩ A B z * G₀ B K₀ (rho z)) z := by
    intro z hz
    have him : 0 < z.im := hz.2.2
    have hre : 1 / 2 < z.re := hz.1
    have hlt : Complex.normSq (z - 1) < Complex.normSq z := by
      rw [normSq_sub_one, Complex.normSq_apply]; nlinarith
    have h := hasDerivAt_comp_rho (ne_zero_of_im_pos him) (ne_one_of_im_pos him)
      (isKZSolOn_G₀ B C K₀ k₀ hK₀ _ (mem_D₀_rho him hlt))
    rw [eBC] at h; exact h
  have s4 : ∀ z ∈ {z : ℂ | 5 < 3 * z.re + 4 * z.im} ∩ Dh,
      HasDerivAt (fun z => G₁ C K₁ (rho z)) (kzΩ A B z * G₁ C K₁ (rho z)) z := by
    intro z hz
    have him : 0 < z.im := hz.2.2
    have hgt : 1 < Complex.normSq z := by
      rw [Complex.normSq_apply]; exact normSq_gt_of_lin hz.1
    have h := hasDerivAt_comp_rho (ne_zero_of_im_pos him) (ne_one_of_im_pos him)
      (isKZSolOn_G₁ B C K₁ k₁ hK₁ _ (mem_D₁_rho him hgt))
    rw [eBC] at h; exact h
  have s5 : ∀ z ∈ {z : ℂ | 2 < -3 * z.re + 4 * z.im} ∩ Dh,
      HasDerivAt (fun z => G₀ C L₀ (rho (rho z))) (kzΩ A B z * G₀ C L₀ (rho (rho z))) z := by
    intro z hz
    have him : 0 < z.im := hz.2.2
    have hz0 := ne_zero_of_im_pos him
    have hz1 := ne_one_of_im_pos him
    have hgt : 1 < Complex.normSq (1 - z) := by
      have h5 : 5 < 3 * (1 - z.re) + 4 * z.im := by have := hz.1; simp at this; linarith
      rw [normSq_one_sub]; exact normSq_gt_of_lin h5
    have h1 := isKZSolOn_G₀ C A L₀ l₀ hL₀ _ (mem_D₀_rho2 him hgt)
    have h2 := hasDerivAt_comp_rho (rho_ne_zero hz1) (rho_ne_one z hz0) h1
    have h3 := hasDerivAt_comp_rho (G := fun u => G₀ C L₀ (rho u)) hz0 hz1 h2
    rw [eCA, eBC] at h3; exact h3
  have s6 : ∀ z ∈ {z : ℂ | z.re < 1 / 2} ∩ Dh,
      HasDerivAt (fun z => G₁ A L₁ (rho (rho z))) (kzΩ A B z * G₁ A L₁ (rho (rho z))) z := by
    intro z hz
    have him : 0 < z.im := hz.2.2
    have hz0 := ne_zero_of_im_pos him
    have hz1 := ne_one_of_im_pos him
    have h1 := isKZSolOn_G₁ C A L₁ l₁ hL₁ _ (mem_D₁_rho2 him hz.1)
    have h2 := hasDerivAt_comp_rho (rho_ne_zero hz1) (rho_ne_one z hz0) h1
    have h3 := hasDerivAt_comp_rho (G := fun u => G₁ A L₁ (rho u)) hz0 hz1 h2
    rw [eCA, eBC] at h3; exact h3
  -- connection constants on the six pieces
  obtain ⟨α₁, e₁⟩ := rep _ _ ⟨1 / 2, 4 / 5⟩ hQ1 inter_subset_right
    ⟨mem_ball_of_normSq (by norm_num [Complex.normSq_apply]),
      mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)⟩ s1
  obtain ⟨α₂, e₂⟩ := rep _ _ ⟨1 / 2, 4 / 5⟩ hQ2 inter_subset_right
    ⟨mem_ball_of_normSq (by norm_num [Complex.normSq_apply]),
      mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)⟩ s2
  obtain ⟨α₃, e₃⟩ := rep _ _ ⟨3 / 5, 4 / 5⟩ hQ3 inter_subset_right
    ⟨by norm_num, mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)⟩ s3
  obtain ⟨α₄, e₄⟩ := rep _ _ ⟨3 / 5, 9 / 10⟩ hQ4 inter_subset_right
    ⟨by norm_num, mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)⟩ s4
  obtain ⟨α₅, e₅⟩ := rep _ _ ⟨1 / 2, 1⟩ hQ5 inter_subset_right
    ⟨by norm_num, mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)⟩ s5
  obtain ⟨α₆, e₆⟩ := rep _ _ ⟨2 / 5, 9 / 10⟩ hQ6 inter_subset_right
    ⟨by norm_num, mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)⟩ s6
  -- c₁ : the associator `Φ(A,B)` at `p₁ = 1/2 + 4i/5`
  have r1 : α₁ = α₂ * ΦAB := by
    have hp : (⟨1 / 2, 4 / 5⟩ : ℂ) ∈ Dh :=
      mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)
    refine link hp (e₁ ⟨mem_ball_of_normSq (by norm_num [Complex.normSq_apply]), hp⟩)
      (e₂ ⟨mem_ball_of_normSq (by norm_num [Complex.normSq_apply]), hp⟩)
      (lens_rel A B H₀ H₁ h₀ hH₀ h₁ hH₁
        ⟨mem_ball_of_normSq (by norm_num [Complex.normSq_apply]),
          mem_ball_of_normSq (by norm_num [Complex.normSq_apply])⟩)
  -- c₂ : half-monodromy of `KZ(B, C)` at `p₂ = 3/5 + 4i/5`
  have r2 : α₂ = α₃ * eπ B := by
    have hp : (⟨3 / 5, 4 / 5⟩ : ℂ) ∈ Dh :=
      mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)
    have him : (0 : ℝ) < (⟨3 / 5, 4 / 5⟩ : ℂ).im := by norm_num
    have h := half_monodromy B C hB K₀ H₁ k₀ hK₀ h₁ (by rw [eBC]; exact hH₁)
      (mem_T_rho him (by norm_num [Complex.normSq_apply]) (by norm_num [Complex.normSq_apply]))
    beta_reduce at h
    rw [rho_rho_rho (ne_zero_of_im_pos him) (ne_one_of_im_pos him)] at h
    exact link hp (e₂ ⟨mem_ball_of_normSq (by norm_num [Complex.normSq_apply]), hp⟩)
      (e₃ ⟨by norm_num, hp⟩) h
  -- c₃ : the associator `Φ(B,C)` at `p₃ = 3/5 + 9i/10`
  have r3 : α₃ = α₄ * ΦBC := by
    have hp : (⟨3 / 5, 9 / 10⟩ : ℂ) ∈ Dh :=
      mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)
    have him : (0 : ℝ) < (⟨3 / 5, 9 / 10⟩ : ℂ).im := by norm_num
    exact link hp (e₃ ⟨by norm_num, hp⟩) (e₄ ⟨by norm_num, hp⟩)
      (lens_rel B C K₀ K₁ k₀ hK₀ k₁ hK₁
        (mem_L_rho him (by norm_num [Complex.normSq_apply]) (by norm_num [Complex.normSq_apply])))
  -- c₄ : half-monodromy of `KZ(C, A)` at `p₄ = 1/2 + i`
  have r4 : α₄ = α₅ * eπ C := by
    have hp : (⟨1 / 2, 1⟩ : ℂ) ∈ Dh :=
      mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)
    have him : (0 : ℝ) < (⟨1 / 2, 1⟩ : ℂ).im := by norm_num
    have h := half_monodromy C A hC L₀ K₁ l₀ hL₀ k₁ (by rw [eCA]; exact hK₁)
      (mem_T_rho2 him (by norm_num [Complex.normSq_apply]) (by norm_num [Complex.normSq_apply]))
    beta_reduce at h
    rw [rho_rho_rho (rho_ne_zero (ne_one_of_im_pos him))
      (rho_ne_one _ (ne_zero_of_im_pos him))] at h
    exact link hp (e₄ ⟨by norm_num, hp⟩) (e₅ ⟨by norm_num, hp⟩) h
  -- c₅ : the associator `Φ(C,A)` at `p₅ = 2/5 + 9i/10`
  have r5 : α₅ = α₆ * ΦCA := by
    have hp : (⟨2 / 5, 9 / 10⟩ : ℂ) ∈ Dh :=
      mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)
    have him : (0 : ℝ) < (⟨2 / 5, 9 / 10⟩ : ℂ).im := by norm_num
    exact link hp (e₅ ⟨by norm_num, hp⟩) (e₆ ⟨by norm_num, hp⟩)
      (lens_rel C A L₀ L₁ l₀ hL₀ l₁ hL₁
        (mem_L_rho2 him (by norm_num [Complex.normSq_apply]) (by norm_num [Complex.normSq_apply])))
  -- c₆ : half-monodromy of `KZ(A, B)` at `p₆ = 2/5 + 4i/5`
  have r6 : α₆ = α₁ * eπ A := by
    have hp : (⟨2 / 5, 4 / 5⟩ : ℂ) ∈ Dh :=
      mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)
    have hT : (⟨2 / 5, 4 / 5⟩ : ℂ) ∈ T :=
      ⟨⟨by norm_num, mem_ball_of_normSq (by norm_num [Complex.normSq_apply])⟩, by norm_num⟩
    exact link hp (e₆ ⟨by norm_num, hp⟩)
      (e₁ ⟨mem_ball_of_normSq (by norm_num [Complex.normSq_apply]), hp⟩)
      (half_monodromy A B hA H₀ L₁ h₀ hH₀ l₁ hL₁ hT)
  -- once around: `α₁ = α₁ Q`
  set Q := eπ A * ΦCA * eπ C * ΦBC * eπ B * ΦAB with hQ
  have hloop : α₁ = α₁ * Q := by
    calc α₁ = α₂ * ΦAB := r1
      _ = α₃ * eπ B * ΦAB := by rw [r2]
      _ = α₄ * ΦBC * eπ B * ΦAB := by rw [r3]
      _ = α₅ * eπ C * ΦBC * eπ B * ΦAB := by rw [r4]
      _ = α₆ * ΦCA * eπ C * ΦBC * eπ B * ΦAB := by rw [r5]
      _ = α₁ * eπ A * ΦCA * eπ C * ΦBC * eπ B * ΦAB := by rw [r6]
      _ = α₁ * Q := by simp only [hQ, mul_assoc]
  -- hence `G₀ = G₀ Q` on the upper half of the unit disc
  have U0c : Convex ℝ (Metric.ball (0 : ℂ) 1 ∩ {z : ℂ | 0 < z.im}) := (convex_ball _ _).inter cH
  have hsol : ∀ z ∈ Metric.ball (0 : ℂ) 1 ∩ {z : ℂ | 0 < z.im},
      HasDerivAt (G₀ A H₀) (kzΩ A B z * G₀ A H₀ z) z := fun z hz =>
    isKZSolOn_G₀ A B H₀ h₀ hH₀ z
      ⟨by simpa using hz.1, Complex.mem_slitPlane_iff.mpr (Or.inr (ne_of_gt hz.2))⟩
  have hp1 : (⟨1 / 2, 4 / 5⟩ : ℂ) ∈ Metric.ball (0 : ℂ) 1 ∩ Dh :=
    ⟨mem_ball_of_normSq (by norm_num [Complex.normSq_apply]),
      mem_Dh (by norm_num [Complex.normSq_apply]) (by norm_num)⟩
  have hext := eqOn_of_convex U0c
    (fun z hz => (hasDerivAt_kzΩ A B (ne_zero_of_im_pos hz.2)
      (sub_ne_zero.mpr (ne_one_of_im_pos hz.2))).continuousAt.continuousWithinAt)
    hsol (fun z hz => by simpa [mul_assoc] using (hsol z hz).mul_const Q)
    (c := ⟨1 / 2, 4 / 5⟩) ⟨hp1.1, hp1.2.2⟩
    (by show G₀ A H₀ _ = G₀ A H₀ _ * Q; rw [e₁ hp1]; beta_reduce; rw [mul_assoc, ← hloop])
  -- near `0` the solution `G₀` is invertible, so `Q = 1`
  have hcont : ContinuousAt (cseries H₀) 0 :=
    (hasDerivAt_cseries (FuchsianAnalytic.boundedOn_kz_solution A B H₀ h₀ hH₀) (by simp)).continuousAt
  have hu0 : IsUnit (cseries H₀ 0) := by rw [cseries_zero, h₀]; exact isUnit_one
  obtain ⟨ε, hε, hball⟩ := Metric.eventually_nhds_iff.mp
    (hcont.eventually (Units.isOpen.mem_nhds hu0))
  set t : ℝ := min ε 1 / 2 with ht
  have ht0 : 0 < t := by positivity
  have htε : t < ε := by have := min_le_left ε 1; linarith
  have ht1 : t < 1 := by have := min_le_right ε 1; linarith
  set w : ℂ := ⟨0, t⟩ with hw
  have hnw : ‖w‖ = t := by
    rw [← sq_eq_sq₀ (norm_nonneg _) ht0.le, Complex.sq_norm, Complex.normSq_apply]; simp [hw]; ring
  have hwU : w ∈ Metric.ball (0 : ℂ) 1 ∩ {z : ℂ | 0 < z.im} :=
    ⟨by simpa [hnw] using ht1, by simpa [hw] using ht0⟩
  have hu : IsUnit (G₀ A H₀ w) :=
    (hball (by simpa [dist_eq_norm, hnw] using htε)).mul (isUnit_cpowA A w)
  exact (hu.mul_left_cancel ((hext hwU).symm.trans (mul_one _).symm))

end Hexagon

end QOU.KZ.KZHexagon
