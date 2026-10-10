---
# qou-4ads
title: '[REST S-REST-3] Register or route the 248 unregistered library entries and dedupe codata'
status: todo
type: feature
priority: normal
tags:
    - migration
    - rest
created_at: 2026-10-04T16:35:58Z
updated_at: 2026-10-04T16:36:33Z
parent: qou-5lsb
---

From the REST migration analysis (2026-10-04), story S-REST-3. Full report: docs/audits/2026-10-04-workplan-and-migration/REST_report.md.

3. S-REST-3: Register or route the 248 unregistered library entries and dedupe codata. - Scope: 232 get `references.ts` entries (link-into-structure); 16 are owner-review; codata comes from sci. - Done when: zero unregistered entries; codata values are blob-equal to sci before the qou copy is dropped. - Size M. Depends on: S-REST-1.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.
