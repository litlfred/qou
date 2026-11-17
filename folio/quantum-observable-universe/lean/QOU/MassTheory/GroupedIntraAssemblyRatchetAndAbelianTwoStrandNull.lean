/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Grouped Intra-Nucleon Word Assembly Ratchet and Abelian Two-Strand Commutator Null

Formalizes two linked structural diagnostics in the nuclear braid pipeline:

1. **Hand-Assembled Grouped Intra-Nucleon Word Ratchet and Multiset Ratio Invariance (`qou-t29k`)**:
   - The structural audit ratchet tracks $18$ initial hand-assembled grouped intra-nucleon
     word sites ($11$ concatenation sites + $7$ sequential-loop sites), draining $15$
     actionable sites down to $3$ blocked sites ($2$ escalated owner calls + $1$ paused module).
   - For two nucleon arrangements with the same proton/neutron multiset, scaling both
     absolute traces by a common per-nucleon intra-ordering factor $f > 0$ preserves their
     cross-multiplied ratio identity $(f \cdot \text{tr}_A) \cdot \text{tr}_B =
     (f \cdot \text{tr}_B) \cdot \text{tr}_A$ while shifting the absolute trace whenever $f > 1$.

2. **Abelian Two-Strand Commutator Vanishing vs Weighted Non-Abelian Block Charge (`qou-u8w5`)**:
   - In any commutative two-strand algebra ($ab = ba$), every commutator $ab - ba = 0$
     vanishes identically, so the two-strand scalar handle-commutator channel is zero
     and cannot supply the deuteron target $58528 \times 10^{-4}$.
   - On the non-abelian six-strand interface braid where two opposite-chirality block
     charges satisfy $c_1 + c_2 = 0$ ($c_2 = -c_1$) with $c_1 > 0$, the unweighted sum
     vanishes ($c_1 + c_2 = 0$) whereas the eigenphase-weighted block sum
     $w_1 c_1 + w_2 c_2 = (w_1 - w_2) c_1$ is strictly positive whenever $w_2 < w_1$.
-/

namespace QOU.MassTheory.GroupedIntraAssemblyRatchetAndAbelianTwoStrandNull

/-- Initial hand-assembled grouped word site count (`concatSites + loopSites`). -/
def initialGroupedAssemblySites (concatSites loopSites : Int) : Int :=
  concatSites + loopSites

/-- Remaining hand-assembled grouped word sites after draining `drainedSites`. -/
def remainingGroupedAssemblySites (initialSites drainedSites : Int) : Int :=
  initialSites - drainedSites

/-- Intra-ordering scaled absolute trace $f \cdot \text{tr}$. -/
def scaledAbsoluteTrace (intraFactor baseTrace : Int) : Int :=
  intraFactor * baseTrace

/-- Commutator $ab - ba$ of two products $ab$ and $ba$. -/
def commutatorDiff (ab ba : Int) : Int :=
  ab - ba

/-- Two-block eigenphase-weighted commutator charge $w_1 c_1 + w_2 c_2$. -/
def weightedTwoBlockCharge (w1 w2 c1 c2 : Int) : Int :=
  w1 * c1 + w2 * c2

/-- Ratchet drain from $11 + 7 = 18$ sites to $3$ remaining sites and exact cross-ratio
    invariance under a common multiset intra-ordering factor (`qou-t29k`). -/
theorem grouped_intra_assembly_ratchet_drain_and_multiset_ratio_invariance
    (intraFactor trA trB : Int) (hf : 1 < intraFactor) (ha : 0 < trA) :
    initialGroupedAssemblySites 11 7 = 18 ∧
      remainingGroupedAssemblySites (initialGroupedAssemblySites 11 7) 15 = 3 ∧
      trA < scaledAbsoluteTrace intraFactor trA ∧
      scaledAbsoluteTrace intraFactor trA * trB =
        scaledAbsoluteTrace intraFactor trB * trA := by
  dsimp [initialGroupedAssemblySites, remainingGroupedAssemblySites, scaledAbsoluteTrace]
  have hlt : trA < intraFactor * trA := by
    have hsub : 1 * trA < intraFactor * trA :=
      Int.mul_lt_mul_of_pos_right hf ha
    omega
  have hmul : intraFactor * trA * trB = intraFactor * trB * trA := by
    rw [Int.mul_assoc, Int.mul_comm trA trB, ← Int.mul_assoc]
  exact ⟨rfl, rfl, hlt, hmul⟩

/-- Commutative two-strand commutator vanishing versus strictly positive eigenphase-weighted
    non-abelian block charge when $c_2 = -c_1$, $c_1 > 0$, and $w_2 < w_1$ (`qou-u8w5`). -/
theorem abelian_two_strand_commutator_vanishes_vs_weighted_block_charge
    (ab ba w1 w2 c1 c2 : Int)
    (hComm : ab = ba) (hZeroSum : c2 = -c1)
    (hc1 : 0 < c1) (hw : w2 < w1) :
    commutatorDiff ab ba = 0 ∧
      commutatorDiff ab ba ≠ 58528 ∧
      c1 + c2 = 0 ∧
      weightedTwoBlockCharge w1 w2 c1 c2 = (w1 - w2) * c1 ∧
      0 < weightedTwoBlockCharge w1 w2 c1 c2 := by
  dsimp [commutatorDiff, weightedTwoBlockCharge]
  have h0 : ab - ba = 0 := by omega
  have hne : ab - ba ≠ 58528 := by omega
  have hcsum : c1 + c2 = 0 := by omega
  have hfactor : w1 * c1 + w2 * c2 = (w1 - w2) * c1 := by
    rw [hZeroSum, Int.mul_neg, Int.sub_mul]
    omega
  have hpos : 0 < w1 * c1 + w2 * c2 := by
    rw [hfactor]
    have hwpos : 0 < w1 - w2 := by omega
    exact Int.mul_pos hwpos hc1
  exact ⟨h0, hne, hcsum, hfactor, hpos⟩

end QOU.MassTheory.GroupedIntraAssemblyRatchetAndAbelianTwoStrandNull
