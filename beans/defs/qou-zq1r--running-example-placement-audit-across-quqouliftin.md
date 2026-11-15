---
# qou-zq1r
title: Running-example placement audit across QU/QOU/lifting chapters
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-15T18:29:18Z
updated_at: 2026-10-04T15:24:15Z
parent: qou-mub3
---

Where the SU(2) example starts and where a new definition lacks its ex:*-su2 sibling.


2026-09-15 FINDING for the running-example audit: ex:quantum-universe-su2 carries lean.ref "qou:QOU.Examples.su2QuantumUniverse" and NO declaration of that name exists anywhere under content/ (grep over *.lean and *.ts: zero hits outside the manifest itself). The validator does not flag it because example blocks have optional Lean and the ref is not resolved for them. Either write the declaration (a `QuantumUniverse ℂ` instance for Rep(SU(2)) would be the honest object, and is not small) or drop the field; the new ex:su2-characters-and-quantum-dimension sits beside it with a real sibling (su2Character, three identities, sorry-free) and could host the running example's Lean going forward.


2026-09-15 CORRECTION of the entry immediately above, same hour: the claim "NO declaration of that name exists anywhere under content/" is FALSE. `su2QuantumUniverse` is defined in the block's own sibling content/quantum-observable-universe/quantum-universes/quantum-universe-su2.lean:57 (`def su2QuantumUniverse : SU2QuantumUniverseData`), which is exactly where the resolver looks first; my grep had been restricted to lean/QOU/ and never reached the sibling. The lean.ref is NOT dangling. What remains true and worth the audit's attention: the sibling packages the SU(2) data as an `SU2QuantumUniverseData` record rather than as an instance of the library structure `QOU.QuantumUniverse`, so the running example is not yet a `QuantumUniverse ℂ` in the sense of CategoricalFoundations.lean. Nothing else in that entry should be acted on.


2026-09-15 AUDIT WRITTEN: docs/audits/2026-09-15-running-example-placement-audit.md (branch claude/chi-arc-e3-followups-2026-09-15). Measured over every chapter manifest: 35 ex:*-su2 blocks; 14 were not listed in the interpreted block's examples[] — 13 wired on this branch (the 14th target, conj:tannaka-krein-isomorphism, has no examples[] field in the conjecture schema; the validator drops it with a warning, so it was reverted). Definitions without an SU(2) example: quantum-universes 9 of 15, quantum-observable-universes 31 of 37, lifting-and-descent 7 of 13 (47 total; three of them new on #7426 and covered by ex:su2-characters-and-quantum-dimension under its single interprets: edge). Recommendation (judgement, not enacted): write the five that touch second-year material first — def:categorical-point, def:categorical-reeb-derivation, def:fundamental-object, def:tannaka-dual, def:weight-decomposition. SECOND FINDING, substantive: the running example at q = 1 does NOT satisfy axiom 1 (temporal braiding) as written — prop:braiding-induced-ordering supplies the well-ordering ≺_c only for a NON-symmetric braiding, and Rep(SU(2))'s braiding is the flip (c² = id). The example that satisfies axiom 1 is Rep(SU_q(2)) at q ≠ 1 (R-matrix Ř = s + D(q), D(1) = 0, eigenvalues q, −q⁻¹); recorded as item (v) in ex:quantum-universe-su2 on this branch. The Lean sibling's SU2QuantumUniverseData carries no braiding field; a QuantumUniverse ℂ instance for the q ≠ 1 family is the Lean gap (not small).
