---
# qsb3
title: 'QA drain: refresh 174 stale .qa.json sidecars'
status: todo
type: task
priority: normal
tags:
    - qa-drain
    - lean-proof-progress-table
created_at: 2026-07-02T16:43:24Z
updated_at: 2026-07-02T16:43:24Z
---

source_hashes drift vs current .md/.ts. Refresh via bun run content/pipeline/qa-sweep.ts <path> --only <crit> after scripts/setup-folio-assistant.sh; cap <=10 per idle pass per AGENTS idle policy; chore(qa-sweep) commits naming producer+criterion+count.
