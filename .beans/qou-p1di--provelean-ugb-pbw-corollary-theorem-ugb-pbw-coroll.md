---
# qou-p1di
title: 'PROVE(lean): ugb_pbw_corollary — theorem ugb_pbw_corollary (qs : QSerreRelations k) : (∀ m : PBWMonomial, isNormalForm degL [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-ugb
    - repo-infra
created_at: 2026-08-01T23:31:09Z
updated_at: 2026-08-01T23:31:09Z
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
