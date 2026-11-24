import Mathlib.Analysis.Calculus.FDeriv.Symmetric
import Mathlib.Analysis.Calculus.FDeriv.Mul
import Mathlib.Analysis.Complex.RealDeriv

/-!
# The Wirtinger (Dolbeault) operators `∂` and `∂̄` on `ℂ`

Mathlib has no Dolbeault complex. This file gives its degree-0 part on the complex line: for a
function `f : ℂ → ℂ`, real-differentiable at `z`,

* `dz f z  = (∂f/∂x − i ∂f/∂y)/2`,
* `dzbar f z = (∂f/∂x + i ∂f/∂y)/2`,

so that the real derivative splits as `df_z(v) = ∂f(z)·v + ∂̄f(z)·v̄`
(`fderiv_eq_dz_add_dzbar`). The analytic facts are proved here once, from Mathlib:

* `dzbar_eq_zero_iff`: `∂̄f(z) = 0` iff `f` is complex-differentiable at `z`
  (Cauchy–Riemann);
* `dz_of_differentiableAt`: then `∂f(z) = f'(z)`;
* `dz_comp_holo`, `dzbar_comp_holo`: pullback along a holomorphic map
  (`∂(f∘g) = (∂f∘g)·g'`, `∂̄(f∘g) = (∂̄f∘g)·conj g'`);
* `dz_add`, `dz_sub`, `dz_const_mul` and the `dzbar` versions, `dzbar_mul_holo`: linearity and
  the Leibniz rule against a holomorphic factor;
* `dzbar_dz_eq_dz_dzbar`: `∂̄∂ = ∂∂̄` on `C²` functions (symmetry of the second derivative);
* `dzbar_ofReal`, `dzbar_dz_ofReal_im`: for real-valued `φ`, `∂̄φ = conj ∂φ` and
  `∂̄∂φ` is real (it is `Δφ/4`).

Everything downstream can then be done with these identities and algebra.
-/

open Complex

namespace QOU.MathlibExt.Dolbeault

/-- `∂f(z) = (∂ₓf − i ∂ᵧf)/2`. -/
noncomputable def dz (f : ℂ → ℂ) (z : ℂ) : ℂ := (fderiv ℝ f z 1 - I * fderiv ℝ f z I) / 2

/-- `∂̄f(z) = (∂ₓf + i ∂ᵧf)/2`. -/
noncomputable def dzbar (f : ℂ → ℂ) (z : ℂ) : ℂ := (fderiv ℝ f z 1 + I * fderiv ℝ f z I) / 2

/-- Every real-linear `ℂ → ℂ` is `v ↦ a v + b v̄`. -/
theorem rlinear_eq (L : ℂ →L[ℝ] ℂ) (v : ℂ) :
    L v = (L 1 - I * L I) / 2 * v + (L 1 + I * L I) / 2 * (starRingEnd ℂ) v := by
  have hv : v = (v.re : ℝ) • (1 : ℂ) + (v.im : ℝ) • I := by
    apply Complex.ext <;> simp
  conv_lhs => rw [hv]
  rw [map_add, map_smul, map_smul]
  conv_rhs => rw [hv]
  simp only [Complex.real_smul, map_add, map_mul, Complex.conj_ofReal, map_one, Complex.conj_I]
  ring_nf
  rw [Complex.I_sq]
  ring

/-- **The type decomposition of `df`.** -/
theorem fderiv_eq_dz_add_dzbar (f : ℂ → ℂ) (z v : ℂ) :
    fderiv ℝ f z v = dz f z * v + dzbar f z * (starRingEnd ℂ) v :=
  rlinear_eq _ v

/-- The coefficients are determined by any real derivative. -/
theorem dz_dzbar_of_hasFDerivAt {f : ℂ → ℂ} {z : ℂ} {L : ℂ →L[ℝ] ℂ}
    (h : HasFDerivAt f L z) :
    dz f z = (L 1 - I * L I) / 2 ∧ dzbar f z = (L 1 + I * L I) / 2 := by
  simp [dz, dzbar, h.fderiv]

/-- **Cauchy–Riemann.** `∂̄f(z) = 0` iff `f` is complex-differentiable at `z`. -/
theorem dzbar_eq_zero_iff {f : ℂ → ℂ} {z : ℂ} (hf : DifferentiableAt ℝ f z) :
    dzbar f z = 0 ↔ DifferentiableAt ℂ f z := by
  constructor
  · intro h
    refine (differentiableAt_iff_restrictScalars ℝ hf).2 ⟨dz f z • ContinuousLinearMap.id ℂ ℂ, ?_⟩
    ext w
    simp only [ContinuousLinearMap.coe_restrictScalars', ContinuousLinearMap.coe_smul',
      ContinuousLinearMap.coe_id', Pi.smul_apply, id_eq, smul_eq_mul]
    rw [fderiv_eq_dz_add_dzbar, h, zero_mul, add_zero]
  · intro h
    have hL := h.hasFDerivAt.restrictScalars ℝ
    rw [(dz_dzbar_of_hasFDerivAt hL).2]
    simp only [ContinuousLinearMap.coe_restrictScalars']
    rw [show (fderiv ℂ f z) I = I * fderiv ℂ f z 1 by
      rw [← smul_eq_mul, ← map_smul, smul_eq_mul, mul_one]]
    ring_nf
    rw [I_sq]
    ring

/-- For a holomorphic `f`, `∂f = f'`. -/
theorem dz_of_hasDerivAt {f : ℂ → ℂ} {f' z : ℂ} (h : HasDerivAt f f' z) : dz f z = f' := by
  have hL := h.hasFDerivAt.restrictScalars ℝ
  rw [(dz_dzbar_of_hasFDerivAt hL).1]
  simp only [ContinuousLinearMap.coe_restrictScalars', ContinuousLinearMap.smulRight_apply,
    ContinuousLinearMap.one_apply, smul_eq_mul, one_mul]
  ring_nf
  rw [I_sq]
  ring

/-- The derivative of `f ∘ g`, `g` holomorphic, as a real-linear map. -/
theorem hasFDerivAt_comp_holo {f g : ℂ → ℂ} {g' z : ℂ} (hf : DifferentiableAt ℝ f (g z))
    (hg : HasDerivAt g g' z) :
    HasFDerivAt (fun w => f (g w))
      ((fderiv ℝ f (g z)).comp
        ((ContinuousLinearMap.smulRight (1 : ℂ →L[ℂ] ℂ) g').restrictScalars ℝ)) z :=
  hf.hasFDerivAt.comp z (hg.hasFDerivAt.restrictScalars ℝ)

/-- **Pullback of `∂`** along a holomorphic map. -/
theorem dz_comp_holo {f g : ℂ → ℂ} {g' z : ℂ} (hf : DifferentiableAt ℝ f (g z))
    (hg : HasDerivAt g g' z) : dz (fun w => f (g w)) z = dz f (g z) * g' := by
  rw [(dz_dzbar_of_hasFDerivAt (hasFDerivAt_comp_holo hf hg)).1]
  simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.coe_restrictScalars',
    ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.one_apply, smul_eq_mul, one_mul,
    fderiv_eq_dz_add_dzbar f (g z), map_mul, conj_I]
  ring_nf
  rw [I_sq]
  ring

/-- **Pullback of `∂̄`** along a holomorphic map. -/
theorem dzbar_comp_holo {f g : ℂ → ℂ} {g' z : ℂ} (hf : DifferentiableAt ℝ f (g z))
    (hg : HasDerivAt g g' z) :
    dzbar (fun w => f (g w)) z = dzbar f (g z) * (starRingEnd ℂ) g' := by
  rw [(dz_dzbar_of_hasFDerivAt (hasFDerivAt_comp_holo hf hg)).2]
  simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.coe_restrictScalars',
    ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.one_apply, smul_eq_mul, one_mul,
    fderiv_eq_dz_add_dzbar f (g z), map_mul, conj_I]
  ring_nf
  rw [I_sq]
  ring

theorem dz_sub {f g : ℂ → ℂ} {z : ℂ} (hf : DifferentiableAt ℝ f z) (hg : DifferentiableAt ℝ g z) :
    dz (fun w => f w - g w) z = dz f z - dz g z := by
  simp only [dz, fderiv_fun_sub hf hg, ContinuousLinearMap.sub_apply]; ring

theorem dzbar_sub {f g : ℂ → ℂ} {z : ℂ} (hf : DifferentiableAt ℝ f z)
    (hg : DifferentiableAt ℝ g z) : dzbar (fun w => f w - g w) z = dzbar f z - dzbar g z := by
  simp only [dzbar, fderiv_fun_sub hf hg, ContinuousLinearMap.sub_apply]; ring

theorem dz_add {f g : ℂ → ℂ} {z : ℂ} (hf : DifferentiableAt ℝ f z) (hg : DifferentiableAt ℝ g z) :
    dz (fun w => f w + g w) z = dz f z + dz g z := by
  simp only [dz, fderiv_fun_add hf hg, ContinuousLinearMap.add_apply]; ring

theorem dzbar_add {f g : ℂ → ℂ} {z : ℂ} (hf : DifferentiableAt ℝ f z)
    (hg : DifferentiableAt ℝ g z) : dzbar (fun w => f w + g w) z = dzbar f z + dzbar g z := by
  simp only [dzbar, fderiv_fun_add hf hg, ContinuousLinearMap.add_apply]; ring

theorem dz_const_mul {f : ℂ → ℂ} {z : ℂ} (hf : DifferentiableAt ℝ f z) (c : ℂ) :
    dz (fun w => c * f w) z = c * dz f z := by
  simp only [dz, fderiv_const_mul hf c, ContinuousLinearMap.smul_apply, smul_eq_mul]; ring

theorem dzbar_const_mul {f : ℂ → ℂ} {z : ℂ} (hf : DifferentiableAt ℝ f z) (c : ℂ) :
    dzbar (fun w => c * f w) z = c * dzbar f z := by
  simp only [dzbar, fderiv_const_mul hf c, ContinuousLinearMap.smul_apply, smul_eq_mul]; ring

theorem dzbar_const (c z : ℂ) : dzbar (fun _ => c) z = 0 := by simp [dzbar]

/-- **Leibniz against a holomorphic factor:** `∂̄(f·h) = (∂̄f)·h` when `h` is holomorphic. -/
theorem dzbar_mul_holo {f h : ℂ → ℂ} {h' z : ℂ} (hf : DifferentiableAt ℝ f z)
    (hh : HasDerivAt h h' z) : dzbar (fun w => f w * h w) z = dzbar f z * h z := by
  have H := hf.hasFDerivAt.mul (hh.hasFDerivAt.restrictScalars ℝ)
  rw [(dz_dzbar_of_hasFDerivAt (f := fun w => f w * h w) H).2]
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
    ContinuousLinearMap.coe_restrictScalars', ContinuousLinearMap.smulRight_apply,
    ContinuousLinearMap.one_apply, smul_eq_mul, one_mul, fderiv_eq_dz_add_dzbar f z, map_one,
    conj_I]
  ring_nf
  rw [I_sq]
  ring

/-- The real derivative of `z ↦ L_z(v)`, `L = fderiv f`, as the flip of the second derivative. -/
theorem hasFDerivAt_fderiv_apply {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {f : ℂ → F} {z : ℂ}
    (hf : DifferentiableAt ℝ (fderiv ℝ f) z) (v : ℂ) :
    HasFDerivAt (fun z => fderiv ℝ f z v) ((fderiv ℝ (fderiv ℝ f) z).flip v) z := by
  have := hf.hasFDerivAt.clm_apply (hasFDerivAt_const v z)
  simpa using this

/-- The second-derivative form of `∂̄∂f` and `∂∂̄f`. -/
theorem dzbar_dz_eq {f : ℂ → ℂ} {z : ℂ} (hf : DifferentiableAt ℝ (fderiv ℝ f) z) :
    dzbar (dz f) z = (fderiv ℝ (fderiv ℝ f) z 1 1 + I * fderiv ℝ (fderiv ℝ f) z I 1
      - I * fderiv ℝ (fderiv ℝ f) z 1 I + fderiv ℝ (fderiv ℝ f) z I I) / 4 := by
  have H : HasFDerivAt (dz f) ((1 / 2 : ℂ) • ((fderiv ℝ (fderiv ℝ f) z).flip 1
      - I • (fderiv ℝ (fderiv ℝ f) z).flip I)) z := by
    have := ((hasFDerivAt_fderiv_apply hf 1).sub
      ((hasFDerivAt_fderiv_apply hf I).const_mul I)).const_mul (1 / 2 : ℂ)
    convert this using 1
    funext w; simp only [dz, Pi.sub_apply]; ring
  rw [(dz_dzbar_of_hasFDerivAt H).2]
  simp only [ContinuousLinearMap.sub_apply,
    ContinuousLinearMap.smul_apply, ContinuousLinearMap.flip_apply, smul_eq_mul]
  ring_nf
  rw [I_sq]
  ring

theorem dz_dzbar_eq {f : ℂ → ℂ} {z : ℂ} (hf : DifferentiableAt ℝ (fderiv ℝ f) z) :
    dz (dzbar f) z = (fderiv ℝ (fderiv ℝ f) z 1 1 - I * fderiv ℝ (fderiv ℝ f) z I 1
      + I * fderiv ℝ (fderiv ℝ f) z 1 I + fderiv ℝ (fderiv ℝ f) z I I) / 4 := by
  have H : HasFDerivAt (dzbar f) ((1 / 2 : ℂ) • ((fderiv ℝ (fderiv ℝ f) z).flip 1
      + I • (fderiv ℝ (fderiv ℝ f) z).flip I)) z := by
    have := ((hasFDerivAt_fderiv_apply hf 1).add
      ((hasFDerivAt_fderiv_apply hf I).const_mul I)).const_mul (1 / 2 : ℂ)
    convert this using 1
    funext w; simp only [dzbar, Pi.add_apply]; ring
  rw [(dz_dzbar_of_hasFDerivAt H).1]
  simp only [ContinuousLinearMap.add_apply,
    ContinuousLinearMap.smul_apply, ContinuousLinearMap.flip_apply, smul_eq_mul]
  ring_nf
  rw [I_sq]
  ring

/-- **`∂̄∂ = ∂∂̄`** on functions that are `C²` near `z`. -/
theorem dzbar_dz_eq_dz_dzbar {f : ℂ → ℂ} {z : ℂ} (hf : ContDiffAt ℝ 2 f z) :
    dzbar (dz f) z = dz (dzbar f) z := by
  have hs : IsSymmSndFDerivAt ℝ f z := hf.isSymmSndFDerivAt (by simp)
  have hd : DifferentiableAt ℝ (fderiv ℝ f) z :=
    (hf.fderiv_right (m := 1) (by norm_num)).differentiableAt (by norm_num)
  rw [dzbar_dz_eq hd, dz_dzbar_eq hd, hs I 1]
  ring

/-- For real-valued `φ`, `∂̄φ = conj ∂φ`. -/
theorem dzbar_ofReal {φ : ℂ → ℝ} {z : ℂ} (hφ : DifferentiableAt ℝ φ z) :
    dzbar (fun w => (φ w : ℂ)) z = (starRingEnd ℂ) (dz (fun w => (φ w : ℂ)) z) := by
  have H := ofRealCLM.hasFDerivAt.comp z hφ.hasFDerivAt
  rw [(dz_dzbar_of_hasFDerivAt (f := fun w => (φ w : ℂ)) H).2,
    (dz_dzbar_of_hasFDerivAt (f := fun w => (φ w : ℂ)) H).1]
  simp only [ContinuousLinearMap.comp_apply, ofRealCLM_apply, map_div₀, map_sub, map_mul,
    conj_ofReal, conj_I, map_ofNat]
  ring

/-- The second derivative of a real-valued function, read in `ℂ`. -/
theorem fderiv_fderiv_ofReal {φ : ℂ → ℝ} {z : ℂ} (hφ : ContDiffAt ℝ 2 φ z) (u v : ℂ) :
    fderiv ℝ (fderiv ℝ (fun w => (φ w : ℂ))) z u v = (fderiv ℝ (fderiv ℝ φ) z u v : ℂ) := by
  have hdφ : ∀ᶠ w in nhds z, DifferentiableAt ℝ φ w :=
    (hφ.eventually (by simp)).mono fun w hw => hw.differentiableAt (by norm_num)
  have hev : (fun w => fderiv ℝ (fun w => (φ w : ℂ)) w v) =ᶠ[nhds z]
      fun w => ((fderiv ℝ φ w v : ℝ) : ℂ) := hdφ.mono fun w hw => by
    dsimp only
    rw [show (fun w => (φ w : ℂ)) = ofRealCLM ∘ φ from rfl,
      (ofRealCLM.hasFDerivAt.comp w hw.hasFDerivAt).fderiv]; rfl
  have hd2φ : DifferentiableAt ℝ (fderiv ℝ φ) z :=
    (hφ.fderiv_right (m := 1) (by norm_num)).differentiableAt (by norm_num)
  have hg : ContDiffAt ℝ 2 (fun w => (φ w : ℂ)) z := ofRealCLM.contDiff.contDiffAt.comp z hφ
  have hd2g : DifferentiableAt ℝ (fderiv ℝ (fun w => (φ w : ℂ))) z :=
    (hg.fderiv_right (m := 1) (by norm_num)).differentiableAt (by norm_num)
  have A := ofRealCLM.hasFDerivAt.comp z (hasFDerivAt_fderiv_apply hd2φ v)
  have B := hasFDerivAt_fderiv_apply hd2g v
  have h := B.unique (A.congr_of_eventuallyEq hev)
  have := congrArg (fun L => L u) h
  simpa using this

/-- **`∂̄∂φ` is real** for a real-valued `C²` function (it is `Δφ/4`). -/
theorem dzbar_dz_ofReal_im {φ : ℂ → ℝ} {z : ℂ} (hφ : ContDiffAt ℝ 2 φ z) :
    (dzbar (dz (fun w => (φ w : ℂ))) z).im = 0 := by
  have hg : ContDiffAt ℝ 2 (fun w => (φ w : ℂ)) z := ofRealCLM.contDiff.contDiffAt.comp z hφ
  have hd2g : DifferentiableAt ℝ (fderiv ℝ (fun w => (φ w : ℂ))) z :=
    (hg.fderiv_right (m := 1) (by norm_num)).differentiableAt (by norm_num)
  have hs : IsSymmSndFDerivAt ℝ φ z := hφ.isSymmSndFDerivAt (by simp)
  rw [dzbar_dz_eq hd2g, fderiv_fderiv_ofReal hφ, fderiv_fderiv_ofReal hφ,
    fderiv_fderiv_ofReal hφ, fderiv_fderiv_ofReal hφ, hs I 1]
  simp

end QOU.MathlibExt.Dolbeault
