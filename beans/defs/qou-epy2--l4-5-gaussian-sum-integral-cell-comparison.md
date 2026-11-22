---
# qou-epy2
title: 'L4-5: Gaussian sum -> integral cell comparison'
status: in-progress
pr: 8212
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:36:11Z
updated_at: 2026-11-22T22:50:00Z
parent: qou-r9ih
---

RE-SCOPED 2026-08-19 -- this brick is a Gaussian sum/integral CELL COMPARISON,
which is exactly what QOU/MathlibExt/GaussianSumBound (integral_exp_neg_mul_sq_le,
sum_exp_neg_mul_sq_le) and CorrectedTrapezoid / CompositeEulerMaclaurin already
provide generically.  Grep before writing.  Audit:
docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md


## Progress Update (2026-11-16T21:42:42Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/ExtendedBlochFlatteningAndGaussianCell.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/extended-bloch-flattening-and-gaussian-cell.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8212 (`6f86defb7b9ef2d83e38ac9d5dd375a7109fbabd`); keeping `status: in-progress` until PR merges.

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8212 (`QOU/QBeta/ExtendedBlochFlatteningAndGaussianCell.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8212 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.

## 2026-11-22 — applicability verdict (STRICT review, wave-2 brief)

**ALREADY-DONE.** its own 2026-08-19 rescope says the cell comparison is GaussianSumBound.lean:43/57 + CorrectedTrapezoid/CompositeEulerMaclaurin, all on main; left in-progress only for a consumer to confirm it needs nothing more.
