---
# 2o66
title: 'Lean lemma: per-neutron multiplicativity of transfer atom word — tr_free/tr_atom exactly geometric in N (probe 2026-07-02, l(q0)=1.23698, Z-independent)'
status: completed
type: task
priority: normal
created_at: 2026-07-02T12:03:38Z
updated_at: 2026-07-03T00:43:25Z
---


## 2026-07-03 — scope clarification (Copilot review, PR #3249)
Completed AS SCOPED: the formalizable content is the ladder ALGEBRA layer
(QOU/Knot/PerNeutronLadder.lean, sorry-free, merged #3240) — geometric =>
closed form + vanishing multiplicative Casoratian; arithmetic => degenerate
c=2 recurrence; sigma-fixedness; parity descent. The word-builder
identification (the transfer atom word IS per-neutron multiplicative) is
compute-witnessed (binding-qbeta-recurrence-tie-probe.witness.json, exact to
<=1e-15 across two Z-chains) and enters the Lean as an explicit hypothesis by
design — formalizing it would mean modeling the Python transfer construction
itself, out of scope for this bean; if ever needed it belongs to the 8we6/H4
program as its own bean.
