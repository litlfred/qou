---
# qou-affg
title: 'GAP: relate (buildChains config).get! j to chainCrossings config j'
status: completed
type: task
priority: normal
created_at: 2026-09-05T06:22:17Z
updated_at: 2026-09-05T08:36:53Z
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


## UPDATE 2026-09-05 (second) — the three-arm case split was illusory

`buildChains_eq_foldl` (commit 07984d4357, `rfl` on all three branches):

    buildChains config = (config.foldl (buildStep config) ([], 0)).1

The `[]` and `[_]` special-case arms are **redundant** — folding `[]` gives
`([], 0)` and folding `[x]` gives `([], 1)`, first component `[]` either way.
So the "not nil and not singleton" side conditions I flagged in the first
update do NOT survive into the induction. Scratch that obstacle.

**TRAP.** `buildStep`'s body must stay term-identical to `buildChains`'s step,
including the deprecated `List.get! (k - 1)`. Modernising it to
`config[k - 1]!` breaks `buildChains_eq_foldl` — measured, `rfl` fails; the two
accessors are not definitionally equal at that strength. The inherited
deprecation warning is deliberate and documented at the def.

## All that is left: the accumulator invariant

For `m <= config.length`, folding `config.take m`:

    (config.take m).foldl (buildStep config) ([], 0) = (L m, m)
    L m = (List.range (m-1)).map (fun j =>
            (((config.take m).drop (j+1)).map (crossingMatrix config[j]!)).prod)

At `m = config.length` this is the bean's goal. The step case splits at
`m = 0` (counter guard) and `m >= 1`, and needs:

- `List.take_succ` to peel `config.take (m+1) = config.take m ++ [config[m]!]`
- `List.mapIdx` length + getElem lemmas for the `extended` component
- `List.drop_append` for `j < m-1`, and the singleton case for `j = m-1`

The closure indexes the ORIGINAL `config` (`config[j]!`, `config.get! (k-1)`),
not the prefix, so there is no re-indexing to do. `j + 1 < config.length` is
still needed to discharge `get!` partiality on both sides.


## CLOSED 2026-09-05 (commit cb69733d71)

`matrixChain_eq_buildChains` is proved UNCONDITIONALLY. The class hypothesis is
gone from its signature, and `instMatrixChainEqBuildChains` inhabits the class.

    matrixChain_eq_buildChains_unconditional
      (config) (j) (hj : j + 1 < config.length) :
        matrixChain (chainCrossings config j) = (buildChains config).get! j

Six declarations complete the induction, all on [propext, Classical.choice,
Quot.sound] and nothing else:

  mapIdx_map_range · take_succ_of_lt · chainsUpTo · chainsUpTo_succ ·
  foldl_take (the accumulator invariant) · buildChains_get

**Nothing new was needed from Mathlib in this entire arc.**

### The three mislocations, for the record

1. `List.foldl_eq_foldr_of_comm` cited as missing — no such lemma exists.
2. "a pointwise-commuting variant without the `flip`" (mine) — there was no
   fold-direction problem at all; `matrixChain` reverses its list.
3. "the three-arm case split forces side conditions" (also mine) — the `[]`
   and `[_]` arms of `buildChains` are redundant.

Each made the gap look like something other than what it was: one accumulator
invariant over an index-tracking foldl.

### TRAP worth keeping

`Mathlib.Data.List.Indexes` is **absent from the restored olean cache** (39 of
the Mathlib `Data/List` oleans are present), so `List.mapIdx_append_one` is
unreachable in this container without a build. `List.length_mapIdx` and
`List.getElem_mapIdx` come from **Lean core** and are enough — reach for those.
