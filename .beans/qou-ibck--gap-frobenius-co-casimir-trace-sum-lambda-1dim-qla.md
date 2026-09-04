---
# qou-ibck
title: 'GAP: Frobenius co-Casimir trace sum_lambda 1/dim_q(lambda) has no formalised closed form for n >= 6 (UnifiedKnotMass.coCasimirTrace unconstrained there)'
status: todo
type: task
tags:
    - lean
    - gap
created_at: 2026-09-03T09:08:30Z
updated_at: 2026-09-03T09:08:30Z
parent: qou-ggdk
---

Class B (open Lean work) gap (SM-surface Lean sweep, bean qou-08zf, 2026-09-03). mass-theory/knot-mass-formula-unified.lean now defines partitionInverseDimSum q n as the sum of 1/dim_q over explicit q-hook dimensions (qHookDims, labelled by partition) and PROVES the closed forms for n = 2, 3, 4, 5 (previously match-arms read back by rfl — "an axiom relocated, not discharged", audit docs/audits/2026-08-27-unified-knot-mass-class-is-unsatisfiable.md). For n ≥ 6 the previous code returned (n : ℝ) under a docstring saying 0; it is now an unconstrained structure field, with coCasimir_small_n : n ≤ 5 → coCasimirTrace = partitionInverseDimSum q n.

OPEN: the partition sum for n ≥ 6 — either (a) a Fin-enumeration of the p(n) partitions with q-hook dimensions (p(6)=11, p(7)=15, p(8)=22, p(10)=42), or (b) the Hecke/Bratteli recursion route via constructive Markov-trace existence (still sorry-blocked in wedderburn-bratteli-recursion.lean). Also open: a real Lean edge between the qHookDims list and frobenius-codim-universal.lean's heckeH{n}DimQ (chapter siblings cannot import each other, so the cross-validation is by eye). Related: qou-7ase (the pinned-stub defect is addressed by this sweep; the parent should close it).
