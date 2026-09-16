---
# qou-zq1r
title: Running-example placement audit across QU/QOU/lifting chapters
status: todo
type: task
priority: normal
created_at: 2026-09-15T18:29:18Z
updated_at: 2026-09-15T23:02:27Z
parent: qou-dgce
---

Where the SU(2) example starts and where a new definition lacks its ex:*-su2 sibling.


2026-09-15 FINDING for the running-example audit: ex:quantum-universe-su2 carries lean.ref "qou:QOU.Examples.su2QuantumUniverse" and NO declaration of that name exists anywhere under content/ (grep over *.lean and *.ts: zero hits outside the manifest itself). The validator does not flag it because example blocks have optional Lean and the ref is not resolved for them. Either write the declaration (a `QuantumUniverse ℂ` instance for Rep(SU(2)) would be the honest object, and is not small) or drop the field; the new ex:su2-characters-and-quantum-dimension sits beside it with a real sibling (su2Character, three identities, sorry-free) and could host the running example's Lean going forward.


2026-09-15 CORRECTION of the entry immediately above, same hour: the claim "NO declaration of that name exists anywhere under content/" is FALSE. `su2QuantumUniverse` is defined in the block's own sibling content/quantum-observable-universe/quantum-universes/quantum-universe-su2.lean:57 (`def su2QuantumUniverse : SU2QuantumUniverseData`), which is exactly where the resolver looks first; my grep had been restricted to lean/QOU/ and never reached the sibling. The lean.ref is NOT dangling. What remains true and worth the audit's attention: the sibling packages the SU(2) data as an `SU2QuantumUniverseData` record rather than as an instance of the library structure `QOU.QuantumUniverse`, so the running example is not yet a `QuantumUniverse ℂ` in the sense of CategoricalFoundations.lean. Nothing else in that entry should be acted on.
