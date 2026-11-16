---
# qou-wp3h
title: Step-9a chosen joints (m_p/m_e chain)
status: in-progress
type: epic
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:09:58Z
updated_at: 2026-11-16T19:19:00Z
parent: qou-10v9
---

Sub-epic P1.9A of PROGRAM: L2 at 1 ppQ (mass and binding accuracy) (work-plan reorganisation 2026-10-04).

## Progress Update (2026-11-16 — Owner Ruling `Q-WP3H-1 = 1`, PR #8143)

- Executed Option 1 across all 5 child beans under PR `litlfred/qou#8143` (commit `7df80d1c2e228518b2ca15ec1d314be46da8e524`):
  - `qou-ev3a`: Proved the reverse direction (converse) of D2 at $v = n - 1$ for all three depth-1 carrier shapes in `QOU/BraidsAndKnots/HookArmLeg.lean` (`depth1_three_shapes_achieve_hookLen_eq_sum_sub_one`, `0` `sorry`).
  - `qou-zbcj` & `qou-tw5z`: Added `QOU/Torsion/MultiplicativeIntegralCurvature.lean` (`0` `sorry`, wired into `QOU/Torsion.lean` and `QOU.lean`) and 50+ dps `mpmath` probe `computations/probes/yekutieli_multiplicative_integral_curvature_probe.py` + `yekutieli-multiplicative-integral-curvature.witness.json` (registered in `computations/q0_anchor_manifest.json`).
  - `qou-kx92` & `qou-qkbp`: Verified landed `main` commits (`62d3235885`, `a2842b21ac`, `0912f1aa53`, `709b8cc166`, `b9c56a4a59`, `534794e799`) and recorded audit notes.
- All beans kept at `status: in-progress` per owner rule.

## Progress Update (2026-11-16 — Round 48: PR #8160)
- **PR:** [`litlfred/qou#8160`](https://github.com/litlfred/qou/pull/8160) (`c0fb591249c67f13f6a77b40075589852babb011`)
- Completed Lean formalization and impact analysis for `8gzz`, `qou-0w42`, `qou-tknh`, `qou-bhrx`, and `qou-loqn` (`0` `sorry`, `0` self-assuming audit hits).

## Progress Update (2026-11-16 — Round 49: PR #8143 fix + PR #8164)
- **PR #8143 fix:** Stamped `scriptCommitSha: "7df80d1c2e228518b2ca15ec1d314be46da8e524"` in `computations/probes/yekutieli-multiplicative-integral-curvature.witness.json` (`4340428cced694b249ca48316cbb5096751b5f64`).
- **PR #8164:** Opened [`litlfred/qou#8164`](https://github.com/litlfred/qou/pull/8164) (`47da262e4f487a8f51de58f3577a63d5b17e6d6a`) for `qou-ch8w`, `qou-quv8`, `qou-yczy`, `qou-h5aw`, and `qou-n4u6` (`0` `sorry`, `0` self-assuming audit hits, 50+ dps witness `na-stokes-bar-parity-local-bond.witness.json`).
