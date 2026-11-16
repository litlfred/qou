---
# qou-ec5z
title: (TAIL) depth-1 — nu_{n-1} carrier formalization + onset n1=8
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T00:44:56Z
updated_at: 2026-10-04T15:46:33Z
parent: qou-10v9
---


Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: (TAIL) depth-1 — nu_{n-1} carrier formalization + onset n1=8

### Progress Update (2026-11-16, PR #8179)
- Completed the D6 assembly (`nuDepthOneClosedForm`, `depthOneCubicFactor_decomp`, `nuDepthOneClosedForm_pos_of_ge_eight`) in `QOU/BraidsAndKnots/YoungDiagramTailFirstInstance.lean` (`0` `sorry`), joining D1–D5 from PR #8143 and PR #8153.
- Verified against exact `Fraction` enumeration and 3-carrier reduction in `computations/probes/tail_d6_lp_dual_altchar_vlevel_probe.py`.
- Opened PR `litlfred/qou#8179` (`bf3902040cf206123f8aa0b5dc2b79c176dd9ce1`). Keeping status `in-progress` pending owner review.
