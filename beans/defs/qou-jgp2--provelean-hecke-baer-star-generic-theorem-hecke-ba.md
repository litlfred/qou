---
# qou-jgp2
title: 'De-axiomatise hecke_baer_star_generic: claim rests on two axioms in the sibling .lean'
status: completed
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
updated_at: 2026-11-20T09:30:00Z
parent: qou-d8c7
---

**File:** `QOU/BraidKnot/HeckeBaerStarGeneric/hecke_baer_star_generic.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/BraidKnot/HeckeBaerStarGeneric/hecke_baer_star_generic.lean

### `hecke_baer_star_generic`  —  line 99  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem hecke_baer_star_generic [ctx : HeckeBaerStarGenericContext] : ∀ I : ctx.RightAnnihilator, ctx.is_self_adjoint (ctx.generator_of I) ∧ ctx.is_idempotent (ctx.generator_of I) `
- **Cited:** `[manuscript]`, `[kassel1995]`
  - [manuscript] quantum-observable-universe/mass-endomorphism/hecke-baer-star-generic.md
  - [kassel1995] Kassel (1995), *Quantum Groups* — https://doi.org/10.1007/978-1-4612-0783-2
- **Tractability:** Right-annihilator generators are self-adjoint idempotents in a Hecke Baer* algebra; needs repo Hecke Baer*-algebra infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.


## 2026-10-10 — reparented to the mass-endomorphism epic

This bean is carrier M3 of epic `qou-d8c7` (issue litlfred/qou#7547). Parent moved from `qou-an4u` to `qou-d8c7`; nothing in the body above was changed by the move.


## 2026-10-10 — status update (title changed; survey for epic `qou-d8c7`, issue #7547)

Former title began 'PROVE(lean): hecke_baer_star_generic — theorem hecke_baer_star_generic ...'.

Checked on `main` 2026-10-10: the library file `QOU/BraidKnot/HeckeBaerStarGeneric/hecke_baer_star_generic.lean` is 33 lines with no theorem. The chapter sibling `mass-endomorphism/hecke-baer-star-generic.lean` carries the claim and rests on two axioms: `matrix_algebra_baer_right_axiom` (line 60) and `hecke_baer_star_generic_sketch_axiom` (line 144). The open work is replacing those axioms with proofs (Wedderburn decomposition into matrix algebras, then the Baer-* property of each matrix block). Axioms are not a proof (anti-laundering rule), so this stays open.

## 2026-11-20 — W1 survey (session_01VQDpPcT9hCf4RF1bQwk66r, epic PR #8534)

The subject of this bean, the two axioms, is gone from main. `matrix_algebra_baer_right_axiom` was proved and `hecke_baer_star_generic_sketch_axiom` was refuted (M_2(F_2) with transpose), both on 2026-11-15 under `qou-n2un`. Re-verified 2026-11-20: lean-direct exit 0, `#print axioms` `[propext, Classical.choice, Quot.sound]`. New on PR #8534 (commit 98fa99ede6): `baerStarRing_matrix_rclike`, M_n(k) with conjugate transpose is Baer-* for every RCLike k, sorry-free. The proposition itself stays OPEN: it needs a *-isomorphism H_n(q) ≅ ⊕ M_{d_λ}(k) carrying the bar involution to the conjugate transpose. That open statement lives in `qou-n2un`, which stays open.
