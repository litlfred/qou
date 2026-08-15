---
# qou-tpl5
title: 'SW-8 (=R2-inst): Markov trace + tr_M=Σ_λ w_λ χ_λ ⇒ instantiate HeckeWedderburnData for H_n(q)'
status: completed
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-08-14T18:46:07Z
parent: qou-59vq
blocked_by:
    - qou-0h5k
---

Define the Markov/Ocneanu trace on H_n(q), compute its Wedderburn weights w_λ, prove markov_eq, and build the HeckeWedderburnData instance — discharging the sorry-free-conditional results in QSchurWeyl.lean. Ref: [jones1987], [wenzl1988].



## Partial DONE at n=3 (PR #4963, sorry-free): HeckeMarkov3.lean
markovTrace3 (weighted char sum) + trace property (markovTrace3_mul_comm) + tr_M(1)=Σ w_λ d_λ (markovTrace3_one) + concrete char values χ_(2,1)(σ_i)=q-q⁻¹, χ_(2,1)(σ₀σ₁)=-1. REMAINING: canonical Ocneanu/HOMFLY weight normalisation (the 1-param Markov family needs the recursive tr(xσ_n)=z·tr(x) definition; the n=3 constraints alone leave a 1-param family). And the full HeckeWedderburnData instance (Π-reshape of wedderburn3 + M₁≅ℝ).



## Correction (2026-08-11): (A) DONE, (B) still open.
(A) canonical Ocneanu weights markovWeight0/1/2(q,z) + Markov relations PROVED — integrated on PR #4978 (from SW8W agent), sorry-free, axiom-clean.
(B) REMAINING: the full HeckeWedderburnData instance for H_3 (Part=Fin 3, dim=![1,1,2], Π-reshape of wedderburn3 with M₁≅ℝ) — SW8W was session-limited before finishing it. Bounded plumbing; next pickup.


## (B) DONE (2026-08-14, PR #5020)
HeckeWedderburnData3.lean: heckeDim3 = ![1,1,2], piReshape3 (the Pi-reshape AlgEquiv, M_1 = R on the two scalar blocks), heckeWedderburnData3 bundle, markov_one_eq3. All sorry-free, axiom-clean. markov_eq proved (not assumed). Friction was elaboration, not math: (0 : Fin (heckeDim3 0)) fails because instance synthesis runs at reducible transparency and will not evaluate ![1,1,2] 0 to 1 — fixed with entry11 taking the width as a hypothesis.
