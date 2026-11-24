---
# qou-pmgw
title: Fix check-references-bib regeneration and summarize-library rewriting existing entries
status: completed
type: bug
priority: normal
created_at: 2026-11-15T11:14:16Z
updated_at: 2026-11-24T13:43:47Z
parent: qou-s4ws
---

Found 2026-11-15 by the stream-13 library session (PR #7869). (1) scripts/check-references-bib.ts can no longer regenerate references.bib at platform pin 82b389982 (the platform exporter no longer runs when imported), so new entries were added to references.bib by hand. (2) scripts/summarize-library.py --apply rewrites about 7,600 files in existing entries, some for the worse; the session reverted those each time and kept only new entries' summaries.

Closed post-merge: landed on origin/main in PR #9342 (74429fd5f00).
