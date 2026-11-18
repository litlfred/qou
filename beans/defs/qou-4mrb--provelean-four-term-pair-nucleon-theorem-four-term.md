---
# qou-4mrb
title: 'PROVE(lean): four_term_pair_nucleon — theorem four_term_pair_nucleon [ctx : FourTermPairNucleonContext] : (∀ φ₀ φ₁ φ₀₁ : ℝ, ctx. [cited jones1987,manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-jones1987
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:07Z
updated_at: 2026-11-18T07:45:11Z
parent: qou-l2vh
---

**File:** `QOU/ParticleInteractions/four_term_pair_nucleon.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean

### `four_term_pair_nucleon`  —  line 122  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem four_term_pair_nucleon [ctx : FourTermPairNucleonContext] : (∀ φ₀ φ₁ φ₀₁ : ℝ, ctx.confinedNet φ₀ φ₁ φ₀₁ ctx.protonFlavours = protonNetTarget) ∧ (∀ φ₀ φ₁ φ₀₁ : ℝ, ctx.confinedNet φ₀ φ₁ φ₀₁ ctx.neutronFlavours = neutronNetTarget) `
- **Cited:** `[jones1987]`, `[manuscript]`
  - [jones1987] Jones (1987), *Hecke algebra representations of braid groups and link polynomials* — https://doi.org/10.2307/1971403
  - [manuscript] quantum-observable-universe/particle-interactions/four-term-pair-nucleon.md
- **Tractability:** Specific confinement net values ≈0.999/0.811 (proton/neutron); compute-backed numeric from the Hecke/GS engine, not a pure Lean theorem.
- **Next step:** Compute-backed numeric — the value lives in the Hecke/GS engine (witness JSON). Needs that compute formalized in Lean before the goal is provable; not a Mathlib gap.

## Round 82 Progress (PR #8389)
- Branch: `feat/round82-confdiff-gevreypos-hyproot-tracesq-normchain-43c1`
- Commit 1 (code + probe): `9fc5597f0f6558c185cf46ffd6acdc86ad1d4b21`
- Commit 2 (witness): `4a084d4105014f8457a64297f35613ebb0f95d6b` (`scriptSha256 = 0b271ed473fcb7e2f06260119e75930af659f57c2419e9542b05b4df69271355`)
