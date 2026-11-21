import Mathlib.Topology.FiberBundle.Basic
import Mathlib.Topology.Covering
import Mathlib.Topology.Homotopy.Lifting
import Mathlib.Tactic.Group
import Mathlib.AlgebraicTopology.FundamentalGroupoid.Basic

/-!
# Transport of a local cocycle along continuous paths

Let `X` be a topological space and `G` a group.  A **local cocycle** assigns to every point `x`
an open neighbourhood `U x` and to every pair of points an element `P x y : G`, such that
`P x y * P y z = P x z` whenever `y, z ∈ U x`.  (This is what the parallel transport of a flat
connection gives on small convex balls; see `QOU.Mass.KZHolonomy.flat_transport_eq`.)

We extend `P` to **every continuous path** and prove that the result depends only on the
homotopy class rel endpoints and is multiplicative under concatenation.

## Method

The cocycle is turned into a fibre bundle with discrete fibre `G` (a `FiberBundleCore` whose
transition maps are `g ↦ g · P i y · (P j y)⁻¹`; these are constant on each overlap, which is
the only use of the cocycle identity).  A bundle with discrete fibre is a covering map
(`FiberBundle.isCoveringMap`), so Mathlib's path lifting and its monodromy theorem
(`IsCoveringMap.liftPath_apply_one_eq_of_homotopicRel`) do the topology.  The transport of a
path is the fibre coordinate of the endpoint of its lift starting at `1`.

## Results

* `LocalCocycle.transport_of_subset`: a path inside `U x` from `x` to `y` has transport `P x y`.
* `LocalCocycle.transport_trans`: `transport (γ.trans δ) = transport γ * transport δ`.
* `LocalCocycle.transport_eq_of_homotopic`: homotopic paths have equal transport.

Everything here is general topology; nothing about `ℂ`, connections or braids is used.
-/

namespace QOU.MathlibExt

open Topology Set unitInterval Bundle

/-- A group, carrying the discrete topology. -/
def Disc (G : Type*) : Type _ := G

namespace Disc
variable {G : Type*}
instance : TopologicalSpace (Disc G) := ⊥
instance : DiscreteTopology (Disc G) := ⟨rfl⟩
/-- Into the discrete copy. -/
def of (g : G) : Disc G := g
/-- Out of the discrete copy. -/
def val (g : Disc G) : G := g
@[simp] theorem val_of (g : G) : val (of g) = g := rfl
@[simp] theorem of_val (g : Disc G) : of (val g) = g := rfl
end Disc

/-- A local cocycle on `X` with values in `G`. -/
structure LocalCocycle (X : Type*) [TopologicalSpace X] (G : Type*)
    [Group G] where
  /-- The local transport. -/
  P : X → X → G
  /-- The neighbourhood on which the cocycle identity holds, centred at `x`. -/
  U : X → Set X
  isOpen_U : ∀ x, IsOpen (U x)
  mem_U : ∀ x, x ∈ U x
  cocycle : ∀ x, ∀ y ∈ U x, ∀ z ∈ U x, P x y * P y z = P x z

namespace LocalCocycle

variable {X : Type*} [TopologicalSpace X] {G : Type*} [Group G] (C : LocalCocycle X G)

theorem P_self (x : X) : C.P x x = 1 :=
  mul_eq_left.mp (C.cocycle x x (C.mem_U x) x (C.mem_U x))

/-- The transition element `P i y · (P j y)⁻¹` is constant on `U i ∩ U j`. -/
theorem transition_eq (i j : X) {y y' : X} (hy : y ∈ C.U i ∩ C.U j) (hy' : y' ∈ C.U i ∩ C.U j) :
    C.P i y' * (C.P j y')⁻¹ = C.P i y * (C.P j y)⁻¹ := by
  rw [← C.cocycle i y hy.1 y' hy'.1, ← C.cocycle j y hy.2 y' hy'.2]
  group

/-- The fibre bundle with discrete fibre `G` attached to the cocycle. -/
noncomputable def core : FiberBundleCore X X (Disc G) where
  baseSet := C.U
  isOpen_baseSet := C.isOpen_U
  indexAt := id
  mem_baseSet_at := C.mem_U
  coordChange i j y g := Disc.of (g.val * (C.P i y * (C.P j y)⁻¹))
  coordChange_self i y _ g := by simp
  continuousOn_coordChange i j := by
    rcases (C.U i ∩ C.U j).eq_empty_or_nonempty with h | ⟨y₀, hy₀⟩
    · simp [h]
    · have hc : Continuous fun p : X × Disc G => Disc.of (p.2.val * (C.P i y₀ * (C.P j y₀)⁻¹)) :=
        (continuous_of_discreteTopology (f := fun g : Disc G =>
          Disc.of (g.val * (C.P i y₀ * (C.P j y₀)⁻¹)))).comp continuous_snd
      refine hc.continuousOn.congr fun p hp => ?_
      show Disc.of _ = Disc.of _
      rw [C.transition_eq i j hp.1 hy₀]
  coordChange_comp i j k y _ g := by
    simp only [Disc.val_of]
    congr 1
    group

theorem core_coordChange (i j y : X) (g : Disc G) :
    C.core.coordChange i j y g = Disc.of (g.val * (C.P i y * (C.P j y)⁻¹)) := rfl

theorem isCoveringMap : IsCoveringMap (TotalSpace.proj : C.core.TotalSpace → X) :=
  FiberBundle.isCoveringMap

/-- The fibre coordinate of a point of the total space, as an element of `G`. -/
def fib (p : C.core.TotalSpace) : G := Disc.val (G := G) p.2

/-- The point of the total space over `y` with fibre coordinate `g`. -/
def pt (y : X) (g : G) : C.core.TotalSpace := ⟨y, (Disc.of g : Disc G)⟩

@[simp] theorem pt_proj (y : X) (g : G) : (C.pt y g).proj = y := rfl
@[simp] theorem fib_pt (y : X) (g : G) : C.fib (C.pt y g) = g := rfl

theorem ext_pt (p : C.core.TotalSpace) : C.pt p.proj (C.fib p) = p := rfl

/-- Left multiplication on the fibres: an automorphism of the bundle over `X`. -/
def mulLeft (a : G) (p : C.core.TotalSpace) : C.core.TotalSpace := C.pt p.proj (a * C.fib p)

theorem continuous_mulLeft (a : G) : Continuous (C.mulLeft a) := by
  refine continuous_iff_continuousAt.mpr fun p₀ => ?_
  rw [FiberBundle.continuousAt_totalSpace]
  refine ⟨(FiberBundle.continuous_proj (Disc G) C.core.Fiber).continuousAt, ?_⟩
  have h := ((FiberBundle.continuousAt_totalSpace (F := Disc G) (E := C.core.Fiber) id
    (x₀ := p₀)).mp continuousAt_id).2
  have hm : Continuous fun g : Disc G => Disc.of (a * g.val) := continuous_of_discreteTopology
  refine (hm.continuousAt.comp h).congr (Filter.Eventually.of_forall fun p => ?_)
  show Disc.of (a * (Disc.val (C.core.coordChange p.proj p₀.proj p.proj p.2))) =
    C.core.coordChange p.proj p₀.proj p.proj (Disc.of (a * C.fib p))
  simp only [core_coordChange, Disc.val_of, fib]
  congr 1
  group

/-- The lift of a path starting at fibre coordinate `g`. -/
noncomputable def lift {x y : X} (γ : Path x y) (g : G) : C(I, C.core.TotalSpace) :=
  C.isCoveringMap.liftPath γ.toContinuousMap (C.pt x g) γ.source

theorem lift_proj {x y : X} (γ : Path x y) (g : G) (t : I) : (C.lift γ g t).proj = γ t :=
  congrFun (C.isCoveringMap.liftPath_lifts γ.toContinuousMap (C.pt x g) γ.source) t

theorem lift_zero {x y : X} (γ : Path x y) (g : G) : C.lift γ g 0 = C.pt x g :=
  C.isCoveringMap.liftPath_zero γ.toContinuousMap (C.pt x g) γ.source

/-- Lifts are equivariant for left multiplication. -/
theorem lift_mul {x y : X} (γ : Path x y) (a g : G) (t : I) :
    C.lift γ (a * g) t = C.mulLeft a (C.lift γ g t) := by
  have := (C.isCoveringMap.eq_liftPath_iff (Γ := C.mulLeft a ∘ C.lift γ g)
    (γ := γ.toContinuousMap) (e := C.pt x (a * g)) γ.source).mpr
    ⟨(C.continuous_mulLeft a).comp (C.lift γ g).continuous,
     funext fun s => C.lift_proj γ g s,
     by simp only [Function.comp_apply, lift_zero]; rfl⟩
  exact (congrFun this t).symm

/-- **Transport** of a path: the fibre coordinate at the end of its lift from `1`. -/
noncomputable def transport {x y : X} (γ : Path x y) : G := C.fib (C.lift γ 1 1)

theorem lift_one_eq {x y : X} (γ : Path x y) (g : G) :
    C.lift γ g 1 = C.pt y (g * C.transport γ) := by
  have h := C.lift_mul γ g 1 1
  rw [mul_one] at h
  rw [h, mulLeft, C.lift_proj, γ.target]
  rfl

/-- A path inside `U i` lifts with constant chart-`i` coordinate. -/
theorem lift_of_subset {x y : X} (γ : Path x y) (g : G) (i : X) (hγ : ∀ t, γ t ∈ C.U i) (t : I) :
    C.lift γ g t = C.pt (γ t) (g * (C.P i x)⁻¹ * C.P i (γ t)) := by
  let c : Disc G := Disc.of (g * (C.P i x)⁻¹)
  let e := (C.core.localTriv i).toOpenPartialHomeomorph
  have hval : ∀ s, e.symm (γ s, c) = C.pt (γ s) (g * (C.P i x)⁻¹ * C.P i (γ s)) := by
    intro s
    show (⟨γ s, C.core.coordChange i (γ s) (γ s) c⟩ : C.core.TotalSpace) = _
    rw [core_coordChange, C.P_self]
    simp [c, pt]
  have hcont : Continuous fun s => e.symm (γ s, c) :=
    e.continuousOn_symm.comp_continuous (γ.continuous.prodMk continuous_const)
      fun s => (C.core.mem_localTriv_target i _).mpr (hγ s)
  have := (C.isCoveringMap.eq_liftPath_iff (Γ := fun s => e.symm (γ s, c))
    (γ := γ.toContinuousMap) (e := C.pt x g) γ.source).mpr
    ⟨hcont, funext fun s => by rw [Function.comp_apply, hval]; rfl, by
      rw [hval, γ.source]; simp⟩
  rw [← hval t]
  exact (congrFun this t).symm

/-- **Recognising a lift.**  If `v : I → G` starts at `g` and is locally of the form
`v t = v t₀ · P (γ t₀) (γ t)`, then `t ↦ (γ t, v t)` is the lift of `γ` from `g`. -/
theorem lift_eq_of_local {x y : X} (γ : Path x y) (g : G) (v : I → G) (hv0 : v 0 = g)
    (hv : ∀ t₀, ∀ᶠ t in nhds t₀, v t = v t₀ * C.P (γ t₀) (γ t)) (t : I) :
    C.lift γ g t = C.pt (γ t) (v t) := by
  have hcont : Continuous fun s => C.pt (γ s) (v s) := by
    refine continuous_iff_continuousAt.mpr fun t₀ => ?_
    rw [FiberBundle.continuousAt_totalSpace]
    refine ⟨γ.continuous.continuousAt, ?_⟩
    refine (continuousAt_const (y := (Disc.of (v t₀) : Disc G))).congr ?_
    filter_upwards [hv t₀] with s hs
    show Disc.of (v t₀) = C.core.coordChange (γ s) (γ t₀) (γ s) (Disc.of (v s))
    rw [core_coordChange, C.P_self, hs]
    simp
  have := (C.isCoveringMap.eq_liftPath_iff (Γ := fun s => C.pt (γ s) (v s))
    (γ := γ.toContinuousMap) (e := C.pt x g) γ.source).mpr
    ⟨hcont, funext fun s => rfl, by simp [hv0, pt]⟩
  exact (congrFun this t).symm

/-- The transport of `γ` read off from a local description of its lift from `1`. -/
theorem transport_eq_of_local {x y : X} (γ : Path x y) (v : I → G) (hv0 : v 0 = 1)
    (hv : ∀ t₀, ∀ᶠ t in nhds t₀, v t = v t₀ * C.P (γ t₀) (γ t)) :
    C.transport γ = v 1 := by
  rw [transport, C.lift_eq_of_local γ 1 v hv0 hv]
  rfl

/-- A path inside `U x` from `x` to `y` has transport `P x y`. -/
theorem transport_of_subset {x y : X} (γ : Path x y) (hγ : ∀ t, γ t ∈ C.U x) :
    C.transport γ = C.P x y := by
  have h := C.lift_of_subset γ 1 x hγ 1
  rw [C.lift_one_eq, γ.target, C.P_self] at h
  have h2 := congrArg C.fib h
  simpa using h2

/-- The lift of a path from `g`, as a path in the total space. -/
noncomputable def liftAsPath {x y : X} (γ : Path x y) (g : G) :
    Path (C.pt x g) (C.pt y (g * C.transport γ)) where
  toContinuousMap := C.lift γ g
  source' := C.lift_zero γ g
  target' := C.lift_one_eq γ g

/-- Transport is multiplicative under concatenation. -/
theorem transport_trans {x y z : X} (γ : Path x y) (δ : Path y z) :
    C.transport (γ.trans δ) = C.transport γ * C.transport δ := by
  let Γ := (C.liftAsPath γ 1).trans (C.liftAsPath δ (1 * C.transport γ))
  have hT : C.pt z (1 * C.transport γ * C.transport δ) = Γ 1 := Γ.target.symm
  have hproj : Γ.map (FiberBundle.continuous_proj (Disc G) C.core.Fiber) = γ.trans δ := by
    rw [Path.map_trans]
    congr 1 <;> ext t <;> exact C.lift_proj _ _ t
  have hl := (C.isCoveringMap.eq_liftPath_iff (Γ := Γ) (γ := (γ.trans δ).toContinuousMap)
    (e := C.pt x 1) (γ.trans δ).source).mpr
    ⟨Γ.continuous, funext fun t => congrArg (fun p : Path x z => p t) hproj, Γ.source⟩
  have h1 : C.lift (γ.trans δ) 1 1 = Γ 1 := (congrFun hl 1).symm
  rw [← hT, C.lift_one_eq] at h1
  have h2 := congrArg C.fib h1
  simpa using h2

/-- Homotopic paths have the same transport. -/
theorem transport_eq_of_homotopic {x y : X} {γ γ' : Path x y} (h : γ.Homotopic γ') :
    C.transport γ = C.transport γ' := by
  have := C.isCoveringMap.liftPath_apply_one_eq_of_homotopicRel h (C.pt x 1) γ.source γ'.source
  exact congrArg C.fib this

/-- Transport on homotopy classes of paths. -/
noncomputable def transportQ {x y : X} : Path.Homotopic.Quotient x y → G :=
  Quotient.lift C.transport fun _ _ h => C.transport_eq_of_homotopic h

theorem transportQ_mk {x y : X} (γ : Path x y) : C.transportQ ⟦γ⟧ = C.transport γ := rfl

theorem transport_refl (x : X) : C.transport (Path.refl x) = 1 := by
  rw [C.transport_of_subset _ fun _ => C.mem_U x, C.P_self]

theorem transport_symm {x y : X} (γ : Path x y) : C.transport γ.symm = (C.transport γ)⁻¹ := by
  have h := C.transport_eq_of_homotopic ⟨Path.Homotopy.reflTransSymm γ⟩
  rw [transport_refl, transport_trans] at h
  exact eq_inv_of_mul_eq_one_right h.symm

/-! ### Gauge between two cocycles with conjugate monodromy

Given two local cocycles `C₁, C₂` and `c : G` with `T₁(λ)⁻¹ · c · T₂(λ) = c` for every loop `λ`
at `x₀`, the element `T₁(γ)⁻¹ · c · T₂(γ)` depends only on the endpoint `y` of a path `γ` from
`x₀`.  This is the single-valued gauge between the two local systems. -/

section Gauge

variable (C₁ C₂ : LocalCocycle X G) (x₀ : X) (c : G)

/-- The gauge computed along a path from the base point. -/
noncomputable def gaugeAlong {y : X} (γ : Path x₀ y) : G :=
  (C₁.transport γ)⁻¹ * c * C₂.transport γ

/-- The monodromies of `C₁` and `C₂` at `x₀` are conjugate by `c`. -/
def ConjMonodromy : Prop :=
  ∀ l : Path x₀ x₀, (C₁.transport l)⁻¹ * c * C₂.transport l = c

variable {C₁ C₂ x₀ c}

theorem gaugeAlong_eq (h : ConjMonodromy C₁ C₂ x₀ c) {y : X} (γ γ' : Path x₀ y) :
    gaugeAlong C₁ C₂ x₀ c γ = gaugeAlong C₁ C₂ x₀ c γ' := by
  have hl := h (γ.trans γ'.symm)
  rw [C₁.transport_trans, C₂.transport_trans, C₁.transport_symm, C₂.transport_symm] at hl
  unfold gaugeAlong
  nth_rewrite 2 [← hl]
  group

variable (C₁ C₂ x₀ c) in
/-- The single-valued gauge on a path-connected space. -/
noncomputable def gauge [PathConnectedSpace X] (y : X) : G :=
  gaugeAlong C₁ C₂ x₀ c (PathConnectedSpace.somePath x₀ y)

theorem gauge_eq_along [PathConnectedSpace X] (h : ConjMonodromy C₁ C₂ x₀ c) {y : X}
    (γ : Path x₀ y) : gauge C₁ C₂ x₀ c y = gaugeAlong C₁ C₂ x₀ c γ :=
  gaugeAlong_eq h _ _

/-- **Local formula for the gauge.**  If a path from `y` to `z` stays in both cocycle
neighbourhoods of `y`, then `g z = P₁(y,z)⁻¹ · g y · P₂(y,z)`. -/
theorem gauge_local [PathConnectedSpace X] (h : ConjMonodromy C₁ C₂ x₀ c) {y z : X}
    (δ : Path y z) (h₁ : ∀ t, δ t ∈ C₁.U y) (h₂ : ∀ t, δ t ∈ C₂.U y) :
    gauge C₁ C₂ x₀ c z = (C₁.P y z)⁻¹ * gauge C₁ C₂ x₀ c y * C₂.P y z := by
  rw [gauge_eq_along h ((PathConnectedSpace.somePath x₀ y).trans δ), gaugeAlong, C₁.transport_trans, C₂.transport_trans,
    C₁.transport_of_subset δ h₁, C₂.transport_of_subset δ h₂, gauge, gaugeAlong]
  group

end Gauge

end LocalCocycle

end QOU.MathlibExt
