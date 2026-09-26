---
# nezk
title: 'Tranche 7: A=4 per-bond open/loop decomposition — spanning-tree open pn bonds (linear) + loop edges (det), E_unit calibrated on 2H, predict light series'
status: completed
type: task
priority: normal
created_at: 2026-07-07T11:53:32Z
updated_at: 2026-07-07T11:59:11Z
parent: il97
---

2026-07-07 DONE (PR pending). NEGATIVE + crossover finding. Additive
open/loop split (2H-calibrated, pn-tree open bonds linear + loop det)
UNDER-predicts A>2 badly: 3H -37%, 3He -30%, 4He -64%. FAR worse than
the collective full determinant (all-loops): 4He 0.940×. So many-body
binding is COLLECTIVE (cross terms), NOT additive per-bond — dichotomy
is a single-bond (2H) result only. Full-det non-monotone (3H 0.74, 3He
0.30 — p↔n mirror), so collective det is the right DIRECTION but not a
predictor; 4He 6% + 3He mirror are the open GAP-A-4 legs. Closes the
"extend dichotomy additively to A>=3" route. §2i + probe
light_series_open_loop_decomposition.py.
