---
# qou-dau6
title: 'GAP: cross_check_trM_1ppb --strict fails on main — peel witness computed at proton q0 but gate expects the muon pin'
status: todo
type: task
priority: normal
created_at: 2026-08-09T12:34:43Z
updated_at: 2026-08-23T07:59:27Z
---

## Cross-link — and a retraction of my own framing (2026-08-23)

I appended a note here calling this bean's diagnosis one of **three competing
hypotheses**. That was wrong and never merged; this replaces it.

**This bean and `qou-3zby` are both correct.** `667c9ab3f6` on `main`
(2026-08-21) adjudicated the red and found **two simultaneous causes**: the
C/D convention straddle (`qou-3zby`) *and* the muon/proton pin mismatch
(this bean). The four-method classification, the fix path for each, and the
withdrawal of my spurious third candidate are recorded on `qou-3zby`.

**Relevant to this bean specifically:** the guard gave *false assurance*. It
refused to start off-muon, which made the run look pin-uniform while a
committed input (Habiro) sat at the **proton** pin — matching convention C
there to 2.71e-13, exact rather than near. It survived because the guard
checked one of its four inputs; Habiro has no `q0Value` to compare
(`q0Anchor: ambiguous`) and Hoefsmit has no anchor at all. `667c9ab3f6`
widened the guard to every input that records a q0 and to NAME the ones that
do not.

Fix for this half: regenerate `habiro-coefficients-extended` under
`QOU_Q0_ANCHOR=ideal`. Blocked — see `qou-iayk`.
