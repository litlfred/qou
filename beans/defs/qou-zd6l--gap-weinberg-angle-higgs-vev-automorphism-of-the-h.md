---
# qou-zd6l
title: 'GAP: Weinberg angle — Higgs-vev automorphism of the Hoefsmit decomposition and the corrected trace ratio are not formalised (WeinbergAngleCategorical has no instance)'
status: in-progress
pr: 8211
type: task
priority: normal
tags:
    - lean
    - gap
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-09-03T09:08:29Z
updated_at: 2026-10-10T18:10:00Z
parent: qou-20sx
---

Class B (mathematical) gap left as a content-bearing carrier with NO instance. Found in the SM-surface Lean sweep of bean qou-08zf (2026-09-03); report: docs/audits/2026-09-03-sm-surface-lean-best-practices-sweep.md.

WHAT IS FORMALISED: folio/quantum-observable-universe/nuclear-interactions/weinberg-angle-categorical.lean — EWHoefsmitData (Markov trace functional, Hoefsmit idempotents e_W, e_B, generators σ₁, σ₅) and class WeinbergAngleCategorical R q A d cotW with fields trM_cyclic, eW_idem, eB_idem, hecke_σ₁, hecke_σ₅, trB_ne_zero and the identification cot θ_W · tr_M(e_B σ₅⁸) = tr_M(e_W σ₁⁴). Generic [Field R] (§7c). Inlined copy in mass-theory/categorical-higgs-mechanism.lean. Previously the class had four True fields closed by a global trivial instance.

WHAT IS OPEN: (1) the Higgs-vev automorphism of the Hoefsmit projector decomposition whose restriction to the (W³,B) plane is the θ_W rotation — a trace-preserving automorphism exists trivially (the identity), so an existential field would be the Round-11 vacuity; it needs the actual change-of-basis formula; (2) the corrected ratio: the .md records that the pure-pattern evaluation gives cot θ_W = q⁻⁴ (about 0.659 at q₀) against the CODATA 1.823, so the non-uniform pure-pattern multiplicities, the categorical-linking operation and the vev weighting must be derived before the class can be instantiated at the physical data. Tower status ORDER-ZERO-ONLY (single ratio at n = 6; the owner ruling of 2026-09-03 asks for the full tower).

NEXT HONEST STEP: derive the vev rotation as an explicit R-algebra automorphism of H₆(q) acting on the Hoefsmit decomposition; compute tr_M(e_W σ₁⁴) and tr_M(e_B σ₅⁸) with non-uniform multiplicities (pyhecke) in exact arithmetic; compare at the boundary only. Do not add an instance.

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.

## Progress (2026-11-16, PR #8211)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/ElectroweakWeinbergTraceLeptonFiltrationHiggsAndVevScale.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`8ca6e00d291446c4a5427c3266d272e793c16d8e`, `scriptHash: f6006da25e32`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8211`
