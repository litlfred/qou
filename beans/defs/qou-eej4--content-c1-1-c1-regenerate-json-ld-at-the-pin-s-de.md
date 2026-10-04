---
# qou-eej4
title: '[CONTENT C1] Regenerate JSON-LD at the pin'
status: completed
type: feature
priority: normal
tags:
    - migration
    - content
created_at: 2026-10-04T16:35:54Z
updated_at: 2026-10-04T16:40:57Z
parent: qou-n4r9
---

From the CONTENT migration analysis (2026-10-04), story C1. Full report: docs/audits/2026-10-04-workplan-and-migration/CONTENT_report.md.

1. C1: Regenerate JSON-LD at the pin (S; depends on the S2 pin bump). - Run `gen-block-jsonld.ts`. - Done when: `--check` is green; each `.jsonld` diff touches only `@context`, or the file is new; P-C holds with zero `.ts` exceptions.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Summary of Changes

Done 2026-10-04 (commit 6cbed9f75): gen-block-jsonld at pin 26c5d37 wrote 3,613 files; parsed before/after, the only differing key is @context. No .ts/.md/.lean changed.
