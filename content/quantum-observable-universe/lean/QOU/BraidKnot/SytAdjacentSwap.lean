import QOU.BraidKnot.StandardYoungTableau

/-!
# The consecutive-label cell-swap constructor for standard Young tableaux

The Okounkov–Vershik exchange argument (`JucysMurphy.lean`:
`syt_all_connect_to_some`) walks every standard tableau toward the
row-superstandard base by repeatedly swapping the cells of two **consecutive
labels** `a, a+1` when those cells lie in **different rows and different
columns**.  This file builds the elementary object that walk consumes: given a
`QOU.BraidKnot.StandardYoungTableau μ` and two cells `p, q ∈ μ` with
`entry q = entry p + 1` (consecutive labels) in different rows and columns, the
tableau obtained by exchanging their entries is again a standard Young tableau
(`swapCellsSYT`).

**The clean idea (why no cell geometry is needed).**  Realise the exchange as a
*value*-level involution `swapSucc a` that swaps the two integers `a` and `a+1`
and fixes everything else.  It is order-reversing **only** on the single pair
`(a, a+1)`; on every other strictly-increasing pair it is order-*preserving*
(`swapSucc_lt`).  The one bad pair is exactly the values of `p, q`, and — since
`entry` determines the cell (`inj_on`) — the different-row / different-column
hypotheses guarantee **no** row- or column-adjacent pair of cells carries the
values `(a, a+1)`.  So row/column strictness transfers verbatim, with the two
hypotheses discharging the single exceptional case.

Scope: pure combinatorics on `ℕ`; §7c-clean (no `ℝ`, no ordering on `q`); no fit.
-/

namespace QOU.BraidKnot

open YoungDiagram Classical

variable {μ : YoungDiagram}

/-- **The successor-swap involution on `ℕ`**: exchange `a` and `a+1`, fix all else.
This is the value-level shadow of exchanging the two consecutive labels. -/
def swapSucc (a e : ℕ) : ℕ := if e = a then a + 1 else if e = a + 1 then a else e

/-- `swapSucc a` is an involution, hence injective. -/
theorem swapSucc_injective (a : ℕ) : Function.Injective (swapSucc a) := by
  intro x y h
  simp only [swapSucc] at h
  split_ifs at h <;> omega

/-- `swapSucc a` preserves `<` **except** on the single pair `(a, a+1)`. -/
theorem swapSucc_lt (a : ℕ) {v w : ℕ} (h : v < w) (hne : ¬(v = a ∧ w = a + 1)) :
    swapSucc a v < swapSucc a w := by
  simp only [swapSucc]
  split_ifs <;> omega

/-- `swapSucc a` keeps values below a common bound `c`, provided `a` and `a+1` are
below `c`. -/
theorem swapSucc_lt_card (a : ℕ) {e c : ℕ} (he : e < c) (hb : a + 1 < c) :
    swapSucc a e < c := by
  simp only [swapSucc]
  split_ifs <;> omega

/-- **The consecutive-label cell-swap standard tableau.**  Exchange the entries of
the cells `p` and `q` (holding labels `a` and `a+1`) that lie in different rows
and different columns; the result is again a `StandardYoungTableau μ`. -/
noncomputable def swapCellsSYT (T : StandardYoungTableau μ) (p q : ℕ × ℕ)
    (hp : p ∈ μ) (hq : q ∈ μ)
    (hval : T.entry q.1 q.2 = T.entry p.1 p.2 + 1)
    (hrow : p.1 ≠ q.1) (hcol : p.2 ≠ q.2) :
    StandardYoungTableau μ where
  entry i j := if (i, j) ∈ μ then swapSucc (T.entry p.1 p.2) (T.entry i j) else 0
  lt_card i j hij := by
    have ha : T.entry p.1 p.2 < μ.card := T.lt_card p.1 p.2 (by rwa [Prod.mk.eta])
    have hb : T.entry q.1 q.2 < μ.card := T.lt_card q.1 q.2 (by rwa [Prod.mk.eta])
    rw [if_pos hij]
    exact swapSucc_lt_card _ (T.lt_card i j hij) (by rw [← hval]; exact hb)
  zero_off i j hij := by rw [if_neg hij]
  inj_on i j i' j' hij hij' heq := by
    rw [if_pos hij, if_pos hij'] at heq
    have hT := swapSucc_injective (T.entry p.1 p.2) heq
    exact T.inj_on i j i' j' hij hij' hT
  row_strict i j hcell := by
    have hij : (i, j) ∈ μ := μ.up_left_mem (le_refl i) (Nat.le_succ j) hcell
    rw [if_pos hij, if_pos hcell]
    refine swapSucc_lt _ (T.row_strict i j hcell) ?_
    -- the bad pair (a, a+1) can only be (p, q), which are NOT in the same row
    rintro ⟨hva, hvb⟩
    have hpcell : (i, j) = p := by
      have := T.inj_on i j p.1 p.2 hij (by rwa [Prod.mk.eta]) (by rw [hva])
      exact Prod.ext this.1 this.2
    have hqcell : (i, j + 1) = q := by
      have := T.inj_on i (j + 1) q.1 q.2 hcell (by rwa [Prod.mk.eta]) (by rw [hval]; rw [hvb])
      exact Prod.ext this.1 this.2
    exact hrow (by rw [← congrArg Prod.fst hpcell, ← congrArg Prod.fst hqcell])
  col_strict i j hcell := by
    have hij : (i, j) ∈ μ := μ.up_left_mem (Nat.le_succ i) (le_refl j) hcell
    rw [if_pos hij, if_pos hcell]
    refine swapSucc_lt _ (T.col_strict i j hcell) ?_
    -- the bad pair (a, a+1) can only be (p, q), which are NOT in the same column
    rintro ⟨hva, hvb⟩
    have hpcell : (i, j) = p := by
      have := T.inj_on i j p.1 p.2 hij (by rwa [Prod.mk.eta]) (by rw [hva])
      exact Prod.ext this.1 this.2
    have hqcell : (i + 1, j) = q := by
      have := T.inj_on (i + 1) j q.1 q.2 hcell (by rwa [Prod.mk.eta]) (by rw [hval]; rw [hvb])
      exact Prod.ext this.1 this.2
    exact hcol (by rw [← congrArg Prod.snd hpcell, ← congrArg Prod.snd hqcell])

end QOU.BraidKnot
