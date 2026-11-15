---
# qou-gl33
title: 'G3.3: highest-weight spaces HW_μ = V_μ ∩ ⋂_i ker E_i (the d=2 Wmod); ρ(H) acts on them'
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

Generalises Archimedean/SchurWeylTrace W_{r,j} = ker E ∩ V_{r−j} to gl_d. ρ(H) preserves HW_μ because it commutes with E_i (G3.1) and preserves weights (G3.2). Target: HW_μ = 0 unless μ is dominant; the H-module HW_λ ≅ S_λ for λ ⊢ n with ℓ(λ) ≤ d. Field.

Owner ruling 2026-11-15 ("G3: add infra"): build the highest-weight theory that Mathlib lacks, in PR-sized pieces.

## 2026-11-15: partly proved (QuantumGLWeights.lean)

hwSpace μ = V_μ ∩ ⋂ ker E_i is a submodule, and jimbo_mem_hwSpace shows ρ(H) preserves it, so each hwSpace μ is an
H-module. Still open (this is where G3.4 starts): hwSpace μ = 0 unless μ is dominant, and hwSpace λ ≅ S_λ.
