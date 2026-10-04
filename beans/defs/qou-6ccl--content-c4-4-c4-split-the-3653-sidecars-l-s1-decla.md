---
# qou-6ccl
title: '[CONTENT C4] Split the 3,653 sidecars'
status: todo
type: feature
priority: normal
tags:
    - migration
    - content
    - needs-owner
created_at: 2026-10-04T16:35:55Z
updated_at: 2026-10-04T16:36:30Z
parent: qou-5lsb
---

From the CONTENT migration analysis (2026-10-04), story C4. Full report: docs/audits/2026-10-04-workplan-and-migration/CONTENT_report.md.

4. C4: Split the 3,653 sidecars (L; S1 declares `test/attestations` + `qa` storage; owner confirm for removal). - Derived: `qa:refresh` → `qa:publish` to qou's qa-reports branch. - Judgements: `qa:attestations:migrate`, verbatim. - Done when: the attestation store holds exactly 126,315 agent+human entries; the 128 null entries have an owner ruling; `qa:verify-moved` answers IDENTICAL; `qa:attestations:migrate:check` exits 0; P-C holds.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
