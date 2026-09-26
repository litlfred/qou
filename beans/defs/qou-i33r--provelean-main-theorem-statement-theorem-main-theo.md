---
# qou-i33r
title: 'PROVE(lean): main_theorem_statement — theorem main_theorem_statement (ord : AdmissibleOrder G) (sys : RewritingSystem G k) (hgs  [cited manuscript]'
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

**File:** `UGB/Introduction/main_theorem_statement.lean` (UGB)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/unital-groebner-bases/lean/UGB/Introduction/main_theorem_statement.lean

### `main_theorem_statement`  —  line 85  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem main_theorem_statement (ord : AdmissibleOrder G) (sys : RewritingSystem G k) (hgs : IsGrobnerShirshovBasis G k ord sys) : ∀ f : AlgElement G k, (∃ nf : AlgElement G k, ReducesToNF ord sys f nf) ∧ (∀ nf₁ nf₂ : AlgElement G k, ReducesToNF ord sys f nf₁ → ReducesToNF ord sys f nf₂ → nf₁ = nf₂) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] unital-groebner-bases/introduction/ugb-main-theorem-statement.ts
  - [manuscript] unital-groebner-bases
- **Tractability:** Main theorem: GS basis ⇒ NF exists + unique (Diamond Lemma); central repo theorem, self-contained but large.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
