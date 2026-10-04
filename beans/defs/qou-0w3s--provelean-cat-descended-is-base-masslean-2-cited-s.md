---
# qou-0w3s
title: 'PROVE(lean): cat_descended_is_base_mass.lean — 2 cited sorries [cited manuscript]'
status: todo
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:08Z
updated_at: 2026-10-04T15:22:23Z
parent: qou-aabg
---

**File:** `QOU/TopologicalMass/cat_descended_is_base_mass.lean` (QOU)  ·  2 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/TopologicalMass/cat_descended_is_base_mass.lean

### `descended_trace_is_base_trace`  —  line 79  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem descended_trace_is_base_trace : trFrob (tauHat alpha) = baseTrace `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-descended.md
- **Tractability:** trFrob(τ̂ α) = baseTrace descent identity; repo categorical-trace infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `base_mass_is_norm_of_base_trace`  —  line 89  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem base_mass_is_norm_of_base_trace : mnorm baseTrace = baseMass `
- **Cited:** `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-descended.md
- **Tractability:** mnorm(baseTrace) = baseMass; repo mass-norm identity.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
