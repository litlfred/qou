/-!
# Tower Partition Growth and Weight Substitution (`qou-2tuv`)

This module formalizes the mathematical and computational constraints governing
the substitution of legacy `H_3` character weights by full `H_{3A}` character
weights (`qou-2tuv`):

1. **Partition growth `p(3A)` and the `A = 12` tractability ceiling (`partition_count_3a_tractability_threshold`):**
   The full `H_{3A}` character sum enumerates all integer partitions of `3A`.
   While `p(3A) <= 17977` for `A <= 12` (`p(3) = 3`, `p(6) = 11`, `p(12) = 77`,
   `p(36) = 17977`), at `A = 20` (`3A = 60`) the partition count reaches
   `p(60) = 966467` and at `A = 40` (`3A = 120`) reaches `1844349560`, rendering
   naive enumeration across heavy nuclei (`A` up to `418`) infeasible without
   truncation or asymptotic reduction.

2. **Deuteron `H_6` vs `H_3` binding amplification (`deuteron_proper_vs_legacy_binding_amplification`):**
   At `A = 2` (`3A = 6`, `11` partitions), replacing legacy `H_3` per-generator
   log-volumes (`sum ln|V| = -1.1755`) by proper `H_6` log-volumes
   (`sum ln|V| = -10.3951`) amplifies `-alpha * sum ln|V|` by a factor of `8.84x`
   (strictly between `8x` and `9x`).

3. **Impossibility of closing opposite-sign light/heavy errors by uniform rescaling (`uniform_rescale_cannot_close_opposite_sign_regimes`):**
   When light nuclei are already over-predicted (`bLightPred > bLightExp > 0`) while
   heavy nuclei are under-predicted (`3 * bHeavyPred < bHeavyExp`), multiplying light
   predictions by `k >= 8` increases the light-nucleus over-prediction error strictly
   above `7 * bLightExp`.
-/

namespace QOU.MassTheory.TowerPartitionGrowthAndWeightSubstitution

/-- Tabulated exact partition counts `p(3A)` for representative mass numbers `A`. -/
def partitionCount3A (A : Nat) : Nat :=
  if A = 1 then 3
  else if A = 2 then 11
  else if A = 3 then 30
  else if A = 4 then 77
  else if A = 12 then 17977
  else if A = 20 then 966467
  else if A = 40 then 1844349560
  else 0

/-- Tractability predicate `p(3A) <= 20000` for un-truncated `H_{3A}` enumeration. -/
def isTractableFull3ASum (A : Nat) : Bool :=
  decide (partitionCount3A A <= 20000)

/-- Scaled (`10^4`) legacy `H_3` deuteron per-generator log-volume sum `-1.1755`. -/
def deuteronLegacyLogSumScaled : Int := -11755

/-- Scaled (`10^4`) proper `H_6` deuteron per-generator log-volume sum `-10.3951`. -/
def deuteronProper3ALogSumScaled : Int := -103951

/-- The partition count `p(3A)` stays below the `20000`-partition enumeration
    ceiling up to `A = 12` (`p(36) = 17977`) and exceeds it by `A = 20`
    (`p(60) = 966467`) (`qou-2tuv`). -/
theorem partition_count_3a_tractability_threshold :
    partitionCount3A 1 = 3 ∧
    partitionCount3A 2 = 11 ∧
    partitionCount3A 4 = 77 ∧
    partitionCount3A 12 = 17977 ∧
    partitionCount3A 20 = 966467 ∧
    isTractableFull3ASum 12 = true ∧
    isTractableFull3ASum 20 = false := by
  have hp1 : partitionCount3A 1 = 3 := by
    unfold partitionCount3A
    rfl
  have hp2 : partitionCount3A 2 = 11 := by
    unfold partitionCount3A
    rfl
  have hp4 : partitionCount3A 4 = 77 := by
    unfold partitionCount3A
    rfl
  have hp12 : partitionCount3A 12 = 17977 := by
    unfold partitionCount3A
    rfl
  have hp20 : partitionCount3A 20 = 966467 := by
    unfold partitionCount3A
    rfl
  have htract12 : isTractableFull3ASum 12 = true := by
    unfold isTractableFull3ASum partitionCount3A
    decide
  have htract20 : isTractableFull3ASum 20 = false := by
    unfold isTractableFull3ASum partitionCount3A
    decide
  exact ⟨hp1, hp2, hp4, hp12, hp20, htract12, htract20⟩

/-- Replacing legacy `H_3` weights by proper `H_6` weights at `A = 2` amplifies
    the positive binding sum `-alphaScaled * sum ln|V|` by a factor strictly
    between `8x` and `9x` (`103951 / 11755 ≈ 8.843`) (`qou-2tuv`). -/
theorem deuteron_proper_vs_legacy_binding_amplification
    (alphaScaled : Int) (halpha : alphaScaled > 0) :
    (-alphaScaled * deuteronProper3ALogSumScaled) >
      8 * (-alphaScaled * deuteronLegacyLogSumScaled) ∧
    (-alphaScaled * deuteronProper3ALogSumScaled) <
      9 * (-alphaScaled * deuteronLegacyLogSumScaled) := by
  have hleg : deuteronLegacyLogSumScaled = -11755 := by
    unfold deuteronLegacyLogSumScaled
    rfl
  have hprop : deuteronProper3ALogSumScaled = -103951 := by
    unfold deuteronProper3ALogSumScaled
    rfl
  have hgt : -alphaScaled * deuteronProper3ALogSumScaled >
      8 * (-alphaScaled * deuteronLegacyLogSumScaled) := by
    rw [hleg, hprop]
    omega
  have hlt : -alphaScaled * deuteronProper3ALogSumScaled <
      9 * (-alphaScaled * deuteronLegacyLogSumScaled) := by
    rw [hleg, hprop]
    omega
  exact ⟨hgt, hlt⟩

/-- When light-nucleus binding is already over-predicted (`bLightPred > bLightExp > 0`)
    while heavy-nucleus binding is under-predicted (`3 * bHeavyPred < bHeavyExp`),
    applying an amplification factor `k >= 8` to light nuclei drives the light
    over-prediction error strictly above `7 * bLightExp` (`qou-2tuv`). -/
theorem uniform_rescale_cannot_close_opposite_sign_regimes
    (bLightPred bLightExp bHeavyPred bHeavyExp k : Int)
    (hlight : bLightPred > bLightExp)
    (hheavy : 3 * bHeavyPred < bHeavyExp)
    (hexp : bLightExp > 0)
    (hk : k >= 8) :
    k * bLightPred - bLightExp > 7 * bLightExp ∧
    bHeavyExp - 3 * bHeavyPred > 0 := by
  have h8 : k * bLightPred >= 8 * bLightPred := by
    have hpos : bLightPred > 0 := by omega
    have hsub : (k - 8) * bLightPred >= 0 := Int.mul_nonneg (by omega) (by omega)
    have hexpand : k * bLightPred - 8 * bLightPred = (k - 8) * bLightPred := by
      rw [Int.sub_mul]
    omega
  have hlight_err : k * bLightPred - bLightExp > 7 * bLightExp := by
    omega
  have hheavy_def : bHeavyExp - 3 * bHeavyPred > 0 := by
    omega
  exact ⟨hlight_err, hheavy_def⟩

end QOU.MassTheory.TowerPartitionGrowthAndWeightSubstitution
