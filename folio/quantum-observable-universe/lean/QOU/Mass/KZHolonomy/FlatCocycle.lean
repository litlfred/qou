import QOU.Mass.KZHolonomy.FlatTransport
import QOU.MathlibExt.LocalCocycleTransport

/-!
# A flat connection on an open set is a local cocycle

Let `D ⊆ E` be open and `ω` a flat connection form on `D` (`IsFlatOn`).  For `x ∈ D` pick a ball
`B x ⊆ D` around `x` and let `Φ_x = radialTransport ω x` (transport along straight segments out
of `x`).  On `B x`, transport only depends on endpoints (`flat_transport_eq`), so for
`y, z ∈ B x`

    Φ_y(z) · Φ_x(y) = Φ_x(z).

Transport composes on the left (`U' = X U`), so the cocycle takes values in the opposite group
of units, `Aˣᵐᵒᵖ`.  `flatCocycle` packages this as a `LocalCocycle` on the subtype `D`, and
`LocalCocycle.transport` then extends the transport of `ω` to every continuous path in `D`,
homotopy invariantly (`QOU.MathlibExt.LocalCocycleTransport`).
-/

set_option autoImplicit false
set_option linter.unusedSectionVars false

namespace QOU.Mass.KZHolonomy

open Set Metric QOU.MathlibExt

variable {E A : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedRing A] [NormedAlgebra ℝ A] [CompleteSpace A]

omit [CompleteSpace A] in
theorem IsFlatOn.mono' {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A} {D D' : Set E}
    (h : IsFlatOn ω ω' D) (hD : D' ⊆ D) : IsFlatOn ω ω' D' :=
  ⟨fun y hy => h.hasFDerivAt y (hD hy), h.continuousOn.mono hD, fun y hy => h.flat y (hD hy)⟩

/-- **Local cocycle identity.**  On a convex open set `B` on which `ω` is flat, radial transport
from `y` to `z` composed after radial transport from `x` to `y` is radial transport from `x` to
`z`, for `x, y, z ∈ B`. -/
theorem radialTransport_comp {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A} {B : Set E}
    (hB : IsOpen B) (hconv : Convex ℝ B) (hfl : IsFlatOn ω ω' B) {x y z : E}
    (hx : x ∈ B) (hy : y ∈ B) (hz : z ∈ B) :
    radialTransport ω y z * radialTransport ω x y = radialTransport ω x z := by
  set γ : ℝ → E := fun t => y + t • (z - y)
  have hγD : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ B := fun t ht =>
    seg_mem_of_starConvex (hconv.starConvex hy) hz ht
  have hγd : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt γ (z - y) (Icc 0 1) t := fun t _ => by
    have := ((hasDerivAt_id t).smul_const (z - y)).const_add y
    simpa [γ] using this.hasDerivWithinAt
  have hXc : ContinuousOn (radialX ω y z) (Icc 0 1) := continuousOn_radialX fun t ht =>
    (hfl.hasFDerivAt _ (hγD t ht)).continuousAt
  obtain ⟨U, hU⟩ := exists_isFundSol hXc
  have h := flat_transport_eq hB (hconv.starConvex hx) hfl hγD hγd continuousOn_const
    (γ' := fun _ => z - y) hU
  rw [radialTransport_eq hXc hU]
  simpa [γ] using h

theorem isUnit_radialTransport_of_convex {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A}
    {B : Set E} (hconv : Convex ℝ B) (hfl : IsFlatOn ω ω' B) {x y : E} (hx : x ∈ B)
    (hy : y ∈ B) : IsUnit (radialTransport ω x y) :=
  isUnit_radialTransport (hconv.starConvex hx) hfl hy

/-- Radial transport as an element of `Aˣᵐᵒᵖ` (and `1` where it is not a unit). -/
noncomputable def radialUnit (ω : E → E →L[ℝ] A) (x y : E) : Aˣᵐᵒᵖ := by
  classical
  exact if h : IsUnit (radialTransport ω x y) then MulOpposite.op h.unit else 1

theorem radialUnit_val {ω : E → E →L[ℝ] A} {x y : E} (h : IsUnit (radialTransport ω x y)) :
    ((radialUnit ω x y).unop : A) = radialTransport ω x y := by
  rw [radialUnit, dif_pos h]; rfl

variable {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A} {D : Set E}

/-- A radius at each point of an open set, with the ball inside the set. -/
noncomputable def ballRadius (hD : IsOpen D) (x : D) : ℝ :=
  (Metric.isOpen_iff.mp hD x.1 x.2).choose

theorem ballRadius_pos (hD : IsOpen D) (x : D) : 0 < ballRadius hD x :=
  (Metric.isOpen_iff.mp hD x.1 x.2).choose_spec.1

theorem ball_subset (hD : IsOpen D) (x : D) : ball x.1 (ballRadius hD x) ⊆ D :=
  (Metric.isOpen_iff.mp hD x.1 x.2).choose_spec.2

/-- **The local cocycle of a flat connection** on an open set `D`. -/
noncomputable def flatCocycle (hD : IsOpen D) (hfl : IsFlatOn ω ω' D) : LocalCocycle D Aˣᵐᵒᵖ where
  P x y := radialUnit ω x.1 y.1
  U x := Subtype.val ⁻¹' ball x.1 (ballRadius hD x)
  isOpen_U x := isOpen_ball.preimage continuous_subtype_val
  mem_U x := mem_ball_self (ballRadius_pos hD x)
  cocycle x y hy z hz := by
    have hB := hfl.mono' (ball_subset hD x)
    have hc := convex_ball x.1 (ballRadius hD x)
    have hx : x.1 ∈ ball x.1 (ballRadius hD x) := mem_ball_self (ballRadius_pos hD x)
    apply MulOpposite.unop_injective
    apply Units.ext
    rw [MulOpposite.unop_mul, Units.val_mul,
      radialUnit_val (isUnit_radialTransport_of_convex hc hB hy hz),
      radialUnit_val (isUnit_radialTransport_of_convex hc hB hx hy),
      radialUnit_val (isUnit_radialTransport_of_convex hc hB hx hz)]
    exact radialTransport_comp isOpen_ball hc hB hx hy hz

theorem flatCocycle_P (hD : IsOpen D) (hfl : IsFlatOn ω ω' D) (x y : D) :
    (flatCocycle hD hfl).P x y = radialUnit ω x.1 y.1 := rfl

end QOU.Mass.KZHolonomy
