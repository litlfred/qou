import QOU.BraidKnot.SpechtGarnirGeom

/-!
# QOU.BraidKnot.SpechtGarnirCard — the Garnir pigeonhole cardinality bound

Piece C of the brick-4 straightening core.  Supplies the strict cardinality
inequality

  `μ.colLen j < (garnirA t j r ∪ garnirB t j r).card`

that drives the Garnir pigeonhole argument: the union of the column-`j` cells in
rows `≥ r` (`garnirA`) and the column-`(j+1)` cells in rows `≤ r` (`garnirB`) has
strictly more labels than the height of column `j`, so any column permutation
must collapse two of them into the same row — the input to
`SpechtGarnirWt`-style straightening.

The two pieces are *disjoint* (a label cannot have column pattern both `j` and
`j+1`), and we count them by transporting along the bijection `t`:

* `|garnirA t j r| = μ.colLen j - r`  — its image under `l ↦ (t l).val` is the
  cell set `{(i, j) : r ≤ i < μ.colLen j}`, in bijection with `Finset.Ico r (μ.colLen j)`.
* `|garnirB t j r| = r + 1`  — its image is `{(i, j+1) : i ≤ r}`, in bijection
  with `Finset.range (r + 1)` (every such row is in `μ` by down-closure from the
  witness cell `(r, j+1) ∈ μ`).

Then `(μ.colLen j - r) + (r + 1) > μ.colLen j` whenever `r < μ.colLen j`.
-/

namespace QOU.BraidKnot.SpechtGarnirCard

open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtGarnirGeom

variable {μ : YoungDiagram}

/-- The label-to-cell map of a tableau, packaged as a function `Fin n → ℕ × ℕ`. -/
private def cellOf (t : Tableau μ) (l : Fin (Specht.nOf μ)) : ℕ × ℕ := (t l : ℕ × ℕ)

private theorem cellOf_injective (t : Tableau μ) : Function.Injective (cellOf t) := by
  intro l l' h
  exact t.injective (Subtype.ext h)

/-- The image of `garnirA t j r` under the cell map is the cell set
`{(i, j) : r ≤ i ∧ i < μ.colLen j}`. -/
private theorem image_garnirA (t : Tableau μ) (j r : ℕ) :
    (garnirA t j r).image (cellOf t)
      = (Finset.Ico r (μ.colLen j)).image (fun i => (i, j)) := by
  ext c
  simp only [Finset.mem_image, garnirA, Finset.mem_filter, Finset.mem_univ, true_and,
    Finset.mem_Ico]
  constructor
  · rintro ⟨l, ⟨hcol, hrow⟩, rfl⟩
    refine ⟨(cellOf t l).1, ⟨?_, ?_⟩, ?_⟩
    · -- r ≤ row
      simpa [cellOf, Specht.rowPattern] using hrow
    · -- row < colLen j
      have hlt := rowPattern_lt_colLen t l
      have : Specht.colPattern t l = j := hcol
      rw [this] at hlt
      simpa [cellOf, Specht.rowPattern] using hlt
    · -- (row, j) = cellOf t l
      have : Specht.colPattern t l = j := hcol
      apply Prod.ext
      · rfl
      · simpa [cellOf, Specht.colPattern] using this.symm
  · rintro ⟨i, ⟨hri, hilt⟩, rfl⟩
    -- the cell (i, j) is in μ since i < colLen j
    have hmem : (i, j) ∈ μ := by
      rw [YoungDiagram.mem_iff_lt_colLen]; exact hilt
    refine ⟨t.symm ⟨(i, j), by rw [YoungDiagram.mem_cells]; exact hmem⟩, ⟨?_, ?_⟩, ?_⟩
    · -- colPattern = j
      show Specht.colPattern t (t.symm _) = j
      simp [Specht.colPattern, Equiv.apply_symm_apply]
    · -- r ≤ rowPattern
      show r ≤ Specht.rowPattern t (t.symm _)
      simp [Specht.rowPattern, Equiv.apply_symm_apply]; exact hri
    · -- cellOf maps back to (i, j)
      show cellOf t (t.symm _) = (i, j)
      simp [cellOf, Equiv.apply_symm_apply]

/-- `|garnirA t j r| = μ.colLen j - r`. -/
theorem card_garnirA (t : Tableau μ) (j r : ℕ) :
    (garnirA t j r).card = μ.colLen j - r := by
  have hinj : (garnirA t j r).card = ((garnirA t j r).image (cellOf t)).card :=
    (Finset.card_image_of_injective _ (cellOf_injective t)).symm
  rw [hinj, image_garnirA]
  rw [Finset.card_image_of_injective _ (by
    intro a b hab; simpa using (Prod.ext_iff.mp hab).1)]
  rw [Nat.card_Ico]

/-- The image of `garnirB t j r` under the cell map is the cell set
`{(i, j+1) : i ≤ r}`, given that row `r` of column `j+1` is in `μ`
(i.e. `r < μ.colLen (j+1)`). -/
private theorem image_garnirB (t : Tableau μ) (j r : ℕ)
    (hrj1 : r < μ.colLen (j + 1)) :
    (garnirB t j r).image (cellOf t)
      = (Finset.range (r + 1)).image (fun i => (i, j + 1)) := by
  ext c
  simp only [Finset.mem_image, garnirB, Finset.mem_filter, Finset.mem_univ, true_and,
    Finset.mem_range]
  constructor
  · rintro ⟨l, ⟨hcol, hrow⟩, rfl⟩
    refine ⟨(cellOf t l).1, ?_, ?_⟩
    · -- row ≤ r  →  row < r + 1
      have : (cellOf t l).1 ≤ r := by simpa [cellOf, Specht.rowPattern] using hrow
      omega
    · -- (row, j+1) = cellOf t l
      have : Specht.colPattern t l = j + 1 := hcol
      apply Prod.ext
      · rfl
      · simpa [cellOf, Specht.colPattern] using this.symm
  · rintro ⟨i, hilt, rfl⟩
    -- (i, j+1) ∈ μ: down-closure from (r, j+1) ∈ μ (since i ≤ r)
    have hrmem : (r, j + 1) ∈ μ := by
      rw [YoungDiagram.mem_iff_lt_colLen]; exact hrj1
    have hile : i ≤ r := by omega
    have hmem : (i, j + 1) ∈ μ :=
      μ.up_left_mem hile (le_refl (j + 1)) hrmem
    refine ⟨t.symm ⟨(i, j + 1), by rw [YoungDiagram.mem_cells]; exact hmem⟩, ⟨?_, ?_⟩, ?_⟩
    · -- colPattern = j+1
      show Specht.colPattern t (t.symm _) = j + 1
      simp [Specht.colPattern, Equiv.apply_symm_apply]
    · -- rowPattern ≤ r
      show Specht.rowPattern t (t.symm _) ≤ r
      simp [Specht.rowPattern, Equiv.apply_symm_apply]; exact hile
    · -- cellOf maps back to (i, j+1)
      show cellOf t (t.symm _) = (i, j + 1)
      simp [cellOf, Equiv.apply_symm_apply]

/-- `|garnirB t j r| = r + 1`, given `r < μ.colLen (j+1)`. -/
theorem card_garnirB (t : Tableau μ) (j r : ℕ) (hrj1 : r < μ.colLen (j + 1)) :
    (garnirB t j r).card = r + 1 := by
  have hinj : (garnirB t j r).card = ((garnirB t j r).image (cellOf t)).card :=
    (Finset.card_image_of_injective _ (cellOf_injective t)).symm
  rw [hinj, image_garnirB t j r hrj1]
  rw [Finset.card_image_of_injective _ (by
    intro a b hab; simpa using (Prod.ext_iff.mp hab).1)]
  rw [Finset.card_range]

/-- `garnirA` and `garnirB` are disjoint: a label cannot have column pattern both
`j` and `j+1`. -/
theorem disjoint_garnirAB (t : Tableau μ) (j r : ℕ) :
    Disjoint (garnirA t j r) (garnirB t j r) := by
  rw [Finset.disjoint_left]
  intro l hA hB
  rw [garnirA, Finset.mem_filter] at hA
  rw [garnirB, Finset.mem_filter] at hB
  have h1 : Specht.colPattern t l = j := hA.2.1
  have h2 : Specht.colPattern t l = j + 1 := hB.2.1
  omega

/-- **The Garnir pigeonhole cardinality bound.** The union of the column-`j`
Garnir cells (rows `≥ r`) and the column-`(j+1)` Garnir cells (rows `≤ r`) has
strictly more labels than the height of column `j`. -/
theorem garnir_card_gt {t : Tableau μ} {j r : ℕ}
    (hrj  : r < μ.colLen j)
    (hrj1 : r < μ.colLen (j + 1)) :
    μ.colLen j < (garnirA t j r ∪ garnirB t j r).card := by
  rw [Finset.card_union_of_disjoint (disjoint_garnirAB t j r),
    card_garnirA t j r, card_garnirB t j r hrj1]
  omega

end QOU.BraidKnot.SpechtGarnirCard
