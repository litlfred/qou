---
# qou-my68
title: 'Infra: GS-filtration ↔ cyclotomic-projection identification (b3ix residual same_element)'
status: todo
type: task
priority: normal
tags:
    - alien-habiro
    - reorg-2026-10-04
created_at: 2026-07-18T17:48:54Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

N1 (polynomial-shadow injectivity) attempted: rootsOfUnity_infinite via primitive-root order-uniqueness — blocked in sandbox on Complex.isPrimitiveRoot_exp (not in cached imports; needs Mathlib.RingTheory.RootsOfUnity.Complex build). poly_eq_of_eval_eq_on_rootsOfUnity then follows from Polynomial.eq_of_infinite_eval_eq + Set.Infinite.mono. Do in full-build session alongside the meromorphic clone. Plan: docs/workplans/2026-07-18-alien-habiro-hard-infra-execution-plan.md §2 (N1 first — days-scale, discharges atom instances of HabiroGBSameElement).


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** N1 is done (PolynomialShadowRigidity.lean, sorry-free, via qou-uqen). The target `HabiroGBSameElement` no longer exists in the Lean tree, so re-scope what "same_element" this bean should discharge before resuming N2–N4.

Evidence: N1 landed as `qou-uqen` (completed): `folio/.../lean/QOU/BraidKnot/PolynomialShadowRigidity.lean` (`setOf_isRootOfUnity_infinite`, `eq_of_eval_eq_on_rootsOfUnity`, no sorry). However, `HabiroGBSameElement`, the structure N1 was meant to discharge (`docs/workplans/2026-07-18-alien-habiro-hard-infra-execution-plan.md` §2), appears in no `.lean` file in the tree. N2–N4 have not been done.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
