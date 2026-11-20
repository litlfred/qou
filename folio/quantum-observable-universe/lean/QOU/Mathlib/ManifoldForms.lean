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

* `ManifoldForm.extDeriv ω` (`ManifoldForm I M F k → ManifoldForm I M F (k+1)`): at `x`, `d` of
  the chart-`x` representation at `extChartAt I x x`, transported to `TangentSpace I x` by the
  chart derivative.
* `ManifoldForm.IsSmoothForm ω s`: every chart representation is `C^s` on its chart target.
* **`ManifoldForm.inChart_extDeriv`** (boundaryless, `C^r`, `minSmoothness 𝕜 2 ≤ r`): at any point
  of any chart target where `ω.inChart x₀` is differentiable,
  `(ω.extDeriv).inChart x₀ y = extDeriv (ω.inChart x₀) y`; `inChart_extDeriv_eqOn` is the
  on-the-whole-target version for `C^s` forms, `1 ≤ s`.
* **`ManifoldForm.extDeriv_extDeriv`** (`d ∘ d = 0` on `M`): for a `C^s` form with
  `minSmoothness 𝕜 2 ≤ s` on a boundaryless `C^r` manifold with `minSmoothness 𝕜 2 ≤ r`.
* `IsSmoothForm.extDeriv`: `d` maps `C^s` forms to `C^m` forms when `m + 1 ≤ s`, `1 ≤ s`.
* `AddCommGroup` / `Module 𝕜` on `ManifoldForm`; `extDeriv_smul` (unconditional),
  `extDeriv_add_apply` (pointwise, differentiable charts), `extDeriv_add` (`C^s`, `1 ≤ s`).
* `ManifoldForm.extDeriv_modelSpace`: on `M = E` with model `𝓘(𝕜, E)`, `ManifoldForm.extDeriv`
  is Mathlib's `extDeriv`.

## What is NOT built

* No vector bundle with fibre `TangentSpace I x [⋀^Fin k]→L[𝕜] F`, hence no notion of a
  smooth (`ContMDiff`) section and no bundled `C^r` forms on `M`; smoothness is the chartwise
  predicate `IsSmoothForm` instead.
* `extDeriv_add` needs differentiability of both chart representations; there is no general
  additivity for arbitrary (non-differentiable) pointwise forms, as for Mathlib's `extDeriv`.
* Manifolds with boundary/corners are excluded (`I.Boundaryless`): `pullback` uses `fderiv`,
  not `fderivWithin` on `range I`.
* No pullback of manifold forms along smooth maps `M → N`, no wedge product, no integration,
  no Stokes.
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


/-! ### The exterior derivative on `M` -/

/-- The exterior derivative of a manifold form, defined at `x` by computing `d` of the local
representation in the extended chart at `x` itself, at the point `extChartAt I x x`, and
transporting the result back to `TangentSpace I x` along the chart derivative. By
`extDeriv_inChart_eq_pullback` this does not depend on the chart used (see `inChart_extDeriv`). -/
noncomputable def extDeriv (ω : ManifoldForm I M F k) : ManifoldForm I M F (k + 1) :=
  fun x ↦ (_root_.extDeriv (ω.inChart x) (extChartAt I x x)).compContinuousLinearMap
    (mfderiv I 𝓘(𝕜, E) (extChartAt I x) x)

omit [I.Boundaryless] in
theorem extDeriv_apply (ω : ManifoldForm I M F k) (x : M) (v : Fin (k + 1) → TangentSpace I x) :
    ω.extDeriv x v = _root_.extDeriv (ω.inChart x) (extChartAt I x x)
      (fun i ↦ mfderiv I 𝓘(𝕜, E) (extChartAt I x) x (v i)) := rfl

/-- A manifold form is of class `C^s` if each of its chart representations is `C^s` on the
target of the chart. -/
def IsSmoothForm (ω : ManifoldForm I M F k) (s : WithTop ℕ∞) : Prop :=
  ∀ x₀ : M, ContDiffOn 𝕜 s (ω.inChart x₀) (extChartAt I x₀).target

omit [I.Boundaryless] in
theorem mfderivWithin_range_eq [I.Boundaryless] {N : Type*} [TopologicalSpace N]
    [ChartedSpace H N] (g : E → N) (y : E) :
    mfderivWithin 𝓘(𝕜, E) I g (range I) y = mfderiv 𝓘(𝕜, E) I g y := by
  rw [ModelWithCorners.Boundaryless.range_eq_univ, mfderivWithin_univ]

/-- The chart derivatives compose to the identity: with `p = (extChartAt I x₀).symm y` and
`τ = extChartAt I x₀ ∘ (extChartAt I p).symm` the coordinate change,
`Dτ (φ_p p) ∘ Dφ_p (p) ∘ D(φ_{x₀}⁻¹)(y) = id`. -/
theorem fderiv_coordChange_comp_eq_id [IsManifold I 1 M] (x₀ : M) {y : E}
    (hy : y ∈ (extChartAt I x₀).target) :
    (fderiv 𝕜 (extChartAt I x₀ ∘ (extChartAt I ((extChartAt I x₀).symm y)).symm)
        (extChartAt I ((extChartAt I x₀).symm y) ((extChartAt I x₀).symm y))).comp
      ((mfderiv I 𝓘(𝕜, E) (extChartAt I ((extChartAt I x₀).symm y))
          ((extChartAt I x₀).symm y)).comp
        (mfderiv 𝓘(𝕜, E) I (extChartAt I x₀).symm y)) = ContinuousLinearMap.id 𝕜 E := by
  set p := (extChartAt I x₀).symm y with hp
  have hpsrc : p ∈ (extChartAt I x₀).source := (extChartAt I x₀).map_target hy
  have hp' : (extChartAt I p).symm (extChartAt I p p) = p := extChartAt_to_inv p
  have hg : MDifferentiableAt I 𝓘(𝕜, E) (extChartAt I x₀)
      ((extChartAt I p).symm (extChartAt I p p)) := by
    rw [hp']
    exact mdifferentiableAt_extChartAt (by rwa [← extChartAt_source (I := I)])
  have hf : MDifferentiableAt 𝓘(𝕜, E) I (extChartAt I p).symm (extChartAt I p p) := by
    have h := mdifferentiableWithinAt_extChartAt_symm (mem_extChartAt_target (I := I) p)
    rwa [ModelWithCorners.Boundaryless.range_eq_univ, mdifferentiableWithinAt_univ] at h
  have hτ : fderiv 𝕜 (extChartAt I x₀ ∘ (extChartAt I p).symm) (extChartAt I p p) =
      (mfderiv I 𝓘(𝕜, E) (extChartAt I x₀) p).comp
        (mfderiv 𝓘(𝕜, E) I (extChartAt I p).symm (extChartAt I p p)) := by
    rw [← mfderiv_eq_fderiv, mfderiv_comp _ hg hf, hp']
  have hBC := mfderivWithin_extChartAt_symm_comp_mfderiv_extChartAt' (I := I) (x := p)
    (mem_extChartAt_source (I := I) p)
  have hAD := mfderiv_extChartAt_comp_mfderivWithin_extChartAt_symm (I := I) hy
  rw [mfderivWithin_range_eq] at hBC hAD
  rw [hτ]
  ext v
  have h1 : mfderiv 𝓘(𝕜, E) I (extChartAt I p).symm (extChartAt I p p)
      (mfderiv I 𝓘(𝕜, E) (extChartAt I p) p (mfderiv 𝓘(𝕜, E) I (extChartAt I x₀).symm y v)) =
      mfderiv 𝓘(𝕜, E) I (extChartAt I x₀).symm y v :=
    DFunLike.congr_fun hBC (mfderiv 𝓘(𝕜, E) I (extChartAt I x₀).symm y v)
  have h2 : mfderiv I 𝓘(𝕜, E) (extChartAt I x₀) p
      (mfderiv 𝓘(𝕜, E) I (extChartAt I x₀).symm y v) = v :=
    DFunLike.congr_fun hAD v
  change mfderiv I 𝓘(𝕜, E) (extChartAt I x₀) p (mfderiv 𝓘(𝕜, E) I (extChartAt I p).symm
    (extChartAt I p p) (mfderiv I 𝓘(𝕜, E) (extChartAt I p) p
      (mfderiv 𝓘(𝕜, E) I (extChartAt I x₀).symm y v))) = v
  rw [h1, h2]

/-- **The exterior derivative in a chart.** At every point `y` of the target of the chart at
`x₀` where the chart representation of `ω` is differentiable, the chart representation of
`ω.extDeriv` is the normed-space exterior derivative of the chart representation of `ω`. -/
theorem inChart_extDeriv {r : WithTop ℕ∞} [IsManifold I r M] (hr : minSmoothness 𝕜 2 ≤ r)
    (ω : ManifoldForm I M F k) (x₀ : M) {y : E} (hy : y ∈ (extChartAt I x₀).target)
    (hω : DifferentiableAt 𝕜 (ω.inChart x₀) y) :
    ω.extDeriv.inChart x₀ y = _root_.extDeriv (ω.inChart x₀) y := by
  have : IsManifold I 1 M := IsManifold.of_le (n := r)
    (((by norm_num : (1 : WithTop ℕ∞) ≤ 2)).trans (le_minSmoothness.trans hr))
  have hD := fderiv_coordChange_comp_eq_id (I := I) x₀ hy
  set p := (extChartAt I x₀).symm y with hp
  have hpsrc : p ∈ (extChartAt I x₀).source := (extChartAt I x₀).map_target hy
  have hyp : extChartAt I x₀ p = y := (extChartAt I x₀).right_inv hy
  have hp' : (extChartAt I p).symm (extChartAt I p p) = p := extChartAt_to_inv p
  have hy' : extChartAt I p p ∈ ((extChartAt I p).symm ≫ extChartAt I x₀).source := by
    simp only [PartialEquiv.trans_source, PartialEquiv.symm_source, mem_inter_iff, mem_preimage]
    exact ⟨mem_extChartAt_target p, by rw [hp']; exact hpsrc⟩
  have hτ : (extChartAt I x₀ ∘ (extChartAt I p).symm) (extChartAt I p p) = y := by
    simp only [Function.comp_apply, hp', hyp]
  have key := extDeriv_inChart_eq_pullback hr ω x₀ p hy' (by rw [hτ]; exact hω)
  ext w
  change _root_.extDeriv (ω.inChart p) (extChartAt I p p)
    (fun i ↦ mfderiv I 𝓘(𝕜, E) (extChartAt I p) p
      (mfderiv 𝓘(𝕜, E) I (extChartAt I x₀).symm y (w i))) = _
  rw [key, pullback_apply, hτ]
  congr 1
  funext i
  exact DFunLike.congr_fun hD (w i)

/-- For a `C^s` form (`1 ≤ s`), the chart representation of `ω.extDeriv` agrees with the
normed-space exterior derivative of the chart representation on the whole chart target. -/
theorem inChart_extDeriv_eqOn {r s : WithTop ℕ∞} [IsManifold I r M]
    (hr : minSmoothness 𝕜 2 ≤ r) {ω : ManifoldForm I M F k} (hω : ω.IsSmoothForm s)
    (hs : 1 ≤ s) (x₀ : M) :
    EqOn (ω.extDeriv.inChart x₀) (_root_.extDeriv (ω.inChart x₀)) (extChartAt I x₀).target :=
  fun _ hy ↦ inChart_extDeriv hr ω x₀ hy
    (((hω x₀).differentiableOn hs).differentiableAt
      ((isOpen_extChartAt_target x₀).mem_nhds hy))

/-- **`d ∘ d = 0` on a manifold.** On a boundaryless `C^r` manifold (`minSmoothness 𝕜 2 ≤ r`),
for every form of class `C^s` with `minSmoothness 𝕜 2 ≤ s`, `d (d ω) = 0` at every point. -/
theorem extDeriv_extDeriv_apply {r s : WithTop ℕ∞} [IsManifold I r M]
    (hr : minSmoothness 𝕜 2 ≤ r) {ω : ManifoldForm I M F k} (hω : ω.IsSmoothForm s)
    (hs : minSmoothness 𝕜 2 ≤ s) (x : M) : ω.extDeriv.extDeriv x = 0 := by
  have hs1 : (1 : WithTop ℕ∞) ≤ s :=
    ((by norm_num : (1 : WithTop ℕ∞) ≤ 2)).trans (le_minSmoothness.trans hs)
  have hmem : extChartAt I x x ∈ (extChartAt I x).target := mem_extChartAt_target x
  have hev : ω.extDeriv.inChart x =ᶠ[𝓝 (extChartAt I x x)] _root_.extDeriv (ω.inChart x) :=
    Filter.eventuallyEq_of_mem ((isOpen_extChartAt_target x).mem_nhds hmem)
      (inChart_extDeriv_eqOn hr hω hs1 x)
  have hcd : ContDiffAt 𝕜 s (ω.inChart x) (extChartAt I x x) :=
    (hω x).contDiffAt ((isOpen_extChartAt_target x).mem_nhds hmem)
  ext v
  rw [extDeriv_apply, hev.extDeriv_eq, _root_.extDeriv_extDeriv_apply hcd hs]
  rfl


/-- The exterior derivative of a `C^s` form is a `C^m` form whenever `m + 1 ≤ s` (and `1 ≤ s`,
needed to identify `d` with its chart representation). -/
theorem IsSmoothForm.extDeriv {r s m : WithTop ℕ∞} [IsManifold I r M]
    (hr : minSmoothness 𝕜 2 ≤ r) {ω : ManifoldForm I M F k} (hω : ω.IsSmoothForm s)
    (hs : 1 ≤ s) (hm : m + 1 ≤ s) : ω.extDeriv.IsSmoothForm m := by
  intro x₀
  have h : ContDiffOn 𝕜 m (_root_.extDeriv (ω.inChart x₀)) (extChartAt I x₀).target := by
    have hf := (hω x₀).fderiv_of_isOpen (isOpen_extChartAt_target x₀) hm
    exact ((alternatizeUncurryFinCLM 𝕜 E F (n := k)).contDiff.comp_contDiffOn hf).congr
      fun y _ ↦ by simp [_root_.extDeriv, alternatizeUncurryFinCLM_apply]
  exact h.congr (inChart_extDeriv_eqOn hr hω hs x₀)

/-! ### Linearity -/

omit [I.Boundaryless] in
noncomputable instance : AddCommGroup (ManifoldForm I M F k) :=
  inferInstanceAs (AddCommGroup (∀ x : M, TangentSpace I x [⋀^Fin k]→L[𝕜] F))

omit [I.Boundaryless] in
noncomputable instance : Module 𝕜 (ManifoldForm I M F k) :=
  inferInstanceAs (Module 𝕜 (∀ x : M, TangentSpace I x [⋀^Fin k]→L[𝕜] F))

omit [I.Boundaryless] in
theorem inChart_add (ω₁ ω₂ : ManifoldForm I M F k) (x₀ : M) :
    (ω₁ + ω₂).inChart x₀ = ω₁.inChart x₀ + ω₂.inChart x₀ := by
  funext y; ext w; rfl

omit [I.Boundaryless] in
theorem inChart_smul (c : 𝕜) (ω : ManifoldForm I M F k) (x₀ : M) :
    (c • ω).inChart x₀ = c • ω.inChart x₀ := by
  funext y; ext w; rfl

omit [I.Boundaryless] in
/-- `ManifoldForm.extDeriv` is additive at `x` whenever both chart representations at `x` are
differentiable at `extChartAt I x x`. -/
theorem extDeriv_add_apply {ω₁ ω₂ : ManifoldForm I M F k} {x : M}
    (h₁ : DifferentiableAt 𝕜 (ω₁.inChart x) (extChartAt I x x))
    (h₂ : DifferentiableAt 𝕜 (ω₂.inChart x) (extChartAt I x x)) :
    (ω₁ + ω₂).extDeriv x = ω₁.extDeriv x + ω₂.extDeriv x := by
  ext v
  rw [extDeriv_apply, inChart_add, _root_.extDeriv_add h₁ h₂]
  rfl

omit [I.Boundaryless] in
theorem extDeriv_smul (c : 𝕜) (ω : ManifoldForm I M F k) :
    (c • ω).extDeriv = c • ω.extDeriv := by
  funext x
  ext v
  rw [extDeriv_apply, inChart_smul, _root_.extDeriv_smul]
  rfl

/-- Additivity of `d` on `C^s` forms, `1 ≤ s`. -/
theorem extDeriv_add {s : WithTop ℕ∞} {ω₁ ω₂ : ManifoldForm I M F k}
    (h₁ : ω₁.IsSmoothForm s) (h₂ : ω₂.IsSmoothForm s) (hs : 1 ≤ s) :
    (ω₁ + ω₂).extDeriv = ω₁.extDeriv + ω₂.extDeriv := by
  funext x
  have hmem := (isOpen_extChartAt_target (I := I) x).mem_nhds (mem_extChartAt_target x)
  exact extDeriv_add_apply (((h₁ x).differentiableOn hs).differentiableAt hmem)
    (((h₂ x).differentiableOn hs).differentiableAt hmem)


/-- **`d ∘ d = 0` on a manifold**, as an equality of manifold forms. -/
theorem extDeriv_extDeriv {r s : WithTop ℕ∞} [IsManifold I r M]
    (hr : minSmoothness 𝕜 2 ≤ r) {ω : ManifoldForm I M F k} (hω : ω.IsSmoothForm s)
    (hs : minSmoothness 𝕜 2 ≤ s) : ω.extDeriv.extDeriv = 0 :=
  funext (extDeriv_extDeriv_apply hr hω hs)

end ManifoldForm

/-- On the model space `E` itself (with the trivial model `𝓘(𝕜, E)`), the exterior derivative of
manifold forms is Mathlib's normed-space exterior derivative. -/
theorem ManifoldForm.extDeriv_modelSpace {k : ℕ} (ω : ManifoldForm 𝓘(𝕜, E) E F k) (x : E) :
    ω.extDeriv x = _root_.extDeriv (ω : E → E [⋀^Fin k]→L[𝕜] F) x := by
  have hc : ∀ y : E, ω.inChart y = (ω : E → E [⋀^Fin k]→L[𝕜] F) := by
    intro y
    funext z
    ext w
    simp [ManifoldForm.inChart, mfderiv_id]
    rfl
  ext v
  rw [ManifoldForm.extDeriv_apply, hc]
  simp [mfderiv_id]
  rfl


end Manifold

end QOU.Mathlib.ManifoldForms

-- Ref: [leitner2026] standard: Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 14 (differential forms, exterior derivative, naturality of d)
