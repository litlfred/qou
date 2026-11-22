---
# qou-fa5c
title: 'GAP: GNS embedding beyond the quotient step (A/N inner product + left action)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-22T10:47:15Z
updated_at: 2026-11-22T11:06:52Z
parent: qou-uwyf
---

markov_gns_null_ideal gives N a two-sided ideal. Remaining: the inner product <[x],[y]> = tr(x* y) is well defined and positive definite on A/N, and left multiplication descends to an action pi with pi(x)=0 on A/N iff x in the annihilator; Hilbert completion separate. Lean: QOU/Observations/AlgebraicGnsEmbedding.lean.

Follow-up to qou-02q4 (PR #9001, merged). Owner 2026-11-22: 'Fill the gaps ... Make them beans and work them.' Session https://claude.ai/code/session_01Qmmkt5ngCVGxt8cKmAnoR2

2026-11-22: null_pair_eq_zero, gns_form_well_defined, gns_form_definite, gns_action_well_defined, gns_action_adjoint, gns_action_faithful proved (needs hermitian tr). Completion to a Hilbert space not done. Complete on merge.
