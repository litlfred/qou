import QOU.Mathlib.SYTHookFormulaRows

/-!
# QOU.Mathlib.SYTHookFormulaGeneral — the general Frame–Robinson–Thrall hook-length formula

**Target (open):**

    numSYTenum_eq_dimHLF (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (hpos : ∀ a ∈ l, 0 < a) :
        QOU.Mathlib.SYTEnum.numSYTenum l = QOU.BraidKnot.IdentityI.dimHLF l

The merged bridge (`SYTEnumerationFintype.numSYTenum_eq_numStandardYoungTableaux`,
`dimSYT_eq_numSYTenum`, all `n`, sorry-free) collapses the dimension hook-length formula
`dimSYT = dimHLF` to this single pure-combinatorial identity — no `StandardYoungTableau` structure,
nothing archimedean.  It is already closed for `∑l ≤ 4` (`numSYTenum_eq_dimHLF_le4`) and for
**one-row / two-row** shapes in full generality (`SYTHookFormulaRows`).

**Two routes to general `n`:**

* **Beta-numbers / Frobenius determinant.**  With `k = l.length` and `β_i = l[i] + (k-1-i)`,
  `∏_c h_λ(c) = (∏_i β_i!)/(∏_{i<j}(β_i−β_j))` and `#SYT(λ) = n!·(∏_{i<j}(β_i−β_j))/(∏_i β_i!)`
  (Vandermonde / Aitken determinant); dividing gives `#SYT = n!/∏h_c`.
* **Corner recursion + GNW.**  `#SYT(λ) = Σ_{removable corners} #SYT(λ∖c)`, with the
  Greene–Nijenhuis–Wilf hook-summation identity supplying the same recursion for `dimHLF`.

This module collects the general-`n` proof as it is built.  Pure combinatorics on `ℕ`; nothing
archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

-- General-n hook-length formula: under construction (see module docstring for the target + routes).

end QOU.Mathlib.SYTEnum
