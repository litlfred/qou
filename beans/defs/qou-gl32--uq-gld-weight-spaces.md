---
# qou-gl32
title: 'G3.2: weight-space decomposition of (R^d)^{⊗n} under the Cartan; Hecke action preserves weights'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - schur-weyl
created_at: 2026-11-15T10:10:00Z
updated_at: 2026-11-15T10:10:00Z
parent: qou-gld3
---

V_μ = span{e_a : content(a) = μ}, μ ∈ ℕ^d with |μ| = n. Cartan acts on V_μ by q^{μ_j}. Ř preserves content, so ρ(H) preserves each V_μ. E_i maps V_μ to V_{μ+α_i}. Generic CommRing; separating the weights needs q not a root of unity (field).

Owner ruling 2026-11-15 ("G3: add infra"): build the highest-weight theory that Mathlib lacks, in PR-sized pieces.

## 2026-11-15: proved (QuantumGLWeights.lean)

- content and weightProj; Ř preserves content.
- jimbo_commute_weightProj: ρ(H) preserves every V_μ.
- cartan_mul_weightProj: the Cartan acts on V_μ by ∏ c(x)^{μ(x)}.
- weightProj_mul_raiseOp_mul_weightProj: E_i maps V_μ into V_{μ+α_i}.
