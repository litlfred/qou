---
# qou-38vi
title: 'base-ring audit: Haar files use Field for intrinsic division (accepted, warn-only)'
status: todo
type: task
created_at: 2026-11-27T20:21:35Z
updated_at: 2026-11-27T20:21:35Z
parent: qou-s028
---

Thread 'Construct the O_q(SU(2)) Haar state' reports that the Field binders and field_simp calls flagged by scripts/base-ring-audit.py in HaarMomentKernel, OqSU2HaarPositivity, OqSU2HaarState and PickKernelSOS are intrinsic: haarMoment = (-q)^k/[k+1]_{q^2}, the Pick kernel 1/(1-xy), and the q-Pick denominators are quotients, and positivity needs an ordered field. The division-free parts (zeroWeightFunctional, torus invariance, invHom) are already over CommRing. Reason: division by q-integers and Pick denominators is intrinsic; the division-free parts are already over CommRing. base-ring-audit.py only has --shrink and never raises a count, so these stay as warn-only GREW lines. Open question: does the audit need an accept-with-reason mechanism rather than a hand edit to the baseline? OqSU2BudgetHaar and OqSU2BudgetSign belong to another thread and are not covered here.
