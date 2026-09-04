---
# qou-w0tx
title: 'C1 kernel dictionary parity: a mono-commuting D_q carries no (−1)^m residual — does Door-v force σ = unit shift?'
status: todo
type: task
created_at: 2026-09-04T08:31:31Z
updated_at: 2026-09-04T08:31:31Z
---

Follow-on to `qou-33hb` (#6582). The two σ ↔ t-shift dictionaries for the C1 kernel disagree on parity: (a) unit shift has an odd component, (b) double cover commutes with the covering monodromy. Question: does the Door-v `(−1)^m` residual (the target property #6474 demanded of D_q's tower) decide between them?

PLAN
1. Lean `QOU.Mass.C1KernelDictionaryParity`: (i) generic — a monodromy-commuting homogeneous operator whose tower alternates from level n₀ on has ZERO tower from n₀+1 (two consecutive levels suffice, no seed hypothesis); (ii) apply to `c1KernelOpCover`; (iii) dictionary (a) via `residual_from_level_tower_is_odd_part`: E Y = 0 and E(O Y) = 0 are two q-recurrences differing by q^{e+2} vs q^{e+1} in the shift-2 weight — jointly they force Y = 0 (needs q ≠ 0, q ≠ 1).
2. Exact probe (sympy, symbolic q/u).
3. Audit doc; scope sentence on the conjecture block and/or `c1-ggm-bar-parity-faces`.

Expected shape (to be verified, not assumed): the residual kills BOTH dictionaries — so it does not discriminate; if D_q's symbol is L_K, the Door-v twist is not carried by D_q's own tower. Scope-(b) with invariants named; scoped as "the kernel itself as the operator" (lower-order corrections not excluded).
