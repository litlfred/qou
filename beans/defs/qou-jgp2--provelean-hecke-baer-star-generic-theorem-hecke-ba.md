---
# qou-jgp2
title: 'PROVE(lean): hecke_baer_star_generic — theorem hecke_baer_star_generic [ctx : HeckeBaerStarGenericContext] : ∀ I : ctx.RightAnnih [cited kassel1995,manuscript]'
status: todo
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-kassel1995
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:02Z
updated_at: 2026-10-10T07:00:32Z
parent: qou-d8c7
---

**File:** `QOU/BraidKnot/HeckeBaerStarGeneric/hecke_baer_star_generic.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidKnot/HeckeBaerStarGeneric/hecke_baer_star_generic.lean

### `hecke_baer_star_generic`  —  line 99  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem hecke_baer_star_generic [ctx : HeckeBaerStarGenericContext] : ∀ I : ctx.RightAnnihilator, ctx.is_self_adjoint (ctx.generator_of I) ∧ ctx.is_idempotent (ctx.generator_of I) `
- **Cited:** `[manuscript]`, `[kassel1995]`
  - [manuscript] quantum-observable-universe/mass-endomorphism/hecke-baer-star-generic.md
  - [kassel1995] Kassel (1995), *Quantum Groups* — https://doi.org/10.1007/978-1-4612-0783-2
- **Tractability:** Right-annihilator generators are self-adjoint idempotents in a Hecke Baer* algebra; needs repo Hecke Baer*-algebra infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.


## 2026-10-10 — reparented to the mass-endomorphism epic

This bean is carrier M3 of epic `qou-d8c7` (issue litlfred/qou#7547). Parent moved from `qou-an4u` to `qou-d8c7`; nothing in the body above was changed by the move.
