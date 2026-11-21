---
# qou-72py
title: '[SKILLS2 S10] Retire the stale forks'
status: todo
type: feature
priority: normal
tags:
    - migration
    - skills2
    - needs-owner
created_at: 2026-10-04T16:35:50Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-7vh1
---

From the SKILLS2 migration analysis (2026-10-04), story S10. Full report: docs/audits/2026-10-04-workplan-and-migration/SKILLS2_report.md.

2. S10 Retire the stale forks. Replace the 54 stale forks with pointers, after confirming that their diff against f-a is empty or that f-a is ahead. Done when: each removal is listed with its sizes and confirmed by the owner, and `skill_fetch` serves each name from f-a. Size M. Depends on S9.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
