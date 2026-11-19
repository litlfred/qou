---
# qou-blf1
title: 'GS-3: Nilpotent Scalar Collapse & Explicit Split-Ring Non-Zero/Non-Unit FrobeniusHopfData Model'
status: todo
type: task
priority: high
created_at: 2026-11-19T16:48:46Z
updated_at: 2026-11-19T20:03:00Z
parent: qou-uhx0
---

Extend `FrobeniusHopfModelDichotomy.lean` (`qou-aawz`): prove nilpotent `sigma = eta >> epsilon` forces `id_A = 0` (closing Artinian local rings / dual numbers) and construct an explicit non-zero non-unit `FrobeniusHopfData` over a split product ring / category (`FrobeniusHopfNilpotentAndNonFieldModel.lean`).

## Resolution (2026-11-19)
- Proved `id_eq_zero_of_unitCounit_nilpotent`, `dichotomy_of_nonunits_nilpotent_ring`, and the explicit split-ring sharpness model `SplitPairCat R` (`splitPairFrobeniusHopfData_sharpness`) in `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/FrobeniusHopfNilpotentAndNonFieldModel.lean` (829 lines, 0 sorry, 0 axiom, 0 warnings).
