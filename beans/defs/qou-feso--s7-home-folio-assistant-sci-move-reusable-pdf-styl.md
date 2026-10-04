---
# qou-feso
title: 'S7 (home: folio-assistant-sci) Move PDF generation tooling and reusable styling to sci'
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:17Z
updated_at: 2026-10-04T18:10:46Z
parent: qou-n4r9
---

Size S. Geometry, section formats, theorem styles, table style, Lean status marks move to folio-assistant-sci. qou's notation macros (frakr, ordw, bigbowtie, pp, yng, ...) stay with qou content.

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.


## Scope widened 2026-10-04 (owner): the tooling, not only the styling
Owner, verbatim: "pdf generation tooling needs to be migrated over to f-a-sci. there is already some stuff there in beans/tools."
- Platform: the TeX/PDF render group (16 files, folio-assistant-jh2j = TOOL 7/13 under d308) still lives in cat-harness; its declared target is folio-assistant-sci.
- qou: main.tex (styling; notation macros stay qou-side, verbatim), qou-all-tables.tex, standalone-index-of-definitions.tex, .github/docker plus paper-builder-image.yml, build.yml (calls the platform publish.yml), split-pdf-by-chapter.py, make-all-tables, check-reference-pdfs, fix-python-pdf-deps.sh, and the build-pdf command and skills.
- Inventory and plan: docs/audits/2026-10-04-workplan-and-migration/PDF_{inventory.tsv,report.md} (in progress).
- Claimed by session_01NdDGeP1SyShmoUssLuRZ91. Duplicate qou-eidn scrapped in its favour.
