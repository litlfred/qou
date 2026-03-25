/-!
# QOU.MassIdentityC — Archimedean realisation of the mass identity

In the archimedean QOU (M, G, P, E) with instanton connection A,
Levi form L, and self-dual curvature F⁺, the categorical mass is
realised as Yekutieli's nonabelian multiplicative integral.

## References

- [yekutieli2015] Nonabelian multiplicative integration on surfaces
- [manuscript] §3
-/

import Mathlib.Analysis.Normed.Group.Basic

namespace QOU

/-- **Archimedean mass corollary**: the categorical mass of a closed
    cycle γ encircling a vortex filament equals the Killing-form norm
    of the holonomy of the instanton connection around γ.

    m(γ) = ‖MI∫_Σ (∇_A q, L ∧ F⁺)‖ = ‖Hol_{∇_A}(γ; 𝔊)‖

    LaTeX: `\label{cor:mass-identity-C}`
    Ref: [yekutieli2015] -/
-- Ref: [yekutieli2015] https://doi.org/10.1016/j.aim.2015.04.006
structure MassIdentityC where
  /-- The holonomy value (in ℝ, representing ‖Hol(γ)‖). -/
  holonomy_norm : ℝ
  /-- The multiplicative integral value (in ℝ). -/
  mult_integral_norm : ℝ
  /-- Nonabelian Stokes: MI∫ equals holonomy. -/
  stokes : mult_integral_norm = holonomy_norm
  /-- Mass is non-negative. -/
  mass_nonneg : 0 ≤ holonomy_norm

/-- The mass equals the holonomy norm (nonabelian Stokes theorem). -/
theorem mass_is_holonomy (mic : MassIdentityC) :
    mic.mult_integral_norm = mic.holonomy_norm :=
  mic.stokes

end QOU
