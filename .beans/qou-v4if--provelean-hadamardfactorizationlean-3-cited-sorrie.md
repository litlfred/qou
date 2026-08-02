---
# qou-v4if
title: 'PROVE(lean): HadamardFactorization.lean — 3 cited sorries [cited manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - repo-infra
    - tractable
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-08-02T00:15:53Z
parent: qou-k1mq
---

STILL-OPEN (honest) for norm_one_sub_weierstrassFactor_le (the PI-2 brick). Statement TRUE and standard (Ahlfors 5.3): for ||z||<=1, ||1 - E_p(z)|| <= ||z||^(p+1), E_p(z)=(1-z)exp(sum_{k<p} z^(k+1)/(k+1)).

NOT tractable in Mathlib v4.24.0 within reason. The classical proof is NOT an elementary norm inequality: it goes through the power-series identity E_p'(z) = -z^p * exp(g(z)) with g nonneg-coeff, hence 1 - E_p(z) = z^(p+1) * sum_{n>=0} d_n z^n with d_n >= 0 and sum d_n = 1 - E_p(1) = 1; then |1-E_p(z)| <= ||z||^(p+1) sum d_n ||z||^n <= ||z||^(p+1). Formalizing needs: (i) exp of a nonneg-coeff formal/analytic series has nonneg coeffs, (ii) term-by-term integration of E_p' to get the coeff structure, (iii) evaluating the coeff-sum at z=1 via E_p(1)=0. Mathlib has Complex.exp series + FormalMultilinearSeries but no Weierstrass primary factor / canonical-product infra; assembling (i)-(iii) is a multi-hundred-line build. The file's own roadmap marks it PI-2 'not elementary; deferred', and the other two sorries in the file (multipliable_canonicalProduct PI-3, hadamard_factorization PI-5) are strictly harder (Jensen/Nevanlinna).

No sub-case removes the sorry (statement is universally quantified over p and ||z||<=1; p=0 is just the equality ||z||=||z||). Left sorry + -- Ref: [Ahlfors] intact; NOT weakened or faked. Recommend building the nonneg-coeff exp-series lemma as a dedicated brick first. Branch claude/prove-tractable-cited-sorries-2026-08-01.
