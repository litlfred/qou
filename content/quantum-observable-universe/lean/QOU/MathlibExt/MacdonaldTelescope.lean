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

end QOU.MathlibExt.MacdonaldTelescope
