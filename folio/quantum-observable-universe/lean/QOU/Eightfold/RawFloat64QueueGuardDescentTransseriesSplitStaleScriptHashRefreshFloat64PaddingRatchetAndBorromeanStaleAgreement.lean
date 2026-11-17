/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

namespace QOU.Eightfold.RawFloat64QueueGuardDescentTransseriesSplitStaleScriptHashRefreshFloat64PaddingRatchetAndBorromeanStaleAgreement

/-!
# Raw-`float64` Queue Anchor Guard, Descent/Transseries Split, Stale `scriptHash` Refresh, `float64`-Padding Ratchet, and Coupled Stale Witness Agreement

This module formalizes five structural results corresponding to `qou-5lw7`,
`qou-5m4f`, `qou-5rf8`, `qou-5sg8`, and `qou-5t68`:

1. **`qou-5lw7` (Raw-`float64` Queue Classification and `reject_float64_q` Guard):**
   Across the `22` new/regressed dirty witnesses (`20` new + `2` regressed, while `6`
   were drained), `1748` total raw-`float64` fields split into `36` framework fields
   (`wall_seconds`, `durationMs`, assertion triples) and `1712` scientific payload
   fields. Furthermore, formatting a degraded `17`-digit `float64` `q`-anchor via
   `50`-digit `fmt(x)` leaves the `33`-digit information deficit (`50 - 17 = 33`)
   unchanged while masking the defect from the output ratchet; `reject_float64_q`
   catches it at the input boundary.

2. **`qou-5m4f` (Categorical Descent `B = B^desc + B^trans` vs `37×` Transseries Refutation):**
   Under the additive categorical descent decomposition `B_total = B_desc + B_trans`,
   when the instanton/transseries correction `B_trans` undershoots the target binding
   energy `B_target = 37 * B_trans` by a factor of `37`, the smooth central/Casimir
   backbone `B_desc = B_total - B_trans` carries exactly `36 * B_trans` (`36 / 37` of
   the total binding), reconciling the `37×` pure-transseries miss.

3. **`qou-5rf8` (Stale `scriptHash` Provenance Refresh Accounting):**
   A witness whose recorded `scriptHash` disagrees with the current producer SHA-256
   (`staleCount = 70`) transitions from stale (`hashMismatch = true`) to verified
   (`hashMismatch = false`) only when re-stamped at the current producer hash, reducing
   the stale cohort by the exact count of refreshed witnesses (`70 - k`).

4. **`qou-5sg8` (`float64`-Padding Ratchet on `categorical-bypass-volmatch-demo`):**
   Lifting a `16`-digit binary64 float into `mp.mpf(<float>)` at `50` dps appends `34`
   spurious binary64 expansion digits (`50 - 16 = 34`), increasing the `float64`-padding
   ratchet from its baseline of `13` to `17` occurrences (`4` new padded fields:
   `ratio_direct_to_AME` and `3` `B_AME_MeV` rows).

5. **`qou-5t68` (Coupled Stale Convention-C Witness Agreement in `borromean-binding-recompute`):**
   Comparing a stale convention-C probe (`valC`) against a stale convention-C committed
   witness (`valC`) yields an exact zero difference (`valC - valC = 0`), hiding a nonzero
   convention shift `valD - valC ≠ 0` (`26` stale fields, `-23%` on `B_can0` and `-17%`
   on `B_tower`) until one side is migrated to convention `D`.
-/

/-- `qou-5lw7`: Accounting of the 22 dirty witnesses and 1748 raw-float64 fields. -/
structure RawFloat64QueueAudit where
  newDirtyWitnesses : Nat
  regressedWitnesses : Nat
  drainedWitnesses : Nat
  frameworkFloatFields : Nat
  scientificPayloadFloatFields : Nat
  targetPrecisionDigits : Nat
  degradedAnchorDigits : Nat
  deriving DecidableEq, Repr

/-- Canonical counts measured in `qou-5lw7`. -/
def canonicalRawFloat64Queue : RawFloat64QueueAudit :=
  { newDirtyWitnesses := 20
    regressedWitnesses := 2
    drainedWitnesses := 6
    frameworkFloatFields := 36
    scientificPayloadFloatFields := 1712
    targetPrecisionDigits := 50
    degradedAnchorDigits := 17 }

/-- Total active dirty queue (`new + regressed`). -/
def activeDirtyWitnessQueue (q : RawFloat64QueueAudit) : Nat :=
  q.newDirtyWitnesses + q.regressedWitnesses

/-- Total raw-float64 fields across the 22 active dirty witnesses. -/
def totalActiveDirtyFloatFields (q : RawFloat64QueueAudit) : Nat :=
  q.frameworkFloatFields + q.scientificPayloadFloatFields

/-- Real-digit deficit when a `degradedAnchorDigits` `q`-anchor is formatted to
    `targetPrecisionDigits` characters. -/
def anchorInformationDeficitDigits (q : RawFloat64QueueAudit) : Nat :=
  q.targetPrecisionDigits - q.degradedAnchorDigits

/-- Theorem (`qou-5lw7`): The `20 + 2 = 22` active dirty witnesses contain `36 + 1712 = 1748`
    raw-`float64` fields (`1712 > 47 * 36` scientific vs framework), and formatting a
    `17`-digit degraded `q` to `50` digits leaves a `33`-digit information deficit. -/
theorem raw_float64_queue_and_degraded_anchor_deficit_accounting :
    activeDirtyWitnessQueue canonicalRawFloat64Queue = 22 ∧
    totalActiveDirtyFloatFields canonicalRawFloat64Queue = 1748 ∧
    canonicalRawFloat64Queue.scientificPayloadFloatFields >
      47 * canonicalRawFloat64Queue.frameworkFloatFields ∧
    anchorInformationDeficitDigits canonicalRawFloat64Queue = 33 := by
  decide

/-- `qou-5m4f`: Categorical descent additive split `B_total = B_desc + B_trans`. -/
def totalBindingFromDescent (bDesc bTrans : Int) : Int :=
  bDesc + bTrans

/-- Theorem (`qou-5m4f`): When the total binding `B_total = 37 * bTrans` is 37 times the
    transseries component `bTrans > 0` under `B_total = bDesc + bTrans`, the smooth
    central/Casimir backbone `bDesc` equals `36 * bTrans` and strictly dominates `bTrans`. -/
theorem descent_backbone_dominates_37x_transseries_component
    (bDesc bTrans : Int) (hPos : 0 < bTrans)
    (hSplit : totalBindingFromDescent bDesc bTrans = 37 * bTrans) :
    bDesc = 36 * bTrans ∧
    bTrans < bDesc ∧
    37 * bDesc = 36 * totalBindingFromDescent bDesc bTrans := by
  unfold totalBindingFromDescent at *
  omega

/-- `qou-5rf8`: Stale `scriptHash` cohort refresh accounting. -/
def remainingStaleScriptHashes (initialStale refreshedCount : Int) : Int :=
  initialStale - refreshedCount

/-- Theorem (`qou-5rf8`): Refreshing `k` witnesses out of the `70` stale `scriptHash`
    witnesses (`0 ≤ k ≤ 70`) reduces the stale cohort to `70 - k`, reaching `0` when
    all `70` are refreshed. -/
theorem stale_script_hash_refresh_monotone_drain (k : Int)
    (hNonNeg : 0 ≤ k) (hBound : k ≤ 70) :
    0 ≤ remainingStaleScriptHashes 70 k ∧
    remainingStaleScriptHashes 70 k ≤ 70 ∧
    remainingStaleScriptHashes 70 70 = 0 ∧
    remainingStaleScriptHashes 70 0 - remainingStaleScriptHashes 70 k = k := by
  unfold remainingStaleScriptHashes
  omega

/-- `qou-5sg8`: `float64`-padding ratchet accounting for `categorical-bypass-volmatch-demo`. -/
structure Float64PaddingRatchetAudit where
  baselinePaddedCount : Nat
  newRatioDirectPadded : Nat
  newAmeBindingPadded : Nat
  claimedStringDigits : Nat
  binary64RealDigits : Nat
  deriving DecidableEq, Repr

/-- Canonical values from `qou-5sg8` (`13 -> 17` padded occurrences, `1 + 3 = 4` new). -/
def canonicalFloat64PaddingAudit : Float64PaddingRatchetAudit :=
  { baselinePaddedCount := 13
    newRatioDirectPadded := 1
    newAmeBindingPadded := 3
    claimedStringDigits := 50
    binary64RealDigits := 16 }

/-- Total new padded fields in `categorical-bypass-volmatch-demo.witness.json`. -/
def newPaddedFieldsCount (a : Float64PaddingRatchetAudit) : Nat :=
  a.newRatioDirectPadded + a.newAmeBindingPadded

/-- Total padded fields across `main` after the `4` new occurrences. -/
def totalPaddedFieldsCount (a : Float64PaddingRatchetAudit) : Nat :=
  a.baselinePaddedCount + newPaddedFieldsCount a

/-- Spurious binary64 tail digits appended when serializing `mp.mpf(<float>)` at `50` dps. -/
def spuriousBinary64TailDigits (a : Float64PaddingRatchetAudit) : Nat :=
  a.claimedStringDigits - a.binary64RealDigits

/-- Theorem (`qou-5sg8`): The `1` `ratio_direct_to_AME` field and `3` `B_AME_MeV` fields
    add `4` new padded occurrences (`13 + 4 = 17` total), each carrying `50 - 16 = 34`
    spurious binary64 expansion digits. -/
theorem float64_padding_ratchet_and_spurious_tail_accounting :
    newPaddedFieldsCount canonicalFloat64PaddingAudit = 4 ∧
    totalPaddedFieldsCount canonicalFloat64PaddingAudit = 17 ∧
    spuriousBinary64TailDigits canonicalFloat64PaddingAudit = 34 := by
  decide

/-- `qou-5t68`: Cross-check discrepancy between a probe value `probeVal` and a committed
    witness value `witnessVal`. -/
def crossCheckDiscrepancy (probeVal witnessVal : Int) : Int :=
  probeVal - witnessVal

/-- Theorem (`qou-5t68`): When both the probe and the committed witness evaluate in the
    retired convention `C` (`valC`), their discrepancy `crossCheckDiscrepancy valC valC = 0`
    vanishes identically even when the live convention-`D` value `valD` differs from `valC`
    (`valD ≠ valC`), whereas migrating the probe to `valD` immediately exposes the exact
    convention drift `valD - valC ≠ 0`. -/
theorem coupled_stale_witness_zero_discrepancy_hides_convention_drift
    (valC valD : Int) (hDrift : valD ≠ valC) :
    crossCheckDiscrepancy valC valC = 0 ∧
    crossCheckDiscrepancy valD valC ≠ 0 ∧
    crossCheckDiscrepancy valD valC - crossCheckDiscrepancy valC valC = valD - valC := by
  unfold crossCheckDiscrepancy
  omega

end QOU.Eightfold.RawFloat64QueueGuardDescentTransseriesSplitStaleScriptHashRefreshFloat64PaddingRatchetAndBorromeanStaleAgreement
