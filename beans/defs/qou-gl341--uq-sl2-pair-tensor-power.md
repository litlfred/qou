---
# qou-gl341
title: 'G3.4a: each Chevalley pair as a U_q(sl2) Rep on (K^d)^{⊗n}; its E is raiseOp, its K is the Cartan'
status: completed
type: task
priority: normal
tags:
    - quark-state
    - schur-weyl
created_at: 2026-11-15T10:20:00Z
updated_at: 2026-11-15T10:55:00Z
parent: qou-gl34
---

Fundamental of gl_d restricted to the pair (i,i+1) as QuantumSl2Fundamental.Rep (E = E_{i+1,i}, F = E_{i,i+1}, K = κ_i); n-fold Rep.tensor reindexed to Fin n → Fin d; identify E with raiseOp and K with cartan κ_i. The standard F is Δ(F) = F⊗1 + κ⁻¹⊗F (head weight). The merged lowerOp (tail κ) commutes with Ř but does NOT satisfy [E,F] = (K−K⁻¹)/(q−q⁻¹) (sympy, d ∈ {2,3}, n ≤ 3); the head-weight F satisfies it and also commutes with Ř.

Owner ruling via coordinator 2026-11-15: "work G3.4, dispatch siblings". Direct highest-weight route (session 7a).

## Done 2026-11-15
`QuantumGLSl2Pair.lean`: `fundPair`, `powRep`, `powRep_E` (= `raiseOp`), `powRep_Kp` (= `cartan κ`).
Sorry-free, axioms `[propext, Classical.choice, Quot.sound]`. Note: the merged `lowerOp` is not the
standard `Δ(F)`; `powRep`'s `F` is the standard one.
Merged as #7870 on 2026-11-15.
