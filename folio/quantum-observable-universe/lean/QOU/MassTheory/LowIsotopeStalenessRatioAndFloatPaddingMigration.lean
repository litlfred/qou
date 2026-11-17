/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Low-Isotope Witness Staleness Ratio and Float64-Padding Ratchet Migration

Formalizes the two quantitative findings of `qou-syit`:

1. **$24.8\times$ Headline Staleness of `unified-low-isotope-predictor.witness.json`**:
   - Between the committed witness (`commitSha 6949424f7a`) and a live re-run of the
     producer, the predicted deuteron binding magnitude moves from
     $|-10570.83|\text{ MeV} \approx 10571\text{ MeV}$ to $|-261780.85|\text{ MeV} \approx 261781\text{ MeV}$
     (strictly between $24\times$ and $25\times$, i.e. $24.8\times$ stale), and the
     triton binding magnitude moves from $14509\text{ MeV}$ to $340647\text{ MeV}$
     (strictly between $23\times$ and $24\times$).

2. **Promoting Unfixed `float64` Products to `mpf` Strings Migrates Fields into the Padding Ratchet**:
   - Before the character-closed-form string drain, the witness carried $33$ local and
     $24$ inherited raw `float64` fields ($57$ total).
   - Promoting $21$ inherited `float64` products (`float * mpf`) to 50-digit strings
     without removing the upstream `float(...)` casts reduces the raw `float64` count
     from $57$ to $36$ ($21$ local + $15$ inherited) while adding $21$ float64-padded
     strings, leaving the total count of 53-bit precision-contaminated fields invariant at $57$.
-/

namespace QOU.MassTheory.LowIsotopeStalenessRatioAndFloatPaddingMigration

/-- Total raw `float64` payload fields before string promotion (`local + inherited`). -/
def preMergeRawFloat64Fields (localFields inheritedFields : Int) : Int :=
  localFields + inheritedFields

/-- Remaining raw `float64` payload fields after promoting `promotedToPaddedStrings` fields. -/
def postMergeRawFloat64Fields (preTotal promotedToPaddedStrings : Int) : Int :=
  preTotal - promotedToPaddedStrings

/-- Total 53-bit precision-contaminated fields (`rawFloat64 + paddedStrings`). -/
def totalPrecisionContaminatedFields (rawFloat64Count paddedStringCount : Int) : Int :=
  rawFloat64Count + paddedStringCount

/-- Headline $24.8\times$ deuteron and $23.5\times$ triton staleness bounds (`qou-syit`):
    the live deuteron magnitude $261781\text{ MeV}$ lies strictly between $24\times$ and
    $25\times$ the committed value $10571\text{ MeV}$, and the live triton magnitude
    $340647\text{ MeV}$ lies strictly between $23\times$ and $24\times$ the committed
    value $14509\text{ MeV}$. -/
theorem deuteron_and_triton_binding_staleness_exceeds_23x
    (dCommittedMeV dLiveMeV tCommittedMeV tLiveMeV : Int)
    (hdc : dCommittedMeV = 10571) (hdl : dLiveMeV = 261781)
    (htc : tCommittedMeV = 14509) (htl : tLiveMeV = 340647) :
    24 * dCommittedMeV < dLiveMeV ∧
      dLiveMeV < 25 * dCommittedMeV ∧
      23 * tCommittedMeV < tLiveMeV ∧
      tLiveMeV < 24 * tCommittedMeV := by
  have hd1 : 24 * dCommittedMeV < dLiveMeV := by omega
  have hd2 : dLiveMeV < 25 * dCommittedMeV := by omega
  have ht1 : 23 * tCommittedMeV < tLiveMeV := by omega
  have ht2 : tLiveMeV < 24 * tCommittedMeV := by omega
  exact ⟨hd1, hd2, ht1, ht2⟩

/-- Conservation of 53-bit precision contamination under unfixed `float64` string
    promotion (`qou-syit`): promoting $21$ of the $33 + 24 = 57$ raw `float64` fields
    to `mpf` strings without fixing the `float64` multiplicands reduces raw `float64`
    fields to $36$ while leaving total precision-contaminated fields equal to $57$. -/
theorem unfixed_float64_promotion_migrates_raw_fields_to_padding_ratchet
    (preLocal preInherited promotedCount : Int)
    (hl : preLocal = 33) (hi : preInherited = 24) (hp : promotedCount = 21) :
    preMergeRawFloat64Fields preLocal preInherited = 57 ∧
      postMergeRawFloat64Fields (preMergeRawFloat64Fields preLocal preInherited) promotedCount = 36 ∧
      totalPrecisionContaminatedFields
        (postMergeRawFloat64Fields (preMergeRawFloat64Fields preLocal preInherited) promotedCount)
        promotedCount = preMergeRawFloat64Fields preLocal preInherited := by
  dsimp [preMergeRawFloat64Fields, postMergeRawFloat64Fields,
    totalPrecisionContaminatedFields]
  have hpre : preLocal + preInherited = 57 := by omega
  have hpost : preLocal + preInherited - promotedCount = 36 := by omega
  have hinv : preLocal + preInherited - promotedCount + promotedCount =
      preLocal + preInherited := by omega
  exact ⟨hpre, hpost, hinv⟩

end QOU.MassTheory.LowIsotopeStalenessRatioAndFloatPaddingMigration
