---
# qou-6x9g
title: 'PROVE(lean): finite_cascade_depth — theorem finite_cascade_depth : (ctx.N_modes : ℝ) ≤ (3 : ℝ) / 4 * Real.log ctx.Re_q / Real. [cited manuscript]'
status: todo
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-l2vh
---

**File:** `QOU/FluidDynamics/q_turbulence_spectrum.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_turbulence_spectrum.lean

### `finite_cascade_depth`  —  line 139  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem finite_cascade_depth : (ctx.N_modes : ℝ) ≤ (3 : ℝ) / 4 * Real.log ctx.Re_q / Real.log ctx.q `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/fluid-dynamics/q-turbulence-spectrum.md
- **Tractability:** N_modes ≤ (3/4)·log Re_q/log q cascade-depth bound; real-analysis estimate over context.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8292, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
