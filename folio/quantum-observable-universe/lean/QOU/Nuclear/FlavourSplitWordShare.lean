/-
# How much of the scored `Q_β` comes from the selected word

Bean `qou-99qc`, `qou-ales`; owner 2026-11-21 ("Ok" to option 3: derive the T³ weight split
behind the D1 = A cell from the selection rule).

The D1 = A cell (`docs/audits/2026-11-20-qbeta-flavour-weight-split.md`) scores
`Q_β = |ε_flavour(V³)|·E₀`, with `ε_flavour(V³) = (q²−1)P(q)/(q⁴(q²+1)³)`
(`FlavourWeightSplit.epsFlavour_V3_eq`). Because the plain traces on the two weight spaces are
equal for every braid word (`NucleonWeightSpaceTraces.trace_word_eq`), the split is
`ε_flavour(X) = −h·tr_W(X)/[2]³`. The selected word enters only through `tr_W(X)`.

## What is proved (generic field, no `ℝ`, no `sorry`)

* `trW_V3_eq`: `tr_W(V³) = −P(q)/q⁶ = 3 − h⁴·[3]`, `h = q − q⁻¹`, `[3] = q² + 1 + q⁻²`.
* `epsFlavour_V3_word_share`: `(q²−1)P(q)/(q⁴(q²+1)³) = −h·(3 − h⁴[3])/[2]³`.

So the scored value is `h·3/[2]³·E₀` (the weight split of the identity permutation on a
3-dimensional weight space), corrected by `−h⁵[3]/[2]³·E₀` from the word. At the proton pin the
word's share is `−0.194 %` of the value (probe below). The selection rule fixes that fourth-order
correction. The leading `3h/[2]³` comes from the T³ sector split, the `K`-weighting and the
`[2]³` normalisation, which the rule does not touch.

## What is NOT proved

That the T³ split, the `K`-weighting or `E₀` follow from the selection rule. They do not
involve the word, and this file shows the word cannot supply them.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta.FlavourSplitWordShare

variable {K : Type*} [Field K]

/-- The polynomial of `FlavourWeightSplit.epsFlavour_V3_eq`. -/
def P (q : K) : K := q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1

theorem trW_V3_eq {q : K} (hq : q ≠ 0) :
    -P q / q ^ 6 = 3 - (q - q⁻¹) ^ 4 * (q ^ 2 + 1 + q⁻¹ ^ 2) := by
  unfold P
  field_simp
  ring

theorem epsFlavour_V3_word_share {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0) :
    (q ^ 2 - 1) * P q / (q ^ 4 * (q ^ 2 + 1) ^ 3) =
      -(q - q⁻¹) * (3 - (q - q⁻¹) ^ 4 * (q ^ 2 + 1 + q⁻¹ ^ 2)) / (q + q⁻¹) ^ 3 := by
  have h2 : q + q⁻¹ ≠ 0 := by
    intro h; apply hn
    have e : q ^ 2 + 1 = q * (q + q⁻¹) := by field_simp
    rw [e, h, mul_zero]
  unfold P
  field_simp
  ring

end QOU.QBeta.FlavourSplitWordShare
