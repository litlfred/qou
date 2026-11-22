import QOU.Archimedean.BlochRigidity.Abstract
import QOU.Archimedean.BlochRigidity.ReebPlane
import QOU.MathlibExt.Dolbeault
import QOU.Archimedean.BlochRigidity.Regularity
import QOU.Archimedean.BlochRigidity.Instance

/-!
# The smooth instance of the Dolbeault structure

The fibre is the real cotangent space `ℂ →L[ℝ] ℂ`, the class is "smooth on an open
neighbourhood", and `d = fderiv ℝ`. The complex structure `J` is precomposition with the
rotation by `i`, which is the Reeb operator `reebM_i` of the Bring cone restricted to the plane
`span(1, i)` (`reebRot_ofComplex`); `dz̄` is complex conjugation, the restriction of the real
structures `realStr (orthW c d)` (`realStr_ofComplex`).
-/

open Complex Filter Topology

namespace QOU.Archimedean.BlochRigidity

open QOU.Tetraplectic

/-- Rotation by `i`, as a real-linear map of the plane. -/
noncomputable def reebRot : ℂ →L[ℝ] ℂ := (I • ContinuousLinearMap.id ℂ ℂ).restrictScalars ℝ

theorem reebRot_apply (v : ℂ) : reebRot v = I * v := by simp [reebRot]

/-- `reebRot` is the Reeb operator `reebM_i` of the Bring cone, restricted to the plane. -/
theorem reebRot_ofComplex (v : ℂ) : ofComplex (reebRot v) = reebM_i (ofComplex v) := by
  rw [reebRot_apply, reebM_i_ofComplex]

/-- `dz̄`, complex conjugation, is the restriction of each real structure `realStr (orthW c d)`. -/
theorem conjCLE_ofComplex {c d : ℝ} (h : c * c + d * d = 1) (v : ℂ) :
    ofComplex (conjCLE.toContinuousLinearMap v) = realStr (orthW c d) (ofComplex v) := by
  rw [realStr_ofComplex h]; rfl

/-- The smooth class: `f` is `C^∞` on an open neighbourhood of `z`. -/
def SmoothNear (z : ℂ) (f : ℂ → ℂ) : Prop :=
  ∃ U : Set ℂ, IsOpen U ∧ z ∈ U ∧ ContDiffOn ℝ (⊤ : ℕ∞) f U

namespace SmoothNear

theorem contDiffAt {z : ℂ} {f : ℂ → ℂ} (h : SmoothNear z f) : ContDiffAt ℝ (⊤ : ℕ∞) f z := by
  obtain ⟨U, hU, hz, hf⟩ := h
  exact hf.contDiffAt (hU.mem_nhds hz)

theorem differentiableAt {z : ℂ} {f : ℂ → ℂ} (h : SmoothNear z f) : DifferentiableAt ℝ f z :=
  h.contDiffAt.differentiableAt (by simp)

end SmoothNear

/-- The `dz`-coordinate of a real-linear map. -/
noncomputable def cOne : (ℂ →L[ℝ] ℂ) →ₗ[ℂ] ℂ where
  toFun α := (α 1 - I * α I) / 2
  map_add' α β := by simp only [ContinuousLinearMap.add_apply]; ring
  map_smul' c α := by simp only [ContinuousLinearMap.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

/-- The `dz̄`-coordinate of a real-linear map. -/
noncomputable def cTwo : (ℂ →L[ℝ] ℂ) →ₗ[ℂ] ℂ where
  toFun α := (α 1 + I * α I) / 2
  map_add' α β := by simp only [ContinuousLinearMap.add_apply]; ring
  map_smul' c α := by simp only [ContinuousLinearMap.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

/-- Precomposition with `reebRot`. -/
noncomputable def reebJ : (ℂ →L[ℝ] ℂ) →ₗ[ℂ] (ℂ →L[ℝ] ℂ) where
  toFun α := α.comp reebRot
  map_add' α β := by ext; simp
  map_smul' c α := by ext; simp

theorem reebJ_apply (α : ℂ →L[ℝ] ℂ) (v : ℂ) : reebJ α v = α (I * v) := by
  simp [reebJ, reebRot_apply]

theorem decomp_apply (α : ℂ →L[ℝ] ℂ) (v : ℂ) :
    α v = cOne α * v + cTwo α * (starRingEnd ℂ) v :=
  QOU.MathlibExt.Dolbeault.rlinear_eq α v

theorem ext_c {α β : ℂ →L[ℝ] ℂ} (h1 : cOne α = cOne β) (h2 : cTwo α = cTwo β) : α = β := by
  ext1 v; rw [decomp_apply α, decomp_apply β, h1, h2]

theorem cOne_fderiv (f : ℂ → ℂ) (z : ℂ) :
    cOne (fderiv ℝ f z) = QOU.MathlibExt.Dolbeault.dz f z := rfl

theorem cTwo_fderiv (f : ℂ → ℂ) (z : ℂ) :
    cTwo (fderiv ℝ f z) = QOU.MathlibExt.Dolbeault.dzbar f z := rfl


/-- `dz` as a real-linear map: the identity. -/
noncomputable def eZ : ℂ →L[ℝ] ℂ := ContinuousLinearMap.id ℝ ℂ

/-- `dz̄` as a real-linear map: complex conjugation. -/
noncomputable def eZbar : ℂ →L[ℝ] ℂ := conjCLE.toContinuousLinearMap

@[simp] theorem eZ_apply (v : ℂ) : eZ v = v := rfl
@[simp] theorem eZbar_apply (v : ℂ) : eZbar v = (starRingEnd ℂ) v := rfl

namespace SmoothNear

variable {z : ℂ} {f g : ℂ → ℂ}

theorem congr (hf : SmoothNear z f) (h : f =ᶠ[𝓝 z] g) : SmoothNear z g := by
  obtain ⟨U, hU, hz, hfU⟩ := hf
  obtain ⟨t, ht, htop, hzt⟩ := eventually_nhds_iff.1 h
  exact ⟨U ∩ t, hU.inter htop, ⟨hz, hzt⟩,
    (hfU.mono Set.inter_subset_left).congr fun y hy => (ht y hy.2).symm⟩

theorem nhds (hf : SmoothNear z f) : ∀ᶠ w in 𝓝 z, SmoothNear w f := by
  obtain ⟨U, hU, hz, hfU⟩ := hf
  filter_upwards [hU.mem_nhds hz] with w hw
  exact ⟨U, hU, hw, hfU⟩

theorem add (hf : SmoothNear z f) (hg : SmoothNear z g) : SmoothNear z (fun w => f w + g w) := by
  obtain ⟨U, hU, hz, hfU⟩ := hf
  obtain ⟨V, hV, hzV, hgV⟩ := hg
  exact ⟨U ∩ V, hU.inter hV, ⟨hz, hzV⟩,
    (hfU.mono Set.inter_subset_left).add (hgV.mono Set.inter_subset_right)⟩

theorem mul (hf : SmoothNear z f) (hg : SmoothNear z g) : SmoothNear z (fun w => f w * g w) := by
  obtain ⟨U, hU, hz, hfU⟩ := hf
  obtain ⟨V, hV, hzV, hgV⟩ := hg
  exact ⟨U ∩ V, hU.inter hV, ⟨hz, hzV⟩,
    (hfU.mono Set.inter_subset_left).mul (hgV.mono Set.inter_subset_right)⟩

theorem analyticNhd (hg : AnalyticAt ℂ g z) :
    ∃ t : Set ℂ, IsOpen t ∧ z ∈ t ∧ AnalyticOnNhd ℂ g t := by
  obtain ⟨t, ht, htop, hzt⟩ := eventually_nhds_iff.1 hg.eventually_analyticAt
  exact ⟨t, htop, hzt, ht⟩

theorem holo (hg : AnalyticAt ℂ g z) : SmoothNear z g := by
  obtain ⟨t, htop, hzt, ht⟩ := analyticNhd hg
  exact ⟨t, htop, hzt, (ht.contDiffOn (n := ((⊤ : ℕ∞) : WithTop ℕ∞)) htop.uniqueDiffOn).restrict_scalars ℝ⟩

theorem comp (hg : AnalyticAt ℂ g z) (hf : SmoothNear (g z) f) :
    SmoothNear z (fun w => f (g w)) := by
  obtain ⟨t, htop, hzt, ht⟩ := analyticNhd hg
  obtain ⟨U, hU, hgz, hfU⟩ := hf
  have hgc : ContinuousOn g t := ht.continuousOn
  have hgs : ContDiffOn ℝ (⊤ : ℕ∞) g t :=
    (ht.contDiffOn (n := ((⊤ : ℕ∞) : WithTop ℕ∞)) htop.uniqueDiffOn).restrict_scalars ℝ
  exact ⟨t ∩ g ⁻¹' U, hgc.isOpen_inter_preimage htop hU, ⟨hzt, hgz⟩,
    hfU.comp (hgs.mono Set.inter_subset_left) fun y hy => hy.2⟩

theorem conj (hf : SmoothNear z f) : SmoothNear z (fun w => (starRingEnd ℂ) (f w)) := by
  obtain ⟨U, hU, hz, hfU⟩ := hf
  exact ⟨U, hU, hz, conjCLE.contDiff.comp_contDiffOn hfU⟩

theorem dz (hf : SmoothNear z f) : SmoothNear z (fun w => cOne (fderiv ℝ f w)) := by
  obtain ⟨U, hU, hz, hfU⟩ := hf
  have hd : ContDiffOn ℝ (⊤ : ℕ∞) (fun y => fderiv ℝ f y) U :=
    hfU.fderiv_of_isOpen hU (by simp)
  refine ⟨U, hU, hz, ?_⟩
  show ContDiffOn ℝ (⊤ : ℕ∞) (fun w => (fderiv ℝ f w 1 - I * fderiv ℝ f w I) / 2) U
  exact ((hd.clm_apply contDiffOn_const).sub
    (contDiffOn_const.mul (hd.clm_apply contDiffOn_const))).div_const 2

end SmoothNear

/-- **The smooth Dolbeault structure.** -/
noncomputable def smoothDolbeault : DolbeaultStructure where
  M := ℂ →L[ℝ] ℂ
  J := reebJ
  J_sq α := by ext v; simp [reebJ_apply, ← mul_assoc]
  e := eZ
  ebar := eZbar
  J_e := by ext v; simp [reebJ_apply]
  J_ebar := by ext v; simp [reebJ_apply]
  e_ne h := by have := congrArg (fun L : ℂ →L[ℝ] ℂ => L 1) h; simp at this
  ebar_ne h := by have := congrArg (fun L : ℂ →L[ℝ] ℂ => L 1) h; simp at this
  c₁ := cOne
  c₂ := cTwo
  proj₁ α := by
    ext v
    have h1 := decomp_apply α v
    have h2 := decomp_apply α (I * v)
    simp only [ContinuousLinearMap.smul_apply, ContinuousLinearMap.sub_apply,
      reebJ_apply, eZ_apply, smul_eq_mul, map_mul, conj_I] at h2 ⊢
    rw [h1, h2]
    ring_nf; rw [I_sq]; ring
  proj₂ α := by
    ext v
    have h1 := decomp_apply α v
    have h2 := decomp_apply α (I * v)
    simp only [ContinuousLinearMap.smul_apply, ContinuousLinearMap.add_apply,
      reebJ_apply, eZbar_apply, smul_eq_mul, map_mul, conj_I] at h2 ⊢
    rw [h1, h2]
    ring_nf; rw [I_sq]; ring
  mem := SmoothNear
  d f z := fderiv ℝ f z
  mem_congr := SmoothNear.congr
  mem_nhds := SmoothNear.nhds
  mem_add := SmoothNear.add
  mem_mul := SmoothNear.mul
  mem_holo := SmoothNear.holo
  mem_comp := SmoothNear.comp
  mem_conj := SmoothNear.conj
  mem_dz := SmoothNear.dz
  d_congr h := h.fderiv_eq
  d_add hf hg := fderiv_fun_add hf.differentiableAt hg.differentiableAt
  d_mul {z f g} hf hg := by
    ext v
    rw [fderiv_fun_mul hf.differentiableAt hg.differentiableAt]
  d_holo {z h} hh := by
    rw [(hh.differentiableAt.hasDerivAt.hasFDerivAt.restrictScalars ℝ).fderiv]
    ext v; simp [mul_comm]
  d_comp {z f g} hg hf := by
    rw [(QOU.MathlibExt.Dolbeault.hasFDerivAt_comp_holo hf.differentiableAt
      hg.differentiableAt.hasDerivAt).fderiv]
    ext v
    simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.coe_restrictScalars',
      ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.one_apply, smul_eq_mul,
      ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply, eZ_apply, eZbar_apply]
    rw [decomp_apply]
    simp only [map_mul]
    ring
  d_conj {z f} hf := by
    have H : HasFDerivAt (fun w => (starRingEnd ℂ) (f w))
        (conjCLE.toContinuousLinearMap.comp (fderiv ℝ f z)) z :=
      conjCLE.hasFDerivAt.comp z hf.differentiableAt.hasFDerivAt
    rw [H.fderiv]
    ext v
    simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.add_apply,
      ContinuousLinearMap.smul_apply, eZ_apply, eZbar_apply, smul_eq_mul]
    rw [decomp_apply (fderiv ℝ f z) v]
    simp only [ContinuousLinearEquiv.coe_coe, conjCLE_apply, map_add, map_mul,
      Complex.conj_conj]
    ring
  d_comm {z f} hf := by
    show QOU.MathlibExt.Dolbeault.dzbar (QOU.MathlibExt.Dolbeault.dz f) z
      = QOU.MathlibExt.Dolbeault.dz (QOU.MathlibExt.Dolbeault.dzbar f) z
    exact QOU.MathlibExt.Dolbeault.dzbar_dz_eq_dz_dzbar (hf.contDiffAt.of_le (WithTop.coe_le_coe.2 le_top))
  cont hf := hf.contDiffAt.continuousAt
  cauchyRiemann hf h := (QOU.MathlibExt.Dolbeault.dzbar_eq_zero_iff hf.differentiableAt).1 h
  const hU hpre h z hz w hw :=
    hU.is_const_of_fderiv_eq_zero (𝕜 := ℝ) hpre
      (fun y hy => (h y hy).1.differentiableAt.differentiableWithinAt) (fun y hy => (h y hy).2)
      hz hw

/-- A continuous solution is in the smooth class (Proposition R). -/
theorem inClass_smooth_of_fiveTerm {φ : ℂ → ℝ} (hφ : ContinuousOn φ {0, 1}ᶜ)
    (hs : BlochSymmetric φ) (h5 : SuslinFiveTerm φ) :
    DolbeaultStructure.InClass smoothDolbeault φ := by
  have hd := contDiffOn_of_fiveTerm hφ hs.inv h5
  intro z h0 h1
  exact ⟨{0, 1}ᶜ, isOpen_U, mem_U'.2 ⟨h0, h1⟩, ofRealCLM.contDiff.comp_contDiffOn hd⟩

/-- **Bloch–Suslin rigidity, from the abstract theorem.** Continuous solutions are smooth
(Proposition R), so `eq_mul_of_fiveTermS` for `smoothDolbeault` applies. -/
theorem blochSuslinRigidity_of_smooth {D : ℂ → ℝ} (hDc : ContinuousOn D {0, 1}ᶜ)
    (hDs : BlochSymmetric D) (hD5 : SuslinFiveTerm D) {z₀ : ℂ} (hz₀0 : z₀ ≠ 0) (hz₀1 : z₀ ≠ 1)
    (hDz : D z₀ ≠ 0) : BlochSuslinRigidity D :=
  ⟨fun _ hφc hφs hφ5 => DolbeaultStructure.eq_mul_of_fiveTermS
    (inClass_smooth_of_fiveTerm hDc hDs hD5) hDs hD5 hz₀0 hz₀1 hDz
    (inClass_smooth_of_fiveTerm hφc hφs hφ5) hφs hφ5⟩

/-- The Bloch–Wigner function, through the abstract theorem: the same conclusion as the
instance `blochSuslinRigidity_blochD`, now as one instance of the Dolbeault-conditional
statement. -/
theorem blochSuslinRigidity_blochD_via_dolbeault :
    BlochSuslinRigidity FiveTermProof.blochD :=
  blochSuslinRigidity_of_smooth FiveTermProof.continuousOn_blochD
    FiveTermProof.blochSymmetric_blochD blochWignerFiveTerm_blochD.five_term I_ne_zero
    (by intro h; have := congrArg Complex.im h; simp at this)
    FiveTermProof.blochD_I_pos.ne'

end QOU.Archimedean.BlochRigidity

