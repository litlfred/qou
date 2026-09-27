import QOU.Mathlib.SchenstedStandardTableau

/-!
# Generic list tableau → standard Young tableau, and `P(w)` standardness

**Brick 10.**  Factors the `insertWordSYT` construction (Brick 9b) into a
reusable primitive: any list tableau `T` with weakly-increasing rows
(`RowsSorted`), strictly-increasing columns (`ColStrict`), and content the full
set `{1, …, n}` is a `QOU.Mathlib.StandardYoungTableau` on its row-length shape
(`listStandardYT`).  The `bijOn` proof is exactly the Brick 9b assembly with the
content hypothesis abstracted.

Two immediate instances:

* the recording tableau `Q̃(w)` — content `{1,…,|w|}` unconditionally (Brick 8/9a);
* **the insertion tableau `P(w)`** — content `↑w` (`insertWord_content`), which is
  `{1,…,n}` exactly when `w` is a **permutation word** (`insertWordPSYT`).

So for a permutation word both `P(w)` and `Q(w)` are standard tableaux of the
same shape — the input to the RSK map `Sym n → Σ_λ SYT(λ)²` toward Identity-I.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

open YoungDiagram Finset

/-- **Any standard-filled list tableau is a standard Young tableau.**  A list
    tableau with weakly-increasing rows, strictly-increasing columns, and content
    `{1, …, n}` realises as a `QOU.Mathlib.StandardYoungTableau` on its row-length
    shape; its entry map bijects the cells onto `Set.Icc 1 n`. -/
noncomputable def listStandardYT {T : List (List ℕ)} {n : ℕ}
    (hrow : RowsSorted T) (hcol : ColStrict T)
    (hcontent : content T = (↑(List.range n) : Multiset ℕ).map (· + 1)) :
    StandardYoungTableau (ofRowLens (tableauShape T) (tableauShape_sorted hcol)) where
  toSsyt := toSSYT hrow hcol
  bijOn := by
    have hmap : (ofRowLens (tableauShape T) (tableauShape_sorted hcol)).cells.val.map
        (fun c : ℕ × ℕ => (T.getD c.1 []).getD c.2 0)
        = (↑(List.range n) : Multiset ℕ).map (· + 1) := by
      rw [content_eq_cells_map, hcontent]
    have hcard : (ofRowLens (tableauShape T) (tableauShape_sorted hcol)).cells.card = n := by
      have h := congrArg Multiset.card hmap
      simpa [Multiset.card_map] using h
    rw [hcard]
    have hnodup : ((ofRowLens (tableauShape T) (tableauShape_sorted hcol)).cells.val.map
        (fun c : ℕ × ℕ => (T.getD c.1 []).getD c.2 0)).Nodup := by
      rw [hmap, Multiset.map_coe, Multiset.coe_nodup]
      exact List.nodup_range.map Nat.succ_injective
    have hinj : Set.InjOn (fun c : ℕ × ℕ => (T.getD c.1 []).getD c.2 0)
        ↑(ofRowLens (tableauShape T) (tableauShape_sorted hcol)).cells :=
      nodup_map_iff_injOn.mp hnodup
    have himg : (fun c : ℕ × ℕ => (T.getD c.1 []).getD c.2 0) ''
        ↑(ofRowLens (tableauShape T) (tableauShape_sorted hcol)).cells = Set.Icc 1 n := by
      rw [← Finset.coe_image]
      have hfin : (ofRowLens (tableauShape T) (tableauShape_sorted hcol)).cells.image
          (fun c : ℕ × ℕ => (T.getD c.1 []).getD c.2 0) = Finset.Icc 1 n := by
        ext y
        simp only [Finset.mem_image, Finset.mem_Icc]
        constructor
        · rintro ⟨⟨i, j⟩, hc, rfl⟩
          have hm := Multiset.mem_map_of_mem (fun c : ℕ × ℕ => (T.getD c.1 []).getD c.2 0)
            (show (i, j) ∈ (ofRowLens (tableauShape T) (tableauShape_sorted hcol)).cells.val by
              simpa using hc)
          rw [hmap] at hm
          simp only [Multiset.mem_map, Multiset.mem_coe, List.mem_range] at hm
          obtain ⟨a, ha, hay⟩ := hm
          rw [← hay]; omega
        · rintro ⟨h1, h2⟩
          have hm : y ∈ (ofRowLens (tableauShape T) (tableauShape_sorted hcol)).cells.val.map
              (fun c : ℕ × ℕ => (T.getD c.1 []).getD c.2 0) := by
            rw [hmap]
            simp only [Multiset.mem_map, Multiset.mem_coe, List.mem_range]
            exact ⟨y - 1, by omega, by omega⟩
          rw [Multiset.mem_map] at hm
          obtain ⟨c, hc, hfc⟩ := hm
          exact ⟨c, by simpa using hc, hfc⟩
      rw [hfin, Finset.coe_Icc]
    exact himg ▸ hinj.bijOn_image

/-- **The insertion tableau `P(w)` as a standard Young tableau**, for a permutation
    word `w` (content `{1, …, n}`).  Together with `insertWordSYT` (the recording
    tableau `Q̃(w)`), this gives both halves of the RSK pair as standard tableaux. -/
noncomputable def insertWordPSYT {w : List ℕ} {n : ℕ}
    (hw : (↑w : Multiset ℕ) = (↑(List.range n) : Multiset ℕ).map (· + 1)) :
    StandardYoungTableau (ofRowLens (tableauShape (insertWord w))
      (tableauShape_sorted (insertWord_colStrict w))) :=
  listStandardYT (insertWord_rowsSorted w) (insertWord_colStrict w)
    (by rw [insertWord_content, hw])

/-- `insertWordSYT` factors through the generic primitive. -/
theorem insertWordSYT_eq (w : List ℕ) :
    insertWordSYT w = listStandardYT (shiftT_rowsSorted (insertWordRec_snd_rowsSorted w))
      (shiftT_colStrict (insertWordRec_colStrict w)) (content_shiftT_recording w) := rfl

end QOU.Mathlib.Schensted
