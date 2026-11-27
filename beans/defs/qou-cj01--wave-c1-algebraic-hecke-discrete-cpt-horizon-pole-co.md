---
# qou-cj01
title: 'Wave C1: Algebraic, Hecke, Discrete CPT, & Horizon-Pole Conjecture Discharges (18 blocks)'
status: open
type: task
priority: high
created_at: 2026-11-19T19:55:00Z
updated_at: 2026-11-19T19:55:00Z
parent: qou-cj90
---

Attack and discharge/prove the 18 algebraic, Hecke, crystal, CPT, and horizon-pole conjectures: `conj:lqg-entropy-qdim-partition-pole`, `conj:explicit-central-idempotent`, `conj:brunnian-property-of-borromean`, `conj:quantum-langlands-dual`, `conj:p-from-braid-mirror`, `conj:t-from-trace-cyclicity`, `conj:c-from-color-flavor-swap`, `conj:cpt-d6-d7-d8-closure`, `conj:type-b-folding-cpt`, `conj:symmetric-crystal-pair-production`, `conj:reverse-limit-q-to-infinity`, `conj:lusztig-canonical-basis-q-eq-1`, `conj:kazhdan-lusztig-classical-limit`, `conj:graded-baer-star-Hq`, `conj:block-multiplicativity-v-free`, `conj:reidemeister-mass-invariance`, `conj:categorical-linking-operation`, `conj:cyclotomic-boundary-at-keystone`.

## 2026-11-27 — `conj:quantum-langlands-dual`: type-A algebra content proved for every n (PR #9760)

New library file `HeckeTemperleyLieb/HeckeLanglandsDual.lean` on `QOU.Hecke.IwahoriHecke K q n`, any commutative ring with `q` a unit: `rescaleEquiv` (H_n(q⁻¹) ≃ₐ H_n(q), T_i ↦ −q⁻¹T_i), `inverseEquiv` (T_i ↦ T_i⁻¹), the involution `theta` (T_i ↦ (q−1) − T_i) = rescale ∘ inverse⁻¹, `theta_ne_refl` (≠ id when q ≠ −1, via index/sign characters), `not_algHom_of_inverts_param` (distinct from bar). lean-direct exit 0, no warnings, axioms [propext, Quot.sound]. Previously only H_3. The conjecture itself stays open: item 2 (reverse limit q → ∞) and item 3 (non-simply-laced folding) are untouched.
