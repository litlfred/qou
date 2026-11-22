---
# qou-zuuz
title: 'dilog Part-B a.e. residual: Borel-Cantelli resonance-window route (Mathlib HAS BorelCantelli, LACKS Weyl equidistribution) -- 4 bricks: W_m measure bound, summable schedule, BC a.e., glue to boundary seed'
status: in-progress
pr: 8220
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-31T20:39:12Z
updated_at: 2026-11-22T21:45:00Z
parent: qou-r9ih
---



## Progress Update (2026-11-16T22:11:55Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/DilogPartBJointAndOhtsukiSaddleBrick.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/dilog-part-b-joint-and-ohtsuki-saddle-brick.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8220 (`4fed1eb1d2c9f99be67799649865fd4f3ddd3d6a`); keeping `status: in-progress` until PR merges.

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8220 (`QOU/QBeta/DilogPartBJointAndOhtsukiSaddleBrick.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8220 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.
