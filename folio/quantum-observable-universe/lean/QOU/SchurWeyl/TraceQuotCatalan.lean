/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.TwoRowIdxReindex
import QOU.SchurWeyl.TwoRowSYTBallot
import QOU.Mathlib.TwoRowDimCatalan

/-!
# `dim (H_n(q)/rad(wtrace)) = catalan (n+1)`

The arc's chain, closed. Every link was proved separately; this file is the composition.

    finrank R (H_n(q)/rad(wtrace))
      = Σ_{λ ⊢ n+1, ℓ(λ) ≤ 2} (f^λ)²          WtraceRadicalSemisimple.finrank_traceQuot
      = Σ_{k ≤ ⌊(n+1)/2⌋} (#SYT (n+1−k, k))²   TwoRowIdxReindex.finrank_traceQuot_eq_range_sum
      = Σ_{k ≤ ⌊(n+1)/2⌋} (ballot (n+1) k)²    TwoRowSYTBallot.numSYT_twoRow_eq_ballot
      = Σ_{k ≤ ⌊(n+1)/2⌋} (dimHLF [n+1−k, k])²  Mathlib.dimHLF_two_row_eq_ballot
      = catalan (n+1)                           Mathlib.dimHLF_two_row_sq_sum

The third step is the one that was missing until now: it is the **two-row** hook length formula,
and it is what lets a genuine tableau count meet a hook-length-formula value.  The general
Frame–Robinson–Thrall theorem is still absent from Mathlib and still proved in this corpus only
for `n ≤ 4` plus `n = 5`; it is **not** needed here.

## 🛑 This is a DIMENSION, not an isomorphism with `TL_n(δ)`

`catalan (n+1)` is the dimension of `TL_n(δ)`, so this says the quotient has exactly the right
dimension to be the Temperley–Lieb algebra — and, with
`WtraceRadicalSemisimple.traceQuotEquiv`, exactly the right Wedderburn block structure too.

**It does not say the two algebras are isomorphic.**  That needs
`⟨U_i U_j U_i − v²·U_i⟩ = rad(tr_M)`, the open item `QOU.MathlibExt.HeckeToTemperleyLieb`
records, and nothing here closes it.  The content block `hecke-radical-is-temperley-lieb`'s
sentence — *"a count of blocks and a count of dimensions are not an isomorphism of algebras"* —
remains **true**, and this file is precisely a count of dimensions.  Do not cite it otherwise.

What it does buy: the dimension obstruction to that identification is gone.  Previously the two
sides were a count and a formula with no bridge; now they agree, for every `n`.

-- Ref: [leitner2026] beans qou-7vht, qou-7wf6, qou-8iru, qou-cds1.
-/

namespace QOU.SchurWeyl.TraceQuotCatalan

open QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep
open QOU.SchurWeyl.TwoRowIdxReindex QOU.SchurWeyl.TwoRowSYTBallot
open QOU.QBeta.MarkovTraceQuotient

/-- **The quotient's dimension is the Catalan number**, for every `n`, at convention D.

`catalan (n+1) = dim TL_n(δ)`.  🛑 A dimension, **not** an isomorphism — see the module
docstring. -/
theorem finrank_traceQuot_eq_catalan {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (n : ℕ) :
    (Module.finrank ℝ (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) : ℤ)
      = catalan (n + 1) := by
  rw [finrank_traceQuot_eq_range_sum hq0 hq2 hq21 hgen n, ← dimHLF_two_row_sq_sum (n + 1)]
  push_cast
  refine Finset.sum_congr rfl fun k hk => ?_
  have hkr : k < (n + 1) / 2 + 1 := Finset.mem_range.mp hk
  have hk2 : 2 * k ≤ n + 1 := by omega
  have h1 : k ≤ n + 1 - k := by omega
  rw [twoRowDim_eq h1]
  rw [numSYT_twoRow_eq_ballot (n + 1 - k) k h1,
    show (n + 1 - k + k : ℕ) = n + 1 from by omega,
    ← dimHLF_two_row_eq_ballot (n + 1) k hk2]

end QOU.SchurWeyl.TraceQuotCatalan
