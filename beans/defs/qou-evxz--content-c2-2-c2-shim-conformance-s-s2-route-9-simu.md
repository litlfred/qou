---
# qou-evxz
title: '[CONTENT C2] Shim conformance'
status: completed
type: feature
priority: normal
tags:
    - migration
    - content
created_at: 2026-10-04T16:35:55Z
updated_at: 2026-10-04T16:40:58Z
parent: qou-n4r9
---

From the CONTENT migration analysis (2026-10-04), story C2. Full report: docs/audits/2026-10-04-workplan-and-migration/CONTENT_report.md.

2. C2: Shim conformance (S; S2). - Route 9 simulator imports through `../../schema/builders` (one import line each). - Add `figure` to the shim. - Done when: `grep "folio-assistant/" folio//*.ts` hits only the shim and `pipeline/`; P-C holds with an exception for line 1 of those 9 files only.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Summary of Changes

Done 2026-10-04 (commit 3d64c59ae): line 1 of 9 simulator blocks now imports ../../schema/builders; the shim re-exports figure. The shim is the only folio/ file (outside folio/pipeline) naming the platform path. run-validate issue lines unchanged.
