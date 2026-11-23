/-
  The column-superstandard filling as an honest `StandardYoungTableau`.

  `ColSuperstandardTableau.colSuperstandard μ : Specht.Tableau μ` is a bare
  bijection `Fin (nOf μ) ≃ μ.cells`.  The Okounkov–Vershik statement
  `JucysMurphy.seminormalVector_base_exists` quantifies instead over
  `StandardYoungTableau μ` and reads cells through
  `JucysMurphy.tableauCellEquiv`.  This file supplies the missing bridge:

    * `colSuperstandardSYT μ : StandardYoungTableau μ`, and
    * `tableauCellEquiv μ (colSuperstandardSYT μ) = colSuperstandard μ`.

  Both come from the pre-existing recognition pair
  `SpechtStandardBasis.sytOfStrict` / `sytToTableau_sytOfStrict`, so nothing
  here re-proves SYT recognition; the only content is that the
  column-major filling really is strict along rows and down columns, which is
  `lt_iff_colRow` read in the two degenerate directions.

  Base ring: none — this is tableau combinatorics only, no `k`, no `ℝ`
  (AGENTS.md §7c).

  Refs: prop:ov-seminormal-base-vector,
        [vershik-kerov1977] Vershik–Kerov, Young's seminormal form,
        [sagan2001] Sagan, "The Symmetric Group", §2.5–2.6.
-/

import QOU.BraidKnot.ColSuperstandardTableau
import QOU.BraidKnot.SpechtStandardBasisCore

namespace QOU.BraidKnot.ColSuperstandardTableau

open QOU.BraidKnot

/-- Reading the column-superstandard filling at the label it assigns to `(i, j)`
returns `(i, j)`.  Pure `Equiv.apply_symm_apply`, isolated because the two
strictness proofs below each use it twice and the coercion tower
(`μ.cells → ℕ × ℕ`) makes it awkward inline. -/
theorem coe_apply_symm (μ : YoungDiagram) {i j : ℕ} (h : (i, j) ∈ μ) :
    ((colSuperstandard μ ((colSuperstandard μ).symm
        ⟨(i, j), (YoungDiagram.mem_cells (i, j)).2 h⟩) : {c // c ∈ μ.cells}) : ℕ × ℕ)
      = (i, j) := by
  rw [Equiv.apply_symm_apply]

/-- **Row-strictness.** `(i, j)` and `(i, j + 1)` sit in *different* columns, so
`lt_iff_colRow`'s first disjunct applies and the label order is the column order
`j < j + 1`. -/
theorem labelAt_row_strict (μ : YoungDiagram) (i j : ℕ)
    (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ) :
    SpechtStandardBasis.labelAt (colSuperstandard μ) hij
      < SpechtStandardBasis.labelAt (colSuperstandard μ) hij1 := by
  simp only [SpechtStandardBasis.labelAt]
  rw [← Fin.lt_def, lt_iff_colRow]
  left
  rw [coe_apply_symm μ hij, coe_apply_symm μ hij1]
  exact Nat.lt_succ_self j

/-- **Column-strictness.** `(i, j)` and `(i + 1, j)` share column `j`, so the
first disjunct of `lt_iff_colRow` is unavailable and the second one — same
column, smaller row — gives `i < i + 1`. -/
theorem labelAt_col_strict (μ : YoungDiagram) (i j : ℕ)
    (hij : (i, j) ∈ μ) (hi1j : (i + 1, j) ∈ μ) :
    SpechtStandardBasis.labelAt (colSuperstandard μ) hij
      < SpechtStandardBasis.labelAt (colSuperstandard μ) hi1j := by
  simp only [SpechtStandardBasis.labelAt]
  rw [← Fin.lt_def, lt_iff_colRow]
  right
  rw [coe_apply_symm μ hij, coe_apply_symm μ hi1j]
  exact ⟨rfl, Nat.lt_succ_self i⟩

/-- **The column-superstandard tableau, as a `StandardYoungTableau`.** -/
noncomputable def colSuperstandardSYT (μ : YoungDiagram) :
    QOU.BraidKnot.StandardYoungTableau μ :=
  SpechtStandardBasis.sytOfStrict (colSuperstandard μ)
    (fun i j hij hij1 => labelAt_row_strict μ i j hij hij1)
    (fun i j hij hi1j => labelAt_col_strict μ i j hij hi1j)

/-- **The bridge.** Reading `colSuperstandardSYT μ` back through the
label→cell bijection returns the original column-superstandard filling, so every
`colSuperstandard`-indexed statement transfers verbatim to the SYT-indexed
`seminormalVector_base_exists`. -/
theorem sytToTableau_colSuperstandardSYT (μ : YoungDiagram) :
    SpechtStandardBasis.sytToTableau (colSuperstandardSYT μ) = colSuperstandard μ :=
  SpechtStandardBasis.sytToTableau_sytOfStrict _ _ _

/-- Strictness of column-adjacent labels in the column-superstandard filling implies inequality (`qou-geqa`). -/
theorem labelAt_col_ne (μ : YoungDiagram) (i j : ℕ)
    (hij : (i, j) ∈ μ) (hi1j : (i + 1, j) ∈ μ) :
    SpechtStandardBasis.labelAt (colSuperstandard μ) hij
      ≠ SpechtStandardBasis.labelAt (colSuperstandard μ) hi1j :=
  ne_of_lt (labelAt_col_strict μ i j hij hi1j)

end QOU.BraidKnot.ColSuperstandardTableau
