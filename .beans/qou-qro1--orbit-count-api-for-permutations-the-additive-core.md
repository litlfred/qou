---
# qou-qro1
title: 'Orbit-count API for permutations: the additive core, and the one classical lemma Mathlib lacks'
status: todo
type: task
priority: normal
created_at: 2026-09-04T02:38:34Z
updated_at: 2026-09-04T02:38:34Z
---

Owner-directed (2026-09-04), successor to qou-zrx2 follow-up (5). ClassicalTraceFloor and LeadingOrderTraceCoefficient take c(sigma_free)=2A and c(sigma_atom)=A+1 as stated hypotheses because Mathlib has no orbit-count API and no transposition-step lemma. QOU/MassTheory/OrbitCount.lean supplies the API: orbitDefect = #support - card cycleType (additive, unlike the count), proved additive over disjoint products and over lists; orbitDefect_swap = 1; sign = (-1)^orbitDefect, so the transposition step's PARITY is proved free. The FREE half of ClassicalTraceFloor's hypotheses is now closed outright (orbitCount_prod_of_disjoint_unit_defect: A disjoint blocks of defect 1 on 3A strands leave 2A orbits). REMAINING: the magnitude |Delta| <= 1 of the transposition step, which reduces via cycleOf splitting to the two-cycle JOIN -- Mathlib has the split direction (IsCycle.swap_mul) but not the merge. Carried as two sorry + -- Ref: [manuscript] per the state-and-queue disposition; consumed by nothing.
