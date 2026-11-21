---
# qou-tzej
title: '[TARGET T7] Move qou-specific CI and BPMN (item 14) out of the platform'
status: todo
type: feature
priority: normal
tags:
    - migration
    - target
created_at: 2026-10-04T16:35:40Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-k3er
---

From the TARGET migration analysis (2026-10-04), story T7. Full report: docs/audits/2026-10-04-workplan-and-migration/TARGET_report.md.

T7 — Move qou-specific CI and BPMN (item 14) out of the platform. Size M. Depends on: T6. - Done when: - The moves are pure renames. - `check:workflow-coverage` is green in both repositories.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
