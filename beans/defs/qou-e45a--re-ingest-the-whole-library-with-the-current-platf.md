---
# qou-e45a
title: Re-ingest the whole library with the current platform tool, then fix cited section paths
status: completed
type: task
created_at: 2026-11-15T11:14:16Z
updated_at: 2026-11-17T23:20:00Z
parent: qou-s4ws
---

Owner chose option 2 (2026-11-15, relayed by coordinator): re-ingest every existing library entry with ingest-document.ts at pin 82b389982, then rewrite the corpus citations of renumbered section files. Pilot: docs/audits/2026-11-15-library-reingest-pilot.md. Method: stage all, compare section text per entry, keep the current entry where re-ingest would lose text (OCR-only documents such as procrsoclondona92). Branch claude/library-reingest-kg-2026-11-15.

## Completed 2026-11-17
Done by #7925 (688 of 736 entries re-ingested, 43 cited section paths remapped) and #7938 (16 of the 48 kept entries retried; issue #7937 closed). Left on purpose: 26 entries whose old sections carry the author's arXiv LaTeX. Left by accident: `arxiv-2211.13362v2`, which hit the 2-hour limit in the vector-figures step. The dotless-i fix (`re.ASCII` in `_pdf_page_labels.roman_to_int`) was applied locally only and still needs to land in cat-harness-tools. Closed on the owner's pick in the library-ingestion thread (PR #8368).
