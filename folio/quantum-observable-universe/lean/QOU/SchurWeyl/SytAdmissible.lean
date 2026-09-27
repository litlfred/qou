import QOU.SchurWeyl.TableauCells
import QOU.SchurWeyl.YoungTableaux

/-!
# A standard tableau admitting an adjacent swap, whenever the shape has two of them

`SeminormalRep.genMat_ne_scalar` shows the generator matrix `σ_k` is non-scalar as soon as **some**
tableau is `SwapAdmissible` at `k` — with no hypothesis on `q`.  What it does not supply, and what
`hoefsmit_seminormal_rep`'s non-degeneracy payload needs, is that a shape with `#SYT μ ≥ 2` has such
a tableau at all.  This file closes that step (bean SW-5, the second of the two gaps named in
`qou-im9l`).

## The argument, and why it is not the one the bean predicted

The bean's planned route was geometric: `#SYT μ ≥ 2` forces `μ` to have two rows and two columns,
then the *row-reading* tableau is admissible at `k = λ₁`, where the last cell of row `0` and the
first of row `1` differ in both coordinates.  That route needs (a) a proof that a single row or
single column has exactly one SYT, and (b) an explicit construction of a standard tableau — both
real work.

**Neither is needed.**  Run the contradiction on the *anti-diagonal* `i + j` instead:

* If `k` and `k+1` are **not** swap-admissible in `T`, they share a row or a column, and
  `sameRow_adjacent` / `sameCol_adjacent` (already in `TableauCells`) put them in *adjacent* cells.
  Either way the anti-diagonal goes up by exactly one (`antiDiag_cellOf_succ`).
* So if `T` is admissible nowhere, `antiDiag (cellOf T k) = k - 1` for every entry — an induction
  whose base case is `cellOf T 1 = (0,0)` (`cellOf_one`).
* That reads backwards as `T.entry i j = i + j + 1`: the filling is **determined by the shape**.
  Two tableaux admissible nowhere therefore agree on every cell, hence are equal.

So `#SYT μ ≥ 2` and "no tableau is ever admissible" are contradictory, which is exactly the claim.
The shape never has to be classified and no tableau is ever constructed.

**Scope.**  This gives one admissible pair somewhere.  It is *not* the connectivity of `SYT μ` under
admissible transpositions (the stronger, standard fact); nothing here needs it, and it is not
claimed.  Nor does it say where the admissible index is: for `μ = (2,1)` and `T = [[1,2],[3]]` the
witness is `k = 2` and `k = 1` fails, so the index genuinely depends on the tableau — which is why
the argument locates a tableau by contradiction rather than naming an index in advance.

Refs: no external result is used; `[ram1997]` and `[hoefsmit1974]` are cited at the consumer.
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)

namespace TableauCells

variable {μ : YoungDiagram}

/-- The anti-diagonal index `i + j` of a cell.  Constant on the diagonals of the Young diagram,
and the quantity the swap-free argument tracks. -/
def antiDiag (c : ℕ × ℕ) : ℕ := c.1 + c.2

@[simp] theorem antiDiag_mk (i j : ℕ) : antiDiag (i, j) = i + j := rfl

/-- **Two standard tableaux of the same shape that agree on every cell are equal.**  Off the shape
both are `0` by the semistandard `zeros` field, so cell-wise agreement is full agreement. -/
theorem syt_ext_on_cells {T₁ T₂ : StandardYoungTableau μ}
    (h : ∀ i j, (i, j) ∈ μ → T₁.entry i j = T₂.entry i j) : T₁ = T₂ := by
  have hall : ∀ i j, T₁.toSsyt.entry i j = T₂.toSsyt.entry i j := by
    intro i j
    by_cases hij : (i, j) ∈ μ
    · exact h i j hij
    · exact (T₁.toSsyt.zeros hij).trans (T₂.toSsyt.zeros hij).symm
  have hssyt : T₁.toSsyt = T₂.toSsyt := SemistandardYoungTableau.ext hall
  cases T₁; cases T₂; cases hssyt; rfl

/-- **An inadmissible step moves one along the anti-diagonal.**  Sharing a row puts `k+1` one column
to the right (`sameRow_adjacent`); sharing a column puts it one row down (`sameCol_adjacent`).  Both
raise `i + j` by exactly one, which is the whole content of the swap-free case. -/
theorem antiDiag_cellOf_succ (T : StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) (hk' : k + 1 ∈ Set.Icc 1 μ.cells.card)
    (h : ¬ SwapAdmissible T k) :
    antiDiag (cellOf T (k + 1)) = antiDiag (cellOf T k) + 1 := by
  have hm₁ : cellOf T k ∈ μ.cells := cellOf_mem T hk
  have hm₂ : cellOf T (k + 1) ∈ μ.cells := cellOf_mem T hk'
  have hμ₁ : ((cellOf T k).1, (cellOf T k).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using hm₁
  have hμ₂ : ((cellOf T (k + 1)).1, (cellOf T (k + 1)).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using hm₂
  have he₁ : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hk
  have he₂ : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hk'
  rw [SwapAdmissible] at h
  push_neg at h
  by_cases hrow : (cellOf T k).1 = (cellOf T (k + 1)).1
  · have hadj : (cellOf T (k + 1)).2 = (cellOf T k).2 + 1 :=
      sameRow_adjacent T hμ₁ (by rw [← hrow] at hμ₂; exact hμ₂) he₁
        (by rw [← hrow] at he₂; exact he₂)
    simp only [antiDiag, ← hrow, hadj]
    omega
  · have hcol : (cellOf T k).2 = (cellOf T (k + 1)).2 := h hrow
    have hadj : (cellOf T (k + 1)).1 = (cellOf T k).1 + 1 :=
      sameCol_adjacent T hμ₁ (by rw [← hcol] at hμ₂; exact hμ₂) he₁
        (by rw [← hcol] at he₂; exact he₂)
    simp only [antiDiag, ← hcol, hadj]
    omega

/-- The corner entry is minimal: `T.entry 0 0 ≤ T.entry i j` for every cell.  Weak rows take
`(0,0)` to `(0,j)`, strict columns take `(0,j)` to `(i,j)`. -/
theorem entry_corner_le (T : StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∈ μ) :
    T.entry 0 0 ≤ T.entry i j := by
  have h0j : ((0 : ℕ), j) ∈ μ := μ.up_left_mem (Nat.zero_le i) (le_refl j) h
  have h1 : T.entry 0 0 ≤ T.entry 0 j := by
    rcases Nat.eq_zero_or_pos j with hj | hj
    · subst hj; exact le_refl _
    · exact T.toSsyt.row_weak hj h0j
  have h2 : T.entry 0 j ≤ T.entry i j := by
    rcases Nat.eq_zero_or_pos i with hi | hi
    · subst hi; exact le_refl _
    · exact le_of_lt (T.toSsyt.col_strict hi h)
  omega

/-- **Entry `1` sits in the corner.**  The base case of the anti-diagonal induction. -/
theorem cellOf_one (T : StandardYoungTableau μ) (hne : 0 < μ.cells.card) :
    cellOf T 1 = (0, 0) := by
  have h1 : (1 : ℕ) ∈ Set.Icc 1 μ.cells.card := ⟨le_refl 1, hne⟩
  have hmem : cellOf T 1 ∈ μ.cells := cellOf_mem T h1
  have hent : T.entry (cellOf T 1).1 (cellOf T 1).2 = 1 := entry_cellOf T h1
  have hμ : ((cellOf T 1).1, (cellOf T 1).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using hmem
  have h00 : ((0 : ℕ), (0 : ℕ)) ∈ μ := μ.up_left_mem (Nat.zero_le _) (Nat.zero_le _) hμ
  have hc00 : ((0, 0) : ℕ × ℕ) ∈ μ.cells := (YoungDiagram.mem_cells _).mpr h00
  have hle : T.entry 0 0 ≤ 1 := by
    have := entry_corner_le T hμ
    omega
  have hge : 1 ≤ T.entry 0 0 := (T.mapsTo_cells (by simpa using hc00)).1
  have heq : T.entry ((0, 0) : ℕ × ℕ).1 ((0, 0) : ℕ × ℕ).2 = 1 := by
    simpa using le_antisymm hle hge
  exact cellOf_unique T hc00 heq

/-- **A tableau admissible nowhere puts entry `k` on anti-diagonal `k - 1`.** -/
theorem antiDiag_cellOf_eq (T : StandardYoungTableau μ)
    (hno : ∀ k, 1 ≤ k → k + 1 ≤ μ.cells.card → ¬ SwapAdmissible T k) :
    ∀ k, 1 ≤ k → k ≤ μ.cells.card → antiDiag (cellOf T k) + 1 = k := by
  intro k
  induction k with
  | zero => intro h; omega
  | succ m ih =>
    intro _ hle
    rcases Nat.eq_zero_or_pos m with hm | hm
    · subst hm
      rw [cellOf_one T (by omega)]
      simp [antiDiag]
    · have hstep : antiDiag (cellOf T (m + 1)) = antiDiag (cellOf T m) + 1 :=
        antiDiag_cellOf_succ T ⟨hm, by omega⟩ ⟨by omega, hle⟩ (hno m hm (by omega))
      have hprev := ih hm (by omega)
      omega

/-- **The filling of a nowhere-admissible tableau is forced by the shape.** -/
theorem entry_eq_of_no_admissible (T : StandardYoungTableau μ)
    (hno : ∀ k, 1 ≤ k → k + 1 ≤ μ.cells.card → ¬ SwapAdmissible T k)
    {i j : ℕ} (hij : (i, j) ∈ μ) : T.entry i j = i + j + 1 := by
  have hc : ((i, j) : ℕ × ℕ) ∈ μ.cells := (YoungDiagram.mem_cells _).mpr hij
  have hrange : T.entry i j ∈ Set.Icc 1 μ.cells.card := T.mapsTo_cells (by simpa using hc)
  have hcell : cellOf T (T.entry i j) = (i, j) := cellOf_unique T hc rfl
  have hkey := antiDiag_cellOf_eq T hno (T.entry i j) hrange.1 hrange.2
  rw [hcell] at hkey
  simp only [antiDiag_mk] at hkey
  omega

/-- **The gap this file exists to close (bean SW-5).**  A shape with more than one standard tableau
has a tableau admitting an adjacent swap.

Feeding this to `SeminormalRep.genMat_ne_scalar` gives the non-degeneracy payload of
`hoefsmit_seminormal_rep`: some generator is sent to a non-scalar matrix once `dLambda ≥ 2`. -/
theorem exists_swapAdmissible_of_one_lt_card
    (h2 : 1 < Fintype.card (StandardYoungTableau μ)) :
    ∃ (T : StandardYoungTableau μ) (k : ℕ),
      1 ≤ k ∧ k + 1 ≤ μ.cells.card ∧ SwapAdmissible T k := by
  by_contra hcon
  push_neg at hcon
  obtain ⟨T, T', hne⟩ := Fintype.exists_pair_of_one_lt_card h2
  exact hne (syt_ext_on_cells fun i j hij => by
    rw [entry_eq_of_no_admissible T (fun k hk hk' => hcon T k hk hk') hij,
        entry_eq_of_no_admissible T' (fun k hk hk' => hcon T' k hk hk') hij])

end TableauCells

end QOU.SchurWeyl
