---
# qou-pjfi
title: '[REST S-REST-1] Declare qou''s undeclared directories'
status: todo
type: feature
priority: normal
tags:
    - migration
    - rest
created_at: 2026-10-04T16:35:58Z
updated_at: 2026-10-04T16:36:32Z
parent: qou-n4r9
---

From the REST migration analysis (2026-10-04), story S-REST-1. Full report: docs/audits/2026-10-04-workplan-and-migration/REST_report.md.

1. S-REST-1: Declare qou's undeclared directories. - Scope: add `docs` (split into `notes`/`archive` context kinds), `uploads`, `schemas` and `figures` entries to `qou.json`. - Done when: `harness:dirs:check` and `audit:coverage` list them; `git diff --stat` touches only `qou.json`. - Size S. Depends on: platform pin move (qou-8321).

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
