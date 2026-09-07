---
# qou-b6ti
title: 'Library: DeTurck-Gluck (0406276v1) sectionised to 4510 chars of 40 pages — the paper defining the EM-linking kernel is ungreppable'
status: todo
type: task
priority: normal
created_at: 2026-09-07T08:20:08Z
updated_at: 2026-09-07T08:55:48Z
---

Found 2026-09-07 by a six-path corpus-grep on the EM-linking front
(`qou-17mq`). Verified directly, not inferred.

`library/0406276v1/` is **DeTurck & Gluck, _The Gauss Linking Integral on the
3-Sphere and in Hyperbolic 3-Space_** — the paper this whole front reads its
kernel off. Thm 1(3) is where `phi_0(alpha) = -coth(alpha)/4pi` comes from;
it is cited at `content/schema/references.ts:10125`.

Measured on the committed tree:

    structure.json: pages 40, chars_total 4510, sections 1, toc_entries 1
                    pages_without_text 0, likely_scanned FALSE
    sections/:      sec-000-references.md (4888 B) + sec-000.jsonld only
    grep -rl coth library/0406276v1/  ->  NO HIT

~113 characters per page extracted, and the one section file is the
**bibliography** (pages 38-40 of 40). So corpus-grep **path 5 cannot be cited
as evidence about this kernel's literature at all** — a `sections/` grep for
`coth`, `linking integral`, or `hyperbolic Green` misses the defining source
and returns a clean bill.

## Why this is a NEW sub-class

Not the `thurston1978` held-but-partial class (a scanning failure). Here
`pages_without_text = 0` and `likely_scanned = false` — **the text extracts
fine; the SECTIONISER produced one section and kept only the references.**
The `ocr/` fourth tier does not help either: there is no `ocr/` directory,
because nothing thought this document needed one.

Detection shape worth generalising: `chars_total / pages` far below the
corpus norm while `likely_scanned` is false is a sectionisation failure that
no existing guard looks for. A tier-4 `ocr/` sweep will not catch it.

## Fix

Re-ingest this one PDF (`scripts/pdf-structure.py`). Highest-leverage single
library action on the EM-linking front: it is the only held primary source
for the kernel, and `qou-17mq` / `qou-zp6a` / `qou-o6ml` all reason from
Thm 1(3) without being able to grep it.

## Also observed, separately

`library/` INDEX.md is behind again: 655 directories, 609 rows, 23
duplicate-marked, leaving **23 real documents with no index row**. Tier 1 is
not a clean bill until `python3 scripts/summarize-library.py --apply` runs.
Recorded here rather than beaned separately — this is the recurring class
AGENTS.md already documents.


## 🛑 RETRACTED, same day: the cause is SECTIONING, not extraction. And the 8.9x was my measurement error.

The text above says `pypdf.extract_text()` fails on this PDF and that
`pdfminer.six` recovers 12.1x more, generalising to a class of 9 documents
"recoverable 8.9x by an extractor swap". **Both halves are wrong.**

**What I did wrong.** I compared pdfminer's RAW output against pypdf's
POST-SECTIONING output — `diagnostics.chars_total` is
`sum(s.n_chars for s in sections)`, not the page text. Measured raw-to-raw:

    doc                         sectioned   pypdf RAW  pdfminer RAW  ratio  sec  toc
    0406276v1                        4510       53937         54418  1.01x    1    1
    1-s20-0040938387900097-main      2079       27714         32996  1.19x    1    1
    67-6-1860                        1647        1632          3536  2.17x    1    0
    90-1-219                         4506       43222         48559  1.12x    3    3
    arxiv-nucl-th-0409040v2          2213       20713         20774  1.00x    1    2
    neumann-zagier-1985 (x2)         5437       55012         63793  1.16x    2    2
    procrsoclondona92                1597        1580          1716  1.09x    1    0
    the-period-matrix-of-brings      8674       28861         30543  1.06x    2    6

**pypdf reads these documents fine** — 1.00x to 1.19x of pdfminer on seven of
nine. The DeTurck-Gluck text it returns is clean and includes the defining
line verbatim. What is lost is lost afterwards: 53937 -> 4510 is **92%
discarded by `split_sections`**, and the same is true at 90%, 90%, 93%, 89%,
70% for the others.

**The actual bug**, at `scripts/pdf-structure.py:589` in `folio-assistant`:

    marks.sort(...)
    if not marks:
        whole = "\n".join(pages).strip()
        return [Section("sec-000-document", ..., whole)]     # keeps EVERYTHING
    for i, (pi, li, e) in enumerate(marks):                  # starts at marks[0]
        ...

Sections are emitted starting at the FIRST heading mark. **Text before
`marks[0]` is never emitted.** `0406276v1`'s heading inference finds exactly
one heading — "References", on page 38 of 40 — so pages 1-37 are silently
discarded.

The shape is perverse and is why this went unnoticed: a document with **zero**
headings hits the `if not marks` branch and keeps all its text, while a
document with **one late** heading loses everything before it. Correct when it
finds nothing; broken when it finds one thing.

**This also re-splits the class.** The two documents with `toc = 0` —
`procrsoclondona92` (1597 kept of 1580 raw) and `67-6-1860` (1647 of 1632) —
are NOT sectioning losses at all. They keep ~100% of what pypdf finds and are
genuinely low-text (scans); `procrsoclondona92` already has its `ocr/` tier,
exactly as AGENTS.md describes. So the sectioning-loss class is **7**, not 9,
and the extractor is not implicated in any of them.

**The fix I wrote first was the wrong fix and is reverted.** A pdfminer
fallback in `page_texts` would not have fired here anyway: its trigger reads
the RAW yield, which is healthy at 1348 chars/page.

**What the fix is:** emit a leading section for the text before `marks[0]`.
Whether that should apply corpus-wide is being measured — nearly every paper
has a title and abstract before its first heading, so this may mean the whole
library is losing its front matter, not just these seven. That measurement is
running; do not act on the "7" until it lands.

Detection shape, corrected: NOT chars/page (which measures the extractor).
The signal is **`chars_total` divided by the raw page-text total** — a
sectioning-retention ratio. Nothing in the corpus computes it today.
