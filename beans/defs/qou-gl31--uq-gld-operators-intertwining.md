---
# qou-gl31
title: 'G3.1: U_q(gl_d) Cartan and E_i/F_i on (R^d)^{⊗n}; [Ř_t, Δ(X)] = 0 (image ⊆ commutant)'
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

Matrix model of TensorEmbeddingGL. Cartan K_j = diag q^{#j}; E_i: e_i→e_{i+1} and F_i: e_{i+1}→e_i, each as Σ_s (site op at s) ⊗ κ_i^{⊗(sites>s)}, κ_i(x) = q^{[x=i+1]−[x=i]}. Convention checked in sympy at d=3, n=3: this tail commutes with Ř for both E and F, and the q^{[x=i]−[x=i+1]} tail does not. Generic lemma: a site operator commutes with Ř_t if the two-site Δ² commutes with Ř and Ř commutes with κ⊗κ. Generic CommRing, q*qi = 1.

Owner ruling 2026-11-15 ("G3: add infra"): build the highest-weight theory that Mathlib lacks, in PR-sized pieces.

## 2026-11-15: proved (draft PR)

QuantumGLAction.lean and QuantumGLIntertwine.lean. ρ(H_{m+1}(q)) commutes with E_i, F_i (raiseOp, lowerOp) and with every
Cartan product weight, for every d. This is the inclusion image ⊆ commutant. It is sorry-free and uses the standard axioms only.
