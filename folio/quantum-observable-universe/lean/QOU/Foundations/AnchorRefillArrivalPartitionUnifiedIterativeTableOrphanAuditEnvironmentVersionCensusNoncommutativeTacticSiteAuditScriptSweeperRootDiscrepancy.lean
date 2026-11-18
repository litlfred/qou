/-!
# Anchor Refill Arrival Partition, Unified Iterative Table Orphan Audit, Environment Version Census, Noncommutative Tactic Site Audit, and Script Sweeper Root Discrepancy

This module formalizes the exact discrete and polynomial identities governing five
provenance-refill, orphaned-table, environment-census, noncommutative-tactic, and
script-sweeper audit gates across the Quantum Observable Universe (`QOU`) program:

1. **Anchor Refill Arrival Partition (`qou-y98b`)**:
   Models the `q0Anchor` missing-cause partition over `liveAuditMissing = 1678`:
   - `undeclaredPinCount = 1199`, `notBuilderCount = 365`,
   - `noProducerCount = 55`, `declaredStaleCount = 59`,
   - `rawMissingCount = 2066`, `deprecatedExcludedGap = 388`,
   along with the parallelogram quadratic identity
   `(a + b) ^ 2 + (a - b) ^ 2 = 2 * (a ^ 2 + b ^ 2)`
   and non-negativity of the squared arrival imbalance `(a - b) ^ 2 >= 0`.

2. **Unified Iterative Correction Table Orphan Audit (`qou-ypq6`)**:
   Models the unified-iterative-correction citation and table-row partition:
   - `citingContentBlocks = 9`, `numericTableBlocks = 1`, `proseOnlyBlocks = 8`,
   - `tabulatedIsotopeRows = 7`, `partitionCutoffMax = 11`,
   together with the trinomial square expansion
   `(p + q + r) ^ 2 = p ^ 2 + q ^ 2 + r ^ 2 + 2 * (p * q + q * r + r * p)`.

3. **Environment Version Census Partition (`qou-yrt4`)**:
   Models the four-way environment version partition across `totalCorpusWitnesses = 3065`:
   - `version130Witnesses = 1184`, `noEnvBlockWitnesses = 1176`,
   - `version141Witnesses = 703`, `version000Witnesses = 2`,
   together with the quarter-square polarization identity
   `(u + v) ^ 2 - (u - v) ^ 2 = 4 * (u * v)`
   and difference-of-squares factorization `(u + v) * (u - v) = u ^ 2 - v ^ 2`.

4. **Noncommutative Tactic Site Audit (`qou-yzl8`)**:
   Models the six noncommutative tactic failure sites partitioned into two three-site
   inverse-product chains (`forwardChainSites = 3`, `inverseChainSites = 3`,
   `totalTacticFailureSites = 6`), together with the cubic difference factorization
   `(w - s) * (w ^ 2 + w * s + s ^ 2) = w ^ 3 - s ^ 3`.

5. **Script Sweeper Root Discrepancy Audit (`qou-z8x9`)**:
   Models the script-QA sidecar census across `sweptDirectories = 18`:
   - `hashFreshSidecars = 708`, `hashStaleSidecars = 1086`,
   - `missingPathSidecars = 4`, `totalSidecars = 1798`, `auditedProducersInPlatformRoot = 0`,
   together with the two-square composition identity
   `(a * c - b * d) ^ 2 + (a * d + b * c) ^ 2 = (a ^ 2 + b ^ 2) * (c ^ 2 + d ^ 2)`.
-/

namespace QOU.Foundations.AnchorRefillArrivalPartitionUnifiedIterativeTableOrphanAuditEnvironmentVersionCensusNoncommutativeTacticSiteAuditScriptSweeperRootDiscrepancy

/-! ## Helper Lemmas -/

/-- Any integer squared is non-negative (`a * a >= 0`). -/
theorem int_mul_self_nonneg (a : Int) : 0 ≤ a * a := by
  cases Int.le_total 0 a with
  | inl h =>
    exact Int.mul_nonneg h h
  | inr h =>
    have hneg : 0 ≤ -a := Int.neg_nonneg_of_nonpos h
    have hmul : 0 ≤ (-a) * (-a) := Int.mul_nonneg hneg hneg
    rw [Int.neg_mul_neg] at hmul
    exact hmul

/-- Expansion of `(a + b) * (a + b)`. -/
theorem int_add_sq_expand (a b : Int) :
    (a + b) * (a + b) = a * a + 2 * (a * b) + b * b := by
  rw [Int.mul_add, Int.add_mul, Int.add_mul]
  have hba : b * a = a * b := Int.mul_comm b a
  omega

/-- Expansion of `(a - b) * (a - b)`. -/
theorem int_sub_sq_expand (a b : Int) :
    (a - b) * (a - b) = a * a - 2 * (a * b) + b * b := by
  rw [Int.mul_sub, Int.sub_mul, Int.sub_mul]
  have hba : b * a = a * b := Int.mul_comm b a
  omega

/-! ## Section 1: Anchor Refill Arrival Partition (`qou-y98b`) -/

/-- Ledger tracking the `q0Anchor` missing-cause partition and the bookkeeping gap between
    raw `computations/**` and live audit scope (`qou-y98b`). -/
structure AnchorRefillArrivalPartitionLedger where
  undeclaredPinCount : Int
  notBuilderCount : Int
  noProducerCount : Int
  declaredStaleCount : Int
  liveAuditMissingCount : Int
  deprecatedBookkeepingGap : Int
  rawMissingCount : Int
  hCausePartition :
    undeclaredPinCount + notBuilderCount + noProducerCount + declaredStaleCount =
      liveAuditMissingCount
  hScopePartition :
    liveAuditMissingCount + deprecatedBookkeepingGap = rawMissingCount
  hUndeclaredMajority :
    notBuilderCount + noProducerCount + declaredStaleCount < undeclaredPinCount
  deriving Repr, DecidableEq

/-- Canonical anchor-refill arrival and cause-partition ledger
    (`1199 + 365 + 55 + 59 = 1678`, `1678 + 388 = 2066`). -/
def canonicalAnchorRefillArrivalPartitionLedger : AnchorRefillArrivalPartitionLedger where
  undeclaredPinCount := 1199
  notBuilderCount := 365
  noProducerCount := 55
  declaredStaleCount := 59
  liveAuditMissingCount := 1678
  deprecatedBookkeepingGap := 388
  rawMissingCount := 2066
  hCausePartition := rfl
  hScopePartition := rfl
  hUndeclaredMajority := by decide

/-- Parallelogram quadratic identity on stamped vs unstamped arrival counts:
    `(a + b) ^ 2 + (a - b) ^ 2 = 2 * (a ^ 2 + b ^ 2)`. -/
theorem anchor_arrival_parallelogram_identity (a b : Int) :
    (a + b) * (a + b) + (a - b) * (a - b) = 2 * (a * a + b * b) := by
  have h1 := int_add_sq_expand a b
  have h2 := int_sub_sq_expand a b
  omega

/-- Non-negativity of the squared arrival difference `(a - b) ^ 2 >= 0`. -/
theorem anchor_arrival_diff_sq_nonneg (a b : Int) :
    0 ≤ (a - b) * (a - b) :=
  int_mul_self_nonneg (a - b)

/-- In any `AnchorRefillArrivalPartitionLedger`, the undeclared-pin population strictly
    exceeds half of `liveAuditMissingCount` (`liveAuditMissingCount < 2 * undeclaredPinCount`),
    and `rawMissingCount - deprecatedBookkeepingGap = liveAuditMissingCount`. -/
theorem anchor_undeclared_strict_majority_and_scope_recovery
    (L : AnchorRefillArrivalPartitionLedger) :
    L.liveAuditMissingCount < 2 * L.undeclaredPinCount ∧
    L.rawMissingCount - L.deprecatedBookkeepingGap = L.liveAuditMissingCount := by
  have h1 := L.hCausePartition
  have h2 := L.hScopePartition
  have h3 := L.hUndeclaredMajority
  omega

/-! ## Section 2: Unified Iterative Correction Table Orphan Audit (`qou-ypq6`) -/

/-- Ledger tracking the unified-iterative-correction citing blocks, orphaned numeric table
    block, tabulated isotope rows, and partition cutoff (`qou-ypq6`). -/
structure UnifiedIterativeTableOrphanLedger where
  numericTableBlocks : Int
  proseOnlyCitingBlocks : Int
  totalCitingBlocks : Int
  tabulatedIsotopeRows : Int
  partitionCutoffMax : Int
  liveProducerCount : Int
  hCitationSum : numericTableBlocks + proseOnlyCitingBlocks = totalCitingBlocks
  hOrphanProducer : liveProducerCount = 0
  hRowsPos : 0 < tabulatedIsotopeRows
  deriving Repr, DecidableEq

/-- Canonical unified-iterative-correction table orphan ledger
    (`1 + 8 = 9` citing blocks, `7` tabulated isotope rows, `k_max = 11`, `0` live producers). -/
def canonicalUnifiedIterativeTableOrphanLedger : UnifiedIterativeTableOrphanLedger where
  numericTableBlocks := 1
  proseOnlyCitingBlocks := 8
  totalCitingBlocks := 9
  tabulatedIsotopeRows := 7
  partitionCutoffMax := 11
  liveProducerCount := 0
  hCitationSum := rfl
  hOrphanProducer := rfl
  hRowsPos := by decide

/-- Trinomial square expansion for three table-audit invariants `p, q, r`:
    `(p + q + r) ^ 2 = p ^ 2 + q ^ 2 + r ^ 2 + 2 * (p * q + q * r + r * p)`. -/
theorem unified_table_trinomial_square (p q r : Int) :
    (p + q + r) * (p + q + r) =
      p * p + q * q + r * r + 2 * (p * q + q * r + r * p) := by
  have h1 := int_add_sq_expand (p + q) r
  have h2 := int_add_sq_expand p q
  have h3 : (p + q) * r = p * r + q * r := Int.add_mul p q r
  have hpr : p * r = r * p := Int.mul_comm p r
  omega

/-- In any `UnifiedIterativeTableOrphanLedger`, subtracting prose-only citing blocks from
    total citing blocks recovers the numeric table block count, and `liveProducerCount = 0`. -/
theorem unified_table_citing_recovery (L : UnifiedIterativeTableOrphanLedger) :
    L.totalCitingBlocks - L.proseOnlyCitingBlocks = L.numericTableBlocks ∧
    L.liveProducerCount = 0 := by
  have h1 := L.hCitationSum
  have h2 := L.hOrphanProducer
  omega

/-! ## Section 3: Environment Version Census Partition (`qou-yrt4`) -/

/-- Ledger tracking the four-way environment version partition across the witness corpus
    and the 9-producer migration batch ledger (`qou-yrt4`). -/
structure EnvironmentVersionCensusLedger where
  version130Witnesses : Int
  noEnvBlockWitnesses : Int
  version141Witnesses : Int
  version000Witnesses : Int
  totalMeasuredWitnesses : Int
  batchOkProducers : Int
  batchNonzeroProducers : Int
  batchTimeoutProducers : Int
  batchTotalProducers : Int
  hCorpusSum :
    version130Witnesses + noEnvBlockWitnesses + version141Witnesses + version000Witnesses =
      totalMeasuredWitnesses
  hBatchSum :
    batchOkProducers + batchNonzeroProducers + batchTimeoutProducers =
      batchTotalProducers
  hVersion141Pos : 0 < version141Witnesses
  deriving Repr, DecidableEq

/-- Canonical environment version census ledger
    (`1184 + 1176 + 703 + 2 = 3065`, batch `6 + 2 + 1 = 9`). -/
def canonicalEnvironmentVersionCensusLedger : EnvironmentVersionCensusLedger where
  version130Witnesses := 1184
  noEnvBlockWitnesses := 1176
  version141Witnesses := 703
  version000Witnesses := 2
  totalMeasuredWitnesses := 3065
  batchOkProducers := 6
  batchNonzeroProducers := 2
  batchTimeoutProducers := 1
  batchTotalProducers := 9
  hCorpusSum := rfl
  hBatchSum := rfl
  hVersion141Pos := by decide

/-- Quarter-square polarization identity for environment version cohorts `u` and `v`:
    `(u + v) ^ 2 - (u - v) ^ 2 = 4 * (u * v)`. -/
theorem environment_census_polarization (u v : Int) :
    (u + v) * (u + v) - (u - v) * (u - v) = 4 * (u * v) := by
  have h1 := int_add_sq_expand u v
  have h2 := int_sub_sq_expand u v
  omega

/-- Difference-of-squares factorization for environment version cohorts `u` and `v`:
    `(u + v) * (u - v) = u ^ 2 - v ^ 2`. -/
theorem environment_census_diff_sq (u v : Int) :
    (u + v) * (u - v) = u * u - v * v := by
  rw [Int.mul_sub, Int.add_mul, Int.add_mul]
  have hvu : v * u = u * v := Int.mul_comm v u
  omega

/-! ## Section 4: Noncommutative Tactic Site Audit (`qou-yzl8`) -/

/-- Ledger tracking the six commutative-ring tactic failure sites on a noncommutative
    braid-group algebra (`3` sites in the forward inverse-product proof + `3` sites in
    the reverse inverse-product proof = `6` total sites, `qou-yzl8`). -/
structure NoncommutativeTacticSiteLedger where
  forwardProductSites : Int
  reverseProductSites : Int
  totalFailureSites : Int
  surfacedPerBuildErrors : Int
  hiddenCascadedErrors : Int
  hSiteSum : forwardProductSites + reverseProductSites = totalFailureSites
  hCascadeSum : surfacedPerBuildErrors + hiddenCascadedErrors = totalFailureSites
  hSymmetry : forwardProductSites = reverseProductSites
  deriving Repr, DecidableEq

/-- Canonical noncommutative tactic site ledger (`3 + 3 = 6 = 1 + 5`). -/
def canonicalNoncommutativeTacticSiteLedger : NoncommutativeTacticSiteLedger where
  forwardProductSites := 3
  reverseProductSites := 3
  totalFailureSites := 6
  surfacedPerBuildErrors := 1
  hiddenCascadedErrors := 5
  hSiteSum := rfl
  hCascadeSum := rfl
  hSymmetry := rfl

/-- In any `NoncommutativeTacticSiteLedger`, the total failure sites equal twice the
    forward-product site count, and `totalFailureSites - surfacedPerBuildErrors` equals
    the hidden cascaded error count. -/
theorem noncommutative_tactic_double_and_cascade_recovery
    (L : NoncommutativeTacticSiteLedger) :
    L.totalFailureSites = 2 * L.forwardProductSites ∧
    L.totalFailureSites - L.surfacedPerBuildErrors = L.hiddenCascadedErrors := by
  have h1 := L.hSiteSum
  have h2 := L.hCascadeSum
  have h3 := L.hSymmetry
  omega

/-- Cubic difference factorization for noncommutative step reductions:
    `(w - s) * (w ^ 2 + w * s + s ^ 2) = w ^ 3 - s ^ 3`. -/
theorem noncommutative_site_cubic_factorization (w s : Int) :
    (w - s) * (w * w + w * s + s * s) = w * (w * w) - s * (s * s) := by
  rw [Int.sub_mul, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add]
  have h1 : s * (w * w) = w * (w * s) := by
    rw [← Int.mul_assoc, Int.mul_comm s w, Int.mul_assoc, Int.mul_comm s w]
  have h2 : s * (w * s) = w * (s * s) := by
    rw [← Int.mul_assoc, Int.mul_comm s w, Int.mul_assoc]
  omega

/-! ## Section 5: Script Sweeper Root Discrepancy Audit (`qou-z8x9`) -/

/-- Ledger tracking the script-QA sidecar population (`708` fresh + `1086` hash-stale +
    `4` missing-path = `1798` sidecars across `18` directories, while the platform root
    audits `0` Python producers, `qou-z8x9`). -/
structure ScriptSweeperRootDiscrepancyLedger where
  sweptDirectories : Int
  hashFreshSidecars : Int
  hashStaleSidecars : Int
  missingPathSidecars : Int
  totalSidecars : Int
  auditedProducersInPlatformRoot : Int
  hSidecarSum :
    hashFreshSidecars + hashStaleSidecars + missingPathSidecars = totalSidecars
  hZeroAudited : auditedProducersInPlatformRoot = 0
  hStaleMajority : hashFreshSidecars + missingPathSidecars < hashStaleSidecars
  deriving Repr, DecidableEq

/-- Canonical script-sweeper root discrepancy ledger
    (`18` dirs, `708 + 1086 + 4 = 1798` sidecars, `0` audited in platform root). -/
def canonicalScriptSweeperRootDiscrepancyLedger : ScriptSweeperRootDiscrepancyLedger where
  sweptDirectories := 18
  hashFreshSidecars := 708
  hashStaleSidecars := 1086
  missingPathSidecars := 4
  totalSidecars := 1798
  auditedProducersInPlatformRoot := 0
  hSidecarSum := rfl
  hZeroAudited := rfl
  hStaleMajority := by decide

/-- Two-square composition identity for sidecar cohort pairs `(a, b)` and `(c, d)`:
    `(a * c - b * d) ^ 2 + (a * d + b * c) ^ 2 = (a ^ 2 + b ^ 2) * (c ^ 2 + d ^ 2)`. -/
theorem script_sweeper_two_square_composition (a b c d : Int) :
    (a * c - b * d) * (a * c - b * d) + (a * d + b * c) * (a * d + b * c) =
      (a * a + b * b) * (c * c + d * d) := by
  have h1 := int_sub_sq_expand (a * c) (b * d)
  have h2 := int_add_sq_expand (a * d) (b * c)
  have h3 : (a * a + b * b) * (c * c + d * d) =
      (a * a) * (c * c) + (b * b) * (c * c) + ((a * a) * (d * d) + (b * b) * (d * d)) := by
    rw [Int.mul_add, Int.add_mul, Int.add_mul]
  have hac : (a * c) * (a * c) = (a * a) * (c * c) := by
    rw [Int.mul_assoc, ← Int.mul_assoc c a c, Int.mul_comm c a, Int.mul_assoc, ← Int.mul_assoc]
  have had : (a * d) * (a * d) = (a * a) * (d * d) := by
    rw [Int.mul_assoc, ← Int.mul_assoc d a d, Int.mul_comm d a, Int.mul_assoc, ← Int.mul_assoc]
  have hbc : (b * c) * (b * c) = (b * b) * (c * c) := by
    rw [Int.mul_assoc, ← Int.mul_assoc c b c, Int.mul_comm c b, Int.mul_assoc, ← Int.mul_assoc]
  have hbd : (b * d) * (b * d) = (b * b) * (d * d) := by
    rw [Int.mul_assoc, ← Int.mul_assoc d b d, Int.mul_comm d b, Int.mul_assoc, ← Int.mul_assoc]
  have hcross : (a * c) * (b * d) = (a * d) * (b * c) := by
    have hL : (a * c) * (b * d) = a * (b * (c * d)) := by
      rw [Int.mul_assoc, ← Int.mul_assoc c b d, Int.mul_comm c b, Int.mul_assoc]
    have hR : (a * d) * (b * c) = a * (b * (c * d)) := by
      rw [Int.mul_assoc, ← Int.mul_assoc d b c, Int.mul_comm d b, Int.mul_assoc, Int.mul_comm d c]
    rw [hL, hR]
  omega

/-- Joint five-component synthesis certificate across `qou-y98b`, `qou-ypq6`, `qou-yrt4`,
    `qou-yzl8`, and `qou-z8x9`. -/
theorem round_ninety_six_joint_certificate (a b p q r w s : Int) :
    ((a + b) * (a + b) + (a - b) * (a - b) = 2 * (a * a + b * b)) ∧
    ((p + q + r) * (p + q + r) =
      p * p + q * q + r * r + 2 * (p * q + q * r + r * p)) ∧
    ((a + b) * (a + b) - (a - b) * (a - b) = 4 * (a * b)) ∧
    ((w - s) * (w * w + w * s + s * s) = w * (w * w) - s * (s * s)) ∧
    (canonicalScriptSweeperRootDiscrepancyLedger.hashFreshSidecars +
      canonicalScriptSweeperRootDiscrepancyLedger.hashStaleSidecars +
      canonicalScriptSweeperRootDiscrepancyLedger.missingPathSidecars = 1798) := by
  refine ⟨anchor_arrival_parallelogram_identity a b,
          unified_table_trinomial_square p q r,
          environment_census_polarization a b,
          noncommutative_site_cubic_factorization w s,
          rfl⟩

end QOU.Foundations.AnchorRefillArrivalPartitionUnifiedIterativeTableOrphanAuditEnvironmentVersionCensusNoncommutativeTacticSiteAuditScriptSweeperRootDiscrepancy
