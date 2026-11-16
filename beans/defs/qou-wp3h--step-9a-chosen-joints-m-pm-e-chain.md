---
# qou-wp3h
title: Step-9a chosen joints (m_p/m_e chain)
status: in-progress
type: epic
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:09:58Z
updated_at: 2026-11-16T18:02:18Z
parent: qou-10v9
---

Sub-epic P1.9A of PROGRAM: L2 at 1 ppQ (mass and binding accuracy) (work-plan reorganisation 2026-10-04).

## Progress Update (2026-11-16 — Owner Ruling `Q-WP3H-1 = 1`, PR #8143)

- Executed Option 1 across all 5 child beans under PR `litlfred/qou#8143` (commit `7df80d1c2e228518b2ca15ec1d314be46da8e524`):
  - `qou-ev3a`: Proved the reverse direction (converse) of D2 at $v = n - 1$ for all three depth-1 carrier shapes in `QOU/BraidsAndKnots/HookArmLeg.lean` (`depth1_three_shapes_achieve_hookLen_eq_sum_sub_one`, `0` `sorry`).
  - `qou-zbcj` & `qou-tw5z`: Added `QOU/Torsion/MultiplicativeIntegralCurvature.lean` (`0` `sorry`, wired into `QOU/Torsion.lean` and `QOU.lean`) and 50+ dps `mpmath` probe `computations/probes/yekutieli_multiplicative_integral_curvature_probe.py` + `yekutieli-multiplicative-integral-curvature.witness.json` (registered in `computations/q0_anchor_manifest.json`).
  - `qou-kx92` & `qou-qkbp`: Verified landed `main` commits (`62d3235885`, `a2842b21ac`, `0912f1aa53`, `709b8cc166`, `b9c56a4a59`, `534794e799`) and recorded audit notes.
- All beans kept at `status: in-progress` per owner rule.
