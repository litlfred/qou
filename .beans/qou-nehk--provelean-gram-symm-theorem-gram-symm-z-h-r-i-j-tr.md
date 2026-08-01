---
# qou-nehk
title: 'PROVE(lean): gram_symm — theorem gram_symm (z h : R) : ∀ i j, trM z h (mulNF h (e i) (e j)) = trM z h (mulNF h (e j [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-08-01T23:31:06Z
parent: qou-k1mq
---

**File:** `QOU/Machinery/MarkovTraceH4.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceH4.lean

### `gram_symm`  —  line 185  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem gram_symm (z h : R) : ∀ i j, trM z h (mulNF h (e i) (e j)) = trM z h (mulNF h (e j) (e i)) `
- **Cited:** `[manuscript]`
  - [manuscript] §mass-theory
- **Tractability:** trM(ab)=trM(ba) cyclicity over the H4 normal-form multiplication; concrete algebra, heavy but repo-internal (candidate decide/ring).
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
