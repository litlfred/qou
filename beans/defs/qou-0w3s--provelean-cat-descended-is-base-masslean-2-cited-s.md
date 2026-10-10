---
# qou-0w3s
title: 'Frobenius descent: prove tr(τ̂α)=tr₀(α₀) + base norm (cat_descended_is_base_mass has 0 sorries; gap is the CatDescendedInputs ''Open input'' class)'
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
updated_at: 2026-10-10T06:49:33Z
parent: qou-thkm
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



## 2026-10-10 — consolidated (owner-approved, session_01ST9RpvTF7JHNdUNafrjf9J)
Re-homed under thread qou-thkm. Previous parent: qou-aabg.


## 2026-10-10 re-scope (session_01ST9RpvTF7JHNdUNafrjf9J)
Verified at HEAD: no sorries remain; bodies are ctx.trace_compat / ctx.base_norm projections of CatDescendedInputs. Old title ('2 cited sorries') was stale. Kept OPEN (rule 13a: the descent theorem itself is unproved). Blocked by qou-e524.
