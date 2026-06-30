import QOU.BraidKnot.SpechtColInv
import QOU.BraidKnot.SpechtGarnirGeom
import QOU.BraidKnot.SpechtGarnirSyt
import QOU.BraidKnot.SpechtGarnirCard
import QOU.BraidKnot.SpechtGarnirMeasure
import QOU.BraidKnot.SpechtGarnirColInvStep
import QOU.BraidKnot.SpechtGarnirStep
import QOU.BraidKnot.SpechtSpanningCore

/-!
# QOU.BraidKnot.SpechtGarnirClose — closing the Specht straightening core

This module assembles the already-proven straightening pieces into a **sorry-free**
proof of the brick-4 spanning core
`SpechtSpanningCore.polytabloid_garnir_core` (reproved here as
`polytabloid_garnir_core'`, with `wt := SpechtGarnirMeasure.garnirWt`).

The assembly is:

1. **`colMono_bridge`** — the two column-monotonicity predicates
   (`SpechtColInv.ColMono`, the *label-order ⟹ row-order* form, and
   `SpechtGarnirGeom.ColMono`, the *row-order ⟹ label-order* form) are equivalent.
   Within a fixed column the (label ↔ row) map is a bijection on a finite total
   order, so monotone one way ⟺ monotone the other way. The proof is by
   trichotomy, using `cell_inj` (equal row + column ⟹ equal label).

2. **`colInv_ne_zero_adjacent`** — adjacency lemma A: a nonzero column-inversion
   count produces an *adjacent-row* same-column inversion. Proved by contraposition
   of a "no adjacent inversion ⟹ column monotone" helper
   (`colMono_of_no_adjacent`), itself proved by strong induction on the row gap,
   producing intermediate-row labels by column down-closure
   (`intermediate_label`).

3. **`not_rowMono_adjacent`** — adjacency lemma B: in a column-monotone tableau
   that is not row-monotone, there is an *adjacent-column* row-violation. Proved by
   the row analogue of the same machinery (`rowMono_of_no_adjacent_col`,
   `intermediate_label_row`).

4. **`polytabloid_garnir_core'`** — the final theorem: case-split on
   `colInv t = 0`. If zero, `t` is column-monotone; non-standard ⟹ not row-monotone
   (else `mono_eq_syt`), so lemma B + `polytabloid_garnir_step` + `garnir_card_gt`
   + `garnir_rowBound`. If nonzero, lemma A + `polytabloid_colInv_step`.

All sorry-free; assembles only the proved pieces listed above.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.6 (the straightening algorithm).
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtGarnirClose

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtStandardBasis

variable {μ : YoungDiagram}

/-! ## 0. Intermediate-row / intermediate-column labels (column / row down-closure) -/

/-- **Intermediate-row label.** If a label `y` sits in column `col` at row `R₂`,
then for every row `i ≤ R₂` there is a label `x` in the same column `col` at row
`i`. (The cell `(i, col)` lies in `μ` by down-closure from `(R₂, col)`.) -/
theorem intermediate_label {t : Tableau μ} {y : Fin (nOf μ)} {col i : ℕ}
    (hcol : colPattern t y = col) (hle : i ≤ rowPattern t y) :
    ∃ x : Fin (nOf μ), colPattern t x = col ∧ rowPattern t x = i := by
  -- The cell of `y` lies in `μ`.
  have hymem : ((t y : ℕ × ℕ).1, (t y : ℕ × ℕ).2) ∈ μ := (t y).2
  -- Rewrite that cell as `(rowPattern t y, col)`.
  have hcell : ((t y : ℕ × ℕ).1, (t y : ℕ × ℕ).2) = (rowPattern t y, col) := by
    simp only [rowPattern, colPattern] at hcol ⊢
    rw [← hcol]
  rw [hcell] at hymem
  -- Down-closure: `(i, col) ∈ μ`.
  have hmem : (i, col) ∈ μ := μ.up_left_mem hle (le_refl col) hymem
  refine ⟨t.symm ⟨(i, col), by rw [YoungDiagram.mem_cells]; exact hmem⟩, ?_, ?_⟩
  · show colPattern t (t.symm _) = col
    simp [colPattern, Equiv.apply_symm_apply]
  · show rowPattern t (t.symm _) = i
    simp [rowPattern, Equiv.apply_symm_apply]

/-- **Intermediate-column label.** If a label `y` sits in row `row` at column `C₂`,
then for every column `j ≤ C₂` there is a label `x` in the same row `row` at
column `j`. (The cell `(row, j)` lies in `μ` by down-closure from `(row, C₂)`.) -/
theorem intermediate_label_row {t : Tableau μ} {y : Fin (nOf μ)} {row j : ℕ}
    (hrow : rowPattern t y = row) (hle : j ≤ colPattern t y) :
    ∃ x : Fin (nOf μ), rowPattern t x = row ∧ colPattern t x = j := by
  have hymem : ((t y : ℕ × ℕ).1, (t y : ℕ × ℕ).2) ∈ μ := (t y).2
  have hcell : ((t y : ℕ × ℕ).1, (t y : ℕ × ℕ).2) = (row, colPattern t y) := by
    simp only [rowPattern, colPattern] at hrow ⊢
    rw [← hrow]
  rw [hcell] at hymem
  have hmem : (row, j) ∈ μ := μ.up_left_mem (le_refl row) hle hymem
  refine ⟨t.symm ⟨(row, j), by rw [YoungDiagram.mem_cells]; exact hmem⟩, ?_, ?_⟩
  · show rowPattern t (t.symm _) = row
    simp [rowPattern, Equiv.apply_symm_apply]
  · show colPattern t (t.symm _) = j
    simp [colPattern, Equiv.apply_symm_apply]

/-! ## 1. The ColMono bridge -/

/-- **The two `ColMono` predicates agree.** `SpechtColInv.ColMono` (label-order ⟹
row-order) and `SpechtGarnirGeom.ColMono` (row-order ⟹ label-order) are equivalent:
within a column the label and row are in bijection on a finite total order. -/
theorem colMono_bridge (t : Tableau μ) :
    SpechtColInv.ColMono t ↔ SpechtGarnirGeom.ColMono t := by
  constructor
  · -- label-order ⟹ row-order  gives  row-order ⟹ label-order
    intro h l l' hcol hrow
    -- want (l:ℕ) < (l':ℕ); trichotomy on (l:ℕ) vs (l':ℕ)
    rcases lt_trichotomy (l : ℕ) (l' : ℕ) with hlt | heq | hgt
    · exact hlt
    · -- (l:ℕ) = (l':ℕ) ⟹ l = l' ⟹ rows equal, contradicting hrow
      have : l = l' := Fin.ext heq
      rw [this] at hrow; exact absurd hrow (lt_irrefl _)
    · -- (l':ℕ) < (l:ℕ): apply h to (l', l) to get rowPattern t l' < rowPattern t l
      have := h l' l hcol.symm hgt
      omega
  · -- row-order ⟹ label-order  gives  label-order ⟹ row-order
    intro h l l' hcol hlt
    rcases lt_trichotomy (rowPattern t l) (rowPattern t l') with hr | heq | hr
    · exact hr
    · -- rows equal ⟹ same cell ⟹ same label, contradicting (l:ℕ) < (l':ℕ)
      have : l = l' := SpechtGarnirGeom.cell_inj hcol heq
      rw [this] at hlt; exact absurd hlt (lt_irrefl _)
    · -- rowPattern t l' < rowPattern t l: apply h to (l', l) to get (l':ℕ) < (l:ℕ)
      have := h l' l hcol.symm hr
      omega

/-! ## 2. Adjacency lemma A — column inversion ⟹ adjacent column inversion -/

/-- **No adjacent inversion ⟹ column monotone.** If for every adjacent-row
same-column pair the lower-row label is the larger
(`rowPattern t a = rowPattern t b + 1 ⟹ (b:ℕ) < (a:ℕ)`), then `t` is
`SpechtGarnirGeom.ColMono`. Proved by strong induction on the row gap, producing
the intermediate-row cell at each step via `intermediate_label`. -/
theorem colMono_of_no_adjacent {t : Tableau μ}
    (hadj : ∀ a b : Fin (nOf μ), colPattern t a = colPattern t b →
      rowPattern t a = rowPattern t b + 1 → (b : ℕ) < (a : ℕ)) :
    SpechtGarnirGeom.ColMono t := by
  -- It suffices to prove: for every gap `d`, and labels `l, l'` in the same column
  -- with `rowPattern t l' = rowPattern t l + d` and `0 < d`, we have `(l:ℕ)<(l':ℕ)`.
  have key : ∀ d : ℕ, ∀ l l' : Fin (nOf μ), colPattern t l = colPattern t l' →
      rowPattern t l' = rowPattern t l + d → 0 < d → (l : ℕ) < (l' : ℕ) := by
    intro d
    induction d using Nat.strong_induction_on with
    | _ d IH =>
      intro l l' hcol hgap hd
      rcases Nat.lt_or_ge d 2 with hlt2 | hge2
      · -- d = 1 (since 0 < d < 2): adjacent, use hadj
        have hd1 : d = 1 := by omega
        rw [hd1] at hgap
        -- hgap : rowPattern t l' = rowPattern t l + 1, so l' is one row below l.
        exact hadj l' l hcol.symm hgap
      · -- d ≥ 2: find an intermediate label at row `rowPattern t l + 1`.
        -- `i := rowPattern t l + 1 ≤ rowPattern t l'` since gap ≥ 2.
        have hi_le : rowPattern t l + 1 ≤ rowPattern t l' := by omega
        obtain ⟨x, hxcol, hxrow⟩ :=
          intermediate_label (t := t) (y := l') (col := colPattern t l')
            (i := rowPattern t l + 1) rfl hi_le
        -- l → x is gap 1; x → l' is gap d-1; both same column as l.
        have hcol_lx : colPattern t l = colPattern t x := by rw [hxcol, hcol]
        have hcol_xl' : colPattern t x = colPattern t l' := hxcol
        -- step 1: (l:ℕ) < (x:ℕ) via hadj
        have hlx : (l : ℕ) < (x : ℕ) := by
          apply hadj x l hcol_lx.symm
          rw [hxrow]
        -- step 2: (x:ℕ) < (l':ℕ) via IH at gap d-1
        have hxgap : rowPattern t l' = rowPattern t x + (d - 1) := by
          rw [hxrow]; omega
        have hxl' : (x : ℕ) < (l' : ℕ) :=
          IH (d - 1) (by omega) x l' hcol_xl' hxgap (by omega)
        omega
  -- Now derive ColMono from `key`.
  intro l l' hcol hrow
  -- rowPattern t l < rowPattern t l', set d := rowPattern t l' - rowPattern t l > 0
  apply key (rowPattern t l' - rowPattern t l) l l' hcol
  · omega
  · omega

/-- **Adjacency lemma A.** A nonzero column-inversion count produces an
*adjacent-row* same-column inversion. -/
theorem colInv_ne_zero_adjacent {t : Tableau μ} (h : SpechtColInv.colInv t ≠ 0) :
    ∃ a b : Fin (nOf μ), colPattern t a = colPattern t b ∧ (a : ℕ) < (b : ℕ) ∧
      rowPattern t b < rowPattern t a ∧ rowPattern t a = rowPattern t b + 1 := by
  by_contra hcon
  push_neg at hcon
  -- hcon : ∀ a b, colPattern t a = colPattern t b → (a:ℕ)<(b:ℕ) →
  --        rowPattern t b < rowPattern t a → rowPattern t a ≠ rowPattern t b + 1
  -- Show: no adjacent inversion, hence ColMono, hence colInv = 0, contradiction.
  have hnoadj : ∀ a b : Fin (nOf μ), colPattern t a = colPattern t b →
      rowPattern t a = rowPattern t b + 1 → (b : ℕ) < (a : ℕ) := by
    intro a b hcol hadjeq
    -- a is one row below b; want (b:ℕ) < (a:ℕ).  Trichotomy on (b:ℕ) vs (a:ℕ).
    rcases lt_trichotomy (b : ℕ) (a : ℕ) with hlt | heq | hgt
    · exact hlt
    · -- equal labels ⟹ same cell, but rows differ (hadjeq), contradiction
      have : a = b := Fin.ext heq.symm
      rw [this] at hadjeq; omega
    · -- (a:ℕ) < (b:ℕ): then (a, b) is an inversion (a smaller label, lower row),
      -- adjacent — contradicts hcon applied to (a, b).
      have hrowlt : rowPattern t b < rowPattern t a := by omega
      have := hcon a b hcol hgt hrowlt
      -- this : rowPattern t a ≠ rowPattern t b + 1, but hadjeq says equal
      exact absurd hadjeq this
  have hmono : SpechtGarnirGeom.ColMono t := colMono_of_no_adjacent hnoadj
  have hmono' : SpechtColInv.ColMono t := (colMono_bridge t).mpr hmono
  have : SpechtColInv.colInv t = 0 := (SpechtColInv.colInv_eq_zero_iff_colMono t).mpr hmono'
  exact h this

/-! ## 3. Adjacency lemma B — row violation ⟹ adjacent-column row violation -/

/-- **No adjacent-column row violation ⟹ row monotone.** If every adjacent-column
same-row pair is in label-order, then `t` is `SpechtGarnirSyt.RowMono`. Row analogue
of `colMono_of_no_adjacent`, via `intermediate_label_row`. -/
theorem rowMono_of_no_adjacent_col {t : Tableau μ}
    (hadj : ∀ a b : Fin (nOf μ), rowPattern t a = rowPattern t b →
      colPattern t a = colPattern t b + 1 → (b : ℕ) < (a : ℕ)) :
    SpechtGarnirSyt.RowMono t := by
  have key : ∀ d : ℕ, ∀ l l' : Fin (nOf μ), rowPattern t l = rowPattern t l' →
      colPattern t l' = colPattern t l + d → 0 < d → (l : ℕ) < (l' : ℕ) := by
    intro d
    induction d using Nat.strong_induction_on with
    | _ d IH =>
      intro l l' hrow hgap hd
      rcases Nat.lt_or_ge d 2 with hlt2 | hge2
      · have hd1 : d = 1 := by omega
        rw [hd1] at hgap
        exact hadj l' l hrow.symm hgap
      · have hi_le : colPattern t l + 1 ≤ colPattern t l' := by omega
        obtain ⟨x, hxrow, hxcol⟩ :=
          intermediate_label_row (t := t) (y := l') (row := rowPattern t l')
            (j := colPattern t l + 1) rfl hi_le
        have hrow_lx : rowPattern t l = rowPattern t x := by rw [hxrow, hrow]
        have hrow_xl' : rowPattern t x = rowPattern t l' := hxrow
        have hlx : (l : ℕ) < (x : ℕ) := by
          apply hadj x l hrow_lx.symm
          rw [hxcol]
        have hxgap : colPattern t l' = colPattern t x + (d - 1) := by
          rw [hxcol]; omega
        have hxl' : (x : ℕ) < (l' : ℕ) :=
          IH (d - 1) (by omega) x l' hrow_xl' hxgap (by omega)
        omega
  intro l l' hrow hcol
  apply key (colPattern t l' - colPattern t l) l l' hrow
  · omega
  · omega

/-- **Adjacency lemma B.** In a column-monotone tableau that is *not* row-monotone,
there is an *adjacent-column* row-violation: column-`j` label `ar` and column-`(j+1)`
label `br` in the *same* row `r`, with `(br:ℕ) < (ar:ℕ)`, and `r` within both
columns. -/
theorem not_rowMono_adjacent {t : Tableau μ} (hnr : ¬ SpechtGarnirSyt.RowMono t) :
    ∃ (j r : ℕ) (ar br : Fin (nOf μ)),
      colPattern t ar = j ∧ rowPattern t ar = r ∧
      colPattern t br = j + 1 ∧ rowPattern t br = r ∧
      (br : ℕ) < (ar : ℕ) ∧ r < μ.colLen j ∧ r < μ.colLen (j + 1) := by
  -- Contrapose `rowMono_of_no_adjacent_col`: there is an adjacent-column violation.
  -- First, get the negation of the "no adjacent" hypothesis.
  have hexists : ∃ a b : Fin (nOf μ), rowPattern t a = rowPattern t b ∧
      colPattern t a = colPattern t b + 1 ∧ ¬ ((b : ℕ) < (a : ℕ)) := by
    by_contra hc
    push_neg at hc
    -- hc : ∀ a b, rowPattern t a = rowPattern t b → colPattern t a = colPattern t b + 1
    --      → (b:ℕ) < (a:ℕ)
    exact hnr (rowMono_of_no_adjacent_col hc)
  obtain ⟨a, b, hrow, hcoladj, hnlt⟩ := hexists
  -- Here `a` is the column-`(j+1)` label (its column = b's + 1), `b` is column-`j`.
  -- The violation: `a` (right column) has the *smaller* label.  We need a≠b.
  have hab_ne : a ≠ b := by
    intro h; rw [h] at hcoladj; omega
  -- (a:ℕ) ≠ (b:ℕ)
  have hval_ne : (a : ℕ) ≠ (b : ℕ) := fun h => hab_ne (Fin.ext h)
  -- ¬(b < a) and a ≠ b ⟹ a < b  (right-column label `a` is the smaller)
  have hba : (a : ℕ) < (b : ℕ) := by omega
  -- Set j := colPattern t b, r := rowPattern t a (= rowPattern t b).
  -- ar := b (column j, label larger), br := a (column j+1, label smaller).
  -- Check: colPattern ar = j ✓ ; colPattern br = j+1 = colPattern a ✓.
  refine ⟨colPattern t b, rowPattern t b, b, a, rfl, rfl, ?_, ?_, ?_, ?_, ?_⟩
  · -- colPattern t a = colPattern t b + 1
    exact hcoladj
  · -- rowPattern t a = rowPattern t b
    exact hrow
  · -- (a:ℕ) < (b:ℕ)  — wait: target is (br:ℕ) < (ar:ℕ) = (a:ℕ) < (b:ℕ)
    exact hba
  · -- rowPattern t b < μ.colLen (colPattern t b): cell of b in column j at its row
    have := SpechtGarnirGeom.rowPattern_lt_colLen t b
    -- this : rowPattern t b < μ.colLen (colPattern t b)
    exact this
  · -- rowPattern t b < μ.colLen (colPattern t b + 1):
    -- a is in column (colPattern t b + 1) at row rowPattern t a = rowPattern t b.
    have ha := SpechtGarnirGeom.rowPattern_lt_colLen t a
    -- ha : rowPattern t a < μ.colLen (colPattern t a)
    rw [hcoladj] at ha
    -- ha : rowPattern t a < μ.colLen (colPattern t b + 1)
    rw [hrow] at ha
    -- ha : rowPattern t b < μ.colLen (colPattern t b + 1)
    exact ha

/-! ## 4. The final theorem -/

variable {k : Type} [Field k] [CharZero k]

/-- **The Specht straightening core — sorry-free.** Verbatim restatement of
`SpechtSpanningCore.polytabloid_garnir_core` (the brick-4 spanning stub), with the
explicit measure `wt := SpechtGarnirMeasure.garnirWt`: for every *non-standard*
tableau `t`, the polytabloid `e_t` is a `k`-combination of polytabloids of strictly
smaller `garnirWt`.

Both straightening legs are assembled: the **column-sort** leg
(`polytabloid_colInv_step`, when `colInv t ≠ 0`) and the **Garnir** leg
(`polytabloid_garnir_step`, when `colInv t = 0` and `t` is non-standard hence not
row-monotone). -/
theorem polytabloid_garnir_core' :
    ∃ wt : Specht.Tableau μ → ℕ,
      ∀ t : Specht.Tableau μ,
        (∀ T : StandardYoungTableau μ, sytToTableau T ≠ t) →
        Specht.polytabloid (k := k) t ∈
          Submodule.span k
            {x | ∃ t', wt t' < wt t ∧ x = Specht.polytabloid (k := k) t'} := by
  refine ⟨SpechtGarnirMeasure.garnirWt, fun t hns => ?_⟩
  by_cases hci : SpechtColInv.colInv t = 0
  · -- Column-monotone branch: t is column-monotone but non-standard ⟹ not row-monotone.
    have hmono' : SpechtColInv.ColMono t :=
      (SpechtColInv.colInv_eq_zero_iff_colMono t).mp hci
    have hmono : SpechtGarnirGeom.ColMono t := (colMono_bridge t).mp hmono'
    -- not row-monotone (else mono_eq_syt yields a standard tableau equal to t)
    have hnr : ¬ SpechtGarnirSyt.RowMono t := by
      intro hrow
      obtain ⟨T, hT⟩ := SpechtGarnirSyt.mono_eq_syt hmono hrow
      exact hns T hT
    obtain ⟨j, r, ar, br, har, harr, hbr, hbrr, hviol, hrj, hrj1⟩ :=
      not_rowMono_adjacent hnr
    -- Apply the Garnir straightening step with m := μ.colLen j.
    have hstep :
        Specht.polytabloid (k := k) t ∈ Submodule.span k
          {x | ∃ s : Tableau μ, SpechtGarnirWt.colWt s < SpechtGarnirWt.colWt t ∧
            x = Specht.polytabloid (k := k) s} :=
      SpechtGarnirStep.polytabloid_garnir_step (k := k) hmono har harr hbr hbrr hviol
        (m := μ.colLen j)
        (SpechtGarnirCard.garnir_card_gt hrj hrj1)
        (fun π l hl => SpechtGarnirGeom.garnir_rowBound t j r π hl)
    -- Widen the span: colWt-smaller ⟹ garnirWt-smaller.
    refine Submodule.span_mono ?_ hstep
    rintro x ⟨s, hs, rfl⟩
    exact ⟨s, SpechtGarnirMeasure.garnirWt_lt_of_colWt_lt hs, rfl⟩
  · -- Column-inversion branch: an adjacent column inversion exists.
    obtain ⟨a, b, hcol, hab, hrow, hadj⟩ := colInv_ne_zero_adjacent hci
    exact SpechtGarnirColInvStep.polytabloid_colInv_step (k := k) hcol hab hrow hadj

end QOU.BraidKnot.SpechtGarnirClose
