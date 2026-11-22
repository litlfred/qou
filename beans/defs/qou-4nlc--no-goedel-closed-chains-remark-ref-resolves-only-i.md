---
# qou-4nlc
title: 'no-goedel-closed-chains-remark: ref resolves only into another block''s sibling'
status: in-progress
type: task
priority: low
tags:
    - lean
created_at: 2026-11-22T09:20:31Z
updated_at: 2026-11-22T09:50:00Z
parent: qou-uwyf
---

QOU.word_no_closedChainAt is declared in quantum-observable-universes/braiding-induced-ordering.lean, a different block's sibling. Either move the theorem into the library (lean/QOU/...), give the block its own sibling, or let the resolver follow uses[] siblings.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.

## 2026-11-22 finding (thread "Pick Lean refs for TLIsXXZChain and remark")

The remark only interprets lem:crossing-application-chains (its .ts comment says so). The library file QOU/QuantumObservableUniverses/NoClosedCausalChains.lean holds parts (b) `not_closedChainAt_tick`, (c) `closedChainAt_of_pow_eq_one` / `_of_sq_eq_one`, and the B_n / S_n examples; part (a), words, exists only as `QOU.word_no_closedChainAt` in braiding-induced-ordering.lean. 1037 of 1084 remarks carry no lean ref. Options put to owner: drop the remark's ref (recommended), repoint to the lemma's ref, or add a word-case theorem to the library and point there. Awaiting owner pick.
