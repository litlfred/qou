import QOU.Mathlib.BallotNumbers
import QOU.Mathlib.SYTBranching2Row

/-!
# `QOU.Mathlib.TwoRowDimCatalan` — two-row Specht dimensions square-sum to `catalan n`

This file joins the two halves of the general-`n` corank statement, which were
already in the corpus but had never been put together:

* `SYTHookRows.dimHLF_pair` — the two-row hook-length dimension **is** the
  ballot number, `dimHLF [a,b] = C(a+b,b) − C(a+b,b−1)`, sorry-free.
* `BallotNumbers.ballot_sq_sum_catalan` — the ballot numbers square-sum to
  `catalan n`, sorry-free, general `n`.

Composing them gives

    Σ_{k ≤ ⌊n/2⌋} (dim S^{(n−k,k)})² = catalan n                (`dimHLF_two_row_sq_sum`)

the form the Wedderburn accounting needs — a statement about two-row Specht dimensions rather
than about binomial coefficients.

### 🛑 Read `dimHLF` as the FORMULA, and note what makes it a count

`dimHLF l := (sz l).factorial / prodHooks l` is the hook length **formula**, a quotient of
factorials; `numStandardYoungTableaux μ := Nat.card (StandardYoungTableau μ)` is the genuine
**count**.  The two are equal for every shape only by Frame–Robinson–Thrall, which is **absent
from Mathlib** and proved in this corpus only for `n ≤ 4` (by `decide`) plus `n = 5` — so at
general `n` nothing in *this* file, on its own, is about tableau counts.

For the **two-row** shapes appearing here they are nonetheless equal at general `n`:

    QOU.SchurWeyl.TwoRowSYTBallot.numSYT_twoRow_eq_dimHLF (m k) (h : k ≤ m) :
      (numStandardYoungTableaux (twoRow m k h) : ℤ) = (dimHLF [m, k] : ℕ)

sorry-free, no Frame–Robinson–Thrall — both sides were already identified with the same ballot
number, `dimHLF` by `dimHLF_two_row_eq_ballot` below and the count by `numSYT_twoRow_eq_ballot`.
**Cite that theorem** whenever the sum above is to be read as a statement about counts.

This paragraph previously asserted the counts reading flatly, which over-claimed: at the time it
was written the tie to any tableau count at general `n` did not exist in the corpus.  The theorem
it now cites supplies exactly that tie, so the reading is available — but it is a *composition*,
not something this file proves.

## Why this is the load-bearing step for `corank(n) = n! − catalan n`

The Markov-trace Gram form is diagonal in the Wedderburn basis with entries
proportional to `y_λ`, so its corank is `n!` minus the sum of `(dim V_λ)²` over
the blocks the trace can see. Under convention D the visible blocks are exactly
the partitions with `ℓ(λ) ≤ 2` (Wenzl level `r = 2`), whose dimensions are the
two-row Specht dimensions counted above. So

    dim radical = n! − Σ_{ℓ(λ) ≤ 2} (dim V_λ)² = n! − catalan n

for **every** `n`, superseding the four measured values `n = 3,4,5,6 →
1, 10, 78, 588` (`computations/probes/tl_n6_discriminator.py`).

## What is and is not proved here — read before citing

Everything in *this* file is unconditional: `#print axioms` gives
`[propext, Classical.choice, Quot.sound]` on every declaration, with no
`sorryAx`.

The **arithmetic** — that the two-row square-sum is `catalan n` — is therefore
settled for all `n`. What is *not* settled here, and is not claimed, is the
identification of the visible blocks with `ℓ(λ) ≤ 2`.  That once rested on the Wenzl
weight system carried as the class `QOU.QBeta.WenzlWeight.IsOcneanuWeightSystem`; the
class is deleted (2026-11-15, bean `qou-gld2`) and the identification is now proved
unconditionally: `SchurWeyl.JimboActionKernel.finrank_range_jimbo` (`d = 2`) and
`SchurWeyl.JimboGL.finrank_range_jimbo` (any `d`).  The `_of_wenzl` names in
`MassTheory.TwoRowCapDerived` are historical; those lemmas never used the class.

Numerical cross-check of the whole reduction (hook length formula against full
partition enumeration, `n ≤ 14`):
`computations/probes/two_row_ballot_catalan_reduction.py`.
-/

namespace QOU.Mathlib

open QOU.BraidKnot.IdentityI (dimHLF)
open QOU.Mathlib.SYTHookRows (dimHLF_pair)
open QOU.Mathlib.SYTEnum (dimHLF_zero_row choose_mono_pair)

/-- **The two-row hook-length dimension is the ballot number**, in `ballot`'s
indexing: `dim S^{(n−k,k)} = m_k(n)` whenever `2k ≤ n`.

`dimHLF_pair` already says this as a `ℕ` difference of binomials; the work here
is the cast to `ℤ`, which needs `C(n,k−1) ≤ C(n,k)` so that the truncated `ℕ`
subtraction agrees with the honest `ℤ` one. That monotonicity holds precisely
below the centre of the row, i.e. exactly under the hypothesis `2k ≤ n` that
makes `(n−k, k)` a partition — so the side condition is not an artefact, it is
the same condition twice.

The `k = 0` case is separate because `m_0` is pinned rather than computed
(see `ballot`); there the shape is `(n)` with an empty second row and
`dimHLF_zero_row` gives `1`. -/
theorem dimHLF_two_row_eq_ballot (n k : ℕ) (hk : 2 * k ≤ n) :
    ((dimHLF [n - k, k] : ℕ) : ℤ) = ballot n k := by
  cases k with
  | zero =>
      have hn : n - 0 = n := by omega
      rw [hn, dimHLF_zero_row, ballot_zero]
      norm_num
  | succ j =>
      have hb : 1 ≤ j + 1 := by omega
      have hab : j + 1 ≤ n - (j + 1) := by omega
      have hsum : n - (j + 1) + (j + 1) = n := by omega
      rw [dimHLF_pair (n - (j + 1)) (j + 1) hab hb, hsum]
      have hmono : n.choose (j + 1 - 1) ≤ n.choose (j + 1) :=
        choose_mono_pair n (j + 1) hb (by omega)
      have hj : j + 1 - 1 = j := by omega
      rw [hj] at hmono
      rw [hj, ballot_succ, Nat.cast_sub hmono]

/-- **`Σ_{k ≤ ⌊n/2⌋} (dim S^{(n−k,k)})² = catalan n`.**

The sum of squared dimensions over all partitions of `n` with at most two rows
is the `n`-th Catalan number — for every `n`, with the dimensions given by the
Frame–Robinson–Thrall hook length formula rather than by a closed form assumed
in advance.

Equivalently, by RSK, 321-avoiding permutations of `n` are counted by `C_n`;
but the proof goes nowhere near RSK — see `BallotNumbers.ballot_sq_sum_catalan`
for the reflection-plus-Vandermonde argument that replaces it. -/
theorem dimHLF_two_row_sq_sum (n : ℕ) :
    ∑ k ∈ Finset.range (n / 2 + 1), ((dimHLF [n - k, k] : ℕ) : ℤ) ^ 2
      = (catalan n : ℤ) := by
  rw [← ballot_sq_sum_catalan n]
  refine Finset.sum_congr rfl ?_
  intro k hk
  have hkr : k < n / 2 + 1 := Finset.mem_range.mp hk
  have h2k : 2 * k ≤ n := by omega
  rw [dimHLF_two_row_eq_ballot n k h2k]

/-- **The general-`n` rank accounting**: `n!` minus the visible-block dimension
count is `n! − catalan n`.

This is the arithmetic identity that `QOU.QBeta.MarkovGramDegenerate.corank_three`
/ `_four` / `_five` were three hand-computed instances of. Those wrote the
two-row dimensions out by hand (`1, 2` / `1, 3, 2` / `1, 4, 5`); this derives
the whole count from `catalan n` with nothing listed by hand. -/
theorem factorial_sub_two_row_sq_sum (n : ℕ) :
    (n.factorial : ℤ) - ∑ k ∈ Finset.range (n / 2 + 1), ((dimHLF [n - k, k] : ℕ) : ℤ) ^ 2
      = (n.factorial : ℤ) - (catalan n : ℤ) := by
  rw [dimHLF_two_row_sq_sum n]

/-! ### The measured values, as instances of the general theorem

`n = 3, 4, 5, 6` are the values `computations/probes/tl_n6_discriminator.py`
measured as Gram coranks (`1, 10, 78, 588`). `n = 7, 8` are stated here as
*arithmetic predictions* — the numbers a rank measurement at those levels would
have to produce. They are not themselves rank measurements, and nothing below
claims otherwise. -/

theorem corank_value_three : (Nat.factorial 3 : ℤ) - (catalan 3 : ℤ) = 1 := by
  norm_num [catalan_eq_centralBinom_div, Nat.centralBinom, Nat.choose, Nat.factorial]

theorem corank_value_four : (Nat.factorial 4 : ℤ) - (catalan 4 : ℤ) = 10 := by
  norm_num [catalan_eq_centralBinom_div, Nat.centralBinom, Nat.choose, Nat.factorial]

theorem corank_value_five : (Nat.factorial 5 : ℤ) - (catalan 5 : ℤ) = 78 := by
  norm_num [catalan_eq_centralBinom_div, Nat.centralBinom, Nat.choose, Nat.factorial]

theorem corank_value_six : (Nat.factorial 6 : ℤ) - (catalan 6 : ℤ) = 588 := by
  norm_num [catalan_eq_centralBinom_div, Nat.centralBinom, Nat.choose, Nat.factorial]

theorem corank_value_seven : (Nat.factorial 7 : ℤ) - (catalan 7 : ℤ) = 4611 := by
  norm_num [catalan_eq_centralBinom_div, Nat.centralBinom, Nat.choose, Nat.factorial]

theorem corank_value_eight : (Nat.factorial 8 : ℤ) - (catalan 8 : ℤ) = 38890 := by
  norm_num [catalan_eq_centralBinom_div, Nat.centralBinom, Nat.choose, Nat.factorial]

end QOU.Mathlib
