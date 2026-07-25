---
# qou-ogrk
title: 'A2 (leg 1): prove Cov_Planch(ln f, omega3) <= 0 via Ivanov-Olshanski 2nd-order covariance'
status: in-progress
type: task
priority: high
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T16:29:00Z
parent: qou-v8t7
---

A2 — leg 1: Cov_Planch(ln f, ω₃) ≤ 0. ADVANCE (2026-07-25 hook/Frullani reduction). Exact reduction to a clean one-parameter sign: (1) hook-length formula ln f=ln n!−Σ ln h ⇒ Cov(ln f,ω₃)=−Σ_v ln(v)ν_v, ν_v=Cov(N_v,ω₃); moments Σν_v=0, Σv²ν_v=Cov(Σh²,ω₃)=Var(ω₃)=n(n-1)(n-2)/3 via the CLASSICAL IDENTITY Σ_□h²=Σ_□c²+n² (verified all λ). (2) Frullani ⇒ EXACT integral rep Cov(ln f,ω₃)=∫_0^∞(1/s)Cov(H_s,ω₃)ds, H_s=Σ_□ e^{−s h} (verified n≤10). REDUCTION: A2 ⇐ Cov_Planch(H_s,ω₃)≤0 ∀s>0, VERIFIED strictly<0 on interior (fine grid n≤13). OPEN sub-problem: prove Cov(H_s,ω₃)≤0 ∀s>0 (H_s a hook functional ∉ algebra A; the dim²→dim³ obstruction trades log for exp). Materially cleaner target: a single positive analytic statistic with 2 exact moment constraints (Σν_v=0, Σv²ν_v=|C₃|). Audit: 2026-07-25-covariance-kernel-A2-hook-reduction.md



A2 ADVANCE 2 (2026-07-25 polynomial-positivity). Exact reduction: with P(x)=Sum_v nu_v x^v (nu_v=Cov(N_v,omega3)), Cov(H_s,omega3)=P(e^{-s}), P(0)=P(1)=0 => P(x)=x(x-1)R(x), deg R=n-2; x(x-1)<0 on (0,1) => A2 <== R(x)>=0 on (0,1). VERIFIED n<=15: R>0 on [0,inf) (all real roots negative, no positive real root). Moment tower M_k=Cov(Sum h^k,omega3): M_0=0, M_2=|C3|, M_1..M_8>0. THREE easy-proof certs FALSE: (a) nu single-crossing FALSE for all n>=6 (oscillates, up to 7 changes) -- Karlin variation-diminishing dead; (b) cumulative S_v<=0 has counterexample (n=6 S_2=+1) -- Abel cert dead; (c) R nonneg-coeffs has counterexample (n=6) -- positive-coeff cert dead. OPEN sub-target: prove R has no nonnegative real root for all n (nontrivial dominance; Hurwitz/root-location, not sign-variation). Audit: 2026-07-25-covariance-kernel-A2-polynomial-positivity.md
