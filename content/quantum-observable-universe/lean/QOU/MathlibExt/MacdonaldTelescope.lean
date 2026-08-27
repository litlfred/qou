import QOU.MathlibExt.WenzlSchurElement

/-!
# QOU.MathlibExt.MacdonaldTelescope — the hook telescope, proved at low rank

The **Macdonald hook telescope** is

  `Σ_{λ ⊢ n} f_λ · s_λ(Q, X)  =  ((1 − X)/(1 − Q))^n`

with `f_λ` the number of standard Young tableaux of shape `λ` and `s_λ` the
Wenzl Schur element (`WenzlSchurElement.schurElement`). It is the identity the
`y_λ` closed form reduces to, and it is currently carried in the corpus as an
`axiom` (`mass-theory/macdonald-hook-telescope.lean`).

## Why it is true, and why the general case is not proved here

`s_λ(Q, X)` with `X = Q^r` **is** the principal specialisation
`s_λ(1, Q, …, Q^{r−1})` of the Schur function, since `1 − X·Q^{c(x)} = 1 − Q^{r+c(x)}`.
The identity is then the Frobenius/Cauchy identity for the regular representation

  `Σ_λ f_λ · s_λ = p₁ⁿ`

specialised at `(1, Q, …, Q^{r−1})`, where `p₁ = 1 + Q + ⋯ + Q^{r−1} = (1 − X)/(1 − Q)`.

Both halves — the Frobenius identity and the principal-specialisation product
formula — are **symmetric-function infrastructure Mathlib does not have**. That
is the honest reason the general `n` is not proved here, and it is a real gap
rather than a hard step: the mathematics is classical (Stanley EC2 Cor. 7.12.5;
Macdonald I.3 ex. 1), the Lean substrate is missing.

## What IS proved here, unconditionally

The identity at `n = 1` and `n = 2`, **computed from the concrete
`schurElement`** — not from an axiom, not from a restatement. At `n = 2` it is a
genuine cancellation: the two partitions contribute

  `s₍₂₎ = (1 − X)(1 − XQ) / ((1 − Q²)(1 − Q))`,
  `s₍₁,₁₎ = Q · (1 − X)(1 − X·Q⁻¹) / ((1 − Q²)(1 − Q))`,

and the bracket `(1 − XQ) + Q(1 − X·Q⁻¹) = (1 + Q)(1 − X)` is what makes the
`(1 + Q)` cancel against `1 − Q²`, leaving `((1 − X)/(1 − Q))²`. Nothing here is
true by construction; the cancellation is the content.

These are the base cases any induction would need, and they are the first
non-vacuous check that the corrected `n(λ)` prefactor is the right one — with
the old `contentSum` prefactor, `telescope_two` below is **false**.
-/

namespace QOU.MathlibExt.MacdonaldTelescope

open QOU.MathlibExt QOU.MathlibExt.QPartitionCombinatorics

/-! `norm_num` will not unroll `List.range` at a numeral on its own, and the
`schurElement` folds are over exactly that. These two rewrites are all it needs;
without them the inner column-fold survives every tactic below. -/

private theorem range_one_eq : List.range 1 = [0] := rfl
private theorem range_two_eq : List.range 2 = [0, 1] := rfl
private theorem range_three_eq : List.range 3 = [0, 1, 2] := rfl

/-- The right-hand side of the telescope, `((1 − X)/(1 − Q))^n`. -/
noncomputable def telescopeRHS (n : ℕ) (Q X : ℝ) : ℝ := ((1 - X) / (1 - Q)) ^ n

/-- **`n = 1`.** The single partition `(1)` has `f = 1` and
`s₍₁₎ = (1 − X)/(1 − Q)`. -/
theorem telescope_one (Q X : ℝ) :
    WenzlSchurElement.schurElement Q X [1] = telescopeRHS 1 Q X := by
  norm_num [WenzlSchurElement.schurElement, nLambda, telescopeRHS,
    WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
    range_one_eq]

/-- **`n = 2`, the first case with content.** Both partitions of `2` have
`f_λ = 1`, so the telescope reads `s₍₂₎ + s₍₁,₁₎ = ((1 − X)/(1 − Q))²`.

The hypotheses are exactly what the denominators and the `Q⁻¹` in the
`(1,0)`-cell content require: `Q ≠ 0` for the negative power, and `Q ≠ 1`,
`Q ≠ −1` for `1 − Q` and `1 − Q²`. -/
theorem telescope_two (Q X : ℝ) (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (hQm1 : Q ≠ -1) :
    WenzlSchurElement.schurElement Q X [2]
      + WenzlSchurElement.schurElement Q X [1, 1] = telescopeRHS 2 Q X := by
  have h1 : (1 : ℝ) - Q ≠ 0 := sub_ne_zero.mpr (Ne.symm hQ1)
  have hp1 : (1 : ℝ) + Q ≠ 0 := by
    intro h; exact hQm1 (by linarith)
  have h2 : (1 : ℝ) - Q ^ 2 ≠ 0 := by
    have hfac : (1 : ℝ) - Q ^ 2 = (1 - Q) * (1 + Q) := by ring
    rw [hfac]; exact mul_ne_zero h1 hp1
  norm_num [WenzlSchurElement.schurElement, nLambda, telescopeRHS,
    WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
    range_one_eq, range_two_eq]
  field_simp
  ring

/-! ### The old prefactor made this FALSE — proved, not merely measured

`schurElement`'s prefactor read `contentSum` rather than `n(λ)` until
2026-08-26. Since the two differ only in the prefactor, the old value at `λ` is
`schurElement Q X λ · Q^{contentSum λ − n(λ)}`; concretely `·Q` at `(2)` (where
`contentSum = 1`, `n(λ) = 0`) and `·Q⁻²` at `(1,1)` (where `contentSum = −1`,
`n(λ) = 1`).

Evaluated at `Q = 2`, `X = 3` the corrected telescope gives exactly `4`, and the
old one gives `41/6`. The theorem below proves the old form is **not** equal to
the target, which is what makes `telescope_two` a real constraint rather than
one convention among several. -/

/-- **The corrected telescope is sharp at a point**: `Q = 2`, `X = 3` gives
exactly `4 = ((1−3)/(1−2))²`. -/
theorem telescope_two_at_two_three :
    WenzlSchurElement.schurElement 2 3 [2]
      + WenzlSchurElement.schurElement 2 3 [1, 1] = 4 := by
  have h := telescope_two 2 3 (by norm_num) (by norm_num) (by norm_num)
  rw [h]
  norm_num [telescopeRHS]

/-- **With the OLD `contentSum` prefactor the identity FAILS**, at the same
point: the sum is `41/6`, not `4`.

This is the theorem that makes the bug fix a correction rather than a
preference. If someone reverts `schurElement`'s prefactor to `contentSum`, this
statement — and `telescope_two` — become unprovable together. -/
theorem old_contentSum_prefactor_breaks_telescope :
    WenzlSchurElement.schurElement 2 3 [2] * 2
      + WenzlSchurElement.schurElement 2 3 [1, 1] * ((2 : ℝ) ^ (-2 : ℤ)) ≠ 4 := by
  have h2 : WenzlSchurElement.schurElement (2 : ℝ) 3 [2] = 10 / 3 := by
    norm_num [WenzlSchurElement.schurElement, nLambda,
      WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
      range_two_eq]
  have h11 : WenzlSchurElement.schurElement (2 : ℝ) 3 [1, 1] = 2 / 3 := by
    norm_num [WenzlSchurElement.schurElement, nLambda,
      WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
      range_two_eq]
  rw [h2, h11]
  norm_num

/-! ### `n = 3` — the first case where the SYT multiplicity does any work

`n = 1` and `n = 2` both have `f_λ = 1` for every `λ`, so the multiplicity in
`Σ_λ f_λ · s_λ` was never exercised: those cases would hold equally for an
unweighted sum. `n = 3` is the first that distinguishes them —

  `λ = (3)`      `f = 1`,  `n(λ) = 0`,  hooks `3,2,1`
  `λ = (2,1)`    `f = 2`,  `n(λ) = 1`,  hooks `3,1,1`
  `λ = (1,1,1)`  `f = 1`,  `n(λ) = 3`,  hooks `3,2,1`

and the `2` is load-bearing: drop it and the identity fails. So this is the base
case that actually tests the shape of the telescope, and the one an induction
would need to trust. -/

/-- **`n = 3`.** `s₍₃₎ + 2·s₍₂,₁₎ + s₍₁,₁,₁₎ = ((1−X)/(1−Q))³`.

The `2` is the number of standard Young tableaux of shape `(2,1)`. This is the
first telescope case in which `f_λ ≠ 1` for some `λ`. -/
theorem telescope_three (Q X : ℝ) (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (hQm1 : Q ≠ -1) :
    WenzlSchurElement.schurElement Q X [3]
      + 2 * WenzlSchurElement.schurElement Q X [2, 1]
      + WenzlSchurElement.schurElement Q X [1, 1, 1] = telescopeRHS 3 Q X := by
  have h1 : (1 : ℝ) - Q ≠ 0 := sub_ne_zero.mpr (Ne.symm hQ1)
  have hp1 : (1 : ℝ) + Q ≠ 0 := fun h => hQm1 (by linarith)
  have h2 : (1 : ℝ) - Q ^ 2 ≠ 0 := by
    have hfac : (1 : ℝ) - Q ^ 2 = (1 - Q) * (1 + Q) := by ring
    rw [hfac]; exact mul_ne_zero h1 hp1
  have hq2q1 : (1 : ℝ) + Q + Q ^ 2 ≠ 0 := by
    intro h
    -- `1 + Q + Q² = (Q + 1/2)² + 3/4 > 0` over `ℝ`, so it cannot vanish.
    nlinarith [sq_nonneg (Q + 1 / 2), sq_nonneg Q]
  have h3 : (1 : ℝ) - Q ^ 3 ≠ 0 := by
    have hfac : (1 : ℝ) - Q ^ 3 = (1 - Q) * (1 + Q + Q ^ 2) := by ring
    rw [hfac]; exact mul_ne_zero h1 hq2q1
  norm_num [WenzlSchurElement.schurElement, nLambda, telescopeRHS,
    WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
    range_two_eq, range_three_eq]
  field_simp
  ring

/-- **`n = 3` is sharp at `Q = 2`, `X = 3`**: the weighted sum is exactly `8`. -/
theorem telescope_three_at_two_three :
    WenzlSchurElement.schurElement 2 3 [3]
      + 2 * WenzlSchurElement.schurElement 2 3 [2, 1]
      + WenzlSchurElement.schurElement 2 3 [1, 1, 1] = 8 := by
  have h := telescope_three 2 3 (by norm_num) (by norm_num) (by norm_num)
  rw [h]; norm_num [telescopeRHS]

/-- **The multiplicity is load-bearing.** Replacing `f₍₂,₁₎ = 2` by `1` breaks
the identity at `Q = 2`, `X = 3`. Stated so that "the sum of Schur elements"
cannot be mistaken for the telescope: the *weighting* is part of the claim.

At `Q = 2, X = 3` the three Schur elements are `110/21`, `10/7`, `−2/21`. With
multiplicities `(1, 2, 1)` they sum to exactly `8`; unweighted they sum to
`46/7`. -/
theorem telescope_three_needs_multiplicity :
    WenzlSchurElement.schurElement 2 3 [3]
      + WenzlSchurElement.schurElement 2 3 [2, 1]
      + WenzlSchurElement.schurElement 2 3 [1, 1, 1] ≠ 8 := by
  have h3 : WenzlSchurElement.schurElement (2 : ℝ) 3 [3] = 110 / 21 := by
    norm_num [WenzlSchurElement.schurElement, nLambda,
      WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
      range_three_eq]
  have h21 : WenzlSchurElement.schurElement (2 : ℝ) 3 [2, 1] = 10 / 7 := by
    norm_num [WenzlSchurElement.schurElement, nLambda,
      WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
      range_two_eq, range_three_eq]
  have h111 : WenzlSchurElement.schurElement (2 : ℝ) 3 [1, 1, 1] = -2 / 21 := by
    norm_num [WenzlSchurElement.schurElement, nLambda,
      WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
      range_three_eq]
  rw [h3, h21, h111]; norm_num

/-! ### The reduction: general `n` does NOT need symmetric-function theory

**A correction to what this file said above, and to what I told the author
repeatedly.** The general case was described as resting on symmetric-function
infrastructure Mathlib lacks — the Frobenius identity and the
principal-specialisation product formula. That is one route, and it is not the
cheapest. The telescope follows by induction on `n` from two **elementary**
statements, neither of which mentions a symmetric function:

* **(P) Pieri, specialised.**
  `Σ_{λ = μ + box} s_λ(Q, X) = ((1 − X)/(1 − Q)) · s_μ(Q, X)`,
  a rational-function identity in `Q, X` over the cells of `μ` and its addable
  corners. Verified symbolically with `X` **free** (not just at `X = Q^r`) for
  `μ = ∅, (1), (2), (1,1), (2,1), (3), (2,2), (3,1)`.
* **(F) the SYT recursion.** `f_λ = Σ_{μ = λ − box} f_μ`.

Given those, the step is three rewrites:

  `Σ_{λ⊢n+1} f_λ s_λ  =  Σ_{λ⊢n+1} (Σ_{μ=λ−box} f_μ) s_λ`   (F)
                     `=  Σ_{μ⊢n} f_μ (Σ_{λ=μ+box} s_λ)`      (reindex)
                     `=  ((1−X)/(1−Q)) · Σ_{μ⊢n} f_μ s_μ`    (P)

Both inputs are Mathlib-shaped and elementary; `Nat.Partition n` (with its
`Fintype`) and `YoungDiagram` already exist, so the enumeration and the
box-addition maps are available. The remaining work is real but it is
**combinatorics, not symmetric-function theory** — a materially smaller and
differently-shaped gap than the one previously recorded here.

The theorems below are not another base case. They exercise the *engine*:
`pieri_one` is (P) at `μ = (1)`, and `telescope_two_via_pieri` derives `n = 2`
from `n = 1` **through it**, showing the induction step is real rather than
merely checked numerically. -/

/-- **(P) at `μ = (1)`**: `s₍₂₎ + s₍₁,₁₎ = ((1 − X)/(1 − Q)) · s₍₁₎`.

The two addable corners of a single box are `(2)` and `(1,1)`. Note this holds
with `X` free — it is not special to `X = Q^r`. -/
theorem pieri_one (Q X : ℝ) (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (hQm1 : Q ≠ -1) :
    WenzlSchurElement.schurElement Q X [2]
      + WenzlSchurElement.schurElement Q X [1, 1]
      = ((1 - X) / (1 - Q)) * WenzlSchurElement.schurElement Q X [1] := by
  have h1 : (1 : ℝ) - Q ≠ 0 := sub_ne_zero.mpr (Ne.symm hQ1)
  have hp1 : (1 : ℝ) + Q ≠ 0 := fun h => hQm1 (by linarith)
  have h2 : (1 : ℝ) - Q ^ 2 ≠ 0 := by
    have hfac : (1 : ℝ) - Q ^ 2 = (1 - Q) * (1 + Q) := by ring
    rw [hfac]; exact mul_ne_zero h1 hp1
  norm_num [WenzlSchurElement.schurElement, nLambda,
    WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
    range_one_eq, range_two_eq]
  field_simp
  ring

/-- **The induction step, executed once.** `n = 2` derived from `n = 1` through
`pieri_one` — not re-proved from scratch.

This is the point of the reduction: `telescope_two` above is proved directly,
whereas this obtains the same statement from the previous rung plus (P). If the
general induction is ever formalised, this is the shape it will take. -/
theorem telescope_two_via_pieri (Q X : ℝ)
    (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (hQm1 : Q ≠ -1) :
    WenzlSchurElement.schurElement Q X [2]
      + WenzlSchurElement.schurElement Q X [1, 1] = telescopeRHS 2 Q X := by
  rw [pieri_one Q X hQ0 hQ1 hQm1, telescope_one Q X]
  simp [telescopeRHS, pow_succ]

/-! ### (P) at a shape that exercises the whole engine

`pieri_one` is (P) at `λ = (1)`, whose two corners are both trivial: one is a
single row, the other a single column, and neither has a cell above or below the
new box. It cannot distinguish the three row cases from each other.

`λ = (2,1)` is the first shape that does. It has **three** addable corners:

| corner | what it exercises |
|---|---|
| `(3,1)` | a box in row `0`, with row `1` **below** it — `rowFactor_addBoxRow_row_below` |
| `(2,2)` | a box in row `1`, with row `0` **above** it in the changed column — the interior case, the one needing product surgery |
| `(2,1,1)` | a **new bottom row**, which `addBoxRow` cannot express at all (§ `addBoxNewRow`) |

So this is the (P) analogue of `telescope_three`: the first case where the
statement's moving parts are all in play at once, and the one an induction would
have to trust. Verified symbolically with `X` free beforehand in
`computations/y_lambda_pieri_step_probe.py`. -/

/-- **(P) at `λ = (2,1)`**: `s₍₃,₁₎ + s₍₂,₂₎ + s₍₂,₁,₁₎ = ((1 − X)/(1 − Q)) · s₍₂,₁₎`.

Three corners, one of each kind — a row with something below it, a row with
something above it in the changed column, and a new bottom row. -/
theorem pieri_two_one (Q X : ℝ) (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (hQm1 : Q ≠ -1) :
    WenzlSchurElement.schurElement Q X [3, 1]
      + WenzlSchurElement.schurElement Q X [2, 2]
      + WenzlSchurElement.schurElement Q X [2, 1, 1]
      = ((1 - X) / (1 - Q)) * WenzlSchurElement.schurElement Q X [2, 1] := by
  have h1 : (1 : ℝ) - Q ≠ 0 := sub_ne_zero.mpr (Ne.symm hQ1)
  have hp1 : (1 : ℝ) + Q ≠ 0 := fun h => hQm1 (by linarith)
  have h2 : (1 : ℝ) - Q ^ 2 ≠ 0 := by
    have hfac : (1 : ℝ) - Q ^ 2 = (1 - Q) * (1 + Q) := by ring
    rw [hfac]; exact mul_ne_zero h1 hp1
  have hq2q1 : (1 : ℝ) + Q + Q ^ 2 ≠ 0 := by
    intro h; nlinarith [sq_nonneg (Q + 1 / 2), sq_nonneg Q]
  have h3 : (1 : ℝ) - Q ^ 3 ≠ 0 := by
    have hfac : (1 : ℝ) - Q ^ 3 = (1 - Q) * (1 + Q + Q ^ 2) := by ring
    rw [hfac]; exact mul_ne_zero h1 hq2q1
  have hsq1 : (1 : ℝ) + Q ^ 2 ≠ 0 := by positivity
  have h4 : (1 : ℝ) - Q ^ 4 ≠ 0 := by
    have hfac : (1 : ℝ) - Q ^ 4 = (1 - Q ^ 2) * (1 + Q ^ 2) := by ring
    rw [hfac]; exact mul_ne_zero h2 hsq1
  norm_num [WenzlSchurElement.schurElement, nLambda,
    WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
    range_one_eq, range_two_eq, range_three_eq]
  field_simp
  ring

/-- **(P) at `λ = (2,1)` is sharp at `Q = 2`, `X = 3`**: both sides are `20/7`,
so the identity is not satisfied vacuously by both sides vanishing. -/
theorem pieri_two_one_at_two_three :
    WenzlSchurElement.schurElement 2 3 [3, 1]
      + WenzlSchurElement.schurElement 2 3 [2, 2]
      + WenzlSchurElement.schurElement 2 3 [2, 1, 1] = 20 / 7 := by
  have h := pieri_two_one 2 3 (by norm_num) (by norm_num) (by norm_num)
  rw [h]
  norm_num [WenzlSchurElement.schurElement, nLambda,
    WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
    range_one_eq, range_two_eq]

/-- **The three corners contribute genuinely different amounts**, and one is
negative: at `Q = 2`, `X = 3` they are `22/9`, `40/63` and `−2/9`, summing to
`20/7`. Recorded because a sum identity whose summands happened to be equal —
or all of one sign — would be a much weaker check than it looks. -/
theorem pieri_two_one_summands_at_two_three :
    WenzlSchurElement.schurElement 2 3 [3, 1] = 22 / 9
      ∧ WenzlSchurElement.schurElement 2 3 [2, 2] = 40 / 63
      ∧ WenzlSchurElement.schurElement 2 3 [2, 1, 1] = -2 / 9 := by
  refine ⟨?_, ?_, ?_⟩ <;>
    norm_num [WenzlSchurElement.schurElement, nLambda,
      WenzlSchurElement.cellContent, Partition.hookLength, Partition.length,
      range_one_eq, range_two_eq, range_three_eq]

/-! ### (P) stated in general

`QPartitionCombinatorics.addableCorners` enumerates the shapes one box larger.
With it, (P) is a single equation about one shape, and the two cases proved
above are **instances of it** rather than statements that merely resemble it —
which is what `pieriStep_one` and `pieriStep_two_one` below establish.

Stating it does not prove it. The general case is the induction over corners,
and it is open; nothing here asserts otherwise. What this buys is that the open
goal is now a *named proposition with verified instances*, so the next attempt
starts from a statement that has been checked against the probe rather than
from prose. -/

/-- The left side of (P): the Schur elements of `λ`'s addable corners, summed. -/
noncomputable def pieriSum (Q X : ℝ) (lam : Partition) : ℝ :=
  ((addableCorners lam).map (WenzlSchurElement.schurElement Q X)).sum

/-- **(P) at one shape**: the corner sum equals `((1 − X)/(1 − Q))` times the
shape's own Schur element. -/
def PieriStep (Q X : ℝ) (lam : Partition) : Prop :=
  pieriSum Q X lam = ((1 - X) / (1 - Q)) * WenzlSchurElement.schurElement Q X lam

/-- `pieri_one` **is** (P) at `λ = (1)` — the enumeration produces exactly the
two corners that theorem sums. -/
theorem pieriStep_one (Q X : ℝ) (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (hQm1 : Q ≠ -1) :
    PieriStep Q X [1] := by
  unfold PieriStep pieriSum
  rw [addableCorners_one]
  simpa using pieri_one Q X hQ0 hQ1 hQm1

/-- `pieri_two_one` **is** (P) at `λ = (2,1)` — the enumeration produces exactly
the three corners that theorem sums, in the same order.

This is the load-bearing one: `(2,1)` is where the enumeration has to get the
weak-decrease condition right (row 1 is strictly shorter than row 0, so it is
addable) *and* remember the new bottom row. -/
theorem pieriStep_two_one (Q X : ℝ) (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (hQm1 : Q ≠ -1) :
    PieriStep Q X [2, 1] := by
  unfold PieriStep pieriSum
  rw [addableCorners_two_one]
  have h := pieri_two_one Q X hQ0 hQ1 hQm1
  simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
  linarith [h]

end QOU.MathlibExt.MacdonaldTelescope
