---
# qou-lbth
title: 'MATHLIB-INFRA EPIC (pentagon): complex-analysis gaps blocking PentagonRigidity Φ₁/Φ₂-entire leg — Hadamard factorization + elliptic divisor-degree (both absent from Mathlib v4.24.0; audit docs/audits/2026-07-20-pentagon-entire-leg.md)'
status: in-progress
pr: 8235
updated_at: 2026-11-22T22:50:00Z
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T05:12:52Z
updated_at: 2026-11-22T22:50:00Z
parent: qou-r9ih
---

## Progress Update (PR #8235)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8235` at `83fd5b4cb41e61d75f72ddd82bda505e34bd92f4`).
- **Lean Formalization**: `QOU.QBeta.ThimbleDecompositionAndSymmetricPolytopeBrick.elliptic_divisor_degree_zero_and_weierstrass_factor_cancellation` (Divisor-degree and Abel-sum cancellation for the ratio of two doubly-periodic meromorphic candidates sharing zero/pole multiplicities and divisor centres.)
- **80-dps Witness**: `computations/probes/thimble-decomposition-and-symmetric-polytope-brick.witness.json` (`scriptHash: e55db77fb2bb`, `scriptCommitSha: 6020aea5785046b552772c9a42fc52ac2db9f3a2`).

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8235 (`QOU/QBeta/ThimbleDecompositionAndSymmetricPolytopeBrick.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8235 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.

## 2026-11-22 — applicability verdict (STRICT review, wave-2 brief)

**APPLIES.** pure mathematics; no retired premise found (grep for photon/trefoil/convention C/census/muon pin/virtual photon: none); claim is hollow (vacuous brick PR, see note above), the open work stands.
