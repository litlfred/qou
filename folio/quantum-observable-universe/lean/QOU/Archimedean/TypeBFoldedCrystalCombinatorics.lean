import Mathlib.Tactic


/-!
# Type-B folded crystal combinatorics

Following AGENTS.md §7b "Type B folding for chirality / CPT", this
file gives concrete Lean infrastructure for the Type-B folded
$\mathfrak{sl}_n$ crystal used in
`prop:crystal-basis-resolves-mass-tower-open-problems`:

* `PartitionWithContent` — a list-of-cells representation of a
  partition together with each cell's content `c(x) = column - row`.
* `transpose_partition` — the involution `λ ↔ λ^T` that pairs
  cells with `c(λ) + c(λ^T) = 0` summand-by-summand.
* `Cell.content_neg_under_transpose` — the unconditional
  cancellation lemma: each cell `(r, c)` and its transpose `(c, r)`
  satisfy `content (r, c) + content (c, r) = 0`.

These are the combinatorial primitives needed to encode the
chirality factor's $\langle c \rangle_\beta$ Wedderburn-weighted
sum as a Type-B-folded crystal computation. The folding pairs
`λ ↔ λ^T`, and the cell-level content cancellation makes the
self-paired part of $\langle c \rangle_\beta$ vanish; the
non-trivial part is the imbalance between $\chi^\lambda(\beta)$
and $\chi^{\lambda^T}(\beta)$ along the Demazure components.

-- Ref: [leitner2026] prop:crystal-basis-resolves-mass-tower-open-problems
-- Ref: [leitner2026] prop:chirality-writhe-ribbon-derivation
-- Ref: [kashiwara1991] DOI 10.1215/S0012-7094-91-06321-0
-- Ref: [brundankleshchev2009] DOI 10.1007/s00222-009-0204-8
-- Ref: [leitner2026] AGENTS.md §7b "Symmetric-crystal techniques"
-/

namespace QOU.Archimedean.TypeBCrystal

/-- A cell of a Young diagram, parameterised by `(row, column)`
    with both components 0-indexed. The **content** of a cell is
    `c(r, col) := col - r`. -/
structure Cell where
  row : ℕ
  col : ℕ
deriving DecidableEq, Repr

/-- Cell content `c(r, col) = col - r ∈ ℤ`. -/
def Cell.content (x : Cell) : ℤ := (x.col : ℤ) - (x.row : ℤ)

/-- The transpose of a cell: swap row and column. -/
def Cell.transpose (x : Cell) : Cell := ⟨x.col, x.row⟩

/-- The transpose involution is involutive: `(x.transpose).transpose = x`. -/
@[simp] theorem Cell.transpose_transpose (x : Cell) :
    x.transpose.transpose = x := by
  cases x; rfl

/-- **Key lemma:** the content of a cell and the content of its
    transpose sum to zero. This is the unconditional
    cancellation identity that makes Type-B folding "work":

      c(λ) + c(λ^T) = 0  cell-by-cell.

    The proof is direct integer arithmetic. -/
theorem content_plus_transpose_content_eq_zero (x : Cell) :
    x.content + x.transpose.content = 0 := by
  unfold Cell.content Cell.transpose
  simp

/-- A **partition with explicit cells** — a `List` of `Cell`s
    representing the Young diagram. (We do not enforce the
    partition shape constraints here; downstream callers can.) -/
structure PartitionWithCells where
  cells : List Cell
deriving Repr

/-- The **content sum** of a partition is `Σ_{x ∈ λ} c(x)`. -/
def PartitionWithCells.content_sum (P : PartitionWithCells) : ℤ :=
  (P.cells.map Cell.content).sum

/-- The **transpose** of a partition: transpose every cell. -/
def PartitionWithCells.transpose (P : PartitionWithCells) :
    PartitionWithCells :=
  ⟨P.cells.map Cell.transpose⟩

/-- **Folding cancellation theorem (sorry-free).** The content sum
    of a partition plus the content sum of its transpose is zero.

    This is the partition-level lift of `Cell.content_plus_transpose_content_eq_zero`:
    every cell's content cancels with the transpose-image cell's
    content, so the two list-sums sum to zero. -/
-- Ref: [leitner2026] AGENTS.md §7b "Type B folding ⇒ symmetric crystal,
-- bar-involution invariant by construction"
theorem PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero
    (P : PartitionWithCells) :
    P.content_sum + P.transpose.content_sum = 0 := by
  unfold PartitionWithCells.content_sum PartitionWithCells.transpose
  rw [List.map_map]
  rw [show (Cell.content ∘ Cell.transpose) =
        (fun x => -x.content) by
    funext x
    simp [Cell.content, Cell.transpose]]
  rw [show (P.cells.map (fun x => -x.content)) =
        ((P.cells.map Cell.content).map (fun y => -y)) by
    rw [List.map_map]; rfl]
  -- Now we have: (P.cells.map Cell.content).sum +
  --              ((P.cells.map Cell.content).map (· · -)).sum = 0
  generalize P.cells.map Cell.content = L
  induction L with
  | nil => simp
  | cons x xs ih =>
    simp [List.sum_cons, List.map_cons]
    linarith

/-- **Self-pair fixed-point property.** A partition equal to its
    own transpose has content sum zero. This is the "self-dual"
    partition case (e.g. `(2, 2)`, `(3, 1)`, `(4, 1, 1, 1)` etc.):
    folding pairs each cell with its transpose, and the
    fixed-point partition sits at the symmetric centre. -/
theorem self_transpose_content_sum_zero
    (P : PartitionWithCells)
    (h : P = P.transpose) :
    P.content_sum = 0 := by
  have key := PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero P
  rw [← h] at key
  linarith

end QOU.Archimedean.TypeBCrystal
