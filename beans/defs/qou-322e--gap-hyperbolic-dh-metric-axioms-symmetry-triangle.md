---
# qou-322e
title: 'GAP: hyperbolic dH metric axioms — symmetry, triangle, separation'
status: todo
type: task
priority: normal
created_at: 2026-08-16T11:11:36Z
updated_at: 2026-08-16T11:13:00Z
---

Origin: PR #5211 (T2 hyperbolic metric backfill). QOU/Archimedean/HyperbolicMetric.lean derives dH = ⨅ path lengths and proves dH_self sorry-free, but the three remaining pseudometric axioms are open: dH_comm (path-reversal reflection CoV on the Icc-restricted lintegral), dH_triangle (path concatenation + reparametrisation-invariance CoV), separation dH x y = 0 → x = y (needs FTC/absolute-continuity lower bound; Cantor-path obstruction to a naive bound). Not needed for the isometry engine or the geodesic classification. Kept as a bean (not a sorry) per AGENTS.md rule 13.
