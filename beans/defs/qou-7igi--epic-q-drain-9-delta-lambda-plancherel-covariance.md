---
# qou-7igi
title: 'EPIC [Q-Drain-9]: Delta_lambda Plancherel Covariance, REV_n = O(sqrt n) & Jack/Kerov Asymptotics'
status: todo
type: epic
priority: high
created_at: 2026-11-23T20:55:50Z
updated_at: 2026-11-23T20:55:50Z
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
