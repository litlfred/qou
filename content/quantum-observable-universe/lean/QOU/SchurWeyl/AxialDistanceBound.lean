import QOU.SchurWeyl.TableauCells

/-!
# QOU.SchurWeyl.AxialDistanceBound — admissible swaps are at axial distance `≥ 2`

**A prerequisite of the irreducibility half of SW-5** (bean `qou-jfr8`), and the reason it is
needed is not obvious from the statement.

`axialDist_trichotomy` says *same row ⟹ `+1`* and *same column ⟹ `−1`*.  It does **not** say the
converse, and the converse is what the matrix-unit argument needs.  The off-diagonal entry of the
generator matrix is `offDiag`, and `offDiag q (-1) = 0` — a `@[simp]` lemma, not an edge case.  So
if an *admissible* swap could sit at distance `−1`, the entry the chain argument wants to promote
to a matrix unit would vanish, and `single_mem_range_of_entry_ne_zero` would have nothing to
consume.  (`genMat_ne_scalar` sidesteps this by reading the *partner* column, which it can afford
because it needs only one nonzero entry anywhere; a chain needs a *direction*, which is strictly
stronger.)

This file closes that: an admissible swap has `|axialDist| ≥ 2`, so the scalar distances `±1` are
exactly the row/column cases and nothing else.

## The proof is one squeeze, run four ways

If `k` and `k+1` sit at distance `±1` in different rows *and* different columns, then either

* they are ordered strictly up-left, so the entry order is reversed — `k + 1 < k`; or
* the rectangle they span has a corner cell that up-left closure puts in `μ`, and that cell's
  entry is squeezed strictly between `k` and `k+1`, of which there is none.

Which corner works depends only on the sign of the distance: `(i₂, j₁)` when `d = −1`, and
`(i₁, j₂)` when `d = +1`.  Everything else is arithmetic.

Pure tableau combinatorics: no `ℝ`, no `q`, nothing archimedean (§7c-clean).
-/

namespace QOU.SchurWeyl

namespace TableauCells

open QOU.Mathlib (StandardYoungTableau)

variable {μ : YoungDiagram}

/-- **Entries increase strictly along the up-left order.**  Weakly up-left and not equal gives a
strict inequality, by one row step and one column step. -/
theorem entry_lt_of_le_of_ne (T : StandardYoungTableau μ) {i₁ j₁ i₂ j₂ : ℕ}
    (hi : i₁ ≤ i₂) (hj : j₁ ≤ j₂) (hne : i₁ ≠ i₂ ∨ j₁ ≠ j₂) (hcell : (i₂, j₂) ∈ μ) :
    T.entry i₁ j₁ < T.entry i₂ j₂ := by
  have hmid : (i₁, j₂) ∈ μ := μ.up_left_mem hi (le_refl j₂) hcell
  rcases eq_or_lt_of_le hj with hje | hjl
  · subst hje
    have hil : i₁ < i₂ := by
      rcases hne with h | h
      · omega
      · exact absurd rfl h
    exact T.toSsyt.col_strict hil hcell
  · have h1 : T.entry i₁ j₁ < T.entry i₁ j₂ := T.row_strict hjl hmid
    rcases eq_or_lt_of_le hi with hie | hil
    · subst hie; exact h1
    · exact lt_trans h1 (T.toSsyt.col_strict hil hcell)

/-- **An admissible swap has axial distance at least `2` in absolute value.**

Equivalently: the scalar distances `±1` occur *exactly* in the same-row and same-column cases —
the converse of `axialDist_trichotomy`, which that theorem does not provide.

This is what keeps `offDiag` away from its zero: `offDiag q (-1) = 0`, so without this bound an
admissible swap could carry a vanishing off-diagonal entry. -/
theorem two_le_natAbs_axialDist (T : StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) (hk' : k + 1 ∈ Set.Icc 1 μ.cells.card)
    (hadm : SwapAdmissible T k) : 2 ≤ (axialDist T k).natAbs := by
  obtain ⟨hrow, hcol⟩ := hadm
  have hm₁ : cellOf T k ∈ μ.cells := cellOf_mem T hk
  have hm₂ : cellOf T (k + 1) ∈ μ.cells := cellOf_mem T hk'
  have hμ₁ : ((cellOf T k).1, (cellOf T k).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using hm₁
  have hμ₂ : ((cellOf T (k + 1)).1, (cellOf T (k + 1)).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using hm₂
  have he₁ : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hk
  have he₂ : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hk'
  have hne0 : axialDist T k ≠ 0 := axialDist_ne_zero T hk hk'
  have hd : axialDist T k
      = (((cellOf T (k + 1)).2 : ℤ) - ((cellOf T (k + 1)).1 : ℤ))
        - (((cellOf T k).2 : ℤ) - ((cellOf T k).1 : ℤ)) := by
    simp only [axialDist, axialDistance, cellContent]
  by_contra hcon
  -- the distance is `+1` or `-1`
  have hpm : axialDist T k = 1 ∨ axialDist T k = -1 := by omega
  -- the reversed-order contradiction, available whenever `k+1` sits weakly up-left of `k`
  have hrev : (cellOf T (k + 1)).1 ≤ (cellOf T k).1 → (cellOf T (k + 1)).2 ≤ (cellOf T k).2 →
      False := by
    intro ha hb
    have := entry_lt_of_le_of_ne T ha hb (Or.inl (Ne.symm hrow)) hμ₁
    omega
  rcases hpm with hp | hn
  · -- `d = +1`: the corner `(i₁, j₂)` is squeezed
    rcases lt_trichotomy (cellOf T k).1 (cellOf T (k + 1)).1 with hlt | heq | hgt
    · have hjlt : (cellOf T k).2 < (cellOf T (k + 1)).2 := by omega
      have hcorner : ((cellOf T k).1, (cellOf T (k + 1)).2) ∈ μ :=
        μ.up_left_mem (le_of_lt hlt) (le_refl _) hμ₂
      have h1 : T.entry (cellOf T k).1 (cellOf T k).2
          < T.entry (cellOf T k).1 (cellOf T (k + 1)).2 := T.row_strict hjlt hcorner
      have h2 : T.entry (cellOf T k).1 (cellOf T (k + 1)).2
          < T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 :=
        T.toSsyt.col_strict hlt hμ₂
      omega
    · exact hrow heq
    · exact hrev (by omega) (by omega)
  · -- `d = -1`: the corner `(i₂, j₁)` is squeezed
    rcases lt_trichotomy (cellOf T k).1 (cellOf T (k + 1)).1 with hlt | heq | hgt
    · have hjlt : (cellOf T k).2 < (cellOf T (k + 1)).2 := by omega
      have hcorner : ((cellOf T (k + 1)).1, (cellOf T k).2) ∈ μ :=
        μ.up_left_mem (le_refl _) (le_of_lt hjlt) hμ₂
      have h1 : T.entry (cellOf T k).1 (cellOf T k).2
          < T.entry (cellOf T (k + 1)).1 (cellOf T k).2 := T.toSsyt.col_strict hlt hcorner
      have h2 : T.entry (cellOf T (k + 1)).1 (cellOf T k).2
          < T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 := T.row_strict hjlt hμ₂
      omega
    · exact hrow heq
    · exact hrev (by omega) (by omega)

end TableauCells

end QOU.SchurWeyl
