---
# qou-fuil
title: 'PROVE(lean): Ctil_has_nonreal_root — theorem Ctil_has_nonreal_root : ∃ y : ℂ, Ctilℂ y = 0 ∧ y.im ≠ 0  [cited manuscript]'
status: completed
type: task
priority: normal
tags:
    - cited-sorry
    - paper-qou
    - tractable
    - reorg-2026-10-04
    - lean
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-10-04T15:13:33Z
parent: qou-k1mq
---

STILL-OPEN (honest). Statement is TRUE (verified: Ctil = y^4+4y^3+2y^2-10y-8 has roots ~1.498, ~-0.849 real and ~-2.325+-0.942i complex conjugate). But the triage 'norm_num/explicit-witness discharge' is MATHEMATICALLY WRONG: Ctil is irreducible over Q (no rational root; no integer/rational quadratic factorization, exhaustively checked), so the complex roots are irrational algebraic numbers with no elementary closed form -> NO explicit witness to hand norm_num.

The two rigorous routes both need Mathlib-v4.24.0-absent infra:
(A) DISCRIMINANT: assume all 4 roots real, extract Vieta (e1=-4,e2=2,e3=10,e4=-8 via Polynomial.coeff_eq_esymm_roots_of_card -- this API DOES exist), then prod_{i<j}(ri-rj)^2 = disc = -44208 < 0 contradicts product-of-squares >= 0. Ideal membership CONFIRMED in sympy (disc+44208 in <Vieta>). BLOCKER: the degree-12 identity prod(ri-rj)^2 = -44208 mod Vieta cannot be discharged offline: nlinarith too weak (needs degree-12 cert; Newton inequalities pass so no low-degree SOS), polyrith network-blocked, and explicit linear_combination cofactors are astronomical (714-term degree-11) -- unmanageable/brittle source. Plus root-extraction scaffolding (Multiset card=4 destructuring + esymm over C + real conversion) is heavy.
(B) REAL-ROOT-COUNT via calculus: show P has <=2 real roots (with mult) since P' has a single real root => P is strictly dec-then-inc with a unique min at m, P(m)<0; combine with 4 complex roots => a non-real one. Needs deriv/StrictMonoOn/IVT analysis nested two levels (P' root-count needs P''), ~150-250 lines, high risk with search tools 403-blocked.

Root API confirmed available: Polynomial.roots, splits_iff_card_roots, coeff_eq_esymm_roots_of_card, Complex.exists_root, Multiset.prod_X_sub_C_coeff. NOT the wall -- the degree-12 discriminant identity is. Recommend: either add a small quartic-discriminant lemma to QOU/Mathlib, OR prove the calculus real-root-count as its own sizable brick. Left sorry intact + -- Ref: comment. Branch claude/prove-tractable-cited-sorries-2026-08-01.



--- UPDATE 2026-08-02 (agent ctil-root) — PROVED SORRY-FREE (awaiting human close) ---
Branch claude/prove-ctil-nonreal-root-2026-08-02, commit 07f0ff8f. File compiles lean-direct exit 0, real-sorry 1 -> 0.
Route A (discriminant) taken, built from scratch since Mathlib v4.24.0 has NO quartic-discriminant = prod(ri-rj)^2 bridge:
  * Ctil_no_four_real_roots (helper, over R): for reals with C-tilde's Vieta data (e1=-4,e2=2,e3=10,e4=-8), the Vandermonde square prod_{i<j}(ri-rj)^2 EQUALS the explicit 16-term discriminant polynomial in the elementary symmetric functions -- a PURE ring identity (verified in sympy: V^2 = Disc(coeffs) exactly) -- whose value at those Vieta numbers is -44208 < 0; but a real Vandermonde square is >= 0 (sq_nonneg). Contradiction. Key: discriminant-in-elementary-symmetrics is only 16 terms, so no monster cofactors -- the 714-term linear_combination the prior note feared is avoided entirely.
  * Ctil_has_nonreal_root: C-tilde monic deg 4 splits over C (IsAlgClosed.splits_codomain + eq_prod_roots_of_monic_of_splits_id + Multiset.card_eq_four -> roots = {a,b,c,d}); if all four had im=0 they'd be real, Vieta feeds the helper -> False.
  * Vieta over R extracted via linear_combination of the real polynomial identity hr at the 4 points {0,1,-1,2} (Vandermonde weights precomputed).
Imports added: Mathlib.Tactic.ComputeDegree, Mathlib.Tactic.LinearCombination. maxHeartbeats 4000000 on the helper (degree-12 ring). DO NOT CLOSE -- human-only per AGENTS.md 4a.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] k1mq child: no real sorry left in target file. Ctil_has_nonreal_root theorem uncond, 0 sorry | previously stalled; last update 2026-08-02
