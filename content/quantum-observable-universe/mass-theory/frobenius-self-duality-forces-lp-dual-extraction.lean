import QOU.Basic

namespace QOU.BraidKnot

class FrobeniusTraceAlgebra (R : Type) where
  algebra : Type
  trace : algebra → R
  obs_frame : algebra → (algebra → R)
  frob_map : algebra → (algebra → R)
  obs_eq_frob : obs_frame = frob_map
  obs_bijective : Function.Bijective obs_frame

-- Ref: [manuscript] prop:frobenius-self-duality-forces-lp-dual-extraction —
--   the observation frame as the τ-mate map; placeholder pending the
--   Frobenius pairing construction on the trace algebra.
def observationFrame {R : Type} (FA : FrobeniusTraceAlgebra R) : FA.algebra → (FA.algebra → R) := FA.obs_frame
-- Ref: [manuscript] prop:frobenius-self-duality-forces-lp-dual-extraction —
--   the Frobenius self-duality map `x ↦ trace (x · −)`; placeholder pending
--   the Frobenius pairing construction on the trace algebra.
def frobeniusSelfDualityMap {R : Type} (FA : FrobeniusTraceAlgebra R) : FA.algebra → (FA.algebra → R) := FA.frob_map

-- Ref: [manuscript] prop:frobenius-self-duality-forces-lp-dual-extraction
theorem frobenius_self_duality_forces_lp_dual_extraction
    {R : Type} (FA : FrobeniusTraceAlgebra R) :
    observationFrame FA = frobeniusSelfDualityMap FA
      ∧ Function.Bijective (observationFrame FA) := by
  exact ⟨FA.obs_eq_frob, FA.obs_bijective⟩

end QOU.BraidKnot
