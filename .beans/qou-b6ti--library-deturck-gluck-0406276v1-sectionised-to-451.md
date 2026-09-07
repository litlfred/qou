---
# qou-b6ti
title: 'Library: DeTurck-Gluck (0406276v1) sectionised to 4510 chars of 40 pages — the paper defining the EM-linking kernel is ungreppable'
status: todo
type: task
priority: normal
created_at: 2026-09-07T08:20:08Z
updated_at: 2026-09-07T08:20:40Z
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
