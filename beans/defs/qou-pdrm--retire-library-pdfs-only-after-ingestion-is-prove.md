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
updated_at: 2026-10-12T21:00:00Z
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

## 2026-10-12 — exit criteria 2 and 3 measured (PR #7749, issue #7748)

**Criterion 2, the 2 sha mismatches: the records are right, and the
ingested bytes are present.** In both entries the QA report's mismatch is a
SECOND PDF sitting beside the recorded one, not the recorded file changed:

| entry | recorded file (sha matches) | extra file (different bytes) |
|---|---|---|
| `arxiv-1107.1559v1` | `1107.1559v1.pdf`, `b9f867ae…`, 145,704 B | `1107.1559.pdf`, `90d63f2e…`, 140,680 B |
| `arxiv-math-0405508v1` | `0405508v1.pdf`, `ef2e41cf…`, 223,914 B | `math0405508.pdf`, `90b403a5…`, 239,040 B |

Evidence the sections came from the recorded file: every `sections/*.md`
front matter carries `source_sha256` equal to the recorded sha prefix
(`b9f867ae7120eda6`, `ef2e41cf67f3a411`). qa.json itself lists the recorded
file of each entry as `verdict: ok`. Each extra file is the same arXiv
version (page-1 stamp `arXiv:1107.1559v1 … 8 Jul 2011`,
`arXiv:math/0405508v1 … 26 May 2004`) rendered on a different date (PDF
CreationDate 2011 vs 2018; 2008 vs 2019). No record change is needed. What
to do with the two extra files is open.

A third mismatch the QA report did not cover (it checked PDFs only):
`arxiv-2101.10016v16` records `2101.10016v16.pdf.txt`, sha `51d21209…`,
786,094 B; the committed file is 802,870 B. The committed blob has 16,776
CRLF line endings out of 17,296; with CRLF -> LF it hashes to exactly the
recorded sha and size. So the record describes the line-ending-normalised
text, not the stored bytes. Not changed.

**Criterion 3, `retiredCopy`: no such field exists yet.** Measured on
origin/main, on `cat/cat-harness/fsh-guts` (ddc90c3094), in cat-harness
(263d88e) and cat-harness-tools (2f7f3c2): zero occurrences outside this
bean. `retire-library-pdf.py` is not in either tools tree. There is no
field to repoint and no convention for its shape; the only fsh-guts
convention on record is the copy's PATH,
`fsh-guts/retired-pdfs/library/<entry>/<file>` on
`cat/cat-harness/fsh-guts`.
