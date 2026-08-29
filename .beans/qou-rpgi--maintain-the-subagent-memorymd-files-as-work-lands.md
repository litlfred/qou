---
# qou-rpgi
title: Maintain the subagent MEMORY.md files as work lands
status: todo
type: task
priority: normal
created_at: 2026-08-29T10:24:44Z
updated_at: 2026-08-29T10:25:12Z
parent: qou-j5jq
---

Standing obligation created by `qou-j5jq`, not a scheduled task.

The eight MEMORY.md files decay the way any hand-kept record here decays. Two
rules, both stated in AGENTS.md §"Subagents with persistent memory":

1. A session that establishes a durable fact in one of these areas — a detector
   blind spot, a producer that refuses by design, a gate that cannot fire —
   adds it as a **TRAP** in the same PR.
2. A session that re-measures a **BASELINE** updates that entry with the fresh
   number and date rather than leaving the old one beside it.

A memory file that only accretes becomes the thing it exists to prevent.

Keep MEMORY.md under 200 lines — it is the injected entry point. Split detail
into sibling files the agent reads on demand;
`.claude/agent-memory/compute-precision-auditor/producer-health.md` is the
worked example.
