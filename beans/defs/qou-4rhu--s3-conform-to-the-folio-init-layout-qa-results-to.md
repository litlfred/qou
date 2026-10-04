---
# qou-4rhu
title: S3 Conform to the folio_init layout; QA results to the cat-harness qa-reports branch
status: todo
type: feature
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:15Z
updated_at: 2026-10-04T15:10:15Z
parent: qou-n4r9
---

Size M. Owner ruling 2026-10-04 (decision 11): QA sidecars use cat-harness qa-reports. README markers via readme:sync:check. Audit 786 .tex tables vs 444 table blocks and REPORT tables that exist only in .tex; never drop content.

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.
