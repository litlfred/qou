import QOU.BraidsAndKnots.YoungDiagramKernel
import QOU.BraidsAndKnots.YoungDiagramTransposeBridge
import QOU.Mathlib.SYTHookGNW

/-!
# QOU.BraidsAndKnots.YoungDiagramKernelDimPos — `sytDim` positivity via the HLF chain

The pincer scaffold (`YoungDiagramKernelPincer`) carries the dimension-positivity hypothesis
`∀ l ∈ partsOf k, 0 < sytDim l` on its bridge theorems. It is true — `f^λ = #SYT(λ) ≥ 1` — but
its list-level proof needs the Frame–Robinson–Thrall divisibility, which the corpus carries in a
*different* list formalization (`QOU.BraidKnot.IdentityI.prodHooks` / the machine-checked
`QOU.Mathlib.SYTEnum.numSYTenum_mul_prodHooks`). This file **bridges the two hook products and
discharges the hypothesis**:

* `hookProd_eq_prodHooks` — the kernel's `hookProd` (per-cell `λ_i + λ'_j − j − i − 1`) equals
  `IdentityI.prodHooks` (per-cell `(λ_i − j) + (colLen_j − i) − 1`) for sorted `l`. The two
  ℕ-truncated expressions agree exactly because on genuine cells both subtractions are
  non-truncating: `j < λ_i` (the cell bound) and `i < λ'_j` (its **staircase** mirror,
  `YoungDiagramTransposeBridge.lt_countP_iff`).
* `sytDim_eq_numSYTenum` / `sytDim_pos` — hence `sytDim l = numSYTenum l` and `0 < sytDim l`
  from `numSYTenum · prodHooks = n!` (`n! > 0` forces both factors positive; no separate
  `#SYT`-nonemptiness argument needed).
* `sytDim_pos_of_mem_partsOf` — the hypothesis in exactly the form the pincer consumes, with the
  sortedness/positivity supplied by the enumeration soundness (`partsOf_facts`).

Pure `ℕ` combinatorics; no fit; kernel conjecture untouched. Standalone library file (no
`.ts`/`.md` sibling), verified per-file by `lean`-direct, like its parents.

-- Ref: [leitner2026] docs/audits/2026-07-18-deltalambda-covariance-kernel-frontier.md
-/

namespace QOU.BraidsAndKnots.YoungDiagramKernelDimPos

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge

/-- `IdentityI.colLen` is `countP` (filter-length form). -/
theorem colLen_eq_countP (l : List ℕ) (j : ℕ) :
    QOU.BraidKnot.IdentityI.colLen l j = l.countP (fun x => decide (j < x)) := by
  unfold QOU.BraidKnot.IdentityI.colLen
  rw [List.countP_eq_length_filter]

/-- **The two list-level hook products agree** on sorted lists: the kernel's
`λ_i + λ'_j − j − i − 1` and `IdentityI`'s `(λ_i − j) + (colLen_j − i) − 1` compute the same hook
at every genuine cell, because `j < λ_i` (cell bound) and `i < λ'_j` (staircase) make both
ℕ-subtractions non-truncating. -/
theorem hookProd_eq_prodHooks (l : List ℕ) (hs : l.Sorted (· ≥ ·)) :
    hookProd l = QOU.BraidKnot.IdentityI.prodHooks l := by
  unfold hookProd QOU.BraidKnot.IdentityI.prodHooks
  refine congrArg List.prod (List.map_congr_left fun i _ => ?_)
  refine congrArg List.prod (List.map_congr_left fun j hj => ?_)
  rw [List.mem_range] at hj
  have hconj : (conj l).getD j 0 = l.countP (fun x => decide (j < x)) := conj_getD l hs j
  have hcol := colLen_eq_countP l j
  have hstair : i < l.countP (fun x => decide (j < x)) := (lt_countP_iff l hs j i).mpr hj
  rw [hconj, hcol]
  omega

/-- **`sytDim` is the genuine `#SYT` count**: the kernel's hook-length dimension equals the
enumeration count `numSYTenum` (sorted positive lists), via the hook-product bridge and the
machine-checked FRT identity `numSYTenum · prodHooks = n!`. -/
theorem sytDim_eq_numSYTenum (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) :
    sytDim l = QOU.Mathlib.SYTEnum.numSYTenum l := by
  have hmul := QOU.Mathlib.SYTEnum.numSYTenum_mul_prodHooks l hs hpos
  have hph : 0 < QOU.BraidKnot.IdentityI.prodHooks l :=
    QOU.Mathlib.SYTEnum.prodHooks_pos l hs hpos
  unfold sytDim
  rw [hookProd_eq_prodHooks l hs,
    show l.sum = QOU.BraidKnot.IdentityI.sz l from rfl, ← hmul,
    Nat.mul_div_cancel _ hph]

/-- **Dimension positivity** (the pincer's hypothesis, proved): `0 < sytDim l` for sorted
positive lists — `numSYTenum · prodHooks = n! > 0` forces `numSYTenum > 0`. -/
theorem sytDim_pos (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (hpos : ∀ x ∈ l, 0 < x) :
    0 < sytDim l := by
  rw [sytDim_eq_numSYTenum l hs hpos]
  have hmul := QOU.Mathlib.SYTEnum.numSYTenum_mul_prodHooks l hs hpos
  rcases Nat.eq_zero_or_pos (QOU.Mathlib.SYTEnum.numSYTenum l) with h0 | h
  · exfalso
    rw [h0, zero_mul] at hmul
    exact absurd hmul.symm (Nat.factorial_pos _).ne'
  · exact h

/-- The hypothesis in exactly the form the pincer bridge theorems consume. -/
theorem sytDim_pos_of_mem_partsOf (k : ℕ) : ∀ l ∈ partsOf k, 0 < sytDim l := by
  intro l hl
  obtain ⟨_, hpos, hsort⟩ := partsOf_facts k l hl
  exact sytDim_pos l hsort hpos

end QOU.BraidsAndKnots.YoungDiagramKernelDimPos
