---
# qou-be7o
title: '[REST S-REST-2] Library archival bytes decision'
status: todo
type: feature
priority: normal
tags:
    - migration
    - rest
    - needs-owner
created_at: 2026-10-04T16:35:58Z
updated_at: 2026-10-04T16:36:32Z
parent: qou-5lsb
---

From the REST migration analysis (2026-10-04), story S-REST-2. Full report: docs/audits/2026-10-04-workplan-and-migration/REST_report.md.

2. S-REST-2: Library archival bytes decision. - Scope: write a `folio-materialization/v1` record with sha256 for each of the 719 PDFs; the owner picks keep, release assets, LFS or history rewrite. - Done when: every record's digest matches the file before any removal, the derived `sections/`/`blocks/` tree hash is unchanged, and `bun run health` repository-size is below major (or the owner accepts major). - Size M. Depends on: owner ruling.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
