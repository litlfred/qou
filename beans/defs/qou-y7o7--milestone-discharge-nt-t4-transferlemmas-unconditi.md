---
# qou-y7o7
title: Discharge NT-T4 TransferLemmas → UNCONDITIONAL strong-AJ (provide the class instance)
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T04:47:59Z
updated_at: 2026-11-22T21:15:43Z
parent: c7vs
---


Former title (before 2026-10-04, when this became a story under a programme epic): MILESTONE: discharge NT-T4 TransferLemmas → UNCONDITIONAL strong-AJ (provide the class instance)

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

**Re-scoped, still open.** As titled ("provide the class instance") this is impossible: `not_transferLemmas` (`Machinery/StrongAJFigureEightInstances.lean`) proves `TransferLemmas` has no instance over a nontrivial ring, because `minimality` is phrased with `topDeg` on a Laurent ring. Before any instance work, the class needs restating: `minimality` in terms of the L-length `topDeg − bottomDeg`, or the ideal taken in the non-localized `A⟨L⟩` (Nguyen–Tran's order). That is a change to a source class, so it was put to the owner on a decision card on 2026-11-22. Even after the restatement, `minimality` for the real recurrence ideal is the [Tr4] Lemmas 3.1–3.3 content, i.e. the strong AJ conjecture itself for 4₁: the restatement makes the carrier honest, it does not prove it. Sibling `qou-xru7` scrapped.
