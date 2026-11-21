---
# qou-36aa
title: '[SKILLS2 S15] Turn subagents and memory into nodes'
status: todo
type: feature
priority: normal
tags:
    - migration
    - skills2
created_at: 2026-10-04T16:35:53Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-7vh1
---

From the SKILLS2 migration analysis (2026-10-04), story S15. Full report: docs/audits/2026-10-04-workplan-and-migration/SKILLS2_report.md.

7. S15 Turn subagents and memory into nodes. The five actors go to `scenarios/actors`, their memory entries become `memory/` nodes, and `MEMORY.md` is generated. Done when: the entry count matches, the 200-line budget is met per agent, and no entry text is changed. Size M. Depends on S9.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## Measured 2026-10-04 (session_01NdDGeP1SyShmoUssLuRZ91); not started, two blockers
- The platform's `parseMemoryFile` (cat-harness/scripts/agent-memory.ts @26c5d37) splits qou's five MEMORY.md files into **117 labelled entries**: merge-coordinator 20, convention-auditor 14, corpus-grepper 19, compute-precision-auditor 20, lean-verifier 44 (trap 75 / stable 35 / baseline 7). Four non-entry sections (Session log ×3, corpus-grepper "Resolved topics") stay outside the generated region by design.
- Blocker 1: `agent-memory.ts` sets ROOT from `import.meta.dir`, so run from qou it reads the platform's memory/ and .claude/agent-memory/. Same downstream-discovery gap as kg-validate (T6, qou-bcuy). Possible workaround: a thin qou wrapper that calls the exported pure functions (`readMemoryNodes(dir)`, `memoryForAgent`, `renderEntries`, `spliceRegion`) with qou paths.
- Blocker 2: `MemoryNodeSchema` requires `measured {command, date, result}` on every BASELINE. qou's 7 baselines carry these in prose; pulling them into fields is a judgement, not a verbatim move. Needs an owner OK, or per-entry review.
- The 200-line budget: the entry bodies alone are 147/202/264/299/676 lines. Only merge-coordinator fits without the `<!-- detail -->` split, and choosing each split point is per-entry judgement (a split marker changes no text, but where it goes decides what an agent is shown).


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
