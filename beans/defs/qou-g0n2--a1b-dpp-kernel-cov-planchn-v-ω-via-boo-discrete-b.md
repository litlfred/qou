---
# qou-g0n2
title: 'A1b (DPP kernel): Cov_Planch(N_v, ω₃) via BOO discrete-Bessel determinantal kernel'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T16:37:35Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-m6dn
---


DELIVERABLE 1 (2026-07-25). Maya-diagram quadratic representation VERIFIED exact (n<=10): N_v=Sum_a(1-m_a)m_{a+v} (hook=particle-hole distance), omega3=Sum_v v^2 N_v - n^2 - C(n,2) (via Sum h^2=Sum c^2+n^2). Occupations determinantal under poissonized Plancherel (BOO discrete-Bessel, math/9905032) => Cov(N_v,N_w) has Wick/kernel reduction. OBSTRUCTION found: fixed-n Sum nu=0 holds because Sum N_v=n constant (|lambda|-comovement projected out); at poissonized level Cov_theta(N_v,Sum h^2) is ALL POSITIVE (|lambda|-fluctuation dominates). So DEPOISSONIZATION (condition on |lambda|=n) is the real difficulty, not the kernel algebra. NEXT: |lambda|=n-conditioned discrete-Bessel kernel / steepest-descent depoissonization with |lambda|-mean-field subtraction. Audit: 2026-07-25-covariance-kernel-A1b-dpp-maya-representation.md



DELIVERABLE 1b (2026-07-25, bounded probe, NOT yet PR'd — fold into deliverable 2). Tested linear-response (Gaussian mean-field) depoissonization: Cov_n(A,B) ~ Cov_theta(A,B) - Cov_theta(A,|lambda|)Cov_theta(B,|lambda|)/Var(|lambda|) at theta=n. RESULT: INSUFFICIENT — recovers only 5-8/8 signs, values wrong (exact n=10 nu is fully alternating -+-+-+-+, linear-response gives -+-----+). So |lambda|=n conditioning is NON-PERTURBATIVE; the cheap poissonized+correction shortcut fails. Route needs the full fixed-n discrete-orthogonal-polynomial (Hahn/Charlier-type) kernel. This is research-grade asymptotics with asymptotic-only (large-n) payoff — NOT a finite-n proof of the conjecture. Deliverable 2 = the fixed-n DOP kernel or accept large-n-only asymptotic sign.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 86 Progress (`litlfred/qou#8317`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/BesserDeJeuDilogAndMayaHookVarianceBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all 7 static audits).
- **80-dps Probe & Witness**: `computations/probes/besser_de_jeu_dilog_and_maya_hook_variance_brick_probe.py` & `computations/probes/besser-de-jeu-dilog-and-maya-hook-variance-brick.witness.json` (`scriptCommitSha = 4d5b778d1b105fc173cd0374f785742bf18bf727`, HEAD `9739386c32e9d7fc534b2e9229d93f0174f0cf95`, `allPassed = true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8317, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
