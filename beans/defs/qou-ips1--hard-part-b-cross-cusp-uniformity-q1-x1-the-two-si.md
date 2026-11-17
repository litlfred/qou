---
# qou-ips1
title: 'HARD: Part B cross-cusp uniformity (q→1⁺, x→1⁻) — the two-sided/complex analytic successor to B3.1-B3.5; iπ branch-phase assembly (algebraic pieces log_neg_factor_split + LiTwo_one already sorry-free)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T20:47:13Z
updated_at: 2026-11-17T10:23:09Z
parent: b9cj
---


## 2026-07-24 progress — building block landed (Part B still open)

Formalize-first chip landed on PR #4173 (`DilogPartBBranchPhase.lean`, sorry-free):
- `clog_one_sub_of_gt_one` — `Log(1-w) = log(w-1) + i*pi` (w>1), the branch phase.
- `clog_one_sub_pole_phase_split` — `Log(1-w) = log w + log(1-w^-1) + i*pi`, the
  exact per-factor pole + regularized-piece + branch-phase split the Part-B audit
  subtracts (no free parameter).

Still open (the hard analytic core): the *uniform* cancellation of the i*pi tower
+ linear pole across the cusp, i.e. that the sum over negative factors of the
subtracted regularization converges (uniformly in the q->1+ x n->inf scaling) to
Li2(x) - pi^2/3. Two-sided Tauberian successor to B3.1-B3.5; needs complex/
meromorphic uniformity, not just the per-factor identity. Bean stays open.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 83 Execution Note (2026-11-17T10:23:09Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8301`](https://github.com/litlfred/qou/pull/8301) (`feat/qou-b9cj-1gkf-gz37-ips1-ized-m1nz`, HEAD `8def28bdd6676a091a84204c0314f39da9ee6d5c`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/GaroufalidisZagierS3BlockAndFiveTwoDiscBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/garoufalidis_zagier_s3_block_and_five_two_disc_brick_probe.py` & `computations/probes/garoufalidis-zagier-s3-block-and-five-two-disc-brick.witness.json` (`scriptCommitSha = d726ce17152d0bdd416fbd50d86ba08930c726e7`, `scriptHash = 1b13751c9d60`, `outputHash = 36c8353af8986ccd33f16fae6cef94ba4dab83e96f5a0e688d772b07b9d32e72`).
