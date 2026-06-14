import QOU.Basic

namespace QOU.BraidKnot

class FrobeniusTraceAlgebra (R : Type) where
  algebra : Type
  trace : algebra → R

def observationFrame {R : Type} (FA : FrobeniusTraceAlgebra R) : FA.algebra → (FA.algebra → R) := sorry
def frobeniusSelfDualityMap {R : Type} (FA : FrobeniusTraceAlgebra R) : FA.algebra → (FA.algebra → R) := sorry

-- Ref: [manuscript] prop:frobenius-self-duality-forces-lp-dual-extraction
theorem frobenius_self_duality_forces_lp_dual_extraction
    {R : Type} (FA : FrobeniusTraceAlgebra R) :
    observationFrame FA = frobeniusSelfDualityMap FA
      ∧ Function.Bijective (observationFrame FA) := by
  sorry

end QOU.BraidKnot
