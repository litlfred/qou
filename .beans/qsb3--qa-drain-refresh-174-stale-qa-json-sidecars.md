---
# qsb3
title: 'QA drain: refresh 174 stale .qa.json sidecars'
status: completed
type: task
priority: normal
tags:
    - qa-drain
    - lean-proof-progress-table
created_at: 2026-07-02T16:43:24Z
updated_at: 2026-07-05T05:05:00Z
---

source_hashes drift vs current .md/.ts. Refresh via bun run content/pipeline/qa-sweep.ts <path> --only <crit> after scripts/setup-folio-assistant.sh; cap <=10 per idle pass per AGENTS idle policy; chore(qa-sweep) commits naming producer+criterion+count.

> **Resolved 2026-07-05 (swarm 1).** 199 stale/missing .qa.json sidecars refreshed via qa-sweep. Merged in PR #3338.
