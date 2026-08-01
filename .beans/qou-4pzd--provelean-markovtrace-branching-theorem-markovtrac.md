---
# qou-4pzd
title: 'PROVE(lean): markovTrace_branching — theorem markovTrace_branching : markovTrace = (Finset.range nPartitions).sum (fun l => mar [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
created_at: 2026-08-01T23:31:04Z
updated_at: 2026-08-01T23:31:04Z
parent: qou-k1mq
---

**File:** `QOU/FeynmanPathIntegrals/markov_identification.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/FeynmanPathIntegrals/markov_identification.lean

### `markovTrace_branching`  —  line 88  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem markovTrace_branching : markovTrace = (Finset.range nPartitions).sum (fun l => markovWeight l * spechtPartialTrace l) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] lem:feynman-markov-identification
- **Tractability:** markovTrace = Σ markovWeight·spechtPartialTrace; repo Hecke/Markov-trace branching.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
