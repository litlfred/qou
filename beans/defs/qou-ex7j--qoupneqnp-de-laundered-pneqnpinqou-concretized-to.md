---
# qou-ex7j
title: QouPNeqNp de-laundered + PNeqNPInQOU concretized to not-FamilyPolyBounded
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T20:48:51Z
updated_at: 2026-11-15T12:00:00Z
parent: qou-b1je
---

Resolves the qou-2yrn audit finding. (1) Removed axiom conj_qou_p_neq_np_faithful + the global instance -> qou_implies_p_neq_np_at_chi is now genuinely conditional (visible [QouPNeqNp ..] hypothesis, no axiom in #print axioms). (2) Replaced opaque PNeqNPInQOU with def PNeqNPInQOU (decisionCost) := not FamilyPolyBounded decisionCost -- concrete, falsifiable, wired to CountingModuliGrade; threaded decisionCost through JetHorizonTransfer + ComplexityDictionary. The counting->decision transfer stays the open conjecture (QouPNeqNp.faithful, no instance). PR #4687.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Closed 2026-11-15 (E7 triage)

Checked against `main`: PR #4687 merged 2026-08-08. `QOU/Information/QouPNeqNp.lean` defines `PNeqNPInQOU := ¬ FamilyPolyBounded decisionCost` (line 57) and carries no `axiom` and no `QouPNeqNp` instance. That is the work this task names. The conjecture itself (the `faithful` transfer) is still open and is tracked by `cj2b6`, which stays open per §13a.
