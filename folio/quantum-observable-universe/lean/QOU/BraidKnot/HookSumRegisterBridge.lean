import QOU.BraidKnot.HookSumClosedForm
import QOU.Common.HookSumComplete

/-!
# Bridging the two hook-sum registers

The hook-sum identity is proved twice in this corpus, in registers that did not
talk to each other:

1. `QOU.HookSumComplete.hookSum_eq` (module `QOU.Common.HookSumComplete`) — over
   a sorted `List ℕ`, in `ℕ` with truncated subtraction, with its own
   `colLen` / `bStat` / `colSum` / `hookSum`, and an explicit sortedness
   hypothesis.
2. `QOU.BraidKnot.HookSum` — over Mathlib's `YoungDiagram`, in `ℤ`, on
   `PieceAGeneral`'s `armZ` / `legZ` / `hookZ`, with no sortedness hypothesis
   (`YoungDiagram` carries that structurally).

`HookSum`'s docstring asserted they were the same identity and stated (1)'s
shape term-for-term so a reader could check. That is a human reading. This
module makes it a proof: `hookSum_rowLens` identifies the two hook sums, and
`sum_hookZ_eq_bStat_via_list` re-derives the `YoungDiagram` closed form **from**
the list one, so the two are demonstrably one theorem rather than two that
happen to agree.

## The four component bridges

`rowLens_getD`, `colLen_rowLens`, `rowLens_sum_eq_card` translate the data;
`rowLens_sorted'` and `rowLens_le_rowLen_zero` discharge (1)'s two hypotheses
from `YoungDiagram.rowLen_anti` alone. Note that `rowLens_sorted'` does **not**
go through `YoungDiagram.rowLens_sorted`: `rowLen_anti` gives the statement in
the form `hookSum_eq` wants directly, without unpacking `List.Sorted`.

## Where the work actually is

The `ℕ`-to-`ℤ` cast, as expected — but only because it is *conditional*. (1)
writes an arm as `l.getD i 0 - 1 - j` in truncated `ℕ` subtraction, which agrees
with `armZ`'s `ℤ` subtraction **only on a cell**. So the cellwise step carries
`j < μ.rowLen i`, and derives `i < μ.colLen j` from it through
`mem_iff_lt_rowLen` / `mem_iff_lt_colLen`, before `omega` may equate the two.
Off a cell the two registers genuinely disagree, and nothing here says
otherwise.

## Index sets

`hookSum_eq` takes a column bound `M`; `μ.rowLen 0` is the natural choice and
`rowLens_le_rowLen_zero` supplies it. The row count is forced: `List.length` of
`μ.rowLens`, which `YoungDiagram.length_rowLens` identifies with `μ.colLen 0`.
-/

namespace QOU.BraidKnot.HookSumBridge

open Finset QOU.BraidKnot.PieceA

/-! ## Translating the data -/

/-- Past the last nonempty row, the row length is zero. -/
theorem rowLen_eq_zero_of_le (μ : YoungDiagram) {i : ℕ} (hi : μ.colLen 0 ≤ i) :
    μ.rowLen i = 0 := by
  by_contra h
  have hmem : (i, 0) ∈ μ :=
    YoungDiagram.mem_iff_lt_rowLen.mpr (Nat.pos_of_ne_zero h)
  have : i < μ.colLen 0 := YoungDiagram.mem_iff_lt_colLen.mp hmem
  omega

/-- `μ.rowLens.getD i 0 = μ.rowLen i`, for **every** `i`: inside the list by
`get_rowLens`, past its end because both sides are `0`. The total form is what
the list-register statements need — they index by `getD` over
`range l.length` and never carry a bound. -/
theorem rowLens_getD (μ : YoungDiagram) (i : ℕ) :
    μ.rowLens.getD i 0 = μ.rowLen i := by
  rw [List.getD_eq_getElem?_getD]
  by_cases h : i < μ.rowLens.length
  · rw [List.getElem?_eq_getElem h, Option.getD_some, YoungDiagram.get_rowLens]
  · rw [List.getElem?_eq_none (by omega), Option.getD_none]
    refine (rowLen_eq_zero_of_le μ ?_).symm
    rw [← YoungDiagram.length_rowLens]
    omega

/-- The list register's column length is the diagram's. -/
theorem colLen_rowLens (μ : YoungDiagram) (j : ℕ) :
    QOU.HookSumComplete.colLen μ.rowLens j = μ.colLen j := by
  rw [QOU.HookSumComplete.colLen]
  have hset : (range μ.rowLens.length).filter (fun i => j < μ.rowLens.getD i 0)
      = range (μ.colLen j) := by
    ext i
    simp only [Finset.mem_filter, Finset.mem_range, rowLens_getD,
      YoungDiagram.length_rowLens]
    constructor
    · rintro ⟨-, h⟩
      exact YoungDiagram.mem_iff_lt_colLen.mp
        (YoungDiagram.mem_iff_lt_rowLen.mpr h)
    · intro h
      refine ⟨lt_of_lt_of_le h (μ.colLen_anti 0 j (Nat.zero_le _)), ?_⟩
      exact YoungDiagram.mem_iff_lt_rowLen.mp
        (YoungDiagram.mem_iff_lt_colLen.mpr h)
  rw [hset, Finset.card_range]

/-- The row lengths sum to the cell count. -/
theorem rowLens_sum_eq_card (μ : YoungDiagram) :
    μ.rowLens.sum = μ.cells.card := by
  have hN : μ.colLen 0 ≤ μ.rowLens.length :=
    le_of_eq YoungDiagram.length_rowLens.symm
  have hZ := QOU.BraidKnot.HookSum.sum_rowLen_eq_card μ hN
  rw [← QOU.HookSumComplete.sum_range_getD,
    Finset.sum_congr rfl (fun i _ => rowLens_getD μ i)]
  exact_mod_cast hZ

/-! ## Discharging the list register's two hypotheses -/

/-- `hookSum_eq`'s sortedness hypothesis, straight from `rowLen_anti` — no need
to unpack `YoungDiagram.rowLens_sorted` into this shape. -/
theorem rowLens_sorted' (μ : YoungDiagram) :
    ∀ a b, a ≤ b → b < μ.rowLens.length →
      μ.rowLens.getD b 0 ≤ μ.rowLens.getD a 0 := by
  intro a b hab _
  rw [rowLens_getD, rowLens_getD]
  exact μ.rowLen_anti a b hab

/-- `hookSum_eq`'s column-bound hypothesis at `M = μ.rowLen 0`. -/
theorem rowLens_le_rowLen_zero (μ : YoungDiagram) :
    ∀ i ∈ range μ.rowLens.length, μ.rowLens.getD i 0 ≤ μ.rowLen 0 := by
  intro i _
  rw [rowLens_getD]
  exact μ.rowLen_anti 0 i (Nat.zero_le _)

/-! ## The bridge -/

/-- **The two hook sums are the same number.** `HookSumComplete.hookSum` of
`μ.rowLens`, cast to `ℤ`, is `Σ_c hookZ μ c`.

The cellwise step is where the registers actually meet: the list side's
truncated `ℕ` subtraction agrees with `armZ`/`legZ` only because `j` indexes a
real cell of row `i`, which also forces `i < μ.colLen j`. -/
theorem hookSum_rowLens (μ : YoungDiagram) :
    (QOU.HookSumComplete.hookSum μ.rowLens : ℤ) = ∑ c ∈ μ.cells, hookZ μ c := by
  have hN : μ.colLen 0 ≤ μ.rowLens.length :=
    le_of_eq YoungDiagram.length_rowLens.symm
  rw [QOU.BraidKnot.HookSum.sum_cells_eq_sum_rows μ hN (fun c => hookZ μ c),
    QOU.HookSumComplete.hookSum, Nat.cast_sum]
  refine Finset.sum_congr rfl ?_
  intro i _
  rw [Nat.cast_sum, rowLens_getD]
  refine Finset.sum_congr rfl ?_
  intro j hj
  have h1 : j < μ.rowLen i := Finset.mem_range.mp hj
  have h2 : i < μ.colLen j :=
    YoungDiagram.mem_iff_lt_colLen.mp (YoungDiagram.mem_iff_lt_rowLen.mpr h1)
  simp only [hookZ, armZ, legZ, colLen_rowLens]
  omega

/-- **The list-register closed form, transported.** `Σ_c hookZ = b(λ') + b(λ) + n`
derived from `HookSumComplete.hookSum_eq` through the bridge — a second,
independent route to `HookSum.sum_hookZ_eq_bStat`, which proves the same
proposition from the `YoungDiagram` arm/leg reflections instead. -/
theorem sum_hookZ_eq_bStat_via_list (μ : YoungDiagram) :
    ∑ c ∈ μ.cells, hookZ μ c
      = ∑ j ∈ range (μ.rowLen 0), (j : ℤ) * (μ.colLen j : ℤ)
        + ∑ i ∈ range (μ.colLen 0), (i : ℤ) * (μ.rowLen i : ℤ)
        + (μ.cells.card : ℤ) := by
  rw [← hookSum_rowLens μ,
    QOU.HookSumComplete.hookSum_eq μ.rowLens (μ.rowLen 0) (rowLens_sorted' μ)
      (rowLens_le_rowLen_zero μ),
    QOU.HookSumComplete.colSum, QOU.HookSumComplete.bStat,
    rowLens_sum_eq_card]
  push_cast [colLen_rowLens, rowLens_getD, YoungDiagram.length_rowLens]
  -- All that separates the two sides now is the factor order inside the column
  -- sum: `colSum` is defined as `Σ_j (colLen j) * j`, and the `YoungDiagram`
  -- statement writes `Σ_j j * (colLen j)`. Everything else, association
  -- included, already matches — so this rewrite closes the goal by `rfl`.
  -- Stated explicitly rather than left to `ring`, which cannot reach inside the
  -- binder and so sees the two column sums as unrelated atoms.
  have hcomm : ∑ x ∈ range (μ.rowLen 0), ((μ.colLen x : ℤ) * (x : ℤ))
      = ∑ j ∈ range (μ.rowLen 0), ((j : ℤ) * (μ.colLen j : ℤ)) :=
    Finset.sum_congr rfl (fun j _ => mul_comm _ _)
  rw [hcomm]

/-- The reflection route proves the very same proposition — same statement, so
the two derivations are not merely consistent, they are one theorem. -/
theorem sum_hookZ_eq_bStat_via_reflections (μ : YoungDiagram) :
    ∑ c ∈ μ.cells, hookZ μ c
      = ∑ j ∈ range (μ.rowLen 0), (j : ℤ) * (μ.colLen j : ℤ)
        + ∑ i ∈ range (μ.colLen 0), (i : ℤ) * (μ.rowLen i : ℤ)
        + (μ.cells.card : ℤ) :=
  QOU.BraidKnot.HookSum.sum_hookZ_eq_bStat μ le_rfl le_rfl

/-- Subtracting the list-register b-statistic sum from the cellwise hook sum yields zero. -/
theorem sum_hookZ_sub_bStat_eq_zero (μ : YoungDiagram) :
    ∑ c ∈ μ.cells, hookZ μ c
      - (∑ j ∈ range (μ.rowLen 0), (j : ℤ) * (μ.colLen j : ℤ)
        + ∑ i ∈ range (μ.colLen 0), (i : ℤ) * (μ.rowLen i : ℤ)
        + (μ.cells.card : ℤ)) = 0 := by
  rw [sum_hookZ_eq_bStat_via_list, sub_self]

end QOU.BraidKnot.HookSumBridge
