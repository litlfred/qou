---
# qou-v8t7
title: 'ATTACK PLAN: prove Delta_lambda covariance kernel Cov(f,Sc2)<=0'
status: todo
type: feature
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T03:29:34Z
updated_at: 2026-11-27T21:52:48Z
parent: b9cj
---

## Target
Prove `cov(k)=Σ_{λ⊢k}(f^λ)³(Σ_□c²−C(k,2)) ≤ 0` ⇔ `Cov_Planch(f^λ,Σc²)≤0`. Sole open input of the
Δ_λ growth chain (Lean-proved modulo this). Verified k≤40; NOT proved.

## Framework RESOLVED (2026-07-25 scaling probe): SECOND-ORDER / fluctuation scale
Tilt shift E_3[ω₃] ≈ const·σ(ω₃) (~15%), and Var_P(ln f)=O(1) (≈0.25, BOUNDED). ⇒ log-dimension has
O(1) fluctuations, β=2→3 tilt is a fixed NON-Gaussian reweighting (⇒ transfer ratio ~0.65≠1). Home =
Ivanov-Olshanski/Śniady second-order asymptotics + mixed cumulants κ_{m+1}(ln f;…;ω₃). Large-deviation
/ limit-shape is the WRONG scale (leading n² shape is β-independent for β≥2; sign is in the fluctuation
correction).

## Sufficient legs (verified k≤14, unproved): [A2] Cov(ln f,ω₃)≤0  AND  [A3] |R|=|g(1)−g'(0)|<|g'(0)|,
g(θ)=E_{2+θ}[ω₃], g(1)=kernel, g'(0)=Cov(ln f,ω₃). ~9 local certificates already eliminated.

## Resources: 7 papers in library/ (pdfminer-readable — cffi installed): Fulman 0305423, Ivanov-
Olshanski 0304010, Dołęga-Féray 1402.4615, Śniady 0411647, Biane 0006111, Dołęga-Śniady 1704.02352,
Okounkov-Olshanski 9608020. lean-lsp available (A4). arXiv-search MCP network-blocked in sandbox.

## Children: A1 exact-eval · A2 log-cov sign · A3 remainder bound · A4 Lean scaffold · A5 Śniady genus.
## Session order: A2+A3 (the two legs) first; A4 in parallel (achievable now); A1/A5 as deep bets.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-15 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-22: applicability review (owner instruction 21:27Z; session_01Qmmkt8qREoAzcE1YKVx5nz)
Verdict: RESCOPE. The target is x631 and still applies. The plan's child A5 (Sniady genus expansion) was eliminated as route #11 on 2026-07-25 (docs/audits/2026-07-25-covariance-kernel-A5-genus-eliminated-A4-lean.md; qou-t5m1 scrapped), and the recursion route was eliminated at scope (a) on 2026-11-22 (note on qou-x631). Corrected plan: legs A2 (qou-ogrk) and A3 (qou-4wl1) only, plus A1/DPP (qou-g0n2). Left todo.

## 2026-11-27: square-law inverse + large-tilt obstruction (PR #9757, session_01VQDpPgJRT1LXn57NpaDLVw)
- NEW exact form: cov(n)<=0 iff [3-cycle]Q^{-1}<=0, Q=(1/n!)sum_x x^2 (Q acts on V^lambda by 1/f^lambda; Frobenius-Schur indicator 1). Checked in the class algebra n=3..7 with zero shared code. phi(s)=[sigma]Q^{-s}: phi(1)=kernel, phi'(0)=A2.
- ELIMINATED (structural, Lean decide): "[sigma](e-Q)^m<=0 for all m", i.e. any tilt-uniform or increasing-psi(f) argument. Large-tilt sign = omega_3 at the max-dim shape: +3 at n=18, +1 at n=26; Cov(omega_3,f^s)>0 for s>362.94 at n=18. Lean: HeckeTemperleyLieb/YoungDiagramKernelLargeTilt.lean, not_forall_tiltedSum_nonpos.
- A proof must use s=1 or a bounded s-window. Audit: docs/audits/2026-11-27-covariance-kernel-square-law-inverse.md.
