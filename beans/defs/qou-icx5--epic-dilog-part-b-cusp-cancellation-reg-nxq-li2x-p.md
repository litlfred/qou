---
# qou-icx5
title: Dilog Part-B cusp cancellation — reg_n(x;q) -> Li2(x)-pi^2/3 (uniform iπ-tower + linear-pole)
status: in-progress
pr: 8233
updated_at: 2026-11-22T21:45:00Z
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T03:17:08Z
updated_at: 2026-11-22T21:45:00Z
parent: qou-r9ih
---


Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: dilog Part-B cusp cancellation — reg_n(x;q) -> Li2(x)-pi^2/3 (uniform iπ-tower + linear-pole)

## Progress Update (PR #8233)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8233` at `0df1f54777395f7641371a1bd56d61fa352927af`).
- **Lean Formalization**: `QOU.QBeta.DilogCuspCancellationAndBorelProperTimeBrick.dilog_part_b_cusp_linear_pole_and_pi_sq_third_cancellation` (Part-B cusp linear-pole counterterm cancellation reg_n = Li2(x) - pi^2/3 + R_n and exact remainder error identity.)
- **80-dps Witness**: `computations/probes/dilog-cusp-cancellation-and-borel-proper-time-brick.witness.json` (`scriptHash: 3bb3c88effd9`, `scriptCommitSha: 162d2914798b1189f0082f4e029eb8fed83ca8ee`).

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8233 (`QOU/QBeta/DilogCuspCancellationAndBorelProperTimeBrick.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8233 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.
