import QOU.BraidKnot.SpechtIrreducible

/-!
# Sagan Lemma 2.2.6 — the cross-shape dominance criterion

If `t` is a `μ`-tableau and `s` a `ν`-tableau on the same label set, and **no two
labels sharing a column of `t` share a row of `s`**, then `μ` dominates `ν`.

This is the combinatorial core of Sagan's cross-shape theory (§2.2–2.4), and the
missing ingredient of `SpechtClassification.spechtIso_imp_dom_both`.

## The argument

Fix `r` and count the labels in the first `r` rows of `s`, sorted by their column
in `t`:

* by rows of `s`, there are `Σ_{j<r} ν_j` of them;
* in a fixed column `c` of `t` there are at most `min r (μ.colLen c)` — at most
  `r` because the no-clash hypothesis makes the row-in-`s` map injective on each
  column of `t`, and at most `μ.colLen c` because that is how long the column is;
* summing over columns, `Σ_c min r (μ.colLen c)` counts the cells of `μ` in its
  first `r` rows, which is `Σ_{j<r} μ_j`.

So `Σ_{j<r} ν_j ≤ Σ_{j<r} μ_j` for every `r`, which is dominance.

## Relation to `SpechtIrreducible` §4.x

The **same-shape** specialisation of this count already lives there, inside
`row_lt_colLen`, where it feeds the Gale–Ryser matching `noclash_match_exists`.
This module states the count in the cross-shape generality Sagan's §2.4 needs.
Its two cell-counting ingredients were `private` there and are now public; they
are imported rather than re-derived.

## What this does *not* finish

`spechtIso_imp_dom_both` also needs the module-theoretic half of Sagan 2.4.4 —
the cross-shape `κ_t` acting on `M^ν`, the vanishing `κ_t {s} = 0` under a clash,
and the extension of a homomorphism `S^μ → M^ν` to `M^μ` along the decomposition
`SpechtIrreducible.isCompl_specht_perp`. See the bean for the plan.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtCrossDominance

open QOU.BraidKnot QOU.BraidKnot.Specht

/-! ## 1. Counting cells through a tableau bijection

`filterCard_reindex` and `colCells_card` are `SpechtIrreducible`'s §4.x helpers,
made public there rather than re-derived here — they are the same counts, and a
second copy would be a second thing to keep true. -/

open QOU.BraidKnot.SpechtIrreducible (filterCard_reindex colCells_card Col_card)

/-- The number of labels in the first `r` rows, read off the cells: it is the
partial sum of row lengths. -/
theorem card_cells_row_lt (μ : YoungDiagram) (r : ℕ) :
    (μ.cells.filter (fun cell => cell.1 < r)).card = ∑ j ∈ Finset.range r, μ.rowLen j := by
  classical
  rw [Finset.card_eq_sum_card_fiberwise
        (f := Prod.fst) (t := Finset.range r)
        (by intro cell hcell
            exact Finset.mem_range.mpr (Finset.mem_filter.mp hcell).2)]
  refine Finset.sum_congr rfl (fun j hj => ?_)
  rw [YoungDiagram.rowLen_eq_card, YoungDiagram.row]
  congr 1
  ext cell
  simp only [Finset.mem_filter, YoungDiagram.mem_cells]
  constructor
  · rintro ⟨⟨hmem, -⟩, hfst⟩; exact ⟨hmem, hfst⟩
  · rintro ⟨hmem, hfst⟩
    exact ⟨⟨hmem, by rw [hfst]; exact Finset.mem_range.mp hj⟩, hfst⟩

/-! ## 2. The dominance criterion, abstractly

Stated on a bare label type with the two pattern functions and their fiber
counts as hypotheses, so it can be applied across two different shapes without
transporting a tableau. -/

/-- **Sagan Lemma 2.2.6 (abstract form).**

`ct` is the column pattern of a `μ`-tableau, `rs` the row pattern of a
`ν`-tableau, both on the same `n` labels. If no two labels share both a column
under `ct` and a row under `rs`, then `μ ⊵ ν`.

The conclusion is stated as the raw partial-sum inequality, which is
definitionally `SpechtClassification.partitionDom μ ν`. -/
theorem dominance_of_noclash {n : ℕ} {μ ν : YoungDiagram} (ct rs : Fin n → ℕ)
    (hcolMem : ∀ l : Fin n, ct l ∈ μ.cells.image Prod.snd)
    (hcolCard : ∀ c : ℕ, (Finset.univ.filter (fun l : Fin n => ct l = c)).card = μ.colLen c)
    (hrowCard : ∀ r : ℕ, (Finset.univ.filter (fun l : Fin n => rs l < r)).card
        = ∑ j ∈ Finset.range r, ν.rowLen j)
    (hnoclash : ∀ a b : Fin n, ct a = ct b → rs a = rs b → a = b) :
    ∀ i, (∑ j ∈ Finset.range i, ν.rowLen j) ≤ ∑ j ∈ Finset.range i, μ.rowLen j := by
  classical
  intro r
  -- split the first-`r`-rows labels by their column under `ct`
  have hfib : (Finset.univ.filter (fun l : Fin n => rs l < r)).card
      = ∑ c ∈ μ.cells.image Prod.snd,
          (Finset.univ.filter (fun l : Fin n => rs l < r ∧ ct l = c)).card := by
    rw [Finset.card_eq_sum_card_fiberwise
          (f := ct) (t := μ.cells.image Prod.snd) (by intro l _; exact hcolMem l)]
    simp only [Finset.filter_filter]
  -- each column contributes at most `min r (colLen c)` …
  have hle : ∀ c ∈ μ.cells.image Prod.snd,
      (Finset.univ.filter (fun l : Fin n => rs l < r ∧ ct l = c)).card ≤ min r (μ.colLen c) := by
    intro c _
    refine le_min ?_ ?_
    · -- at most `r`: `rs` is injective on a column, by no-clash
      have hbound : (Finset.univ.filter (fun l : Fin n => rs l < r ∧ ct l = c)).card
          ≤ (Finset.range r).card := by
        refine Finset.card_le_card_of_injOn rs ?_ ?_
        · intro l hl
          simp only [Finset.coe_filter, Set.mem_setOf_eq, Finset.mem_univ, true_and,
            Finset.mem_coe, Finset.mem_range] at hl ⊢
          exact hl.1
        · intro l hl l' hl' heq
          simp only [Finset.coe_filter, Set.mem_setOf_eq, Finset.mem_univ, true_and] at hl hl'
          exact hnoclash l l' (hl.2.trans hl'.2.symm) heq
      rwa [Finset.card_range] at hbound
    · -- at most the column's length
      rw [← hcolCard c]
      refine Finset.card_le_card (fun l hl => ?_)
      rw [Finset.mem_filter] at hl ⊢
      exact ⟨hl.1, hl.2.2⟩
  -- … and the column bounds sum to the cells of `μ` in its first `r` rows
  have hcells : (μ.cells.filter (fun cell => cell.1 < r)).card
      = ∑ c ∈ μ.cells.image Prod.snd, min r (μ.colLen c) := by
    rw [Finset.card_eq_sum_card_fiberwise
          (f := Prod.snd) (t := μ.cells.image Prod.snd)
          (by intro cell hcell
              exact Finset.mem_image.2 ⟨cell, (Finset.mem_filter.mp hcell).1, rfl⟩)]
    refine Finset.sum_congr rfl (fun c _ => ?_)
    rw [Finset.filter_filter]
    exact colCells_card r c
  calc (∑ j ∈ Finset.range r, ν.rowLen j)
      = ∑ c ∈ μ.cells.image Prod.snd,
          (Finset.univ.filter (fun l : Fin n => rs l < r ∧ ct l = c)).card := by
        rw [← hrowCard r, hfib]
    _ ≤ ∑ c ∈ μ.cells.image Prod.snd, min r (μ.colLen c) := Finset.sum_le_sum hle
    _ = (μ.cells.filter (fun cell => cell.1 < r)).card := hcells.symm
    _ = ∑ j ∈ Finset.range r, μ.rowLen j := card_cells_row_lt μ r

/-! ## 3. The tableau-facing form

The two fiber-count hypotheses hold for any tableau, by `filterCard_reindex`. -/

/-- The labels of a tableau in column `c` number `μ.colLen c` — `Col_card`,
renamed for symmetry with `rowPattern_card`. -/
theorem colPattern_card {μ : YoungDiagram} (t : Tableau μ) (c : ℕ) :
    (Finset.univ.filter (fun l => colPattern t l = c)).card = μ.colLen c :=
  Col_card t c

/-- The labels of a tableau in the first `r` rows number `Σ_{j<r} μ_j`. -/
theorem rowPattern_card {μ : YoungDiagram} (t : Tableau μ) (r : ℕ) :
    (Finset.univ.filter (fun l => rowPattern t l < r)).card
      = ∑ j ∈ Finset.range r, μ.rowLen j := by
  classical
  have h := filterCard_reindex t (fun cell => cell.1 < r)
  simp only [rowPattern] at *
  rw [h, card_cells_row_lt]

/-- Every label of a tableau sits in a column of `μ`. -/
theorem colPattern_mem {μ : YoungDiagram} (t : Tableau μ) (l : Fin (nOf μ)) :
    colPattern t l ∈ μ.cells.image Prod.snd :=
  Finset.mem_image.2 ⟨(t l : ℕ × ℕ), (t l).2, rfl⟩

/-- **Sagan Lemma 2.2.6, for tableaux.** `t` of shape `μ` and `s` of shape `ν`
on the same labels (via `h`): if no column of `t` meets a row of `s` twice, then
`μ` dominates `ν`.

The conclusion is definitionally `SpechtClassification.partitionDom μ ν`. -/
theorem dominance_of_tableau_noclash {μ ν : YoungDiagram} (h : nOf μ = nOf ν)
    (t : Tableau μ) (s : Tableau ν)
    (hnoclash : ∀ a b : Fin (nOf μ),
      colPattern t a = colPattern t b →
      rowPattern s (Fin.cast h a) = rowPattern s (Fin.cast h b) → a = b) :
    ∀ i, (∑ j ∈ Finset.range i, ν.rowLen j) ≤ ∑ j ∈ Finset.range i, μ.rowLen j := by
  classical
  refine dominance_of_noclash (colPattern t) (fun l => rowPattern s (Fin.cast h l))
    (colPattern_mem t) (colPattern_card t) ?_ hnoclash
  -- the row count transports along the label bijection `Fin.cast h`
  intro r
  rw [← rowPattern_card s r]
  refine Finset.card_nbij (Fin.cast h) ?_ ?_ ?_
  · intro l hl
    simpa using (by simpa using hl : rowPattern s (Fin.cast h l) < r)
  · intro a _ b _ hab
    exact (Fin.cast_injective h) hab
  · intro l hl
    refine ⟨Fin.cast h.symm l, ?_, ?_⟩
    · simpa using (by simpa using hl : rowPattern s l < r)
    · exact Fin.ext rfl

/-- Zero-subtracted partial row-length deficit vanishes under the no-clash column/row tableau condition. -/
theorem partial_rowLen_sub_eq_zero_of_tableau_noclash {μ ν : YoungDiagram} (h : nOf μ = nOf ν)
    (t : Tableau μ) (s : Tableau ν)
    (hnoclash : ∀ a b : Fin (nOf μ),
      colPattern t a = colPattern t b →
      rowPattern s (Fin.cast h a) = rowPattern s (Fin.cast h b) → a = b)
    (i : ℕ) :
    (∑ j ∈ Finset.range i, ν.rowLen j) - (∑ j ∈ Finset.range i, μ.rowLen j) = 0 :=
  Nat.sub_eq_zero_of_le (dominance_of_tableau_noclash h t s hnoclash i)

end QOU.BraidKnot.SpechtCrossDominance
