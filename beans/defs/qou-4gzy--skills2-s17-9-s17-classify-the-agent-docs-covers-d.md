---
# qou-4gzy
title: '[SKILLS2 S17] Classify the agent docs'
status: in-progress
type: feature
priority: normal
tags:
    - migration
    - skills2
created_at: 2026-10-04T16:35:53Z
updated_at: 2026-10-04T17:35:38Z
parent: qou-7vh1
---

From the SKILLS2 migration analysis (2026-10-04), story S17. Full report: docs/audits/2026-10-04-workplan-and-migration/SKILLS2_report.md.

9. S17 Classify the agent docs. Covers `docs/coordination` (198), the 3 handover dirs (9), `agent-briefs` (4) and `.claude/validation-errors-handoff.md`. Classify only, per decision 10. Done when: there is a classification TSV and no file is moved. Size S.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Owner ruling 2026-10-04: split docs/

- Outstanding-work docs (docs/backlog/, plans, attack-option lists) go to beans (agent work) or todos/ (the owner's own work).
- Math notes (derivation notes, cheat sheets, proofs, refutations) are NOT todos: filing them there would count finished derivations as open work. They wait for a working-notes graph kind, filed upstream as folio-assistant bean folio-assistant-8npa (child of 8jt6), or move into folio/ blocks only by an owner-approved verbatim move.
- Handoffs and coordination logs go to beans/notes; status surveys to beans/surveys (classify first, move by rename after approval).

Claimed 2026-10-04 by session_01NdDGeP1SyShmoUssLuRZ91 on branch claude/migration-wave6-2026-10-04.
