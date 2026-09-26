---
# qou-4mrb
title: 'PROVE(lean): four_term_pair_nucleon — theorem four_term_pair_nucleon [ctx : FourTermPairNucleonContext] : (∀ φ₀ φ₁ φ₀₁ : ℝ, ctx. [cited jones1987,manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-jones1987
created_at: 2026-08-01T23:31:07Z
updated_at: 2026-08-01T23:31:07Z
parent: qou-k1mq
---

**File:** `QOU/ParticleInteractions/four_term_pair_nucleon.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean

### `four_term_pair_nucleon`  —  line 122  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem four_term_pair_nucleon [ctx : FourTermPairNucleonContext] : (∀ φ₀ φ₁ φ₀₁ : ℝ, ctx.confinedNet φ₀ φ₁ φ₀₁ ctx.protonFlavours = protonNetTarget) ∧ (∀ φ₀ φ₁ φ₀₁ : ℝ, ctx.confinedNet φ₀ φ₁ φ₀₁ ctx.neutronFlavours = neutronNetTarget) `
- **Cited:** `[jones1987]`, `[manuscript]`
  - [jones1987] Jones (1987), *Hecke algebra representations of braid groups and link polynomials* — https://doi.org/10.2307/1971403
  - [manuscript] quantum-observable-universe/particle-interactions/four-term-pair-nucleon.md
- **Tractability:** Specific confinement net values ≈0.999/0.811 (proton/neutron); compute-backed numeric from the Hecke/GS engine, not a pure Lean theorem.
- **Next step:** Compute-backed numeric — the value lives in the Hecke/GS engine (witness JSON). Needs that compute formalized in Lean before the goal is provable; not a Mathlib gap.
