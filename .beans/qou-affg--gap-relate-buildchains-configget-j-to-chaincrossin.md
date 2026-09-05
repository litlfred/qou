---
# qou-affg
title: 'GAP: relate (buildChains config).get! j to chainCrossings config j'
status: todo
type: task
priority: normal
created_at: 2026-09-05T06:22:17Z
updated_at: 2026-09-05T06:22:44Z
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
