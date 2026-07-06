import QOU.Mathlib.SYTMaxCorner

/-!
# QOU.Mathlib.SYTEraseMax — deleting the max-value cell (forward branching map)

The forward half of the Greene–Nijenhuis–Wilf branching bijection: given a standard tableau `T` of `μ`
and the removable corner `c` carrying the top value `|μ|`, blank that cell to obtain a standard tableau
of `μ ∖ c`.  Its entry map is `T`'s, restricted to the cells of `μ ∖ c` (and `0` elsewhere); the strict
row/column laws are inherited, and the entry bijection lands on `{1, …, |μ|−1} = {1, …, |μ ∖ c|}`
because the only cell that carried `|μ|` was the deleted corner.

Pure combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open YoungDiagram

variable {μ : YoungDiagram}

/-- Membership in `μ ∖ c`, at the `cells` (Finset) level. -/
private theorem mem_erase_cells {c x : ℕ × ℕ} (hc : IsCornerCell μ c) :
    x ∈ (eraseCorner μ c hc).cells ↔ x ∈ μ ∧ x ≠ c := by
  rw [mem_cells]; exact mem_eraseCorner μ c hc x

/-- **Semistandard tableau of `μ ∖ c`** obtained by blanking the corner cell `c` of `T`. -/
def eraseMaxSsyt (T : StandardYoungTableau μ) (c : ℕ × ℕ) (hc : IsCornerCell μ c) :
    SemistandardYoungTableau (eraseCorner μ c hc) where
  entry := fun i j => if (i, j) ∈ (eraseCorner μ c hc).cells then T.entry i j else 0
  row_weak' := by
    intro i j1 j2 hj hmem
    have hmem2 : (i, j2) ∈ (eraseCorner μ c hc).cells := (mem_cells _).mpr hmem
    have hmem1 : (i, j1) ∈ (eraseCorner μ c hc).cells :=
      (mem_cells _).mpr ((eraseCorner μ c hc).up_left_mem (le_refl i) (le_of_lt hj) hmem)
    rw [if_pos hmem1, if_pos hmem2]
    exact T.toSsyt.row_weak hj (((mem_erase_cells hc).mp hmem2).1)
  col_strict' := by
    intro i1 i2 j hi hmem
    have hmem2 : (i2, j) ∈ (eraseCorner μ c hc).cells := (mem_cells _).mpr hmem
    have hmem1 : (i1, j) ∈ (eraseCorner μ c hc).cells :=
      (mem_cells _).mpr ((eraseCorner μ c hc).up_left_mem (le_of_lt hi) (le_refl j) hmem)
    rw [if_pos hmem1, if_pos hmem2]
    exact T.toSsyt.col_strict hi (((mem_erase_cells hc).mp hmem2).1)
  zeros' := by
    intro i j hmem
    rw [if_neg (fun h => hmem ((mem_cells _).mp h))]

/-- **The forward branching map.** Delete the max-value corner `c` of `T` to get a standard tableau of
`μ ∖ c`: its entry map is `T`'s on the surviving cells, and the entry bijection lands on
`{1, …, |μ ∖ c|}` because the only cell that held `|μ|` was the deleted corner. -/
def eraseMax (T : StandardYoungTableau μ) (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (hmax : T.entry c.1 c.2 = μ.cells.card) :
    StandardYoungTableau (eraseCorner μ c hc) where
  toSsyt := eraseMaxSsyt T c hc
  bijOn := by
    have hcard : (eraseCorner μ c hc).cells.card + 1 = μ.cells.card := card_eraseCorner μ c hc
    -- entry of the restricted tableau is `T.entry` on surviving cells
    have hfeq : ∀ x ∈ (eraseCorner μ c hc).cells,
        (eraseMaxSsyt T c hc).entry x.1 x.2 = T.entry x.1 x.2 := by
      intro x hx
      show (if (x.1, x.2) ∈ (eraseCorner μ c hc).cells then T.entry x.1 x.2 else 0)
        = T.entry x.1 x.2
      rw [if_pos (by simpa using hx)]
    -- only the corner `c` carries the top value `|μ|`
    have honly : ∀ d ∈ μ.cells, T.entry d.1 d.2 = μ.cells.card → d = c := by
      intro d hd he
      have hdset : d ∈ (μ.cells : Set (ℕ × ℕ)) := Finset.mem_coe.mpr hd
      have hcset : c ∈ (μ.cells : Set (ℕ × ℕ)) := Finset.mem_coe.mpr ((mem_cells _).mpr hc.1)
      exact T.injOn_cells hdset hcset (by show T.entry d.1 d.2 = T.entry c.1 c.2; rw [he, hmax])
    refine ⟨?_, ?_, ?_⟩
    · -- MapsTo
      intro x hx
      have hxc : x ∈ (eraseCorner μ c hc).cells := Finset.mem_coe.mp hx
      have hxμ : x ∈ μ := ((mem_erase_cells hc).mp hxc).1
      have hxne : x ≠ c := ((mem_erase_cells hc).mp hxc).2
      have hxin : x ∈ (μ.cells : Set (ℕ × ℕ)) := Finset.mem_coe.mpr ((mem_cells _).mpr hxμ)
      have hb := T.mapsTo_cells hxin
      rw [Set.mem_Icc] at hb
      have hb1 : 1 ≤ T.entry x.1 x.2 := hb.1
      have hb2 : T.entry x.1 x.2 ≤ μ.cells.card := hb.2
      have hne_max : T.entry x.1 x.2 ≠ μ.cells.card :=
        fun h => hxne (honly x ((mem_cells _).mpr hxμ) h)
      show (eraseMaxSsyt T c hc).entry x.1 x.2 ∈ Set.Icc 1 (eraseCorner μ c hc).cells.card
      rw [Set.mem_Icc, hfeq x hxc]
      exact ⟨hb1, by omega⟩
    · -- InjOn
      intro x hx y hy hxy
      have hxc : x ∈ (eraseCorner μ c hc).cells := Finset.mem_coe.mp hx
      have hyc : y ∈ (eraseCorner μ c hc).cells := Finset.mem_coe.mp hy
      have hxy' : T.entry x.1 x.2 = T.entry y.1 y.2 := by
        rw [← hfeq x hxc, ← hfeq y hyc]; exact hxy
      have hxin : x ∈ (μ.cells : Set (ℕ × ℕ)) :=
        Finset.mem_coe.mpr ((mem_cells _).mpr ((mem_erase_cells hc).mp hxc).1)
      have hyin : y ∈ (μ.cells : Set (ℕ × ℕ)) :=
        Finset.mem_coe.mpr ((mem_cells _).mpr ((mem_erase_cells hc).mp hyc).1)
      exact T.injOn_cells hxin hyin hxy'
    · -- SurjOn
      intro v hv
      rw [Set.mem_Icc] at hv
      have hvμ : v ∈ Set.Icc 1 μ.cells.card := by rw [Set.mem_Icc]; omega
      obtain ⟨d, hd, hde⟩ := T.bijOn.surjOn hvμ
      have hdμ : d ∈ μ := (mem_cells _).mp (Finset.mem_coe.mp hd)
      have hde' : T.entry d.1 d.2 = v := hde
      have hdne : d ≠ c := by
        intro h; subst h; rw [hmax] at hde'; omega
      have hdν : d ∈ (eraseCorner μ c hc).cells := (mem_erase_cells hc).mpr ⟨hdμ, hdne⟩
      exact ⟨d, Finset.mem_coe.mpr hdν, by
        show (eraseMaxSsyt T c hc).entry d.1 d.2 = v
        rw [hfeq d hdν]; exact hde'⟩

end QOU.Mathlib
