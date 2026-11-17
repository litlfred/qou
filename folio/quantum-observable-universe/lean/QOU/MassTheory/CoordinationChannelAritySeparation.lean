/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# Coordination Saturation Premise Separation Between Free-Energy and Observe-Early Channels (`qou-x0su`)

This module formalizes the structural separation between the two binding channels in bean `qou-x0su`:

1. **Channel 1 (Additive free-energy `−log(∏ f_i) = ε · M`):**
   - The bond count `M` enters linearly. Comparing the complete graph (`2 M_K = A(A - 1)`) against
     the 1-D chain (`2 M_C = 2(A - 1)`), their difference factors as
     `A(A - 1) - 2(A - 1) = (A - 1)(A - 2)`, which is strictly positive for all `A ≥ 3` and grows
     quadratically in `A`.
2. **Channel 2 (Observe-early multiplicative difference `Q_β · |tr_free| · (1 − ∏ f_i)`):**
   - For any rational bond factor `f / D ∈ (0, 1)` (`0 < f < D`), the cleared factor `D^M - f^M`
     satisfies `0 < D^M - f^M < D^M` for every `M ≥ 1` (since `0 < f^M < D^M`).
   - Moreover, the cleared discrepancy between the complete-graph and chain multiplicative factors
     `D^{M_K}`-scaled equals `f^{M_C} (D^{M_K - M_C} - f^{M_K - M_C})`, which is suppressed by the
     exponentially decaying prefactor `f^{M_C}`.
-/

namespace QOU.MassTheory.CoordinationChannelAritySeparation

/-- Doubled bond count `2(A - 1)` of the 1-D chain on `A` nucleons (`qou-x0su`). -/
def chainBondCountDoubled (A : Int) : Int :=
  2 * (A - 1)

/-- Doubled bond count `A(A - 1)` of the complete graph `K_A` on `A` nucleons (`qou-x0su`). -/
def completeGraphBondCountDoubled (A : Int) : Int :=
  A * (A - 1)

/-- The excess of complete-graph over chain bond counts (doubled) factors as `(A - 1)(A - 2)` (`qou-x0su`). -/
theorem completeMinusChainBondCountDoubled_factor (A : Int) :
    completeGraphBondCountDoubled A - chainBondCountDoubled A = (A - 1) * (A - 2) := by
  unfold completeGraphBondCountDoubled chainBondCountDoubled
  have hd : (A - 1) * (A - 2) = A * (A - 1) - 2 * (A - 1) := by
    rw [Int.mul_comm (A - 1) (A - 2), Int.sub_mul A 2 (A - 1)]
  omega

/-- For `A ≥ 3`, the complete-graph bond count strictly exceeds the chain bond count (`qou-x0su`). -/
theorem completeBondCount_gt_chainBondCount_of_ge_three (A : Int) (hA : 3 ≤ A) :
    chainBondCountDoubled A < completeGraphBondCountDoubled A := by
  have hfac := completeMinusChainBondCountDoubled_factor A
  have hpos : 0 < (A - 1) * (A - 2) := by
    have h1 : 0 < A - 1 := by omega
    have h2 : 0 < A - 2 := by omega
    exact Int.mul_pos h1 h2
  omega

/-- Cleared observe-early factor `D_pow - f_pow` representing `D^M (1 - (f/D)^M)` (`qou-x0su`). -/
def observeEarlyClearedFactor (D_pow f_pow : Int) : Int :=
  D_pow - f_pow

/-- Whenever `0 < f_pow < D_pow` (i.e. `(f/D)^M ∈ (0, 1)`), the observe-early factor lies strictly
inside `(0, D_pow)` regardless of the bond count `M` (`qou-x0su`). -/
theorem observeEarlyClearedFactor_bounded (D_pow f_pow : Int)
    (hf_pos : 0 < f_pow) (hf_lt : f_pow < D_pow) :
    0 < observeEarlyClearedFactor D_pow f_pow ∧
    observeEarlyClearedFactor D_pow f_pow < D_pow := by
  dsimp [observeEarlyClearedFactor]
  constructor <;> omega

/-- Cleared discrepancy between complete-graph and chain observe-early factors (`qou-x0su`). -/
def observeEarlyCompleteMinusChainCleared (D_pow_delta f_pow_chain f_pow_delta : Int) : Int :=
  f_pow_chain * (D_pow_delta - f_pow_delta)

/-- Exact factorization of the difference between complete-graph `(D^{M_C + ΔM} - f^{M_C + ΔM})`
and `D^{ΔM}`-scaled chain `(D^{M_C} - f^{M_C})` (`qou-x0su`). -/
theorem observeEarlyCompleteMinusChain_factor
    (D_pow_chain D_pow_delta f_pow_chain f_pow_delta : Int) :
    observeEarlyClearedFactor (D_pow_chain * D_pow_delta) (f_pow_chain * f_pow_delta) -
      D_pow_delta * observeEarlyClearedFactor D_pow_chain f_pow_chain =
    observeEarlyCompleteMinusChainCleared D_pow_delta f_pow_chain f_pow_delta := by
  unfold observeEarlyClearedFactor observeEarlyCompleteMinusChainCleared
  have h1 : D_pow_delta * (D_pow_chain - f_pow_chain) =
      D_pow_chain * D_pow_delta - f_pow_chain * D_pow_delta := by
    rw [Int.mul_sub, Int.mul_comm D_pow_delta D_pow_chain, Int.mul_comm D_pow_delta f_pow_chain]
  have h2 : f_pow_chain * (D_pow_delta - f_pow_delta) =
      f_pow_chain * D_pow_delta - f_pow_chain * f_pow_delta :=
    Int.mul_sub f_pow_chain D_pow_delta f_pow_delta
  omega

end QOU.MassTheory.CoordinationChannelAritySeparation
