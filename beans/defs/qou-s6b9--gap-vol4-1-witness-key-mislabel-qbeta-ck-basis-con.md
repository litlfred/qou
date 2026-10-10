---
# qou-s6b9
title: 'GAP: Vol(4_1) witness key mislabel — qbeta_ck_basis_constrained_pslq.py:313 needs producer re-run'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T15:05:13Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** The key rename is in both the producer (50c8eb422f) and the regenerated witness (2026-09-15, line 107). The witness's red c3 assertion belongs to qou-v6wz, not to this bean.

Evidence: The producer label was fixed by `50c8eb422f` (2026-08-18, "zdz5: drain the 2 genuine Vol(4_1) naming defects"). `computations/probes/qbeta_ck_basis_constrained_pslq.py:372` emits `"Vol(4_1)=2*Cl_2(pi/3)=6*Lambda(pi/3)"`. The committed witness `qbeta-ck-basis-constrained-pslq.witness.json:107` carries that key, value 2.029883212819307… = Vol(4₁) (computedAt 2026-09-15). The witness is honestly red: `allPassed false`, `extraction_chain_reproduces_cache_c3` fails with c3 = −974.38. That is the qou-v6wz defect, not this bean's. Blocker qou-u6cz was scrapped as a duplicate of qou-v6wz.

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
