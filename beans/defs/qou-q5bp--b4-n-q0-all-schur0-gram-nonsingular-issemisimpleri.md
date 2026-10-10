---
# qou-q5bp
title: 'B4: [n]_q!≠0 ⟹ all Schur≠0 ⟹ Gram nonsingular ⟹ IsSemisimpleRing H_n(q). Discharges WenzlCriterion as a THEOREM (deep brick, Mathlib IsSemisimpleRing)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:21:38Z
updated_at: 2026-10-04T15:16:36Z
---


MATHLIB ANCHOR (probed 2026-07-24): the route is `isSemisimpleRing_iff_jacobson`
(Mathlib RingTheory/Artinian/Module.lean:647): IsSemisimpleRing R ↔ Ring.jacobson R = ⊥.
So B4 = prove Ring.jacobson (H_n(q)) = ⊥ from Gram/form nondegeneracy. NOTE: there is
NO general "nondegenerate trace form ⟹ semisimple" in Mathlib — traceForm_nondegenerate
(Trace/Basic.lean:496) is SEPARABLE FIELD EXTENSIONS ONLY, not general algebras. So the
symmetric-algebra argument (J nilpotent ∧ λ(nilpotent)=0 ⟹ J ⊆ rad(form)=0) must be
built from scratch over the jacobson route. Also available: Maschke (RepresentationTheory),
Wedderburn-Artin (SimpleModule/WedderburnArtin.lean), isSemisimpleRing_of_isReduced.
This is the deep brick; keep honest, no sorry-laundering.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] isSemisimpleRing_hecke_generic (HeckeSemisimpleGeneral) for q not root of unity
