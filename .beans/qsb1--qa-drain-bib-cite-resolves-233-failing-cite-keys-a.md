---
# qsb1
title: 'QA drain: bib-cite-resolves — 233 failing cite keys across 233 blocks'
status: completed
type: task
priority: normal
tags:
    - qa-drain
    - lean-proof-progress-table
created_at: 2026-07-02T16:43:24Z
updated_at: 2026-07-02T16:43:24Z
---

Fix unresolvable cite keys flagged by the bib-cite-resolves criterion (233 sidecar fails, top offender chapters: qou-universes, particle-interactions, mass-theory). Mostly mechanical: typo'd keys vs content/schema/references.ts, or missing ref() entries. Small-swarm batches; verify keys case-sensitively; never edit references.bib directly.

**2026-07-03 DRAINED:** all 240 stale fail entries deleted + re-swept with the bridged checker: 884 pass / 0 fail. Root cause was the post-miga references.ts path bug (see scripts/setup-folio-assistant.sh bridge); no content edits were needed. Upstream checker fix belongs in folio-assistant (CONTENT_DIR vs content-root arg).
