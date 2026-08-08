import QOU.BraidKnot.OVBaseSeminormalVector

/-!
# QOU.BraidKnot.ColSuperstandardTableau — the column-superstandard tableau

Constructs the **column-superstandard** tableau of a Young diagram: the labelling that
fills cells column by column, top to bottom, left to right. This is the tableau whose
polytabloid is the Okounkov–Vershik base seminormal vector
(`JucysMurphy.seminormalVector_base_exists`, bean `sv8b`).

Before this file the tableau did not exist anywhere in the corpus. Note the *row*-
superstandard tableau that does exist (`SytRowSuperstandard`) is **not** the right object:
its polytabloid is not a JM eigenvector, so building toward it would be proving a false
statement (audit `2026-07-19-ov-base-vector-column-superstandard-verification.md`).

## The construction

`Specht.Tableau μ` is *definitionally* `Fin (nOf μ) ≃ μ.cells`, and `nOf μ = μ.cells.card`
by `rfl`. So the column-superstandard tableau is not a hand-rolled enumeration — it **is**
the order isomorphism `Finset.orderIsoOfFin` for the column-then-row lexicographic order on
cells.

## Why the order lives on `ℕ ×ₗ ℕ` and not on `ℕ × ℕ`

The obvious route — declare `LinearOrder (ℕ × ℕ)` by column-then-row and apply
`orderIsoOfFin` to `μ.cells` directly — **does not work**, and fails in a way that looks
like it should. `ℕ × ℕ` already carries Mathlib's componentwise order `Prod.instLE_mathlib`,
so a competing `LinearOrder` instance forms a diamond: the bare definition elaborates, but
every declaration that *annotates* the type resolves `LE` to the ambient componentwise
instance and mismatches —

    has type      @OrderIso … (@Subtype.instLE _ instDistribLatticeOfLinearOrder.…toLE _)
    but expected  @OrderIso … (@Subtype.instLE _ Prod.instLE_mathlib _)

— and every order lemma below states the order, so all of them would hit it. It is an
instance-level mismatch, not a syntactic one; `show`/`unfold` do not fix it.

Instead we map the cells into Mathlib's **existing** lex synonym `ℕ ×ₗ ℕ` (whose
`LinearOrder` is the intended instance, no diamond) via `swapLex`, take the order
isomorphism there, and transport back. `ℕ × ℕ`'s Mathlib order is left untouched, so
nothing else in the tree that reasons about cells is disturbed.

-- Ref: [vershik-kerov1977] Vershik–Kerov, Young's seminormal form
-- Ref: [sagan2001] Sagan, The Symmetric Group §2.5–§3.1
-/

namespace QOU.BraidKnot.ColSuperstandardTableau

open QOU.BraidKnot

/-- Cell `(row, col)` ↦ lex key `(col, row)`. Composing `prodComm` with `toLex` puts the
column first, so the lex order on keys is exactly "column-major, then row". -/
def swapLex : (ℕ × ℕ) ≃ (ℕ ×ₗ ℕ) := (Equiv.prodComm ℕ ℕ).trans (toLex (α := ℕ × ℕ))

/-- The cells of `μ`, carried into the lex synonym where the order lives. -/
def lexCells (μ : YoungDiagram) : Finset (ℕ ×ₗ ℕ) := μ.cells.map swapLex.toEmbedding

theorem lexCells_card (μ : YoungDiagram) : (lexCells μ).card = Specht.nOf μ := by
  simp [lexCells, Specht.nOf, YoungDiagram.card]

/-- Transport back: a lex key in `lexCells μ` is a cell of `μ`. -/
def lexCellsEquiv (μ : YoungDiagram) : {x // x ∈ lexCells μ} ≃ {y // y ∈ μ.cells} :=
  Equiv.subtypeEquiv swapLex.symm (fun x => by simp [lexCells, Finset.mem_map_equiv])

/-- The order isomorphism `Fin (nOf μ) ≃o lexCells μ` — labels in increasing key order. -/
noncomputable def lexIso (μ : YoungDiagram) : Fin (Specht.nOf μ) ≃o {x // x ∈ lexCells μ} :=
  (lexCells μ).orderIsoOfFin (lexCells_card μ)

/-- **The column-superstandard tableau**: label `l` sits at the `l`-th cell in
column-then-row order. -/
noncomputable def colSuperstandard (μ : YoungDiagram) : Specht.Tableau μ :=
  (lexIso μ).toEquiv.trans (lexCellsEquiv μ)

/-- The lex key of label `l`'s cell is exactly `lexIso`'s value at `l`. -/
theorem key_apply (μ : YoungDiagram) (l : Fin (Specht.nOf μ)) :
    swapLex (colSuperstandard μ l : ℕ × ℕ) = (lexIso μ l : ℕ ×ₗ ℕ) := by
  simp [colSuperstandard, lexCellsEquiv, Equiv.subtypeEquiv]

/-- Label order is exactly lex-key order. -/
theorem lt_iff_key (μ : YoungDiagram) (l m : Fin (Specht.nOf μ)) :
    l < m ↔ swapLex (colSuperstandard μ l : ℕ × ℕ) < swapLex (colSuperstandard μ m : ℕ × ℕ) := by
  rw [key_apply, key_apply]
  exact ((lexIso μ).lt_iff_lt).symm

/-- **The defining property — column-major.** Label `l` precedes `m` iff `l`'s cell is in an
earlier column, or the same column and an earlier row. -/
theorem lt_iff_colRow (μ : YoungDiagram) (l m : Fin (Specht.nOf μ)) :
    l < m ↔ ((colSuperstandard μ l : ℕ × ℕ).2 < (colSuperstandard μ m : ℕ × ℕ).2
      ∨ ((colSuperstandard μ l : ℕ × ℕ).2 = (colSuperstandard μ m : ℕ × ℕ).2
        ∧ (colSuperstandard μ l : ℕ × ℕ).1 < (colSuperstandard μ m : ℕ × ℕ).1)) := by
  rw [lt_iff_key]
  exact Prod.Lex.lt_iff

/-- Within a fixed column, label order is row order. The specialisation of
`lt_iff_colRow` that the same-column count consumes. -/
theorem lt_iff_row_of_sameCol (μ : YoungDiagram) {l m : Fin (Specht.nOf μ)}
    (hcol : (colSuperstandard μ l : ℕ × ℕ).2 = (colSuperstandard μ m : ℕ × ℕ).2) :
    l < m ↔ (colSuperstandard μ l : ℕ × ℕ).1 < (colSuperstandard μ m : ℕ × ℕ).1 := by
  rw [lt_iff_colRow]
  constructor
  · rintro (h | ⟨_, h⟩)
    · exact absurd hcol (Nat.ne_of_lt h)
    · exact h
  · intro h; exact Or.inr ⟨hcol, h⟩

/-! ### Bridging `colStab` membership to the column pattern

`colPattern t l` is the column of label `l`, so for a transposition, lying in the column
stabiliser is exactly "same column". `SpechtStandardBasisCore.colStab_swap_mem` supplies
the forward direction; the converse is evaluation at `a`. -/

/-- **Same column ↔ the transposition stabilises the column pattern.** -/
theorem swap_mem_colStab_iff {μ : YoungDiagram} (t : Specht.Tableau μ)
    {a b : Fin (Specht.nOf μ)} :
    Equiv.swap a b ∈ Specht.colStab t ↔ Specht.colPattern t a = Specht.colPattern t b := by
  constructor
  · intro h
    have h' := congrFun (Specht.mem_colStab.mp h) a
    rw [Specht.arrow_smul_apply, Equiv.symm_swap, Equiv.swap_apply_left] at h'
    exact h'.symm
  · exact SpechtStandardBasis.colStab_swap_mem t

/-- `colPattern` of the column-superstandard tableau is the cell's column. -/
theorem colPattern_colSuperstandard (μ : YoungDiagram) (l : Fin (Specht.nOf μ)) :
    Specht.colPattern (colSuperstandard μ) l = (colSuperstandard μ l : ℕ × ℕ).2 := rfl

/-! ### The same-column count — the first half of the eigen-equation

`OVBaseSeminormalVector.jm_polytabloid_split` writes the JM action on `e_t` as

  `X_s · e_t = (same-column count) · (−e_t) + (off-column Garnir sum)`,

where the same-column count is `#{j < s : (j s) ∈ colStab t}`. For the
column-superstandard tableau that count is exactly the **row index** of `s`'s cell,
which is where the `−i` of `content (i,j) = j − i` comes from. -/

/-- The `colStab` filter is exactly a (same column, smaller row) condition. -/
theorem sameColumn_filter_eq (μ : YoungDiagram) (s : Fin (Specht.nOf μ)) :
    Finset.univ.filter (fun j : Fin (Specht.nOf μ) =>
        j.val < s.val ∧ Equiv.swap j s ∈ Specht.colStab (colSuperstandard μ))
      = Finset.univ.filter (fun j : Fin (Specht.nOf μ) =>
        (colSuperstandard μ j : ℕ × ℕ).2 = (colSuperstandard μ s : ℕ × ℕ).2
          ∧ (colSuperstandard μ j : ℕ × ℕ).1 < (colSuperstandard μ s : ℕ × ℕ).1) := by
  ext j
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  rw [swap_mem_colStab_iff, colPattern_colSuperstandard, colPattern_colSuperstandard]
  constructor
  · rintro ⟨hlt, hcol⟩
    exact ⟨hcol, (lt_iff_row_of_sameCol μ hcol).mp (Fin.lt_def.mpr hlt)⟩
  · rintro ⟨hcol, hrow⟩
    exact ⟨Fin.lt_def.mp ((lt_iff_row_of_sameCol μ hcol).mpr hrow), hcol⟩

/-- **The same-column count is the row index.** For the column-superstandard tableau,
`#{j < s : (j s) ∈ colStab}` equals the row of `s`'s cell.

The bijection sends `j` to its row. It lands in `range (row s)` by
`sameColumn_filter_eq`; it is injective because a label is determined by its cell and
the column is pinned; and it is surjective because a Young diagram is down-closed in
columns (`YoungDiagram.up_left_mem`), so every row below `s`'s in the same column is
occupied. -/
theorem sameColumn_count (μ : YoungDiagram) (s : Fin (Specht.nOf μ)) :
    (Finset.univ.filter (fun j : Fin (Specht.nOf μ) =>
        j.val < s.val ∧ Equiv.swap j s ∈ Specht.colStab (colSuperstandard μ))).card
      = (colSuperstandard μ s : ℕ × ℕ).1 := by
  classical
  rw [sameColumn_filter_eq]
  refine Eq.trans ?_ (Finset.card_range ((colSuperstandard μ s : ℕ × ℕ).1))
  refine Finset.card_bij (fun j _ => (colSuperstandard μ j : ℕ × ℕ).1) ?_ ?_ ?_
  · intro j hj
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hj
    exact Finset.mem_range.mpr hj.2
  · intro a ha b hb hab
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at ha hb
    exact (colSuperstandard μ).injective
      (Subtype.ext (Prod.ext hab (ha.1.trans hb.1.symm)))
  · intro r hr
    rw [Finset.mem_range] at hr
    have hs : ((colSuperstandard μ s : ℕ × ℕ)) ∈ μ := (colSuperstandard μ s).2
    have hmem : ((r, (colSuperstandard μ s : ℕ × ℕ).2) : ℕ × ℕ) ∈ μ.cells :=
      μ.up_left_mem (le_of_lt hr) (le_refl _) hs
    refine ⟨(colSuperstandard μ).symm ⟨_, hmem⟩, ?_, ?_⟩
    · simp only [Finset.mem_filter, Finset.mem_univ, true_and, Equiv.apply_symm_apply]
      exact hr
    · simp [Equiv.apply_symm_apply]

end QOU.BraidKnot.ColSuperstandardTableau
