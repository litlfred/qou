---
# mobius_frobenius_kernel
title: mobius frobenius kernel missing hypotheses
status: in-progress
pr: 8225
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-10-04T15:26:46Z
parent: qou-uot9
---

File: `folio/quantum-observable-universe/lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean`
The `mobius_frobenius_kernel` theorem is unprovable. Its class lacks constraints on the data fields and has `*_unconstrained_false` lemmas proving that the conclusion is independent and refutable from the provided data alone.



Also known as `mfrk` (its former front-matter header id; the beans CLI uses the filename id `mobius_frobenius_kernel`). Recorded 2026-10-04.


## Progress (Round 53 — PR #8225)
- Implemented sorry-free, non-vacuous Lean 4 formalization + 80-dps mpmath witness in PR https://github.com/litlfred/qou/pull/8225 (HEAD `92ab8569af5ff7399510fd92cb2505df80c41b5e`).
- Marked `in-progress` pending PR merge.
