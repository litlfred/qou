---
# qou-jgp2
title: 'hecke_baer_star_generic: discharged by an external AXIOM (hecke_baer_star_generic_sketch_axiom), not proved; module unimported'
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
updated_at: 2026-10-10T06:49:34Z
parent: qou-thkm
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



## 2026-10-10 — consolidated (owner-approved, session_01ST9RpvTF7JHNdUNafrjf9J)
Re-homed under thread qou-thkm. Previous parent: qou-an4u.


## 2026-10-10 re-scope (session_01ST9RpvTF7JHNdUNafrjf9J)
A reader reported this stale ('0 sorries'). Checked: 0 sorries because the theorem is a one-line projection of `axiom hecke_baer_star_generic_sketch_axiom` (Kassel §V.5 cited). Per the anti-laundering rule an axiom is not a proof, so this stays OPEN. Real task: prove matrix-block Baer-* (matrix_algebra_baer_right exists in the file) + the Wedderburn reduction, then delete the axiom.
