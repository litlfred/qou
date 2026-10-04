---
# qou-e4yl
title: 'PROVE(lean): mkDegLexOrder — noncomputable def mkDegLexOrder {G : Type u} [DecidableEq G] (rank : G → ℕ) (rank_inj : Fu [cited bergman1978]'
status: completed
type: task
priority: normal
tags:
    - paper-ugb
    - tractable
    - cite-bergman1978
    - reorg-2026-10-04
    - lean
    - cited-sorry
    - verify-build
created_at: 2026-08-01T23:31:10Z
updated_at: 2026-10-04T15:30:49Z
parent: qou-k1mq
---

CLOSED. Proved mkDegLexOrder.wf sorry-free by adding a generic 'shortLex_wellFounded' theorem (Mathlib v4.24.0 lacks shortlex/List.Lex wf). Length-first refinement of List.Lex; double accessibility induction (outer on Acc r head, inner on Acc SL tail). wf := shortLex_wellFounded (InvImage.wf rank Nat.lt_wfRel.wf). lean-direct exit 0, no sorry warning. Branch claude/prove-tractable-cited-sorries-2026-08-01.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] decl found sorry-free & unconditional in folio/unital-groebner-bases or fred2005 tree (k1mq child; sorry gone) | previously stalled; last update 2026-08-02



## Verify by build (2026-10-04)

Closed on 'sorry-free on main' evidence, but the cited declaration could not be matched automatically to a file that a CI Lake target is known to compile (orphan census 2026-10-04: only 654 of 1,309 lean.refs resolve into the compiled library; ugb and fred2005 are separate required packages). Confirm with a build and `#print axioms`; reopen if it does not compile.
