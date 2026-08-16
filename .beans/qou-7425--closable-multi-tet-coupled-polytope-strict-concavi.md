---
# qou-7425
title: 'CLOSABLE: multi-tet coupled-polytope strict concavity (m004/L6a4) -> full qou-krvm(ii)'
status: completed
type: task
priority: normal
created_at: 2026-08-15T20:45:18Z
updated_at: 2026-08-15T21:37:25Z
parent: qou-5lm6
---

tcfb (#5130) discharged qou-krvm(ii) for the single-tetrahedron anchor sorry-free (strictConcaveOn_maximizer_unique + tetVol_maximizer_unique). Remaining analytic piece: total-volume Sigma tetVol strict concavity on the COUPLED polytope (m004 = 2 tets, L6a4 = octahedron) + wiring to the concrete M004AngleStructure/L6a4AngleStructure. REACHABLE: block-separated sum of strictly-concave is strictly-concave (Mathlib StrictConcaveOn.add on product domains). The only non-analytic residual is T2 geometric identification (qou-7y3g/qou-idvt). Also: qou-krvm(ii) as originally stated is FALSE for m004 (fixed locus is a line) — the corrected route is concavity-then-symmetry, now on main in AngleStructureUniqueness.lean.
