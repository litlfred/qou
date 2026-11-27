---
# qou-j5b6
title: 'precision: gg_scalar_per_step_probe.py:96 hard-codes 1.75923699418 copied from a witness'
status: todo
type: bug
created_at: 2026-11-27T20:29:09Z
updated_at: 2026-11-27T20:29:09Z
parent: qou-myts
---

The witness-value-copy ratchet in scripts/precision-gates.sh is RED on main at computations/probes/gg_ntower/gg_scalar_per_step_probe.py:96, which hard-codes 1.75923699418 (F_required on the z_D order-zero base, per AGENTS.md) taken from the protium witness. Fix at the producer: read the value from its witness or derive it in mpmath, instead of copying the literal. Reported by several threads on 2026-11-27 as pre-existing on main. The other red, the raw-float64 ratchet on binding-scale-tl.witness.json, is fixed by PR #9656.
