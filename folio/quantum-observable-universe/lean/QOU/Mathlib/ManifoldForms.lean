import Mathlib.Analysis.Calculus.DifferentialForm.Basic
import Mathlib.Analysis.Calculus.FDeriv.Analytic
import Mathlib.Geometry.Manifold.MFDeriv.Atlas
import Mathlib.Geometry.Manifold.MFDeriv.FDeriv

/-!
# Differential forms on manifolds: pullback, naturality of `d`, chart compatibility

Mathlib (`Mathlib/Analysis/Calculus/DifferentialForm/Basic.lean`) defines differential forms
`E → E [⋀^Fin n]→L[𝕜] F` and the exterior derivative `extDeriv` only on a normed space; its
TODO lists forms on manifolds as "not defined yet". This file builds the first tranche.

## What is built (all sorry-free, axioms `propext, Classical.choice, Quot.sound`)

* `pullback φ ω`: pullback of a normed-space form along `φ : E → E'`,
  `(φ^* ω) x = (ω (φ x)).compContinuousLinearMap (fderiv 𝕜 φ x)`.
* `sum_symm_vanish`: the combinatorial identity that the second-derivative contribution to
  `d (φ^* ω)` vanishes after alternation when the second derivative is symmetric.
* `differentiableAt_of_hasFDerivAt_toContinuousMultilinearMap`: an alternating-map-valued
  function is differentiable once its image in continuous multilinear maps is (closed range).
* `differentiableAt_pullback`, `fderiv_pullback_apply_apply`: differentiability of `φ^* ω`
  and an explicit formula for its derivative.
* **`extDeriv_pullback`** (naturality of `d`): for `φ` `ContDiffAt 𝕜 r` with
  `minSmoothness 𝕜 2 ≤ r` and `ω` differentiable at `φ x`,
  `extDeriv (pullback φ ω) x = pullback φ (extDeriv ω) x`.
* `extDeriv_eq_pullback_of_eventuallyEq`: the local (germ) version of naturality.
* `ManifoldForm I M F k := ∀ x : M, TangentSpace I x [⋀^Fin k]→L[𝕜] F` (pointwise forms, no
  regularity) and `ManifoldForm.inChart ω x₀`, its representation in the extended chart at `x₀`.
* `ManifoldForm.inChart_eq_pullback` (boundaryless, `C¹`): on a chart overlap the two local
  representations are related by pullback along the coordinate change.
* `ManifoldForm.extDeriv_inChart_eq_pullback` (boundaryless, `C^r`, `minSmoothness 𝕜 2 ≤ r`):
  the chartwise exterior derivatives are related by the same coordinate-change pullback, i.e.
  `d` computed chart by chart is chart-independent.

## What is NOT built

* No vector bundle with fibre `TangentSpace I x [⋀^Fin k]→L[𝕜] F`, hence no notion of a
  smooth (`ContMDiff`) section and no bundled `C^r` forms on `M`.
* No exterior derivative as an operation `ManifoldForm I M F k → ManifoldForm I M F (k+1)`:
  the results above are the compatibility needed to define it chartwise, but the gluing
  (choosing `chartAt` and transporting `extDeriv (ω.inChart x)` back to `TangentSpace I x`)
  is not carried out, nor is `d ∘ d = 0` on `M`.
* Manifolds with boundary/corners are excluded (`I.Boundaryless`): `pullback` uses `fderiv`,
  not `fderivWithin` on `range I`.
* No wedge product, no integration, no Stokes.
-/

open Filter ContinuousAlternatingMap Set
open scoped Topology Manifold

namespace QOU.Mathlib.ManifoldForms

variable {𝕜 E E' F : Type*} [NontriviallyNormedField 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup E'] [NormedSpace 𝕜 E']
  [NormedAddCommGroup F] [NormedSpace 𝕜 F]

/-- If `B` is symmetric, then the alternated "second-derivative" term
`∑ᵢ (-1)ⁱ ∑ⱼ ω₀ (L v₀, …, B (vᵢ) (vⱼ), …)` (with `vᵢ` removed) vanishes. -/
theorem sum_symm_vanish {n : ℕ} (ω₀ : E' [⋀^Fin n]→L[𝕜] F) (L : E →L[𝕜] E')
    (B : E →L[𝕜] E →L[𝕜] E') (hB : ∀ a b, B a b = B b a) (v : Fin (n + 1) → E) :
    ∑ i : Fin (n + 1), (-1 : ℤ) ^ (i : ℕ) •
      ∑ j : Fin n, ω₀ (Function.update (fun k ↦ L (i.removeNth v k)) j
        (B (v i) (i.removeNth v j))) = 0 := by
  cases n with
  | zero => simp
  | succ m =>
    set f : E →L[𝕜] E →L[𝕜] E [⋀^Fin m]→L[𝕜] F :=
      ContinuousLinearMap.compL 𝕜 E E' (E [⋀^Fin m]→L[𝕜] F)
        ((compContinuousLinearMapCLM L) ∘L ω₀.curryLeft) ∘L B with hf
    have hfs : ∀ a b, f a b = f b a := by intro a b; simp [hf, hB a b]
    have h0 := alternatizeUncurryFin_alternatizeUncurryFinCLM_comp_of_symmetric hfs
    have h1 := congrArg (fun g ↦ g v) h0
    simp only [ContinuousAlternatingMap.coe_zero, Pi.zero_apply] at h1
    rw [← h1, alternatizeUncurryFin_apply]
    refine Finset.sum_congr rfl fun i _ ↦ ?_
    congr 1
    simp only [ContinuousLinearMap.comp_apply, alternatizeUncurryFinCLM_apply,
      alternatizeUncurryFin_apply]
    refine Finset.sum_congr rfl fun j _ ↦ ?_
    rw [← Fin.insertNth_removeNth, map_insertNth]
    simp [hf, Fin.removeNth]
    rfl

private theorem toCML_sub {ι : Type*} [Fintype ι] (f g : E [⋀^ι]→L[𝕜] F) :
    (f - g).toContinuousMultilinearMap = f.toContinuousMultilinearMap - g.toContinuousMultilinearMap :=
  rfl

/-- A function into continuous alternating maps is differentiable as soon as its composition
with the (isometric, closed-range) inclusion into continuous multilinear maps is. -/
theorem differentiableAt_of_hasFDerivAt_toContinuousMultilinearMap
    {X : Type*} [NormedAddCommGroup X] [NormedSpace 𝕜 X] {ι : Type*} [Fintype ι]
    {g : X → E [⋀^ι]→L[𝕜] F} {M : X →L[𝕜] ContinuousMultilinearMap 𝕜 (fun _ : ι ↦ E) F}
    {x : X} (h : HasFDerivAt (fun y ↦ (g y).toContinuousMultilinearMap) M x) :
    DifferentiableAt 𝕜 g x := by
  obtain ⟨c, hc⟩ := NormedField.exists_one_lt_norm 𝕜
  have hct : Tendsto (fun k : ℕ ↦ ‖c ^ k‖) atTop atTop := by
    simpa [norm_pow] using tendsto_pow_atTop_atTop_of_one_lt hc
  have hmem : ∀ u, M u ∈ Set.range (toContinuousMultilinearMap :
      (E [⋀^ι]→L[𝕜] F) → ContinuousMultilinearMap 𝕜 (fun _ : ι ↦ E) F) := by
    intro u
    refine isClosed_range_toContinuousMultilinearMap.mem_of_tendsto (h.lim u hct) ?_
    exact Eventually.of_forall fun k ↦
      ⟨c ^ k • (g (x + (c ^ k)⁻¹ • u) - g x), by simp [toCML_sub]⟩
  choose M'' hM'' using hmem
  have hadd : ∀ u v, M'' (u + v) = M'' u + M'' v := by
    intro u v; apply toContinuousMultilinearMap_injective; simp [hM'']
  have hsmul : ∀ (a : 𝕜) u, M'' (a • u) = a • M'' u := by
    intro a u; apply toContinuousMultilinearMap_injective; simp [hM'']
  let M' : X →L[𝕜] E [⋀^ι]→L[𝕜] F :=
    LinearMap.mkContinuous ⟨⟨M'', hadd⟩, hsmul⟩ ‖M‖ fun u ↦ by
      change ‖M'' u‖ ≤ ‖M‖ * ‖u‖
      rw [← norm_toContinuousMultilinearMap, hM'']
      exact M.le_opNorm u
  have hM' : ∀ u, (M' u).toContinuousMultilinearMap = M u := hM''
  refine ⟨M', ?_⟩
  rw [hasFDerivAt_iff_isLittleO_nhds_zero] at h ⊢
  refine (h.norm_left.congr_left fun k ↦ ?_).of_norm_left
  rw [← hM', ← norm_toContinuousMultilinearMap, toCML_sub, toCML_sub]

/-- Pullback of a differential form along a map of normed spaces. -/
noncomputable def pullback {n : ℕ} (φ : E → E') (ω : E' → E' [⋀^Fin n]→L[𝕜] F) (x : E) :
    E [⋀^Fin n]→L[𝕜] F :=
  (ω (φ x)).compContinuousLinearMap (fderiv 𝕜 φ x)

theorem pullback_apply {n : ℕ} (φ : E → E') (ω : E' → E' [⋀^Fin n]→L[𝕜] F) (x : E)
    (w : Fin n → E) : pullback φ ω x w = ω (φ x) (fun k ↦ fderiv 𝕜 φ x (w k)) := rfl

variable {n : ℕ} {φ : E → E'} {ω : E' → E' [⋀^Fin n]→L[𝕜] F} {x : E}

theorem hasFDerivAt_pullback_apply (hφ : DifferentiableAt 𝕜 φ x)
    (hφ' : DifferentiableAt 𝕜 (fderiv 𝕜 φ) x) (hω : DifferentiableAt 𝕜 ω (φ x))
    (w : Fin n → E) :
    HasFDerivAt (fun y ↦ pullback φ ω y w)
      (ContinuousMultilinearMap.apply 𝕜 (fun _ : Fin n ↦ E') F
          (fun k ↦ fderiv 𝕜 φ x (w k)) ∘L
        (toContinuousMultilinearMapLI.toContinuousLinearMap ∘L
          (fderiv 𝕜 ω (φ x) ∘L fderiv 𝕜 φ x)) +
       ∑ j, (ω (φ x)).toContinuousMultilinearMap.toContinuousLinearMap
          (fun k ↦ fderiv 𝕜 φ x (w k)) j ∘L
          ((fderiv 𝕜 φ x).comp (0 : E →L[𝕜] E) + (fderiv 𝕜 (fderiv 𝕜 φ) x).flip (w j))) x := by
  have hf : HasFDerivAt (fun y ↦ (ω (φ y)).toContinuousMultilinearMap)
      (toContinuousMultilinearMapLI.toContinuousLinearMap ∘L
          (fderiv 𝕜 ω (φ x) ∘L fderiv 𝕜 φ x)) x :=
    (toContinuousMultilinearMapLI (𝕜 := 𝕜) (E := E') (F := F)
      (ι := Fin n)).toContinuousLinearMap.hasFDerivAt.comp x
      (hω.hasFDerivAt.comp x hφ.hasFDerivAt)
  have hg : ∀ j, HasFDerivAt (fun y ↦ fderiv 𝕜 φ y (w j))
      ((fderiv 𝕜 φ x).comp (0 : E →L[𝕜] E) + (fderiv 𝕜 (fderiv 𝕜 φ) x).flip (w j)) x :=
    fun j ↦ hφ'.hasFDerivAt.clm_apply (hasFDerivAt_const (w j) x)
  exact hf.continuousMultilinearMap_apply hg

theorem fderiv_pullback_apply_apply (hφ : DifferentiableAt 𝕜 φ x)
    (hφ' : DifferentiableAt 𝕜 (fderiv 𝕜 φ) x) (hω : DifferentiableAt 𝕜 ω (φ x))
    (w : Fin n → E) (u : E) :
    fderiv 𝕜 (fun y ↦ pullback φ ω y w) x u =
      fderiv 𝕜 ω (φ x) (fderiv 𝕜 φ x u) (fun k ↦ fderiv 𝕜 φ x (w k)) +
      ∑ j, ω (φ x) (Function.update (fun k ↦ fderiv 𝕜 φ x (w k)) j
        (fderiv 𝕜 (fderiv 𝕜 φ) x u (w j))) := by
  rw [(hasFDerivAt_pullback_apply hφ hφ' hω w).fderiv]
  simp

set_option maxSynthPendingDepth 3 in
theorem differentiableAt_pullback (hφ : DifferentiableAt 𝕜 φ x)
    (hφ' : DifferentiableAt 𝕜 (fderiv 𝕜 φ) x) (hω : DifferentiableAt 𝕜 ω (φ x)) :
    DifferentiableAt 𝕜 (pullback φ ω) x := by
  have hf : HasFDerivAt (fun y ↦ (ω (φ y)).toContinuousMultilinearMap)
      (toContinuousMultilinearMapLI.toContinuousLinearMap ∘L
          (fderiv 𝕜 ω (φ x) ∘L fderiv 𝕜 φ x)) x :=
    (toContinuousMultilinearMapLI (𝕜 := 𝕜) (E := E') (F := F)
      (ι := Fin n)).toContinuousLinearMap.hasFDerivAt.comp x
      (hω.hasFDerivAt.comp x hφ.hasFDerivAt)
  have hΨ := (hasFDerivAt_const
    (ContinuousMultilinearMap.compContinuousLinearMapContinuousMultilinear 𝕜
      (fun _ : Fin n ↦ E) (fun _ : Fin n ↦ E') F) x).continuousMultilinearMap_apply
    (g := fun (_ : Fin n) (y : E) ↦ fderiv 𝕜 φ y) (fun _ ↦ hφ'.hasFDerivAt)
  refine differentiableAt_of_hasFDerivAt_toContinuousMultilinearMap
    ((hΨ.clm_apply hf).congr_of_eventuallyEq (Eventually.of_forall fun y ↦ ?_))
  ext w
  rfl

/-- **Naturality of the exterior derivative** (normed-space version): for `φ` of class `C²`
at `x` (in the sense of `minSmoothness 𝕜 2`) and `ω` differentiable at `φ x`,
`d (φ^* ω) = φ^* (d ω)` at `x`. -/
theorem extDeriv_pullback {r : WithTop ℕ∞} (hφ : ContDiffAt 𝕜 r φ x)
    (hr : minSmoothness 𝕜 2 ≤ r) (hω : DifferentiableAt 𝕜 ω (φ x)) :
    extDeriv (pullback φ ω) x = pullback φ (extDeriv ω) x := by
  have h2r : (2 : WithTop ℕ∞) ≤ r := le_minSmoothness.trans hr
  have h1 : DifferentiableAt 𝕜 φ x :=
    hφ.differentiableAt ((by norm_num : (1 : WithTop ℕ∞) ≤ 2).trans h2r)
  have h2 : DifferentiableAt 𝕜 (fderiv 𝕜 φ) x :=
    (hφ.fderiv_right (m := 1) (by simpa using h2r)).differentiableAt le_rfl
  have hsym := hφ.isSymmSndFDerivAt hr
  ext v
  rw [extDeriv_apply (differentiableAt_pullback h1 h2 hω), pullback_apply,
    extDeriv_apply hω]
  simp only [fderiv_pullback_apply_apply h1 h2 hω,
    fderiv_continuousAlternatingMap_apply_const_apply hω, smul_add, Finset.sum_add_distrib]
  rw [sum_symm_vanish (ω (φ x)) (fderiv 𝕜 φ x) (fderiv 𝕜 (fderiv 𝕜 φ) x) hsym v, add_zero]
  rfl

/-- Local transport of the exterior derivative: if `ω₁` agrees near `y` with the pullback of
`ω₀` along a `C²` map `φ`, then `d ω₁ (y) = (φ^* d ω₀)(y)`. -/
theorem extDeriv_eq_pullback_of_eventuallyEq {r : WithTop ℕ∞} {ω₁ : E → E [⋀^Fin n]→L[𝕜] F}
    {y : E} (h : ω₁ =ᶠ[𝓝 y] pullback φ ω) (hφ : ContDiffAt 𝕜 r φ y)
    (hr : minSmoothness 𝕜 2 ≤ r) (hω : DifferentiableAt 𝕜 ω (φ y)) :
    extDeriv ω₁ y = pullback φ (extDeriv ω) y := by
  rw [h.extDeriv_eq, extDeriv_pullback hφ hr hω]

/-! ### Pointwise differential forms on a manifold and their chart representations -/

section Manifold

variable {H : Type*} [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M]

/-- A (pointwise, not necessarily continuous or smooth) differential `k`-form on the manifold
`M` with values in `F`: a continuous alternating `k`-linear map on each tangent space. -/
def ManifoldForm (I : ModelWithCorners 𝕜 E H) (M : Type*) [TopologicalSpace M]
    [ChartedSpace H M] (V : Type*) [NormedAddCommGroup V] [NormedSpace 𝕜 V] (k : ℕ) : Type _ :=
  ∀ x : M, TangentSpace I x [⋀^Fin k]→L[𝕜] V

namespace ManifoldForm

variable {k : ℕ}

/-- The local representation of a manifold form in the extended chart at `x₀`:
`(ω.inChart x₀) y = ω ((extChartAt I x₀).symm y) ∘ (D (extChartAt I x₀).symm y)`. -/
noncomputable def inChart (ω : ManifoldForm I M F k) (x₀ : M) : E → E [⋀^Fin k]→L[𝕜] F :=
  fun y ↦ (ω ((extChartAt I x₀).symm y)).compContinuousLinearMap
    (mfderiv 𝓘(𝕜, E) I (extChartAt I x₀).symm y)

variable [I.Boundaryless]

/-- **Chart compatibility.** On the overlap of two extended charts, the local representations of
a manifold form are related by pullback along the coordinate change. -/
theorem inChart_eq_pullback [IsManifold I 1 M] (ω : ManifoldForm I M F k) (x₀ x₁ : M) {y : E}
    (hy : y ∈ ((extChartAt I x₁).symm ≫ extChartAt I x₀).source) :
    ω.inChart x₁ y = pullback (extChartAt I x₀ ∘ (extChartAt I x₁).symm) (ω.inChart x₀) y := by
  simp only [PartialEquiv.trans_source, PartialEquiv.symm_source, mem_inter_iff,
    mem_preimage] at hy
  obtain ⟨hy₁, hy₀⟩ := hy
  set τ := extChartAt I x₀ ∘ (extChartAt I x₁).symm with hτ
  have hτy : τ y ∈ (extChartAt I x₀).target := (extChartAt I x₀).map_source hy₀
  -- the two inverse charts agree after the coordinate change, near `y`
  have hev : (extChartAt I x₁).symm =ᶠ[𝓝 y] (extChartAt I x₀).symm ∘ τ := by
    have : ∀ᶠ y' in 𝓝 y, (extChartAt I x₁).symm y' ∈ (extChartAt I x₀).source :=
      (continuousAt_extChartAt_symm'' hy₁).preimage_mem_nhds
        ((isOpen_extChartAt_source x₀).mem_nhds hy₀)
    filter_upwards [this] with y' hy'
    change _ = (extChartAt I x₀).symm ((extChartAt I x₀) ((extChartAt I x₁).symm y'))
    rw [(extChartAt I x₀).left_inv hy']
  have hτd : DifferentiableAt 𝕜 τ y := by
    have h := contDiffWithinAt_ext_coord_change (I := I) (n := 1) x₀ x₁
      (by simp only [PartialEquiv.trans_source, PartialEquiv.symm_source, mem_inter_iff,
        mem_preimage]; exact ⟨hy₁, hy₀⟩)
    rw [ModelWithCorners.Boundaryless.range_eq_univ, contDiffWithinAt_univ] at h
    exact h.differentiableAt le_rfl
  have hsymm : MDifferentiableAt 𝓘(𝕜, E) I (extChartAt I x₀).symm (τ y) := by
    have h := mdifferentiableWithinAt_extChartAt_symm hτy
    rwa [ModelWithCorners.Boundaryless.range_eq_univ, mdifferentiableWithinAt_univ] at h
  have hmf : mfderiv 𝓘(𝕜, E) I (extChartAt I x₁).symm y =
      (mfderiv 𝓘(𝕜, E) I (extChartAt I x₀).symm (τ y)).comp (fderiv 𝕜 τ y) := by
    rw [hev.mfderiv_eq, mfderiv_comp y hsymm
      (mdifferentiableAt_iff_differentiableAt.2 hτd), mfderiv_eq_fderiv]
  have hpt : (extChartAt I x₁).symm y = (extChartAt I x₀).symm (τ y) := hev.self_of_nhds
  have hω : (ω ((extChartAt I x₁).symm y) : E [⋀^Fin k]→L[𝕜] F) =
      ω ((extChartAt I x₀).symm (τ y)) := by rw [hpt]
  ext w
  simp only [inChart, pullback_apply, compContinuousLinearMap_apply, hmf]
  rw [hω]
  rfl

/-- **Chartwise transport of the exterior derivative.** On a `C^r` boundaryless manifold with
`minSmoothness 𝕜 2 ≤ r`, the exterior derivative of the chart-`x₁` representation of a manifold
form is the coordinate-change pullback of the exterior derivative of its chart-`x₀`
representation, wherever the latter is differentiable. This is the compatibility that makes a
chart-by-chart definition of `d` on `M` independent of the chart. -/
theorem extDeriv_inChart_eq_pullback {r : WithTop ℕ∞} [IsManifold I r M]
    (hr : minSmoothness 𝕜 2 ≤ r) (ω : ManifoldForm I M F k) (x₀ x₁ : M) {y : E}
    (hy : y ∈ ((extChartAt I x₁).symm ≫ extChartAt I x₀).source)
    (hω : DifferentiableAt 𝕜 (ω.inChart x₀) ((extChartAt I x₀ ∘ (extChartAt I x₁).symm) y)) :
    extDeriv (ω.inChart x₁) y =
      pullback (extChartAt I x₀ ∘ (extChartAt I x₁).symm) (extDeriv (ω.inChart x₀)) y := by
  have hsrc : IsOpen ((extChartAt I x₁).symm ≫ extChartAt I x₀).source := by
    simp only [PartialEquiv.trans_source, PartialEquiv.symm_source]
    exact (continuousOn_extChartAt_symm x₁).isOpen_inter_preimage
      (isOpen_extChartAt_target x₁) (isOpen_extChartAt_source x₀)
  have hτ : ContDiffAt 𝕜 r (extChartAt I x₀ ∘ (extChartAt I x₁).symm) y := by
    have h := contDiffWithinAt_ext_coord_change (I := I) (n := r) x₀ x₁ hy
    rwa [ModelWithCorners.Boundaryless.range_eq_univ, contDiffWithinAt_univ] at h
  have : IsManifold I 1 M := IsManifold.of_le (n := r)
    (((by norm_num : (1 : WithTop ℕ∞) ≤ 2)).trans (le_minSmoothness.trans hr))
  refine extDeriv_eq_pullback_of_eventuallyEq ?_ hτ hr hω
  filter_upwards [hsrc.mem_nhds hy] with y' hy'
  exact inChart_eq_pullback ω x₀ x₁ hy'

end ManifoldForm

end Manifold

end QOU.Mathlib.ManifoldForms

-- Ref: [leitner2026] standard: Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 14 (differential forms, exterior derivative, naturality of d)
