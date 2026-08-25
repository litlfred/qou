import QOU.BraidKnot.HeckeJucysMurphyReduction
import Mathlib.Data.List.GetD

/-!
# Standard Young tableaux, and the base case of the JM spectrum

This is the **start of the spectral half** — the half of `JucysMurphySpectrum` that says `Lᵢ` acts
on the seminormal basis with eigenvalue `q^{2·content}`.  It is the larger half and is **not**
closed here; what this file does is make its indexing objects real.

## Why a bijection is not enough

`KeystoneJucysMurphyTwist.lean` models a tableau as a bijection `Fin n ≃ cells λ`.  That is exactly
right for `sum_content_of_equiv` — the content sum reindexes along *any* bijection — but it is
**too weak for the spectral statement**, which holds for *standard* tableaux only.  The seminormal
representation is built on the standard ones; an arbitrary filling indexes nothing.

So this file defines `StandardTableau`, carrying the increasing conditions, and records that the
weaker results still apply to it (`StandardTableau.sum_content`).

## The base case is forced, and proved

`Lᵢ`'s spectral rule must give eigenvalue `q^{2·content}` of the cell holding entry `i`.  At `i = 0`
the JM recursion gives `L₁ = 1`, so the rule is only consistent if entry `0` sits at a cell of
content `0`.  `StandardTableau.zero_at_corner` proves it sits at `(0,0)` exactly — hence content
`0 − 0 = 0` and `q⁰ = 1`.

That is a genuine consistency check on the assumed spectral rule, discharged rather than assumed:
the rule's base case is **forced** by standardness plus the partition shape, not chosen to fit.

## What remains

Everything else.  The seminormal representation, the diagonal action of `Lᵢ`, and the eigenvalue at
general `i` are all still absent, and remain the content of `JucysMurphySpectrum`.  Nothing here
discharges it; this narrows what a future proof has to construct, and pins one endpoint.

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.1 (partitions, contents).
- [wenzl1988] Hecke algebra representations (seminormal form).
-/

namespace QOU.BraidKnot.Keystone

open QOU.MathlibExt.QPartitionCombinatorics

/-! ## Young diagrams are closed upward in a column -/

/-- **A Young diagram is closed upward within a column.**  If `(r, c)` is a cell and `r > 0`, then
`(r−1, c)` is a cell too — because the partition's rows are weakly decreasing, so row `r−1` is at
least as long as row `r`. -/
theorem mem_cells_pred_row {l : Partition} (hl : l.Sorted (· ≥ ·)) {r c : ℕ}
    (h : (r, c) ∈ cells l) (hr : 0 < r) : (r - 1, c) ∈ cells l := by
  rw [mem_cells] at h ⊢
  obtain ⟨hrow, hcol⟩ := h
  dsimp only at hrow hcol ⊢
  have hr1 : r - 1 < l.length := by omega
  have hmono : l.getD r 0 ≤ l.getD (r - 1) 0 := by
    rw [List.getD_eq_getElem l 0 hrow, List.getD_eq_getElem l 0 hr1]
    exact List.pairwise_iff_getElem.mp hl (r - 1) r hr1 hrow (by omega)
  exact ⟨by omega, by omega⟩

/-! ## Standard Young tableaux -/

/-- **A standard Young tableau** of shape `λ` with `n` entries: a bijection from entries to cells
whose inverse is increasing along rows and down columns.

The conditions are stated in the direction that is convenient to *use*: if two entries share a row
(resp. column) and the first is further right (resp. down), then it is the larger entry. -/
structure StandardTableau (l : Partition) (n : ℕ) where
  /-- The underlying entries-to-cells bijection. -/
  toEquiv : Fin n ≃ {c // c ∈ cells l}
  /-- Entries increase along a row. -/
  row_incr : ∀ i j : Fin n, ((toEquiv i) : ℕ × ℕ).1 = ((toEquiv j) : ℕ × ℕ).1 →
    ((toEquiv i) : ℕ × ℕ).2 < ((toEquiv j) : ℕ × ℕ).2 → i < j
  /-- Entries increase down a column. -/
  col_incr : ∀ i j : Fin n, ((toEquiv i) : ℕ × ℕ).2 = ((toEquiv j) : ℕ × ℕ).2 →
    ((toEquiv i) : ℕ × ℕ).1 < ((toEquiv j) : ℕ × ℕ).1 → i < j

namespace StandardTableau

variable {l : Partition} {n : ℕ}

/-- The weaker bijection results still apply: the content of a standard tableau's entries sums to
`c(λ)`, by `sum_content_of_equiv`. -/
theorem sum_content (T : StandardTableau l n) :
    ∑ i : Fin n, cellContent ((T.toEquiv i) : ℕ × ℕ).1 ((T.toEquiv i) : ℕ × ℕ).2 = contentSum l :=
  sum_content_of_equiv T.toEquiv

/-- **Entry `0` sits in the first row.**  If it were in row `r > 0`, the cell directly above it
would also be a cell (`mem_cells_pred_row`), its entry would share the column and sit in a strictly
smaller row, and `col_incr` would make that entry `< 0` — impossible. -/
theorem zero_row (hl : l.Sorted (· ≥ ·)) (T : StandardTableau l n) (h0 : 0 < n) :
    ((T.toEquiv ⟨0, h0⟩) : ℕ × ℕ).1 = 0 := by
  by_contra hne
  set z : Fin n := ⟨0, h0⟩ with hz
  set p : ℕ × ℕ := ((T.toEquiv z) : ℕ × ℕ) with hp
  have hr : 0 < p.1 := Nat.pos_of_ne_zero hne
  have hmem : p ∈ cells l := (T.toEquiv z).2
  have hup : (p.1 - 1, p.2) ∈ cells l := mem_cells_pred_row hl (by simpa using hmem) hr
  -- the entry occupying the cell above
  set w : Fin n := T.toEquiv.symm ⟨(p.1 - 1, p.2), hup⟩ with hw
  have hwval : ((T.toEquiv w) : ℕ × ℕ) = (p.1 - 1, p.2) := by
    rw [hw, Equiv.apply_symm_apply]
  have hcol : ((T.toEquiv w) : ℕ × ℕ).2 = ((T.toEquiv z) : ℕ × ℕ).2 := by
    rw [hwval, ← hp]
  have hrow : ((T.toEquiv w) : ℕ × ℕ).1 < ((T.toEquiv z) : ℕ × ℕ).1 := by
    rw [hwval, ← hp]; simp; omega
  have hlt := T.col_incr w z hcol hrow
  rw [Fin.lt_def, hz] at hlt
  exact Nat.not_lt_zero _ hlt

/-- **Entry `0` sits at the corner `(0,0)`** — hence its content is `0`, and the JM base case
`L₁ = 1 = q^{2·0}` is *forced* by standardness rather than chosen. -/
theorem zero_at_corner (hl : l.Sorted (· ≥ ·)) (T : StandardTableau l n) (h0 : 0 < n) :
    ((T.toEquiv ⟨0, h0⟩) : ℕ × ℕ) = (0, 0) := by
  set z : Fin n := ⟨0, h0⟩ with hz
  have hrow : ((T.toEquiv z) : ℕ × ℕ).1 = 0 := zero_row hl T h0
  have hcol : ((T.toEquiv z) : ℕ × ℕ).2 = 0 := by
    by_contra hne
    have hpos : 0 < ((T.toEquiv z) : ℕ × ℕ).2 := Nat.pos_of_ne_zero hne
    have hmem : ((T.toEquiv z) : ℕ × ℕ) ∈ cells l := (T.toEquiv z).2
    rw [mem_cells] at hmem
    obtain ⟨hm1, hm2⟩ := hmem
    have hleft : (((T.toEquiv z) : ℕ × ℕ).1, ((T.toEquiv z) : ℕ × ℕ).2 - 1) ∈ cells l := by
      rw [mem_cells]; dsimp only; exact ⟨hm1, by omega⟩
    set w : Fin n := T.toEquiv.symm ⟨_, hleft⟩ with hw
    have hwval : ((T.toEquiv w) : ℕ × ℕ)
        = (((T.toEquiv z) : ℕ × ℕ).1, ((T.toEquiv z) : ℕ × ℕ).2 - 1) := by
      rw [hw, Equiv.apply_symm_apply]
    have hr : ((T.toEquiv w) : ℕ × ℕ).1 = ((T.toEquiv z) : ℕ × ℕ).1 := by rw [hwval]
    have hc : ((T.toEquiv w) : ℕ × ℕ).2 < ((T.toEquiv z) : ℕ × ℕ).2 := by
      rw [hwval]; dsimp only; omega
    have hlt := T.row_incr w z hr hc
    rw [Fin.lt_def, hz] at hlt
    exact Nat.not_lt_zero _ hlt
  have : ((T.toEquiv z) : ℕ × ℕ) = (((T.toEquiv z) : ℕ × ℕ).1, ((T.toEquiv z) : ℕ × ℕ).2) := rfl
  rw [this, hrow, hcol]

/-- **The spectral rule's base case is consistent.**  Entry `0` has content `0`, so the rule
`eigenvalue of L₁ = q^{2·content}` gives `q⁰ = 1` — matching `jmRaw_zero : L₁ = 1` exactly. -/
theorem zero_content (hl : l.Sorted (· ≥ ·)) (T : StandardTableau l n) (h0 : 0 < n) :
    cellContent ((T.toEquiv ⟨0, h0⟩) : ℕ × ℕ).1 ((T.toEquiv ⟨0, h0⟩) : ℕ × ℕ).2 = 0 := by
  rw [zero_at_corner hl T h0]
  simp [cellContent]

end StandardTableau

end QOU.BraidKnot.Keystone
