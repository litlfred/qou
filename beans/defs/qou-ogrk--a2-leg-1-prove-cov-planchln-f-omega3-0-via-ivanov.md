---
# qou-ogrk
title: 'A2 (leg 1): prove Cov_Planch(ln f, omega3) <= 0 via Ivanov-Olshanski 2nd-order covariance'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-m6dn
---

A2 — leg 1: Cov_Planch(ln f, ω₃) ≤ 0. ADVANCE (2026-07-25 hook/Frullani reduction). Exact reduction to a clean one-parameter sign: (1) hook-length formula ln f=ln n!−Σ ln h ⇒ Cov(ln f,ω₃)=−Σ_v ln(v)ν_v, ν_v=Cov(N_v,ω₃); moments Σν_v=0, Σv²ν_v=Cov(Σh²,ω₃)=Var(ω₃)=n(n-1)(n-2)/3 via the CLASSICAL IDENTITY Σ_□h²=Σ_□c²+n² (verified all λ). (2) Frullani ⇒ EXACT integral rep Cov(ln f,ω₃)=∫_0^∞(1/s)Cov(H_s,ω₃)ds, H_s=Σ_□ e^{−s h} (verified n≤10). REDUCTION: A2 ⇐ Cov_Planch(H_s,ω₃)≤0 ∀s>0, VERIFIED strictly<0 on interior (fine grid n≤13). OPEN sub-problem: prove Cov(H_s,ω₃)≤0 ∀s>0 (H_s a hook functional ∉ algebra A; the dim²→dim³ obstruction trades log for exp). Materially cleaner target: a single positive analytic statistic with 2 exact moment constraints (Σν_v=0, Σv²ν_v=|C₃|). Audit: 2026-07-25-covariance-kernel-A2-hook-reduction.md



A2 ADVANCE 2 (2026-07-25 polynomial-positivity). Exact reduction: with P(x)=Sum_v nu_v x^v (nu_v=Cov(N_v,omega3)), Cov(H_s,omega3)=P(e^{-s}), P(0)=P(1)=0 => P(x)=x(x-1)R(x), deg R=n-2; x(x-1)<0 on (0,1) => A2 <== R(x)>=0 on (0,1). VERIFIED n<=15: R>0 on [0,inf) (all real roots negative, no positive real root). Moment tower M_k=Cov(Sum h^k,omega3): M_0=0, M_2=|C3|, M_1..M_8>0. THREE easy-proof certs FALSE: (a) nu single-crossing FALSE for all n>=6 (oscillates, up to 7 changes) -- Karlin variation-diminishing dead; (b) cumulative S_v<=0 has counterexample (n=6 S_2=+1) -- Abel cert dead; (c) R nonneg-coeffs has counterexample (n=6) -- positive-coeff cert dead. OPEN sub-target: prove R has no nonnegative real root for all n (nontrivial dominance; Hurwitz/root-location, not sign-variation). Audit: 2026-07-25-covariance-kernel-A2-polynomial-positivity.md



CORRECTION (2026-07-25). The A2 POINTWISE reduction Cov(H_s,omega3)<=0 for-all-s (<=> R>=0 on (0,1)) is FALSE for n>=29 -- verified EXACTLY (first failure n=29, max_s Cov=+0.056 at s~0.52; R gains a root in (0,1) at n=30; grows with n). It was verified only to n<=13/15 -- a small-n artifact. So the polynomial-positivity/pointwise route CANNOT prove A2. BUT: the KERNEL cov(k)=Sum(f)^3 omega3<=0 AND the A2 leg Cov(ln f,omega3)=-Sum ln(v) nu_v<=0 BOTH SURVIVE exactly (k,n<=40); A2 holds by CANCELLATION in the full Frullani integral even though its integrand goes positive. Retracts #4242 'R>0 on [0,inf)' general framing + the 'A2<=>R>=0' equivalence (only R>=0 => A2, false premise). A proof of A2 must be GLOBAL (full signed integral / dimension-functional expansion), not pointwise. Audit: 2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md



SURVIVING STRUCTURE (2026-07-25, after pointwise-route correction). Moment skeleton M_k=Sum v^k nu_v=Cov(Sum h^k, Sum h^2): M_0=0, M_2=|C3|, M_1..M_12>0 ROBUST (n<=40) -- unlike the pointwise property (failed n=29). GF dichotomy: G(t)=Sum nu_v e^{tv}=Sum_{k>=1} t^k M_k/k! is >0 for t>0 (all terms positive) but for t<0 equals Cov(H_s,omega3) (alternating, positive for n>=29) -- same GF, opposite half-lines. ln(v) increasing => A2<=0 robust, but ln concave (not positive power combo) => M_k>0 doesn't close A2 (needs global arg). PROOF LEAD: even-k M_{2j}=Cov(Sum h^{2j},Sum h^2) shifted-symmetric => exact poly in n (deg j+2, positive leading coeff) via Ivanov-Olshanski Prop 5.1 => provable by finite positivity check. Audit: 2026-07-25-covariance-kernel-A2-moment-skeleton.md



PROVED SUB-RESULT (2026-07-25). Executed the even-k proof lead: even hook-power moments M_{2j}=Cov(Sum h^{2j}, Sum h^2)>0 for all n>=3, PROVED with manifest certificates. Exact polys (interp-verified): M_2=n(n-1)(n-2)/3=|C3|; M_4=n(n-1)(n-2)/3*5(n-8/3); M_6=n(n-1)(n-2)/3*7(3n-8)^2 (perfect square). Cofactors manifestly positive (constant/linear-past-root/perfect-square) => theorem. First proved positivity in the epic beyond k<=7 decide. Settles EVEN half of moment skeleton; odd-k empirical; does NOT prove A2 (ln concave). Lean-ready (M_6 = positivity one-liner). Audit: 2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md



M_1 REFORMULATION (2026-08-21). M_1 = Cov_Planch(Sum(i+j), Sum c^2) -- antidiagonal vs diagonal spread (transpose-even, = 2Cov(n_lam,Sc2) = Cov(Sum h,Sum h^2), n<=17). rho ~ 0.85-0.92 near-perfect; Var(Sum c^2)=|C3| exact; no closed form. Route = Kerov CLT integral (open). Audit: 2026-08-21-covariance-kernel-M1-antidiagonal-reformulation.md



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-21 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 91 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/HookEvenMomentAndBorromeanTripleBrick.lean` with 80-dps probe `computations/probes/hook_even_moment_and_borromean_triple_brick_probe.py` and witness `computations/probes/hook-even-moment-and-borromean-triple-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8343 (`feat/qou-b9cj-ogrk-ohaz-omr7-ooqh-po72`, HEAD `8c185bc247a4dfba4e6316715175039c0defb340`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8343, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
