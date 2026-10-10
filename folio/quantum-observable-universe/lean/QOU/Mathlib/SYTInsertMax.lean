import QOU.Mathlib.SYTEraseMax

/-!
# QOU.Mathlib.SYTInsertMax — re-inserting the max value at a corner (inverse branching map)

The inverse half of the Greene–Nijenhuis–Wilf branching bijection: given a removable corner `c` of `μ`
and a standard tableau `S` of `μ ∖ c`, put the top value `|μ|` back into cell `c` to recover a standard
tableau of `μ`.  Strict rows/columns hold because `|μ|` exceeds every value of `S`, and `c` has no cell
to its right or below (it is a corner); the entry bijection lands on `{1, …, |μ|}` since `S` already
bijects `μ ∖ c` onto `{1, …, |μ|−1}` and `c ↦ |μ|`.

Pure combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open YoungDiagram

variable {μ : YoungDiagram}

/-- Membership in `μ ∖ c`, at the `cells` (Finset) level (re-exported for this file). -/
private theorem mem_erase_cells' {c x : ℕ × ℕ} (hc : IsCornerCell μ c) :
    x ∈ (eraseCorner μ c hc).cells ↔ x ∈ μ ∧ x ≠ c := by
  rw [mem_cells]; exact mem_eraseCorner μ c hc x

/-- **Semistandard tableau of `μ`** obtained by writing `|μ|` into the corner `c` of `S`. -/
def insertMaxSsyt (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (S : StandardYoungTableau (eraseCorner μ c hc)) : SemistandardYoungTableau μ where
  entry := fun i j => if (i, j) = c then μ.cells.card else S.entry i j
  zeros' := by
    intro i j hmem
    have hne : (i, j) ≠ c := fun h => hmem (by rw [h]; exact hc.1)
    rw [if_neg hne]
    apply S.toSsyt.zeros
    intro hin
    exact hmem ((mem_eraseCorner μ c hc (i, j)).mp hin).1
  row_weak' := by
    intro i j1 j2 hj hmem
    by_cases h2 : (i, j2) = c
    · rw [if_pos h2]
      have h1ne : (i, j1) ≠ c := by
        rw [← h2]; intro he; have := (Prod.ext_iff.mp he).2; omega
      rw [if_neg h1ne]
      have h1ν : (i, j1) ∈ eraseCorner μ c hc :=
        (mem_erase_cells' hc).mpr ⟨μ.up_left_mem (le_refl i) (le_of_lt hj) hmem, h1ne⟩
      have hb := S.mapsTo_cells (StandardYoungTableau.mem_coe_cells h1ν)
      rw [Set.mem_Icc] at hb
      have hle : S.entry i j1 ≤ (eraseCorner μ c hc).cells.card := hb.2
      have hcard := card_eraseCorner μ c hc
      omega
    · have h1ne : (i, j1) ≠ c := by
        intro h1
        apply hc.2.2
        have hc1 : c.1 = i := (Prod.ext_iff.mp h1).1.symm
        have hc2 : c.2 = j1 := (Prod.ext_iff.mp h1).2.symm
        rw [hc1, hc2]
        exact μ.up_left_mem (le_refl i) (by omega : j1 + 1 ≤ j2) hmem
      rw [if_neg h1ne, if_neg h2]
      exact S.toSsyt.row_weak hj ((mem_erase_cells' hc).mpr ⟨hmem, h2⟩)
  col_strict' := by
    intro i1 i2 j hi hmem
    by_cases h2 : (i2, j) = c
    · rw [if_pos h2]
      have h1ne : (i1, j) ≠ c := by
        rw [← h2]; intro he; have := (Prod.ext_iff.mp he).1; omega
      rw [if_neg h1ne]
      have h1ν : (i1, j) ∈ eraseCorner μ c hc :=
        (mem_erase_cells' hc).mpr ⟨μ.up_left_mem (le_of_lt hi) (le_refl j) hmem, h1ne⟩
      have hb := S.mapsTo_cells (StandardYoungTableau.mem_coe_cells h1ν)
      rw [Set.mem_Icc] at hb
      have hle : S.entry i1 j ≤ (eraseCorner μ c hc).cells.card := hb.2
      have hcard := card_eraseCorner μ c hc
      omega
    · have h1ne : (i1, j) ≠ c := by
        intro h1
        apply hc.2.1
        have hc1 : c.1 = i1 := (Prod.ext_iff.mp h1).1.symm
        have hc2 : c.2 = j := (Prod.ext_iff.mp h1).2.symm
        rw [hc1, hc2]
        exact μ.up_left_mem (by omega : i1 + 1 ≤ i2) (le_refl j) hmem
      rw [if_neg h1ne, if_neg h2]
      exact S.toSsyt.col_strict hi ((mem_erase_cells' hc).mpr ⟨hmem, h2⟩)

/-- **The inverse branching map.** Re-insert `|μ|` at the removable corner `c` of `S : SYT(μ ∖ c)` to
recover a standard tableau of `μ`. -/
def insertMax (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (S : StandardYoungTableau (eraseCorner μ c hc)) : StandardYoungTableau μ where
  toSsyt := insertMaxSsyt c hc S
  bijOn := by
    have hcard : (eraseCorner μ c hc).cells.card + 1 = μ.cells.card := card_eraseCorner μ c hc
    have hcpos : 1 ≤ μ.cells.card := by
      have : c ∈ μ.cells := (mem_cells _).mpr hc.1
      have := Finset.card_pos.mpr ⟨c, this⟩; omega
    -- entry on a non-corner cell is `S.entry`; bound `S.entry ≤ |μ∖c|`
    have hScell : ∀ x ∈ (eraseCorner μ c hc).cells,
        (insertMaxSsyt c hc S).entry x.1 x.2 = S.entry x.1 x.2 := by
      intro x hx
      have hxne : (x.1, x.2) ≠ c := by
        have := ((mem_erase_cells' hc).mp hx).2; simpa using this
      show (if (x.1, x.2) = c then μ.cells.card else S.entry x.1 x.2) = S.entry x.1 x.2
      rw [if_neg hxne]
    have hSle : ∀ x ∈ (eraseCorner μ c hc).cells, S.entry x.1 x.2 ≤ (eraseCorner μ c hc).cells.card := by
      intro x hx
      have hb := S.mapsTo_cells (Finset.mem_coe.mpr hx)
      rw [Set.mem_Icc] at hb; exact hb.2
    refine ⟨?_, ?_, ?_⟩
    · -- MapsTo
      intro x hx
      have hxμ : x ∈ μ := (mem_cells _).mp (Finset.mem_coe.mp hx)
      show (insertMaxSsyt c hc S).entry x.1 x.2 ∈ Set.Icc 1 μ.cells.card
      have hval : (insertMaxSsyt c hc S).entry x.1 x.2
          = if (x.1, x.2) = c then μ.cells.card else S.entry x.1 x.2 := rfl
      rw [Set.mem_Icc, hval]
      by_cases hxc : (x.1, x.2) = c
      · rw [if_pos hxc]; exact ⟨hcpos, le_refl _⟩
      · rw [if_neg hxc]
        have hxν : x ∈ (eraseCorner μ c hc).cells :=
          (mem_erase_cells' hc).mpr ⟨hxμ, by simpa using hxc⟩
        have hb := S.mapsTo_cells (Finset.mem_coe.mpr hxν)
        rw [Set.mem_Icc] at hb
        exact ⟨hb.1, le_trans (hSle x hxν) (by omega)⟩
    · -- InjOn
      intro x hx y hy hxy
      have hxμ : x ∈ μ := (mem_cells _).mp (Finset.mem_coe.mp hx)
      have hyμ : y ∈ μ := (mem_cells _).mp (Finset.mem_coe.mp hy)
      have key : (insertMaxSsyt c hc S).entry x.1 x.2 = (insertMaxSsyt c hc S).entry y.1 y.2 := hxy
      by_cases hxc : (x.1, x.2) = c
      · by_cases hyc : (y.1, y.2) = c
        · have ex : x = c := by simpa using hxc
          have ey : y = c := by simpa using hyc
          rw [ex, ey]
        · -- x = c, y ≠ c: values μ.card vs S.entry < μ.card, contradiction
          exfalso
          have hyν : y ∈ (eraseCorner μ c hc).cells :=
            (mem_erase_cells' hc).mpr ⟨hyμ, by simpa using hyc⟩
          rw [show (insertMaxSsyt c hc S).entry x.1 x.2 = μ.cells.card from by
                show (if (x.1, x.2) = c then μ.cells.card else _) = _; rw [if_pos hxc],
              show (insertMaxSsyt c hc S).entry y.1 y.2 = S.entry y.1 y.2 from hScell y hyν] at key
          have := hSle y hyν; omega
      · by_cases hyc : (y.1, y.2) = c
        · exfalso
          have hxν : x ∈ (eraseCorner μ c hc).cells :=
            (mem_erase_cells' hc).mpr ⟨hxμ, by simpa using hxc⟩
          rw [show (insertMaxSsyt c hc S).entry y.1 y.2 = μ.cells.card from by
                show (if (y.1, y.2) = c then μ.cells.card else _) = _; rw [if_pos hyc],
              show (insertMaxSsyt c hc S).entry x.1 x.2 = S.entry x.1 x.2 from hScell x hxν] at key
          have := hSle x hxν; omega
        · -- both ≠ c: S.injOn
          have hxν : x ∈ (eraseCorner μ c hc).cells :=
            (mem_erase_cells' hc).mpr ⟨hxμ, by simpa using hxc⟩
          have hyν : y ∈ (eraseCorner μ c hc).cells :=
            (mem_erase_cells' hc).mpr ⟨hyμ, by simpa using hyc⟩
          rw [hScell x hxν, hScell y hyν] at key
          exact S.injOn_cells (Finset.mem_coe.mpr hxν) (Finset.mem_coe.mpr hyν) key
    · -- SurjOn
      intro v hv
      rw [Set.mem_Icc] at hv
      by_cases hvmax : v = μ.cells.card
      · refine ⟨c, Finset.mem_coe.mpr ((mem_cells _).mpr hc.1), ?_⟩
        show (insertMaxSsyt c hc S).entry c.1 c.2 = v
        show (if (c.1, c.2) = c then μ.cells.card else _) = v
        rw [if_pos (by rfl), hvmax]
      · have hvν : v ∈ Set.Icc 1 (eraseCorner μ c hc).cells.card := by
          rw [Set.mem_Icc]; omega
        obtain ⟨d, hd, hde⟩ := S.bijOn.surjOn hvν
        have hdν : d ∈ (eraseCorner μ c hc).cells := Finset.mem_coe.mp hd
        have hdμ : d ∈ μ := ((mem_erase_cells' hc).mp hdν).1
        refine ⟨d, Finset.mem_coe.mpr ((mem_cells _).mpr hdμ), ?_⟩
        show (insertMaxSsyt c hc S).entry d.1 d.2 = v
        rw [hScell d hdν]; exact hde

end QOU.Mathlib
