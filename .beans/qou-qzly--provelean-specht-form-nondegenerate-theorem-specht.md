---
# qou-qzly
title: 'PROVE(lean): specht_form_nondegenerate — theorem specht_form_nondegenerate {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) (hμ [cited sagan2001]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-sagan2001
created_at: 2026-08-01T23:31:03Z
updated_at: 2026-08-01T23:31:03Z
parent: qou-k1mq
---

**File:** `QOU/BraidKnot/SpechtIrreducible.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtIrreducible.lean

### `specht_form_nondegenerate`  —  line 740  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem specht_form_nondegenerate {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) (hμ : μ.card ≠ 0) : SpechtSubmodule (k := k) μ ⊓ spechtPerp (k := k) μ = ⊥ `
- **Cited:** `[sagan2001]`
  - [sagan2001] Sagan (2001), *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* — (no DOI/URL)
- **Tractability:** Gram form nondegenerate in char 0 (S^μ ∩ perp = ⊥); repo route via ℤ Gram of standardBasis + char-0 base-change corank.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
