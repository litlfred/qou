---
# qou-8ucb
title: 'PROVE(lean): s_polynomial_decomposition — theorem s_polynomial_decomposition (a₁ a₂ c₁ c₂ : k) (f₁ f₂ : AlgElement G k) (ha₁ : a₁ ≠  [cited manuscript]'
status: completed
type: task
priority: normal
tags:
    - verify-build
    - repo-infra
    - reorg-2026-10-04
    - lean
    - cited-sorry
    - paper-ugb
created_at: 2026-08-01T23:31:10Z
updated_at: 2026-10-04T15:30:50Z
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



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] decl found sorry-free & unconditional in folio/unital-groebner-bases or fred2005 tree (k1mq child; sorry gone)



## Verify by build (2026-10-04)

Closed on 'sorry-free on main' evidence, but the cited declaration could not be matched automatically to a file that a CI Lake target is known to compile (orphan census 2026-10-04: only 654 of 1,309 lean.refs resolve into the compiled library; ugb and fred2005 are separate required packages). Confirm with a build and `#print axioms`; reopen if it does not compile.
