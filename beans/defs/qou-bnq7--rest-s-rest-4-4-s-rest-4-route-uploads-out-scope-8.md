---
# qou-bnq7
title: '[REST S-REST-4] Route uploads/ out'
status: todo
type: feature
priority: normal
tags:
    - migration
    - rest
created_at: 2026-10-04T16:35:59Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
---

From the REST migration analysis (2026-10-04), story S-REST-4. Full report: docs/audits/2026-10-04-workplan-and-migration/REST_report.md.

4. S-REST-4: Route uploads/ out. - Scope: 8 platform PDFs → cat-harness library, 7 WHO → smart-base. - Done when: every PDF's sha256 is found in its destination entry's record, and qou `uploads/` holds only the keep marker. - Size S.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Measured: `uploads/` on main holds only `.gitignore` (the keep marker). The local half of the done-when is met. NOT checked: whether each PDF's sha256 is recorded at its destination (cat-harness library, smart-base). Close once that parity is shown.
