---
# qou-dygk
title: 'GAP: HasAction.action takes a scalar — no field space, so no variation, so no rank-2 Einstein tensor'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T19:08:39Z
updated_at: 2026-10-04T15:20:05Z
---

MEASURED. MathlibExt/MonoidalCalcVar.lean:67 'class HasAction (R) (C) where action : ((1_C) --> (1_C)) -> R'. End(1_C) is the ground ring (Eckmann-Hilton), so the action is a function FROM A SCALAR TO A SCALAR. There is no space of fields anywhere in it. A variational derivative dS/dg needs S to be a function on a SPACE OF METRICS; its derivative lives in that space's dual, and THAT dual is where rank-2 comes from. No field space => no derivative => no tensor => everything collapses to 1_C --> 1_C. So einsteinTensor : (1_C) --> (1_C) (GaugeTheory.lean:127, MonoidalCalcVar.lean:89) is DOWNSTREAM of the defect, not the defect. Worse: hasMonoidalEOM_of_def makes the EOM hold BY rfl once vd.gravity := ec.einsteinTensor + ec.stressTensor, so the instance is free. The file's own docstring is honest: 'The full proof requires a categorical calculus of variations ... concrete instances are the conjectural input.' THE RANK-2 CARRIER ALREADY EXISTS IN THE REPO and is good: FrobeniusHopfData/FrobeniusPairingCategorical.lean:51, 'structure FrobeniusPairingData where obj : C; dual : C; eval : dual (x) obj --> 1_C' — a nondegenerate symmetric bilinear form, i.e. a metric — with Nondegenerate stated via the snake identities and exactPairing_of_nondegenerate landing it in Mathlib's rigid API. Its own header records that a previous version asserted nothing. So this is a WIRING GAP, not a category error: the metric is formalized, the action does not take it as an argument. LADDER (each rung standard): (1) action : FrobeniusPairingData C -> R instead of (1 --> 1) -> R; (2) a tangent/variation notion on that space — it is a torsor under Aut(A); (3) dS/d<,> : dual (x) obj --> 1_C, the Einstein tensor, rank-2 BY CONSTRUCTION and the same type as the metric; (4) Aut(A)-invariance of S => a contracted Bianchi identity, which is Noether — and climax-volume-mass/noether-theorem-callout.md already claims exactly this, currently on top of the projections.



## Reasons for Scrapping

Duplicate of `qou-h0ou` (work-plan reorganisation 2026-10-04). Evidence: [B] same diagnosis; qou-h0ou "DIAGNOSIS CONFIRMED", rank-2 field space formalised
Content is untouched; only this work item is closed.
