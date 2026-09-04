import QOU.BraidKnot.GarnirTableau
import QOU.BraidKnot.RowStandardTableau
import QOU.BraidKnot.GarnirDescentAdditive

/-!
# A non-standard row-standard tableau has a descent node

This is the second half of Mathas' Lemma 3.13, and the last piece of it.
`QOU.BraidKnot.GarnirDescentAdditive` proves that length is additive **at** any
descent node; 3.13 also asserts that a row-standard non-standard tableau **has**
one.  That is what is proved here.

## The statement

  `exists_descentNode_of_not_standard :`
  `  IsRowStandard t → ¬ IsStandard t → ∃ i j, IsDescentNode t i j`

Together with `invSet_garnirPerm_subset_of_descent` this closes the length half
of 3.13: for a row-standard non-standard `t` there *is* a Garnir tableau `g` and
a `w` with `t = w • g` and `ℓ(d(t)) = ℓ(d(g)) + ℓ(w)`.

## The argument

Contrapositive.  A descent node is a failure of column-strictness between
*adjacent* rows, while `IsColStandard` quantifies over *arbitrary* row pairs, so
the two are not immediately interchangeable: the content is that having no
adjacent failure forces the whole column to increase.  `lt_of_noDescent` is that
induction, mirroring `entry_lt_entry_of_lt_row` (which proves the same shape for
a `StandardYoungTableau`, where column-strictness is part of the structure
rather than a hypothesis).

Strictness at the induction step needs one extra step beyond "not a descent":
`¬ IsDescentNode` gives only `≤`, and the labels are distinct because `t` is a
bijection and the two cells differ.
-/

open Equiv

namespace QOU.BraidKnot.DescentNodeExists

open QOU.BraidKnot.TableauPerm QOU.BraidKnot.GarnirTableau
open QOU.BraidKnot.RowStandardTableau QOU.BraidKnot.Specht
open QOU.BraidKnot.GarnirDescentAdditive QOU.Hecke.Inversions

variable {μ : YoungDiagram}

/-- **No adjacent failure forces the whole column to increase.**

The induction that separates a descent node (adjacent rows) from
`IsColStandard` (arbitrary rows). -/
theorem lt_of_noDescent {t : Specht.Tableau μ}
    (hnd : ∀ a b, ¬ IsDescentNode t a b) {j : ℕ} :
    ∀ {i i' : ℕ} (hi : (i, j) ∈ μ) (hi' : (i', j) ∈ μ), i < i' →
      (t.symm ⟨(i, j), (YoungDiagram.mem_cells _).2 hi⟩ : Fin (Specht.nOf μ))
        < t.symm ⟨(i', j), (YoungDiagram.mem_cells _).2 hi'⟩ := by
  intro i i'
  induction i' with
  | zero => intro _ _ h; omega
  | succ k ih =>
    intro hi hk1 hlt
    -- the adjacent step `k → k+1`
    have hk : (k, j) ∈ μ := μ.up_left_mem (Nat.le_succ k) (le_refl j) hk1
    have hstep : (t.symm ⟨(k, j), (YoungDiagram.mem_cells _).2 hk⟩ : Fin (Specht.nOf μ))
        < t.symm ⟨(k + 1, j), (YoungDiagram.mem_cells _).2 hk1⟩ := by
      have hnotlt : ¬ ((t.symm ⟨(k + 1, j), (YoungDiagram.mem_cells _).2 hk1⟩ :
          Fin (Specht.nOf μ)) < t.symm ⟨(k, j), (YoungDiagram.mem_cells _).2 hk⟩) :=
        fun hc => hnd k j ⟨hk1, hc⟩
      have hne : (t.symm ⟨(k, j), (YoungDiagram.mem_cells _).2 hk⟩ : Fin (Specht.nOf μ))
          ≠ t.symm ⟨(k + 1, j), (YoungDiagram.mem_cells _).2 hk1⟩ := by
        intro heq
        have hcell := t.symm.injective heq
        rw [Subtype.ext_iff, Prod.mk.injEq] at hcell
        omega
      exact lt_of_le_of_ne (not_lt.1 hnotlt) hne
    rcases Nat.lt_succ_iff_lt_or_eq.mp hlt with h | h
    · exact lt_trans (ih hi hk h) hstep
    · subst h; exact hstep

/-- The cell of a label, written out of its row and column patterns. -/
theorem mem_pattern (t : Specht.Tableau μ) (l : Fin (Specht.nOf μ)) :
    (rowPattern t l, colPattern t l) ∈ μ := by
  simp [rowPattern, colPattern]

/-- Reading a label off its own cell returns it. -/
theorem symm_pattern (t : Specht.Tableau μ) (l : Fin (Specht.nOf μ)) :
    t.symm ⟨(rowPattern t l, colPattern t l),
        (YoungDiagram.mem_cells _).2 (mem_pattern t l)⟩ = l := by
  have hc : (⟨(rowPattern t l, colPattern t l),
      (YoungDiagram.mem_cells _).2 (mem_pattern t l)⟩ : μ.cells) = t l :=
    Subtype.ext (by simp [rowPattern, colPattern])
  rw [hc, Equiv.symm_apply_apply]

/-- `symm_pattern` with the column supplied as a variable, so it transports along
an equality of columns. -/
theorem symm_pattern_of_col (t : Specht.Tableau μ) (l : Fin (Specht.nOf μ)) {j : ℕ}
    (hj : colPattern t l = j) (h : (rowPattern t l, j) ∈ μ) :
    t.symm ⟨(rowPattern t l, j), (YoungDiagram.mem_cells _).2 h⟩ = l := by
  subst hj
  exact symm_pattern t l

/-- **A row-standard tableau with no descent node is standard.** -/
theorem isStandard_of_noDescent {t : Specht.Tableau μ}
    (hrs : IsRowStandard t) (hnd : ∀ a b, ¬ IsDescentNode t a b) : IsStandard t := by
  refine ⟨hrs, ?_⟩
  intro l l' hcol hrow
  have hm : (rowPattern t l, colPattern t l) ∈ μ := mem_pattern t l
  have hm' : (rowPattern t l', colPattern t l) ∈ μ := hcol ▸ mem_pattern t l'
  have key := lt_of_noDescent hnd hm hm' hrow
  rwa [symm_pattern_of_col t l rfl hm, symm_pattern_of_col t l' hcol.symm hm'] at key

/-- **The second half of Mathas 3.13**: a row-standard tableau that is not
standard has a descent node. -/
theorem exists_descentNode_of_not_standard {t : Specht.Tableau μ}
    (hrs : IsRowStandard t) (hns : ¬ IsStandard t) :
    ∃ i j, IsDescentNode t i j := by
  by_contra hc
  push_neg at hc
  exact hns (isStandard_of_noDescent hrs (fun a b => hc a b))

/-! ### Both halves together -/

/-- **The length half of Mathas' Lemma 3.13, complete.**

For a row-standard tableau that is not standard there *exists* a Garnir tableau
whose every inversion survives in `d(t)` — which by `length_dOf_smul_eq_add_iff`
is `ℓ(d(t)) = ℓ(d(g)) + ℓ(w)` for the `w` with `t = w • g`.

The existence half is this file; the additivity half is
`invSet_garnirPerm_subset_of_descent`. -/
theorem exists_garnir_length_additive {t : Specht.Tableau μ}
    (hrs : IsRowStandard t) (hns : ¬ IsStandard t) :
    ∃ (i j : ℕ) (h : (i + 1, j) ∈ μ),
      invSet (garnirPerm i j h) ⊆ invSet (dOf t) := by
  obtain ⟨i, j, hd⟩ := exists_descentNode_of_not_standard hrs hns
  obtain ⟨h, hlt⟩ := hd
  exact ⟨i, j, h, invSet_garnirPerm_subset_of_descent hrs h ⟨h, hlt⟩⟩

/-! ### Non-vacuity by cross-check

`GarnirTableau.not_isDescentNode_refTab` proves the reference tableau has no
descent node, by an argument about `rowPrefix`.  This file's criterion then
*must* call it standard.  It does — and that is a check on both, since the two
were proved independently and neither cites the other. -/

/-- The reference tableau is standard, via the descent-node criterion. -/
theorem isStandard_refTab : IsStandard (refTab μ) :=
  isStandard_of_noDescent
    (QOU.BraidKnot.RowStandardTableau.isRowStandard_sytToTableau _)
    (fun a b => not_isDescentNode_refTab a b)

end QOU.BraidKnot.DescentNodeExists
