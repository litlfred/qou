---
# qou-j5jq
title: 'Session: subagent persistent memory for qou + folio-assistant'
status: completed
type: epic
priority: normal
created_at: 2026-08-29T10:24:23Z
updated_at: 2026-08-29T10:25:12Z
---

Landed as two PRs, both markdown-only:

- litlfred/qou#5997 — `.claude/agents/` with `lean-verifier`, `corpus-grepper`,
  `compute-precision-auditor`, `convention-auditor`, `merge-coordinator`.
- litlfred/folio-assistant#149 — `platform-boundary-guard`,
  `ci-health-watcher`, `content-pipeline-navigator`.

Each agent carries `memory: project`, so it gets `.claude/agent-memory/<name>/`
whose MEMORY.md (first 200 lines / 25 KB) is injected into that subagent's
system prompt at start.

**The design call.** AGENTS.md is largely a record of its own stale figures
being corrected, so a memory holding *answers* would become the next entry in
that list. Every entry is therefore labelled exactly one of STABLE (path,
command, ruling) / TRAP (a failure mode with its evidence) / BASELINE (a number
stored with its command and date, never quoted as current).

**Verification** (no Lean, no content blocks, no computations/ touched; this
repo's workflows are dispatch-only so no run exists): all five qou agents
registered as available agent types as their commits landed; every MEMORY.md is
inside the injection cap, largest 200 lines / 10.7 KB (convention-auditor);
every agent name has a matching memory directory.

Upkeep is `qou-rpgi`.
