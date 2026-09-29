---
# qou-e4yl
title: 'PROVE(lean): mkDegLexOrder — noncomputable def mkDegLexOrder {G : Type u} [DecidableEq G] (rank : G → ℕ) (rank_inj : Fu [cited bergman1978]'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-ugb
    - tractable
    - cite-bergman1978
created_at: 2026-08-01T23:31:10Z
updated_at: 2026-08-02T00:17:34Z
parent: qou-k1mq
---

CLOSED. Proved mkDegLexOrder.wf sorry-free by adding a generic 'shortLex_wellFounded' theorem (Mathlib v4.24.0 lacks shortlex/List.Lex wf). Length-first refinement of List.Lex; double accessibility induction (outer on Acc r head, inner on Acc SL tail). wf := shortLex_wellFounded (InvImage.wf rank Nat.lt_wfRel.wf). lean-direct exit 0, no sorry warning. Branch claude/prove-tractable-cited-sorries-2026-08-01.
