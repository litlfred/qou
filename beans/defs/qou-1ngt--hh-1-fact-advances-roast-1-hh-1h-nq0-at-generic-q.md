---
# qou-1ngt
title: 'HH_1 fact (advances roast): (1) HH_1(H_n(q))=0 at generic q (semisimple/separable, Wenzl) -- the HH_1 non-trace-functional route is EMPTY at the observable substrate q0; nonzero only at roots of unity (fibre level). (2) HH_1(D^b(Bring curve))=H^1(O)=C^4, dim = g = (2-chi)/2, so chi=-6 => dim 4; as S_5-rep it is the STANDARD 4-dim irrep (=H^0(K) dual), = tangent to Jac(Bring) (4-dim ppav). CAVEATS: finite 4-dim under-resolves exp-many braids (magnitude/info tension); derivation != decision procedure. Candidate: formalize dim HH_1(Bring)=(2-chi)/2 as a STRUCTURAL fact, not a wall-crossing. Cite HKR + Bring genus-4 S5.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T15:19:33Z
updated_at: 2026-11-17T13:00:03Z
parent: qou-59vq
---

### Progress Update (Round 68 — PR litlfred/qou#8356)
- **PR:** https://github.com/litlfred/qou/pull/8356 (`2c058b5e380e076d0aec9233aad57fa6af43d018`)
- **Lean 4 Module:** `QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling` (`LEAN_EXIT=0`, `0` warnings, `0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 major, 0 advisory` across all directory-mode static vacuity & borrowed-name audits)
- **Numerical Probe & Witness:** `computations/probes/bring_curve_hochschild_stale_weight_cyclicity_three_cell_comparability_quadratic_rescaling_probe.py` & `computations/probes/bring-curve-hochschild-stale-weight-cyclicity-three-cell-comparability-quadratic-rescaling.witness.json` (`COMMIT1 = 8ee314938e6a9bac9ee46faedf9aebdee8b895fb`, `scriptHash = 326bd13833f0`, `allPassed = True`, `dps = 80`)
