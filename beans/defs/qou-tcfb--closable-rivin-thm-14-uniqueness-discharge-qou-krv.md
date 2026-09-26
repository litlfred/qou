---
# qou-tcfb
title: 'CLOSABLE: Rivin Thm 1.4 uniqueness -> discharge qou-krvm(ii) via SymmetricOptimum wiring'
status: completed
type: task
priority: high
created_at: 2026-08-15T15:57:50Z
updated_at: 2026-08-15T20:45:18Z
parent: qou-5lm6
---

Thm 1.4: at most one structure with prescribed dihedral angles. qou-krvm(ii) needs uniqueness of the symmetric point; SymmetricOptimum.optima_coincide (PR #4513) already proves strictly-convex-objective-on-symmetric-convex-set has a unique symmetric maximiser. Mostly WIRING: instantiate optima_coincide premise at the angle-structure polytope to discharge qou-krvm(ii). Coordinate w/ qou-krvm.
