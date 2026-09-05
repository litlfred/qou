---
# qou-affg
title: 'GAP: relate (buildChains config).get! j to chainCrossings config j'
status: todo
type: task
priority: normal
created_at: 2026-09-05T06:22:17Z
updated_at: 2026-09-05T07:19:16Z
---

## What is open

`QOU.TMCorrespondence.MatrixChainEqBuildChains` (a no-instance conditional
class, §3b-cond) asserts

    matrixChain (chainCrossings config j) = (buildChains config).get! j

`matrixChain_eq_prod` (proved 2026-09-05, sorry-free, no instance) now closes
the **left** side completely: `matrixChain seq = (seq.map T).prod`, with the
recursion's list reversal removed via `transferMatrix_comm` +
`QOU.MathlibExt.prod_reverse_eq_of_pairwise_commute`.

What is left is the **right** side, and it is not a list-lemma problem.
`buildChains` (`QOU/Archimedean/TransferMatrix.lean:223`) is a `foldl` over the
nuclear configuration carrying a `(List TMatrix × ℕ)` accumulator which, per
step, `mapIdx`-extends every existing chain through `extendChain`, appends one
new chain, is guarded by `if k = 0`, and reads nucleons with `get!`. Relating
`(buildChains config).get! j` to `chainCrossings config j` is a structural
induction on the configuration with index bookkeeping over a **partial**
accessor.

## What NOT to try

- **A foldl/foldr bridge lemma.** Two prior statements of this gap named one
  (`List.foldl_eq_foldr_of_comm`, which does not exist; then "a
  pointwise-commuting variant without the `flip`"). Both mislocated it. There
  is no fold-direction problem left.
- **`QOU.MathlibExt.foldl_eq_foldr_of_commute_init`.** Its docstring claimed
  to discharge this class "after some rearrangement". It does not — it moves
  the *accumulator* between ends and leaves list order alone. Corrected
  in-place 2026-09-05.

## Next honest step

Induct on `config` and prove a strengthened invariant about the `foldl`
accumulator (both the chain list and the counter `k`) rather than about
`buildChains` directly; the `get!`/`get!`-partiality will need
`j + 1 < config.length` threaded through.


## UPDATE 2026-09-05 — the left-hand side is now fully discharged

`matrixChain_chainCrossings` (commit 207f4372dd, sorry-free, no instance):

    matrixChain (chainCrossings config j)
      = ((config.drop (j+1)).map (fun nk => crossingMatrix config[j]! nk)).prod

built from `smul_transferMatrix` + `crossingMatrix_eq` (step 1 of the file's own
four-step sketch) on top of `matrixChain_eq_prod` (the reversal).

**So this bean is now a purely combinatorial statement about `buildChains`:**

    (buildChains config).get! j
      = ((config.drop (j+1)).map (fun nk => crossingMatrix config[j]! nk)).prod

No Hecke content, no transfer matrices, no fold direction, no `Pairwise Commute`.
`crossingMatrix` can be treated as an opaque `NucleonType -> NucleonType -> TMatrix`
throughout — nothing about its value is needed any more.

### Shape of the remaining work

`buildChains` has three match arms (`[]`, `[_]`, catch-all), so the catch-all's
equation lemma carries "not nil and not singleton" side conditions. The induction
wants a strengthened invariant on the `foldl` accumulator, over BOTH components:
after processing a prefix of length `m`, the counter is `m` and the chain list has
length `m-1` with entry `j` equal to the product over the nucleons strictly between
`j` and `m`. Note the closure reads `config[j]!` and `config.get! (k-1)` against the
ORIGINAL list, not the prefix, so no re-indexing is needed — but `j + 1 < config.length`
has to be threaded to discharge the `get!` partiality on both sides.
