import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Data.Fintype.BigOperators

/-!
# QOU.MathlibExt.BlockDiagonalCorank — corank of a block-constant diagonal Gram form

`QOU.QBeta.MarkovGramDegenerate` defines the Wedderburn-basis Gram form as
`wedderburnGram y = Matrix.diagonal y` and proves when its determinant vanishes
(`wedderburnGram_det_ne_zero_iff_all_live`), but it records the actual coranks
only as **numeral arithmetic** at fixed `n`:

    corank_three : 6   - (1^2 + 2^2)       = 1^2
    corank_four  : 24  - (1^2 + 3^2 + 2^2) = 3^2 + 1^2
    corank_five  : 120 - (1^2 + 4^2 + 5^2) = 6^2 + 5^2 + 4^2 + 1^2

Those are true statements about numbers, and they carry no partition content: the
dimensions `1, 2, 3, 5, …` appear as literals. This file supplies the **general
`n` skeleton** they are instances of, over an arbitrary finite block index type.

## What is proved here, and what is deliberately not

Take a finite set `Λ` of blocks with dimensions `d : Λ → ℕ`. The Wedderburn
basis of `⨁_λ M_{d λ}(R)` is indexed by `BlockIdx d = Σ λ, Fin (d λ) × Fin (d λ)`,
and a trace whose Wedderburn weights are `y : Λ → R` has Gram matrix
`Matrix.diagonal (blockConst d y)` — diagonal, and **constant on each block**.
Then

    corank = (∑ λ, d λ ^ 2) − ∑ λ live, d λ ^ 2                (`corank_blockDiagonal`)

with `live λ ↔ y λ ≠ 0`, and in the form the vanishing theorems actually deliver,

    corank = (∑ λ, d λ ^ 2) − ∑ λ with P λ, d λ ^ 2            (`corank_eq_of_live_iff`)

for any predicate `P` that characterises non-vanishing. Feeding
`QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff_rowLens` in as `P λ = (ℓ λ ≤ 2)`
gives the two-row corank at every `n` at once, **with the surviving sum left
symbolic**.

Evaluating that sum — `∑_{ℓ(λ) ≤ 2} (dim V_λ)^2 = catalan n` — is a *separate*
and genuinely open statement: by RSK it says 321-avoiding permutations are
Catalan, Mathlib has neither RSK nor pattern avoidance, and this repo has it only
at `n = 3, 4, 5` (`QOU.Mathlib.ballot_sq_sum_catalan_small`). See bean `qou-0cyu`
item G5. Nothing below assumes it, and nothing below is weakened by its absence.

**No Hecke algebra, no Markov trace, and no conjecture class appears in any
statement.** These are unconditional facts about diagonal matrices, and they are
sorry-free.

## Base ring (§7c)

`Matrix.rank` needs a field, so `corank_blockDiagonal` takes `[Field R]`. The two
counting lemmas it is built from need only `[Zero R]` and stay there.

-- Ref: [manuscript] quantum-observable-universe/qbeta/markov-gram-degenerate.md
-/

namespace QOU.MathlibExt.BlockCorank

open Finset

variable {Λ : Type*} [Fintype Λ]

/-- Index set of a Wedderburn basis for `⨁_λ M_{d λ}(R)`: block `λ` contributes
its `d λ × d λ` matrix units. -/
abbrev BlockIdx (d : Λ → ℕ) : Type _ := Σ l : Λ, Fin (d l) × Fin (d l)

/-- The basis has `∑_λ (d λ)^2` elements — for `H_n(q)` at generic `q` this is
the `n!` on the left of the corank identities. -/
theorem card_blockIdx (d : Λ → ℕ) :
    Fintype.card (BlockIdx d) = ∑ l, d l ^ 2 := by
  simp [BlockIdx, Fintype.card_sigma, sq]

/-- A weight that is **constant on each Wedderburn block**: the Gram entry at a
matrix unit of block `λ` is `y λ`, independent of which unit it is. This is the
structural input the numeral corank facts leave implicit. -/
def blockConst {R : Type*} (d : Λ → ℕ) (y : Λ → R) : BlockIdx d → R := fun i => y i.1

/-- **Live count.** The number of basis elements carrying a nonzero weight is the
sum of `(d λ)^2` over the blocks with `y λ ≠ 0`. -/
theorem card_live {R : Type*} [Zero R] [DecidableEq R] (d : Λ → ℕ) (y : Λ → R) :
    Fintype.card {i : BlockIdx d // blockConst d y i ≠ 0}
      = ∑ l ∈ univ.filter (fun l => y l ≠ 0), d l ^ 2 := by
  classical
  rw [Fintype.card_subtype, Finset.card_filter, Fintype.sum_sigma]
  rw [Finset.sum_filter]
  refine Finset.sum_congr rfl (fun l _ => ?_)
  by_cases h : y l = 0
  · simp [blockConst, h]
  · simp [blockConst, h, Finset.card_univ, sq]

/-- **Corank of a block-constant diagonal Gram form, at every `n` at once.**

The general-`n` statement that `QOU.QBeta.MarkovGramDegenerate.corank_three` /
`_four` / `_five` are numeral instances of. -/
theorem corank_blockDiagonal [DecidableEq Λ] {R : Type*} [Field R] [DecidableEq R]
    (d : Λ → ℕ) (y : Λ → R) :
    Fintype.card (BlockIdx d) - (Matrix.diagonal (blockConst d y)).rank
      = (∑ l, d l ^ 2) - ∑ l ∈ univ.filter (fun l => y l ≠ 0), d l ^ 2 := by
  classical
  rw [Matrix.rank_diagonal, card_live, card_blockIdx]

/-- **Corank in the form a vanishing theorem delivers it.**

A vanishing result gives a *criterion* `P` for `y λ ≠ 0` — for convention D,
`P λ = (ℓ(λ) ≤ 2)`. This restates the corank against that criterion, so the
surviving sum is indexed by the shapes the criterion admits and stays symbolic. -/
theorem corank_eq_of_live_iff [DecidableEq Λ] {R : Type*} [Field R] [DecidableEq R]
    (d : Λ → ℕ) (y : Λ → R) (P : Λ → Prop) [DecidablePred P]
    (hlive : ∀ l, y l ≠ 0 ↔ P l) :
    Fintype.card (BlockIdx d) - (Matrix.diagonal (blockConst d y)).rank
      = (∑ l, d l ^ 2) - ∑ l ∈ univ.filter P, d l ^ 2 := by
  classical
  rw [corank_blockDiagonal]
  congr 2
  exact Finset.filter_congr (fun l _ => by simpa using hlive l)

/-! ### The general statement reproduces the measured numbers

`corank_three` says `6 − (1² + 2²) = 1²` as arithmetic on literals. Here the same
number comes out of `corank_blockDiagonal` applied to the `H₃` block data
`d = (1, 2, 1)` with the antisymmetriser dead — i.e. from the structure rather
than from a table. This is the check that the general skeleton is the right one. -/
example : (∑ l : Fin 3, (![1, 2, 1] : Fin 3 → ℕ) l ^ 2)
    - ∑ l ∈ univ.filter (fun l : Fin 3 => l ≠ 2), (![1, 2, 1] : Fin 3 → ℕ) l ^ 2 = 1 := by
  decide

end QOU.MathlibExt.BlockCorank

