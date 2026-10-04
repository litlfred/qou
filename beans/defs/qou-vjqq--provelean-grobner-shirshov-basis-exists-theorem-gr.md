---
# qou-vjqq
title: 'PROVE(lean): grobner_shirshov_basis_exists — theorem grobner_shirshov_basis_exists (G : NoncommutativeFormalGroup) : ∃ (gsb : GrobnerSh [cited fred2005]'
status: completed
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-fred2005
    - repo-infra
    - cite-fred2005
    - reorg-2026-10-04
    - verify-build
created_at: 2026-08-01T23:31:00Z
updated_at: 2026-10-04T15:30:49Z
parent: qou-k1mq
---

**File:** `Fred2005/FormalGroups.lean` (Fred2005)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/fred2005-formal-groups/lean/Fred2005/FormalGroups.lean

### `grobner_shirshov_basis_exists`  —  line 222  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem grobner_shirshov_basis_exists (G : NoncommutativeFormalGroup) : ∃ (gsb : GrobnerShirshovBasis), gsb.formalGroup = G ∧ (∃ a b, a ≠ b ∧ gsb.reduce a = gsb.reduce b) `
- **Cited:** `[fred2005]`
  - [fred2005] Fred (2005), *Integration of Skewed-Poisson Structures on Non-commutative Formal Groups* — https://repository.arizona.edu/handle/10150/193802
- **Tractability:** Existence of a GS basis + a non-confluence witness for a noncommutative formal group; needs the repo GS/Diamond-Lemma engine, no Mathlib gap.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] decl found sorry-free & unconditional in folio/unital-groebner-bases or fred2005 tree (k1mq child; sorry gone)



## Verify by build (2026-10-04)

Closed on 'sorry-free on main' evidence, but the cited declaration could not be matched automatically to a file that a CI Lake target is known to compile (orphan census 2026-10-04: only 654 of 1,309 lean.refs resolve into the compiled library; ugb and fred2005 are separate required packages). Confirm with a build and `#print axioms`; reopen if it does not compile.
