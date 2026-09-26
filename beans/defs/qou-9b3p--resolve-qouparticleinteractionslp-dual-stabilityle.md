---
# qou-9b3p
title: Resolve QOU/ParticleInteractions/lp_dual_stability.lean sorries
status: todo
type: task
priority: normal
created_at: 2026-08-21T18:14:38Z
updated_at: 2026-08-21T21:16:14Z
---

REOPENED 2026-08-21 by the sorry-closure honesty audit (PR #5411).

This bean was marked `completed` by the 2026-08-21 closure batch, but the
gap was NOT closed. The `sorry` was replaced by a new context-class field
carrying the theorem's own conclusion, and the proof became a projection
(AGENTS.md §3b-cond item 5). The commit also deleted the sorry-free
`*_unconstrained_false` refutation that proved the class was too weak.

PR #5411 restored the prior state: honest `sorry` + `-- Ref:` citation,
and the refutation theorem back in place. `lean`-direct exit 0.

TO RESTART COLD: read
docs/audits/2026-08-21-sorry-closure-honesty-audit.md for the verdict
table and the three-way disposition rubric. The honest closures are (a)
prove it, (b) leave the cited `sorry`, (c) demote to a conjecture / a
content-bearing class with no instance. Adding the conclusion as a field
is NOT one of them. If a genuine upstream physical hypothesis exists,
the correct pattern is a SEPARATE `extends` model class carrying that
hypothesis with the theorem DERIVING the conclusion from it — the
verified exemplar is QOU/FluidDynamics/q_bkm_criterion.lean, and the
in-file precedent is the `QTurbulenceCascadeModel` this same batch
deleted.
