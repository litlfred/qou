import QOU.SchurWeyl.YoungTableaux

/-!
# `#cells` of a Young diagram, and of a partition's shape

The pinned Mathlib knows `YoungDiagram.rowLens`, `rowLen_ofRowLens`, `mem_ofRowLens` and
`rowLens_ofRowLens_eq_self`, but it does **not** relate a diagram's cell count to its row lengths.
Probed against the olean tree before writing this file: `card_ofRowLens`, `card_eq_sum`,
`card_cells_ofRowLens`, `ofRowLens_card`, `rowLens_sum_eq_card`, `sum_rowLens_eq_card` and
`card_eq_rowLens_sum` are all unknown constants, and `exact?` cannot close
`μ.cells.card = μ.rowLens.sum`.

That absence is what blocks the reindexing half of `hoefsmit_seminormal_rep`
(bean `qou-im9l`, gap (i)): `SeminormalRep.seminormalRep` takes `μ.cells.card = n + 1`, and with
`μ = partitionShape lam` and `n = N - 1` that is exactly `card_cells_partitionShape` below.  The
step was called "mechanical" in the bean and in PR #5076's body; the *reindex* is, but this
precondition is a genuine missing lemma, which is why it lives in its own file.

## Contents

* `card_cells_eq_sum_rowLen` — `#μ = ∑_{i < colLen 0} rowLen i`, by splitting the cells over rows.
* `colLen_zero_ofRowLens` — a positive row-length list has exactly as many rows as it has entries.
* `card_cells_ofRowLens` — `#(ofRowLens w) = w.sum`, for positive `w`.
* `card_cells_partitionShape` — `#(partitionShape lam) = N` for `lam : Partition N`.

Positivity is not decoration: `ofRowLens` tolerates zero entries in `w`, and a trailing `0` adds no
cells while still lengthening `w`, so `colLen 0 = w.length` genuinely needs `∀ x ∈ w, 0 < x`.
Partitions supply it via `Nat.Partition.parts_pos`.
-/

namespace QOU.Mathlib

open Finset

/-- **The cells of a Young diagram split over its rows.**  Row `i` contributes `rowLen i` cells, and
only rows `i < colLen 0` are nonempty. -/
theorem card_cells_eq_sum_rowLen (μ : YoungDiagram) :
    μ.cells.card = ∑ i ∈ Finset.range (μ.colLen 0), μ.rowLen i := by
  classical
  have hdecomp : μ.cells
      = (Finset.range (μ.colLen 0)).biUnion
          (fun i => (Finset.range (μ.rowLen i)).image (fun j => ((i, j) : ℕ × ℕ))) := by
    ext c
    simp only [Finset.mem_biUnion, Finset.mem_range, Finset.mem_image, YoungDiagram.mem_cells]
    constructor
    · intro hc
      have hc' : (c.1, c.2) ∈ μ := by simpa using hc
      refine ⟨c.1, ?_, c.2, ?_, ?_⟩
      · have h0 : (c.1, 0) ∈ μ := μ.up_left_mem (le_refl c.1) (Nat.zero_le c.2) hc'
        exact YoungDiagram.mem_iff_lt_colLen.mp h0
      · exact YoungDiagram.mem_iff_lt_rowLen.mp hc'
      · rfl
    · rintro ⟨i, _, j, hj, rfl⟩
      simpa using YoungDiagram.mem_iff_lt_rowLen.mpr hj
  rw [hdecomp, Finset.card_biUnion]
  · refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Finset.card_image_of_injective _ (fun a b hab => by simpa using hab), Finset.card_range]
  · intro i _ j _ hij
    simp only [Finset.disjoint_left, Finset.mem_image, Finset.mem_range]
    rintro c ⟨a, _, rfl⟩ ⟨b, _, hb⟩
    exact hij (congrArg Prod.fst hb.symm)

/-- **A positive row-length list has one row per entry.**  Without positivity a trailing `0` would
lengthen `w` without adding a row. -/
theorem colLen_zero_ofRowLens {w : List ℕ} {hw : List.Sorted (· ≥ ·) w}
    (hpos : ∀ x ∈ w, 0 < x) : (YoungDiagram.ofRowLens w hw).colLen 0 = w.length := by
  have key : ∀ i : ℕ, i < (YoungDiagram.ofRowLens w hw).colLen 0 ↔ i < w.length := by
    intro i
    rw [← YoungDiagram.mem_iff_lt_colLen, YoungDiagram.mem_ofRowLens]
    constructor
    · rintro ⟨h, -⟩; exact h
    · intro h; exact ⟨h, hpos _ (List.getElem_mem h)⟩
  refine Nat.le_antisymm ?_ ?_
  · by_contra hcon
    push_neg at hcon
    exact absurd ((key _).mp hcon) (Nat.lt_irrefl _)
  · by_contra hcon
    push_neg at hcon
    exact absurd ((key _).mpr hcon) (Nat.lt_irrefl _)

/-- **The cell count of `ofRowLens` is the sum of the row lengths.** -/
theorem card_cells_ofRowLens {w : List ℕ} {hw : List.Sorted (· ≥ ·) w}
    (hpos : ∀ x ∈ w, 0 < x) : (YoungDiagram.ofRowLens w hw).cells.card = w.sum := by
  rw [card_cells_eq_sum_rowLen, colLen_zero_ofRowLens hpos,
    ← Fin.sum_univ_eq_sum_range (fun i => (YoungDiagram.ofRowLens w hw).rowLen i) w.length]
  have h1 : ∀ i : Fin w.length, (YoungDiagram.ofRowLens w hw).rowLen (i : ℕ) = w[i] :=
    fun i => YoungDiagram.rowLen_ofRowLens i
  simp only [h1]
  rw [← List.sum_ofFn]
  congr 1
  exact List.ofFn_getElem w

/-- **A partition's Young diagram has as many cells as the partition has units.**  This is the
precondition `SeminormalRep.seminormalRep` needs in order to be reindexed onto
`Fin (dLambda lam)` — gap (i) of bean `qou-im9l`. -/
theorem card_cells_partitionShape {N : ℕ} (lam : Nat.Partition N) :
    (partitionShape lam).cells.card = N := by
  classical
  have hpos : ∀ x ∈ lam.parts.sort (· ≥ ·), 0 < x := by
    intro x hx
    exact lam.parts_pos ((Multiset.mem_sort (· ≥ ·)).mp hx)
  rw [partitionShape, card_cells_ofRowLens hpos]
  show (Multiset.sort (· ≥ ·) lam.parts).sum = N
  have hcoe := Multiset.sort_eq (α := ℕ) (· ≥ ·) lam.parts
  calc (Multiset.sort (· ≥ ·) lam.parts).sum
      = Multiset.sum ((Multiset.sort (· ≥ ·) lam.parts : List ℕ) : Multiset ℕ) := rfl
    _ = lam.parts.sum := by rw [hcoe]
    _ = N := lam.parts_sum

end QOU.Mathlib
