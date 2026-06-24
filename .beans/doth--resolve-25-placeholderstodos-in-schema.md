---
# doth
title: Resolve 25 placeholders/TODOs in schema
status: todo
type: task
priority: normal
created_at: 2026-06-22T02:25:52Z
updated_at: 2026-06-24T00:06:39Z
---

resweep 2026-06-22: honest counter = 22 actionable (claimed 25) via scripts/count-actionable-placeholders.ts.

resweep 2026-06-23 (#2637): honest actionable = 22 (claimed 25) — roughly ACCURATE; the one genuinely large backlog item. See docs/audits/2026-06-23-placeholder-bean-resweep.md.

finding 2026-06-24: the ~7 actionable items are all bib-metadata verification TODOs in content/schema/references.ts (verify exact title/authors/pages/DOI for: kashiwara Duke 1990 + CMP refs, Carter arxiv math/0008040, Pawlowski-Leitner 2009, Chlouveraki HDR 2016). These need DOI/arxiv/source lookup — BLOCKED in this sandbox (agent proxy denies doi.org/api.crossref.org/export.arxiv.org with 403; only package registries are allowlisted). Anti-fabrication bib discipline forbids guessing the metadata, so these are bib-human-review items (route via local/bib-human-review, assign @litlfred), NOT a mechanical drain. Not drainable without web access. (The '22' counts placeholder doc-tokens; real TODO refs ≈ 5-7.)
