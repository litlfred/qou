import QOU.Mass.KZHolonomy.ODETransport

/-!
# Smooth Riemann–Hilbert uniqueness from conjugate monodromy on generators

Let `ω₁, ω₂` be flat connection forms on an open path-connected set `D ⊆ E`, and let
`γ_j` (`j ∈ J`) be `C¹` loops in `D` at a base point `x₀`, with ODE transports
`U¹_j, U²_j` (`U' = ωᵢ(γ_j)(γ_j') U`, `U 0 = 1`).  Suppose

* the classes of the `γ_j` generate `π₁(D, x₀)`, and
* a unit `c` intertwines the monodromies on the generators: `U²_j(1) · c = c · U¹_j(1)`.

Then there is a differentiable `g : E → A`, a unit at every point of `D`, with `g x₀ = c` and

    dg = ω₂ g − g ω₁      on D               (`flat_gauge_of_generators`).

All three inputs are stated as hypotheses about the given data; nothing about the topology of
`D` beyond openness and path-connectedness is assumed.  For the KZ application, `D` is a
configuration space and the generation hypothesis is the classical presentation of its
fundamental group (Artin's pure braid generators), which is not proved here.
-/

set_option autoImplicit false
set_option linter.unusedSectionVars false

namespace QOU.Mass.KZHolonomy

open Set Metric QOU.MathlibExt

variable {E A : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedRing A] [NormedAlgebra ℝ A] [CompleteSpace A]

/-- A path in the subtype `D` from a map `γ : ℝ → E`, continuous on `[0,1]` with values in `D`. -/
def pathOfMap {D : Set E} (γ : ℝ → E) (hc : ContinuousOn γ (Icc 0 1))
    (hD : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ D) {a b : D} (h0 : γ 0 = a) (h1 : γ 1 = b) : Path a b where
  toFun t := ⟨γ t, hD t t.2⟩
  continuous_toFun := (hc.comp_continuous continuous_subtype_val fun t => t.2).subtype_mk _
  source' := Subtype.ext h0
  target' := Subtype.ext h1

variable {ω₁ ω₂ : E → E →L[ℝ] A} {ω₁' ω₂' : E → E →L[ℝ] E →L[ℝ] A} {D : Set E}

/-- **Smooth gauge from conjugacy on generating loops.** -/
theorem flat_gauge_of_generators (hD : IsOpen D) (h₁ : IsFlatOn ω₁ ω₁' D)
    (h₂ : IsFlatOn ω₂ ω₂' D) [PathConnectedSpace D] (x₀ : D) {J : Type*}
    (γ γ' : J → ℝ → E) (hγd : ∀ j, ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt (γ j) (γ' j t) (Icc 0 1) t)
    (hγ'c : ∀ j, ContinuousOn (γ' j) (Icc 0 1)) (hγD : ∀ j, ∀ t ∈ Icc (0:ℝ) 1, γ j t ∈ D)
    (hγ0 : ∀ j, γ j 0 = x₀) (hγ1 : ∀ j, γ j 1 = x₀)
    (hgen : Subgroup.closure (range fun j => (CategoryTheory.Groupoid.isoEquivHom _ _).symm
      (Quotient.mk _ (pathOfMap (γ j) (fun t ht => (hγd j t ht).continuousWithinAt) (hγD j)
        (hγ0 j) (hγ1 j))) : Set (FundamentalGroup D x₀)) = ⊤)
    (U₁ U₂ : J → ℝ → A) (hU₁ : ∀ j, IsTransport ω₁ (γ j) (γ' j) (U₁ j))
    (hU₂ : ∀ j, IsTransport ω₂ (γ j) (γ' j) (U₂ j)) (c : Aˣ)
    (hc : ∀ j, U₂ j 1 * c = c * U₁ j 1) :
    ∃ g : E → A, g x₀ = c ∧ (∀ z ∈ D, IsUnit (g z)) ∧ ∀ y ∈ D,
      HasFDerivAt g ((ContinuousLinearMap.mul ℝ A).flip (g y) ∘L ω₂ y -
        (ContinuousLinearMap.mul ℝ A (g y)) ∘L ω₁ y) y := by
  set c' : Aˣᵐᵒᵖ := MulOpposite.op c
  have hconj : LocalCocycle.ConjMonodromy (flatCocycle hD h₁) (flatCocycle hD h₂) x₀ c' := by
    refine LocalCocycle.conjMonodromy_of_closure _ ?_ hgen
    rintro _ ⟨j, rfl⟩
    simp only [CategoryTheory.Groupoid.isoEquivHom_symm_apply_hom, LocalCocycle.transportQ_mk]
    set p := pathOfMap (γ j) (fun t ht => (hγd j t ht).continuousWithinAt) (hγD j) (hγ0 j)
      (hγ1 j)
    have e₁ := transport_flatCocycle_eq hD h₁ (hγd j) (hγ'c j) (hU₁ j) p fun _ => rfl
    have e₂ := transport_flatCocycle_eq hD h₂ (hγd j) (hγ'c j) (hU₂ j) p fun _ => rfl
    apply MulOpposite.unop_injective; apply Units.ext
    simp only [MulOpposite.unop_mul, MulOpposite.unop_inv, Units.val_mul, c',
      MulOpposite.unop_op]
    rw [e₂, ← mul_assoc, hc j, mul_assoc, ← e₁, ← Units.val_mul, mul_inv_cancel,
      Units.val_one, mul_one]
  refine ⟨flatGauge hD h₁ h₂ x₀ c', ?_, fun z hz => isUnit_flatGauge hz,
    fun y hy => hasFDerivAt_flatGauge hconj ⟨y, hy⟩⟩
  rw [flatGauge_of_mem x₀.2, LocalCocycle.gauge_eq_along hconj (Path.refl x₀)]
  simp [LocalCocycle.gaugeAlong, LocalCocycle.transport_refl, c']

end QOU.Mass.KZHolonomy
