---
# qou-4s33
title: '[CONTENT C7] Classify the data and stray files'
status: completed
type: feature
priority: normal
tags:
    - migration
    - content
    - needs-owner
created_at: 2026-10-04T16:35:57Z
updated_at: 2026-10-05T15:58:40Z
parent: qou-5lsb
---

From the CONTENT migration analysis (2026-10-04), story C7. Full report: docs/audits/2026-10-04-workplan-and-migration/CONTENT_report.md.

7. C7: Classify the data and stray files (S; owner). - Covers glossary/lean-coverage/foreshadows (regenerate), jwst, bach2013-as-library, visualizer-as-paper, `references.review.json`, `get_*.py`, `triage_stubs.ts`, `folio/package.json`, and the empty `bib-qa-images/`. - Done when: there is a ruling per row; nothing is deleted without confirmation; P-C holds.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.

Owner ruled 2026-10-05: all four groups approved. Regenerated foreshadows/glossary/lean-coverage .json; moved get_*.py ×3 + triage_stubs.ts to fsh-guts/deprecated/folio-strays/; JWST left byte-identical (provenance: from the internet, Kokorev et al. 2026); bib/references → migration plan requested (C5, qou-f2ri). bach2013/visualizer kept as papers. Record: docs/audits/2026-10-04-workplan-and-migration/C7_data_and_stray_files.md
