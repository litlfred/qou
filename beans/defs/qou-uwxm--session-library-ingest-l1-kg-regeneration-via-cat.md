---
# qou-uwxm
title: 'Session: library ingest + L1 KG regeneration via cat-harness-tools (#7608, superseded)'
status: scrapped
type: epic
created_at: 2026-10-10T13:24:05Z
updated_at: 2026-11-17T23:20:00Z
---

Recorded 2026-11-17. This epic and its children (`qou-15n1` driver, `qou-v9av` ingest 10 uploads + 3 methodology papers, `qou-0nko` methodology note, `qou-i0xl` regenerate L1 KG, `qou-np0p` re-ingest existing PDFs) existed only on branch `claude/busy-wright-hntswj` and never reached the bean store. PR #7608 was closed as superseded on 2026-10-12 (issue #7735):

- the 3 methodology papers went to folio-assistant-sci (#23, merged);
- the 10 uploads were already in cat-harness's library, byte-identical;
- the driver `scripts/library-ingest.ts` is replaced by `cat ingest --instance` (cat-harness-tools#169).

The re-ingest goal (`qou-np0p`, `qou-i0xl`) was carried out under `qou-e45a` by #7925 and #7938. The branch is kept as a record.
