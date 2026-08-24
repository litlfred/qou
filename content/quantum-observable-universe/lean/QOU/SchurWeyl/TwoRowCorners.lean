import QOU.SchurWeyl.OcneanuWeightBranching
import QOU.Mathlib.YoungDiagramCornerReindex

/-!
# QOU.SchurWeyl.TwoRowCorners — the corners of a ≤2-row diagram, and what adding one does

`MarkovAssembly` reduces the Markov condition to a per-corner identity quantified over **every**
diagram `ν` and every removable corner of it.  `OcneanuWeightMarkovCorner` proves that identity at
convention D in the form the arithmetic wants — as a two-term statement about `twoRow`.  Between
the two sits pure combinatorics: *which* cells are addable, *which* are removable, and *what
diagram* adding one produces.  This file is that layer.

| | |
|---|---|
| `isAddableCell_twoRow_iff` | addable ⟺ `(0,m)`, or `(1,k)` with `k < m`, or `(2,0)` with `0 < k` |
| `isCornerCell_twoRow_iff` | removable ⟺ `(0,m−1)` with `k < m`, or `(1,k−1)` with `0 < k` |
| `addableTwoRow`, `sum_addable_twoRow`, `sum_addableTwoRow_expand` | the addable-cell sum, as at most three explicit terms |
| `addCell_twoRow_row0`, `addCell_twoRow_row1` | adding at the end of a row gives the next `twoRow` |
| `rowLen_two_addCell_row2` | adding `(2,0)` gives a 3-row diagram — hence weight zero at convention D |

## Why the third addable cell does not need arithmetic

A ≤2-row diagram has up to **three** addable cells, but `OcneanuWeightMarkovCorner` is a **two**-term
identity.  The gap is closed not by an arithmetic cancellation but by the convention-D vanishing:
`(2,0)` produces a 3-row diagram, whose Ocneanu weight is `0`.  `rowLen_two_addCell_row2` is the
combinatorial half of that argument.

## Base ring (§7c)

None — pure `ℕ × ℕ` combinatorics.  Nothing archimedean, no ring.

LaTeX label: `thm:two-row-corners`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib YoungDiagram

variable {m k : ℕ}

theorem isAddableCell_twoRow_iff (h : k ≤ m) (s : ℕ × ℕ) :
    IsAddableCell (twoRow m k h) s ↔
      s = (0, m) ∨ (s = (1, k) ∧ k < m) ∨ (s = (2, 0) ∧ 0 < k) := by
  obtain ⟨i, j⟩ := s
  simp only [IsAddableCell, mem_twoRow h, Prod.mk.injEq]
  constructor
  · rintro ⟨hnot, h1, h2⟩
    push_neg at hnot
    match i with
    | 0 =>
      have hj : m ≤ j := by simpa using hnot
      have hj2 : j = 0 ∨ j - 1 < m := by
        rcases h2 with hz | (⟨-, hlt⟩ | ⟨hc, -⟩)
        · exact Or.inl (by simpa using hz)
        · exact Or.inr hlt
        · exact absurd hc (by omega)
      exact Or.inl ⟨rfl, by omega⟩
    | 1 =>
      have hj : k ≤ j := by simpa using hnot
      have hkm : k < m := by
        rcases h1 with hc | (⟨-, hlt⟩ | ⟨hc, -⟩)
        · exact absurd hc (by omega)
        · omega
        · exact absurd hc (by omega)
      have hj2 : j = 0 ∨ j - 1 < k := by
        rcases h2 with hz | (⟨hc, -⟩ | ⟨-, hlt⟩)
        · exact Or.inl (by simpa using hz)
        · exact absurd hc (by omega)
        · exact Or.inr hlt
      exact Or.inr (Or.inl ⟨⟨rfl, by omega⟩, hkm⟩)
    | 2 =>
      have hj0 : j = 0 := by
        rcases h2 with hz | (⟨hc, -⟩ | ⟨hc, -⟩)
        · simpa using hz
        · exact absurd hc (by omega)
        · exact absurd hc (by omega)
      have hk0 : 0 < k := by
        rcases h1 with hc | (⟨hc, -⟩ | ⟨-, hlt⟩)
        · exact absurd hc (by omega)
        · exact absurd hc (by omega)
        · omega
      exact Or.inr (Or.inr ⟨⟨rfl, hj0⟩, hk0⟩)
    | (n+3) =>
      exfalso
      rcases h1 with hc | (⟨hc, -⟩ | ⟨hc, -⟩) <;> omega
  · rintro (⟨rfl, rfl⟩ | ⟨⟨rfl, rfl⟩, hkm⟩ | ⟨⟨rfl, rfl⟩, hk0⟩)
    · refine ⟨by simp, Or.inl rfl, ?_⟩
      rcases Nat.eq_zero_or_pos j with rfl | hp
      · exact Or.inl rfl
      · exact Or.inr (Or.inl ⟨rfl, by omega⟩)
    · refine ⟨by simp, Or.inr (Or.inl ⟨rfl, hkm⟩), ?_⟩
      rcases Nat.eq_zero_or_pos j with rfl | hp
      · exact Or.inl rfl
      · exact Or.inr (Or.inr ⟨rfl, by omega⟩)
    · exact ⟨by simp, Or.inr (Or.inr ⟨rfl, hk0⟩), Or.inl rfl⟩

/-- The addable cells of `twoRow m k`, as an explicit finset. -/
def addableTwoRow (m k : ℕ) : Finset (ℕ × ℕ) :=
  {(0, m)} ∪ (if k < m then {((1 : ℕ), k)} else ∅) ∪ (if 0 < k then {((2 : ℕ), 0)} else ∅)

theorem mem_addableTwoRow (s : ℕ × ℕ) :
    s ∈ addableTwoRow m k ↔
      s = (0, m) ∨ (s = (1, k) ∧ k < m) ∨ (s = (2, 0) ∧ 0 < k) := by
  unfold addableTwoRow
  split_ifs <;> simp_all [Prod.ext_iff] <;> omega

theorem sum_addable_twoRow {M : Type*} [AddCommMonoid M] (h : k ≤ m) (f : ℕ × ℕ → M) :
    ∑ s : {s : ℕ × ℕ // IsAddableCell (twoRow m k h) s}, f s.1
      = ∑ s ∈ addableTwoRow m k, f s := by
  rw [← Finset.sum_coe_sort (addableTwoRow m k) f]
  exact Fintype.sum_equiv
    (Equiv.subtypeEquivRight (fun s => (isAddableCell_twoRow_iff h s).trans
      (mem_addableTwoRow s).symm)) _ _ (fun _ => rfl)

theorem sum_addableTwoRow_expand {M : Type*} [AddCommMonoid M] (f : ℕ × ℕ → M) :
    ∑ s ∈ addableTwoRow m k, f s
      = f (0, m) + (if k < m then f (1, k) else 0) + (if 0 < k then f (2, 0) else 0) := by
  unfold addableTwoRow
  split_ifs <;>
    simp [Finset.sum_insert, Finset.mem_insert, Prod.ext_iff] <;> abel

/-- The removable corners of a ≤2-row diagram. -/
theorem isCornerCell_twoRow_iff (h : k ≤ m) (r : ℕ × ℕ) :
    IsCornerCell (twoRow m k h) r ↔
      (r = (0, m - 1) ∧ k < m) ∨ (r = (1, k - 1) ∧ 0 < k) := by
  obtain ⟨i, j⟩ := r
  simp only [IsCornerCell, mem_twoRow h, Prod.mk.injEq]
  constructor
  · rintro ⟨hin, h1, h2⟩
    push_neg at h1 h2
    rcases hin with ⟨rfl, hj⟩ | ⟨rfl, hj⟩
    · left
      have hjk : k ≤ j := by simpa using h1
      have hjm : m ≤ j + 1 := by simpa using h2
      exact ⟨⟨rfl, by omega⟩, by omega⟩
    · right
      have hjk : k ≤ j + 1 := by simpa using h2
      exact ⟨⟨rfl, by omega⟩, by omega⟩
  · rintro (⟨⟨rfl, rfl⟩, hkm⟩ | ⟨⟨rfl, rfl⟩, hk0⟩)
    · refine ⟨Or.inl ⟨rfl, by omega⟩, ?_, ?_⟩ <;> (simp; try omega)
    · refine ⟨Or.inr ⟨rfl, by omega⟩, ?_, ?_⟩ <;> (simp; try omega)

theorem addCell_twoRow_row0 (h : k ≤ m) (hs : IsAddableCell (twoRow m k h) (0, m)) :
    addCell (twoRow m k h) (0, m) hs = twoRow (m + 1) k (by omega) := by
  ext c
  obtain ⟨i, j⟩ := c
  simp only [YoungDiagram.mem_cells, mem_addCell, mem_twoRow, Prod.mk.injEq]
  constructor
  · rintro (⟨rfl, rfl⟩ | (⟨rfl, hj⟩ | ⟨rfl, hj⟩))
    · exact Or.inl ⟨rfl, by omega⟩
    · exact Or.inl ⟨rfl, by omega⟩
    · exact Or.inr ⟨rfl, hj⟩
  · rintro (⟨rfl, hj⟩ | ⟨rfl, hj⟩)
    · rcases Nat.lt_or_ge j m with hlt | hge
      · exact Or.inr (Or.inl ⟨rfl, hlt⟩)
      · exact Or.inl ⟨rfl, by omega⟩
    · exact Or.inr (Or.inr ⟨rfl, hj⟩)

theorem addCell_twoRow_row1 (h : k ≤ m) (hkm : k < m)
    (hs : IsAddableCell (twoRow m k h) (1, k)) :
    addCell (twoRow m k h) (1, k) hs = twoRow m (k + 1) (by omega) := by
  ext c
  obtain ⟨i, j⟩ := c
  simp only [YoungDiagram.mem_cells, mem_addCell, mem_twoRow, Prod.mk.injEq]
  constructor
  · rintro (⟨rfl, rfl⟩ | (⟨rfl, hj⟩ | ⟨rfl, hj⟩))
    · exact Or.inr ⟨rfl, by omega⟩
    · exact Or.inl ⟨rfl, hj⟩
    · exact Or.inr ⟨rfl, by omega⟩
  · rintro (⟨rfl, hj⟩ | ⟨rfl, hj⟩)
    · exact Or.inr (Or.inl ⟨rfl, hj⟩)
    · rcases Nat.lt_or_ge j k with hlt | hge
      · exact Or.inr (Or.inr ⟨rfl, hlt⟩)
      · exact Or.inl ⟨rfl, by omega⟩

theorem rowLen_two_addCell_row2 (h : k ≤ m) (hs : IsAddableCell (twoRow m k h) (2, 0)) :
    0 < (addCell (twoRow m k h) (2, 0) hs).rowLen 2 := by
  rw [← YoungDiagram.mem_iff_lt_rowLen]
  exact (mem_addCell (2, 0) hs (2, 0)).mpr (Or.inl rfl)

end QOU.SchurWeyl
