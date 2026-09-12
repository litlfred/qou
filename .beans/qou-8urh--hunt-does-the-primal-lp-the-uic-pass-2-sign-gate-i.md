---
# qou-8urh
title: 'HUNT: does the primal LP the UIC Pass-2 sign gate invokes exist, and does complementary slackness on it yield the gate?'
status: in-progress
type: task
priority: normal
created_at: 2026-09-12T21:31:26Z
updated_at: 2026-09-12T21:31:52Z
---

## Scope

`hecke_core_legacy.unified_iterative_correction` Pass 2 (`:2176-2199`) keeps only
Wedderburn blocks with `final_tr_sign <= 0` and returns that gated sum. Its own
comment derives the gate from **complementary slackness on a primal LP**, and
that LP is not in the file. Owner ruled 2026-09-12 to *drop the gate* AND to
*hunt the primal LP*; this bean is the hunt. A separate agent drops the gate —
**this bean does not touch the producer.**

Three outcomes: (a) the LP exists and CS yields the sign gate — would REVERSE
the drop; (b) the LP exists and CS yields something else; (c) no such LP exists.

## Finding (preliminary, 2026-09-12)

The LP **exists** and is formalized sorry-free: `prop:operator-selection-lp`
(`content/quantum-observable-universe/mass-theory/operator-selection-lp.md`),
Lean `QOU.ParticleInteractions.operator_selection_lp`
(`.../lean/QOU/ParticleInteractions/operator_selection_lp.lean`). Verdict is
shaping as **(b)**: CS on it constrains the *selected operator's* Frobenius
constraint values `(Gx*)_i`, which are non-negative on every feasible point, so
`<= 0` collapses to `= 0`. The gate's quantity is the *cost* vector `t_lambda =
tr_lambda(W_atom)`, which is a different vector and is unconstrained in sign.
