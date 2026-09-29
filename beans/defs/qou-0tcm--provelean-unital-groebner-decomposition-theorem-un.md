---
# qou-0tcm
title: 'PROVE(lean): unital_groebner_decomposition — theorem unital_groebner_decomposition [Field k] [DecidableEq G] (ord : AdmissibleOrder G)  [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-ugb
    - repo-infra
created_at: 2026-08-01T23:31:10Z
updated_at: 2026-08-01T23:31:10Z
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
