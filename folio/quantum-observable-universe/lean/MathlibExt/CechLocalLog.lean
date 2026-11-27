import MathlibExt.CechChernClass
import Mathlib.Analysis.SpecialFunctions.Complex.Arg

/-!
# Local logarithms on `U(1)` and existence of local real lifts

Bean `qou-bvxd` (parent `qou-533l`), open item (a): the Čech first Chern class
`chernClass γ ξ hξ` of `MathlibExt.CechChernClass` takes the local real lift
`ξ` (`IsRealLift γ ξ`) as an explicit hypothesis. This file proves that such a
lift **exists** whenever each transition function misses a point of the circle.

* `Circle.localLog w z`: a real logarithm of `z ∈ U(1)` that is continuous on
  `U(1) ∖ {w}`, with `Circle.exp (localLog w z) = z` for every `z`
  (`Circle.exp_localLog`) and `continuousAt_localLog` at every `z ≠ w`.
* `Cech.AvoidsPoints γ w`: on every test open, the transition function `γᵢⱼ`
  never takes the value `wᵢⱼ`.
* `Cech.avoidsPoints_of_overlap`: it suffices to check this on the overlaps
  `Uᵢ ⊓ Uⱼ`, by naturality of the cocycle.
* `Cech.realLiftOfAvoids` and `Cech.isRealLift_realLiftOfAvoids`: the cochain
  `ξᵢⱼ = localLog wᵢⱼ ∘ γᵢⱼ` is a local real lift. Hence
  `Cech.exists_isRealLift_of_avoids` and the Chern class
  `Cech.chernClassOfAvoids` with no lift hypothesis.

## What is not done

That every `U(1)`-cocycle avoids points after passing to a suitable refinement
of the cover (by continuity, each `γᵢⱼ` is close to a constant near each point)
is **not** proved here. The cover-independent class then needs the refinement
colimit of `MathlibExt.CechColimit`. The covering-map statement
`IsCoveringMap Circle.exp` (a Mathlib TODO at
`Mathlib/Analysis/SpecialFunctions/Complex/Circle.lean`) is also not used:
the local logarithm only needs continuity of `Complex.arg` off the slit.

Nothing here is a numerical input: `π` enters only as the point `-1 = exp(iπ)`
of the circle and as the period of `exp(i·)`.
-/

-- Ref: [manuscript] lifting-and-descent, thm:qu-to-qou item 2 (Čech c₁, local lifts)

open CategoryTheory Opposite TopologicalSpace Complex

namespace QOU.CentralExtension

namespace Circle

/-- The rotation `z ↦ z w⁻¹ e^{iπ}`, which sends `w` to `-1`. -/
noncomputable def shift (w z : _root_.Circle) : _root_.Circle :=
  z * w⁻¹ * _root_.Circle.exp Real.pi

theorem shift_ne (w z : _root_.Circle) (hz : z ≠ w) :
    shift w z ≠ _root_.Circle.exp Real.pi := by
  intro h
  apply hz
  have h' : z * w⁻¹ = 1 := by
    have := congrArg (· * (_root_.Circle.exp Real.pi)⁻¹) h
    simpa [shift, mul_assoc] using this
  exact mul_inv_eq_one.mp h'

theorem continuous_shift (w : _root_.Circle) : Continuous (shift w) :=
  (continuous_mul_right _).comp (continuous_mul_right _)

/-- A real logarithm of `z ∈ U(1)`, continuous away from `w`:
`localLog w z = arg (z w⁻¹ e^{iπ}) + arg w − π`. -/
noncomputable def localLog (w z : _root_.Circle) : ℝ :=
  arg (shift w z : ℂ) + arg (w : ℂ) - Real.pi

theorem exp_localLog (w z : _root_.Circle) : _root_.Circle.exp (localLog w z) = z := by
  unfold localLog
  rw [sub_eq_add_neg, _root_.Circle.exp_add, _root_.Circle.exp_add, _root_.Circle.exp_arg,
    _root_.Circle.exp_arg, _root_.Circle.exp_neg, shift]
  calc z * w⁻¹ * _root_.Circle.exp Real.pi * w * (_root_.Circle.exp Real.pi)⁻¹
      = z * (w⁻¹ * w) * (_root_.Circle.exp Real.pi * (_root_.Circle.exp Real.pi)⁻¹) := by
        ac_rfl
    _ = z := by rw [inv_mul_cancel, mul_inv_cancel, mul_one, mul_one]

/-- A point of the circle other than `-1 = e^{iπ}` lies in the slit plane. -/
theorem mem_slitPlane_of_ne (h : _root_.Circle) (hh : h ≠ _root_.Circle.exp Real.pi) :
    (h : ℂ) ∈ slitPlane := by
  rw [mem_slitPlane_iff_arg]
  refine ⟨fun harg => hh ?_, _root_.Circle.coe_ne_zero h⟩
  rw [← _root_.Circle.exp_arg h, harg]

theorem continuousAt_localLog (w z : _root_.Circle) (hz : z ≠ w) :
    ContinuousAt (localLog w) z := by
  unfold localLog
  refine ContinuousAt.sub (ContinuousAt.add ?_ continuousAt_const) continuousAt_const
  have h1 : ContinuousAt (fun u : _root_.Circle => (shift w u : ℂ)) z :=
    (continuous_subtype_val.comp (continuous_shift w)).continuousAt
  exact ContinuousAt.comp (g := arg) (continuousAt_arg (mem_slitPlane_of_ne _ (shift_ne w z hz))) h1

end Circle

namespace Cech

variable {X : Type} [TopologicalSpace X] {I : Type} {U : I → Opens X}

/-- Each transition function `γᵢⱼ` misses the point `wᵢⱼ` of the circle, on
every test open. -/
def AvoidsPoints (γ : PresheafOfGroups.OneCocycle (contPresheaf X _root_.Circle) U)
    (w : I → I → _root_.Circle) : Prop :=
  ∀ (i j : I) ⦃T : Opens X⦄ (a : T ⟶ U i) (b : T ⟶ U j) (x : T), sec (γ.ev i j a b) x ≠ w i j

/-- It suffices to check avoidance on the overlaps `Uᵢ ⊓ Uⱼ`. -/
theorem avoidsPoints_of_overlap
    (γ : PresheafOfGroups.OneCocycle (contPresheaf X _root_.Circle) U)
    (w : I → I → _root_.Circle)
    (h : ∀ (i j : I) (x : (U i ⊓ U j : Opens X)),
      sec (γ.ev i j (homOfLE inf_le_left) (homOfLE inf_le_right)) x ≠ w i j) :
    AvoidsPoints γ w := by
  intro i j T a b x
  have hT : T ≤ U i ⊓ U j := le_inf (leOfHom a) (leOfHom b)
  have e := γ.ev_precomp i j (homOfLE hT) (homOfLE inf_le_left) (homOfLE inf_le_right)
  have e' := congrArg (fun F : (contPresheaf X _root_.Circle).obj (op T) => sec F x) e
  simp only at e'
  have ha : a = homOfLE hT ≫ homOfLE inf_le_left := rfl
  have hb : b = homOfLE hT ≫ homOfLE inf_le_right := rfl
  rw [ha, hb, ← e']
  exact h i j ⟨x.1, hT x.2⟩

variable (γ : PresheafOfGroups.OneCocycle (contPresheaf X _root_.Circle) U)
  (w : I → I → _root_.Circle) (hw : AvoidsPoints γ w)

/-- The section `ofAdd ∘ localLog w ∘ f` of `C(T, ℝ)` for a section `f` of
`C(T, U(1))` that misses `w`. -/
noncomputable def logSection {T : Opens X} (w : _root_.Circle)
    (f : (contPresheaf X _root_.Circle).obj (op T)) (hf : ∀ x, sec f x ≠ w) :
    (contPresheaf X (Multiplicative ℝ)).obj (op T) :=
  (⟨fun x => Multiplicative.ofAdd (Circle.localLog w (sec f x)), by
    refine continuous_ofAdd.comp (continuous_iff_continuousAt.mpr fun x => ?_)
    exact (Circle.continuousAt_localLog w _ (hf x)).comp (sec f).continuous.continuousAt⟩ :
    C(T, Multiplicative ℝ))

include hw in
/-- **The local real lift** `ξᵢⱼ = localLog wᵢⱼ ∘ γᵢⱼ`. -/
noncomputable def realLiftOfAvoids :
    PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U where
  ev i j T a b := logSection (w i j) (γ.ev i j a b) (hw i j a b)
  ev_precomp i j T T' φ a b := by
    apply ContinuousMap.ext
    intro x
    have e := γ.ev_precomp i j φ a b
    have e' := congrArg (fun F : (contPresheaf X _root_.Circle).obj (op T) => sec F x) e
    simp only at e'
    change Multiplicative.ofAdd (Circle.localLog (w i j) (sec (γ.ev i j a b) _)) =
      Multiplicative.ofAdd (Circle.localLog (w i j) (sec (γ.ev i j (φ ≫ a) (φ ≫ b)) x))
    rw [← e']
    rfl

include hw in
theorem isRealLift_realLiftOfAvoids : IsRealLift γ (realLiftOfAvoids γ w hw) := by
  intro i j T a b
  apply ContinuousMap.ext
  intro x
  change Circle.exp (Multiplicative.toAdd (Multiplicative.ofAdd
    (Circle.localLog (w i j) (sec (γ.ev i j a b) x)))) = sec (γ.ev i j a b) x
  rw [toAdd_ofAdd]
  exact Circle.exp_localLog _ _

include hw in
/-- **Existence of local real lifts**: a `U(1)`-cocycle whose transition
functions each miss a point of the circle has a local real lift. -/
theorem exists_isRealLift_of_avoids :
    ∃ ξ : PresheafOfGroups.OneCochain (contPresheaf X (Multiplicative ℝ)) U, IsRealLift γ ξ :=
  ⟨realLiftOfAvoids γ w hw, isRealLift_realLiftOfAvoids γ w hw⟩

/-- The Čech first Chern class of a cocycle that avoids points, with the lift
supplied by `realLiftOfAvoids` (no lift hypothesis). By `chernClass_lift_change`
any other real lift changes it by an integer coboundary. -/
noncomputable def chernClassOfAvoids : TwoCochain U (contPresheaf X (Multiplicative ℤ)) :=
  chernClass γ (realLiftOfAvoids γ w hw) (isRealLift_realLiftOfAvoids γ w hw)

end Cech

end QOU.CentralExtension
