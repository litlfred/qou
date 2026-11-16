---
# qou-ibck
title: 'GAP: Frobenius co-Casimir trace sum_lambda 1/dim_q(lambda) has no formalised closed form for n >= 6 (UnifiedKnotMass.coCasimirTrace unconstrained there)'
status: in-progress
pr: 8183
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-lean
    - lean
    - gap
    - 8f-open
created_at: 2026-09-03T09:08:30Z
updated_at: 2026-10-10T07:56:51Z
parent: qou-8lxd
---

Class B (open Lean work) gap (SM-surface Lean sweep, bean qou-08zf, 2026-09-03). mass-theory/knot-mass-formula-unified.lean now defines partitionInverseDimSum q n as the sum of 1/dim_q over explicit q-hook dimensions (qHookDims, labelled by partition) and PROVES the closed forms for n = 2, 3, 4, 5 (previously match-arms read back by rfl — "an axiom relocated, not discharged", audit docs/audits/2026-08-27-unified-knot-mass-class-is-unsatisfiable.md). For n ≥ 6 the previous code returned (n : ℝ) under a docstring saying 0; it is now an unconstrained structure field, with coCasimir_small_n : n ≤ 5 → coCasimirTrace = partitionInverseDimSum q n.

OPEN: the partition sum for n ≥ 6 — either (a) a Fin-enumeration of the p(n) partitions with q-hook dimensions (p(6)=11, p(7)=15, p(8)=22, p(10)=42), or (b) the Hecke/Bratteli recursion route via constructive Markov-trace existence (still sorry-blocked in wedderburn-bratteli-recursion.lean). Also open: a real Lean edge between the qHookDims list and frobenius-codim-universal.lean's heckeH{n}DimQ (chapter siblings cannot import each other, so the cross-validation is by eye). Related: qou-7ase (the pinned-stub defect is addressed by this sweep; the parent should close it).


## Triaged 2026-10-10 — OPEN Lean work, not mechanical; tagged `8f-open`

Read as part of working the `8f-lean` front. This is the bean's own
"Class B (open Lean work)" and it is correctly that: closing it needs either
(a) a `Fin`-enumeration of the `p(n)` partitions with q-hook dimensions
(`p(6)=11`, `p(7)=15`, `p(8)=22`, `p(10)=42`) or (b) the Hecke/Bratteli
recursion route, which is **still sorry-blocked** in
`wedderburn-bratteli-recursion.lean`. Neither is a repair; both are formalisation.

**Its one actionable sub-item is already done.** The body says *"Related:
`qou-7ase` (the pinned-stub defect is addressed by this sweep; the parent should
close it)."* Checked: **`qou-7ase` is already `completed`.** Nothing to do, and
recorded here so the next reader does not chase it.

Still genuinely open, unchanged: the `n >= 6` partition sum, and the absent Lean
edge between `qHookDims` and `frobenius-codim-universal.lean`'s `heckeH{n}DimQ` —
chapter siblings cannot import each other, so that cross-validation is by eye.

## Progress Update (Round 54 — PR #8183)
- [x] Formalized non-vacuous Lean 4 theorems (`0` `sorry`, `0` vacuity candidates across all 4 static audits) in `folio/quantum-observable-universe/lean/QOU/Eightfold/CoCasimirFigureEightAndGenerationCompleteness.lean` and wired into `QOU.lean`.
- [x] Added 50-dps `mpmath` probe `computations/probes/co_casimir_figure_eight_and_generation_completeness_probe.py` and 2-commit stamped witness `computations/probes/co-casimir-figure-eight-and-generation-completeness.witness.json` (`scriptCommitSha: 0a9a3d4c2110ac1fe5749fd28e2cb610a48c9e50`, `HEAD: 531c8d4812e2909b18a4bc18eeba6be23a873d7f`).
- [x] Opened `litlfred/qou#8183` (status kept at `in-progress` per no-unilateral-closure policy).
