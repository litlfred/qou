---
# qou-500d
title: witness shape guard cannot distinguish a producer speedup from an interrupted write
status: in-progress
pr: 8333
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-27T07:19:03Z
updated_at: 2026-10-04T15:25:39Z
parent: qou-5vkl
---

## The false positive, measured

`computations/witness_shape_guard.py` flagged
`computations/block-swap-binding.witness.json` as **COLLAPSED**:

> durationMs collapsed: 37,731 -> 1,818 — the hallmark of a run that was
> interrupted mid-write

It was not interrupted. It got **faster**. The witness was last changed by
`6e1009bed8` / `cdb64587b8` — the sibling's `perf(block_swap_binding)` work,
whose own commit reports **1800s -> 5 seconds** (seminormal instead of
Geck-Pfeiffer).

Content, measured, before vs after:

    top-level keys   18  ->  19     (GAINED one)
    data keys         6  ->   6
    assertions        1  ->   1
    data keys lost              none
    data keys gained            none

So **every content measure held or grew** while `durationMs` fell 20x. The guard
fired on the duration alone.

## Why this will recur

A perf win and a truncated write look identical under a duration heuristic, and
this repo actively optimises producers — `qou-mtx9`, the `block_swap_binding`
work, the batched GP reduction. Every future speedup of a witness-emitting
producer trips this.

The guard's own text says the raw-float64 ratchet cannot catch a gutted witness
(`qou-h4xk`), which is why the duration signal was added. That reasoning is
sound; the discriminator is what needs work.

## Suggested fix — do not just raise the threshold

A gutted witness loses **content**. A fast one does not. The guard already has
both files in hand, so key the verdict on content rather than time:

- flag only if `durationMs` collapses **AND** some content measure shrinks
  (data keys, assertion count, top-level keys, serialized size);
- when duration collapses with content intact or larger, that is a **speedup** —
  report it as an informational line, not a RED.

Raising the duration ratio would only move the goalposts: a 1800s -> 5s win is
360x, larger than any threshold that still catches real truncation.

## Second, smaller point: the comparison basis mid-merge

The guard diffs the working tree against `HEAD`. During an uncommitted merge,
HEAD is still the pre-merge tip, so **every witness edit arriving with the merged
branch reads as an uncommitted modification** — here, 20 of them from main's 43
commits. Committing the merge restored the basis and the gate went green with no
other change.

That is not a defect on its own, but combined with the above it means a routine
`git merge origin/main` on any branch can produce a RED that belongs to neither
branch. Worth a line in the guard's output naming the merge case.

## Provenance

Found on PR #5869 while merging main (43 commits) into
`claude/trace-invisible-pairing-representable-2026-08-27`. Established as
not-this-PR's before proceeding: the branch has never touched that file (empty
diff against the merge base). Nothing was baselined or hand-edited; the merge was
committed and the gate went green on its own.


## Round 56 Implementation (PR #8333)
- Implemented on branch `claude/round56-trd0-9nnz-fixes` (commit `e33bff7d43b72a19e618441a16ae41a21af05e0e`, https://github.com/litlfred/qou/pull/8333).
