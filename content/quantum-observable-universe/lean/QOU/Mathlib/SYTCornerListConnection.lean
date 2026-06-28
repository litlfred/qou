import QOU.Mathlib.SYTListCorner
import QOU.Mathlib.SYTBranchingRule
import QOU.Mathlib.SYTEnumerationFintype

/-!
# QOU.Mathlib.SYTCornerListConnection — discharging `cornerRecursion` via the structural branching rule

Connects the list-level corner combinatorics (`corners l`, `removeCorner l i`) to the structural GNW
branching count (`numStandardYoungTableaux_branching`), through the counting bridge
`numSYTenum l = numStandardYoungTableaux (ofRowLens l hl)`.

The geometric heart is `eraseCorner_ofRowLens`: deleting the corner cell `(i, λ_i − 1)` from the
diagram of `λ` gives the diagram of `removeCorner λ i`.

Pure combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (sz)

/-- `getD` at an in-range index. -/
private theorem getD_lt (l : List ℕ) {r : ℕ} (h : r < l.length) : l.getD r 0 = l[r] := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h, Option.getD_some]

/-- `getD` past the end is the default. -/
private theorem getD_ge (l : List ℕ) {r : ℕ} (h : l.length ≤ r) : l.getD r 0 = 0 := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none h, Option.getD_none]

/-- **Filtering trailing zeros preserves `getD` at every index, for a descending-sorted list.** In a
list sorted `≥`, the nonzero entries are a prefix, so `filter (· ≠ 0)` drops only trailing zeros and
the indexed lookup is unchanged (out-of-range lookups are `0` on both sides). -/
theorem filter_ne_zero_getD : ∀ (m : List ℕ), List.Sorted (· ≥ ·) m → ∀ r,
    (m.filter (· != 0)).getD r 0 = m.getD r 0
  | [], _, r => by simp
  | a :: t, hm, r => by
    have ht : List.Sorted (· ≥ ·) t := (List.sorted_cons.mp hm).2
    by_cases ha : a = 0
    · have htz : ∀ x ∈ t, x = 0 := fun x hx => by
        have : a ≥ x := (List.sorted_cons.mp hm).1 x hx
        omega
      have hft : (t.filter (· != 0)) = [] := by
        rw [List.filter_eq_nil_iff]; intro x hx; simp [htz x hx]
      have hae : (a != 0) = false := by simp only [ha]; rfl
      rw [List.filter_cons, hae, if_neg (by simp), hft]
      cases r with
      | zero => subst ha; simp
      | succ n =>
        rw [List.getD_nil, List.getD_cons_succ]
        rcases Nat.lt_or_ge n t.length with h | h
        · rw [getD_lt t h]; exact (htz _ (List.getElem_mem h)).symm
        · rw [getD_ge t h]
    · have hae : (a != 0) = true := by simpa using ha
      rw [List.filter_cons, hae, if_pos (by simpa using ha)]
      cases r with
      | zero => simp
      | succ n => simp only [List.getD_cons_succ]; exact filter_ne_zero_getD t ht n

/-- **Row-length lookup of `removeCorner`.** For a removable corner `i` of a descending shape,
`removeCorner λ i` has row lengths `λ` with row `i` decremented (and the vanished last row dropped). -/
theorem removeCorner_getD (l : List ℕ) (i : ℕ) (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l i)
    (r : ℕ) :
    (removeCorner l i).getD r 0 = if r = i then l.getD i 0 - 1 else l.getD r 0 := by
  unfold removeCorner
  rw [filter_ne_zero_getD _ (sorted_set_corner l i hl hc)]
  by_cases hr : r = i
  · subst hr
    rw [if_pos rfl, getD_lt _ (by rw [List.length_set]; exact hc.1), List.getElem_set_self]
  · rw [if_neg hr]
    rcases Nat.lt_or_ge r l.length with h | h
    · rw [getD_lt _ (by rw [List.length_set]; exact h),
        List.getElem_set_ne (Ne.symm hr), getD_lt _ h]
    · rw [getD_ge _ (by rw [List.length_set]; exact h), getD_ge _ h]

open YoungDiagram

/-- Cell membership in `ofRowLens` via `getD`: `(r,c) ∈ ofRowLens w hw ↔ c < w_r`. -/
theorem mem_ofRowLens_iff (w : List ℕ) (hw : List.Sorted (· ≥ ·) w) (r c : ℕ) :
    ((r, c) ∈ ofRowLens w hw) ↔ c < w.getD r 0 := by
  rw [YoungDiagram.mem_ofRowLens]
  constructor
  · rintro ⟨h, hc⟩; rw [getD_lt w h]; exact hc
  · intro hc
    rcases Nat.lt_or_ge r w.length with h | h
    · exact ⟨h, by rw [← getD_lt w h]; exact hc⟩
    · rw [getD_ge w h] at hc; omega

/-- The corner cell of row `i` is `(i, λ_i − 1)`. -/
def cornerCell (l : List ℕ) (i : ℕ) : ℕ × ℕ := (i, l.getD i 0 - 1)

/-- **List corner ⇔ diagram corner.** Row index `i` is a removable corner of `λ` iff the cell
`(i, λ_i − 1)` is a removable corner of the diagram of `λ`. -/
theorem isCornerCell_ofRowLens_iff (l : List ℕ) (i : ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) :
    IsCornerCell (ofRowLens l hl) (cornerCell l i) ↔ IsCorner l i := by
  unfold IsCornerCell IsCorner cornerCell
  simp only [mem_ofRowLens_iff]
  constructor
  · rintro ⟨_hin, _hright, hdown⟩
    -- hdown : ¬ (l.getD i 0 - 1 < l.getD (i+1) 0); _hin : l.getD i 0 - 1 < l.getD i 0
    have hilen : i < l.length := by
      by_contra h
      rw [getD_ge l (by omega)] at _hin; omega
    have hpi : 1 ≤ l.getD i 0 := by
      rw [getD_lt l hilen]; exact hpos _ (List.getElem_mem hilen)
    exact ⟨hilen, by omega⟩
  · rintro ⟨hilen, hnext⟩
    have hpi : 1 ≤ l.getD i 0 := by
      rw [getD_lt l hilen]; exact hpos _ (List.getElem_mem hilen)
    refine ⟨by omega, by omega, by omega⟩

/-- **The geometric heart.** Deleting the corner cell `(i, λ_i − 1)` from the diagram of `λ` gives the
diagram of `removeCorner λ i`. -/
theorem eraseCorner_ofRowLens (l : List ℕ) (i : ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) (hci : IsCorner l i)
    (hcc : IsCornerCell (ofRowLens l hl) (cornerCell l i)) :
    eraseCorner (ofRowLens l hl) (cornerCell l i) hcc
      = ofRowLens (removeCorner l i) (sorted_removeCorner l i hl hci) := by
  have hpi : 1 ≤ l.getD i 0 := by
    rw [getD_lt l hci.1]; exact hpos _ (List.getElem_mem hci.1)
  apply YoungDiagram.ext
  ext x
  obtain ⟨r, c⟩ := x
  rw [mem_cells, mem_cells, mem_eraseCorner, mem_ofRowLens_iff, mem_ofRowLens_iff,
    removeCorner_getD l i hl hci]
  unfold cornerCell
  by_cases hr : r = i
  · rw [hr, if_pos rfl]
    simp only [ne_eq, Prod.mk.injEq, true_and]
    omega
  · simp only [if_neg hr]
    constructor
    · rintro ⟨h, _⟩; exact h
    · intro h; exact ⟨h, fun heq => hr (congrArg Prod.fst heq)⟩

/-- **A diagram corner is the last cell of its row.** Any removable corner `cell` of the diagram of `λ`
equals `cornerCell λ (row)` — its column is `λ_row − 1`. -/
theorem eq_cornerCell_of_isCornerCell (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (cell : ℕ × ℕ)
    (h : IsCornerCell (ofRowLens l hl) cell) : cell = cornerCell l cell.1 := by
  obtain ⟨r, c⟩ := cell
  obtain ⟨hin, _hdown, hright⟩ := h
  dsimp only at hin hright
  rw [mem_ofRowLens_iff] at hin hright
  dsimp only [cornerCell]
  simp only [Prod.mk.injEq, true_and]
  omega

/-- **Per-corner summand equality.** The structural count of the corner-deleted diagram equals the
brute-force count of the list-level `removeCorner`. -/
theorem num_eraseCorner_eq (l : List ℕ) (i : ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hpos : ∀ a ∈ l, 0 < a) (hci : IsCorner l i)
    (hcc : IsCornerCell (ofRowLens l hl) (cornerCell l i)) :
    numStandardYoungTableaux (eraseCorner (ofRowLens l hl) (cornerCell l i) hcc)
      = numSYTenum (removeCorner l i) := by
  rw [eraseCorner_ofRowLens l i hl hpos hci hcc,
    ← numSYTenum_eq_numStandardYoungTableaux (removeCorner l i) (sorted_removeCorner l i hl hci)]

/-- Corner removal depends only on the cell: equal corner cells give the same diagram. -/
theorem eraseCorner_congr {μ : YoungDiagram} {a b : ℕ × ℕ} (ha : IsCornerCell μ a)
    (hb : IsCornerCell μ b) (hab : a = b) : eraseCorner μ a ha = eraseCorner μ b hb := by
  subst hab; apply YoungDiagram.ext; rfl

/-- A removable corner row index belongs to `corners l`. -/
theorem mem_corners_of {l : List ℕ} {i : ℕ} (h : IsCorner l i) : i ∈ corners l := by
  unfold corners
  rw [List.mem_filter, List.mem_range]
  exact ⟨h.1, decide_eq_true h⟩

/-- **`cornerRecursion`, discharged.** `#SYT(λ) = ∑_{removable corners i} #SYT(removeCorner λ i)`,
proved through the structural branching rule and the diagram↔list corner correspondence. -/
theorem cornerRecursion_proof (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a)
    (hne : l ≠ []) :
    numSYTenum l = ((corners l).map (fun i => numSYTenum (removeCorner l i))).sum := by
  have hszpos : 0 < (ofRowLens l hl).cells.card := by
    rw [card_cells_ofRowLens l hl]
    cases l with
    | nil => exact absurd rfl hne
    | cons a t => have := hpos a (List.mem_cons_self ..); simp only [List.sum_cons]; omega
  rw [numSYTenum_eq_numStandardYoungTableaux l hl, numStandardYoungTableaux_branching hszpos]
  -- replace each structural summand by its list-level count
  have hsummand : ∀ cc : {cell : ℕ × ℕ // IsCornerCell (ofRowLens l hl) cell},
      numStandardYoungTableaux (eraseCorner (ofRowLens l hl) cc.1 cc.2)
        = numSYTenum (removeCorner l cc.1.1) := by
    intro cc
    have hcell : cc.1 = cornerCell l cc.1.1 := eq_cornerCell_of_isCornerCell l hl cc.1 cc.2
    have hcc' : IsCornerCell (ofRowLens l hl) (cornerCell l cc.1.1) := hcell ▸ cc.2
    have hci : IsCorner l cc.1.1 := (isCornerCell_ofRowLens_iff l cc.1.1 hl hpos).mp hcc'
    rw [eraseCorner_congr cc.2 hcc' hcell, num_eraseCorner_eq l cc.1.1 hl hpos hci hcc']
  rw [Finset.sum_congr rfl (fun cc _ => hsummand cc)]
  -- reindex the corner subtype onto `corners l`
  have hnodup : (corners l).Nodup := List.Nodup.filter _ (List.nodup_range)
  rw [← List.sum_toFinset _ hnodup]
  refine Finset.sum_bij (fun cc _ => cc.1.1) ?_ ?_ ?_ ?_
  · -- hi : the row index is a corner
    intro cc _
    rw [List.mem_toFinset]
    exact mem_corners_of ((isCornerCell_ofRowLens_iff l cc.1.1 hl hpos).mp
      (eq_cornerCell_of_isCornerCell l hl cc.1 cc.2 ▸ cc.2))
  · -- i_inj
    intro cc1 _ cc2 _ heq
    have h1 := eq_cornerCell_of_isCornerCell l hl cc1.1 cc1.2
    have h2 := eq_cornerCell_of_isCornerCell l hl cc2.1 cc2.2
    exact Subtype.ext (h1.trans ((congrArg (cornerCell l) heq).trans h2.symm))
  · -- i_surj
    intro b hb
    rw [List.mem_toFinset] at hb
    have hci : IsCorner l b := mem_corners hb
    exact ⟨⟨cornerCell l b, (isCornerCell_ofRowLens_iff l b hl hpos).mpr hci⟩,
      Finset.mem_univ _, rfl⟩
  · -- summand equality
    intro cc _
    rfl

end QOU.Mathlib.SYTEnum
