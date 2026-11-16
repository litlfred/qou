---
# qou-1a69
title: 'D6: assemble nu_{n-1} sign + closed form; check the onset n1=8 against the probe witness'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T00:45:22Z
updated_at: 2026-10-04T15:18:34Z
parent: qou-10v9
---

### Progress Update (2026-11-16, PR #8179)
- Formalized `depthOneCubicFactor`, `depthOnePolyFactor`, `nuDepthOneClosedForm`, `depthOneCubicFactor_decomp` ($n^3 - 11n^2 + 32n - 30 = (n - 8)((n - 2)^2 + (n - 1) + 5) + 34$), `depthOnePolyFactor_small_values` ($0$ at $n=4$, $-72, -180, -54$ at $n=5,6,7$), `depthOneCubicFactor_pos_of_ge_eight`, `depthOnePolyFactor_pos_of_ge_eight`, and `nuDepthOneClosedForm_pos_of_ge_eight` in `QOU/BraidsAndKnots/YoungDiagramTailFirstInstance.lean` (`0` `sorry`).
- Verified exact `Fraction` agreement across full partition enumeration ($n=4..14$), 3-carrier reduction ($n=4..25$), and the closed form + onset $n_1 = 8$ in `computations/probes/tail_d6_lp_dual_altchar_vlevel_probe.py` (`computations/probes/tail-d6-lp-dual-altchar-vlevel.witness.json`, `scriptCommitSha: f87b601a1fa1aff32eae2de2310d57570f222be9`).
- Opened PR `litlfred/qou#8179` (`bf3902040cf206123f8aa0b5dc2b79c176dd9ce1`). Keeping status `in-progress` pending owner review.
