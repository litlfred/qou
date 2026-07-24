---
# qou-jlto
title: 'C (SUPPORT): explicit numerical pin — Hodge Gram from Braden-Northover τ₀·C vs Markov Gram on std block at q₀ (Hoefsmit); extract/falsify scale c'
status: in-progress
type: task
priority: normal
created_at: 2026-07-24T16:54:55Z
updated_at: 2026-07-25T03:15:56Z
updated_at: 2026-07-24T21:05:32Z
parent: qou-6ufi
---


## 2026-07-24 — Option C Markov-side pin landed (PR #4168)
- (i) contravariant-form space nullity = 1 → scalar-commutant/Schur premise of #4160 CONFIRMED for the actual (4,1) block at q₀.
- (ii) unique invariant form symmetric + diagonal (seminormal Gram) → IsSymm premise confirmed.
- (iii) w_(4,1)(q₀) = d_q²/[5]_q! ≈ 0.128620 = Markov-side pin of c.
- OPEN remaining: Hodge-polarization normalization (Braden–Northover period matrix); c = markov_norm/hodge_norm. Also sub-piece (ii) S₅-equivariance of τ-image. No fabrication; 1/(8π) phase-4.
