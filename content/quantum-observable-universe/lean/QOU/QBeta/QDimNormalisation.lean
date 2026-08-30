import QOU.Mathlib.BallotNumbers
import QOU.QBeta.TemperleyLiebTower

/-!
# The `q`-dimension normalisation `[2]_qⁿ = Σ_j m_j(n) [n − 2j + 1]_q`

**Bean `qou-0cyu` item G2.** The `q`-dimension of `V^⊗n` for the 2-dimensional
`V`, decomposed over its two-row isotypic pieces. It is what makes the closed
form `y₍ₙ₋ₖ,ₖ₎ = [n−2k+1]_q / [2]_qⁿ` normalise — i.e. what makes `tr_M(1) = 1`
hold — at every strand count rather than at the two that were checked by hand.

## Status: `n = 3, 4, 5, 6` proved; general `n` open, with the recipe fixed

Both ingredients of the general induction are proved:

* `TemperleyLiebTower.qint_three_term` — `[m+2] + [m] = [2]·[m+1]`;
* `Mathlib.BallotNumbers.ballot_succ_succ` — `m_{j+1}(n+1) = m_{j+1}(n) + m_j(n)`;
* `Mathlib.BallotNumbers.ballot_boundary_zero` — `m_{j+1}(2j+1) = 0`, which is
  what closes the even case.

and `qou-0cyu` records the assembly step by step. What is *not* done is the
`Finset` bookkeeping, and this file is deliberate about not pretending
otherwise: the general statement is **not** written down here, because writing
it without a proof would either need a `sorry` or would be a claim the file does
not support.

## The indexing trick that makes the general form tractable

Worth recording, because it removes what looked like the main obstacle. Writing
the summand with **natural subtraction** as `qint q (n + 1 - 2*j)` makes the
tail vanish automatically:

* `2j ≤ n` — the index is `n − 2j + 1`, the intended one;
* `2j = n + 1` — the index truncates to `0`, and `qint q 0 = 0` (`qint_zero`);
  the coefficient `m_j(n)` is *also* zero here, by `ballot_boundary_zero`;
* `2j > n + 1` — the index truncates to `0` again.

So the sum may run over all of `Finset.range (n+1)` with **no guard and no
`⌊n/2⌋`**, which was the fiddly part. The remaining work is reindexing one half
of the split sum by `j ↦ j+1`, not case-splitting on parity.
-/

namespace QOU.QBeta.QDimNormalisation

open QOU.Mathlib QOU.QBeta.TemperleyLiebTower

section Helpers

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- `[0]_q = 0`. No hypothesis: the numerator is `1 − 1`. This is what lets the
tail of the sum vanish under natural subtraction. -/
@[simp] theorem qint_zero (q : R) : qint q 0 = 0 := by
  simp [qint]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- `[1]_q = 1`, given `q − q⁻¹ ≠ 0` (i.e. `q² ≠ 1`). At the physical pin
`q₀ = 1.10997858…` this holds with room: `q₀ − q₀⁻¹ = 0.2090603`. -/
@[simp] theorem qint_one (q : R) (h : q - q⁻¹ ≠ 0) : qint q 1 = 1 := by
  unfold qint
  simp only [pow_one]
  exact div_self h

/-- `[2]_q = q + q⁻¹`, the Temperley–Lieb loop parameter `δ`. -/
theorem qint_two (q : R) (h : q - q⁻¹ ≠ 0) : qint q 2 = q + q⁻¹ := by
  unfold qint
  rw [div_eq_iff h]
  ring

end Helpers

section SmallCases

variable {R : Type*} [Field R]

/-! ### The normalisation at `n = 5` and `n = 6`

`TemperleyLiebTower` proved `n = 3` and `n = 4`. These extend verified coverage
to the strand counts `qou-8iru` measured, with the ballot coefficients taken
from `BallotNumbers` rather than from a table:

    n = 5:  m = (1, 4, 5)        [2]⁵ = [6] + 4[4] + 5[2]
    n = 6:  m = (1, 5, 9, 5)     [2]⁶ = [7] + 5[5] + 9[3] + 5[1]

Written with the `q`-integers expanded so `field_simp` supplies `q · q⁻¹ = 1`
and `ring` closes them, matching the idiom of the `n = 3, 4` cases. -/

/-- **`[2]⁵ = [6] + 4[4] + 5[2]`.** Coefficients `1, 4, 5` are
`ballot 5 0, 1, 2` (`ballot_values_five`). -/
theorem qdim_normalisation_five (q : R) (hq : q ≠ 0) :
    (q + q⁻¹) ^ 5
      = (q ^ 5 + q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3 + q⁻¹ ^ 5)
        + 4 * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3)
        + 5 * (q + q⁻¹) := by
  field_simp
  ring

/-- **`[2]⁶ = [7] + 5[5] + 9[3] + 5[1]`.** Coefficients `1, 5, 9, 5` are
`ballot 6 0, 1, 2, 3`. -/
theorem qdim_normalisation_six (q : R) (hq : q ≠ 0) :
    (q + q⁻¹) ^ 6
      = (q ^ 6 + q ^ 4 + q ^ 2 + 1 + q⁻¹ ^ 2 + q⁻¹ ^ 4 + q⁻¹ ^ 6)
        + 5 * (q ^ 4 + q ^ 2 + 1 + q⁻¹ ^ 2 + q⁻¹ ^ 4)
        + 9 * (q ^ 2 + 1 + q⁻¹ ^ 2)
        + 5 * 1 := by
  field_simp
  ring

end SmallCases

section BallotAgreement

/-! ### The coefficients above are the ballot numbers, not a table

Each small case quotes its multiplicities as literals. These check them against
`BallotNumbers.ballot`, so a transcription slip in either place is caught. -/

theorem coeffs_five : ballot 5 0 = 1 ∧ ballot 5 1 = 4 ∧ ballot 5 2 = 5 :=
  ballot_values_five

theorem coeffs_six :
    ballot 6 0 = 1 ∧ ballot 6 1 = 5 ∧ ballot 6 2 = 9 ∧ ballot 6 3 = 5 := by
  refine ⟨rfl, ?_, ?_, ?_⟩ <;> decide

end BallotAgreement

end QOU.QBeta.QDimNormalisation
