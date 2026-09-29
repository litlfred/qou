import QOU.Mathlib.SYTEnumeration

/-!
# QOU.Mathlib.SYTEnumerationN7 — brute-force `#SYT = dimHLF` at `n = 7` (isolated, expensive)

The per-shape hook-length validation `numSYTenum l = dimHLF l` is `decide`-checked for `n ≤ 6` in
`SYTEnumeration`.  This file pushes it one step further, to **every partition of `7`**.

**Why a separate leaf file.**  The `n = 7` check enumerates `7! = 5040` fillings per shape across `15`
shapes; the kernel `decide` takes ≈ 3.5 min wall and needs both `maxHeartbeats 0` (elaborator) and a
raised `maxRecDepth` (the `5040`-deep structural `allPerms` recursion).  Isolating it here — nothing
imports this module — keeps that cost off the build path of `SYTEnumeration`'s dependents
(`SYTHookFormula{,General}`), which stay fast.

**Axiom-free, not `native_decide`.**  This is a genuine kernel `decide`, so it adds **no** axioms
(`#print axioms numSYTenum_eq_dimHLF_7` shows only the propositional-extensionality/quotient core, no
`Lean.ofReduceBool` / `Lean.trustCompiler`).  This deliberately avoids the compiled-evaluator trust
that the `mpi9` cleanup is removing elsewhere (AGENTS.md §1a).  `n = 8` (`40320` fillings/shape) is the
practical kernel ceiling and is left to the aggregate `dim_validated_le12`; recorded, not silently
dropped.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (dimHLF)

/-- The partitions of `7` (every weakly-decreasing shape with `∑ = 7`). -/
def shapes7 : List (List ℕ) :=
  [[7], [6, 1], [5, 2], [5, 1, 1], [4, 3], [4, 2, 1], [4, 1, 1, 1], [3, 3, 1],
   [3, 2, 2], [3, 2, 1, 1], [3, 1, 1, 1, 1], [2, 2, 2, 1], [2, 2, 1, 1, 1],
   [2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- **Per-shape hook-length validation at `n = 7` (sorry-free, axiom-free kernel `decide`).**
`#SYT(λ) = dimHLF(λ)` for every partition of `7`, extending `numSYTenum_eq_dimHLF_6`. -/
theorem numSYTenum_eq_dimHLF_7 :
    ∀ l ∈ shapes7, numSYTenum l = dimHLF l := by decide

end QOU.Mathlib.SYTEnum
