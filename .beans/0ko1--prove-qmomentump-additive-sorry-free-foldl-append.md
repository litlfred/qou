---
# 0ko1
title: Prove qMomentumP_additive sorry-free (foldl_append + induction)
status: todo
type: task
priority: normal
tags:
    - compute-wiring
    - tractable-lean
created_at: 2026-07-06T04:31:27Z
updated_at: 2026-07-06T04:31:27Z
---

Swarm triage (high conf): prop:q-momentum-properties Lean QMomentumProperties.lean has a sorry on qMomentumP_additive. Provable sorry-free via List.foldl_append + an induction lemma pulling the initial accumulator out (tactics: induction on the list, add_assoc/add_zero). A sorry-free proof makes the compute probe redundant (checker exemption). Needs Lean toolchain to verify.
