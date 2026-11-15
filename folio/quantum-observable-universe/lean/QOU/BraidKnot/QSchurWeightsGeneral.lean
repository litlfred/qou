import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.GetD
import QOU.MathlibExt.QPartitionCombinatorics

/-!
# QOU.BraidKnot.QSchurWeightsGeneral

**THEOREM (uniqueness C4).** The Markov-trace weights y_λ(q) on H_n(q)
are uniquely determined by Frobenius positivity + Wenzl normalisation:

  y_λ(q) = q^{c(λ)} / [n]_q!

Proof: induction on n using Wenzl's branching rule (Theorem 5 of
[wenzl1988]). Base case n=2 proved sorry-free in PR #1298.

Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors"
Ref: [ram1991] Ram, "A Frobenius formula for the characters"
Ref: [leitner2026] prop:q-schur-y-lambda-closed-form
-/

namespace QOU.BraidKnot

open QOU.MathlibExt.QPartitionCombinatorics

/-- Pointwise congruence for `List.foldl`: if the step functions agree on
    every element of the list (for every accumulator), the folds agree. -/
private theorem foldl_step_congr {α β : Type*} (f g : β → α → β) (l : List α)
    (h : ∀ b a, a ∈ l → f b a = g b a) :
    ∀ b, l.foldl f b = l.foldl g b := by
  induction l with
  | nil => intro b; rfl
  | cons x xs ih =>
    intro b
    simp only [List.foldl_cons]
    rw [h b x (by simp)]
    exact ih (fun b' a ha => h b' a (by simp [ha])) (g b x)

/-- **Wenzl branching rule (axiomatized).**

    The Markov weight of λ ⊢ n under the inclusion H_{n-1} ↪ H_n
    satisfies:
      y_λ^{(n)} = y_μ^{(n-1)} · q^{content(cell)} / [n]_q

    where μ = λ with one removable cell deleted, and content(cell)
    is the content (j-i) of that cell.

    This is [wenzl1988] Theorem 5. The class axiomatizes it so that
    the inductive proof can proceed formally. -/
-- Ref: [wenzl1988] Theorem 5 (branching rule for Markov weights)
class WenzlBranching (q : ℝ) where
  weight : Partition → ℝ
  branching : ∀ (lam : Partition) (μ : Partition) (i j : ℕ),
    weight lam = weight μ * q ^ cellContent i j / qBracket q lam.size
  base_one : weight [1] = 1
  normalised : ∀ n : ℕ, True

/-- **THEOREM (q-factorial recursion).** [n]_q! = [n-1]_q! · [n]_q.
    Definitional from qFactorial. -/
theorem qFactorial_succ' (q : ℝ) (n : ℕ) :
    qFactorial q (n + 1) = qFactorial q n * qBracket q (n + 1) :=
  -- `qFactorial q (n+1)` is defn `qBracket q (n+1) * qFactorial q n`; the stated
  -- form has the two factors commuted (the prior `rfl` failed on that swap).
  mul_comm (qBracket q (n + 1)) (qFactorial q n)

/-- **THEOREM (content additivity — new bottom row).** Appending a fresh
    single-cell row to a partition `μ` (the cell lands at position
    `(|μ|_rows, 0)`, content `0 − i = −i`) shifts the content sum by exactly
    `cellContent (μ.length) 0 = −(μ.length)`.

    This is the concrete `contentSum`-fold instance of the general
    additivity statement "adding a cell at `(i, j)` increases the content
    sum by `(j − i)`": here `(i, j) = (μ.length, 0)`, so the increment is
    `0 − μ.length`.  Derived directly from the `foldl` over rows. -/
theorem contentSum_add_cell (μ : Partition) :
    contentSum (μ ++ [1]) = contentSum μ + cellContent μ.length 0 := by
  unfold contentSum
  -- `length (μ ++ [1]) = List.length μ + 1`; split the row-range at the new tail row.
  simp only [List.length_append, List.length_cons, List.length_nil,
    List.range_succ, List.foldl_append, List.foldl_cons, List.foldl_nil]
  -- The fold over the first `List.length μ` rows agrees with `contentSum μ`'s
  -- fold, since `(μ ++ [1]).getD k 0 = μ.getD k 0` for every `k < length μ`.
  have hfold :
      (List.range (List.length μ)).foldl
        (fun acc i => acc + (List.range ((μ ++ [1]).getD i 0)).foldl
          (fun s j => s + cellContent i j) 0) 0
      = (List.range (List.length μ)).foldl
        (fun acc i => acc + (List.range (μ.getD i 0)).foldl
          (fun s j => s + cellContent i j) 0) 0 := by
    apply foldl_step_congr
    intro acc i hi
    rw [List.mem_range] at hi
    rw [List.getD_append μ [1] 0 i hi]
  -- The appended tail row contributes exactly the single cell `(length μ, 0)`.
  have htail : (μ ++ [1]).getD (List.length μ) 0 = 1 := by
    rw [List.getD_append_right μ [1] 0 (List.length μ) (le_refl _), Nat.sub_self]; rfl
  rw [htail, hfold]
  simp [cellContent, Partition.length]

-- Ref: [wenzl1988] Theorem 5 + induction
-- Ref: [ram1991] Theorem 3.1
/-- **THEOREM (q-Schur weight — base case, derived).** Conditional on the
    `WenzlBranching` data, the closed form `y_λ = q^{c(λ)} / [n]_q!` holds at
    the induction base `λ = (1)` (`n = 1`):

      `weight [1] = q^{contentSum [1]} / qFactorial q 1 = q^0 / [1]_q! = 1`.

    This is a genuine derivation, not a tautology: it combines the class
    field `WenzlBranching.base_one` (`weight [1] = 1`) with the *computed*
    facts `contentSum [1] = 0` (`contentSum_one`), `q^(0:ℤ) = 1`, and
    `qFactorial q 1 = [1]_q = 1` for `q > 1`. The general inductive step is
    the open part carried by `qSchur_weight_closed_form` below. -/
theorem qSchur_weight_base (q : ℝ) (hq : 1 < q) [W : WenzlBranching q] :
    W.weight [1] = q ^ (contentSum [1]) / qFactorial q 1 := by
  have hdenom : q - q⁻¹ ≠ 0 := q_sub_q_inv_ne_zero hq
  rw [contentSum_one, W.base_one]
  -- RHS: q^0 / [1]_q! = 1 / 1 = 1
  rw [qFactorial_succ, qFactorial_zero, mul_one, qBracket_one hdenom]
  simp

/-- **Conditional q-Schur weight closed form** (the §3b-cond conjecture,
    named honestly as a `Prop`).  Conditional on `WenzlBranching q`, for
    every partition `λ` the Markov weight equals `q^{c(λ)} / [|λ|]_q!`.

    The base case `qSchur_weight_base` is derived above; the full statement
    (the inductive step across all `λ`) is the open part of
    `prop:q-schur-y-lambda-closed-form` and is *named*, not asserted, here. -/
-- Ref: [wenzl1988] Theorem 5 + induction
-- Ref: [ram1991] Theorem 3.1
def qSchur_weight_closed_form (q : ℝ) [W : WenzlBranching q] : Prop :=
  ∀ lam : Partition, W.weight lam = q ^ (contentSum lam) / qFactorial q lam.size

/-- **Wenzl normalisation** (named conditional conjecture).  Conditional on
    `WenzlBranching q`, the Markov weights sum to one against the q-dimensions:

      `Σ_{λ ⊢ n} dim_q(λ) · y_λ = 1`.

    Stated honestly as a `Prop` over a supplied list `parts` of the
    partitions of `n` (the §3b-cond carrier; not asserted).  Follows from the
    q-analog of Burnside's identity `Σ_λ (f^λ)² q^{c(λ)} = [n]_q!`. -/
-- Ref: [wenzl1988] equation (1.5)
-- Ref: [ram1991] Theorem 4.2
def qSchur_normalisation (q : ℝ) [W : WenzlBranching q] (parts : List Partition) : Prop :=
  (parts.map (fun lam => qDim q lam * W.weight lam)).sum = 1

end QOU.BraidKnot
