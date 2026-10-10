---
# qou-v986
title: 'SUB-BRIDGE: numSYT(BraidKnot) = numStandardYoungTableaux(Mathlib) — the two StandardYoungTableau structures differ (BraidKnot 0-indexed entry+zero_off+inj_on; Mathlib SSYT-wrapper BijOn Icc 1 card). Needs an SYT-type equiv (index shift + SSYT wrap), ~50-100 lines. Blocks numSYT=numSYTenum∘rowLens (qou-ftmf)'
status: completed
type: task
priority: normal
created_at: 2026-08-01T23:44:33Z
updated_at: 2026-08-10T04:17:11Z
---

CLOSED by #4548, merged 889da4c823. QOU/BraidKnot/NumSYTBridge.lean is on main; numSYT_eq_numSYTenum_rowLens at line 222, sorry-free (verified lean-direct exit 0, #print axioms clean on all 7 declarations, no sorryAx). The SYT-type equiv this bean asked for (index shift + SSYT wrap) is what landed. Closed by the sweep session rather than by 4548's author, who deliberately declined to self-close it.
