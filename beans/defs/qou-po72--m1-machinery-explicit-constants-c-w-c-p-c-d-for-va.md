---
# qou-po72
title: 'M1 machinery: explicit constants C_W, C_P, C_D for Var(Sum c^2), Cov, linearized Var(SumD2)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T01:34:21Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-m6dn
---

2026-08-29 (PR #5969): de-poissonized (CS) leading constants DERIVED in closed form.
  V_A = 8/(9 pi^2) [k>=2 frozen; NOT step-1's poissonized 8/pi^2], Var(omega3) lead 1/3,
  P = 8/(15 pi), rho_P = 2 sqrt(6)/5 EXACT (pi cancels: rho_P^2 = 24/25), V_D = 0.0415975
  (no elementary form found), margin m_inf = 0.300186 > 0 (reproduces #5901).
  Lean CSMarginCorrelationConstant.lean sorry-free (rhoSq=24/25 generic field; rho=2sqrt6/5 over R).
  OPEN tail: finite-n remainder constants C_A/C_D/C_P hit the Olver-Bessel wall (same as qou-tvok).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 91 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/HookEvenMomentAndBorromeanTripleBrick.lean` with 80-dps probe `computations/probes/hook_even_moment_and_borromean_triple_brick_probe.py` and witness `computations/probes/hook-even-moment-and-borromean-triple-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8343 (`feat/qou-b9cj-ogrk-ohaz-omr7-ooqh-po72`, HEAD `8c185bc247a4dfba4e6316715175039c0defb340`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8343, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-29: "po72(qou-k5r5): de-poissonized (CS) leading constants in closed form; rho_P = 2 sqrt(6)/5"). The work may be partly or fully done. Read the bean before you close it.
