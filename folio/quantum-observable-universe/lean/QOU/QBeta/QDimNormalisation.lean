import Mathlib.Algebra.BigOperators.Field
import QOU.Mathlib.BallotNumbers
import QOU.QBeta.TemperleyLiebTower
import QOU.QBeta.TwoRowNormalisation

/-!
# The `q`-dimension normalisation `[2]_qⁿ = Σ_j m_j(n) [n − 2j + 1]_q`

**Bean `qou-0cyu` item G2.** The `q`-dimension of `V^⊗n` for the 2-dimensional
`V`, decomposed over its two-row isotypic pieces. It is what makes the closed
form `y₍ₙ₋ₖ,ₖ₎ = [n−2k+1]_q / [2]_qⁿ` normalise — i.e. what makes `tr_M(1) = 1`
hold — at every strand count rather than at the two that were checked by hand.

## Status: general `n` PROVED — this file's own header said otherwise

`qdim_normalisation_general` below states and proves
`Σ_k m_k(n)·[n+1−2k]_q = [2]_qⁿ` for **every** `n`, sorry-free.

🛑 **Correction, recorded rather than quietly fixed.** Until 2026-09-07 this
header read:

> `n = 3, 4, 5, 6` proved; general `n` open, with the recipe fixed … the general
> statement is **not** written down here, because writing it without a proof
> would either need a `sorry` or would be a claim the file does not support.

That was true when written and **stale by the time it was read.**
`QOU.QBeta.TwoRowNormalisation.levelSum_eq_one` (bean `qou-f1qs`) proves
`Σ_λ dim_λ · y_λ = 1` at general `n`, sorry-free — and that *is* this statement
divided by `[2]_qⁿ`. The open item had already been closed in a sibling module,
under a different name, by a different route from the one this header proposed.
Nothing here was wrong about the mathematics; the file did not know its own gap
had been filled.

**Two things to take from it, neither about q-integers.** A `## Status` note is a
*dated measurement*, not a standing fact — AGENTS.md says exactly this ("the
source file's `## Status` … notes are **not authoritative**: the corpus is the
source of truth"), and this file is a worked instance of the cost. And the reason
it went unnoticed is a **naming split**: one identity, called `levelSum` there and
`qdim_normalisation` here, so a grep for either name finds neither the other nor
the overlap.

So the general statement below is a **derivation from prior art, not a new
result.** What it adds is that the identity now exists in the `[2]_qⁿ = Σ …` form
this file is named for, and that the ℤ-valued `Mathlib.BallotNumbers.ballot` is
tied to the `R`-valued `TwoRowNormalisation.ballot` — two definitions of the same
numbers that nothing previously connected, so no lemma about either transferred
to the other.

## The route proposed here, and not the one taken

Kept, because it is correct and may be wanted at a different index. Writing the
summand with **natural subtraction** as `qint q (n + 1 - 2*j)` makes the tail
vanish on its own:

* `2j ≤ n` — the index is `n − 2j + 1`, the intended one;
* `2j = n + 1` — the index truncates to `0`, and `qint q 0 = 0` (`qint_zero`);
  the coefficient `m_j(n)` is *also* zero here, by `ballot_boundary_zero`;
* `2j > n + 1` — the index truncates to `0` again.

So the sum may run over all of `Finset.range (n+1)` with **no guard and no
`⌊n/2⌋`**. `TwoRowNormalisation.levelSum` uses exactly this indexing, for exactly
this reason, arrived at independently — and the three ingredients named here are
the ones `levelSum_succ` in fact consumes:

* `TemperleyLiebTower.qint_three_term` — `[m+2] + [m] = [2]·[m+1]`;
* the Pascal step `m_{j+1}(n+1) = m_{j+1}(n) + m_j(n)`, as
  `Mathlib.BallotNumbers.ballot_succ_succ` in ℤ and `ballot_pascal` in `R`;
* the boundary vanishing, as `ballot_eq_zero_of_two_mul_eq_succ`.
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

section GeneralN

/-! ### The general-`n` normalisation, in the form this file is named for

Both statements below are one rewrite away from
`TwoRowNormalisation.levelSum_eq_one`; neither is new mathematics. They exist
because `levelSum_eq_one` is stated as `Σ_λ dim_λ · y_λ = 1` — the weights
*already divided* by `[2]_qⁿ` — and the `q`-dimension count is the same identity
with the denominator cleared. A reader looking for `[2]_qⁿ = Σ …` did not find
it, which is how this file came to declare it open.
-/

variable {R : Type*} [Field R]

/-- **The two `ballot` definitions agree**, `((m_k(n) : ℤ) : R) = m_k(n)`.

`QOU.Mathlib.ballot` is ℤ-valued, because it is squared and compared against
`catalan`. `QOU.QBeta.TwoRowNormalisation.ballot` is `R`-valued, because it is
multiplied by q-integers and carrying it in ℕ breaks Pascal at the boundary (see
that file's header for the worked failure). The two bodies are syntactically the
same recursion in different rings — and nothing connected them, so every lemma
proved about one said nothing whatever about the other. -/
theorem ballot_cast (n k : ℕ) :
    ((ballot n k : ℤ) : R) = TwoRowNormalisation.ballot n k := by
  cases k with
  | zero => simp [TwoRowNormalisation.ballot]
  | succ j =>
      simp only [ballot_succ, TwoRowNormalisation.ballot]
      push_cast
      ring

/-- **`[2]_qⁿ = Σ_k m_k(n) · [n+1−2k]_q`, at every `n`.**

The `q`-dimension of `V^⊗n` for the two-dimensional `V`, split over its two-row
isotypic pieces: the left side is `(dim_q V)ⁿ` and each right-hand term is the
multiplicity `m_k(n)` of the shape `(n−k, k)` times that block's `q`-dimension
`[n−2k+1]_q`.

The sum runs over all of `range (n+1)` with no `⌊n/2⌋` guard: past the last real
shape the ℕ subtraction truncates the index to `0` and `qint q 0 = 0`, and at the
single boundary index `2k = n+1` the *multiplicity* vanishes instead. Two
different reasons, one uniform range — see the header.

Hypotheses are the standing q-integer non-degeneracies: `q ≠ 0`, `q ≠ q⁻¹` (else
`[m]_q` is `0/0`), `q ≠ −q⁻¹` (else `[2]_q = 0`). All three hold at the proton pin
`q₀ ≈ 1.10998` with room. -/
theorem qdim_normalisation_general (q : R) (hq : q ≠ 0) (hq' : q - q⁻¹ ≠ 0)
    (hs : q + q⁻¹ ≠ 0) (n : ℕ) :
    ∑ k ∈ Finset.range (n + 1),
        TwoRowNormalisation.ballot n k * qint q (n + 1 - 2 * k) = (q + q⁻¹) ^ n := by
  have h := TwoRowNormalisation.levelSum_eq_one q hq hq' hs n
  unfold TwoRowNormalisation.levelSum at h
  have hstep : ∀ k ∈ Finset.range (n + 1),
      TwoRowNormalisation.ballot n k * yw q n (n + 1 - 2 * k)
        = TwoRowNormalisation.ballot n k * qint q (n + 1 - 2 * k) / (q + q⁻¹) ^ n := by
    intro k _
    unfold yw
    rw [mul_div_assoc]
  rw [Finset.sum_congr rfl hstep, ← Finset.sum_div,
    div_eq_iff (pow_ne_zero n hs), one_mul] at h
  exact h

/-- The same identity with the **ℤ-valued** ballot numbers of
`Mathlib.BallotNumbers` cast into `R`.

Worth stating separately rather than leaving to the reader: it is the form whose
coefficients are the ones `ballot_sq_sum_catalan` is about, so it is the only
form in which the `q`-dimension count and the Catalan count are visibly about the
same multiplicities. -/
theorem qdim_normalisation_general_int (q : R) (hq : q ≠ 0) (hq' : q - q⁻¹ ≠ 0)
    (hs : q + q⁻¹ ≠ 0) (n : ℕ) :
    ∑ k ∈ Finset.range (n + 1),
        ((ballot n k : ℤ) : R) * qint q (n + 1 - 2 * k) = (q + q⁻¹) ^ n := by
  rw [Finset.sum_congr rfl (fun k _ => by rw [ballot_cast])]
  exact qdim_normalisation_general q hq hq' hs n

/-- **The `n = 5` small case is an instance of the general one**, not an
independent check.

Recorded so the small cases below are not read as the evidence for the general
statement. They predate it; they now corroborate it. -/
theorem five_is_instance (q : R) (hq : q ≠ 0) (hq' : q - q⁻¹ ≠ 0)
    (hs : q + q⁻¹ ≠ 0) :
    ∑ k ∈ Finset.range 6,
        ((ballot 5 k : ℤ) : R) * qint q (6 - 2 * k) = (q + q⁻¹) ^ 5 :=
  qdim_normalisation_general_int q hq hq' hs 5

end GeneralN

end QOU.QBeta.QDimNormalisation
