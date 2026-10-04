---
# qou-eej4
title: '[CONTENT C1] Regenerate JSON-LD at the pin'
status: todo
type: feature
priority: normal
tags:
    - migration
    - content
created_at: 2026-10-04T16:35:54Z
updated_at: 2026-10-04T16:36:29Z
parent: qou-n4r9
---

From the CONTENT migration analysis (2026-10-04), story C1. Full report: docs/audits/2026-10-04-workplan-and-migration/CONTENT_report.md.

1. C1: Regenerate JSON-LD at the pin (S; depends on the S2 pin bump). - Run `gen-block-jsonld.ts`. - Done when: `--check` is green; each `.jsonld` diff touches only `@context`, or the file is new; P-C holds with zero `.ts` exceptions.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
