---
# qou-ogrk
title: 'A2 (leg 1): prove Cov_Planch(ln f, omega3) <= 0 via Ivanov-Olshanski 2nd-order covariance'
status: in-progress
type: task
priority: high
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T12:19:14Z
parent: qou-v8t7
---

A2 — leg 1: Cov_Planch(ln f, ω₃) ≤ 0. ADVANCE (2026-07-25 hook/Frullani reduction). Exact reduction to a clean one-parameter sign: (1) hook-length formula ln f=ln n!−Σ ln h ⇒ Cov(ln f,ω₃)=−Σ_v ln(v)ν_v, ν_v=Cov(N_v,ω₃); moments Σν_v=0, Σv²ν_v=Cov(Σh²,ω₃)=Var(ω₃)=n(n-1)(n-2)/3 via the CLASSICAL IDENTITY Σ_□h²=Σ_□c²+n² (verified all λ). (2) Frullani ⇒ EXACT integral rep Cov(ln f,ω₃)=∫_0^∞(1/s)Cov(H_s,ω₃)ds, H_s=Σ_□ e^{−s h} (verified n≤10). REDUCTION: A2 ⇐ Cov_Planch(H_s,ω₃)≤0 ∀s>0, VERIFIED strictly<0 on interior (fine grid n≤13). OPEN sub-problem: prove Cov(H_s,ω₃)≤0 ∀s>0 (H_s a hook functional ∉ algebra A; the dim²→dim³ obstruction trades log for exp). Materially cleaner target: a single positive analytic statistic with 2 exact moment constraints (Σν_v=0, Σv²ν_v=|C₃|). Audit: 2026-07-25-covariance-kernel-A2-hook-reduction.md
