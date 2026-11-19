---
# qou-y7ek
title: 'PPQ-1 (L1): 80-dps Newton Anchor Round-Trip Polish (2.85 ppt -> < 1e-80 on m_p/m_e -> q_0, q_2t)'
status: todo
type: task
priority: high
created_at: 2026-11-19T16:48:46Z
updated_at: 2026-11-19T16:48:46Z
parent: qou-10v9
---

Eliminate the `0.002852 ppb` (`2,852 ppQ`) anchor round-trip residual on `m_p` in `per-observable-100x-status.witness.json` by solving `q_0` and `q_2t` to full 80-dps Newton convergence against exact `M_P_OVER_M_E`.
