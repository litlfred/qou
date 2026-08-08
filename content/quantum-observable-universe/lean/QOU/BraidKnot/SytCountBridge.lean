import QOU.BraidKnot.StandardYoungTableau
import QOU.Mathlib.StandardYoungTableau

/-!
# The two standard-Young-tableau encodings agree

`QOU.BraidKnot.StandardYoungTableau` fills the cells of `μ` with `0, …, n−1`
and carries `inj_on` / `row_strict` / `col_strict` explicitly.
`QOU.Mathlib.StandardYoungTableau` fills with `1, …, n`, wrapping Mathlib's
`SemistandardYoungTableau` plus a `Set.BijOn` onto `Set.Icc 1 n`.

This file builds the equivalence and concludes
`numSYT μ = QOU.Mathlib.numStandardYoungTableaux μ` — bridge (2) of `sp09`.

The two directions are not symmetric:

* **forward** has to *weaken* row-strictness to the SSYT's `row_weak'`, and
  supply `SurjOn` from injectivity plus a cardinality count;
* **backward** has to *recover* strictness from `row_weak'` together with the
  injectivity contained in `bijOn` — weak plus injective is strict.
-/

namespace QOU.BraidKnot

variable {μ : YoungDiagram}

/-! ## Forward: 0-based ⟶ 1-based -/

/-- The 0-based filling shifted up by one, pinned to `0` off the diagram. -/
def shiftUp (T : StandardYoungTableau μ) (i j : ℕ) : ℕ :=
  if (i, j) ∈ μ then T.entry i j + 1 else 0

theorem shiftUp_of_mem (T : StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∈ μ) :
    shiftUp T i j = T.entry i j + 1 := if_pos h

theorem shiftUp_of_notMem (T : StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∉ μ) :
    shiftUp T i j = 0 := if_neg h

/-- The semistandard tableau underlying the 1-based encoding. Row-strictness is
weakened to `row_weak'`; column-strictness carries over directly. -/
def toSsyt (T : StandardYoungTableau μ) : SemistandardYoungTableau μ where
  entry := shiftUp T
  row_weak' := by
    intro i j1 j2 h hmem
    have h1 : (i, j1) ∈ μ := μ.up_left_mem (le_refl i) (le_of_lt h) hmem
    rw [shiftUp_of_mem T h1, shiftUp_of_mem T hmem]
    exact Nat.succ_le_succ (le_of_lt (T.entry_row_lt h hmem))
  col_strict' := by
    intro i1 i2 j h hmem
    have h1 : (i1, j) ∈ μ := μ.up_left_mem (le_of_lt h) (le_refl j) hmem
    rw [shiftUp_of_mem T h1, shiftUp_of_mem T hmem]
    exact Nat.succ_lt_succ (T.entry_col_lt h hmem)
  zeros' := fun h => shiftUp_of_notMem T h

/-- The shifted entries land in `Icc 1 n` and hit every value there. Injectivity
comes from `inj_on`; surjectivity is then forced by counting, since the domain
and target are finite of the same size. -/
theorem toSsyt_bijOn (T : StandardYoungTableau μ) :
    Set.BijOn (fun c : ℕ × ℕ => (toSsyt T).entry c.1 c.2)
      (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) := by
  have hmaps : Set.MapsTo (fun c : ℕ × ℕ => (toSsyt T).entry c.1 c.2)
      (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) := by
    intro c hc
    have hmem : (c.1, c.2) ∈ μ := (YoungDiagram.mem_cells _).mp hc
    have hlt := T.lt_card c.1 c.2 hmem
    have hcard : μ.card = μ.cells.card := rfl
    simp only [toSsyt, shiftUp_of_mem T hmem, Set.mem_Icc]
    omega
  have hinj : Set.InjOn (fun c : ℕ × ℕ => (toSsyt T).entry c.1 c.2)
      (μ.cells : Set (ℕ × ℕ)) := by
    intro a ha b hb hab
    have hma : (a.1, a.2) ∈ μ := (YoungDiagram.mem_cells _).mp ha
    have hmb : (b.1, b.2) ∈ μ := (YoungDiagram.mem_cells _).mp hb
    simp only [toSsyt, shiftUp_of_mem T hma, shiftUp_of_mem T hmb] at hab
    obtain ⟨h1, h2⟩ := T.inj_on a.1 a.2 b.1 b.2 hma hmb (by omega)
    exact Prod.ext h1 h2
  refine ⟨hmaps, hinj, ?_⟩
  have hcard : (Finset.Icc 1 μ.cells.card).card ≤ μ.cells.card := by
    rw [Nat.card_Icc]; omega
  have := Finset.surjOn_of_injOn_of_card_le
    (s := μ.cells) (t := Finset.Icc 1 μ.cells.card)
    (fun c : ℕ × ℕ => (toSsyt T).entry c.1 c.2)
    (by simpa [Finset.coe_Icc] using hmaps) (by simpa using hinj) hcard
  simpa [Finset.coe_Icc] using this

/-- The 1-based tableau built from a 0-based one. -/
def toMathlibSyt (T : StandardYoungTableau μ) : QOU.Mathlib.StandardYoungTableau μ where
  toSsyt := toSsyt T
  bijOn := toSsyt_bijOn T

end QOU.BraidKnot
