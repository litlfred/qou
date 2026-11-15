---
# neutron_proton_splitting
title: neutron proton splitting missing hypotheses
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-10-04T15:46:32Z
---

File: `folio/quantum-observable-universe/lean/QOU/Torsion/neutron_proton_splitting.lean`
The `neutron_proton_splitting` theorem is unprovable. Its class lacks constraints on the data fields and has `*_unconstrained_false` lemmas proving that the conclusion is independent and refutable from the provided data alone.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: 1be9bf9ec0 "resolve neutron_proton_splitting — add mass_formula + codata_agreement fields". FLAG: a codata_agreement field puts an empirical comparison inside a Lean class; 4 main commits



Also known as `npsp` (its former front-matter header id; the beans CLI uses the filename id `neutron_proton_splitting`). Recorded 2026-10-04.



## Reopened 2026-10-04 (review of PR #7496)

The closing evidence (1be9bf9ec0) resolves the missing hypotheses by adding a `codata_agreement` field, which places an empirical comparison inside a Lean class. The owner's rule keeps empirical values out of formal statements, so this is not closed on that evidence. Owner decides how the hypotheses should be supplied. No content was changed.
