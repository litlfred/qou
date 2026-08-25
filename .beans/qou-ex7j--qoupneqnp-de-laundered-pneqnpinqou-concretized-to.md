---
# qou-ex7j
title: QouPNeqNp de-laundered + PNeqNPInQOU concretized to not-FamilyPolyBounded
status: in-progress
type: task
priority: high
created_at: 2026-08-07T20:48:51Z
updated_at: 2026-08-07T20:48:51Z
---

Resolves the qou-2yrn audit finding. (1) Removed axiom conj_qou_p_neq_np_faithful + the global instance -> qou_implies_p_neq_np_at_chi is now genuinely conditional (visible [QouPNeqNp ..] hypothesis, no axiom in #print axioms). (2) Replaced opaque PNeqNPInQOU with def PNeqNPInQOU (decisionCost) := not FamilyPolyBounded decisionCost -- concrete, falsifiable, wired to CountingModuliGrade; threaded decisionCost through JetHorizonTransfer + ComplexityDictionary. The counting->decision transfer stays the open conjecture (QouPNeqNp.faithful, no instance). PR #4687.
