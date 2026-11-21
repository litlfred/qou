---
# qou-feso
title: 'S7 (home: folio-assistant-sci) Move PDF generation tooling and reusable styling to sci'
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:17Z
updated_at: 2026-11-21T13:00:00Z
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


## D2 measured 2026-10-04: which unicode maps are notation
qou main.tex has 133 \newunicodechar plus 163 \DeclareUnicodeCharacter maps (the 163 are accent maps U+00C0-017F, all typography). Classifying the 133 by what they emit: 92 symbol/operator, 31 Greek, 5 blackboard (ℝℂℕℚℤ), 1 calligraphic (𝓑 → \mathcal{B}, the Borromean braid word 𝓑₃), 1 fraktur (𝔙 → \mathfrak{V}). Only the last two encode a font choice. Default unless the owner overrides: 𝓑 and 𝔙 go verbatim into the qou notation fragment; everything else goes to the sci template.


## Q1 done 2026-10-04 (session_01NdDGeP1SyShmoUssLuRZ91)
folio/quantum-observable-universe/latex/notation-preamble.tex: the 32 notation lines, verbatim (each a line of main.tex's preamble, checked by line multiset), under an 8-line comment header. paper-feature-build reads it by default. Platform side: folio-assistant#2118 carries P1 (sci template), the fixed feature-build Tool and the skill loop. On qou the render completes, and the regenerated preamble equals qou's committed main.tex preamble as a line multiset. run-validate is unchanged (5 issues). Remaining: P2 and P5 (wiring), Q2 (build.yml), Q3 (skill forks), Q4 (legacy outputs; owner D4).

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
