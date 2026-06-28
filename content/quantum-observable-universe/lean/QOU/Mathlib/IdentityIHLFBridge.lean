import QOU.Mathlib.RSKBurnsideTarget
import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# QOU.Mathlib.IdentityIHLFBridge — the hook-length bridge `dimSYT = dimHLF ∘ toList`

The session's two dimension notions for a partition `λ ⊢ n` are:

* `dimSYT p := numStandardYoungTableaux (partitionShape p)` — the **genuine** SYT count, a
  `Finite`-backed `Nat.card` over the `StandardYoungTableau` type (`RSKBurnsideTarget`); and
* `QOU.BraidKnot.IdentityI.dimHLF l := (sz l).factorial / ∏_c h_c` — the **Frame–Robinson–Thrall
  hook-length dimension** over the weakly-decreasing `List ℕ` model (`IdentityIContentDecomposition`),
  already `decide`-validated `Σ_λ dimHLF(λ)² = n!` for `n ≤ 12` (`dim_validated_le12`) and wired into
  the `PlancherelSnData {3..12}` instances.

The **hook-length formula** asserts these agree: `#SYT(λ) = n!/∏_c h_c`.  Stated on the partition
index (`p.parts` sorted weakly-decreasing is exactly the row-length list both `partitionShape` and
`PartitionListBridge.toList` build):

    dimSYT p = dimHLF (p.parts.sort (· ≥ ·)).

**Why this is the load-bearing target.**  A proof of `dimSYT_eq_dimHLF` would, composed with the
already-proved `PartitionListBridge.sum_image_toList`, transport the `decide`-verified `n ≤ 12`
`dimHLF` Plancherel data onto `dimSYT` — grounding `RSKBurnsideHolds n` for those `n` in the genuine
`#SYT` count, *without* a full general-`n` RSK proof.

**Honesty caveat (corrects an over-optimistic review note).**  This is **not** a `decide`-closure:
`dimSYT` is a *noncomputable* `Nat.card`, so `dimSYT p = dimHLF (toList p)` is exactly the
hook-length formula — a real theorem (Greene–Nijenhuis–Wilf / the classical FRT proof), not a bounded
computation.  It is therefore stated here with a cited `sorry` (the honest "queued, not yet proved"
disposition, AGENTS.md §1a), pending either a Lean proof of the HLF or a computable `Fintype`
characterisation of `StandardYoungTableau`.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open QOU.BraidKnot.IdentityI

/-- **Hook-length bridge (target).**  The genuine SYT count equals the Frame–Robinson–Thrall
hook-length dimension of the partition's (weakly-decreasing) row-length list — the hook-length
formula `#SYT(λ) = n!/∏_c h_c`.  See the module docstring for what proving it unlocks and why it is
the HLF (not a `decide`-closure).  Proof deferred. -/
theorem dimSYT_eq_dimHLF {n : ℕ} (p : Nat.Partition n) :
    dimSYT p = dimHLF (p.parts.sort (· ≥ ·)) := by
  -- Ref: [stanley1999] Enumerative Combinatorics II §7.21 (Frame–Robinson–Thrall hook-length
  --      formula: #SYT(λ) = n!/∏_c h_c). The HLF; not yet formalized in pinned Mathlib.
  sorry

end QOU.Mathlib
