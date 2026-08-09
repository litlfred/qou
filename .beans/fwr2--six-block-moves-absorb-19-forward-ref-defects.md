---
# fwr2
title: 'six block moves absorb 19 forward-ref defects'
status: open
type: task
priority: normal
created_at: 2026-08-09T21:35:00Z
updated_at: 2026-08-09T21:35:00Z
parent: fwr1
---
Six blocks each sit late in their chapter while three or more earlier blocks
declare a `uses[]` edge to them. Moving the one target earlier resolves the
whole group; fixing them edge-by-edge would not.

| edges | chapter | move | to before |
|---|---|---|---|
| 4 | mass-theory | `def:quantum-bloch-group` (389) | 61 |
| 3 | mass-theory | `def:archimedean-realization-functor` (319) | 10 |
| 3 | mass-theory | `prop:nuclear-knot-classification` (669) | 347 |
| 3 | brings-surface | `prop:cohomological-embedding` (153) | 100 |
| 3 | nuclear-interactions | `rem:energy-scale-planck` (127) | 68 |
| 3 | quantum-observable-universes | `def:categorical-instanton` (178) | 141 |

Positions are within-chapter manifest indices as of `fwr1`'s review; re-derive
before moving anything, since any earlier move shifts the rest.

Two of these have independent corroboration from the review: `rem:energy-scale-planck`
was flagged by its reviewer as "a single misplaced block accounting for 13% of my
slice", and `def:archimedean-realization-functor` is the target of the false-locator
foreshadow in `rem:motivic-mass-rationale` — the prose calls it "the next
subsection" when it is 21 sections and ~309 blocks away.

Moving a block changes chapter order, so re-run `detangler` after each: a move
that fixes three forward edges can create new ones behind it.
