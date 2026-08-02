---
# qou-2xre
title: 'SW-1: define Iwahori-Hecke algebra H_n(q) in Lean (FreeAlgebra quotient; σ_i, quadratic (σ_i-q)(σ_i+q⁻¹)=0 + braid relations)'
status: todo
type: task
priority: normal
created_at: 2026-08-02T19:30:46Z
updated_at: 2026-08-02T19:33:06Z
parent: qou-59vq
---

Foundational, no deps. Define H_n(q) as a K-algebra: FreeAlgebra K (Fin (n-1)) quotient by the two-sided ideal of quadratic + braid + far-commutation relations, OR as MonoidAlgebra of the braid group quotient. Provide the AlgHom universal property (extend a map on generators satisfying the relations). Ref: [kassel1995]. Sorry-free target; honest sorry+Ref only if a Mathlib quotient lemma is missing.
