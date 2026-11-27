---
# qou-e1uf
title: 'Constructive 6: moments and q-CLT as combinatorial identities'
status: todo
type: task
priority: low
tags:
    - constructive
created_at: 2026-11-27T14:50:13Z
updated_at: 2026-11-27T23:15:09Z
parent: qou-dk7p
---

Doc item 6. 26 files (QClt, Stieltjes, FrechetShohat, Plancherel asymptotics). Options 6.1 Touchard-Riordan pair-partition moments, RSK counts (recommended); 6.2 finite-n only; 6.3 leave.

2026-11-27 (qou#9747, 84dd6045d): exact probe — for tr_M(S_n^k) under convention D (U_q(sl2) quantum trace, product state), m4/m2^2 -> 3 exactly at q=11/10,3/2,2; pinned q-Gaussian 2+q fails for q != 1 (classical CLT by locality + Markov). Also: QCltCut.momentSequence is a FREE field, class trivially instantiable — must be tied to tr_M(S_n^k) before it means anything. Audit docs/audits/2026-11-27-qclt-fourth-moment-classical.md. Stays open.

2026-11-27: QCltCut restated on PR #9747 (commit 0714e7fb8): moments from a tracial state + sum; q_eq_one_of_fourth_limit proved (classical 4th moment forces q=1); ClassicalClt = q=1 member. Bridge from QCltNonCommutative removed. OPEN: ClassicalClt instance for tr_M (needs general-n Markov trace; proposed cumulant/formal-group route). Stays open.

2026-11-27: PR #9817 (Hecke thread) adds a general-n Markov trace = U_q(sl2) spin-chain quantum trace over any field; use it as the state for the tr_M ClassicalClt instance.

2026-11-27: step 1 landed (bcdc06363, QCltMarkovSecondMoment.lean): tau(S_n^2)=n(δε−ε²) for every MarkovTower; secondMoment_converges. Next: step 2 cluster factorisation (needs a shift map TL_k→TL_{k+m} or the concrete spin chain of PR #9817), step 3 pair count, step 4 remainder bound with [Archimedean K], step 5 instance.
