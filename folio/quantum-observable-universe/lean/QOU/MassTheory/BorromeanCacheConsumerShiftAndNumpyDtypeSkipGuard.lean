/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization
-/

/-!
# Borromean Cache Consumer Amplification Shift and Dtype Skip-Guard Separation

This module formalizes the consumer sensitivity analysis under regenerated
Borromean-word character caches (`qou-nmuz`) and the skip-guard vs assertion-failure
state separation for the array dtype benchmark (`qou-nz8e`):

1. **Borromean cache consumer shifts and red-count conservation (`qou-nmuz`)**:
   Replacing grouped-era character caches with Borromean-word caches across the
   four `deltalambda/` consumers decreases the five-body and six-body trace
   invariants (scaled by `10^3`: `3348 → 1224` and `3865 → 1156`), increases the
   required amplification factors (scaled by `10^2`: `6410 → 14340` and
   `8285 → 16435`), and narrows the inter-band ratio (scaled by `10`: `102 → 48`).
   In the saturation mechanism probe, two light-nucleus anchor assertions flip
   from failing to passing while two lithium grouped-pin assertions flip from
   passing to failing, conserving the total failing count at `3`.

2. **Dtype benchmark skip-guard separation and duration speedup (`qou-nz8e`)**:
   When the runtime array library already rejects the legacy precision alias,
   the benchmark takes a skip path (`computed = false`) that drops execution
   time from `408402` ms to `32485` ms (`> 12×` faster: `408402 - 12 * 32485 = 18582 > 0`).
   Separating the skip-guard state from the numerical assertion verdict prevents
   a skipped guard path from flipping the pass indicator to false.
-/

namespace QOU.MassTheory.BorromeanCacheConsumerShiftAndNumpyDtypeSkipGuard

/-- Net shift in scaled required amplification (`10^2 × A_req`) between
    regenerated Borromean-word caches and grouped-era caches (`qou-nmuz`). -/
def amplificationShiftHundredths (borromeanHundredths groupedHundredths : Int) : Int :=
  borromeanHundredths - groupedHundredths

/-- Net reduction in scaled trace value (`10^3 × tr_M`) between grouped-era
    and regenerated Borromean-word caches (`qou-nmuz`). -/
def traceReductionThousandths (groupedThousandths borromeanThousandths : Int) : Int :=
  groupedThousandths - borromeanThousandths

/-- Total failing assertion count partitioned into light-anchor failures,
    lithium-pin failures, and invariant structural failures (`qou-nmuz`). -/
def saturationProbeRedCount (lightAnchorFails lithiumPinFails structuralFails : Int) : Int :=
  lightAnchorFails + lithiumPinFails + structuralFails

/-- Execution duration margin between the full benchmark run and a multiple of
    the skip-guard run (`qou-nz8e`). -/
def benchmarkSkipDurationMargin (fullDurationMs speedupFactor skipDurationMs : Int) : Int :=
  fullDurationMs - speedupFactor * skipDurationMs

/-- Skip-aware benchmark verdict encoding: `0` = failed assertion, `1` = passed
    assertion, `2` = skipped by environment guard (`qou-nz8e`). -/
def skipAwareVerdictCode (computed assertionPassed : Bool) : Int :=
  if computed then
    if assertionPassed then 1 else 0
  else
    2

/-- Legacy conflated verdict encoding that maps `computed = false` to `0` (`qou-nz8e`). -/
def conflatedVerdictCode (computed assertionPassed : Bool) : Int :=
  if computed && assertionPassed then 1 else 0

/-- Regenerating the Borromean-word character caches increases scaled required
    amplification by `7930` (`6410 → 14340`, `> 2×` initial value) for five-body
    and `8150` (`8285 → 16435`) for six-body, while reducing scaled traces by
    `2124` (`3348 → 1224`) and `2709` (`3865 → 1156`) (`qou-nmuz`). -/
theorem borromean_cache_amplification_and_trace_shifts :
    amplificationShiftHundredths 14340 6410 = 7930 ∧
    amplificationShiftHundredths 16435 8285 = 8150 ∧
    traceReductionThousandths 3348 1224 = 2124 ∧
    traceReductionThousandths 3865 1156 = 2709 := by
  dsimp [amplificationShiftHundredths, traceReductionThousandths]
  have h1 : (14340 : Int) - 6410 = 7930 := by omega
  have h2 : (16435 : Int) - 8285 = 8150 := by omega
  have h3 : (3348 : Int) - 1224 = 2124 := by omega
  have h4 : (3865 : Int) - 1156 = 2709 := by omega
  exact ⟨h1, h2, h3, h4⟩

/-- In the saturation mechanism probe, flipping `2` light-anchor assertions from
    failing to passing while `2` lithium-pin assertions flip from passing to
    failing conserves the total red assertion count at `3` (`qou-nmuz`). -/
theorem saturation_probe_red_count_invariant :
    saturationProbeRedCount 2 0 1 = 3 ∧
    saturationProbeRedCount 0 2 1 = 3 ∧
    ∀ (k s : Int), saturationProbeRedCount k 0 s = saturationProbeRedCount 0 k s := by
  dsimp [saturationProbeRedCount]
  have h1 : (2 : Int) + 0 + 1 = 3 := by omega
  have h2 : (0 : Int) + 2 + 1 = 3 := by omega
  refine ⟨h1, h2, ?_⟩
  intro k s
  omega

/-- Under the environment skip-guard (`32485` ms vs `408402` ms full run),
    execution time drops by more than `12×` (`margin = 18582` ms `> 0`), and the
    skip-aware verdict code (`2`) strictly separates a skipped guard from a
    numerical failure (`0`) (`qou-nz8e`). -/
theorem dtype_benchmark_skip_speedup_and_verdict_separation :
    benchmarkSkipDurationMargin 408402 12 32485 = 18582 ∧
    benchmarkSkipDurationMargin 408402 12 32485 > 0 ∧
    skipAwareVerdictCode false false = 2 ∧
    conflatedVerdictCode false false = 0 ∧
    skipAwareVerdictCode false false ≠ conflatedVerdictCode false false := by
  dsimp [benchmarkSkipDurationMargin, skipAwareVerdictCode, conflatedVerdictCode]
  have h1 : (408402 : Int) - 12 * 32485 = 18582 := by omega
  have h2 : (408402 : Int) - 12 * 32485 > 0 := by omega
  have h3 : (2 : Int) = 2 := rfl
  have h4 : (0 : Int) = 0 := rfl
  have h5 : (2 : Int) ≠ 0 := by omega
  exact ⟨h1, h2, h3, h4, h5⟩

end QOU.MassTheory.BorromeanCacheConsumerShiftAndNumpyDtypeSkipGuard
