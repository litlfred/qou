---
# qou-mtcx
title: 'TASK: MarkovTraceContext generic base ring — 16 extenders'
status: todo
type: task
priority: medium
tags: [lean, wall-side, 7c, refactor]
created_at: 2026-08-08T13:00:00Z
updated_at: 2026-08-08T13:00:00Z
---

`lean/QOU/BraidsAndKnots/qmn_recursive_memoized.lean` is a genuine base-ring
candidate that **cannot be ported in isolation**: its class
`QmnRecursiveMemoizedContext extends QOU.Shared.MarkovTraceContext`, so the `ℝ`
would have to be threaded through that shared parent — which **16 classes
extend**.

```
grep -rl "extends QOU.Shared.MarkovTraceContext\|extends MarkovTraceContext" \
  --include=*.lean content/     # -> 16
```

## Why it is worth doing

The Markov trace is the Jones invariant; its algebraic home is `ℤ[q, q⁻¹]`, not
`ℝ`. A generic parent would let every one of the 16 descendants state its
content over the right ring and would take a whole family off the wall-side
queue at once, rather than one block at a time.

## Method

1. Read `lean/QOU/Shared/MarkovTraceClaim.lean` first — it may already be
   `ℝ`-free, in which case the work is only in the descendants.
2. Parameterise the parent, then fix descendants in dependency order.
3. `scripts/lean-direct-cone.sh` per module, `-DautoImplicit=false`. Never
   `lake build`.
4. This is a refactor, not a drain — land it as its own PR with the 16-file
   list in the body.

## Trap recorded

A consumer count of *"appears in 1 `.lean` file"* is what hid this. **A file
count does not measure blast radius when the dependency runs through class
inheritance rather than imports.** Check `extends` edges explicitly.
