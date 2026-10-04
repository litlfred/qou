---
# qou-feso
title: 'S7 (home: folio-assistant-sci) Move PDF generation tooling and reusable styling to sci'
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:17Z
updated_at: 2026-10-04T18:25:48Z
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


## 2026-10-04: inventory and plan landed
docs/audits/2026-10-04-workplan-and-migration/PDF_{inventory.tsv,report.md}. Headline: no source preamble exists anywhere. The platform deleted cat-harness/latex/preamble.tex (34a70659c7, bean 0uu2) and the only live copy is lines 1-828 of qou main.tex, a generated file, so the qou PDF cannot be regenerated today. Moving the renderer first would create 4 core→sci import edges. Plan: platform P1 (recover the preamble into sci) … P5 (repair publish.yml); qou Q1 (verbatim notation fragment) … Q4 (retire legacy outputs). Owner decisions D1-D7; D1 (does sci own a print template, against the Task_Render text 'preamble belongs to the folio') gates P1.


## Owner decision D1, 2026-10-04: YES, split
folio-assistant-sci owns a generic paper print template: class and packages, geometry, titlesec formats, theorem styles, LeanBlueprint macros, Lean status marks and margin annotations, unicode safety maps, \defterm/\refterm, \proofstatuslegend. qou keeps a verbatim notation fragment: \bigbowtie, \varTheta, \pp, \yng, \unicode, and the 8 manifest macros. The sci Task_Render sentence "preamble belongs to the folio" is amended accordingly in P1. Parity: the sci template plus the qou fragment reproduce main.tex lines 1-828 as a line set. Next: P1 (platform), then Q1 (qou). D2-D7 still open.
