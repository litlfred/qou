---
# qou-0w3s
title: 'Descent inputs of CatDescendedInputs (cat_descended_is_base_mass.lean): no sorries remain, two open inputs'
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
updated_at: 2026-10-10T07:01:01Z
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


## 2026-10-10 — status update (title changed; survey for epic `qou-d8c7`, issue #7547)

Former title: 'PROVE(lean): cat_descended_is_base_mass.lean — 2 cited sorries [cited manuscript]'.

The body above describes a file that no longer exists in that form. Checked on `main` 2026-10-10: `QOU/TopologicalMass/cat_descended_is_base_mass.lean` has **no `sorry`**. The two identities are now fields of `class CatDescendedInputs : Prop` (documented as "Open input 1" and "Open input 2"), and the two theorems project them (`ctx.trace_compat` and its sibling). So the open item is the two class inputs, not two sorries. `qou-50p7` recorded the structural wall: as stated the inputs relate independent opaque constants, so nothing in the repo forces them.

Tracked under carrier M2 (`tmvac`) of epic `qou-d8c7`. Stays open: the inputs are conjectural (rule 13a).



## 2026-10-10 — consolidated (owner-approved, session_01ST9RpvTF7JHNdUNafrjf9J)
Re-homed under thread qou-thkm. Previous parent: qou-aabg.


## 2026-10-10 re-scope (session_01ST9RpvTF7JHNdUNafrjf9J)
Verified at HEAD: no sorries remain; bodies are ctx.trace_compat / ctx.base_norm projections of CatDescendedInputs. Old title ('2 cited sorries') was stale. Kept OPEN (rule 13a: the descent theorem itself is unproved). Blocked by qou-e524.
