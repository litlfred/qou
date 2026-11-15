---
# qou-o3so
title: 'PROVE(lean): pair_skein_mass_formula — theorem pair_skein_mass_formula : ∀ a b : ℕ, S_ab a b = (q * μ a + q⁻¹ * μ b) / (Real.sqrt [cited jones1987,manuscript]'
status: todo
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-jones1987
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-10-04T15:22:41Z
parent: qou-aabg
---

**File:** `QOU/HadronicMass/pair_skein_mass_formula.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/HadronicMass/pair_skein_mass_formula.lean

### `pair_skein_mass_formula`  —  line 64  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem pair_skein_mass_formula : ∀ a b : ℕ, S_ab a b = (q * μ a + q⁻¹ * μ b) / (Real.sqrt q + 1 / Real.sqrt q) `
- **Cited:** `[jones1987]`, `[manuscript]`, `[jones1987]`
  - [jones1987] Jones (1987), *Hecke algebra representations of braid groups and link polynomials* — https://doi.org/10.2307/1971403
  - [manuscript] quantum-observable-universe/observations/pair-skein-mass-formula.md
- **Tractability:** S_ab = (q·μ_a+q⁻¹·μ_b)/(√q+1/√q) skein mass formula; repo compute identity (Real.sqrt present).
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
