---
# qou-sibdup
title: 'Detector: a content-block theorem assuming what a sibling block proves'
status: in-progress
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T04:40:00Z
updated_at: 2026-11-21T18:00:00Z
parent: qou-5vkl
---

A defect class §0a makes structurally likely and nothing currently looks for.

## The instance that found it

`spectral-half-line.lean` carried

```lean
(hw : ∀ i, ‖Z.eigenvalues i‖ = Z.q ^ (1 / 2 : ℝ))
```

as a hypothesis of `reeb_spectrum_on_critical_line`. That statement is exactly
the conclusion of `hasse_weil_bound`, **proved** in `hasse-weil-bound.lean` from
`[IsWeilZeta Z]` — the file next to it, in the same chapter.

Neither file was wrong. Content-block siblings are outside the package globs and
cannot import one another, so `spectral-half-line.lean` had no way to reach the
proof and assuming it was the only option available. The defect lived in the gap
between two correct files.

Fixed for this instance (see `qou-qspc`) by lifting the shared core into
`QOU/AlgebraicSubstrate/WeilZeta.lean` and importing it from both.

## Why no existing checker sees it

- The `.qa.json` sidecars audit **one block at a time**. A hypothesis that is
  redundant only relative to a sibling is invisible to every per-block criterion.
- `lean-vacuity-axiom-audit` looks for content-free carriers and vacuous
  conclusions. This hypothesis is neither: it is a real, satisfiable, correctly
  stated proposition. It is simply already proved elsewhere.
- `proof-gap-audit` chases missing steps, not redundant ones.

The signature is a *pair*, so a detector has to be cross-file by construction.

## Proposed check

Within one chapter, for each content-block `.lean`: collect the explicit
hypotheses of every `theorem`, and the conclusions of every `theorem` in sibling
blocks. Flag a hypothesis that matches a sibling's conclusion up to alpha-
renaming and the binder's own parameters.

Two cautions from the worked case:

1. **Syntactic match is enough to *flag*, not to *fix*.** The two statements
   here were textually identical; a real match may differ by argument order or a
   coercion. High recall with an agent verdict is the right shape — the same
   posture as the vacuity ledger.
2. **The fix is a library lift, not a hypothesis deletion.** Deleting `hw`
   without moving `IsWeilZeta` would not have compiled. Any report should say
   which declaration would have to move, since that is the whole cost.

## Scope

Unmeasured. The q-geometric-langlands chapter yielded one instance from three
blocks, which says nothing about the rate — one hit in a chapter an agent had
just spent a session inside is exactly the sample most likely to over-estimate.
Measure before quoting a number.

## 2026-11-21 (thread: Design the remaining Lean vacuity detectors)

Advisory script scripts/lean-sibling-hypothesis-audit.py in PR #8919, with specificity filter; corpus 0 matches (232 with --unfiltered), worked hasse_weil_bound case pinned in --selftest. No ledger category, per owner ruling 2026-11-21. Open until #8919 merges.
