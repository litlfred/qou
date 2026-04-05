import QOU.QuantumObservableUniverse

/-!
# §7  Mass Identity

The inertial mass of a stable vortex via nonabelian multiplicative
integration (Yekutieli): `m = ‖MI∫_Σ (∇_A q, L ∧ F⁺)‖`.
-/


namespace QOU.Torsion

/-! ## §7  Mass Identity -/

/-- **Mass Identity**: `m = ‖MI∫_Σ (∇_A q, L ∧ F⁺)‖ = ‖Hol_{∇_A}(γ; 𝔊)‖`.
    LaTeX: `\label{def:mass-identity}` -/
structure MassIdentity (M : Type*) where
  sp : SubstrateParameter M
  connectionGradient : M → ℝ
  leviCurvatureCoupling : M → ℝ
  vortexCycle : Set M
  cycle_nonempty : vortexCycle.Nonempty
  integrand_nonneg : ∀ (p : M), p ∈ vortexCycle →
    0 ≤ connectionGradient p * leviCurvatureCoupling p

/-- **Corollary (ℂ mass identity).**
    LaTeX: `\label{cor:mass-identity-C}` -/
structure MassIdentityC (M : Type*) extends MassIdentity M where
  cqou : CQuantumObservableUniverse
  base_eq : cqou.M = M
  cycle_dim : ℕ := 2
  cr_compatible : cycle_dim ≤ 2 * cqou.n := by omega
  mass_nonneg : ∀ (p : M), p ∈ vortexCycle →
    0 ≤ connectionGradient p * leviCurvatureCoupling p :=
    integrand_nonneg

end QOU.Torsion
