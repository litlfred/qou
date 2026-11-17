/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization
-/

/-!
# Ordering Fingerprint Producer Taxonomy and Mass Table Multiprecision Slowdown

This module formalizes the arithmetic accounting for the 15-significant-digit
ordering-fingerprint audit across committed witnesses (`qou-4383`) and the
multiprecision runtime and trace-convention triage of the comprehensive mass
table (`qou-53p1`):

1. **Ordering-fingerprint witness and producer taxonomy (`qou-4383`)**:
   Scanning `3548` committed witnesses against `312` live 15-significant-digit
   grouped-era numerical fingerprints yields `89` initial witness hits (`6`
   subtree duplicates plus `83` computation originals split across `59` August
   2026, `21` September 2026, and `3` undated artifacts). After bulk re-execution
   drops `35` purely stale candidates (`81 → 46`), the producer taxonomy splits
   the `46` remaining candidates into `28` actionable producers, `16` downstream
   reflections, and `2` unresolved schema records (`28 + 16 + 2 = 46`).

2. **Comprehensive mass-table slowdown and trace-switch row split (`qou-53p1`)**:
   Moving per-generator volume evaluation from hardware floating point to
   arbitrary-precision arithmetic increases total execution duration from
   `57274` ms to `656759` ms across `14972` rows (`> 11×` slowdown), driven by
   `2724573` multiplications (`6811` per row over a `400`-row profile) and
   `1126208` float conversions (`2815` per row). Across the `14972` rows,
   `14970` shift under the trace-normalisation update while `2` remain invariant.
-/

namespace QOU.MassTheory.OrderingFingerprintTaxonomyAndMassTableSlowdown

/-- Total initial witness hits partitioned into subtree duplicates and
    computation originals (`qou-4383`). -/
def fingerprintInitialHitTotal (subtreeDuplicates computationOriginals : Int) : Int :=
  subtreeDuplicates + computationOriginals

/-- Partition of computation originals across three creation epochs (`qou-4383`). -/
def fingerprintEpochSplit (epochOne epochTwo undated : Int) : Int :=
  epochOne + epochTwo + undated

/-- Residual candidate count after dropping purely stale re-run artifacts (`qou-4383`). -/
def fingerprintBulkDropResidual (initialCandidates staleDropped : Int) : Int :=
  initialCandidates - staleDropped

/-- Producer taxonomy partition of residual candidates into actionable producers,
    downstream reflections, and unresolved records (`qou-4383`). -/
def fingerprintProducerTaxonomy (actionable downstreamReflections unresolved : Int) : Int :=
  actionable + downstreamReflections + unresolved

/-- Runtime duration excess above a linear slowdown multiple (`qou-53p1`). -/
def massTableDurationExcess (postDurationMs slowFactor preDurationMs : Int) : Int :=
  postDurationMs - slowFactor * preDurationMs

/-- Per-row operation count from a profiled batch (`qou-53p1`). -/
def massTablePerRowCallCount (totalCalls sampleRows : Int) : Int :=
  totalCalls / sampleRows

/-- Total mass-table rows partitioned into trace-shifted and invariant rows (`qou-53p1`). -/
def massTableRowShiftSplit (shiftedRows invariantRows : Int) : Int :=
  shiftedRows + invariantRows

/-- Initial ordering-fingerprint hits satisfy `6 + 83 = 89` and the epoch split
    satisfies `59 + 21 + 3 = 83` (`qou-4383`). -/
theorem fingerprint_initial_hits_and_epoch_split :
    fingerprintInitialHitTotal 6 83 = 89 ∧
    fingerprintEpochSplit 59 21 3 = 83 ∧
    fingerprintInitialHitTotal 6 (fingerprintEpochSplit 59 21 3) = 89 := by
  dsimp [fingerprintInitialHitTotal, fingerprintEpochSplit]
  have h1 : (6 : Int) + 83 = 89 := by omega
  have h2 : (59 : Int) + 21 + 3 = 83 := by omega
  have h3 : (6 : Int) + (59 + 21 + 3) = 89 := by omega
  exact ⟨h1, h2, h3⟩

/-- After dropping `35` purely stale artifacts from `81` re-runnable candidates,
    the `46` residual candidates match the producer taxonomy `28 + 16 + 2 = 46`
    (`qou-4383`). -/
theorem fingerprint_bulk_drop_and_producer_taxonomy_exact :
    fingerprintBulkDropResidual 81 35 = 46 ∧
    fingerprintProducerTaxonomy 28 16 2 = 46 ∧
    fingerprintBulkDropResidual 81 35 = fingerprintProducerTaxonomy 28 16 2 := by
  dsimp [fingerprintBulkDropResidual, fingerprintProducerTaxonomy]
  have h1 : (81 : Int) - 35 = 46 := by omega
  have h2 : (28 : Int) + 16 + 2 = 46 := by omega
  have h3 : (81 : Int) - 35 = 28 + 16 + 2 := by omega
  exact ⟨h1, h2, h3⟩

/-- Universal conservation law: adding dropped stale candidates to the three
    producer taxonomy buckets recovers the initial candidate count (`qou-4383`). -/
theorem fingerprint_taxonomy_plus_dropped_recovers_initial
    (actionable downstreamReflections unresolved staleDropped : Int) :
    fingerprintBulkDropResidual
      (fingerprintProducerTaxonomy actionable downstreamReflections unresolved + staleDropped)
      staleDropped =
    fingerprintProducerTaxonomy actionable downstreamReflections unresolved := by
  dsimp [fingerprintBulkDropResidual, fingerprintProducerTaxonomy]
  have h :
      actionable + downstreamReflections + unresolved + staleDropped - staleDropped =
      actionable + downstreamReflections + unresolved := by
    omega
  exact h

/-- The comprehensive mass-table runtime (`656759` ms vs `57274` ms) exceeds an
    `11×` slowdown with `6811` integer-part multiplications and `2815` float
    conversions per row over the `400`-row profile, and `14970 + 2 = 14972` rows
    in total (`qou-53p1`). -/
theorem mass_table_slowdown_and_row_split_exact :
    massTableDurationExcess 656759 11 57274 = 26745 ∧
    massTableDurationExcess 656759 11 57274 > 0 ∧
    massTablePerRowCallCount 2724573 400 = 6811 ∧
    massTablePerRowCallCount 1126208 400 = 2815 ∧
    massTableRowShiftSplit 14970 2 = 14972 := by
  dsimp [massTableDurationExcess, massTablePerRowCallCount, massTableRowShiftSplit]
  have h1 : (656759 : Int) - 11 * 57274 = 26745 := by omega
  have h2 : (656759 : Int) - 11 * 57274 > 0 := by omega
  have h3 : (2724573 : Int) / 400 = 6811 := by omega
  have h4 : (1126208 : Int) / 400 = 2815 := by omega
  have h5 : (14970 : Int) + 2 = 14972 := by omega
  exact ⟨h1, h2, h3, h4, h5⟩

/-- Universal additivity of runtime duration excess across consecutive slowdown
    increments (`qou-53p1`). -/
theorem mass_table_duration_excess_step
    (postDurationMs slowFactor preDurationMs : Int) :
    massTableDurationExcess postDurationMs (slowFactor + 1) preDurationMs =
    massTableDurationExcess postDurationMs slowFactor preDurationMs - preDurationMs := by
  dsimp [massTableDurationExcess]
  have hExpand : (slowFactor + 1) * preDurationMs = slowFactor * preDurationMs + preDurationMs := by
    rw [Int.add_mul, Int.one_mul]
  omega

end QOU.MassTheory.OrderingFingerprintTaxonomyAndMassTableSlowdown
