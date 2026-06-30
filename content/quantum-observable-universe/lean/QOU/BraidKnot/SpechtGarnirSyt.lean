import QOU.BraidKnot.SpechtGarnirGeom
import QOU.BraidKnot.SpechtStandardBasis

/-!
# QOU.BraidKnot.SpechtGarnirSyt — row+column monotone ⟹ standard Young tableau

The straightening step of the Specht standard-basis program (brick 4) needs the
classical fact that a (general) tableau `t : Tableau μ` whose **rows** and
**columns** are both monotone in the label order is, up to the `sytToTableau`
encoding, a *standard* Young tableau.

Concretely: a tableau is column-monotone (`ColMono`, from
`SpechtGarnirGeom`) when labels strictly increase down each column as a function
of the row, and row-monotone (`RowMono`, defined here) when labels strictly
increase along each row as a function of the column. The theorem
`mono_eq_syt` constructs a `StandardYoungTableau μ` whose `sytToTableau` is the
given `t`.

The construction reads `t.symm` as the entry filling: the entry at cell `(i, j)`
is the label `t.symm` assigns to that cell (and `0` off the diagram). The six
`StandardYoungTableau` fields are then discharged from the two monotonicity
hypotheses plus the bijectivity of `t`; the recovery `sytToTableau T = t`
follows from `cellLabel T (t l) = l`.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.5 (standard tableaux; the
  row-and-column standard condition is the definition of an SYT).
-/

namespace QOU.BraidKnot.SpechtGarnirSyt

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtStandardBasis

variable {μ : YoungDiagram}

/-- **Row-monotonicity** (the row-standard condition): within each row, labels
increase as the column increases. Mirror of `SpechtGarnirGeom.ColMono`. -/
def RowMono (t : Tableau μ) : Prop :=
  ∀ l l' : Fin (nOf μ), Specht.rowPattern t l = Specht.rowPattern t l' →
    Specht.colPattern t l < Specht.colPattern t l' → (l : ℕ) < (l' : ℕ)

/-- The entry-filling read off a tableau `t`: the label `t.symm` assigns to the
cell `(i, j)` when it lies in `μ`, and `0` off the diagram. -/
noncomputable def entryOf (t : Tableau μ) (i j : ℕ) : ℕ :=
  if h : (i, j) ∈ μ then
    ((t.symm ⟨(i, j), (YoungDiagram.mem_cells _).mpr h⟩ : Fin (nOf μ)) : ℕ)
  else 0

/-- On a cell of `μ`, `entryOf t` is the val of `t.symm` of that cell. -/
theorem entryOf_cell (t : Tableau μ) {i j : ℕ} (h : (i, j) ∈ μ) :
    entryOf t i j = ((t.symm ⟨(i, j), (YoungDiagram.mem_cells _).mpr h⟩ : Fin (nOf μ)) : ℕ) := by
  rw [entryOf, dif_pos h]

/-- The standard Young tableau built from a row-and-column-monotone tableau. -/
noncomputable def toSYT {t : Tableau μ}
    (hcol : SpechtGarnirGeom.ColMono t) (hrow : RowMono t) :
    StandardYoungTableau μ where
  entry := entryOf t
  lt_card := by
    intro i j h
    rw [entryOf_cell t h]
    have hlt := (t.symm ⟨(i, j), (YoungDiagram.mem_cells _).mpr h⟩).isLt
    -- `nOf μ = μ.card` definitionally (abbrev)
    exact hlt
  zero_off := by
    intro i j h
    rw [entryOf, dif_neg h]
  inj_on := by
    intro i j i' j' h h' heq
    rw [entryOf_cell t h, entryOf_cell t h'] at heq
    -- equal vals ⇒ equal Fin elements ⇒ equal cells (t.symm injective)
    have hfin : t.symm ⟨(i, j), (YoungDiagram.mem_cells _).mpr h⟩
        = t.symm ⟨(i', j'), (YoungDiagram.mem_cells _).mpr h'⟩ := Fin.ext heq
    have hcell : (⟨(i, j), (YoungDiagram.mem_cells _).mpr h⟩ : μ.cells)
        = ⟨(i', j'), (YoungDiagram.mem_cells _).mpr h'⟩ := t.symm.injective hfin
    have : (i, j) = (i', j') := congrArg Subtype.val hcell
    exact ⟨congrArg Prod.fst this, congrArg Prod.snd this⟩
  row_strict := by
    intro i j hmem
    -- (i, j) ∈ μ by down-closure
    have hmem0 : (i, j) ∈ μ := μ.up_left_mem (le_refl i) (Nat.le_succ j) hmem
    set c0 : μ.cells := ⟨(i, j), (YoungDiagram.mem_cells _).mpr hmem0⟩ with hc0
    set c1 : μ.cells := ⟨(i, j + 1), (YoungDiagram.mem_cells _).mpr hmem⟩ with hc1
    set l := t.symm c0 with hl
    set l' := t.symm c1 with hl'
    have hrl : Specht.rowPattern t l = i := by
      rw [Specht.rowPattern, hl, hc0]; simp [Equiv.apply_symm_apply]
    have hrl' : Specht.rowPattern t l' = i := by
      rw [Specht.rowPattern, hl', hc1]; simp [Equiv.apply_symm_apply]
    have hcl : Specht.colPattern t l = j := by
      rw [Specht.colPattern, hl, hc0]; simp [Equiv.apply_symm_apply]
    have hcl' : Specht.colPattern t l' = j + 1 := by
      rw [Specht.colPattern, hl', hc1]; simp [Equiv.apply_symm_apply]
    have hrow_eq : Specht.rowPattern t l = Specht.rowPattern t l' := by rw [hrl, hrl']
    have hcol_lt : Specht.colPattern t l < Specht.colPattern t l' := by
      rw [hcl, hcl']; exact Nat.lt_succ_self j
    have hlt : (l : ℕ) < (l' : ℕ) := hrow l l' hrow_eq hcol_lt
    rw [entryOf_cell t hmem0, entryOf_cell t hmem]
    exact hlt
  col_strict := by
    intro i j hmem
    have hmem0 : (i, j) ∈ μ := μ.up_left_mem (Nat.le_succ i) (le_refl j) hmem
    set c0 : μ.cells := ⟨(i, j), (YoungDiagram.mem_cells _).mpr hmem0⟩ with hc0
    set c1 : μ.cells := ⟨(i + 1, j), (YoungDiagram.mem_cells _).mpr hmem⟩ with hc1
    set l := t.symm c0 with hl
    set l' := t.symm c1 with hl'
    have hrl : Specht.rowPattern t l = i := by
      rw [Specht.rowPattern, hl, hc0]; simp [Equiv.apply_symm_apply]
    have hrl' : Specht.rowPattern t l' = i + 1 := by
      rw [Specht.rowPattern, hl', hc1]; simp [Equiv.apply_symm_apply]
    have hcl : Specht.colPattern t l = j := by
      rw [Specht.colPattern, hl, hc0]; simp [Equiv.apply_symm_apply]
    have hcl' : Specht.colPattern t l' = j := by
      rw [Specht.colPattern, hl', hc1]; simp [Equiv.apply_symm_apply]
    have hcol_eq : Specht.colPattern t l = Specht.colPattern t l' := by rw [hcl, hcl']
    have hrow_lt : Specht.rowPattern t l < Specht.rowPattern t l' := by
      rw [hrl, hrl']; exact Nat.lt_succ_self i
    have hlt : (l : ℕ) < (l' : ℕ) := hcol l l' hcol_eq hrow_lt
    rw [entryOf_cell t hmem0, entryOf_cell t hmem]
    exact hlt

/-- The entry of `toSYT` at a cell equals the val of `cellLabel`'s preimage; the
key bridge for recovering `t`. For a cell `c = t l`, the entry of `toSYT` at `c`
is `(t.symm c : ℕ) = (l : ℕ)`. -/
theorem cellLabel_toSYT {t : Tableau μ}
    (hcol : SpechtGarnirGeom.ColMono t) (hrow : RowMono t) (l : Fin (nOf μ)) :
    cellLabel (toSYT hcol hrow) (t l) = l := by
  -- `cellLabel T c` has val `T.entry c.1.1 c.1.2`; for c = t l this is the
  -- val of `t.symm (t l) = l`.
  apply Fin.ext
  -- unfold cellLabel: val = entry (t l).1.1 (t l).1.2
  show ((toSYT hcol hrow).entry ((t l).1.1) ((t l).1.2) : ℕ) = (l : ℕ)
  have hmem : (((t l).1.1), ((t l).1.2)) ∈ μ := by
    have := (t l).2
    rwa [YoungDiagram.mem_cells] at this
  have hentry : (toSYT hcol hrow).entry ((t l).1.1) ((t l).1.2)
      = ((t.symm ⟨(((t l).1.1), ((t l).1.2)), (YoungDiagram.mem_cells _).mpr hmem⟩ : Fin (nOf μ)) : ℕ) := by
    show entryOf t ((t l).1.1) ((t l).1.2) = _
    rw [entryOf_cell t hmem]
  rw [hentry]
  -- the cell `⟨((t l).1.1, (t l).1.2), _⟩` equals `t l`, so `t.symm` of it is `l`
  have hcell : (⟨(((t l).1.1), ((t l).1.2)), (YoungDiagram.mem_cells _).mpr hmem⟩ : μ.cells)
      = t l := by
    apply Subtype.ext
    rfl
  rw [hcell, Equiv.symm_apply_apply]

/-- **Row-and-column monotone tableau is a standard Young tableau.** Given a
tableau `t` whose rows and columns are both monotone in the label order, there is
a standard Young tableau `T` with `sytToTableau T = t`. -/
theorem mono_eq_syt {t : Tableau μ}
    (hcol : SpechtGarnirGeom.ColMono t) (hrow : RowMono t) :
    ∃ T : StandardYoungTableau μ, sytToTableau T = t := by
  refine ⟨toSYT hcol hrow, ?_⟩
  -- `sytToTableau T = (cellLabel T equiv).symm`; show it agrees with `t` on every label
  apply Equiv.ext
  intro l
  -- it suffices `cellLabel T (t l) = l`, then apply the equiv
  have h := cellLabel_toSYT hcol hrow l
  -- `sytToTableau T l = (Equiv.ofBijective (cellLabel T) _).symm l`
  rw [sytToTableau]
  -- apply the bijection to both sides of `cellLabel T (t l) = l`
  have hb := cellLabel_bijective (toSYT hcol hrow)
  apply (Equiv.ofBijective (cellLabel (toSYT hcol hrow)) hb).injective
  rw [Equiv.apply_symm_apply]
  -- goal: l = Equiv.ofBijective (cellLabel T) hb (t l), i.e. l = cellLabel T (t l)
  exact h.symm

end QOU.BraidKnot.SpechtGarnirSyt
