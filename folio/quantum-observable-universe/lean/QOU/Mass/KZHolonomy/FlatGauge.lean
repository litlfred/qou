import QOU.Mass.KZHolonomy.FlatCocycle

/-!
# Conjugate monodromy gives a single-valued differentiable gauge

Let `D ⊆ E` be open and path-connected and `ω₁, ω₂` flat connection forms on `D`.  Transport of
`ωᵢ` along continuous paths is `LocalCocycle.transport (flatCocycle hD hᵢ)`
(`QOU.MathlibExt.LocalCocycleTransport`, `FlatCocycle`).  Suppose the two monodromies at a base
point `x₀` are conjugate by `c`, in the sense of `LocalCocycle.ConjMonodromy`.  Then

    g(y) = T₂(γ) · c · T₁(γ)⁻¹        (γ any path from x₀ to y)

is well defined (`LocalCocycle.gauge`), a unit at every point, and **differentiable** with

    dg(y)(v) = ω₂(y)(v) · g(y) − g(y) · ω₁(y)(v),

i.e. `ω₂ = (dg + g ω₁) g⁻¹`: the two connections are gauge equivalent by a single-valued
differentiable gauge (`hasFDerivAt_flatGauge`).  This is the uniqueness half of the
Riemann–Hilbert correspondence in the smooth category, proved from Mathlib's covering-space
theory and the corpus's flat transport; no analytic input beyond `IsFlatOn` is used.

(The algebraic upgrade, `g` rational on `Conf_n`, is Deligne's theorem and is not proved here.)
-/

set_option autoImplicit false
set_option linter.unusedSectionVars false

namespace QOU.Mass.KZHolonomy

open Set Metric QOU.MathlibExt

variable {E A : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedRing A] [NormedAlgebra ℝ A] [CompleteSpace A]
  {ω₁ ω₂ : E → E →L[ℝ] A} {ω₁' ω₂' : E → E →L[ℝ] E →L[ℝ] A} {D : Set E}

theorem radialTransport_self_of_mem {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A}
    (hD : IsOpen D) (hfl : IsFlatOn ω ω' D) (y : D) : radialTransport ω y.1 y.1 = 1 := by
  have hu := isUnit_radialTransport_of_convex (convex_ball y.1 (ballRadius hD y))
    (hfl.mono' (ball_subset hD y)) (mem_ball_self (ballRadius_pos hD y))
    (mem_ball_self (ballRadius_pos hD y))
  have h := congrArg (fun u : Aˣᵐᵒᵖ => (u.unop : A)) ((flatCocycle hD hfl).P_self y)
  simpa [flatCocycle_P, radialUnit_val hu] using h

/-- The straight segment from `y` to `z` inside `D`, when it lies in the cocycle ball of `y`. -/
noncomputable def segPath (hD : IsOpen D) (y : D) (z : E) (hz : z ∈ ball y.1 (ballRadius hD y)) :
    Path y ⟨z, ball_subset hD y hz⟩ where
  toFun t := ⟨y.1 + (t : ℝ) • (z - y.1), ball_subset hD y
    ((convex_ball y.1 _).add_smul_sub_mem (mem_ball_self (ballRadius_pos hD y)) hz t.2)⟩
  continuous_toFun := by fun_prop
  source' := by ext; simp
  target' := by ext; simp

theorem segPath_mem (hD : IsOpen D) (y : D) (z : E) (hz : z ∈ ball y.1 (ballRadius hD y))
    (t : unitInterval) : (segPath hD y z hz t).1 ∈ ball y.1 (ballRadius hD y) :=
  (convex_ball y.1 _).add_smul_sub_mem (mem_ball_self (ballRadius_pos hD y)) hz t.2

variable (hD : IsOpen D) (h₁ : IsFlatOn ω₁ ω₁' D) (h₂ : IsFlatOn ω₂ ω₂' D)
  [PathConnectedSpace D] (x₀ : D) (c : Aˣᵐᵒᵖ)

/-- The gauge, as an `A`-valued function on `E` (zero off `D`). -/
noncomputable def flatGauge (z : E) : A := by
  classical
  exact if hz : z ∈ D then
    ((LocalCocycle.gauge (flatCocycle hD h₁) (flatCocycle hD h₂) x₀ c ⟨z, hz⟩).unop : A)
  else 0

variable {hD h₁ h₂ x₀ c}

theorem flatGauge_of_mem {z : E} (hz : z ∈ D) :
    flatGauge hD h₁ h₂ x₀ c z =
      ((LocalCocycle.gauge (flatCocycle hD h₁) (flatCocycle hD h₂) x₀ c ⟨z, hz⟩).unop : A) := by
  rw [flatGauge, dif_pos hz]

theorem isUnit_flatGauge {z : E} (hz : z ∈ D) : IsUnit (flatGauge hD h₁ h₂ x₀ c z) := by
  rw [flatGauge_of_mem hz]; exact Units.isUnit _

/-- **Local formula**: on the cocycle ball of `y`,
`g(z) = Φ₂_y(z) · g(y) · Φ₁_y(z)⁻¹` with `Φᵢ_y` radial transport out of `y`. -/
theorem flatGauge_local (hc : LocalCocycle.ConjMonodromy (flatCocycle hD h₁) (flatCocycle hD h₂) x₀ c)
    (y : D) {z : E} (hz : z ∈ ball y.1 (ballRadius hD y)) :
    flatGauge hD h₁ h₂ x₀ c z =
      radialTransport ω₂ y.1 z * flatGauge hD h₁ h₂ x₀ c y.1 *
        Ring.inverse (radialTransport ω₁ y.1 z) := by
  have hzD := ball_subset hD y hz
  have hm : ∀ t, segPath hD y z hz t ∈ (flatCocycle hD h₁).U y := segPath_mem hD y z hz
  have hm' : ∀ t, segPath hD y z hz t ∈ (flatCocycle hD h₂).U y := segPath_mem hD y z hz
  have hl := LocalCocycle.gauge_local hc (segPath hD y z hz) hm hm'
  have hy : y.1 ∈ ball y.1 (ballRadius hD y) := mem_ball_self (ballRadius_pos hD y)
  have u₁ := isUnit_radialTransport_of_convex (convex_ball y.1 _) (h₁.mono' (ball_subset hD y))
    hy hz
  have u₂ := isUnit_radialTransport_of_convex (convex_ball y.1 _) (h₂.mono' (ball_subset hD y))
    hy hz
  have := congrArg (fun u : Aˣᵐᵒᵖ => (u.unop : A)) hl
  simp only [MulOpposite.unop_mul, MulOpposite.unop_inv, Units.val_mul] at this
  rw [flatGauge_of_mem hzD, flatGauge_of_mem y.2, this, flatCocycle_P, flatCocycle_P,
    mul_assoc, ← Ring.inverse_unit]
  rw [radialUnit_val u₂, radialUnit_val u₁]

/-- **The gauge is differentiable** with `dg = ω₂ g − g ω₁`. -/
theorem hasFDerivAt_flatGauge
    (hc : LocalCocycle.ConjMonodromy (flatCocycle hD h₁) (flatCocycle hD h₂) x₀ c) (y : D) :
    HasFDerivAt (flatGauge hD h₁ h₂ x₀ c)
      ((ContinuousLinearMap.mul ℝ A).flip (flatGauge hD h₁ h₂ x₀ c y.1) ∘L ω₂ y.1 -
        (ContinuousLinearMap.mul ℝ A (flatGauge hD h₁ h₂ x₀ c y.1)) ∘L ω₁ y.1) y.1 := by
  set gy := flatGauge hD h₁ h₂ x₀ c y.1
  have hseg : ∀ t ∈ Icc (0:ℝ) 1, y.1 + t • (y.1 - y.1) ∈ D := fun _ _ => by simp [y.2]
  have d₁ := hasFDerivAt_radialTransport hD h₁ hseg
  have d₂ := hasFDerivAt_radialTransport hD h₂ hseg
  have hinv : HasFDerivAt (Ring.inverse : A → A)
      (-ContinuousLinearMap.mulLeftRight ℝ A 1 1) (radialTransport ω₁ y.1 y.1) := by
    rw [radialTransport_self_of_mem hD h₁ y]
    exact hasFDerivAt_ringInverse (𝕜 := ℝ) (1 : Aˣ) |>.congr_fderiv (by simp)
  have dinv := hinv.comp y.1 d₁
  have hprod := (d₂.mul_const' gy).mul' dinv
  have heq : (fun z => radialTransport ω₂ y.1 z * gy * Ring.inverse (radialTransport ω₁ y.1 z))
      =ᶠ[nhds y.1] flatGauge hD h₁ h₂ x₀ c := by
    filter_upwards [isOpen_ball.mem_nhds (mem_ball_self (ballRadius_pos hD y))] with z hz
    exact (flatGauge_local hc y hz).symm
  refine (hprod.congr_of_eventuallyEq heq.symm).congr_fderiv ?_
  ext v
  simp [radialTransport_self_of_mem hD h₁ y, radialTransport_self_of_mem hD h₂ y, gy]
  abel

end QOU.Mass.KZHolonomy
