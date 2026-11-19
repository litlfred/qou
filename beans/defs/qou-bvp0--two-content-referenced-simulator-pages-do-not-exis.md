---
# qou-bvp0
title: Two content-referenced simulator pages do not exist in either tree
status: completed
type: bug
priority: high
tags:
    - simulators
    - reorg-2026-10-04
created_at: 2026-09-26T10:38:50Z
updated_at: 2026-11-19T16:48:42Z
parent: qou-n4r9
---

**Measured 2026-09-26.** Two simulator pages are referenced from content blocks
and exist in **neither** `qou/simulators/` nor the platform clone's copy.

| page | in `qou/simulators/` | in platform clone | content files referencing it |
|---|---|---|---|
| `descent_rate_probe.html` | **no** | **no** | 2 |
| `multi_level_jet_sum.html` | **no** | **no** | 2 |

Method: every `[a-z_]+\.html` token in `content/**/*.ts`, intersected against
`ls simulators/`. Find the referrers with
`grep -rl 'descent_rate_probe.html' content/`.

## Correction to my own first pass, recorded because it inverted the finding

I first grepped `kind: *"simulator"` across `content/` and got **0 files**, and
was one step from reporting "no content block references any simulator at all".
That pattern is simply wrong: the real spellings are `sim:` (16 files) and
`simulator:` (5 files). Simulators ARE wired in; the defect is two missing files,
not an unwired subsystem. A zero from a grep is a statement about the grep until
the pattern is checked against a known positive.

## Scope

The other nine referenced pages resolve. `double_slit.html` and `empty.html`
exist but are referenced by nothing — not a defect, noted so a later sweep does
not "fix" them by deletion without asking.

## What is NOT claimed

Whether these two pages were deleted, renamed, or never written is **unknown** —
no git archaeology was done. That determines the fix (restore vs re-point the
reference vs drop the block's simulator field) and it is the first thing to
measure. No fix is proposed here.

## Git archaeology & owner ruling (2026-11-15, `Q-N4R9-1 = 2`)

- **Git archaeology (`git log --all -- "*descent_rate_probe*" "*multi_level_jet_sum*"`):**
  - Neither `simulators/descent_rate_probe.html` nor `simulators/multi_level_jet_sum.html` has **ever** existed in git history.
  - Both simulator blocks (`folio/quantum-observable-universe/lifting-and-descent/descent-rate-probe-sim.ts` and `folio/quantum-observable-universe/lifting-and-descent/multi-level-jet-sum-sim.ts`, referenced by `descent-rate-probe.ts` and `multi-level-jet-sum.ts`) were introduced in commit `114b24ba5b` (`2026-06-14`, *"feat(content): migrate lifting-and-descent (Ch 10) to TypeScript schema"*) explicitly tagged `"todo-html"` with comments noting *"Simulator HTML not yet built; tagged 'todo-html'"*.
  - `scripts/run-validate.ts` surfaces both as intentional deferred warnings (`⚠ Simulator asset deferred: ... Tagged todo-html, so this is an intended stub`).
- **Owner ruling (`Q-N4R9-1 = 2`, 2026-11-15):** Keep the 2 simulator blocks as `"todo-html"` deferred stubs until the HTML simulators are authored; kept `status: in-progress` on this bean to track the deferred HTML assets.



## Completed (2026-11-19)
Completed: built and validated `simulators/descent_rate_probe.html` and `simulators/multi_level_jet_sum.html` (`run-validate.ts` reports `0` deferred simulator warnings across all `3,635` blocks).
