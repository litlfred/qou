import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Analytic.Uniqueness
import Mathlib.Geometry.Manifold.MFDeriv.SpecificFunctions
import Mathlib.Geometry.Manifold.MFDeriv.FDeriv
import Mathlib.Topology.Algebra.ConstMulAction
import QOU.RiemannSurface.ChartStep

/-!
# `QOU.RiemannSurface.IdentityTheorem` — the identity theorem on a connected Riemann surface

Bean `qou-4xht` (GAP for the chart step `qou-mq3p`, parent `qou-qhcr`).

Let `M` be a connected Hausdorff complex 1-manifold (`ChartedSpace ℂ M` with a holomorphic
atlas, `IsManifold 𝓘(ℂ) 1 M`). Then:

* **`eq_id_of_eventuallyEq_id`**: a holomorphic `f : M → M` that is the identity on a
  neighbourhood of one point is the identity everywhere.
* **`local_effective_of_faithful`**: for a faithful action of a group by holomorphic maps, no
  `g ≠ 1` fixes a neighbourhood of a point pointwise. This is the hypothesis `hloc` of
  `ChartStep.isCyclic_stabilizer_of_chart`, which is therefore discharged:
  **`isCyclic_stabilizer_of_faithful`**.

## Proof

Let `U` be the set of points near which `f = id`. It is open and nonempty. It is closed: for `q`
in its closure, `f q = q` by continuity; in the chart `φ = chartAt ℂ q` the coordinate
expression `F = φ ∘ f ∘ φ⁻¹` is holomorphic on a small ball `B` around `φ q`, hence analytic,
and `F = id` near the image of some point of `U ∩ φ⁻¹ B`. The one-variable identity theorem
(`AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq`) gives `F = id` on `B`, so `f = id` near
`q`. Connectedness gives `U = M`.

No axiom, no `sorry`, no class standing in for the theorem.
-/

namespace QOU.RiemannSurface.IdentityTheorem

open Filter Topology Set Manifold

variable {M : Type*} [TopologicalSpace M] [ChartedSpace ℂ M] [IsManifold 𝓘(ℂ) 1 M]

/-- In the chart at `q`, the coordinate expression of a holomorphic `f` with `f q = q` is
complex-differentiable at every chart point whose preimage and image stay in the chart. -/
theorem differentiableAt_coord {f : M → M} (hf : MDifferentiable 𝓘(ℂ) 𝓘(ℂ) f) (q : M)
    {z : ℂ} (hz : z ∈ (chartAt ℂ q).target)
    (hfz : f ((chartAt ℂ q).symm z) ∈ (chartAt ℂ q).source) :
    DifferentiableAt ℂ (fun w => chartAt ℂ q (f ((chartAt ℂ q).symm w))) z := by
  set φ := chartAt ℂ q
  have hx : φ.symm z ∈ φ.source := φ.map_target hz
  have h := (hf (φ.symm z))
  rw [← mdifferentiableWithinAt_univ,
    mdifferentiableWithinAt_iff_of_mem_source (x := q) (y := q) hx hfz] at h
  have hd := h.2
  simp only [mfld_simps] at hd
  rw [φ.right_inv hz] at hd
  exact hd.differentiableAt (by simp)

/-- **The identity theorem on a connected Riemann surface.** A holomorphic self-map equal to
the identity near one point is the identity. -/
theorem eq_id_of_eventuallyEq_id [T2Space M] [ConnectedSpace M] {f : M → M}
    (hf : MDifferentiable 𝓘(ℂ) 𝓘(ℂ) f) {x₀ : M} (h₀ : f =ᶠ[𝓝 x₀] id) : f = id := by
  have hfc : Continuous f := hf.continuous
  set U : Set M := {x | f =ᶠ[𝓝 x] id} with hUdef
  have hUo : IsOpen U := isOpen_setOf_eventually_nhds
  have hUne : U.Nonempty := ⟨x₀, h₀⟩
  have hfix : IsClosed {x : M | f x = id x} := isClosed_eq hfc continuous_id
  have hUc : IsClosed U := by
    refine isClosed_of_closure_subset fun q hq => ?_
    have hfq : f q = q := (closure_minimal (fun x hx => Filter.EventuallyEq.eq_of_nhds (f := f) (g := id) hx) hfix) hq
    set φ := chartAt ℂ q
    have hqs : q ∈ φ.source := mem_chart_source ℂ q
    -- the open set of chart points whose preimage is mapped into the chart
    set W : Set ℂ := φ.target ∩ φ.symm ⁻¹' (f ⁻¹' φ.source) with hW
    have hWo : IsOpen W :=
      φ.continuousOn_symm.isOpen_inter_preimage φ.open_target (φ.open_source.preimage hfc)
    have hqW : φ q ∈ W := by
      refine ⟨φ.map_source hqs, ?_⟩
      simp only [mem_preimage, φ.left_inv hqs, hfq]
      exact hqs
    obtain ⟨r, hr, hB⟩ := Metric.isOpen_iff.1 hWo (φ q) hqW
    set B := Metric.ball (φ q) r
    set F : ℂ → ℂ := fun w => φ (f (φ.symm w))
    have hFd : DifferentiableOn ℂ F B := fun z hz =>
      (differentiableAt_coord hf q (hB hz).1 (hB hz).2).differentiableWithinAt
    have hFa : AnalyticOnNhd ℂ F B := hFd.analyticOnNhd Metric.isOpen_ball
    -- a point of `U` inside the chart ball
    set O : Set M := φ.source ∩ φ ⁻¹' B
    have hOo : IsOpen O := φ.continuousOn.isOpen_inter_preimage φ.open_source Metric.isOpen_ball
    have hqO : q ∈ O := ⟨hqs, Metric.mem_ball_self hr⟩
    obtain ⟨x, hxO, hxU⟩ := mem_closure_iff.1 hq O hOo hqO
    have hxt : φ x ∈ φ.target := φ.map_source hxO.1
    have hFx : F =ᶠ[𝓝 (φ x)] id := by
      have hcont : ContinuousAt φ.symm (φ x) := φ.continuousAt_symm hxt
      have hlim : Tendsto φ.symm (𝓝 (φ x)) (𝓝 x) := by
        have := hcont.tendsto
        rwa [φ.left_inv hxO.1] at this
      filter_upwards [hlim.eventually (hxU : f =ᶠ[𝓝 x] id), φ.open_target.mem_nhds hxt]
        with w hw hwt
      simp only [F, id] at hw ⊢
      rw [hw, φ.right_inv hwt]
    have hEq : EqOn F id B :=
      hFa.eqOn_of_preconnected_of_eventuallyEq analyticOnNhd_id
        (convex_ball (φ q) r).isPreconnected hxO.2 hFx
    -- transport back to `M`
    show f =ᶠ[𝓝 q] id
    have hfs : ∀ᶠ y in 𝓝 q, f y ∈ φ.source :=
      hfc.continuousAt.preimage_mem_nhds (by rw [hfq]; exact φ.open_source.mem_nhds hqs)
    filter_upwards [hOo.mem_nhds hqO, hfs] with y hyO hyf
    have h1 := hEq hyO.2
    simp only [F, id, φ.left_inv hyO.1] at h1
    exact φ.injOn hyf hyO.1 h1
  have hU : U = univ := IsClopen.eq_univ ⟨hUc, hUo⟩ hUne
  funext x
  have hx : x ∈ U := hU ▸ mem_univ x
  exact Filter.EventuallyEq.eq_of_nhds (f := f) (g := id) hx

variable {G : Type*} [Group G] [MulAction G M]

/-- **Local effectiveness from faithfulness.** If `G` acts faithfully on a connected Riemann
surface by holomorphic maps, no `g ≠ 1` fixes a neighbourhood of a point pointwise. -/
theorem local_effective_of_faithful [T2Space M] [ConnectedSpace M] [FaithfulSMul G M]
    (hhol : ∀ g : G, MDifferentiable 𝓘(ℂ) 𝓘(ℂ) (fun x : M => g • x)) (p : M) (g : G)
    (hg : ∀ᶠ y in 𝓝 p, g • y = y) : g = 1 := by
  have h := eq_id_of_eventuallyEq_id (hhol g) (x₀ := p) hg
  exact eq_of_smul_eq_smul fun x => by rw [one_smul]; exact congrFun h x

/-- **Point stabilisers of a finite faithful holomorphic action on a connected Riemann surface
are cyclic.** This is `ChartStep.isCyclic_stabilizer_of_chart` with its local-effectiveness
hypothesis `hloc` discharged by the identity theorem. The holomorphy in the chart `φ` at `p`
remains the chart step's own hypothesis. -/
theorem isCyclic_stabilizer_of_faithful [T2Space M] [ConnectedSpace M] [FaithfulSMul G M]
    [ContinuousConstSMul G M] [Finite G]
    (hhol : ∀ g : G, MDifferentiable 𝓘(ℂ) 𝓘(ℂ) (fun x : M => g • x))
    (φ : OpenPartialHomeomorph M ℂ) (p : M) (hp : p ∈ φ.source) (hφp : φ p = 0)
    (hchart : ∀ g ∈ MulAction.stabilizer G p, ∀ᶠ z in 𝓝 (0 : ℂ),
      DifferentiableAt ℂ (fun z => φ (g • φ.symm z)) z) :
    IsCyclic (MulAction.stabilizer G p) :=
  ChartStep.isCyclic_stabilizer_of_chart φ p hp hφp hchart
    (fun g _ hg => local_effective_of_faithful hhol p g hg)

end QOU.RiemannSurface.IdentityTheorem
