import QOU.SchurWeyl.OcneanuWeight
import QOU.Mathlib.YoungDiagramAddCell

/-!
# QOU.SchurWeyl.HookLengthAddCell — how hook lengths move when a cell is added

The first brick for the **arbitrary-`z`** corner identity (bean `qou-j7ln`; the convention-D case
is closed, `MarkovConventionD`).  Read off `ocneanuWeight`'s definition, the weight is

`∏_{x∈μ} [q^{2i}(q²−1−qz) + q^{2j+1}z] / ∏_{x∈μ} [q^{2h(x)} − 1]`,

and the two halves behave completely differently when a cell is added:

* the **numerator** gains exactly one factor, because each factor depends only on that cell's
  `(i, j)` and not on the diagram;
* the **denominator** does not, because `hookLength` *is* diagram-dependent.

This file is that dependence, in closed form.

| | |
|---|---|
| `rowLen_of_isAddableCell`, `colLen_of_isAddableCell` | an addable cell sits at the end of its row and the bottom of its column |
| `hookLength_addCell_self` | the added cell's own hook is `1` |
| `hookLength_addCell_of_mem` | every other cell gains `1` iff it shares the new cell's row or column, and `0` otherwise |

## Why the statement is this clean

The naive expectation is a case split over "arm" and "leg" of `s`.  It collapses, because for
`x ∈ ν` the *order* conditions come free: if `x` shares `s`'s row then `x.2 < rowLen ν x.1 = s.2`
automatically, and symmetrically for the column.  So the hook grows by `1` on exactly the union of
`s`'s row and column, and those two sets meet only at `s` itself — which is not in `ν`.

`not_mem_of_isAddableCell_le` is the one-line reason both filters vanish in
`hookLength_addCell_self`: any cell of `ν` weakly below-right of `s` would drag `s` into `ν` by
`up_left_mem`.

## Scope

Pure `ℕ × ℕ` combinatorics — no ring, nothing archimedean, no `z` and no `q`.  What it does **not**
do is assemble the weight ratio; that is the next brick, and the arm/leg telescoping it needs has
no counterpart in the two-row case, where `schurPrincipal_twoRow` collapsed the whole product.

LaTeX label: `thm:hook-length-add-cell`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib YoungDiagram

/-- No cell of `ν` lies weakly below-right of an addable cell — it would drag `s` into `ν`. -/
theorem not_mem_of_isAddableCell_le {ν : YoungDiagram} {s d : ℕ × ℕ}
    (hs : IsAddableCell ν s) (hd : d ∈ ν) (h1 : s.1 ≤ d.1) (h2 : s.2 ≤ d.2) : False :=
  hs.1 (ν.up_left_mem h1 h2 hd)

/-- **The added cell's own hook is 1.**  It is the last cell of its row and of its column. -/
theorem hookLength_addCell_self (ν : YoungDiagram) (s : ℕ × ℕ) (hs : IsAddableCell ν s) :
    hookLength (addCell ν s hs) s = 1 := by
  classical
  have hcells : (addCell ν s hs).cells = insert s ν.cells := rfl
  have hrow : (ν.cells.filter (fun d => d.1 = s.1 ∧ s.2 ≤ d.2)) = ∅ := by
    refine Finset.filter_eq_empty_iff.mpr ?_
    rintro d hd ⟨h1, h2⟩
    exact not_mem_of_isAddableCell_le hs ((YoungDiagram.mem_cells d).mp hd) (by omega) h2
  have hcol : (ν.cells.filter (fun d => d.2 = s.2 ∧ s.1 < d.1)) = ∅ := by
    refine Finset.filter_eq_empty_iff.mpr ?_
    rintro d hd ⟨h1, h2⟩
    exact not_mem_of_isAddableCell_le hs ((YoungDiagram.mem_cells d).mp hd) (by omega) (by omega)
  unfold hookLength
  rw [hcells, Finset.filter_insert, Finset.filter_insert]
  rw [if_pos ⟨rfl, le_rfl⟩, if_neg (by simp), hrow, hcol]
  simp

/-- An addable cell sits exactly at the end of its row. -/
theorem rowLen_of_isAddableCell {ν : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell ν s) :
    s.2 = ν.rowLen s.1 := by
  obtain ⟨hnot, -, h2⟩ := hs
  have hge : ν.rowLen s.1 ≤ s.2 := by
    by_contra h
    exact hnot (YoungDiagram.mem_iff_lt_rowLen.mpr (by omega))
  rcases h2 with hz | hmem
  · have : s.2 = 0 := hz
    omega
  · have := YoungDiagram.mem_iff_lt_rowLen.mp hmem
    simp only at this
    omega

/-- An addable cell sits exactly at the bottom of its column. -/
theorem colLen_of_isAddableCell {ν : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell ν s) :
    s.1 = ν.colLen s.2 := by
  obtain ⟨hnot, h1, -⟩ := hs
  have hge : ν.colLen s.2 ≤ s.1 := by
    by_contra h
    exact hnot (YoungDiagram.mem_iff_lt_colLen.mpr (by omega))
  rcases h1 with hz | hmem
  · have : s.1 = 0 := hz
    omega
  · have := YoungDiagram.mem_iff_lt_colLen.mp hmem
    simp only at this
    omega

/-- **Hook lengths under `addCell`.**  A cell of `ν` gains exactly one on its hook when the new
cell shares its row or its column, and nothing otherwise. -/
theorem hookLength_addCell_of_mem (ν : YoungDiagram) (s : ℕ × ℕ) (hs : IsAddableCell ν s)
    (x : ℕ × ℕ) (hx : x ∈ ν) :
    hookLength (addCell ν s hs) x
      = hookLength ν x + (if x.1 = s.1 ∨ x.2 = s.2 then 1 else 0) := by
  classical
  have hsn : s ∉ ν.cells := fun h => hs.1 ((YoungDiagram.mem_cells s).mp h)
  have hcells : (addCell ν s hs).cells = insert s ν.cells := rfl
  have hxlt : x.2 < ν.rowLen x.1 := YoungDiagram.mem_iff_lt_rowLen.mp hx
  have hxlt' : x.1 < ν.colLen x.2 := YoungDiagram.mem_iff_lt_colLen.mp hx
  have hrow : (s.1 = x.1 ∧ x.2 ≤ s.2) ↔ x.1 = s.1 := by
    constructor
    · rintro ⟨h, -⟩; exact h.symm
    · intro h
      refine ⟨h.symm, ?_⟩
      have := rowLen_of_isAddableCell hs
      rw [h] at hxlt
      omega
  have hcol : (s.2 = x.2 ∧ x.1 < s.1) ↔ x.2 = s.2 := by
    constructor
    · rintro ⟨h, -⟩; exact h.symm
    · intro h
      refine ⟨h.symm, ?_⟩
      have := colLen_of_isAddableCell hs
      rw [h] at hxlt'
      omega
  have hne : ¬(x.1 = s.1 ∧ x.2 = s.2) := by
    rintro ⟨h1, h2⟩
    exact hsn (by rw [show s = x from Prod.ext h1.symm h2.symm]; exact (YoungDiagram.mem_cells x).mpr hx)
  unfold hookLength
  rw [hcells, Finset.filter_insert, Finset.filter_insert]
  by_cases h1 : x.1 = s.1
  · rw [if_pos (hrow.mpr h1), if_neg (fun hc => hne ⟨h1, hcol.mp hc⟩), if_pos (Or.inl h1),
      Finset.card_insert_of_notMem (fun hm => hsn (Finset.mem_of_mem_filter _ hm))]
    omega
  · by_cases h2 : x.2 = s.2
    · rw [if_neg (fun hc => h1 (hrow.mp hc)), if_pos (hcol.mpr h2), if_pos (Or.inr h2),
        Finset.card_insert_of_notMem (fun hm => hsn (Finset.mem_of_mem_filter _ hm))]
      omega
    · rw [if_neg (fun hc => h1 (hrow.mp hc)), if_neg (fun hc => h2 (hcol.mp hc)),
        if_neg (by tauto)]
      omega

end QOU.SchurWeyl
