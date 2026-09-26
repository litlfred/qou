---
# qou-v8t7
title: 'ATTACK PLAN: prove Delta_lambda covariance kernel Cov(f,Sc2)<=0'
status: in-progress
type: feature
priority: high
created_at: 2026-07-25T03:29:34Z
updated_at: 2026-08-15T23:07:07Z
parent: qou-x631
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
