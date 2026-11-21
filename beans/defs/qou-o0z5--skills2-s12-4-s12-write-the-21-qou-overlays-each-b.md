---
# qou-o0z5
title: '[SKILLS2 S12] Write the 21 qou overlays'
status: todo
type: feature
priority: normal
tags:
    - migration
    - skills2
created_at: 2026-10-04T16:35:51Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-7vh1
---

From the SKILLS2 migration analysis (2026-10-04), story S12. Full report: docs/audits/2026-10-04-workplan-and-migration/SKILLS2_report.md.

4. S12 Write the 21 qou overlays. Each becomes `qou/<name>` with a base pointer, holding only qou data and examples. Done when: the union of base and overlay covers every line of the old qou copy (a line-coverage check), with zero math text changed. Size L. Depends on S11 and GAP-1.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
