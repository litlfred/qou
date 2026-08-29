---
# qou-rpgi
title: Maintain the subagent MEMORY.md files as work lands
status: todo
type: task
priority: normal
created_at: 2026-08-29T10:24:44Z
updated_at: 2026-08-29T10:58:40Z
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

**First firing, 2026-08-29** — one turn after this bean was created.

`qou-961o` landed (`ae8098c3`), renaming the three convention-C `markovZ`.
That staled `convention-auditor`'s markovZ BASELINE exactly as designed. Re-ran
`scripts/lean-markov-convention-audit.py` rather than copying main's prose, and
the re-measurement found something the rename's own resolution note missed:

**`markovZC` (upper C) is convention C; `markovZc` (lower c) is convention D.**
One letter's case, opposite meanings, `0.4993203342` vs `0.6126880371` at the
proton q₀. `AGENTS.md` line 2060 claimed "one convention, no collision" — that
is measurably false and is corrected on this branch.

Recorded as a TRAP; baseline refreshed; `q0-pin-migration.md` split out to keep
MEMORY.md inside the 200-line injection cap.

Merged as #6010 (5ed07e4). Bean returns to `todo` — this is a standing obligation, not a task that completes.

Left open for the author: whether `markovZc` or `markovZC` is the one to rename. Flagged on #5999, not actioned.
