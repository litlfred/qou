---
# qou-xyxc
title: 'KZ Step 2: ribbon lemma (q−q⁻¹)·dim_q V = a−a⁻¹ from the curl identities, instantiated to dim_q V = [2]_q'
status: completed
type: task
priority: normal
created_at: 2026-10-12T18:13:09Z
updated_at: 2026-10-13T11:42:53Z
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


2026-10-13 coordinator: S1–S6 done on PR #7743 (head 3acf450840), re-verified: lean -DautoImplicit=false -s 65536 exit 0 (RibbonDH.lean 20 s); #print axioms qDim_V_eq_qint_two / hecke_DH / not_hecke_unscaled = [propext, Classical.choice, Quot.sound]. D_ℏ (DH c) is a ℂ-linear RibbonCategory for ℏ transcendental, ‖ℏ‖ ≤ 1/12 (admissible ℏ exist: exists_admissible). dim_q V = q + q⁻¹, q = e^{iπℏ} (qDim_V_eq_qint_two), via ribbon_hecke_dimension_scaled: the unscaled Hecke relation is FALSE in sl₂ normalisation (not_hecke_unscaled); the rescaled braiding e^{iπℏ/2}β satisfies it. Hand-checked: eigenvalues e^{iπℏ/2} (Sym²), −e^{−3iπℏ/2} (Λ²), C_V = 3/2. Scope: the real pin ℏ₀ (|ℏ₀| ≈ 0.033) lies in the disc but is not known transcendental, so it is not covered. Subject proved ⇒ completed.
