---
# qou-i33r
title: 'PROVE(lean): main_theorem_statement — theorem main_theorem_statement (ord : AdmissibleOrder G) (sys : RewritingSystem G k) (hgs  [cited manuscript]'
status: completed
type: task
priority: normal
tags:
    - cited-sorry
    - verify-build
    - paper-ugb
    - repo-infra
    - reorg-2026-10-04
    - lean
created_at: 2026-08-01T23:31:10Z
updated_at: 2026-10-04T15:30:49Z
parent: qou-k1mq
---

**File:** `UGB/Introduction/main_theorem_statement.lean` (UGB)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/unital-groebner-bases/lean/UGB/Introduction/main_theorem_statement.lean

### `main_theorem_statement`  —  line 85  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem main_theorem_statement (ord : AdmissibleOrder G) (sys : RewritingSystem G k) (hgs : IsGrobnerShirshovBasis G k ord sys) : ∀ f : AlgElement G k, (∃ nf : AlgElement G k, ReducesToNF ord sys f nf) ∧ (∀ nf₁ nf₂ : AlgElement G k, ReducesToNF ord sys f nf₁ → ReducesToNF ord sys f nf₂ → nf₁ = nf₂) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] unital-groebner-bases/introduction/ugb-main-theorem-statement.ts
  - [manuscript] unital-groebner-bases
- **Tractability:** Main theorem: GS basis ⇒ NF exists + unique (Diamond Lemma); central repo theorem, self-contained but large.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] decl found sorry-free & unconditional in folio/unital-groebner-bases or fred2005 tree (k1mq child; sorry gone)



## Verify by build (2026-10-04)

Closed on 'sorry-free on main' evidence, but the cited declaration could not be matched automatically to a file that a CI Lake target is known to compile (orphan census 2026-10-04: only 654 of 1,309 lean.refs resolve into the compiled library; ugb and fred2005 are separate required packages). Confirm with a build and `#print axioms`; reopen if it does not compile.
