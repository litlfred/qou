---
# qou-xzlt
title: 'L4-1: refined s_n expansion — second-order Euler-Maclaurin for log-sine sums (the crux)'
status: in-progress
pr: 8217
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:36:11Z
updated_at: 2026-11-22T22:50:00Z
parent: qou-r9ih
---


Feasibility pass DONE (docs/audits/2026-08-11-l41-euler-maclaurin-feasibility.md): FEASIBLE multi-session, decomposed into qou-me9q (exact cell-defect representation, first), qou-itg0 (Stirling half-log — Mathlib Stirling.lean exists, 19 thms), qou-q8lc (uniform O(1/N) cot-bound remainder, the genuinely new estimate). vdV's own route avoids the Euler-Maclaurin endpoint singularity; Mathlib has no E-M formula anyway.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-11 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update (2026-11-16T22:04:01Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/SteepestDescentEulerMaclaurinAndFrobeniusDiagonal.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/steepest-descent-euler-maclaurin-and-frobenius-diagonal.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8217 (`f4d145a08828886b4eba631166b3e61717adc12d`); keeping `status: in-progress` until PR merges.

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8217 (`QOU/QBeta/SteepestDescentEulerMaclaurinAndFrobeniusDiagonal.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8217 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.

## 2026-11-22 — applicability verdict (STRICT review, wave-2 brief)

**APPLIES.** pure mathematics; no retired premise found (grep for photon/trefoil/convention C/census/muon pin/virtual photon: none); claim is hollow (vacuous brick PR, see note above), the open work stands.
