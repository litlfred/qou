---
# qou-yhod
title: 'GAP: dimHLF is not known to be transpose-invariant — the two-row/two-column bridge is proved only at n = 3..6'
status: completed
type: task
priority: high
created_at: 2026-09-07T05:08:37Z
updated_at: 2026-09-07T05:20:40Z
---

## What is open

`QOU.BraidKnot.IdentityI.dimHLF` (Frame–Robinson–Thrall, `n!/∏ h_c`, on `List ℕ`)
is not known in this corpus to satisfy `dimHLF λ = dimHLF λ'`. Proved only at
`n = 3, 4, 5, 6`, by `decide`, in
`QOU/MassTheory/TwoRowTwoColumnCollision.lean` (`dim_eq_dim_transpose_three_to_six`).

## Why it matters — the blast radius is a convention straddle, not a missing lemma

Two halves of the Lean tree quantify over Temperley–Lieb survivors in opposite
conventions and nothing related them until PR on branch
`claude/cds1-tl-weights-witness-2026-09-06`:

| module | condition |
|---|---|
| `QBeta.TemperleyLiebTower`, `QBeta.TwoRowNormalisation` | at most two **rows** |
| `MathlibExt.WenzlSchurElement`, `MassTheory.SelfConjugateStratumVanishes` | at most two **columns** |

`TwoRowTwoColumnCollision` now proves the *shape* half at general `n` — the
families are equinumerous under transpose and are different sets. The
*dimension* half is what this bean is: `Mathlib.TwoRowDimCatalan` proves
`Σ dim² = catalan n` for the ≤2-row family at every `n`, and there is no
≤2-column counterpart, so the column family's total is known only where it was
decided.

The consequence is specific: a proof transported between the two halves by
matching totals rather than by transposing is **wrong without ever producing a
wrong number** — at `n = 3` both families total 5, at `n = 6` both total 132 and
the families share nothing at all. The next step anyone takes here is wiring the
proved Wenzl stratification to the mass channel at `n = 3A`.

## The route, so the next attempt does not start cold

Both hook products factor into the *same three* products. For the two-row shape
`(a, b)` with `a = k+m`, `b = k`, against its transpose `2^k 1^m`:

    two-row:     ∏_{j<b}(a−j+1) · ∏_{b≤j<a}(a−j) · ∏_{j<b}(b−j)
    two-column:  ∏_{i<k}(k+m−i+1) · ∏_{k≤i<k+m}(k+m−i) · ∏_{i<k}(k−i)

Termwise identical under `a = k+m`, `b = k`. So `prodHooks` agrees and therefore
`n!/prodHooks` does — **no factorial manipulation is needed**, which is the part
that makes this cheaper than it looks. What is needed is only:

1. `colLen (replicate k 2 ++ replicate m 1) j` = `k+m` at `j=0`, `k` at `j=1`,
   `0` beyond — via `List.filter_append` / `List.filter_replicate`.
2. A `List.range (k+m)` split into the first `k` rows and the rest, with
   `l.getD i 0` = 2 then 1.
3. The termwise match.

Estimated 100–200 lines. Scoped to this family; the fully general
`dim λ = dim λ'` over arbitrary partitions is a larger, Mathlib-shaped statement
and is **not** what this bean asks for.

## What would close it

`theorem dimHLF_two_col_eq_two_row (n k : ℕ) (hk : 2 * k ≤ n) :
   dimHLF (List.replicate k 2 ++ List.replicate (n - 2*k) 1) = dimHLF [n - k, k]`

sorry-free, plus the corollary that the ≤2-column squared-dimension sum is
`catalan n` at general `n`.


## CLOSED 2026-09-07, same session it was filed

`dimHLF_two_col_eq_two_row` and `dimHLF_two_col_sq_sum` in
`QOU/MassTheory/TwoRowTwoColumnCollision.lean`, sorry-free at general `n`.
Verified `lean -DautoImplicit=false -s 65536` exit 0 plus `#print axioms`
([propext, Classical.choice, Quot.sound], no `sorryAx`). Commit `dd0afb7e50`.

The route recorded above held without modification — the three-factor termwise
match, no factorials. Total ~120 lines including the `colLen` / `getD` lemmas
for `List.replicate k 2 ++ List.replicate m 1`.

One thing the estimate missed. `colLen` had to be written out in full: with
`YoungDiagram` opened for the shape half of the same file, the bare name is
ambiguous against `QOU.BraidKnot.IdentityI.colLen`, and Lean refuses it. That is
the encoding straddle the file documents, occurring inside the file that
documents it.

Still open, and NOT what this bean asked for: `dim λ = dim λ'` for a general
partition (three-or-more rows *and* columns). Mathlib-shaped; no longer sits
between the two halves of this corpus.
