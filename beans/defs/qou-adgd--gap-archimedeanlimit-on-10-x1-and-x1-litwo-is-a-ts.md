---
# qou-adgd
title: 'GAP: ArchimedeanLimit on [-1,0), x=1 and x>1 (LiTwo is a tsum, so the class needs Re Li2 there)'
status: in-progress
pr: 8212
type: task
created_at: 2026-11-15T18:12:20Z
updated_at: 2026-11-22T22:05:00Z
parent: qou-r9ih
---

Issue #7942, PR #7946. ArchimedeanLimit is proved on (0,1) on main (DilogPartAConvergence.archimedeanLimit_Ioo). PR #7946 proves it FALSE for x < -1 (ArchimedeanLimitDomain.not_archimedeanLimit_of_lt_neg_one), because LiTwo is a tsum and is 0 when |x|>1 (not summable), while the q-product limit is not 0. Open: [-1,0) (the series converges; needs the alternating/Abel exchange), x=1 (zeta(2) boundary), and x>1 (statement must be restated with Re Li2 or an analytic continuation, not the tsum). No alpha_em Lean theorem takes ArchimedeanLimit as a hypothesis; it appears only in docstrings.


## Progress Update (2026-11-16T21:42:42Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/ExtendedBlochFlatteningAndGaussianCell.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/extended-bloch-flattening-and-gaussian-cell.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8212 (`6f86defb7b9ef2d83e38ac9d5dd375a7109fbabd`); keeping `status: in-progress` until PR merges.

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8212 (`QOU/QBeta/ExtendedBlochFlatteningAndGaussianCell.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8212 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.

## 2026-11-22 — (-1, 0) proved (wave-2, thread "Work dilogarithm and Bloch beans")

`QOU.Archimedean.archimedeanLimit_neg_Ioo : y < 0 → -1 < y → ArchimedeanLimit y`, new file `QOU/Archimedean/ArchimedeanLimitNegative.lean`, commit `a5ee034a3c` on branch `claude/bloch-group-complex-2026-11-22` (PR waits on the owner's go). Route: `denomPolyLocal_mul_neg` (`D_n(x;q) D_n(-x;q) = D_n(x²;q²)`), `LiTwo_add_LiTwo_neg` (`Li₂(x) + Li₂(-x) = Li₂(x²)/2` for `|x| ≤ 1`), then the proved `(0,1)` case at `x` and at `x²` (with `q²`), and `(1-q)/(1-q²) = 1/(1+q)`. Sorry-free; axioms `[propext, Classical.choice, Quot.sound]`; `lean-verify` exit 0.

Still open on this bean: the endpoint `x = -1` (the same route needs the limit at `x² = 1`), `x = 1`, and the restatement for `x > 1`. The PR #8212 note above does not bear on any of this.
