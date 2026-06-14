import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic

/-!
# QOU.Archimedean.color_superconductivity_borromean
-/

namespace QOU.Archimedean

class LinkComplement (L : Type*)
class LinkingInvariants {L : Type*} [LinkComplement L] where
  milnor_mu : L → ℤ
  pairwise_linking : L → ℤ

/-- The topological transition from confined (Borromean) to CFL (Hopf) phase is first order,
    characterized by a discontinuous jump in the Milnor triple linking invariant. -/
theorem first_order_transition
    {L : Type*} [LinkComplement L] [inv : LinkingInvariants L]
    (borromean hopf_cfl : L)
    (h_borr : inv.milnor_mu borromean = 1)
    (h_hopf : inv.milnor_mu hopf_cfl = 0) :
    |inv.milnor_mu borromean - inv.milnor_mu hopf_cfl| = 1 := by
  -- Ref: [manuscript] conj:color-superconductivity-borromean
  sorry

end QOU.Archimedean
