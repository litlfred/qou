---
# qou-lrvc
title: 'SOURCE: which chirality is the Rolfsen 5₂ (and GGM''s S⁺/S⁻) in the derived (μ, λ, Im τ > 0) frame — needs a held table with its orientation convention'
status: todo
type: task
created_at: 2026-09-07T09:54:34Z
updated_at: 2026-09-07T09:54:34Z
---

SOURCE QUESTION (no held source; do not close until one is held and read): in the derived frame of #6985 — λ the cusp class dying in H₁(M), μ the unique complement whose filling admits no nondegenerate representation (Property P certificate), λ oriented so Im(t_λ/t_μ) > 0 for the Im z > 0 solution — the two-bridge triangulation of K(7,3) from the Farey word RL has boundary slopes {−10, −4, 0} and A-polynomial A = L³ + L²(M¹⁰−M⁸+2M⁴+2M²−1) + L(−M¹⁴+2M¹²+2M¹⁰−M⁶+M⁴) + M¹⁴ (the standard printed A_{5₂} under L ↦ 1/L). Its mirror has {0, 4, 10}. WHICH of the two is the Rolfsen-table 5₂ (equivalently: which chirality does GGM's S⁺(0)=[[1,4,0],[0,1,0],[−3,−9,1]] / S⁻(0) belong to in this frame) is a CONVENTION the library does not hold. Candidates to ingest and read: Rolfsen, Knots and Links (Appendix C table, with the diagram's crossing signs); Culler–Shalen / Cooper–Culler–Gillet–Long–Shalen 1994 (A-polynomial table, with their orientation and (μ,λ) convention); SnapPy's Manifold('5_2') orientation + boundary_slopes + A-polynomial (Culler's tables), which fixes a definite mirror; Hatcher–Oertel boundary-slope conventions. What resolves it: one source stating A_{5₂} or the slope set together with the crossing-sign / orientation convention, matched against the derived frame by the sign of the slopes.

What it changes: nothing in the Route-A verdict (both inputs are mirror-invariant — RouteANewtonPolygonDT.absSlopeEq_mirror / lProfile_mirror, PR #7032); it decides which of S⁺/S⁻ (4 vs 3) attaches to the derived triangulation, which any future chirality-graded count (qou-rtec D4, the bar-involution link) must state in a definite frame. Audit: docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md §3 and §3b. Parent qou-yvyd.
