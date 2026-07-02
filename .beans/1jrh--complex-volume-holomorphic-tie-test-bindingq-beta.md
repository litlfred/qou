---
# 1jrh
title: 'Complex-volume holomorphic tie: test (binding,Q_beta) satisfy one Askey-Wilson 3-term recurrence (recurrence_invol_descent)'
status: todo
type: task
created_at: 2026-06-30T20:35:58Z
updated_at: 2026-07-02T15:30:00Z
---


## 2026-07-02 — formalize-first prune: test GATED on c₃^even (no scan run)
DOF count: AW has 4 params (a,b,c,d; q₀ fixed); measured rungs give at most 2
recurrence constraints (odd: c₂=−1 proved, c₃≈−2 near-match, c₄ CAL-anchored;
even: c₂≈−8 ONLY — one rung cannot constrain a recurrence). Under-determined ⇒
any AW identification now = fit (Δ_λ-gate forbidden). Prior art transferred:
constant depth-2 kernel already REFUTED (PR #1900, c₄=1−c₃² over-determination);
AW = the surviving non-constant case, so 1jrh is well-posed but blocked.
DECISIVE GATED TEST (parameter-free Casoratian sign test, one line once
c₃^even exists): W₂ ≈ 16 + c₃^even (numeric part from near-match rungs); AW positivity ⇒ W₃/W₂ > 0; violation
refutes one-recurrence outright. Blocking measurement: extend Hoefsmit Stage-B
net-route one order deeper in u (the c₂^even≈−8 machinery).
Full analysis: ../docs/audits/2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md
