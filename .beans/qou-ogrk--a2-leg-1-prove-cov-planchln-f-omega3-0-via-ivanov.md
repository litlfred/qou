---
# qou-ogrk
title: 'A2 (leg 1): prove Cov_Planch(ln f, omega3) <= 0 via Ivanov-Olshanski 2nd-order covariance'
status: todo
type: task
priority: high
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T11:14:07Z
parent: qou-v8t7
---

## A2 — leg 1: Cov_Planch(ln f, ω₃) ≤ 0. Literature intel in hand (paper-mining agent, 2026-07-25).
EXACT ENGINE (IO Prop 5.1 + Śniady product rule): ⟨p#_ρ⟩_Planch = n↓^r·δ_{ρ=(1^r)}; any Cov(p#_j,p#_k)
(j,k≥2) is a finite signed connection-coefficient sum, EXACT. VALIDATED: Cov_Planch(Σc,ω₃)=0 exactly
(transposition ⊥ 3-cycle char). Notation: ω₃=p#₃=Σ₃=R₄+R₂ (3-cycle char), p#₂=2Σc (transposition).
CAVEAT (agent): ln f ∉ A (algebra of polynomial functions) — NO finite Σ_μ-expansion of log-dim;
do not chase one. But ln f=½ ln M_n+½ ln n!, M_n=dim²/n! ⇒ Cov(ln f,ω₃)=½E[ω₃ ln M_n] (ω₃-weighted
log-likelihood; validated exact, but an algebraic reframing not new leverage).
STATUS: numerics say Cov(ln f,ω₃)<0 all n. The exact p#-engine handles character×character covariances
but NOT ln f (∉A) — so A2 needs either the M_n-entropy correlation sign or the genus route. Open.
