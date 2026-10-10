---
# qou-jlto
title: 'C (SUPPORT): explicit numerical pin — Hodge Gram from Braden-Northover τ₀·C vs Markov Gram on std block at q₀ (Hoefsmit); extract/falsify scale c'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:54:55Z
updated_at: 2026-10-04T15:12:03Z
parent: qou-3l2l
---


## 2026-07-24 — Option C Markov-side pin landed (PR #4168)
- (i) contravariant-form space nullity = 1 → scalar-commutant/Schur premise of #4160 CONFIRMED for the actual (4,1) block at q₀.
- (ii) unique invariant form symmetric + diagonal (seminormal Gram) → IsSymm premise confirmed.
- (iii) w_(4,1)(q₀) = d_q²/[5]_q! ≈ 0.128620 = Markov-side pin of c.
- OPEN remaining: Hodge-polarization normalization (Braden–Northover period matrix); c = markov_norm/hodge_norm. Also sub-piece (ii) S₅-equivariance of τ-image. No fabrication; 1/(8π) phase-4.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
