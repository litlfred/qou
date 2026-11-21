import QOU.RiemannSurface.GermStabiliserCyclic
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Topology.OpenPartialHomeomorph
import Mathlib.Topology.Algebra.ConstMulAction

/-!
# `QOU.RiemannSurface.ChartStep` — a holomorphic point stabiliser is a germ action

Bean `qou-mq3p` / `qou-m1bg` (Bring milestone M2, the chart step), parent `qou-qhcr`.

Let a group `G` act continuously on a space `M`, fix a point `p`, and let `φ` be a chart of `M`
at `p` into `ℂ` with `φ p = 0`. Suppose each `g` is **holomorphic at `p` in that chart**: its
coordinate expression `z ↦ φ (g • φ⁻¹ z)` is complex-differentiable on a neighbourhood of `0`.
Then:

* `germAction`: the coordinate expressions form a `GermAction G ℂ` (the action laws hold near
  `0`, each germ fixes `0` and is analytic there);
* `germ_effective_of_local`: if no `g ≠ 1` fixes a neighbourhood of `p` pointwise, the germ
  action is effective;
* **`isCyclic_of_chart`**: so `G` is cyclic when finite, and
  `isCyclic_stabilizer_of_chart`: the stabiliser of `p` under a finite holomorphic action is
  cyclic.

This discharges the chart step left open in `GermStabiliserCyclic`. The holomorphy hypothesis is
the definition of a holomorphic action read in one chart; analyticity is derived from it
(`DifferentiableOn.analyticAt`, Cauchy–Goursat).

## What stays a hypothesis

* **Local effectiveness** (`hloc`): no non-identity element fixes a neighbourhood of `p`. For an
  effective action on a *connected* Riemann surface this is the identity theorem on the surface,
  which Mathlib does not state for complex manifolds. It is a geometric hypothesis here, not an
  axiom.
* The chart `φ` is supplied; Mathlib's `ChartedSpace ℂ M` provides one at every point, but the
  holomorphy of the action is stated in that chart rather than via `MDifferentiable`.
-/

namespace QOU.RiemannSurface.ChartStep

open Filter Topology
open QOU.RiemannSurface.GermStabiliserCyclic

variable {M : Type*} [TopologicalSpace M] {G : Type*} [Group G] [MulAction G M]
  [ContinuousConstSMul G M]
  (φ : OpenPartialHomeomorph M ℂ) (p : M) (hp : p ∈ φ.source) (hφp : φ p = 0)

/-- The coordinate expression of `g` in the chart `φ`. -/
def coord (g : G) (z : ℂ) : ℂ := φ (g • φ.symm z)

include hp hφp in
theorem symm_zero : φ.symm 0 = p := by rw [← hφp, φ.left_inv hp]

include hp hφp in
theorem zero_mem_target : (0 : ℂ) ∈ φ.target := hφp ▸ φ.map_source hp

include hp hφp in
theorem target_mem_nhds : φ.target ∈ 𝓝 (0 : ℂ) :=
  φ.open_target.mem_nhds (zero_mem_target φ p hp hφp)

include hp hφp in
/-- `z ↦ g • φ⁻¹ z` lands in the chart source near `0`, when `g` fixes `p`. -/
theorem eventually_smul_symm_mem (g : G) (hg : g • p = p) :
    ∀ᶠ z in 𝓝 (0 : ℂ), g • φ.symm z ∈ φ.source := by
  have hcont : ContinuousAt (fun z => g • φ.symm z) 0 :=
    (continuous_const_smul g).continuousAt.comp
      (φ.continuousAt_symm (zero_mem_target φ p hp hφp))
  have hval : g • φ.symm 0 = p := by rw [symm_zero φ p hp hφp, hg]
  have := hcont.preimage_mem_nhds (by rw [hval]; exact φ.open_source.mem_nhds hp)
  exact this

include hp hφp in
/-- **The chart step.** Holomorphic coordinate expressions of a point stabiliser form a germ
action at `0`. -/
noncomputable def germAction (hfix : ∀ g : G, g • p = p)
    (hhol : ∀ g : G, ∀ᶠ z in 𝓝 (0 : ℂ), DifferentiableAt ℂ (coord φ g) z) : GermAction G ℂ :=
  GermAction.ofAnalytic (coord φ)
    (fun g => by simp only [coord]; rw [symm_zero φ p hp hφp, hfix g, hφp])
    (fun g => by
      obtain ⟨s, hs, hd⟩ := (hhol g).exists_mem
      exact DifferentiableOn.analyticAt (fun z hz => (hd z hz).differentiableWithinAt) hs)
    (by
      filter_upwards [target_mem_nhds φ p hp hφp] with z hz
      simp [coord, φ.right_inv hz])
    (fun g h => by
      filter_upwards [eventually_smul_symm_mem φ p hp hφp h (hfix h)] with z hz
      simp only [coord, Function.comp, φ.left_inv hz, mul_smul])

include hp hφp in
/-- Local effectiveness at `p` gives effectiveness of the germ action. -/
theorem germ_effective_of_local (hfix : ∀ g : G, g • p = p)
    (hloc : ∀ g : G, (∀ᶠ y in 𝓝 p, g • y = y) → g = 1)
    (g : G) (hg : coord φ g =ᶠ[𝓝 0] id) : g = 1 := by
  apply hloc g
  have hφ : Tendsto φ (𝓝 p) (𝓝 0) := by
    have := φ.continuousAt hp
    rwa [ContinuousAt, hφp] at this
  have hsmul : ∀ᶠ y in 𝓝 p, g • y ∈ φ.source := by
    have hc : ContinuousAt (fun y => g • y) p := (continuous_const_smul g).continuousAt
    have := hc.preimage_mem_nhds (by rw [hfix g]; exact φ.open_source.mem_nhds hp)
    exact this
  filter_upwards [hφ.eventually hg, φ.open_source.mem_nhds hp, hsmul] with y hy hys hgys
  simp only [coord, id, φ.left_inv hys] at hy
  exact φ.injOn hgys hys hy

include hp hφp in
/-- **A finite group acting holomorphically and locally effectively, fixing `p`, is cyclic.** -/
theorem isCyclic_of_chart [Fintype G] (hfix : ∀ g : G, g • p = p)
    (hhol : ∀ g : G, ∀ᶠ z in 𝓝 (0 : ℂ), DifferentiableAt ℂ (coord φ g) z)
    (hloc : ∀ g : G, (∀ᶠ y in 𝓝 p, g • y = y) → g = 1) : IsCyclic G :=
  (germAction φ p hp hφp hfix hhol).isCyclic
    (germ_effective_of_local φ p hp hφp hfix hloc)

include hp hφp in
/-- **Point stabilisers of a finite holomorphic action are cyclic.** -/
theorem isCyclic_stabilizer_of_chart [Finite G]
    (hhol : ∀ g ∈ MulAction.stabilizer G p, ∀ᶠ z in 𝓝 (0 : ℂ),
      DifferentiableAt ℂ (fun z => φ (g • φ.symm z)) z)
    (hloc : ∀ g ∈ MulAction.stabilizer G p, (∀ᶠ y in 𝓝 p, g • y = y) → g = 1) :
    IsCyclic (MulAction.stabilizer G p) := by
  haveI : Fintype (MulAction.stabilizer G p) := Fintype.ofFinite _
  haveI : ContinuousConstSMul (MulAction.stabilizer G p) M :=
    ⟨fun g => continuous_const_smul (g : G)⟩
  exact isCyclic_of_chart (G := MulAction.stabilizer G p) φ p hp hφp
    (fun g => g.2) (fun g => hhol g.1 g.2) (fun g hg => Subtype.ext (hloc g.1 g.2 hg))

end QOU.RiemannSurface.ChartStep
