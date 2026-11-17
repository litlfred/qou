/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Jet Sign-Gate Zero-Caller Isolation and Constant Inter-Nucleon Volume Offset

Formalizes two linked structural diagnostics in the nuclear mass and binding pipeline:

1. **Legacy Jet Sign Gate and Zero-Caller Isolation (`qou-px38`)**:
   - The exploratory routine `unified_iterative_correction_jet` applies the disproved
     complementary-slackness sign gate (`tr_sign <= 0`) to both its linear cumulant
     contributions and its conjugate-pair cross terms, annihilating positive-trace
     sectors (`0 < trSign1`, `0 < trSign2`).
   - Because `unified_iterative_correction_jet` has `callerCount = 0` across the entire
     production codebase, any per-call shift in that routine produces zero shift
     in published outputs ($\text{publishedOutputShiftFromUnusedRoutine}(0, \Delta) = 0$).

2. **Constant $-7.92 \times 10^{-4}\text{ MeV}$ Inter-Nucleon Volume Offset (`qou-q3f7`)**:
   - In `mass-table-comprehensive`, the binding proxy is $B_{\text{qCLT}} = -\alpha \sum \ln V$
     and the approximate mass is $m_{\text{approx}} = m_{\text{unbound}} - B_{\text{qCLT}}$.
   - Adding an $A$-independent shift $\Delta S$ (from the once-per-atom inter-nucleon
     proton-neutron volume factor) to $\sum \ln V$ shifts $B_{\text{qCLT}}$ by the exact
     constant $-\alpha \Delta S$ and shifts $m_{\text{approx}}$ by the exact opposite
     constant $+\alpha \Delta S$ on every isotope row, matching the measured
     $-792 \times 10^{-6}\text{ MeV}$ shift across $A = 2, 3, 37, 38, 39, 40$.
-/

namespace QOU.MassTheory.JetSignGateZeroCallersAndConstantInterVolumeOffset

/-- Legacy jet sign gate on linear cumulant terms (`trSign <= 0`). -/
def jetSignGateLinear (trSign cumul : Int) : Int :=
  if trSign ≤ 0 then cumul else 0

/-- Legacy jet sign gate on conjugate-pair cross terms (`trSign1 <= 0` or `trSign2 <= 0`). -/
def jetSignGatePairSum (trSign1 trSign2 pairCoupling : Int) : Int :=
  if trSign1 ≤ 0 ∨ trSign2 ≤ 0 then pairCoupling else 0

/-- Total shift in published outputs from a routine called `callerCount` times. -/
def publishedOutputShiftFromUnusedRoutine (callerCount perCallShift : Int) : Int :=
  callerCount * perCallShift

/-- Binding proxy $B_{\text{qCLT}} = -\alpha \sum \ln V$. -/
def bQcltFromLogVolumeSum (alpha sumLogV : Int) : Int :=
  -(alpha * sumLogV)

/-- Approximate mass $m_{\text{approx}} = m_{\text{unbound}} - B_{\text{qCLT}}$. -/
def mApproxFromBinding (mUnbound bQclt : Int) : Int :=
  mUnbound - bQclt

/-- Positive-trace annihilation by the legacy jet sign gate and zero published impact
    at zero callers (`qou-px38`): when $0 < \text{trSign}_1$ and $0 < \text{trSign}_2$,
    both the linear and pair-sum gated terms vanish, while `callerCount = 0` yields zero
    published shift. -/
theorem jetSignGate_annihilates_positive_trace_and_zero_callers_isolated
    (trSign1 trSign2 cumul pairCoupling perCallShift : Int)
    (h1 : 0 < trSign1) (h2 : 0 < trSign2)
    (hc : 0 < cumul) (hp : 0 < pairCoupling) :
    jetSignGateLinear trSign1 cumul = 0 ∧
      jetSignGatePairSum trSign1 trSign2 pairCoupling = 0 ∧
      0 < cumul - jetSignGateLinear trSign1 cumul ∧
      0 < pairCoupling - jetSignGatePairSum trSign1 trSign2 pairCoupling ∧
      publishedOutputShiftFromUnusedRoutine 0 perCallShift = 0 := by
  dsimp [jetSignGateLinear, jetSignGatePairSum, publishedOutputShiftFromUnusedRoutine]
  have hn1 : ¬ (trSign1 ≤ 0) := by omega
  have hn12 : ¬ (trSign1 ≤ 0 ∨ trSign2 ≤ 0) := by omega
  have hg1 : (if trSign1 ≤ 0 then cumul else 0) = 0 := if_neg hn1
  have hg2 : (if trSign1 ≤ 0 ∨ trSign2 ≤ 0 then pairCoupling else 0) = 0 := if_neg hn12
  have hz : 0 * perCallShift = 0 := Int.zero_mul perCallShift
  refine ⟨hg1, hg2, ?_, ?_, hz⟩
  · rw [hg1]
    omega
  · rw [hg2]
    omega

/-- Constant inter-nucleon log-volume shift produces an $A$-independent offset in
    $B_{\text{qCLT}}$ and an equal-and-opposite offset in $m_{\text{approx}}$ (`qou-q3f7`). -/
theorem constant_log_volume_shift_produces_A_independent_binding_and_mass_offset
    (alpha sumLogV deltaS mUnbound : Int) :
    bQcltFromLogVolumeSum alpha (sumLogV + deltaS) -
        bQcltFromLogVolumeSum alpha sumLogV = -(alpha * deltaS) ∧
      mApproxFromBinding mUnbound (bQcltFromLogVolumeSum alpha (sumLogV + deltaS)) -
        mApproxFromBinding mUnbound (bQcltFromLogVolumeSum alpha sumLogV) =
        alpha * deltaS := by
  dsimp [bQcltFromLogVolumeSum, mApproxFromBinding]
  have hd : alpha * (sumLogV + deltaS) = alpha * sumLogV + alpha * deltaS :=
    Int.mul_add alpha sumLogV deltaS
  rw [hd]
  refine ⟨by omega, by omega⟩

/-- Exact $-792 \times 10^{-6}\text{ MeV}$ constant offset across $A = 2, 3, 37, 40$ (`qou-q3f7`). -/
theorem mass_table_comprehensive_constant_792_microMeV_offset
    (dOld dNew tOld tNew cl37Old cl37New cl40Old cl40New : Int)
    (hdO : dOld = 4401529) (hdN : dNew = 4400737)
    (htO : tOld = 10263414) (htN : tNew = 10262622)
    (h37O : cl37Old = 162993882) (h37N : cl37New = 162993090)
    (h40O : cl40Old = 180579537) (h40N : cl40New = 180578745) :
    dNew - dOld = -792 ∧
      tNew - tOld = -792 ∧
      cl37New - cl37Old = -792 ∧
      cl40New - cl40Old = -792 := by
  have h1 : dNew - dOld = -792 := by omega
  have h2 : tNew - tOld = -792 := by omega
  have h3 : cl37New - cl37Old = -792 := by omega
  have h4 : cl40New - cl40Old = -792 := by omega
  exact ⟨h1, h2, h3, h4⟩

end QOU.MassTheory.JetSignGateZeroCallersAndConstantInterVolumeOffset
