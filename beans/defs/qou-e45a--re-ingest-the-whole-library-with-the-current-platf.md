---
# qou-e45a
title: Re-ingest the whole library with the current platform tool, then fix cited section paths
status: in-progress
type: task
created_at: 2026-11-15T11:14:16Z
updated_at: 2026-11-15T11:14:16Z
parent: qou-s4ws
---

Owner chose option 2 (2026-11-15, relayed by coordinator): re-ingest every existing library entry with ingest-document.ts at pin 82b389982, then rewrite the corpus citations of renumbered section files. Pilot: docs/audits/2026-11-15-library-reingest-pilot.md. Method: stage all, compare section text per entry, keep the current entry where re-ingest would lose text (OCR-only documents such as procrsoclondona92). Branch claude/library-reingest-kg-2026-11-15.
