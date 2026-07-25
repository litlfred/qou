---
# qou-4hq0
title: 'A1 (deep bet): exact/semi-exact evaluation of T3=Sum(f)^2 chi(3-cyc) via content-sum formulas'
status: completed
type: task
priority: normal
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T12:03:36Z
parent: qou-v8t7
---

A1 — exact T3 evaluation: ELIMINATED (route #12, 2026-07-25 agent). No closed form for T3=Σ(dim)²χ(σ₃) / cov=Σ(dim)³ω₃ (OEIS-absent, not P-recursive, no product/hypergeometric hit; no manifestly-negative form). PRECISE REASON = the dim²→dim³ threshold: Σ(dim)²·ω₃=0 EXACTLY (closed, Plancherel expectation of shifted-symmetric ω₃, IO Prop 5.1) but Σ(dim)³·ω₃=cov carries one extra dim (=χ(e), NOT shifted-symmetric) ⇒ non-holonomic; even envelope Σdim³=10,64,596,… has no closed form. UNIFIES with A5 (genus): both fail because the extra dim ∉ shifted-symmetric algebra A. Missing tool = non-shifted-symmetric dimension-functional expansion (dim/ln-dim vs Plancherel: Vershik-Kerov ln-dim, Schur-measure, hook-content) — NOT character machinery. This also sharpens A2 (leading term Cov(ln f,ω₃) needs ln-dim expansion). Audit: 2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md
