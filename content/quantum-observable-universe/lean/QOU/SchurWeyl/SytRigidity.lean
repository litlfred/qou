import QOU.SchurWeyl.TableauCells

/-!
# `QOU.SchurWeyl.SytRigidity` — a tableau no generator moves forces `#SYT μ = 1`

The last gap of `hoefsmit_seminormal_rep` (bean `qou-im9l`, child `qou-gjg6`) is the
**non-scalarity** side: `SeminormalRep.genMat_ne_scalar` supplies a non-scalar generator as
soon as *some* generator moves *some* tableau, so what is missing is

  `2 ≤ #SYT μ  ⟹  ∃ T, ∃ k, SwapAdmissible T k`.

`TableauCells` already reduces the hard direction: a tableau admitting **no** admissible
swap has all its cells in one row (`row_const_of_no_admissible`) or one column
(`col_const_of_no_admissible`).  This file closes the remaining step — such a shape carries
exactly one tableau — and assembles the statement above.

The route avoids the full SYT-connectivity theorem (that any two standard tableaux are
joined by a chain of admissible swaps), which is much stronger than what is needed.

## Contents

* `syt_eq_of_cellOf_eq` — two tableaux with the same cell-of-value map are equal.
* `cellOf_col_succ_of_row` / `cellOf_row_succ_of_col` — in the immovable row (resp. column)
  case the cells advance by one column (resp. row) per value.
* `cellOf_eq_of_no_admissible_row` / `_col` — hence `cellOf T j` is `(r, j-1)` (resp.
  `(j-1, c)`), completely determined.
* `exists_admissible_of_ne` — **the target**: two distinct tableaux force an admissible swap.

Base: no `q` anywhere — this is pure tableau combinatorics.
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)

namespace TableauCells

variable {μ : YoungDiagram}

/-- Two standard tableaux of the same shape that place every value in the same cell are
equal.  Inside the diagram the entry is recovered from the cell map (`entry_cellOf`);
outside it both vanish. -/
theorem syt_eq_of_cellOf_eq (U V : StandardYoungTableau μ)
    (h : ∀ j ∈ Set.Icc 1 μ.cells.card, cellOf U j = cellOf V j) : U = V := by
  have hs : U.toSsyt = V.toSsyt := by
    apply SemistandardYoungTableau.ext
    intro i j
    by_cases hij : (i, j) ∈ μ
    · have hmem : (i, j) ∈ μ.cells := by rwa [YoungDiagram.mem_cells]
      have hkI : U.toSsyt.entry i j ∈ Set.Icc 1 μ.cells.card := U.bijOn.mapsTo hmem
      have hcU : cellOf U (U.toSsyt.entry i j) = (i, j) := cellOf_unique U hmem rfl
      have hcV : cellOf V (U.toSsyt.entry i j) = (i, j) := by
        rw [← h _ hkI]; exact hcU
      have hv := entry_cellOf V hkI
      rw [hcV] at hv
      exact hv.symm
    · rw [SemistandardYoungTableau.zeros U.toSsyt hij,
        SemistandardYoungTableau.zeros V.toSsyt hij]
  cases U; cases V; cases hs; rfl

/-- Every cell is the cell of its own entry, and that entry lies in `[1, |μ|]`. -/
theorem exists_cellOf_eq (T : StandardYoungTableau μ) {c : ℕ × ℕ} (hc : c ∈ μ.cells) :
    ∃ j ∈ Set.Icc 1 μ.cells.card, cellOf T j = c := by
  refine ⟨T.toSsyt.entry c.1 c.2, T.bijOn.mapsTo hc, ?_⟩
  exact cellOf_unique T hc rfl

/-! ## The immovable row case: cells advance one column per value -/

/-- In the immovable **row** case consecutive values sit in adjacent columns of one row. -/
theorem cellOf_col_succ_of_row (T : StandardYoungTableau μ)
    (h : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → ¬ SwapAdmissible T m)
    (hd : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → axialDist T m = 1)
    {k : ℕ} (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) :
    (cellOf T (k + 1)).2 = (cellOf T k).2 + 1 := by
  have hrow : (cellOf T k).1 = (cellOf T (k + 1)).1 :=
    sameRow_of_not_admissible_of_one T hk hkn (h k hk hkn) (hd k hk hkn)
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hm1 : ((cellOf T k).1, (cellOf T k).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using cellOf_mem T hkI
  have hm2 : ((cellOf T k).1, (cellOf T (k + 1)).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells, hrow]; simpa using cellOf_mem T hkI'
  exact sameRow_adjacent T hm1 hm2 (entry_cellOf T hkI)
    (by rw [hrow]; exact entry_cellOf T hkI')

/-- The mirror: in the immovable **column** case consecutive values sit in adjacent rows. -/
theorem cellOf_row_succ_of_col (T : StandardYoungTableau μ)
    (h : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → ¬ SwapAdmissible T m)
    (hd : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → axialDist T m = -1)
    {k : ℕ} (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) :
    (cellOf T (k + 1)).1 = (cellOf T k).1 + 1 := by
  have hcol : (cellOf T k).2 = (cellOf T (k + 1)).2 :=
    sameCol_of_not_admissible_of_neg_one T hk hkn (h k hk hkn) (hd k hk hkn)
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  have hm1 : ((cellOf T k).1, (cellOf T k).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using cellOf_mem T hkI
  have hm2 : ((cellOf T (k + 1)).1, (cellOf T k).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells, hcol]; simpa using cellOf_mem T hkI'
  exact sameCol_adjacent T hm1 hm2 (entry_cellOf T hkI)
    (by rw [hcol]; exact entry_cellOf T hkI')

/-- Chained: in the immovable row case the column advances by one per value. -/
theorem cellOf_col_of_row (T : StandardYoungTableau μ)
    (h : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → ¬ SwapAdmissible T m)
    (hd : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → axialDist T m = 1) :
    ∀ j, 1 ≤ j → j ≤ μ.cells.card → (cellOf T j).2 = (cellOf T 1).2 + (j - 1) := by
  intro j
  induction j with
  | zero => omega
  | succ j ih =>
    intro _ hjn
    rcases Nat.lt_or_ge 1 (j + 1) with hlt | hge
    · have hj1 : 1 ≤ j := by omega
      have hstep : (cellOf T (j + 1)).2 = (cellOf T j).2 + 1 :=
        cellOf_col_succ_of_row T h hd hj1 (by omega)
      rw [hstep, ih hj1 (by omega)]
      omega
    · have hj : j + 1 = 1 := by omega
      rw [hj]; omega

/-- Mirror of `cellOf_col_of_row` for the immovable column case. -/
theorem cellOf_row_of_col (T : StandardYoungTableau μ)
    (h : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → ¬ SwapAdmissible T m)
    (hd : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → axialDist T m = -1) :
    ∀ j, 1 ≤ j → j ≤ μ.cells.card → (cellOf T j).1 = (cellOf T 1).1 + (j - 1) := by
  intro j
  induction j with
  | zero => omega
  | succ j ih =>
    intro _ hjn
    rcases Nat.lt_or_ge 1 (j + 1) with hlt | hge
    · have hj1 : 1 ≤ j := by omega
      have hstep : (cellOf T (j + 1)).1 = (cellOf T j).1 + 1 :=
        cellOf_row_succ_of_col T h hd hj1 (by omega)
      rw [hstep, ih hj1 (by omega)]
      omega
    · have hj : j + 1 = 1 := by omega
      rw [hj]; omega

/-! ## The immovable cases pin every cell -/

/-- **Immovable row case: the tableau is the single row.**  `cellOf T j = (0, j-1)`. -/
theorem cellOf_eq_of_row (T : StandardYoungTableau μ) (hcard : 1 ≤ μ.cells.card)
    (h : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → ¬ SwapAdmissible T m)
    (hd : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → axialDist T m = 1)
    {j : ℕ} (hj : 1 ≤ j) (hjn : j ≤ μ.cells.card) :
    cellOf T j = (0, j - 1) := by
  have h1I : (1 : ℕ) ∈ Set.Icc 1 μ.cells.card := ⟨le_refl _, hcard⟩
  have hmem1 : ((cellOf T 1).1, (cellOf T 1).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using cellOf_mem T h1I
  -- the starting column is 0
  have hc0 : (cellOf T 1).2 = 0 := by
    by_contra hne
    have hpos : 0 < (cellOf T 1).2 := Nat.pos_of_ne_zero hne
    have hleft : ((cellOf T 1).1, (cellOf T 1).2 - 1) ∈ μ :=
      μ.up_left_mem (le_refl _) (by omega) hmem1
    obtain ⟨i, hiI, hi⟩ := exists_cellOf_eq T (by rw [YoungDiagram.mem_cells]; exact hleft)
    have hcol := cellOf_col_of_row T h hd i hiI.1 hiI.2
    have hsnd : (cellOf T i).2 = (cellOf T 1).2 - 1 := by rw [hi]
    omega
  -- the row is 0
  have hr0 : (cellOf T 1).1 = 0 := by
    have h00 : ((0 : ℕ), (0 : ℕ)) ∈ μ := by
      have hm := hmem1
      rw [hc0] at hm
      exact μ.up_left_mem (Nat.zero_le _) (le_refl 0) hm
    obtain ⟨i, hiI, hi⟩ := exists_cellOf_eq T (by rw [YoungDiagram.mem_cells]; exact h00)
    have hrow := row_const_of_no_admissible T h hd hiI.1 hiI.2
    have hfst : (cellOf T i).1 = 0 := by rw [hi]
    omega
  have hrowj := row_const_of_no_admissible T h hd hj hjn
  have hcolj := cellOf_col_of_row T h hd j hj hjn
  refine Prod.ext ?_ ?_
  · rw [hrowj, hr0]
  · rw [hcolj, hc0]; omega

/-- **Immovable column case: the tableau is the single column.**  `cellOf T j = (j-1, 0)`. -/
theorem cellOf_eq_of_col (T : StandardYoungTableau μ) (hcard : 1 ≤ μ.cells.card)
    (h : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → ¬ SwapAdmissible T m)
    (hd : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → axialDist T m = -1)
    {j : ℕ} (hj : 1 ≤ j) (hjn : j ≤ μ.cells.card) :
    cellOf T j = (j - 1, 0) := by
  have h1I : (1 : ℕ) ∈ Set.Icc 1 μ.cells.card := ⟨le_refl _, hcard⟩
  have hmem1 : ((cellOf T 1).1, (cellOf T 1).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using cellOf_mem T h1I
  have hr0 : (cellOf T 1).1 = 0 := by
    by_contra hne
    have hpos : 0 < (cellOf T 1).1 := Nat.pos_of_ne_zero hne
    have hup : ((cellOf T 1).1 - 1, (cellOf T 1).2) ∈ μ :=
      μ.up_left_mem (by omega) (le_refl _) hmem1
    obtain ⟨i, hiI, hi⟩ := exists_cellOf_eq T (by rw [YoungDiagram.mem_cells]; exact hup)
    have hrow := cellOf_row_of_col T h hd i hiI.1 hiI.2
    have hfst : (cellOf T i).1 = (cellOf T 1).1 - 1 := by rw [hi]
    omega
  have hc0 : (cellOf T 1).2 = 0 := by
    have h00 : ((0 : ℕ), (0 : ℕ)) ∈ μ := by
      have hm := hmem1
      rw [hr0] at hm
      exact μ.up_left_mem (le_refl 0) (Nat.zero_le _) hm
    obtain ⟨i, hiI, hi⟩ := exists_cellOf_eq T (by rw [YoungDiagram.mem_cells]; exact h00)
    have hcol := col_const_of_no_admissible T h hd hiI.1 hiI.2
    have hsnd : (cellOf T i).2 = 0 := by rw [hi]
    omega
  have hcolj := col_const_of_no_admissible T h hd hj hjn
  have hrowj := cellOf_row_of_col T h hd j hj hjn
  refine Prod.ext ?_ ?_
  · rw [hrowj, hr0]; omega
  · rw [hcolj, hc0]

/-! ## The target: two distinct tableaux force an admissible swap -/

/-- Every tableau that no generator moves is *either* the single row *or* the single
column — both completely determined. -/
theorem cellOf_row_or_col_of_no_admissible (T : StandardYoungTableau μ)
    (hcard2 : 2 ≤ μ.cells.card)
    (hno : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → ¬ SwapAdmissible T m) :
    (∀ j, 1 ≤ j → j ≤ μ.cells.card → cellOf T j = (0, j - 1)) ∨
      (∀ j, 1 ≤ j → j ≤ μ.cells.card → cellOf T j = (j - 1, 0)) := by
  have hcard1 : 1 ≤ μ.cells.card := by omega
  have htri := axialDist_trichotomy T ⟨le_refl 1, by omega⟩ ⟨by omega, hcard2⟩
  rcases htri with hone | hneg | hadm
  · left
    have hall : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → axialDist T m = 1 := by
      intro m hm hmn
      have he : axialDist T m = axialDist T 1 :=
        axialDist_eq_of_no_admissible T hno (le_refl 1) hm hmn
      rw [he, hone]
    intro j hj hjn
    exact cellOf_eq_of_row T hcard1 hno hall hj hjn
  · right
    have hall : ∀ m, 1 ≤ m → m + 1 ≤ μ.cells.card → axialDist T m = -1 := by
      intro m hm hmn
      have he : axialDist T m = axialDist T 1 :=
        axialDist_eq_of_no_admissible T hno (le_refl 1) hm hmn
      rw [he, hneg]
    intro j hj hjn
    exact cellOf_eq_of_col T hcard1 hno hall hj hjn
  · exact absurd hadm (hno 1 (le_refl 1) hcard2)

/-- **Two distinct standard tableaux force an admissible swap.**  This is the missing input
to non-scalarity in `hoefsmit_seminormal_rep`: with `2 ≤ #SYT μ` some generator moves some
tableau, so `SeminormalRep.genMat_ne_scalar` applies.

Proof: if no generator moved any tableau, each tableau would be pinned to the single row
`(0, j-1)` or the single column `(j-1, 0)`.  Two same-orientation tableaux then agree on
every cell, hence are equal; two different-orientation ones put the second value at both
`(0,1)` and `(1,0)`, which no single shape allows. -/
theorem exists_admissible_of_ne {U V : StandardYoungTableau μ} (hUV : U ≠ V) :
    ∃ (T : StandardYoungTableau μ) (k : ℕ),
      1 ≤ k ∧ k + 1 ≤ μ.cells.card ∧ SwapAdmissible T k := by
  by_contra hcon
  push_neg at hcon
  have hno : ∀ (T : StandardYoungTableau μ) m, 1 ≤ m → m + 1 ≤ μ.cells.card →
      ¬ SwapAdmissible T m := fun T m h1 h2 => hcon T m h1 h2
  -- With at most one cell the tableau is unique, contradicting `U ≠ V`.
  have hcard2 : 2 ≤ μ.cells.card := by
    by_contra hlt
    push_neg at hlt
    refine hUV (syt_eq_of_cellOf_eq U V ?_)
    intro j hj
    have hc1 : μ.cells.card = 1 := by have := hj.1; have := hj.2; omega
    obtain ⟨a, ha⟩ := Finset.card_eq_one.mp hc1
    have hU := cellOf_mem U hj
    have hV := cellOf_mem V hj
    rw [ha, Finset.mem_singleton] at hU hV
    rw [hU, hV]
  -- Otherwise each tableau is pinned to a row or a column.
  have hmix : ∀ (A B : StandardYoungTableau μ),
      (∀ j, 1 ≤ j → j ≤ μ.cells.card → cellOf A j = (0, j - 1)) →
      (∀ j, 1 ≤ j → j ≤ μ.cells.card → cellOf B j = (j - 1, 0)) → False := by
    intro A B hArow hBcol
    have h2I : (2 : ℕ) ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hcard2⟩
    have hc : cellOf B 2 = (1, 0) := by
      have := hBcol 2 (by omega) hcard2; simpa using this
    obtain ⟨i, hiI, hi⟩ := exists_cellOf_eq A (cellOf_mem B h2I)
    have hrow := hArow i hiI.1 hiI.2
    rw [hi, hc] at hrow
    exact absurd (congrArg Prod.fst hrow) (by simp)
  rcases cellOf_row_or_col_of_no_admissible U hcard2 (hno U) with hUrow | hUcol <;>
    rcases cellOf_row_or_col_of_no_admissible V hcard2 (hno V) with hVrow | hVcol
  · exact hUV (syt_eq_of_cellOf_eq U V
      (fun j hj => by rw [hUrow j hj.1 hj.2, hVrow j hj.1 hj.2]))
  · exact hmix U V hUrow hVcol
  · exact hmix V U hVrow hUcol
  · exact hUV (syt_eq_of_cellOf_eq U V
      (fun j hj => by rw [hUcol j hj.1 hj.2, hVcol j hj.1 hj.2]))

end TableauCells

end QOU.SchurWeyl
