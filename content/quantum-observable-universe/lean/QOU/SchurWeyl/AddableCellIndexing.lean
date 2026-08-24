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
| `sum_addable_wenzlWeight` | **`∑_{s addable} w_{μ+s} = w_μ`** — branching in the exchange's own indexing |

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

/-! ## Branching in the exchange's own indexing -/

variable {F : Type*} [Field F]

/-- **Branching over the addable cells.**

`∑_{s addable to μ} w_{μ+s} = w_μ`.

Same content as `sum_wenzlWeight_addCellOrSelf`, in the indexing
`YoungDiagramCornerReindex.sum_corner_eq_sum_addable` produces — which is what the normalisation
induction consumes.

The two row ranges are reconciled by cases, and **both directions carry a real fact**:

* `colLen 0 < r` — rows `colLen 0 < a < r` are empty and so is the row above them, so
  `isAddableCell_rowEnd_iff` refuses them and the guard is `0`;
* `colLen 0 = r` — row `r` *is* addable, and its term vanishes only because the resulting diagram
  has `r+1` rows (`wenzlWeight_addCell_beyond_eq_zero`). -/
theorem sum_addable_wenzlWeight (Q : F) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r : ℕ} {μ : YoungDiagram}
    (hbr : levelBracket r Q ≠ 0) (hQ1 : Q ≠ 1) (hrμ : μ.colLen 0 ≤ r) :
    (∑ s : {s : ℕ × ℕ // IsAddableCell μ s}, wenzlWeight r Q (addCellOrSelf μ s.1))
      = wenzlWeight r Q μ := by
  classical
  rw [sum_addable_eq_sum_range μ (fun c => wenzlWeight r Q (addCellOrSelf μ c))]
  have hrange : (∑ a ∈ Finset.range (μ.colLen 0 + 1),
      (if IsAddableCell μ (a, μ.rowLen a) then
        wenzlWeight r Q (addCellOrSelf μ (a, μ.rowLen a)) else 0))
      = ∑ a ∈ Finset.range r,
        (if IsAddableCell μ (a, μ.rowLen a) then
          wenzlWeight r Q (addCellOrSelf μ (a, μ.rowLen a)) else 0) := by
    rcases Nat.lt_or_ge (μ.colLen 0) r with hlt | hge
    · have hsub : Finset.range (μ.colLen 0 + 1) ⊆ Finset.range r := by
        intro x hx
        rw [Finset.mem_range] at hx ⊢
        omega
      refine Finset.sum_subset hsub fun a ha hna => ?_
      rw [Finset.mem_range] at ha hna
      have hna' : μ.colLen 0 < a := by omega
      have h1 : μ.rowLen a = 0 :=
        QOU.Mathlib.SYTBeta.rowLen_eq_zero_of_colLen_le (by omega)
      have h2 : μ.rowLen (a - 1) = 0 :=
        QOU.Mathlib.SYTBeta.rowLen_eq_zero_of_colLen_le (by omega)
      refine if_neg fun hadd => ?_
      rcases (isAddableCell_rowEnd_iff μ a).mp hadd with h | h
      · omega
      · omega
    · have hEq : μ.colLen 0 = r := by omega
      rw [hEq]
      have hsub : Finset.range r ⊆ Finset.range (r + 1) := by
        intro x hx
        rw [Finset.mem_range] at hx ⊢
        omega
      refine (Finset.sum_subset hsub fun a ha hna => ?_).symm
      rw [Finset.mem_range] at ha hna
      have hare : a = r := by omega
      subst hare
      by_cases hadd : IsAddableCell μ (a, μ.rowLen a)
      · rw [if_pos hadd, addCellOrSelf_of hadd]
        exact wenzlWeight_addCell_beyond_eq_zero hQ0 hgen hbr (le_refl a) hadd
      · rw [if_neg hadd]
  rw [hrange, sum_wenzlWeight_addCellOrSelf Q hQ0 hQ1 hgen hrμ hbr]

end QOU.SchurWeyl
