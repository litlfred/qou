import QOU.BraidKnot.StandardTableauSpectral

/-!
# Axial distance: the first real prerequisite of the seminormal form

The seminormal representation of `H_n(q)` writes the action of `σᵢ` on the basis vector `v_T` with
coefficients built from the **axial distance** between the cells holding `i` and `i+1` — and those
coefficients have the axial distance in a *denominator*.  So the representation does not even make
sense until one knows the distance is never zero, i.e. that consecutive entries of a standard
tableau never sit on the same diagonal.

This file proves the sharp combinatorial fact that kills the diagonal case.

## The diagonal gap

`StandardTableau.diag_gap` : if `(r,c)` and `(r+1,c+1)` are both cells, the entry at the second is
at least **two** more than the entry at the first.

The proof is short but the "two" is the whole point.  A one-step chain would only give `<`, which is
useless — consecutive entries would still be allowed on a diagonal.  The gain of two comes from the
**intermediate cell** `(r,c+1)`, which is a cell whenever `(r+1,c+1)` is (rows are weakly
decreasing, so row `r` is at least as long as row `r+1`).  Its entry is strictly between the two, so
the outer two cannot be consecutive.

## Consequence

`StandardTableau.not_consecutive_diag` : entries `i` and `i+1` are never at `(r,c)` and `(r+1,c+1)`.
That is the `d = 1` case of "consecutive entries are never on the same diagonal", and it is the case
the seminormal denominators actually hit.

## Honest scope

This is a **prerequisite**, not the representation.  The general `d ≥ 2` diagonal case, the
seminormal action of `σᵢ` itself, and the eigenvalue `q^{2·content}` for `Lᵢ` are all still absent.
`JucysMurphySpectrum` is untouched and the general-`λ` twist stays conditional.

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.1.
- [wenzl1988] Hecke algebra representations (seminormal form).
-/

namespace QOU.BraidKnot.Keystone

open QOU.MathlibExt.QPartitionCombinatorics

/-- **A Young diagram is closed leftward within a row.** -/
theorem mem_cells_of_le_col {l : Partition} {r c c' : ℕ}
    (h : (r, c) ∈ cells l) (hc : c' ≤ c) : (r, c') ∈ cells l := by
  rw [mem_cells] at h ⊢
  obtain ⟨h1, h2⟩ := h
  have h1' : r < l.length := h1
  have h2' : c < l.getD r 0 := h2
  exact ⟨h1', show c' < l.getD r 0 by omega⟩

namespace StandardTableau

variable {l : Partition} {n : ℕ}

/-- The entry occupying a given cell. -/
def entryAt (T : StandardTableau l n) {p : ℕ × ℕ} (hp : p ∈ cells l) : Fin n :=
  T.toEquiv.symm ⟨p, hp⟩

@[simp] theorem toEquiv_entryAt (T : StandardTableau l n) {p : ℕ × ℕ} (hp : p ∈ cells l) :
    ((T.toEquiv (T.entryAt hp)) : ℕ × ℕ) = p := by
  unfold entryAt; rw [Equiv.apply_symm_apply]

/-- **A diagonal step gains at least two.**

If `(r,c)` and `(r+1,c+1)` are both cells then the intermediate cell `(r,c+1)` exists — row `r` is
at least as long as row `r+1` — and its entry is strictly between the other two, by `row_incr` then
`col_incr`.  Hence the outer entries differ by `≥ 2`.

The strength of "two" rather than "one" is what makes this usable: it is exactly what forbids
consecutive entries on a diagonal, and hence what makes the seminormal denominators nonzero. -/
theorem diag_gap (hl : l.Sorted (· ≥ ·)) (T : StandardTableau l n) {r c : ℕ}
    (h : (r, c) ∈ cells l) (h' : (r + 1, c + 1) ∈ cells l) :
    ((T.entryAt h : Fin n) : ℕ) + 1 < ((T.entryAt h' : Fin n) : ℕ) := by
  -- the intermediate cell (r, c+1)
  have hmid : (r, c + 1) ∈ cells l := by
    have hup : (r + 1 - 1, c + 1) ∈ cells l := mem_cells_pred_row hl h' (by omega)
    simpa using hup
  -- entry(r,c) < entry(r,c+1) : same row, column increases
  have h1 : T.entryAt h < T.entryAt hmid := by
    refine T.row_incr _ _ ?_ ?_
    · rw [toEquiv_entryAt, toEquiv_entryAt]
    · rw [toEquiv_entryAt, toEquiv_entryAt]; dsimp only; omega
  -- entry(r,c+1) < entry(r+1,c+1) : same column, row increases
  have h2 : T.entryAt hmid < T.entryAt h' := by
    refine T.col_incr _ _ ?_ ?_
    · rw [toEquiv_entryAt, toEquiv_entryAt]
    · rw [toEquiv_entryAt, toEquiv_entryAt]; dsimp only; omega
  have := Fin.lt_def.mp h1
  have := Fin.lt_def.mp h2
  omega

/-- **Consecutive entries are never on a diagonal step.**  The `d = 1` case of "consecutive entries
never share a content", and the one the seminormal denominators hit. -/
theorem not_consecutive_diag (hl : l.Sorted (· ≥ ·)) (T : StandardTableau l n) {r c : ℕ}
    (h : (r, c) ∈ cells l) (h' : (r + 1, c + 1) ∈ cells l) :
    ((T.entryAt h' : Fin n) : ℕ) ≠ ((T.entryAt h : Fin n) : ℕ) + 1 := by
  have := diag_gap hl T h h'
  omega

/-- The two cells of a diagonal step have **equal content** — so `diag_gap` is exactly the statement
that a zero axial distance cannot occur between consecutive entries. -/
theorem cellContent_diag_step (r c : ℕ) :
    cellContent (r + 1) (c + 1) = cellContent r c := by
  unfold cellContent; push_cast; ring

end StandardTableau

end QOU.BraidKnot.Keystone
