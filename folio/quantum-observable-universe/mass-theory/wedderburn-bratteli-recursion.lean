/-
  Wedderburn–Bratteli recursion for the Jones–Markov weights `y_λ` at
  `H_n(R, q)`, convention D.

  ## 2026-11-20 rewrite (W8b, gap 3 of bean `qou-w8cg`)

  The previous file was degenerate in three ways, and all three are removed:

  * **The recursion predicate forced `y ≡ 0`.** Its `BratteliEdge` carried the
    added cell's content as a free field and had no `μ ⊂ λ` constraint, so an
    "edge" `λ ↗ λ` was admissible, and `y λ = z·F·y λ` then forces `y λ = 0`
    unless `z·F = 1`. The existence theorem was witnessed by `y ≡ 0` for that
    reason.
  * **An undisclosed `axiom`** (`plancherel_completeness_axiom`,
    `Σ y_λ d_λ = 1` for every `y` satisfying that predicate). Its hypothesis
    "`parts` lists every partition of `n`" can never hold — the skeleton
    `Partition` admits trailing zeros, so infinitely many lists sum to `n` — so
    it was consistent only because it was unusable. Read with a satisfiable
    hypothesis it would be false, since `y ≡ 0` satisfies the predicate.
  * **The `lean.ref` `wedderburn_bratteli_recursion` did not exist.**

  ## What is stated now, and proved sorry-free

  Under **convention D** (`z = q³/(q²+1)`) every shape with three or more rows
  carries Ocneanu weight `0` (`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`),
  so the Jones–Markov weights live on two-row shapes `(a, b)`, `a ≥ b`, where
  they have the closed form

    `y_(a,b) = [a − b + 1]_q / [2]_q^{a+b}`        (`jonesWeightD`),

  `[k]_q` the balanced q-integer. At `n = 3` this is
  `([4]_q/[2]_q³, 1/[2]_q², 0)`, the convention-D vector of
  `QOU.BraidsAndKnots.MarkovTraceTLUniqueness` (`jonesWeightD_h3`).

  * `wedderburn_bratteli_recursion` — **the Bratteli recursion**: restricting
    the trace from `H_{n+1}` to `H_n` sums the weights over the two Bratteli
    edges out of `(a, b)`:
    `y_(a,b) = y_(a+1,b) + y_(a,b+1)`. When `a = b` the second shape is not a
    partition, and the formula gives it weight `[0]_q = 0`
    (`jonesWeightD_diag_succ`), so the identity is the correct one-edge rule
    there too. The key step is the q-integer identity `[d+1] + [d−1] = [2][d]`
    (`qIntBalZ_add_sub`).
  * `jonesWeightD_edge_row` / `jonesWeightD_edge_col` — **the multiplicative
    form along a single edge**, division-free:
    `[2]_q · [d]_q · y_(a+1,b) = [d+1]_q · y_(a,b)` and
    `[2]_q · [d]_q · y_(a,b+1) = [d−1]_q · y_(a,b)` with `d = a − b + 1`. The
    edge factor depends on which row the cell is added to, through `d`; that
    is the content of the `.md`'s "`F_q(c(λ, μ), …)`".

  **Not encoded:** the normalisation `Σ_λ f^λ y_λ = 1` over all `λ ⊢ n`
  (`f^λ` the number of standard tableaux). It follows from the sum rule above
  and the branching rule `f^λ = Σ_{μ ↗ λ} f^μ`, which needs a partition type
  this file does not build. It is a gap, not an axiom.

  Base ring: a generic field (§7c). The divisions are genuine: `[2]_q` and the
  balanced q-integers vanish at roots of unity, excluded as "generic `q`".

  Refs: conj:wedderburn-bratteli-recursion,
        prop:y-lambda-closed-form-wenzl-bridge,
        thm:jones-markov-trace
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import QOU.MathlibExt.QIntegerCanonical

namespace QOU.BraidsAndKnots

open QOU.QInteger

variable {R : Type*} [Field R]

/-- `[d+1]_q + [d−1]_q = [2]_q · [d]_q`, with `[2]_q = q + q⁻¹`. -/
theorem qIntBalZ_add_sub {q : R} (hq : q ≠ 0) (d : ℤ) :
    qIntBalZ q (d + 1) + qIntBalZ q (d - 1) = (q + q⁻¹) * qIntBalZ q d := by
  simp only [qIntBalZ_def]
  rw [← add_div, mul_div_assoc']
  congr 1
  rw [zpow_add₀ hq, zpow_sub₀ hq, show -(d + 1) = -d - 1 by ring,
    show -(d - 1) = -d + 1 by ring, zpow_sub₀ hq, zpow_add₀ hq, zpow_one]
  field_simp
  ring

/-- Convention-D Jones–Markov weight on the two-row shape `(a, b)`:
`y_(a,b) = [a − b + 1]_q / [2]_q^{a+b}`. -/
noncomputable def jonesWeightD (q : R) (a b : ℕ) : R :=
  qIntBalZ q ((a : ℤ) - b + 1) / (q + q⁻¹) ^ (a + b)

/-- The `n = 3` weights: `y_(3) = [4]_q/[2]_q³`, `y_(2,1) = [2]_q/[2]_q³ = 1/[2]_q²`. -/
theorem jonesWeightD_h3 {q : R} (h1 : q - q⁻¹ ≠ 0) :
    jonesWeightD q 3 0 = qIntBalZ q 4 / (q + q⁻¹) ^ 3 ∧
    jonesWeightD q 2 1 = (q + q⁻¹) / (q + q⁻¹) ^ 3 := by
  refine ⟨by norm_num [jonesWeightD], ?_⟩
  have h : qIntBalZ q 2 = q + q⁻¹ := by
    rw [show (2 : ℤ) = ((2 : ℕ) : ℤ) by norm_num, qIntBalZ_natCast, qIntBal_two q h1]
  simp only [jonesWeightD]
  rw [show ((2 : ℕ) : ℤ) - ((1 : ℕ) : ℤ) + 1 = 2 by norm_num, h]

/-- On the diagonal the second Bratteli edge leaves the partitions: the formula
assigns `(a, a+1)` the weight `[0]_q = 0`. -/
theorem jonesWeightD_diag_succ (q : R) (a : ℕ) : jonesWeightD q a (a + 1) = 0 := by
  simp [jonesWeightD]

/-- **The Wedderburn–Bratteli recursion (convention D).** Restricting the trace
from `H_{n+1}` to `H_n` sums the weights over the Bratteli edges out of
`(a, b)`: `y_(a,b) = y_(a+1,b) + y_(a,b+1)`. -/
-- Ref: [leitner2026] mass-theory/wedderburn-bratteli-recursion.md
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
theorem wedderburn_bratteli_recursion {q : R} (hq : q ≠ 0) (h2 : q + q⁻¹ ≠ 0)
    (a b : ℕ) :
    jonesWeightD q a b = jonesWeightD q (a + 1) b + jonesWeightD q a (b + 1) := by
  simp only [jonesWeightD]
  have hk := qIntBalZ_add_sub hq ((a : ℤ) - b + 1)
  have e1 : ((↑(a + 1) : ℤ) - b + 1) = (a : ℤ) - b + 1 + 1 := by push_cast; ring
  have e2 : ((a : ℤ) - ↑(b + 1) + 1) = (a : ℤ) - b + 1 - 1 := by push_cast; ring
  rw [e1, e2, show a + 1 + b = a + b + 1 by ring, show a + (b + 1) = a + b + 1 by ring,
    ← add_div, hk, pow_succ]
  generalize q + q⁻¹ = t at h2 ⊢
  field_simp

/-- Single edge, cell added to the first row: `[2] [d] y_(a+1,b) = [d+1] y_(a,b)`. -/
theorem jonesWeightD_edge_row {q : R} (h2 : q + q⁻¹ ≠ 0) (a b : ℕ) :
    (q + q⁻¹) * qIntBalZ q ((a : ℤ) - b + 1) * jonesWeightD q (a + 1) b =
      qIntBalZ q ((a : ℤ) - b + 1 + 1) * jonesWeightD q a b := by
  simp only [jonesWeightD]
  rw [show ((↑(a + 1) : ℤ) - b + 1) = (a : ℤ) - b + 1 + 1 by push_cast; ring,
    show a + 1 + b = a + b + 1 by ring, pow_succ]
  generalize q + q⁻¹ = t at h2 ⊢
  field_simp

/-- Single edge, cell added to the second row: `[2] [d] y_(a,b+1) = [d−1] y_(a,b)`. -/
theorem jonesWeightD_edge_col {q : R} (h2 : q + q⁻¹ ≠ 0) (a b : ℕ) :
    (q + q⁻¹) * qIntBalZ q ((a : ℤ) - b + 1) * jonesWeightD q a (b + 1) =
      qIntBalZ q ((a : ℤ) - b + 1 - 1) * jonesWeightD q a b := by
  simp only [jonesWeightD]
  rw [show ((a : ℤ) - ↑(b + 1) + 1) = (a : ℤ) - b + 1 - 1 by push_cast; ring,
    show a + (b + 1) = a + b + 1 by ring, pow_succ]
  generalize q + q⁻¹ = t at h2 ⊢
  field_simp

end QOU.BraidsAndKnots
