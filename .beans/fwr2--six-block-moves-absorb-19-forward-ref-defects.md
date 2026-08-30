---
# fwr2
title: 'six block moves absorb 19 forward-ref defects'
status: completed
type: task
priority: normal
created_at: 2026-08-09T21:35:00Z
updated_at: 2026-08-09T23:10:00Z
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

---

**Outcome: 5 of 6 moved, forward references 211 → 200 (measured −11, exactly as
costed).**

Reading changed two of the six. **Two destinations proposed above were wrong and
would have been dependency-violating**: `def:quantum-bloch-group` before position
61 states the Bloch group ahead of `def:habiro-ring`, which it uses; and
`def:archimedean-realization-functor` before 10 puts the π∞ : 𝔸 → ℝ projection
ahead of `def:adelic-substrate`, its own domain. Both landed in corrected slots
instead. The `rem:motivic-mass-rationale` false locator ("the next subsection")
turns out to be a **prose** defect — no ordering fixes it without breaking the
adelic dependency.

**`def:categorical-instanton` was kept.** The move scores −3 at zero cost but
decapitates `sec:instanton`, the section named after it, and strands five
declared dependents. The right remedy is a section-level move of all 13 blocks,
which absorbs 2 of the 3 at zero cost and keeps the section whole — left for
fwr4, where the section-level questions live.

Three prose follow-ups the moves oblige, each a section intro announcing a block
that has now left: `orbital-symmetry-embedding-intro`,
`intro-archimedean-realization-kashaev`, and the `rem:motivic-mass-rationale`
locator. Also visible once the blocks are adjacent: `rem:beta-decay-energy-scale`
and `rem:energy-scale-planck` both derive E₀ ≈ 4.186 MeV from CAL-1/CAL-2.
