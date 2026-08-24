import QOU.SchurWeyl.BranchingGenericity
import QOU.Mathlib.YoungDiagramCornerReindex

/-!
# QOU.SchurWeyl.AddableCellIndexing — the addable-cell sum as a sum over rows

`sum_wenzlWeight_addCellOrSelf` sums over `range r` with a decidable guard.  The branching exchange
(`YoungDiagramCornerReindex.sum_corner_eq_sum_addable`) hands its inner sum over the **addable-cell
subtype**.  This file identifies the two.

| | |
|---|---|
| `isAddableCell_row_le` | an addable cell sits in row `≤ colLen 0` |
| `addableRowSet μ` | the addable cells, as an explicit `Finset` indexed by row |
| `sum_addable_eq_sum_range` | the subtype sum **is** the guarded `range (colLen 0 + 1)` sum |

**Why the row bound is `colLen 0 + 1` and not `colLen 0`.**  A diagram with `k` nonzero rows has an
addable cell at row `k` — start a new row — so the rows carrying an addable cell run `0 … k`, not
`0 … k−1`.  Reconciling that with a `range r` sum is what `wenzlWeight_addCell_beyond_eq_zero`
handles: at `colLen 0 = r` the row-`r` cell is real but its weight is `0`.

## Base ring (§7c)

Generic `[AddCommMonoid M]` — pure reindexing, no ring.

LaTeX label: `lem:addable-cell-indexing`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.Mathlib

/-- An addable cell sits in row `≤ colLen 0`: either it is in row `0`, or the cell above it is in
`μ`, which bounds its row by the column height. -/
theorem isAddableCell_row_le {μ : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell μ s) :
    s.1 ≤ μ.colLen 0 := by
  obtain ⟨-, h1, -⟩ := hs
  rcases h1 with h | h
  · omega
  · have hup : ((s.1 - 1, 0) : ℕ × ℕ) ∈ μ := μ.up_left_mem (le_refl _) (Nat.zero_le _) h
    have := mem_iff_lt_colLen.mp hup
    omega

/-- The addable cells of `μ`, as an explicit `Finset`: one per row `a ≤ colLen 0` that admits a box,
sitting at `(a, μ_a)`. -/
noncomputable def addableRowSet (μ : YoungDiagram) : Finset (ℕ × ℕ) :=
  ((Finset.range (μ.colLen 0 + 1)).filter
    (fun a => IsAddableCell μ (a, μ.rowLen a))).image (fun a => (a, μ.rowLen a))

theorem mem_addableRowSet {μ : YoungDiagram} (c : ℕ × ℕ) :
    c ∈ addableRowSet μ ↔ IsAddableCell μ c := by
  classical
  rw [addableRowSet, Finset.mem_image]
  constructor
  · rintro ⟨a, ha, rfl⟩
    exact (Finset.mem_filter.mp ha).2
  · intro hc
    refine ⟨c.1, Finset.mem_filter.mpr ⟨Finset.mem_range.mpr ?_, ?_⟩, ?_⟩
    · have := isAddableCell_row_le hc
      omega
    · rwa [← QOU.SchurWeyl.rowLen_of_isAddableCell hc]
    · rw [← QOU.SchurWeyl.rowLen_of_isAddableCell hc]

/-- **The addable-cell subtype sum is the guarded row sum.** -/
theorem sum_addable_eq_sum_range {M : Type*} [AddCommMonoid M] (μ : YoungDiagram)
    (G : ℕ × ℕ → M) :
    (∑ s : {s : ℕ × ℕ // IsAddableCell μ s}, G s.1)
      = ∑ a ∈ Finset.range (μ.colLen 0 + 1),
          (if IsAddableCell μ (a, μ.rowLen a) then G (a, μ.rowLen a) else 0) := by
  classical
  rw [← Finset.sum_subtype (addableRowSet μ) mem_addableRowSet G, addableRowSet,
    Finset.sum_image (fun a _ b _ h => congrArg Prod.fst h), Finset.sum_filter]

end QOU.SchurWeyl
