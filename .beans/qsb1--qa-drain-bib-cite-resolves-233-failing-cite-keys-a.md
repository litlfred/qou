---
# qsb1
title: 'QA drain: bib-cite-resolves — 233 failing cite keys across 233 blocks'
status: todo
type: task
priority: normal
tags:
    - qa-drain
    - lean-proof-progress-table
created_at: 2026-07-02T16:43:24Z
updated_at: 2026-07-02T16:43:24Z
---

Fix unresolvable cite keys flagged by the bib-cite-resolves criterion (233 sidecar fails, top offender chapters: qou-universes, particle-interactions, mass-theory). Mostly mechanical: typo'd keys vs content/schema/references.ts, or missing ref() entries. Small-swarm batches; verify keys case-sensitively; never edit references.bib directly.
