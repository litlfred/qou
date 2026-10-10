---
# qou-6pk1
title: '[TARGET T2] Inject Lean packages'
status: todo
type: feature
priority: normal
tags:
    - migration
    - target
created_at: 2026-10-04T16:35:38Z
updated_at: 2026-10-04T16:36:15Z
parent: qou-ahxm
---

From the TARGET migration analysis (2026-10-04), story T2. Full report: docs/audits/2026-10-04-workplan-and-migration/TARGET_report.md.

T2 — Inject Lean packages. Size M. Depends on: T1. - Work: either a `contributes` call to `configureLeanPackages`, or a declarative `leanPackages` config field. The second is platform work for sci. - Done when: - `lean-file-exists` resolves through the Lake tree for a probe block with its sibling removed in a scratch copy. - The `.lean` bytes are unchanged.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
