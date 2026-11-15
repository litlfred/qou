---
# qou-gl342
title: 'G3.4b: HW_μ = 0 unless μ is dominant'
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

sl2 argument: v ∈ HW_μ with K v = q^h v, h = μ(i+1) − μ(i); E F^k v = [k][h−k+1] F^{k−1} v; F nilpotent because K has finitely many eigenvalues and q is generic; so h ≥ 0. Here E raises i → i+1, so 'dominant' means μ(i) ≤ μ(i+1) in index order (the reverse of the usual μ_1 ≥ … ≥ μ_d labelling).

Owner ruling via coordinator 2026-11-15: "work G3.4, dispatch siblings". Direct highest-weight route (session 7a).

## Done 2026-11-15
`QuantumGLDominance.lean`: `le_of_mem_hwSpace` (nonzero v ∈ HW_μ ⇒ μ i ≤ μ (i+1)) and
`hwSpace_eq_bot_of_not_dominant`. Field, q not a root of unity. Sorry-free, standard axioms.
Merged as #7870 on 2026-11-15.
