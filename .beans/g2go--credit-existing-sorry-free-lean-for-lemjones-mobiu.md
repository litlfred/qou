---
# g2go
title: Credit existing sorry-free Lean for lem:jones-mobius-diagonal (checker false-negative)
status: todo
type: task
priority: normal
tags:
    - compute-wiring
    - tractable-lean
created_at: 2026-07-06T04:31:26Z
updated_at: 2026-07-06T04:31:26Z
---

Swarm triage: the block's lean.ref (qou:QOU.Braiding.JonesMobiusDiagonal.markov_eq_mobius_contact) resolves to an EXISTING sorry-free §3b-cond proof, but compute-prop-has-probe/-consumer false-flag NOT-WIRED (no sibling .lean + lean.validation:not_checked; resolveCanonicalLean/library-decl not credited by the compute checkers). Fix: make the compute-prop checkers credit the resolved library .lean (or set lean.validation), then re-sweep. DO NOT add a numeric probe (Mobius-kernel diagonal compute is not written down). No fabrication.
