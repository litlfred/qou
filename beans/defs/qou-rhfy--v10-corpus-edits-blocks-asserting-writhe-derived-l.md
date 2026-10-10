---
# qou-rhfy
title: 'V10: corpus edits -- blocks asserting writhe-derived link invariance'
status: completed
type: task
priority: normal
created_at: 2026-08-10T19:30:51Z
updated_at: 2026-08-15T22:31:27Z
---

KNOWN: sm-lagrangian-selection-rules.md asserts Q = w/2 and w -> I_3 are
'functions on states constant on gauge orbits', while markov-moves-brane-tower.md
says 'horizontal AND VERTICAL moves exhaust the gauge freedom'. Inconsistent.
MINIMAL FIX: state that Q and I_3 are constant on HORIZONTAL orbits at the
tower's lowest level, not on the full Markov orbit. Nothing numerical changes.
Background audit agent is sweeping for the rest of this class.


RESOLVED 2026-08-11 via PR #4961 (merged). Corpus edits landed on the three
definitely-wrong blocks (sm-lagrangian-selection-rules, climax-volume-mass/
q-momentum, mass-theory/torus-knot-delta-q-writhe) plus strangelet-crossing-energy;
three suspect blocks flagged one clause each. Zero numbers moved -- only the LEVEL
at which the claims are stated. Bean was left at 'todo' after the merge.
