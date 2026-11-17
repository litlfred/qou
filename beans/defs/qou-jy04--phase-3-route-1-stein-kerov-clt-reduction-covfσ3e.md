---
# qou-jy04
title: 'Phase 3 route 1: Stein + Kerov-CLT reduction Cov(f,Σ3)~E[f]Cov(ln f,Σ3)'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:21:37Z
updated_at: 2026-11-17T11:44:00Z
parent: qou-m6dn
---

Route 1 (Stein/Kerov-CLT). Phases 5-7 done. Phase 5: exchangeable pair, ω₃ eigenfunction τ₃=3/n, local Dirichlet-form reformulation. Phase 5b: per-edge certificate FAILS. Phase 6 (#4170): marginal 3-cycle Berry-Esseen (rate ~n^-0.3, Var_P(ω₃)=n(n-1)(n-2)/3). Phase 7 (THIS): transfer-error BOUND. g(θ)=E_{2+θ}[ω₃]; kernel=g(1), main=g'(0)=Cov_Planch(ln f,ω₃)<0; Taylor remainder R=g(1)-g'(0). BOUND HOLDS 40dps n≤14: r=g(1)/g'(0)∈(0.54,0.87), |R|/|main|=|r-1|∈(0.13,0.46)<1 ⇒ non-Gaussian correction ≤46%, cannot flip sign. NQD route ELIMINATED (Hoeffding kernel >0 pointwise, bad count grows). Kernel≤0 ⇐ [Cov(lnf,ω₃)≤0] AND [|remainder|<|linear|], both verified numerically. OPEN CORE: rigorous Plancherel-cumulant control of g^(m)(0) via Kerov CLT. Audit: 2026-07-24-covariance-kernel-effective-stein-step2-transfer-bound.md



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 87 Progress (`litlfred/qou#8326`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/JetHorizonHabiroAndSteinMarginBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all directory-mode static audits).
- **80-dps Probe & Witness**: `computations/probes/jet_horizon_habiro_and_stein_margin_brick_probe.py` & `computations/probes/jet-horizon-habiro-and-stein-margin-brick.witness.json` (`scriptCommitSha = 34352b344244b9e4cceaf3e3a4c56aa375f7bdc5`, HEAD `10540538cb20efacf68a8b53a97722f79167a3a5`, `allPassed = true`).
