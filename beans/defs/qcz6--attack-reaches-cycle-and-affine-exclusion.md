---
# qcz6
title: 'ATTACK: q-Collatz reaches_cycle convergence + affine (A≠1) cycle exclusion'
status: in-progress
type: feature
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:46:17Z
updated_at: 2026-11-18T12:11:25Z
parent: qcz14
---

The two genuinely-open pieces of conj:q-collatz (within a QOU), post-cleanup.
Both are hard (q-analog of open classical Collatz); attack incrementally,
formalize-first, no fabricated proofs. Anti-fit / anti-laundering applies:
a probe is evidence, only a derivation closes.

CURRENT PROVED BASE (do not redo): balanced_holonomy_excluded (A=1),
qcollatz_fundamental_odd/even_step (2-cycle), qcollatz_domain_not_forward_invariant,
qi3_sub_q_qi2. Census (period<=18) + divergence probe (6045 seeds) = negative
evidence only.

Children: qcz7 (convergence route), qcz8 (affine-exclusion route),
qcz9 (chi(A) scoping fix — independent, do first, cheap).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 70 Update (2026-11-18T12:11:25Z)
- Addressed in PR `litlfred/qou#8466` (HEAD `57eaba11f749480e8b98e9c5a6020b79b2d5a529`, C1 `ac0018f69fff5e2dec418784b19d5c431d4ed5f3`).
