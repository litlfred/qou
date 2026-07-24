---
# qou-jy04
title: 'Phase 3 route 1: Stein + Kerov-CLT reduction Cov(f,Σ3)~E[f]Cov(ln f,Σ3)'
status: in-progress
type: task
priority: high
created_at: 2026-07-24T16:21:37Z
updated_at: 2026-07-24T20:54:43Z
parent: qou-x631
---

Route 1 (Stein/Kerov-CLT). Phase 5 CONSTRUCTION DONE (2026-07-24): built the Fulman-analogue Plancherel-reversible down-up chain on partitions of n; verified reversible. ω_j=Σc^j−E_P[Σc^j] is a chain eigenfunction for j=1 (Σc, transposition, τ₁=2/n, Fulman) and j=2 (Σc²=ω₃, 3-cycle, τ₃=3/n — OUR object; direct k=2 analogue). Exact identity E_P[Δf·ω₃]=−(3/n)·cov(n)/n! (Δf=f(λ*)−f(λ)), verified n≤9 ⇒ LOCAL reformulation: cov(n)≤0 ⇔ E_P[(f(λ*)−f(λ))·ω₃(λ)]≥0 (one-step dimension increment ⊥ content-spread). Does NOT close the sign yet. Next: (1) explicit combinatorial eval of E_P[Δf·ω₃] via hook-ratio increment; or (2) joint Stein CLT of (f,ω₃) with effective Berry-Esseen error < the negative main term for n>n₀, then exact n≤40 closes. Audit: 2026-07-24-covariance-kernel-route1-exchangeable-pair.md
