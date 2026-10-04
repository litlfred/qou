---
# qou-bvp0
title: Two content-referenced simulator pages do not exist in either tree
status: todo
type: bug
priority: high
tags:
    - simulators
    - reorg-2026-10-04
created_at: 2026-09-26T10:38:50Z
updated_at: 2026-10-04T15:14:37Z
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
