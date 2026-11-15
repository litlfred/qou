import QOU.MathlibExt.WenzlSchurElement

/-!
# TL content stratification — the combinatorial characterisation (bean `qou-lcgj`)

`WenzlSchurElement.schurElement_tl_eq_zero_iff` (already on `main`) reduces
Schur-element vanishing at the physical Markov parameter `X = Q^{-N}` to the
*existential* predicate `HasContentCell lam N`.  That is not yet a
combinatorial description: it still quantifies over cells.

This file eliminates the quantifier.  For a genuine partition (weakly
decreasing, positive parts) the content-`N` hyperplane meets the diagram in a
condition on a **single** shape statistic:

* `N ≥ 0` : `HasContentCell lam N ↔ N < lam₁`   (more than `N` **columns**)
* `N < 0` : `HasContentCell lam N ↔ -N < ℓ(lam)` (more than `-N` **rows**)

Hence at `X = Q^{-N}`, `N ≥ 0`, the surviving Wedderburn blocks are exactly the
partitions with **at most `N` columns**.

Conventions are fixed by `WenzlSchurElement`: rows/columns are `0`-indexed and
`cellContent i j = j - i`.  Note the resulting statement is the **conjugate** of
the textbook `GL(N)`/HOMFLY one ("at most `N` rows"), which corresponds to the
other sign convention `X = Q^{+N}`; see the report for the discussion.

Base ring: `ℝ` only in the Schur-element corollaries, which inherit it from
`schurElement` (§7c).  The combinatorial characterisation itself is ring-free.
-/

namespace QOU.MathlibExt.WenzlSchurElement

open QOU.MathlibExt.QPartitionCombinatorics

/-- The number of **columns** of `lam`, i.e. its first (largest) part.
    `0` on the empty partition. -/
def numCols (lam : Partition) : ℕ := (lam[0]?).getD 0

private theorem getD_eq_getElem {lam : Partition} {i : ℕ} (hi : i < lam.length) :
    (lam[i]?).getD 0 = lam[i] := by
  rw [List.getElem?_eq_getElem hi]; rfl

/-- For a weakly decreasing partition every row is bounded by the first. -/
theorem row_le_numCols {lam : Partition} (hs : lam.Sorted (· ≥ ·))
    {i : ℕ} (hi : i < lam.length) : (lam[i]?).getD 0 ≤ numCols lam := by
  have h0 : 0 < lam.length := Nat.lt_of_le_of_lt (Nat.zero_le i) hi
  rw [getD_eq_getElem hi, numCols, getD_eq_getElem h0]
  rcases Nat.eq_zero_or_pos i with h | h
  · subst h; exact Nat.le_refl _
  · exact List.pairwise_iff_getElem.mp hs 0 i h0 hi h

/-! ## The characterisation, `N ≥ 0`: a column condition -/

/-- **Easy direction (no hypothesis on `lam`).**  If `lam` has more than `N`
    columns then cell `(0, N)` realises content `N`. -/
theorem hasContentCell_of_lt_numCols {lam : Partition} {N : ℤ} (hN : 0 ≤ N)
    (h : N < (numCols lam : ℤ)) : HasContentCell lam N := by
  simp only [numCols] at h
  have hcast : (N.toNat : ℤ) = N := Int.toNat_of_nonneg hN
  have hlen : 0 < lam.length := by
    cases lam with
    | nil => simp at h; omega
    | cons a t => exact Nat.succ_pos _
  refine ⟨0, hlen, N.toNat, by omega, ?_⟩
  · unfold cellContent; omega

/-- **Hard direction (needs weak decrease; holds for every `N`).**  A
    content-`N` cell forces more than `N` columns: the cell sits in some row
    `i` at column `j = N + i ≥ N`, and that row is bounded by the first.  Note
    no sign hypothesis on `N` is needed here — it is only the *converse* that
    requires `0 ≤ N`. -/
theorem lt_numCols_of_hasContentCell {lam : Partition} {N : ℤ}
    (hs : lam.Sorted (· ≥ ·)) (h : HasContentCell lam N) :
    N < (numCols lam : ℤ) := by
  obtain ⟨i, hi, j, hj, hc⟩ := h
  have hrow : (lam[i]?).getD 0 ≤ numCols lam := row_le_numCols hs hi
  unfold cellContent at hc
  simp only [numCols] at hrow ⊢
  omega

/-- **The `N ≥ 0` stratification (column form).** -/
theorem hasContentCell_iff_lt_numCols {lam : Partition} {N : ℤ}
    (hs : lam.Sorted (· ≥ ·)) (hN : 0 ≤ N) :
    HasContentCell lam N ↔ N < (numCols lam : ℤ) :=
  ⟨fun h => lt_numCols_of_hasContentCell hs h, hasContentCell_of_lt_numCols hN⟩

/-! ## The characterisation, `N < 0`: a row condition -/

/-- **Easy direction (no hypothesis on `lam` or `N`).**  A content-`N` cell
    sits in row `i = j - N ≥ -N`, so `lam` has more than `-N` rows. -/
theorem lt_length_of_hasContentCell {lam : Partition} {N : ℤ}
    (h : HasContentCell lam N) : -N < (lam.length : ℤ) := by
  obtain ⟨i, hi, j, hj, hc⟩ := h
  unfold cellContent at hc
  omega

/-- **Hard direction (needs positive parts).**  With more than `-N` rows, the
    cell `(-N, 0)` exists — its row is nonempty because parts are positive —
    and has content `N`. -/
theorem hasContentCell_of_lt_length {lam : Partition} {N : ℤ} (hN : N < 0)
    (hpos : ∀ x ∈ lam, 0 < x) (h : -N < (lam.length : ℤ)) :
    HasContentCell lam N := by
  have hM : ((-N).toNat : ℤ) = -N := Int.toNat_of_nonneg (by omega)
  have hi : (-N).toNat < lam.length := by omega
  refine ⟨(-N).toNat, hi, 0, ?_, ?_⟩
  · rw [getD_eq_getElem hi]
    exact hpos _ (List.getElem_mem hi)
  · unfold cellContent; omega

/-- **The `N < 0` stratification (row form).** -/
theorem hasContentCell_iff_lt_length {lam : Partition} {N : ℤ} (hN : N < 0)
    (hpos : ∀ x ∈ lam, 0 < x) :
    HasContentCell lam N ↔ -N < (lam.length : ℤ) :=
  ⟨fun h => lt_length_of_hasContentCell h, hasContentCell_of_lt_length hN hpos⟩

/-! ## Corollary: the two conditions are jointly necessary

Combining the two forward directions, a content-`N` cell forces **both** more
than `N` columns and more than `-N` rows — the diagram must reach the
content-`N` anti-diagonal from both sides.  This is the "hook" form of the
stratification and needs no sign hypothesis at all. -/

/-- A content-`N` cell forces both bounds simultaneously. -/
theorem numCols_and_length_of_hasContentCell {lam : Partition} {N : ℤ}
    (hs : lam.Sorted (· ≥ ·)) (h : HasContentCell lam N) :
    N < (numCols lam : ℤ) ∧ -N < (lam.length : ℤ) :=
  ⟨lt_numCols_of_hasContentCell hs h, lt_length_of_hasContentCell h⟩

/-! ## Consequences for the Schur element at `X = Q^{-N}` -/

/-- **The Temperley–Lieb quotient, explicitly (`N ≥ 0`).**  At the physical
    Markov parameter `X = Q^{-N}` with `Q > 1`, the Schur element of a
    partition `lam` **survives iff `lam` has at most `N` columns**.  Combined
    with the cited `SchurElementCriterion`, the surviving Wedderburn blocks of
    `H_n(Q)` at `X = Q^{-N}` are exactly `{lam ⊢ n : lam₁ ≤ N}`. -/
theorem schurElement_tl_ne_zero_iff_numCols_le {Q : ℝ} (hQ : 1 < Q) {N : ℤ}
    (hN : 0 ≤ N) {lam : Partition} (hs : lam.Sorted (· ≥ ·)) :
    schurElement Q (Q ^ (-N)) lam ≠ 0 ↔ (numCols lam : ℤ) ≤ N := by
  rw [Ne, schurElement_tl_eq_zero_iff hQ, hasContentCell_iff_lt_numCols hs hN]
  omega

/-- **Dropped blocks (`N ≥ 0`).**  The blocks removed at `X = Q^{-N}` are
    exactly those with strictly more than `N` columns. -/
theorem schurElement_tl_eq_zero_iff_numCols_gt {Q : ℝ} (hQ : 1 < Q) {N : ℤ}
    (hN : 0 ≤ N) {lam : Partition} (hs : lam.Sorted (· ≥ ·)) :
    schurElement Q (Q ^ (-N)) lam = 0 ↔ N < (numCols lam : ℤ) := by
  rw [schurElement_tl_eq_zero_iff hQ, hasContentCell_iff_lt_numCols hs hN]

/-- **The `N < 0` mirror.**  At `X = Q^{|N|}` (i.e. `Q^{-N}` with `N < 0`) the
    surviving blocks are those with at most `-N` rows — the textbook
    `GL(N)`/HOMFLY form of the level-rank truncation. -/
theorem schurElement_tl_ne_zero_iff_length_le {Q : ℝ} (hQ : 1 < Q) {N : ℤ}
    (hN : N < 0) {lam : Partition} (hpos : ∀ x ∈ lam, 0 < x) :
    schurElement Q (Q ^ (-N)) lam ≠ 0 ↔ (lam.length : ℤ) ≤ -N := by
  rw [Ne, schurElement_tl_eq_zero_iff hQ, hasContentCell_iff_lt_length hN hpos]
  omega

/-! ## Sanity instances (no `decide` laundering — these are genuine checks) -/

/-- `TL` level `N = 2`, rank 4: the shape `(2,2)` survives (≤ 2 columns).
    (`decide` here discharges a genuinely finite decidable check — sortedness
    of a concrete two-element list — not a structural claim.) -/
example {Q : ℝ} (hQ : 1 < Q) : schurElement Q (Q ^ (-(2 : ℤ))) [2, 2] ≠ 0 := by
  rw [schurElement_tl_ne_zero_iff_numCols_le hQ (by norm_num) (by decide)]
  simp [numCols]

/-- `TL` level `N = 2`, rank 4: the shape `(3,1)` is dropped (3 columns). -/
example {Q : ℝ} (hQ : 1 < Q) : schurElement Q (Q ^ (-(2 : ℤ))) [3, 1] = 0 := by
  rw [schurElement_tl_eq_zero_iff_numCols_gt hQ (by norm_num) (by decide)]
  simp [numCols]

end QOU.MathlibExt.WenzlSchurElement

