---
# qou-7igi
title: 'EPIC [Q-Drain-9]: Delta_lambda Plancherel Covariance, REV_n = O(sqrt n) & Jack/Kerov Asymptotics'
status: in-progress
type: epic
priority: high
created_at: 2026-11-23T20:55:50Z
updated_at: 2026-11-27T21:52:48Z
parent: qou-hksc
blocking:
    - qou-xip2
---

**Theme:** Delta_lambda Plancherel Covariance, REV_n = O(sqrt n) & Jack/Kerov Asymptotics
**Rationale:** Proves REV_n upper/remainder bounds, Ivanov-Olshanski / BOO Bessel Plancherel covariance Cov(f, omega_3) <= 0, and deuteron-wall resummation.
**Child Beans (11):** `qou-fxym`, `qou-4wl1`, `qou-ogrk`, `qou-v8t7`, `qou-g0n2`, `qou-jy04`, `qou-ik5e`, `qou-r91v`, `qou-cds5`, `qou-hok7`, `qou-zrx2`

### Prioritized Beans in This Batch
- **`qou-fxym`** (`high`, `in-progress`) — A3 (headline): prove REV_n = O(sqrt n) — the beta-bound is the weak step, not the (l,W) reduction *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-4wl1`** (`high`, `todo`) — A3 (leg 2): bound remainder |R|<|g''(0)| via mixed-cumulant (Sniady genus) scaling
- **`qou-ogrk`** (`high`, `todo`) — A2 (leg 1): prove Cov_Planch(ln f, omega3) <= 0 via Ivanov-Olshanski 2nd-order covariance *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-v8t7`** (`high`, `todo`) — ATTACK PLAN: prove Delta_lambda covariance kernel Cov(f,Sc2)<=0
- **`qou-g0n2`** (`high`, `todo`) — A1b (DPP kernel): Cov_Planch(N_v, ω₃) via BOO discrete-Bessel determinantal kernel *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-jy04`** (`high`, `todo`) — Phase 3 route 1: Stein + Kerov-CLT reduction Cov(f,Σ3)~E[f]Cov(ln f,Σ3) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-ik5e`** (`high`, `todo`) — Phase 3 route 3: exact Jack β-derivative dE_β[Σ3]/dβ|_{β=2} (engine for route 1) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-r91v`** (`high`, `todo`) — Phase 4: prove β=2 maximises E_β[C₂] on [2,∞) (Jack/β-Plancherel concentration or lit match) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-cds5`** (`high`, `todo`) — S5 (SCIENCE): verify the r* D-frame band BEFORE re-scoring the six Delta_lambda ansaetze
- **`qou-hok7`** (`high`, `in-progress`) — Deuteron-wall resummation: classical Borel on q=1 period is the WRONG transform (substrate object is q-Gevrey) -> reopen; needs q-Borel of Z_n(q0) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-zrx2`** (`high`, `in-progress`) — GAP: the signed trace difference has an hbar_q^0 classical floor -- it is not a pure deformation observable

### Worker Protocol
- Claim individual child beans via `beans update <bean-id> --status in-progress --body-append "Claimed by <branch> (YYYY-MM-DD)"`.
- Never mark a bean `completed` while an uninstantiated conjecture `class` or explicit `stays open` item remains (AGENTS.md Rule 13a).
- Enforce single-thread CPU caps (`LEAN_NUM_THREADS=1`, `nice -n 15`), zero float64 (`mpmath` >= 50-80 dps), and zero fitting.

Batch 9 Q-Drain-9 complete on origin/claude/backlog-drain-batch9-10-20261123 (2dba8f02dcd): ClassicalTraceFloorParity.lean + DeltaLambdaRStarOrderBounds.lean (0 sorry) + 80-dps witness staged.

## 2026-11-27: square-law inverse + large-tilt obstruction (PR #9757, session_01VQDpPgJRT1LXn57NpaDLVw)
- NEW exact form: cov(n)<=0 iff [3-cycle]Q^{-1}<=0, Q=(1/n!)sum_x x^2 (Q acts on V^lambda by 1/f^lambda; Frobenius-Schur indicator 1). Checked in the class algebra n=3..7 with zero shared code. phi(s)=[sigma]Q^{-s}: phi(1)=kernel, phi'(0)=A2.
- ELIMINATED (structural, Lean decide): "[sigma](e-Q)^m<=0 for all m", i.e. any tilt-uniform or increasing-psi(f) argument. Large-tilt sign = omega_3 at the max-dim shape: +3 at n=18, +1 at n=26; Cov(omega_3,f^s)>0 for s>362.94 at n=18. Lean: HeckeTemperleyLieb/YoungDiagramKernelLargeTilt.lean, not_forall_tiltedSum_nonpos.
- A proof must use s=1 or a bounded s-window. Audit: docs/audits/2026-11-27-covariance-kernel-square-law-inverse.md.
