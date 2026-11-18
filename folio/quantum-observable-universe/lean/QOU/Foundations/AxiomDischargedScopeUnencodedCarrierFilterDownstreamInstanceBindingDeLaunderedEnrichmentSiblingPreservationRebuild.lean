/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Formalization of:
- qou-58rx: Axiom-discharged conjecture scope partition and consumer-bound residual accounting
- qou-hprp: Unencoded `holds : Prop` conjecture-carrier census and comment-stripped filter
- qou-y3x4: Downstream instance-hypothesis audit for `conditional_on_class` blocks (§3b-cond rule 2)
- qou-yl86: Context-enrichment de-laundering campaign partition and anti-reassumption guard
- qou-zatj: Pre-existing sorry-free sibling preservation and batch-rebuild partition
-/

namespace QOU.Foundations.AxiomDischargedScopeUnencodedCarrierFilterDownstreamInstanceBindingDeLaunderedEnrichmentSiblingPreservationRebuild

/-- Auxiliary lemma: the square of any integer is non-negative (`qou-58rx`). -/
theorem int_mul_self_nonneg (a : Int) : 0 ≤ a * a := by
  rcases Int.le_total 0 a with h | h
  · exact Int.mul_nonneg h h
  · have hneg : 0 ≤ -a := by omega
    have hmul : 0 ≤ (-a) * (-a) := Int.mul_nonneg hneg hneg
    rw [Int.neg_mul_neg] at hmul
    exact hmul

/-- Auxiliary lemma: sum of two integer squares vanishes iff both terms vanish (`qou-58rx`). -/
theorem int_sq_add_sq_eq_zero_iff (a b : Int) :
    a * a + b * b = 0 ↔ a = 0 ∧ b = 0 := by
  constructor
  · intro h
    have ha : 0 ≤ a * a := int_mul_self_nonneg a
    have hb : 0 ≤ b * b := int_mul_self_nonneg b
    have ha0 : a * a = 0 := by omega
    have hb0 : b * b = 0 := by omega
    exact ⟨Int.mul_eq_zero.mp ha0 |>.elim id id, Int.mul_eq_zero.mp hb0 |>.elim id id⟩
  · rintro ⟨rfl, rfl⟩
    rfl

/-!
## 1. Axiom-Discharged Conjecture Scope Partition (`qou-58rx`)
-/

/-- Partition ledger for the 35 files carrying axiom-discharged conjectures or standalone axioms (`qou-58rx`). -/
structure AxiomDischargedScopeData where
  totalScopedFiles : Int
  firstPassFixedFiles : Int
  zeroConsumerFixedFiles : Int
  consumerBoundRemainingFiles : Int
  standaloneAxiomRemainingFiles : Int
  deriving DecidableEq, Repr

/-- Total de-laundered file count `firstPassFixedFiles + zeroConsumerFixedFiles` (`qou-58rx`). -/
def deLaunderedFixedTotal (d : AxiomDischargedScopeData) : Int :=
  d.firstPassFixedFiles + d.zeroConsumerFixedFiles

/-- Remaining unfixed file count `consumerBoundRemainingFiles + standaloneAxiomRemainingFiles` (`qou-58rx`). -/
def remainingAxiomDischargedTotal (d : AxiomDischargedScopeData) : Int :=
  d.consumerBoundRemainingFiles + d.standaloneAxiomRemainingFiles

/-- Quadratic scope-completion deficit `(totalScopedFiles - deLaunderedFixedTotal)^2` (`qou-58rx`). -/
def axiomScopeDeficitSq (d : AxiomDischargedScopeData) : Int :=
  (d.totalScopedFiles - deLaunderedFixedTotal d) *
    (d.totalScopedFiles - deLaunderedFixedTotal d)

/-- Canonical 35-file corrected scope witness (`9 + 9 = 18` fixed, `8 + 9 = 17` remaining) (`qou-58rx`). -/
def canonicalAxiomDischargedScope : AxiomDischargedScopeData :=
  { totalScopedFiles := 35
    firstPassFixedFiles := 9
    zeroConsumerFixedFiles := 9
    consumerBoundRemainingFiles := 8
    standaloneAxiomRemainingFiles := 9 }

/-- The scope-completion deficit square vanishes iff all scoped files are de-laundered (`qou-58rx`). -/
theorem axiomScopeDeficitSq_eq_zero_iff (d : AxiomDischargedScopeData) :
    axiomScopeDeficitSq d = 0 ↔
      deLaunderedFixedTotal d = d.totalScopedFiles := by
  unfold axiomScopeDeficitSq
  rw [Int.mul_eq_zero]
  omega

/-- Under the 4-bucket partition, the complement `totalScopedFiles - deLaunderedFixedTotal` equals `remainingAxiomDischargedTotal` (`qou-58rx`). -/
theorem total_sub_fixed_eq_remaining
    (d : AxiomDischargedScopeData)
    (hPart : deLaunderedFixedTotal d + remainingAxiomDischargedTotal d = d.totalScopedFiles) :
    d.totalScopedFiles - deLaunderedFixedTotal d =
      remainingAxiomDischargedTotal d := by
  have hFixed : deLaunderedFixedTotal d =
      d.firstPassFixedFiles + d.zeroConsumerFixedFiles := rfl
  rw [hFixed] at hPart ⊢
  omega

/-- Evaluation of the canonical 35-file (`18` fixed, `17` remaining) scope witness (`qou-58rx`). -/
theorem canonicalAxiomDischargedScope_eval :
    deLaunderedFixedTotal canonicalAxiomDischargedScope = 18 ∧
      remainingAxiomDischargedTotal canonicalAxiomDischargedScope = 17 ∧
      axiomScopeDeficitSq canonicalAxiomDischargedScope = 289 := by
  decide

/-!
## 2. Unencoded `holds : Prop` Conjecture-Carrier Filter (`qou-hprp`)
-/

/-- Comment-stripping filter ledger separating live `holds : Prop` carriers from docstring false positives (`qou-hprp`). -/
structure UnencodedCarrierFilterData where
  naiveGrepMatches : Int
  liveCodeCarriers : Int
  proseCommentFalsePositives : Int
  deriving DecidableEq, Repr

/-- Quadratic filter consistency and live-carrier penalty (`qou-hprp`). -/
def unencodedCarrierAuditSq (d : UnencodedCarrierFilterData) : Int :=
  (d.naiveGrepMatches - d.liveCodeCarriers - d.proseCommentFalsePositives) *
    (d.naiveGrepMatches - d.liveCodeCarriers - d.proseCommentFalsePositives) +
    d.liveCodeCarriers * d.liveCodeCarriers

/-- Canonical 38-match census (`23` live carriers, `15` prose false positives) (`qou-hprp`). -/
def canonicalUnencodedCarrierFilter : UnencodedCarrierFilterData :=
  { naiveGrepMatches := 38
    liveCodeCarriers := 23
    proseCommentFalsePositives := 15 }

/-- The unencoded-carrier audit functional is non-negative (`qou-hprp`). -/
theorem unencodedCarrierAuditSq_nonneg (d : UnencodedCarrierFilterData) :
    0 ≤ unencodedCarrierAuditSq d := by
  unfold unencodedCarrierAuditSq
  have h1 : 0 ≤ (d.naiveGrepMatches - d.liveCodeCarriers - d.proseCommentFalsePositives) *
      (d.naiveGrepMatches - d.liveCodeCarriers - d.proseCommentFalsePositives) :=
    int_mul_self_nonneg (d.naiveGrepMatches - d.liveCodeCarriers - d.proseCommentFalsePositives)
  have h2 : 0 ≤ d.liveCodeCarriers * d.liveCodeCarriers :=
    int_mul_self_nonneg d.liveCodeCarriers
  omega

/-- The unencoded-carrier audit functional vanishes iff the partition balances and zero live `holds : Prop` carriers remain (`qou-hprp`). -/
theorem unencodedCarrierAuditSq_eq_zero_iff (d : UnencodedCarrierFilterData) :
    unencodedCarrierAuditSq d = 0 ↔
      d.liveCodeCarriers + d.proseCommentFalsePositives = d.naiveGrepMatches ∧
        d.liveCodeCarriers = 0 := by
  unfold unencodedCarrierAuditSq
  rw [int_sq_add_sq_eq_zero_iff]
  omega

/-- Evaluation of the canonical 38 / 23 / 15 unencoded carrier census (`qou-hprp`). -/
theorem canonicalUnencodedCarrierFilter_eval :
    canonicalUnencodedCarrierFilter.liveCodeCarriers +
        canonicalUnencodedCarrierFilter.proseCommentFalsePositives =
      canonicalUnencodedCarrierFilter.naiveGrepMatches ∧
      unencodedCarrierAuditSq canonicalUnencodedCarrierFilter = 529 := by
  decide

/-!
## 3. Downstream Instance-Hypothesis Binding Audit (`qou-y3x4`)
-/

/-- Partition of `conditional_on_class` blocks under §3b-cond rule 2 (`qou-y3x4`). -/
structure DownstreamInstanceBindingData where
  totalConditionalBlocks : Int
  ownConeClassBound : Int
  otherCarrierBound : Int
  noCarrierBound : Int
  unresolvedRefBlocks : Int
  deriving DecidableEq, Repr

/-- Total rule-2 non-compliant blocks `otherCarrierBound + noCarrierBound + unresolvedRefBlocks` (`qou-y3x4`). -/
def nonCompliantInstanceBindingCount (d : DownstreamInstanceBindingData) : Int :=
  d.otherCarrierBound + d.noCarrierBound + d.unresolvedRefBlocks

/-- Quadratic rule-2 compliance gap `(totalConditionalBlocks - ownConeClassBound)^2` (`qou-y3x4`). -/
def ruleTwoComplianceGapSq (d : DownstreamInstanceBindingData) : Int :=
  (d.totalConditionalBlocks - d.ownConeClassBound) *
    (d.totalConditionalBlocks - d.ownConeClassBound)

/-- Canonical 139-block §3b-cond rule 2 measurement (`9` own-cone, `72` other, `45` none, `13` unresolved) (`qou-y3x4`). -/
def canonicalDownstreamInstanceBinding : DownstreamInstanceBindingData :=
  { totalConditionalBlocks := 139
    ownConeClassBound := 9
    otherCarrierBound := 72
    noCarrierBound := 45
    unresolvedRefBlocks := 13 }

/-- The rule-2 compliance gap vanishes iff every conditional block binds a class from its own conjecture cone (`qou-y3x4`). -/
theorem ruleTwoComplianceGapSq_eq_zero_iff (d : DownstreamInstanceBindingData) :
    ruleTwoComplianceGapSq d = 0 ↔
      d.ownConeClassBound = d.totalConditionalBlocks := by
  unfold ruleTwoComplianceGapSq
  rw [Int.mul_eq_zero]
  omega

/-- Under the 4-way partition, `totalConditionalBlocks - ownConeClassBound = nonCompliantInstanceBindingCount` (`qou-y3x4`). -/
theorem total_sub_ownCone_eq_nonCompliant
    (d : DownstreamInstanceBindingData)
    (hPart : d.ownConeClassBound + nonCompliantInstanceBindingCount d =
      d.totalConditionalBlocks) :
    d.totalConditionalBlocks - d.ownConeClassBound =
      nonCompliantInstanceBindingCount d := by
  have hDef : nonCompliantInstanceBindingCount d =
      d.otherCarrierBound + d.noCarrierBound + d.unresolvedRefBlocks := rfl
  rw [hDef] at hPart ⊢
  omega

/-- Evaluation of the canonical 139-block §3b-cond rule 2 measurement (`qou-y3x4`). -/
theorem canonicalDownstreamInstanceBinding_eval :
    nonCompliantInstanceBindingCount canonicalDownstreamInstanceBinding = 130 ∧
      ruleTwoComplianceGapSq canonicalDownstreamInstanceBinding = 16900 := by
  decide

/-!
## 4. Context-Enrichment De-Laundering Campaign Partition (`qou-yl86`)
-/

/-- Remediation ledger for the 15 theorems restored from context-enrichment laundering (`qou-yl86`). -/
structure DeLaunderedEnrichmentData where
  restoredTheoremTotal : Int
  genuinelyProvedCount : Int
  conjectureDemotedCount : Int
  reassumedConclusionCount : Int
  deriving DecidableEq, Repr

/-- Honest remediation total `genuinelyProvedCount + conjectureDemotedCount` (`qou-yl86`). -/
def honestRemediationTotal (d : DeLaunderedEnrichmentData) : Int :=
  d.genuinelyProvedCount + d.conjectureDemotedCount

/-- Quadratic anti-reassumption and partition penalty (`qou-yl86`). -/
def deLaunderingCampaignPenaltySq (d : DeLaunderedEnrichmentData) : Int :=
  (d.restoredTheoremTotal - honestRemediationTotal d) *
    (d.restoredTheoremTotal - honestRemediationTotal d) +
    d.reassumedConclusionCount * d.reassumedConclusionCount

/-- Canonical 15-theorem remediation witness (`1` genuine downstream proof, `14` conjecture-demoted, `0` re-assumed) (`qou-yl86`). -/
def canonicalDeLaunderedEnrichment : DeLaunderedEnrichmentData :=
  { restoredTheoremTotal := 15
    genuinelyProvedCount := 1
    conjectureDemotedCount := 14
    reassumedConclusionCount := 0 }

/-- The de-laundering campaign penalty is non-negative (`qou-yl86`). -/
theorem deLaunderingCampaignPenaltySq_nonneg (d : DeLaunderedEnrichmentData) :
    0 ≤ deLaunderingCampaignPenaltySq d := by
  unfold deLaunderingCampaignPenaltySq
  have h1 : 0 ≤ (d.restoredTheoremTotal - honestRemediationTotal d) *
      (d.restoredTheoremTotal - honestRemediationTotal d) :=
    int_mul_self_nonneg (d.restoredTheoremTotal - honestRemediationTotal d)
  have h2 : 0 ≤ d.reassumedConclusionCount * d.reassumedConclusionCount :=
    int_mul_self_nonneg d.reassumedConclusionCount
  omega

/-- The de-laundering campaign penalty vanishes iff all restored theorems are honestly remediated and zero conclusions are re-assumed (`qou-yl86`). -/
theorem deLaunderingCampaignPenaltySq_eq_zero_iff (d : DeLaunderedEnrichmentData) :
    deLaunderingCampaignPenaltySq d = 0 ↔
      honestRemediationTotal d = d.restoredTheoremTotal ∧
        d.reassumedConclusionCount = 0 := by
  unfold deLaunderingCampaignPenaltySq
  rw [int_sq_add_sq_eq_zero_iff]
  omega

/-- Evaluation of the canonical 15-theorem de-laundering campaign witness (`qou-yl86`). -/
theorem canonicalDeLaunderedEnrichment_eval :
    honestRemediationTotal canonicalDeLaunderedEnrichment = 15 ∧
      deLaunderingCampaignPenaltySq canonicalDeLaunderedEnrichment = 0 := by
  decide

/-!
## 5. Pre-Existing Sorry-Free Sibling Preservation Rebuild (`qou-zatj`)
-/

/-- Batch rebuild partition preserving pre-existing sorry-free sibling files (`qou-zatj`). -/
structure SiblingPreservationRebuildData where
  totalBatchEntries : Int
  droppedR1OverwriteCount : Int
  retainedR2Count : Int
  retainedTier2Count : Int
  overwrittenWorkingSiblings : Int
  deriving DecidableEq, Repr

/-- Retained safe rebuild entries `retainedR2Count + retainedTier2Count` (`qou-zatj`). -/
def retainedRebuildTotal (d : SiblingPreservationRebuildData) : Int :=
  d.retainedR2Count + d.retainedTier2Count

/-- Quadratic overwrite-prevention and partition-balance penalty (`qou-zatj`). -/
def siblingPreservationPenaltySq (d : SiblingPreservationRebuildData) : Int :=
  (d.totalBatchEntries - d.droppedR1OverwriteCount - retainedRebuildTotal d) *
    (d.totalBatchEntries - d.droppedR1OverwriteCount - retainedRebuildTotal d) +
    d.overwrittenWorkingSiblings * d.overwrittenWorkingSiblings

/-- Canonical rebuild witness dropping R1 overwrites (`4` dropped, `15` R2 + `10` Tier-2 retained, `0` overwritten) (`qou-zatj`). -/
def canonicalSiblingPreservationRebuild : SiblingPreservationRebuildData :=
  { totalBatchEntries := 29
    droppedR1OverwriteCount := 4
    retainedR2Count := 15
    retainedTier2Count := 10
    overwrittenWorkingSiblings := 0 }

/-- The sibling-preservation penalty is non-negative (`qou-zatj`). -/
theorem siblingPreservationPenaltySq_nonneg (d : SiblingPreservationRebuildData) :
    0 ≤ siblingPreservationPenaltySq d := by
  unfold siblingPreservationPenaltySq
  have h1 : 0 ≤ (d.totalBatchEntries - d.droppedR1OverwriteCount - retainedRebuildTotal d) *
      (d.totalBatchEntries - d.droppedR1OverwriteCount - retainedRebuildTotal d) :=
    int_mul_self_nonneg (d.totalBatchEntries - d.droppedR1OverwriteCount - retainedRebuildTotal d)
  have h2 : 0 ≤ d.overwrittenWorkingSiblings * d.overwrittenWorkingSiblings :=
    int_mul_self_nonneg d.overwrittenWorkingSiblings
  omega

/-- The sibling-preservation penalty vanishes iff the rebuild partition balances and zero working siblings are overwritten (`qou-zatj`). -/
theorem siblingPreservationPenaltySq_eq_zero_iff (d : SiblingPreservationRebuildData) :
    siblingPreservationPenaltySq d = 0 ↔
      d.droppedR1OverwriteCount + retainedRebuildTotal d = d.totalBatchEntries ∧
        d.overwrittenWorkingSiblings = 0 := by
  unfold siblingPreservationPenaltySq
  rw [int_sq_add_sq_eq_zero_iff]
  omega

/-- Evaluation of the canonical sibling-preservation rebuild witness (`qou-zatj`). -/
theorem canonicalSiblingPreservationRebuild_eval :
    retainedRebuildTotal canonicalSiblingPreservationRebuild = 25 ∧
      siblingPreservationPenaltySq canonicalSiblingPreservationRebuild = 0 := by
  decide

end QOU.Foundations.AxiomDischargedScopeUnencodedCarrierFilterDownstreamInstanceBindingDeLaunderedEnrichmentSiblingPreservationRebuild
