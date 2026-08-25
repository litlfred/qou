---
# qou-r3sw
title: GUT SU(5) is near-absent from content/ — decide whether to author it from baez-huerta2010
status: todo
type: task
priority: normal
created_at: 2026-08-25T18:48:29Z
updated_at: 2026-08-25T18:49:15Z
parent: qou-8lxd
---

Owner flagged 2026-08-25: 'we are maybe missing SU(5) in qou'. Measured: grand-unification SU(5) has ~3 hits in content/, all bibliographic (references.ts, bib-qa-verifications.json). The instinct is correct.

DO NOT use arxiv-1205.4617v1 for this. Triaged 2026-08-25 (docs/audits/2026-08-25-octonion-division-algebra-upload-triage.md): it is a relabelling of textbook Georgi-Glashow, physics.gen-ph, whose own culminating gauge field contains no octonions, and whose central map sends 8 su(3) generators onto 7 octonion imaginaries by reusing e_3.

USE baez-huerta2010 (arXiv:0904.1556), which is ALREADY ingested at library/arxiv-0904.1556v2/, registered in references.ts, claim-verified in the source ledger, analysed in docs/audits/2026-07-31-sm-lit-analysis-bean-workplan.md §3, and cited by 3 content blocks. It does SU(5) in Lambda C^5 with hypercharge from the grading.

WHY THIS MIGHT MATTER BEYOND COMPLETENESS: the eightfold chapter's §8 item 2 (hypercharge Y) is OPEN -- the writhe map is falsified since p and n share Y=+1 with different writhes, and the chapter needs a second crossing invariant. SU(5)'s Lambda C^5 grading is exactly a source of Y. Whether QOU can reach that grading is the open question; noting the adjacency, NOT claiming it works.

HAZARD: docs/audits/2026-08-16-su-r-level-tower-gap-map.md:46 has an SU(5) row that is the WENZL LEVEL r=5 (z_5 = q^5/[5]_q), unrelated to grand unification. Same glyph, different object.
