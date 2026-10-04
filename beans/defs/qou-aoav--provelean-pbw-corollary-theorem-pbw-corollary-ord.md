---
# qou-aoav
title: 'PROVE(lean): pbw_corollary — theorem pbw_corollary (ord : AdmissibleOrder G) (sys : RewritingSystem G k) (hgs : IsGrobn [cited manuscript]'
status: completed
type: task
priority: normal
tags:
    - paper-ugb
    - repo-infra
    - reorg-2026-10-04
    - lean
    - cited-sorry
created_at: 2026-08-01T23:31:10Z
updated_at: 2026-10-04T15:22:42Z
parent: qou-k1mq
---

**File:** `UGB/UnitalGroebner/pbw_corollary.lean` (UGB)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/unital-groebner-bases/lean/UGB/UnitalGroebner/pbw_corollary.lean

### `pbw_corollary`  —  line 74  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem pbw_corollary (ord : AdmissibleOrder G) (sys : RewritingSystem G k) (hgs : IsGrobnerShirshovBasis G k ord sys) : ∀ f : AlgElement G k, (∃ nf : AlgElement G k, ReducesToNF ord sys f nf) ∧ (∀ nf₁ nf₂ : AlgElement G k, ReducesToNF ord sys f nf₁ → ReducesToNF ord sys f nf₂ → nf₁ = nf₂) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] unital-groebner-bases/unital-groebner-bases-chapter/pbw-corollary.ts
  - [manuscript] unital-groebner-bases
- **Tractability:** PBW corollary (unital): GS basis ⇒ NF exists+unique; repo GS infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] decl found sorry-free & unconditional in folio/unital-groebner-bases or fred2005 tree (k1mq child; sorry gone)
