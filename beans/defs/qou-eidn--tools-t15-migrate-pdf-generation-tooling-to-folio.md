---
# qou-eidn
title: '[TOOLS T15] Migrate PDF generation tooling to folio-assistant-sci'
status: scrapped
type: feature
priority: normal
tags:
    - migration
    - tools
    - upstream-fa
created_at: 2026-10-04T18:10:25Z
updated_at: 2026-10-04T18:10:46Z
parent: qou-k3er
---

Owner, 2026-10-04: "pdf generation tooling needs to be migrated over to f-a-sci. there is already some stuff there in beans/tools." Earlier ruling: the legacy qou PDF build is not a qou concern, but "some stylings of legacy pdf build can be moved to folio-assistant-sci to get nice PDF print".

Platform side: the TeX/PDF render group (16 files, bean folio-assistant-jh2j, TOOL 7/13 under d308) still lives in cat-harness, and its declared target is folio-assistant-sci.
qou side: main.tex (preamble/styling), qou-all-tables.tex, standalone-index-of-definitions.tex, .github/docker plus paper-builder-image.yml, build.yml (calls the platform publish.yml), split-pdf-by-chapter.py, make-all-tables, check-reference-pdfs, fix-python-pdf-deps.sh, and the build-pdf command and skills.

Inventory and plan: docs/audits/2026-10-04-workplan-and-migration/PDF_{inventory.tsv,report.md} (in progress).

Owner hard rule: no math or physics content changes. Notation macros in main.tex are carried verbatim, never edited. Done-when must include a render-parity check.


Scrapped the same minute it was created: it duplicates qou-feso (S7), which a check-before-create should have found. qou-feso was widened to carry this scope and the owner's instruction.
