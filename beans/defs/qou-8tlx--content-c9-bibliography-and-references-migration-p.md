---
# qou-8tlx
title: '[CONTENT C9] Bibliography and references migration (plan + stories B1-B6)'
status: todo
type: feature
priority: normal
tags:
    - migration
    - content
created_at: 2026-10-05T16:00:50Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-5lsb
---

Owner request 2026-10-05. Plan: docs/audits/2026-10-04-workplan-and-migration/C9_bib_references_migration_plan.md. Issue litlfred/qou#7528. B3/B4/B6 need the owner (human-judgement data moves; references.bib stops being committed). No reference entry, citation key or paper text changes.

B1 done 2026-10-05: run-validate-references.ts defaults --paper (identical output for all 5 papers: 11 errors / 177 warnings / 444 info; the citation check is folio-wide). The 11 errors are Lean -- Ref: keys absent from references.ts. Likely spelling variants of existing keys (would need a .lean comment edit — owner): neumann-zagier-1985→neumann-zagier1985, kassel1995quantum→kassel1995, ohtsuki2016-52→ohtsuki2016?. Missing works (would need new bib entries): bjornerbrenti2005, matsumoto1964, humphreys1990, tits1969, reid1991, bourbaki1968, hatcher2002, garoufalidis-zagier2021 (ambiguous vs garoufalidis2021/-zagier2023). Tracked with qou-e4eu.

B2 done 2026-10-05: scripts/check-references-bib.ts + Tool references-bib-check (exit 0/1/2, writes nothing). It reports real drift: committed references.bib (2026-08-16) 5,658 lines vs 8,920 generated. Regeneration waits (B6/owner). Uploads declaration dropped from B2: bib-qa-images is verification evidence, not an ingestion queue → B4. Platform finding: export-bibtex.ts hardcodes 'Quantum Observable Universe' in its header.

B5 done 2026-10-05: 4 read-only bib Tool nodes (references-pdf-check, references-library-sync-check, references-propose-from-library, reference-literals-dry-run); tools() = 234. Writing modes stay undeclared. Findings: sync-references-library --check is STALE (1 entry to add, 439 to refresh); drain-reference-literals dry run would route 25 literals across 11 files (a sweep → owner).

Owner rulings 1,2,4 applied 2026-10-05: references.bib regenerated (check clean); citations fixed (4 Lean comment key renames + 7 new entries; validate-references 11 errors -> 0); library sync applied ONLY for the 1 addition (ohara1991). NOT applied: sync --apply would drop 10 valid library links (dunfield2001, brown-zhang-2008, hadfield-krahmer-2005, feng-tsygan-1991, caldararu-willerton-2010, bghl-2017, trinh-2021, nest-tsygan-1995, dolgushev-rubtsov-2005, kontsevich-2003 — folders exist, ledger has no row) and swap 2 copies (neumann-zagier1985, riera-rodriguez-1992). Those 12 need the owner; sync --check stays red until then. reid1991 title is a placeholder (doi.org/Crossref blocked). Ruling 3 (attestations) next.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.
