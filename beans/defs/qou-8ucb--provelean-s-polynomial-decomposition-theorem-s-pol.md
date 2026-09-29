---
# qou-8ucb
title: 'PROVE(lean): s_polynomial_decomposition — theorem s_polynomial_decomposition (a₁ a₂ c₁ c₂ : k) (f₁ f₂ : AlgElement G k) (ha₁ : a₁ ≠  [cited manuscript]'
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

**File:** `UGB/UnitalGroebner/s_polynomial_decomposition.lean` (UGB)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/unital-groebner-bases/lean/UGB/UnitalGroebner/s_polynomial_decomposition.lean

### `s_polynomial_decomposition`  —  line 71  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem s_polynomial_decomposition (a₁ a₂ c₁ c₂ : k) (f₁ f₂ : AlgElement G k) (ha₁ : a₁ ≠ 0) (ha₂ : a₂ ≠ 0) (hcancel : c₁ * a₁ + c₂ * a₂ = 0) : ∃ d : k, AlgElement.add (AlgElement.smul c₁ f₁) (AlgElement.smul c₂ f₂) = AlgElement.smul d (sPolynomial a₁ a₂ f₁ f₂) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] unital-groebner-bases/unital-groebner-bases-chapter/s-polynomial-decomposition.ts
  - [manuscript] unital-groebner-bases
- **Tractability:** S-polynomial decomposition (unital); repo GS/Buchberger infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
