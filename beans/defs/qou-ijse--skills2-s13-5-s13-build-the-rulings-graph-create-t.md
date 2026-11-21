---
# qou-ijse
title: '[SKILLS2 S13] Build the rulings graph'
status: todo
type: feature
priority: normal
tags:
    - migration
    - skills2
    - upstream-fa
created_at: 2026-10-04T16:35:52Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-7vh1
---

From the SKILLS2 migration analysis (2026-10-04), story S13. Full report: docs/audits/2026-10-04-workplan-and-migration/SKILLS2_report.md.

5. S13 Build the rulings graph. Create the node kind (ch) and seed qou `rulings/` with the 24 rulings above. Done when: every "OWNER RULING" marker in AGENTS.md resolves to a node, and verbatim quotes are byte-equal to their sources. Size M. Depends on GAP-2.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Partial overlap: since 2026-11-21 the owner's rulings live in `docs/coordination/owner-rulings.md` (owner directive: no project memory). A rulings graph node kind does not exist yet; that ledger is the natural seed. Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
