---
# qou-v1jg
title: 'q-gradient interface: matter/antimatter boundary forced through q=1; branch swap s -> -s'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T12:24:18Z
updated_at: 2026-10-04T15:13:34Z
parent: qou-ddmn
---

GATE FOUND (2026-09-07, PR #7077). q=1 is forced as the matter(q>1)/antimatter(q<1) interface by continuity, and it is where (a) the branch-independent part of s^3*r, = (5/27)(q-1)(4q^2-5q+4), has its ONLY real zero (the quadratic factor's discriminant is -39), and (b) the pair-separation residue 2(p+m)sinh(ln q) of prop:crossing-energy-pair-cancellation vanishes and changes sign. BLOCKER: cosmological-chirality-flip.md says e and mu have 'vanishing masses' at q->1 but m_mu/m_e = Vol(4_1)/hbar_q^2 DIVERGES there (206.77 at q0 -> 2.03e8 at q=1.0001). Whether the interface is soft or violent depends on which is right. Settle before any q=1 interface physics.

SETTLED 2026-09-07: BARRIER, not door. sum_lambda y_lambda(H3) converges to exactly 3/4 as q->1 (0.7527 -> 0.75000000). rho does NOT vanish, so m(K)/m_e = Vol*rho/hbar_q^2 diverges and cosmological-chirality-flip.md's 'vanishing masses' has no support. The q=1 layer is self-shielding; domains never contact; CDG98 evaded by an infinite barrier not a small cross-section. Scope (a): measured the y_lambda SUM, not per-knot rho = sum y_lambda chi^lambda, which could still cancel for a specific knot.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
