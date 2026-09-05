---
# qou-obkt
title: unified-iterative-correction-proof states the Wigner clause over k=4,5 but the k=5 shadow price is identically zero
status: completed
type: task
priority: normal
created_at: 2026-09-05T15:07:39Z
updated_at: 2026-09-05T15:13:11Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. The small certain fix
`qou-ld2a` named.

## The defect

`unified-iterative-correction-proof.md` read:

> *Wigner energy ($k \geq 5$, dedicated $-\Delta_W \cdot T(T+1)/A$):* the
> $k = 4, 5$ self-conjugate shadow prices ($\lambda = (2,2)$ and $(3,1,1)$),
> which vanish on isolated $pn$ crossings ... **but are nonzero on collective
> $pn$ patterns.**

Three things wrong with it:

1. `(3,1,1)` has `ell = 3`, so under convention D `w~ = 0`, hence `C = 0`,
   hence `u* = 0` (`qou-w06d`, `shadow_price_eq_zero_of_weight_eq_zero`). It is
   not a contributing shadow price.
2. "are nonzero on collective pn patterns" is false for `(3,1,1)` at **every**
   `(Z,N)` — the vanishing is upstream of the nuclear datum, so no `S_lambda`
   restores it. The clause promised a nuclear-datum-dependent rescue that
   provably cannot happen.
3. The header `$k \geq 5$` contradicted its own body (`k = 4, 5`), and line 12
   of the same block already credits `(2,2) \vdash 4` alone — so it was
   internally inconsistent as well as wrong.

## Falsifier checked BEFORE editing

The theorem is about `u*_lambda`; if the Wigner term were assembled by some
other path the clause might have been salvageable. Grepped: `(3,1,1)` appears in
**no live computation** — only `computations/_deprecated/next_partition_levels.py`.
So the clause described a mechanism its own implementation never used.

## The fix

Restated over `k = 4` and `(2,2)` alone, singular verbs, plus the reason no
higher self-conjugate partition can contribute (self-conjugacy forces
`ell = lambda_1`, the row cap admits only `(1)`, `(2,1)`, `(2,2)`, and a zeroed
weight kills the shadow price upstream of the scaling function).

## A judgement call worth recording: the qa sidecar was left STALE on purpose

Editing the `.md` changes its hash, so `source_hashes.md` in
`unified-iterative-correction-proof.qa.json` no longer matches. **That is
correct and was left alone.** The mismatch is exactly what marks every existing
verdict as keyed to a block version that no longer exists, so the drain queue
re-queues the block for review. Updating the hash by hand would falsely certify
those verdicts against a version nobody reviewed.

## Gates

`bun run scripts/run-validate.ts` — **✓ Valid**, 4 issues, all pre-existing and
in other blocks (`knot-periodic-table`, the bibliography registry,
`piece-a-corner-removal-obligation`, `em-coupling-projection-table1-data`).
Grepped the corpus for other surfaces repeating the `(2,2)` and `(3,1,1)`
pairing — none outside `_deprecated`.
