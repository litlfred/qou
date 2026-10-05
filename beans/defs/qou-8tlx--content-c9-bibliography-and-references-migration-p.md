---
# qou-8tlx
title: '[CONTENT C9] Bibliography and references migration (plan + stories B1-B6)'
status: in-progress
type: feature
priority: normal
tags:
    - migration
    - content
created_at: 2026-10-05T16:00:50Z
updated_at: 2026-10-05T16:04:20Z
parent: qou-5lsb
---

Owner request 2026-10-05. Plan: docs/audits/2026-10-04-workplan-and-migration/C9_bib_references_migration_plan.md. Issue litlfred/qou#7528. B3/B4/B6 need the owner (human-judgement data moves; references.bib stops being committed). No reference entry, citation key or paper text changes.

B1 done 2026-10-05: run-validate-references.ts defaults --paper (identical output for all 5 papers: 11 errors / 177 warnings / 444 info; the citation check is folio-wide). The 11 errors are Lean -- Ref: keys absent from references.ts. Likely spelling variants of existing keys (would need a .lean comment edit — owner): neumann-zagier-1985→neumann-zagier1985, kassel1995quantum→kassel1995, ohtsuki2016-52→ohtsuki2016?. Missing works (would need new bib entries): bjornerbrenti2005, matsumoto1964, humphreys1990, tits1969, reid1991, bourbaki1968, hatcher2002, garoufalidis-zagier2021 (ambiguous vs garoufalidis2021/-zagier2023). Tracked with qou-e4eu.
