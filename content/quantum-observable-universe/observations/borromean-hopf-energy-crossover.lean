import Mathlib.Data.Real.Basic

/-!
# QOU.Archimedean.borromean_hopf_energy_crossover
-/

namespace QOU.Archimedean

class EnergyFunctional (E : Type*)
class CrossoverDynamics {E : Type*} [EnergyFunctional E] where
  borromean_energy : ℝ → E
  hopf_energy : ℝ → E

/-- **PROPOSITION.** Energy crossover between Borromean and Hopf-diquark phases.
    There exists a critical density where the Borromean binding energy is superseded
    by the Hopf-diquark condensate energy. -/
theorem borromean_hopf_energy_crossover
    {E : Type*} [EnergyFunctional E] [dyn : CrossoverDynamics E] :
    ∃ (rho_c : ℝ), rho_c > 0 ∧
      ∀ rho > rho_c, dyn.hopf_energy rho < dyn.borromean_energy rho := by
  -- Ref: [manuscript] prop:borromean-hopf-energy-crossover
  sorry

end QOU.Archimedean
