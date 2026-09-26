---
# qou-chkh
title: 'Front 2c: PivotalCategory (FGModuleCat K) instance via Module.evalEquiv'
status: completed
type: task
priority: normal
created_at: 2026-08-26T16:22:42Z
updated_at: 2026-08-26T16:38:07Z
---

REACHED, but not by this route -- and the route is now unnecessary.

pivotalOfBraided (qou-knsx) makes every braided right-rigid category pivotal.
FGModuleCat K is symmetric, hence braided, and is right-rigid in Mathlib. So it
is pivotal with NO linear algebra: verified,

  noncomputable example (K : Type) [Field K] : PivotalCategory (FGModuleCat K) :=
    inferInstance     -- exit 0

Module.evalEquiv is not used anywhere. The concrete non-vacuity witness this bean
wanted exists; the plan for getting it was superseded before it was executed.
