---
# qou-p1di
title: 'PROVE(lean): ugb_pbw_corollary — theorem ugb_pbw_corollary (qs : QSerreRelations k) : (∀ m : PBWMonomial, isNormalForm degL [cited manuscript]'
status: completed
type: task
priority: normal
tags:
    - verify-build
    - lean
    - cited-sorry
    - paper-ugb
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:09Z
updated_at: 2026-10-04T15:30:50Z
parent: qou-k1mq
---

**File:** `UGB/BuchbergerPBW/ugb_pbw_corollary.lean` (UGB)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/unital-groebner-bases/lean/UGB/BuchbergerPBW/ugb_pbw_corollary.lean

### `ugb_pbw_corollary`  —  line 87  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem ugb_pbw_corollary (qs : QSerreRelations k) : (∀ m : PBWMonomial, isNormalForm degLexOrder (qSerreRewritingSystem k qs) ⟨fun w => if w = m.toMonomial then (1 : k) else 0, {m.toMonomial}, fun w hw => by simp at hw; simp [hw]⟩) ∧ (∀ f : AlgElement SU2Gen k, (∃ nf : AlgElement SU2Gen k, ReducesT`
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] unital-groebner-bases/buchberger-and-pbw/pbw-corollary.ts
  - [manuscript] unital-groebner-bases
- **Tractability:** PBW corollary: GS basis ⇒ NF exists+unique for Serre relations; repo GS infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] decl found sorry-free & unconditional in folio/unital-groebner-bases or fred2005 tree (k1mq child; sorry gone)



## Verify by build (2026-10-04)

Closed on 'sorry-free on main' evidence, but the cited declaration could not be matched automatically to a file that a CI Lake target is known to compile (orphan census 2026-10-04: only 654 of 1,309 lean.refs resolve into the compiled library; ugb and fred2005 are separate required packages). Confirm with a build and `#print axioms`; reopen if it does not compile.
