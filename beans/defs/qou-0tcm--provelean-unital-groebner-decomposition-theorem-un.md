---
# qou-0tcm
title: 'PROVE(lean): unital_groebner_decomposition — theorem unital_groebner_decomposition [Field k] [DecidableEq G] (ord : AdmissibleOrder G)  [cited manuscript]'
status: completed
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-ugb
    - verify-build
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:10Z
updated_at: 2026-10-04T15:30:51Z
parent: qou-k1mq
---

**File:** `UGB/UnitalGroebner/unital_groebner_decomposition.lean` (UGB)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/unital-groebner-bases/lean/UGB/UnitalGroebner/unital_groebner_decomposition.lean

### `unital_groebner_decomposition`  —  line 79  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem unital_groebner_decomposition [Field k] [DecidableEq G] (ord : AdmissibleOrder G) (sys : RewritingSystem G k) (hgs : IsGrobnerShirshovBasis G k ord sys) (h_deformed h_graded : HilbertFunction) : (∀ f : AlgElement G k, ∃ nf : AlgElement G k, ReducesToNF ord sys f nf) ∧ isFlat h_deformed h_gra`
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] unital-groebner-bases/unital-groebner-bases-chapter/main-theorem.ts
  - [manuscript] unital-groebner-bases
- **Tractability:** GS basis ⇒ decomposition + Hilbert-function equality; repo GS infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] decl found sorry-free & unconditional in folio/unital-groebner-bases or fred2005 tree (k1mq child; sorry gone)



## Verify by build (2026-10-04)

Closed on 'sorry-free on main' evidence, but the cited declaration could not be matched automatically to a file that a CI Lake target is known to compile (orphan census 2026-10-04: only 654 of 1,309 lean.refs resolve into the compiled library; ugb and fred2005 are separate required packages). Confirm with a build and `#print axioms`; reopen if it does not compile.
