---
# qou-bdlp
title: 'Retroactive: shell 2n² capacity demoted; self-square conjecture opened (PR #5476)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T20:39:11Z
updated_at: 2026-08-22T20:39:34Z
---

## Why this bean is retroactive

Opened **after** the work landed on `claude/shell-2n2-self-square-2026-08-22`
(PR #5476). The agent that did the work ran without a bean and flagged the
omission itself; per AGENTS.md §"Agent work-plan policy" item 3, *"Report
unclaimed work as unclaimed. If you did durable work without a bean, say so and
open one."* This is that bean. It is opened at `in-progress`, not `todo`,
because the work exists.

## What landed (4 commits, PR #5476)

| commit | change |
|---|---|
| `db7eec90de` | open `conj:shell-space-is-self-square` — new block + sibling `.lean` |
| `0f42a7f70b` | retire `conj:electron-shell-2n2-capacity` → `rem:` on the derived proposition |
| `0f876794cd` | wire the new conjecture into ch.12; order the shell blocks by role |
| `04af5b81d8` | `rem:hydrogen-orbitals`: SO(3) supplies the `2ℓ+1`, not the cutoff |

## The substantive result

The new conjecture's sibling carries four sorry-free declarations, of which
`qCG_self_square` is new to the corpus:

    [n]_q² = Σ_{ℓ < n} [2ℓ+1]_q

i.e. the `n`-shell space is the self-square `V ⊗ V` of a single element rather
than a representation of either SO(3) or SO(4). That is the 2026-06-20 owner
directive on the SO(3)/SO(4) question, now carried in Lean instead of in prose.

## Two corrections it also made

- `conj:electron-shell-2n2-capacity` asserted as a conjecture what the adjacent
  proposition already derives — demoted to a remark rather than deleted, so the
  interpretive content survives without the standing claim.
- `rem:hydrogen-orbitals` over-attributed the shell cutoff to SO(3). SO(3)
  supplies the `2ℓ+1` multiplicity only; the cutoff `ℓ < n` is separate.

## Deliberately not done

No `uses` edge from the new conjecture back to the shell blocks: it would close
a cycle in the dependency DAG. Recorded rather than forced.
