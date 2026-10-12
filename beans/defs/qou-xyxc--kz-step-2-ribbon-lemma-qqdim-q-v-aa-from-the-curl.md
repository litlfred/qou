---
# qou-xyxc
title: 'KZ Step 2: ribbon lemma (q−q⁻¹)·dim_q V = a−a⁻¹ from the curl identities, instantiated to dim_q V = [2]_q'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:13:09Z
updated_at: 2026-10-12T18:26:37Z
parent: qou-xhci
---

Plan from coordination doc. Lean ribbon layer exists: QOU/MathlibExt/Ribbon.lean, PivotalCategory.lean, SphericalCategory.lean.


## 2026-10-12 — DONE on branch claude/kz-ribbon-qdim-2026-10-12 (no prior 2026-10-11 ribbon branch existed)
File QOU/MathlibExt/RibbonHeckeDimension.lean, sorry-free, axioms [propext, Classical.choice, Quot.sound]:
- ribbon_hecke_dimension: k-linear ribbon C, β_{V,V} − β_{V,V}⁻¹ = (q−q⁻¹)•𝟙, θ_V = a•𝟙, a≠0, qDimTwistedWith V Vᘁ = d•𝟙 ⟹ ((q−q⁻¹)d)•𝟙_V = (a−a⁻¹)•𝟙_V.
- ribbon_hecke_qDim_eq_qint_two: a = q², q−q⁻¹≠0, 𝟙_V≠0 ⟹ d = q + q⁻¹.
- curls from the axioms: ptrWith_braiding (twistless ptr of β is 𝟙, any braided rigid C), ptrTwistWith_braiding (= θ, balanced), ptrTwistWith_braiding_inv (= θ⁻¹; uses ribbon axiom once via twist_closure_eq).
Convention: ribbon trace = closure (θ ▷ Vᘁ) ≫ β ≫ ε, matching qDimTwistedWith.
Open: no nondegenerate (q²≠1) instance exists in the tree (only symmetric θ=1, where q=q⁻¹); instantiation at D_ℏ is qou-zoyv.
