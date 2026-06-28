import QOU.Mathlib.SYTEnumerationFintype

/-!
# QOU.Mathlib.SYTHookFormula — the hook-length formula `dimSYT = dimHLF`, closed for `n ≤ 4`

The Frame–Robinson–Thrall hook-length formula is `#SYT(λ) = |λ|! / ∏_c h_c`, i.e. on the repo's two
dimension notions `dimSYT p = dimHLF (p.parts.sort (·≥·))` (the sorry in `IdentityIHLFBridge`).

**The counting bridge collapses this to pure combinatorics.**  `SYTEnumerationFintype` proved
`dimSYT p = numSYTenum (p.parts.sort (·≥·))` (and the list form
`numSYTenum l = numStandardYoungTableaux (ofRowLens l hl)`) for *all* `n`, sorry-free.  Composing,
the hook-length formula is **equivalent** to the parameter-free combinatorial statement

    numSYTenum l = dimHLF l        (for every weakly-decreasing positive `l`),

with **no `StandardYoungTableau` structure and nothing archimedean left** — "the brute-force count of
standard fillings equals `(∑l)! / ∏ hooks`."  `numSYTenum l = dimHLF l` is already `decide`-proved for
`∑l ≤ 4` (`numSYTenum_eq_dimHLF_le4`); so the hook-length formula on the **genuine** `#SYT` count is a
sorry-free *theorem* for `n ≤ 4` (this file).  The general `n` case is the classical HLF — a real
theorem (Greene–Nijenhuis–Wilf / Novelli–Pak–Stoyanovsky), still open here, now isolated to the single
combinatorial identity `numSYTenum = dimHLF`.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (dimHLF)

/-- **Hook-length formula on the genuine SYT count, for `n ≤ 4` (sorry-free).**  For every shape `l`
with `∑l ≤ 4`, the genuine standard-tableau count `numStandardYoungTableaux (ofRowLens l hl)` equals
the Frame–Robinson–Thrall hook dimension `dimHLF l`.  Composes the counting bridge
`numSYTenum = numStandardYoungTableaux` (all `n`) with the `decide`-verified `numSYTenum = dimHLF`
(`n ≤ 4`).  This closes `dimSYT = dimHLF` on the genuine count for the small-`n` range. -/
theorem numStandardYoungTableaux_eq_dimHLF_le4 (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hmem : l ∈ shapesLE4) :
    numStandardYoungTableaux (YoungDiagram.ofRowLens l hl) = dimHLF l := by
  rw [← numSYTenum_eq_numStandardYoungTableaux l hl]
  exact numSYTenum_eq_dimHLF_le4 l hmem

end QOU.Mathlib.SYTEnum
