---
# qou-pdrm
title: Retire the library PDFs from main only after doc ingestion is proven
status: todo
type: task
priority: normal
tags:
    - library
    - ingestion
parent: qou-1qhv
blocked_by:
    - qou-79vu
created_at: 2026-10-10T18:40:00Z
updated_at: 2026-10-10T18:40:00Z
---

## Ruling

Owner, 2026-10-10: *"once we are sure doc ingestion tools are OK, we can
remove. need to make sure doc ingestion works well first."* And earlier the
same day: *"for now: dont delete the already download pdfs, put in fsh-guts
(with a QA report). we still need to test for a bit."*

So no PDF leaves `library/` on main until the ingestion pipeline is shown to
work well. Until then the PDFs stay on main AND have a copy in fsh-guts.

## Done so far

- The 718 PDFs under `library/` on main `ee2b758144` (637 MB) are held on
  `cat/cat-harness/fsh-guts` at commit `122b1f39c8`, under
  `fsh-guts/retired-pdfs/library/<entry>/<file>`. These are the same git
  blobs as on main, so the copy adds no storage.
- `fsh-guts/retired-pdfs/QA-REPORT.md` and `qa.json` (`retired-pdf-qa/v1`):
  716 PDFs match the sha256 recorded in `structure.json`. 2 do not, which
  means the file present is not the one that was ingested:
  `arxiv-1107.1559v1` and `arxiv-math-0405508v1`. 5 were renamed but have a
  matching sha: `arxiv-0802.1072v2`, `1202.5547v1`, `1406.7337v4`,
  `2406.05311v1` and `math-0606435v2`. Locators: 526 arXiv, 63 DOI only, 129
  none.
- Tool written but NOT applied: `cat-harness-tools/scripts/retire-library-pdf.py`
  (not yet in a PR). It retires a PDF only if the entry is processed, the
  sha matches and there is a locator. In the PDF's place it writes
  `source.materialization.json` (`folio-materialization/v1`, state
  `referenced`). `gen-library-jsonld.ts` then carries that record into the
  entry's manifest, and every derived file stays.

## Exit criteria (proposed; owner to confirm)

1. The ingestion tools are judged OK: section text, the LaTeX overlay
   (qou-79vu), blocks and the KG for the library re-run cleanly.
2. Re-ingest or explain the 2 sha mismatches.
3. Point `retiredCopy` at the fsh-guts copy, not at a main commit.
4. The library viewer reuses the litlfred/who-iris PDF loader: a viewer for
   locally materialized copies, a link only for remote papers (because of the
   XSS limits of GitHub Pages).
5. Do not touch the Kohno 1987 and Drinfeld 1991 scans while qou PR #7637 is
   open.

Only then run `retire-library-pdf.py --apply`.
