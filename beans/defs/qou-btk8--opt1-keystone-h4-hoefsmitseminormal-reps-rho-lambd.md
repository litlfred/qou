---
# qou-btk8
title: 'opt1-KEYSTONE: H4 Hoefsmit/seminormal reps rho_lambda + Markov weights ⇒ tr_M = sum w_lambda chi_lambda'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T17:37:14Z
updated_at: 2026-11-16T19:15:00Z
parent: qou-rtxm
---


## 2026-11-16 — `H₄(q)` 5-Partition Hoefsmit/Wedderburn Trace Keystone in Lean (PR #8162)
- Formalized `Partition4`, `h4IrrepDim`, `h4_wedderburn_burnside_and_catalan` (`1² + 3² + 2² + 3² + 1² = 24 = 4!`, `SU(2)` row-capped `1² + 3² + 2² = 14 = C₄`, radical `3² + 1² = 10`), `evalH4WedderburnTrace`, and `h4_trace_cyclic_of_wedderburn_bridge` in `folio/quantum-observable-universe/lean/QOU/Foundations/WenzlTemperleyLiebH4Keystone.lean` (wired into `QOU.lean`, 0 `sorry`, generic `CommRingOps R` per §7c).
- PR: https://github.com/litlfred/qou/pull/8162 (commit `f3dcbfe5fb51a67f3233319674c13a3791ba91d2`). Status kept `in-progress`.
