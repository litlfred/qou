import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Data.Multiset.Sort
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import QOU.Mathlib.StandardYoungTableau

/-!
# QOU.Mathlib.RSKBurnsideTarget — Identity-I axiom (i) stated with the genuine `#SYT` count

This glue file connects the session's two merged infra pieces — the `Nat.Partition`/sorted-list
bridge (`PartitionListBridge`) and the standard-tableau primitive (`StandardYoungTableau`,
`numStandardYoungTableaux`) — into the precise statement of **Identity-I axiom (i)**, the RSK /
Burnside identity

    ∑_{p ⊢ n} dim(p)² = n!,   dim(p) := #SYT(shape p).

Mathlib's abstract partition index `Nat.Partition n` maps to a `YoungDiagram` via
`YoungDiagram.ofRowLens` applied to the parts sorted weakly-decreasing (the same sorted-list the
`PartitionListBridge` builds), and `numStandardYoungTableaux` of that diagram is the genuine SYT
count (a `Finite`-backed `Nat.card`).  So `RSKBurnsideHolds n` is a faithful, fully-*defined*
`Prop` — a well-typed equation, **not yet a theorem**: its *proof* is the RSK correspondence
`S_n ≃ Σ_λ SYT(λ)²` (absent from pinned Mathlib; the multi-session next step).  This supplies the
concrete `dimSYT` for the abstract `dim` field of `RSKBridge.RSKBijection`.

`rskBurnside_imp_substrate` makes the connection explicit: a proof of `RSKBurnsideHolds n` discharges
`RSKBridge.RSK_substrate_axiom n` (instantiate its existential witness with `dimSYT`).  Two further
targets remain open (the genuine open work, stated here so the discharge paths are visible):

* `dimSYT_eq_dimHLF` — `dimSYT p = dimHLF (toList p)`, the Frame–Robinson–Thrall hook-length formula
  (`#SYT(λ) = n!/∏h_c`).  Combined with the already-proved `PartitionListBridge.sum_image_toList`
  this would transport the `decide`-verified `n ≤ 12` `dimHLF` Plancherel instances
  (`IdentityIPlancherelInstances`) onto `dimSYT`.  **Caveat:** `dimSYT` is a *noncomputable*
  `Nat.card`, so this is NOT a `decide`-closure — it is exactly the HLF (a real theorem), not a
  bounded computation.  Deferred.
* a proof of `RSKBurnsideHolds n` itself (general RSK).  Deferred.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open YoungDiagram

variable {n : ℕ}

/-- The Young diagram of a partition `p ⊢ n`: its parts, sorted weakly-decreasing, as row lengths
(the same sorted list `PartitionListBridge.toList` produces). -/
def partitionShape (p : Nat.Partition n) : YoungDiagram :=
  YoungDiagram.ofRowLens (p.parts.sort (· ≥ ·)) (Multiset.sort_sorted _ _)

/-- The standard-tableau dimension of a partition: `#SYT` of its Young diagram.  This is the
genuine combinatorial `dim(p)` (a `Finite`-backed `Nat.card`), the concrete value the abstract
`RSKBridge.RSKBijection.dim` field should carry. -/
noncomputable def dimSYT (p : Nat.Partition n) : ℕ :=
  numStandardYoungTableaux (partitionShape p)

/-- **Identity-I axiom (i), stated with the genuine SYT count** — the RSK / Burnside identity
`∑_{p ⊢ n} dim(p)² = n!`.  A faithful, fully-*defined* `Prop` (a well-typed equation), **not yet a
theorem**: its proof is the RSK correspondence `S_n ≃ Σ_λ SYT(λ)²`, which the pinned Mathlib lacks
and which is the multi-session next step toward discharging `PlancherelSnData.sum_dim_sq`. -/
def RSKBurnsideHolds (n : ℕ) : Prop :=
  ∑ p : Nat.Partition n, (dimSYT p) ^ 2 = n.factorial

/-- **A proof of `RSKBurnsideHolds n` discharges the (deliberately weak) `RSK_substrate_axiom`.**
`RSKBridge.RSK_substrate_axiom n` only asserts the *existence* of some `dimFn` with `∑ dimFn² = n!`
(satisfiable trivially, hence not the real identity).  This theorem exhibits the genuine witness:
once `RSKBurnsideHolds n` is proved, `dimSYT` is exactly such a `dimFn`.  So the concrete identity is
at least as strong as the abstract existential — the honest direction of the bridge.  (Stated with
the existential inline rather than importing `RSKBridge` to keep this file self-contained.) -/
theorem rskBurnside_imp_substrate (h : RSKBurnsideHolds n) :
    ∃ dimFn : Nat.Partition n → ℕ, ∑ p : Nat.Partition n, (dimFn p) ^ 2 = n.factorial :=
  ⟨dimSYT, h⟩

end QOU.Mathlib
