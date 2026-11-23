import QOU.BraidKnot.Specht
import QOU.BraidKnot.SpechtStandardBasisCore

/-!
# QOU.BraidKnot.RowStandardTableau — the index set Murphy's straightening runs over

Mathas' Lemma 3.14, the one remaining input to the Murphy basis
(`HeckeMurphyYoung.basisOfSpanning`), is a statement about **row-standard** tableaux: for `s, t`
row-standard of shape `λ`, `m_{st}` is a combination of `m_{uv}` with `u, v` **standard** of
shape `ν`, where either `ν ⊳ λ`, or `ν = λ` and `u ⊵ s`, `v ⊵ t`.

The corpus had no row-standard notion, and that absence is what blocks the spanning leg rather
than any difficulty in the argument. The gap is quantitative and it is large:

| shape | row-standard `μ`-tableaux | standard `μ`-tableaux |
|---|---|---|
| general `μ ⊢ n` | `n! / ∏ᵢ μᵢ!` | `f^μ` |
| one column `(1ⁿ)` | **`n!`** | **`1`** |

`HeckeMurphyYoung.span_murphySum_one_conjugates_eq_top` (step 2 of spanning) is exactly the
one-column row: every `T_w` is a Murphy element there, because `x_{(1ⁿ)} = 1` and every filling
of a single column is row-standard. Against the *standard* family that shape contributes a
single element, so the statement cannot be made there at all — hence this file.

## Why a predicate and not a new structure

`Specht.Tableau μ = Fin (nOf μ) ≃ μ.cells` is already the *arbitrary* bijective filling, and it
is what `HeckeMurphyYoung.dOf`, `dAt` and `murphyM` consume. Row-standardness is a condition on
such a filling — labels increase along each row — so it is a predicate, and a row-standard
tableau is a subtype. Nothing downstream has to be re-plumbed. (`BraidKnot.StandardYoungTableau`
is a different, `entry`-based structure carrying both `row_strict` and `col_strict`; the
row-standard condition is that structure minus the column half, but expressed on the filling
type the Hecke side already speaks.)

## References
- [mathas1999] Mathas, *Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group*,
  §3 (the Murphy basis; Lemmas 3.9, 3.12, 3.13, 3.14).
- [sagan2001] Sagan, *The Symmetric Group*, §2.6 (Garnir relations, the `q = 1` template).
-/

namespace QOU.BraidKnot.RowStandardTableau

open QOU.BraidKnot.Specht

variable {μ : YoungDiagram}

/-- **Row-standard**: within any one row, label order agrees with column order.

Stated as the single implication `same row → earlier column → smaller label`. The converse
follows from it (both patterns are determined by the filling, which is a bijection), so this is
the convenient form to *use*: a hypothesis about columns discharges a goal about labels. -/
def IsRowStandard (t : Tableau μ) : Prop :=
  ∀ l l' : Fin (nOf μ), rowPattern t l = rowPattern t l' →
    colPattern t l < colPattern t l' → l < l'

/-- A **row-standard tableau** of shape `μ`. -/
def _root_.QOU.BraidKnot.RowStandardTab (μ : YoungDiagram) : Type :=
  {t : Tableau μ // IsRowStandard t}

instance : CoeOut (QOU.BraidKnot.RowStandardTab μ) (Tableau μ) := ⟨Subtype.val⟩

instance instDecidableIsRowStandard (t : Tableau μ) : Decidable (IsRowStandard t) := by
  unfold IsRowStandard; infer_instance

instance : Fintype (QOU.BraidKnot.RowStandardTab μ) := by
  unfold QOU.BraidKnot.RowStandardTab; infer_instance

/-! ## The one-column shape

A shape with no cell in column `1` has every row of length at most one, so no two distinct
labels share a row and the row-standard condition is **vacuous**: every filling qualifies.
`YoungDiagram` is closed under moving up and left, so `(0,1) ∉ μ` is the whole hypothesis. -/

/-- **Every filling of a one-column shape is row-standard.** -/
theorem isRowStandard_of_no_second_column (hμ : ((0 : ℕ), (1 : ℕ)) ∉ μ) (t : Tableau μ) :
    IsRowStandard t := by
  intro l l' _hrow hcol
  exfalso
  -- put the cell in explicit `(i, j)` form so `up_left_mem` can unify its indices
  have hmem : (((t l' : ℕ × ℕ).1), ((t l' : ℕ × ℕ).2)) ∈ μ := by
    simp
  have hj : 1 ≤ (t l' : ℕ × ℕ).2 := by
    simp only [colPattern] at hcol; omega
  exact hμ (μ.up_left_mem (Nat.zero_le _) hj hmem)

/-- On a one-column shape the row-standard tableaux are **all** the fillings. -/
noncomputable def equivTableauOfNoSecondColumn (hμ : ((0 : ℕ), (1 : ℕ)) ∉ μ) :
    QOU.BraidKnot.RowStandardTab μ ≃ Tableau μ where
  toFun := Subtype.val
  invFun t := ⟨t, isRowStandard_of_no_second_column hμ t⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- **`n!` row-standard tableaux on a one-column shape** — against exactly one standard tableau.

This is the quantitative form of the gap the module docstring names: it is why Mathas' Lemma
3.14 cannot be stated against the standard-pair index set `HeckeMurphyYoung.MurphyIndex`, and
why `span_murphySum_one_conjugates_eq_top` had to be phrased over conjugating permutations
instead of over tableaux. -/
theorem card_eq_factorial_of_no_second_column (hμ : ((0 : ℕ), (1 : ℕ)) ∉ μ) :
    Fintype.card (QOU.BraidKnot.RowStandardTab μ) = (nOf μ).factorial := by
  classical
  have hc : Fintype.card μ.cells = nOf μ := by
    simp [nOf, YoungDiagram.card]
  have e : Fin (nOf μ) ≃ μ.cells := (Fintype.equivFinOfCardEq hc).symm
  rw [Fintype.card_congr (equivTableauOfNoSecondColumn hμ)]
  show Fintype.card (Fin (nOf μ) ≃ μ.cells) = _
  rw [Fintype.card_equiv e, Fintype.card_fin]

/-! ## Standard ⟹ row-standard

Mathas' Lemma 3.14 rewrites a row-standard pair as a combination of **standard** pairs, so the
two index sets have to be related in the obvious direction: a standard tableau, read as a
filling, is row-standard. That is the forgetful map `Std(μ) → RowStd(μ)`.

It is not quite immediate. `StandardYoungTableau.row_strict` compares only **adjacent** cells
(`entry i j < entry i (j+1)`), while row-standardness compares arbitrary pairs in a row, so the
transitive form has to be proved first. `entry_lt_entry_of_lt` below does that by induction on
the right-hand column, using the diagram's up-left closure to know the intermediate cells are
present.

`entry_lt_entry_of_lt` is a statement about `StandardYoungTableau` alone and **belongs upstream**
in `QOU.BraidKnot.StandardYoungTableau`; it is here to keep this change to a single file, the
same call as the `Tw_mul_σ_*` lemmas in `HeckeMurphyYoung`. -/

open QOU.BraidKnot.SpechtStandardBasis in
/-- **Row entries increase across a whole row, not just between neighbours.**

The transitive closure of `row_strict`, by induction on the right-hand column. The up-left
closure of a `YoungDiagram` supplies the intermediate cells: if `(i, j')` is in the diagram then
so is every `(i, k)` with `k ≤ j'`. -/
theorem entry_lt_entry_of_lt (T : QOU.BraidKnot.StandardYoungTableau μ) {i : ℕ} :
    ∀ {j j' : ℕ}, j < j' → (i, j') ∈ μ → T.entry i j < T.entry i j' := by
  intro j j'
  induction j' with
  | zero => intro h _; omega
  | succ k ih =>
    intro hlt hmem
    rcases Nat.lt_succ_iff_lt_or_eq.mp hlt with h | h
    · exact lt_trans (ih h (μ.up_left_mem (le_refl i) (Nat.le_succ k) hmem))
        (T.row_strict i k hmem)
    · subst h; exact T.row_strict i j hmem

open QOU.BraidKnot.SpechtStandardBasis in
/-- **A standard tableau, read as a filling, is row-standard** — the forgetful map
`Std(μ) → RowStd(μ)` that Lemma 3.14's target side needs.

`sytToTableau T` is the inverse of `cellLabel T`, so a label `l` sits at the cell `c` with
`cellLabel T c = l`, and `cellLabel` is literally `T.entry` on that cell. Two labels in the same
row with the earlier column therefore compare exactly as their entries do, which is
`entry_lt_entry_of_lt`. -/
theorem isRowStandard_sytToTableau (T : QOU.BraidKnot.StandardYoungTableau μ) :
    IsRowStandard (sytToTableau T) := by
  intro l l' hrow hcol
  -- `sytToTableau` is the inverse of `cellLabel`, so a label is its own cell's entry
  have hl : cellLabel T (sytToTableau T l) = l :=
    (Equiv.ofBijective (cellLabel T) (cellLabel_bijective T)).apply_symm_apply l
  have hl' : cellLabel T (sytToTableau T l') = l' :=
    (Equiv.ofBijective (cellLabel T) (cellLabel_bijective T)).apply_symm_apply l'
  simp only [rowPattern, colPattern] at hrow hcol
  -- the right-hand cell, in explicit `(i, j)` form
  have hmem : ((((sytToTableau T) l' : μ.cells) : ℕ × ℕ).1,
      (((sytToTableau T) l' : μ.cells) : ℕ × ℕ).2) ∈ μ := by simp
  have key : T.entry ((((sytToTableau T) l : μ.cells) : ℕ × ℕ)).1
        ((((sytToTableau T) l : μ.cells) : ℕ × ℕ)).2
      < T.entry ((((sytToTableau T) l' : μ.cells) : ℕ × ℕ)).1
        ((((sytToTableau T) l' : μ.cells) : ℕ × ℕ)).2 := by
    rw [hrow]
    exact entry_lt_entry_of_lt T hcol hmem
  rw [← hl, ← hl']
  exact Fin.lt_def.mpr key


/-! ## Column-standard, and standard, on the same filling type

Lemma 3.14's **target** side is a standard pair, so "standard" is needed as a predicate on
`Specht.Tableau μ` too — the same type the row-standard predicate and the whole `q = 1` Garnir
apparatus (`colWordNum`, `garnirA`/`garnirB`/`garnirG`) already live on. With `IsStandard` here,
all three index sets of Mathas' Lemma 3.14 — row-standard source, standard target, and the map
between them — are expressed on one type, and the statement of 3.14 no longer has anything
missing.

Everything below mirrors the row case exactly, `col_strict` for `row_strict` throughout. -/

/-- **Column-standard**: within any one column, label order agrees with row order. -/
def IsColStandard (t : Tableau μ) : Prop :=
  ∀ l l' : Fin (nOf μ), colPattern t l = colPattern t l' →
    rowPattern t l < rowPattern t l' → l < l'

/-- **Standard**: row-standard and column-standard. -/
def IsStandard (t : Tableau μ) : Prop := IsRowStandard t ∧ IsColStandard t

instance instDecidableIsColStandard (t : Tableau μ) : Decidable (IsColStandard t) := by
  unfold IsColStandard; infer_instance

instance instDecidableIsStandard (t : Tableau μ) : Decidable (IsStandard t) := by
  unfold IsStandard; infer_instance

open QOU.BraidKnot.SpechtStandardBasis in
/-- **Column entries increase down a whole column, not just between neighbours** — the column
twin of `entry_lt_entry_of_lt`, and, like it, belonging upstream in
`QOU.BraidKnot.StandardYoungTableau`. -/
theorem entry_lt_entry_of_lt_row (T : QOU.BraidKnot.StandardYoungTableau μ) {j : ℕ} :
    ∀ {i i' : ℕ}, i < i' → (i', j) ∈ μ → T.entry i j < T.entry i' j := by
  intro i i'
  induction i' with
  | zero => intro h _; omega
  | succ k ih =>
    intro hlt hmem
    rcases Nat.lt_succ_iff_lt_or_eq.mp hlt with h | h
    · exact lt_trans (ih h (μ.up_left_mem (Nat.le_succ k) (le_refl j) hmem))
        (T.col_strict k j hmem)
    · subst h; exact T.col_strict i j hmem

open QOU.BraidKnot.SpechtStandardBasis in
/-- A standard tableau, read as a filling, is column-standard. -/
theorem isColStandard_sytToTableau (T : QOU.BraidKnot.StandardYoungTableau μ) :
    IsColStandard (sytToTableau T) := by
  intro l l' hcol hrow
  have hl : cellLabel T (sytToTableau T l) = l :=
    (Equiv.ofBijective (cellLabel T) (cellLabel_bijective T)).apply_symm_apply l
  have hl' : cellLabel T (sytToTableau T l') = l' :=
    (Equiv.ofBijective (cellLabel T) (cellLabel_bijective T)).apply_symm_apply l'
  simp only [rowPattern, colPattern] at hcol hrow
  have hmem : ((((sytToTableau T) l' : μ.cells) : ℕ × ℕ).1,
      (((sytToTableau T) l' : μ.cells) : ℕ × ℕ).2) ∈ μ := by simp
  have key : T.entry ((((sytToTableau T) l : μ.cells) : ℕ × ℕ)).1
        ((((sytToTableau T) l : μ.cells) : ℕ × ℕ)).2
      < T.entry ((((sytToTableau T) l' : μ.cells) : ℕ × ℕ)).1
        ((((sytToTableau T) l' : μ.cells) : ℕ × ℕ)).2 := by
    rw [hcol]
    exact entry_lt_entry_of_lt_row T hrow hmem
  rw [← hl, ← hl']
  exact Fin.lt_def.mpr key

open QOU.BraidKnot.SpechtStandardBasis in
/-- **A standard tableau, read as a filling, is standard** — both halves together. This is the
map `Std(μ) → {t : Tableau μ // IsStandard t}` that Lemma 3.14's target side quantifies over. -/
theorem isStandard_sytToTableau (T : QOU.BraidKnot.StandardYoungTableau μ) :
    IsStandard (sytToTableau T) :=
  ⟨isRowStandard_sytToTableau T, isColStandard_sytToTableau T⟩

/-- Standard implies row-standard — the inclusion of index sets Lemma 3.14 moves along. -/
theorem IsStandard.isRowStandard {t : Tableau μ} (h : IsStandard t) : IsRowStandard t := h.1

/-- Zero-subtracted upper-minus-lower column entry vanishes for strictly increasing rows in `μ`. -/
theorem entry_sub_entry_eq_zero_of_lt_row (T : QOU.BraidKnot.StandardYoungTableau μ) {i i' j : ℕ}
    (hlt : i < i') (hmem : (i', j) ∈ μ) :
    T.entry i j - T.entry i' j = 0 :=
  Nat.sub_eq_zero_of_le (Nat.le_of_lt (entry_lt_entry_of_lt_row T hlt hmem))

end QOU.BraidKnot.RowStandardTableau
