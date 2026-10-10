---
# qou-gjs2
title: 'T3: SP2 probe — identify geometric mechanism for hypersensitive spin part Im u > Re u at ~1e-8 anchor gap (resonance / fractional-part / moiré)'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T14:57:31Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-27 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DUPLICATE.** Duplicate of qou-4kr1, and resolved there: the ~1e-8-gap hypersensitivity is the c3 extractor's 1/u³ amplification, not a geometric mechanism.

Evidence: Created from the same workplan commit 856285eeb9 as 4kr1, about the same hypersensitivity crux. Probes 5e5cba591c/225ace3653. The reorg mapping marks it a stalled claim with an empty body.

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
