/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Formalization for beans in the qou-10v9 subtree:
  - qou-07ts: compute_atom_chi_rust 3He/4He 50th-digit nondeterminism attribution vs L1 gate margin
  - qou-324i: q0Anchor `independent` override-sensitivity blindness on hardcoded/direct-read muon pins (7 false positives)
  - qou-49vn: Stale chi cache (0.5751722439) vs fresh/markov-peel/bridge (0.1519683392) 3.78x discrepancy
  - qou-4pdh: Module-level Q_MP 50-digit import cap under OUTPUT_DPS=60 (10 unbacked trailing digits)
  - qou-5mxd: Far-commutativity ([A_a, A_b] = 0 for |a - b| >= 2) reduction of Magnus pair sum and H_9 triton 14/14 overlap
-/

namespace QOU.Eightfold.ChiRustNondeterminismOverrideBlindnessChiCacheStalenessQmpDigitCapAndMagnusFarCommutativity

/-!
## 1. Bean `qou-07ts`: `compute_atom_chi_rust` 50th-Digit Nondeterminism vs L1 Precision Margin
Across `8` consecutive unmodified runs of `compute_atom_chi_rust.py 3He`, `4` distinct SHA-256
fingerprints appear with counts `[4, 2, 1, 1]` (modal count `4 < 8`), and on `4He` `4` of `154`
partitions move by `±1` ulp at digit `50` (`-1 + -1 + -1 + 1 = -2` net ulp). While `50` dps exceeds
the `15`-digit L1 gate (`1 ppQ = 10^-15`) by `35` orders of magnitude, non-zero run variance breaks
single-run byte-identical attribution.
-/

/-- Number of runs in a sample of size `totalRuns` that deviate from the modal fingerprint count `modalCount`. -/
def nonModalAttributionDriftCount (totalRuns modalCount : Int) : Int :=
  totalRuns - modalCount

/-- Precision safety margin in decimal orders of magnitude between `actualDps` and `l1GateDps`. -/
def l1PrecisionOrderMargin (actualDps l1GateDps : Int) : Int :=
  actualDps - l1GateDps

/-- Universal theorem: whenever `modalCount < totalRuns`, the number of non-modal runs is strictly
    positive (`0 < nonModalAttributionDriftCount totalRuns modalCount`), so single-run before/after
    comparison is insufficient for attribution. -/
theorem attribution_drift_pos_of_modal_lt_total (totalRuns modalCount : Int)
    (hLt : modalCount < totalRuns) :
    0 < nonModalAttributionDriftCount totalRuns modalCount := by
  dsimp [nonModalAttributionDriftCount]
  omega

/-- Concrete verification of the `3He` 8-run fingerprint multiplicity `[4, 2, 1, 1]`, the `4He`
    `154`-partition ulp movement (`4` moved: three `-1` and one `+1`), and the `50 - 15 = 35` order
    L1 precision margin. -/
theorem he3_eight_run_nondeterminism_and_he4_ulp_margin :
    (4 : Int) + 2 + 1 + 1 = 8 ∧
    nonModalAttributionDriftCount 8 4 = 4 ∧
    (154 : Int) - 4 = 150 ∧
    (-1 : Int) + (-1) + (-1) + 1 = -2 ∧
    l1PrecisionOrderMargin 50 15 = 35 := by
  decide

/-!
## 2. Bean `qou-324i`: `q0Anchor: independent` Override-Sensitivity Blindness (`7` False Positives)
An environment-override test checks whether `output(env_muon) == output(env_proton)`. When a
producer bypasses `q_parameter` and uses a fixed pin `q_fixed` (`routed = false`), its output
difference between `env_muon` and `env_proton` is `q_fixed - q_fixed = 0` even when
`q_fixed ≠ q_proton`, producing a false-positive `independent` classification.
-/

/-- Effective `q_0` value seen by a producer: `qEnv` if routed through `q_parameter`, or `qFixed`
    if hardcoded / read directly from the pinning witness. -/
def effectiveQ0UnderOverride (routed : Bool) (qEnv qFixed : Int) : Int :=
  if routed then qEnv else qFixed

/-- Override sensitivity difference between running under `qEnvMuon` vs `qEnvProton`. -/
def overrideSensitivityDiff (routed : Bool) (qEnvMuon qEnvProton qFixed : Int) : Int :=
  effectiveQ0UnderOverride routed qEnvMuon qFixed -
    effectiveQ0UnderOverride routed qEnvProton qFixed

/-- Universal theorem: when `routed = false` (hardcoded literal or direct witness read), the
    override sensitivity difference vanishes identically (`= 0`) for ALL `qEnvMuon, qEnvProton, qFixed`,
    even while the actual shift from the proton anchor `qFixed - qEnvProton` is nonzero whenever
    `qFixed ≠ qEnvProton`. -/
theorem unrouted_pin_is_override_blind_yet_anchor_biased (qEnvMuon qEnvProton qFixed : Int)
    (hBiased : qFixed ≠ qEnvProton) :
    overrideSensitivityDiff false qEnvMuon qEnvProton qFixed = 0 ∧
    effectiveQ0UnderOverride false qEnvMuon qFixed - qEnvProton ≠ 0 := by
  dsimp [overrideSensitivityDiff, effectiveQ0UnderOverride]
  omega

/-- Concrete verification of the post-#5457 partition of the `37` `independent`-stamped witnesses:
    `28` clean + `9` carrying muon digits (`6` hardcoded + `1` direct read + `2` inherited = `9`),
    giving `6 + 1 = 7` direct producer false positives. -/
theorem independent_disposition_audit_partition_counts :
    (28 : Int) + 9 = 37 ∧
    (6 : Int) + 1 + 2 = 9 ∧
    (6 : Int) + 1 = 7 := by
  decide

/-!
## 3. Bean `qou-49vn`: Stale `chi` Cache (`0.5751722439`) vs Fresh/Markov-Peel (`0.1519683392`)
For fixed Plancherel weights `y_λ`, a change in character values `χ_λ^cached → χ_λ^fresh` changes
`tr_M = ∑ y_λ χ_λ` by `∑ y_λ (χ_λ^cached - χ_λ^fresh)`. On the deuteron (`n = 6`, `11` partitions,
`9` moved), the cached witness gives `0.5751722439` while `--fresh`, Markov peel, and Hoefsmit+Wenzl
bridge all give `0.1519683392` (`> 3.78x` ratio).
-/

/-- Bilinear trace discrepancy `(y * chiCached) - (y * chiFresh)` for a single partition contribution. -/
def partitionTraceDiscrepancy (yWeight chiCached chiFresh : Int) : Int :=
  yWeight * chiCached - yWeight * chiFresh

/-- Universal factorization: for fixed `y_λ`, the trace discrepancy equals `y_λ * (χ_λ^cached - χ_λ^fresh)`
    and is strictly nonzero whenever `y_λ ≠ 0` and `χ_λ^cached ≠ χ_λ^fresh`. -/
theorem fixed_y_chi_discrepancy_factorization_and_ne_zero (yWeight chiCached chiFresh : Int)
    (hy : yWeight ≠ 0) (hChi : chiCached ≠ chiFresh) :
    partitionTraceDiscrepancy yWeight chiCached chiFresh = yWeight * (chiCached - chiFresh) ∧
    partitionTraceDiscrepancy yWeight chiCached chiFresh ≠ 0 := by
  have hId : partitionTraceDiscrepancy yWeight chiCached chiFresh = yWeight * (chiCached - chiFresh) := by
    dsimp [partitionTraceDiscrepancy]
    rw [Int.mul_sub]
  refine ⟨hId, ?_⟩
  rw [hId]
  have hDiff : chiCached - chiFresh ≠ 0 := by omega
  exact Int.mul_ne_zero hy hDiff

/-- Concrete verification in `10^10`-scaled units that `cached (5751722439) - fresh (1519683392) = 4232039047`,
    that the ratio exceeds `378 / 100` (`3.78x`), and that `9` of `11` partitions moved (`2` unchanged). -/
theorem deuteron_chi_cache_vs_fresh_discrepancy_and_ratio :
    (5751722439 : Int) - 1519683392 = 4232039047 ∧
    100 * (5751722439 : Int) > 378 * 1519683392 ∧
    100 * (5751722439 : Int) < 379 * 1519683392 ∧
    (11 : Int) - 9 = 2 := by
  decide

/-!
## 4. Bean `qou-4pdh`: `Q_MP` 50-Digit Import Cap under `OUTPUT_DPS = 60`
When a module-level constant `Q_MP` is evaluated at import time under `importDps = 50` (`169` bits)
and later consumed in a session with `computeDps = 80` and serialized at `outputDps = 60`, the
true information precision is capped at `min(importDps, computeDps) = 50`, leaving
`outputDps - min(importDps, computeDps) = 10` unbacked trailing digits across importers.
-/

/-- Effective information precision `min(importDps, computeDps)` of a value derived from an
    import-time float `Q_MP`. -/
def effectiveImportCappedDps (importDps computeDps : Int) : Int :=
  if importDps ≤ computeDps then importDps else computeDps

/-- Count of unbacked serialized decimal digits when formatting at `outputDps`. -/
def unbackedSerializedDigits (importDps computeDps outputDps : Int) : Int :=
  outputDps - effectiveImportCappedDps importDps computeDps

/-- Universal theorem: whenever `importDps ≤ computeDps` and `importDps < outputDps`, the number of
    unbacked serialized digits equals `outputDps - importDps > 0`. -/
theorem import_cap_creates_unbacked_digits (importDps computeDps outputDps : Int)
    (hCap : importDps ≤ computeDps) (hOut : importDps < outputDps) :
    unbackedSerializedDigits importDps computeDps outputDps = outputDps - importDps ∧
    0 < unbackedSerializedDigits importDps computeDps outputDps := by
  dsimp [unbackedSerializedDigits, effectiveImportCappedDps]
  split
  · omega
  · contradiction

/-- Concrete verification for `importDps = 50`, `computeDps = 80`, `outputDps = 60` (`10` unbacked
    digits, `266 - 169 = 97` missing significand bits relative to 80-dps `mpf`). -/
theorem q_mp_fifty_digit_cap_under_sixty_output_dps :
    effectiveImportCappedDps 50 80 = 50 ∧
    unbackedSerializedDigits 50 80 60 = 10 ∧
    (266 : Int) - 169 = 97 := by
  decide

/-!
## 5. Bean `qou-5mxd`: Magnus Far-Commutativity (`[A_a, A_b] = 0` for `|a - b| ≥ 2`) Pair Reduction
In a chain of `m ≥ 2` generators `A_1, …, A_m`, there are `m * (m - 1) / 2` ordered index pairs
`1 ≤ a < b ≤ m`, of which `(m - 1) * (m - 2) / 2` satisfy `b - a ≥ 2` (far-commuting) and exactly
`m - 1` are adjacent (`b = a + 1`). Clearing the factor of `2`,
`m * (m - 1) - (m - 1) * (m - 2) = 2 * (m - 1)`.
-/

/-- Twice the total pair count `2 * C(m, 2) = m * (m - 1)`. -/
def twiceTotalGeneratorPairs (m : Int) : Int :=
  m * (m - 1)

/-- Twice the far-commuting pair count `2 * C(m - 1, 2) = (m - 1) * (m - 2)` (`|a - b| ≥ 2`). -/
def twiceFarCommutingPairs (m : Int) : Int :=
  (m - 1) * (m - 2)

/-- Universal algebraic identity: subtracting all far-commuting pairs (`|a - b| ≥ 2`) from all
    generator pairs leaves exactly `2 * (m - 1)` (i.e. `m - 1` adjacent pairs `b = a + 1`). -/
theorem magnus_far_commutativity_leaves_adjacent_pairs (m : Int) :
    twiceTotalGeneratorPairs m - twiceFarCommutingPairs m = 2 * (m - 1) := by
  dsimp [twiceTotalGeneratorPairs, twiceFarCommutingPairs]
  rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.mul_sub]
  omega

/-- Concrete verification for `m = 5` (`5` generators in `B_6`, `10` total pairs = `6` far-commuting + `4` adjacent)
    and `m = 8` (`8` generators in `B_9`, `28` total pairs = `21` far-commuting + `7` adjacent), together
    with the triton `H_9` partition overlap (`14` unpatched, `19` patched, `14` overlapping, `5` new). -/
theorem triton_h9_magnus_pair_reduction_and_partition_overlap :
    twiceTotalGeneratorPairs 5 = 20 ∧
    twiceFarCommutingPairs 5 = 12 ∧
    twiceTotalGeneratorPairs 5 - twiceFarCommutingPairs 5 = 8 ∧
    twiceTotalGeneratorPairs 8 = 56 ∧
    twiceFarCommutingPairs 8 = 42 ∧
    twiceTotalGeneratorPairs 8 - twiceFarCommutingPairs 8 = 14 ∧
    (19 : Int) - 14 = 5 ∧
    (30 : Int) - 19 = 11 := by
  decide

end QOU.Eightfold.ChiRustNondeterminismOverrideBlindnessChiCacheStalenessQmpDigitCapAndMagnusFarCommutativity
