---
# qou-fuil
title: 'PROVE(lean): Ctil_has_nonreal_root — theorem Ctil_has_nonreal_root : ∃ y : ℂ, Ctilℂ y = 0 ∧ y.im ≠ 0  [cited manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - tractable
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-08-02T00:15:29Z
parent: qou-k1mq
---

STILL-OPEN (honest). Statement is TRUE (verified: Ctil = y^4+4y^3+2y^2-10y-8 has roots ~1.498, ~-0.849 real and ~-2.325+-0.942i complex conjugate). But the triage 'norm_num/explicit-witness discharge' is MATHEMATICALLY WRONG: Ctil is irreducible over Q (no rational root; no integer/rational quadratic factorization, exhaustively checked), so the complex roots are irrational algebraic numbers with no elementary closed form -> NO explicit witness to hand norm_num.

The two rigorous routes both need Mathlib-v4.24.0-absent infra:
(A) DISCRIMINANT: assume all 4 roots real, extract Vieta (e1=-4,e2=2,e3=10,e4=-8 via Polynomial.coeff_eq_esymm_roots_of_card -- this API DOES exist), then prod_{i<j}(ri-rj)^2 = disc = -44208 < 0 contradicts product-of-squares >= 0. Ideal membership CONFIRMED in sympy (disc+44208 in <Vieta>). BLOCKER: the degree-12 identity prod(ri-rj)^2 = -44208 mod Vieta cannot be discharged offline: nlinarith too weak (needs degree-12 cert; Newton inequalities pass so no low-degree SOS), polyrith network-blocked, and explicit linear_combination cofactors are astronomical (714-term degree-11) -- unmanageable/brittle source. Plus root-extraction scaffolding (Multiset card=4 destructuring + esymm over C + real conversion) is heavy.
(B) REAL-ROOT-COUNT via calculus: show P has <=2 real roots (with mult) since P' has a single real root => P is strictly dec-then-inc with a unique min at m, P(m)<0; combine with 4 complex roots => a non-real one. Needs deriv/StrictMonoOn/IVT analysis nested two levels (P' root-count needs P''), ~150-250 lines, high risk with search tools 403-blocked.

Root API confirmed available: Polynomial.roots, splits_iff_card_roots, coeff_eq_esymm_roots_of_card, Complex.exists_root, Multiset.prod_X_sub_C_coeff. NOT the wall -- the degree-12 discriminant identity is. Recommend: either add a small quartic-discriminant lemma to QOU/Mathlib, OR prove the calculus real-root-count as its own sizable brick. Left sorry intact + -- Ref: comment. Branch claude/prove-tractable-cited-sorries-2026-08-01.
