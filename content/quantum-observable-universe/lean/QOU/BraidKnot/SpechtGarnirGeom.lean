import QOU.BraidKnot.Specht

/-!
# QOU.BraidKnot.SpechtGarnirGeom — tableau-geometry foundation for the Garnir construction

Piece B of the brick-4 straightening core. This file supplies the *geometric*
hypotheses the abstract Garnir machinery (`SpechtGarnirWt.colWt_lt_of_two_column`,
`hbh_of_moved_top`) consumes — built from cell geometry, with no dependence on the
abstract dominance lemmas.

Key facts:
* `cell_inj` — a cell determines its label (`t` is a bijection): equal row **and**
  column pattern forces equal label.
* `ColMono` — column-monotonicity: labels increase down each column (the
  column-standard condition, stated on patterns).
* `all_B_lt_all_A` — the all-`B`<all-`A` fact at a row-violation: in a
  column-monotone tableau with a row-descent at row `r` (column-`(j+1)` label `<`
  column-`j` label), every column-`(j+1)` label in rows `≤ r` is `<` every
  column-`j` label in rows `≥ r`. This is the `htop` hypothesis of the Garnir
  bottom-heaviness — the column-`j` Garnir cells hold the largest labels.
-/

namespace QOU.BraidKnot.SpechtGarnirGeom

open QOU.BraidKnot.Specht

variable {μ : YoungDiagram}

/-- **A cell determines its label.** Since a tableau is a bijection `Fin n ≃ μ.cells`,
two labels in the same row and column are equal. -/
theorem cell_inj {t : Tableau μ} {l l' : Fin (Specht.nOf μ)}
    (hc : Specht.colPattern t l = Specht.colPattern t l')
    (hr : Specht.rowPattern t l = Specht.rowPattern t l') : l = l' :=
  t.injective (Subtype.ext (Prod.ext hr hc))

/-- **Column-monotonicity** (the column-standard condition): within each column,
labels increase as the row increases. -/
def ColMono (t : Tableau μ) : Prop :=
  ∀ l l' : Fin (Specht.nOf μ), Specht.colPattern t l = Specht.colPattern t l' →
    Specht.rowPattern t l < Specht.rowPattern t l' → (l : ℕ) < (l' : ℕ)

/-- The `≤` form of column-monotonicity (equality of rows forces equality of labels
by `cell_inj`). -/
theorem colMono_le {t : Tableau μ} (h : ColMono t) {l l' : Fin (Specht.nOf μ)}
    (hc : Specht.colPattern t l = Specht.colPattern t l')
    (hr : Specht.rowPattern t l ≤ Specht.rowPattern t l') : (l : ℕ) ≤ (l' : ℕ) := by
  rcases eq_or_lt_of_le hr with he | hlt
  · exact le_of_eq (by rw [cell_inj hc he])
  · exact le_of_lt (h l l' hc hlt)

/-- **all-`B`<all-`A` at a row-violation.** In a column-monotone tableau with a
row-descent at row `r` between columns `j` and `j+1` (the column-`(j+1)` label `b_r`
in row `r` is `<` the column-`j` label `a_r` in row `r`), every column-`(j+1)`
label `b` in rows `≤ r` is strictly less than every column-`j` label `a` in rows
`≥ r`. The column-`j` Garnir cells (rows `≥ r`) thus hold the largest labels — the
`htop` hypothesis. -/
theorem all_B_lt_all_A {t : Tableau μ} (h : ColMono t) {j r : ℕ}
    {ar br : Fin (Specht.nOf μ)}
    (har : Specht.colPattern t ar = j) (harr : Specht.rowPattern t ar = r)
    (hbr : Specht.colPattern t br = j + 1) (hbrr : Specht.rowPattern t br = r)
    (hviol : (br : ℕ) < (ar : ℕ))
    {a b : Fin (Specht.nOf μ)}
    (haj : Specht.colPattern t a = j) (har_ge : r ≤ Specht.rowPattern t a)
    (hbj : Specht.colPattern t b = j + 1) (hbr_le : Specht.rowPattern t b ≤ r) :
    (b : ℕ) < (a : ℕ) := by
  have hb : (b : ℕ) ≤ (br : ℕ) :=
    colMono_le h (by rw [hbj, hbr]) (by rw [hbrr]; exact hbr_le)
  have ha : (ar : ℕ) ≤ (a : ℕ) :=
    colMono_le h (by rw [har, haj]) (by rw [harr]; exact har_ge)
  omega

/-- The **Garnir column-`j` cells** `A`: labels in column `j`, rows `≥ r`. -/
def garnirA (t : Tableau μ) (j r : ℕ) : Finset (Fin (Specht.nOf μ)) :=
  Finset.univ.filter (fun l => Specht.colPattern t l = j ∧ r ≤ Specht.rowPattern t l)

/-- The **Garnir column-`(j+1)` cells** `B`: labels in column `j+1`, rows `≤ r`. -/
def garnirB (t : Tableau μ) (j r : ℕ) : Finset (Fin (Specht.nOf μ)) :=
  Finset.univ.filter (fun l => Specht.colPattern t l = j + 1 ∧ Specht.rowPattern t l ≤ r)

/-- **The `htop` hypothesis for the Garnir set.** Every element of `garnirA ∪ garnirB`
outside `garnirA` (i.e. in `garnirB`) is `<` every element of `garnirA`. Exactly the
shape `SpechtGarnirWt.hbh_of_moved_top` / `colWt_lt_of_two_column` require. -/
theorem garnir_htop {t : Tableau μ} (h : ColMono t) {j r : ℕ}
    {ar br : Fin (Specht.nOf μ)}
    (har : Specht.colPattern t ar = j) (harr : Specht.rowPattern t ar = r)
    (hbr : Specht.colPattern t br = j + 1) (hbrr : Specht.rowPattern t br = r)
    (hviol : (br : ℕ) < (ar : ℕ)) :
    ∀ a ∈ garnirA t j r, ∀ s ∈ garnirA t j r ∪ garnirB t j r,
      s ∉ garnirA t j r → (s : ℕ) < (a : ℕ) := by
  intro a ha s hs hsA
  rw [garnirA, Finset.mem_filter] at ha
  rw [Finset.mem_union] at hs
  rcases hs with hsA' | hsB
  · exact absurd hsA' hsA
  · rw [garnirB, Finset.mem_filter] at hsB
    exact all_B_lt_all_A h har harr hbr hbrr hviol ha.2.1 ha.2.2 hsB.2.1 hsB.2.2

/-! ## The pigeonhole row bound (item 2, `hbound` half) -/

/-- The row of any label is `< ` the length of its column: the cell holding label
`l` lies in `μ`, so `(rowPattern, colPattern)` satisfies `mem_iff_lt_colLen`. -/
theorem rowPattern_lt_colLen (t : Tableau μ) (l : Fin (Specht.nOf μ)) :
    Specht.rowPattern t l < μ.colLen (Specht.colPattern t l) := by
  have hmem : ((t l : ℕ × ℕ).1, (t l : ℕ × ℕ).2) ∈ μ := (t l).2
  rw [YoungDiagram.mem_iff_lt_colLen] at hmem
  exact hmem

/-- **The Garnir row bound** (`hbound` with `m = μ.colLen j`). For any column
permutation `π ∈ C_t` and any Garnir label `l ∈ garnirA ∪ garnirB` (column `j` or
`j+1`), the row of `l` in `π·t` is `< μ.colLen j` — column permutations keep `l`
in its column, whose length is `≤ μ.colLen j` by antitonicity. -/
theorem garnir_rowBound (t : Tableau μ) (j r : ℕ) (π : Specht.colStab t)
    {l : Fin (Specht.nOf μ)} (hl : l ∈ garnirA t j r ∪ garnirB t j r) :
    Specht.rowPattern ((π : Equiv.Perm (Fin (Specht.nOf μ))) • t) l < μ.colLen j := by
  have hcol : Specht.colPattern ((π : Equiv.Perm (Fin (Specht.nOf μ))) • t) l
      = Specht.colPattern t l := by
    rw [Specht.colPattern_smul]; exact congrFun (Specht.mem_colStab.mp π.2) l
  have hlt := rowPattern_lt_colLen ((π : Equiv.Perm (Fin (Specht.nOf μ))) • t) l
  rw [hcol] at hlt
  have hcj : Specht.colPattern t l = j ∨ Specht.colPattern t l = j + 1 := by
    rw [Finset.mem_union, garnirA, garnirB, Finset.mem_filter, Finset.mem_filter] at hl
    rcases hl with ⟨_, h, _⟩ | ⟨_, h, _⟩
    · exact Or.inl h
    · exact Or.inr h
  rcases hcj with h | h
  · rw [h] at hlt; exact hlt
  · rw [h] at hlt
    exact lt_of_lt_of_le hlt (μ.colLen_anti j (j + 1) (Nat.le_succ j))

end QOU.BraidKnot.SpechtGarnirGeom
