import QOU.BraidKnot.SpechtGarnirWt
import QOU.BraidKnot.SpechtColInv

/-!
# QOU.BraidKnot.SpechtGarnirMeasure — the combined straightening measure

The two straightening legs decrease two different ranks:
* a **Garnir** step (a row-violation in a column-monotone tableau) strictly drops
  `colWt` (`SpechtGarnirWt`);
* a **column-sort** step (an adjacent column inversion) keeps `colWt` fixed but
  strictly drops `colInv` (`SpechtColInv`).

This file packages them lexicographically into one `ℕ`-measure
`garnirWt = colWt · K + colInv` with `K = |Fin n × Fin n| + 1 > colInv`, so that
**either** decrease strictly drops `garnirWt`. This is the single measure
`SpechtSpanningCore.span_of_measure_step` needs to drive the straightening to
standard tableaux.
-/

namespace QOU.BraidKnot.SpechtGarnirMeasure

open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtGarnirWt
open QOU.BraidKnot.SpechtColInv

variable {μ : YoungDiagram}

/-- The lexicographic packing constant: strictly larger than any `colInv`. -/
def garnirK (μ : YoungDiagram) : ℕ :=
  Fintype.card (Fin (Specht.nOf μ) × Fin (Specht.nOf μ)) + 1

theorem colInv_lt_garnirK (t : Tableau μ) : colInv t < garnirK μ :=
  Nat.lt_succ_of_le (Finset.card_le_univ _)

/-- **The combined straightening measure** `colWt · K + colInv`. -/
noncomputable def garnirWt (t : Tableau μ) : ℕ :=
  colWt t * garnirK μ + colInv t

/-- A `colWt`-drop (the Garnir step) strictly drops the combined measure: the
`colWt` term changes by `≥ K`, which dominates the whole `colInv` range. -/
theorem garnirWt_lt_of_colWt_lt {s t : Tableau μ} (h : colWt s < colWt t) :
    garnirWt s < garnirWt t := by
  unfold garnirWt
  have h1 : colWt s * garnirK μ + garnirK μ ≤ colWt t * garnirK μ := by
    have hle : colWt s + 1 ≤ colWt t := h
    have := mul_le_mul_right' hle (garnirK μ)
    rwa [add_one_mul] at this
  have h2 : colInv s < garnirK μ := colInv_lt_garnirK s
  omega

/-- A `colInv`-drop at fixed `colWt` (the column-sort step) strictly drops the
combined measure. -/
theorem garnirWt_lt_of_colInv_lt {s t : Tableau μ}
    (hw : colWt s = colWt t) (hi : colInv s < colInv t) :
    garnirWt s < garnirWt t := by
  unfold garnirWt
  rw [hw]
  omega

end QOU.BraidKnot.SpechtGarnirMeasure
