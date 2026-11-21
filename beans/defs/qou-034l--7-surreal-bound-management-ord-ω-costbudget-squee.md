---
# qou-034l
title: '#7 surreal bound-management: ord_ω cost/budget squeeze — grade algebra (super-poly ≻ poly, stable under +,·,∘)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T10:28:35Z
updated_at: 2026-11-21T12:48:00Z
parent: qou-b1je
---

## Round 85 Progress (`litlfred/qou#8312`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/SurrealGradeSqueezeAndBarChainTorsionBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all 7 static audits).
- **80-dps Probe & Witness**: `computations/probes/surreal_grade_squeeze_and_bar_chain_torsion_brick_probe.py` & `computations/probes/surreal-grade-squeeze-and-bar-chain-torsion-brick.witness.json` (`scriptCommitSha = 97adfc3139b01f6834713637c8c180e84b157659`, HEAD `788d96d10c679066e399232d2279c6981861a63b`, `allPassed = true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8312, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.


## 2026-11-21T12:18:03Z — grade algebra complete under +, ·, ∘ (pnp-collatz drain, https://claude.ai/code/session_01Qmmkt4pcG1jyT27PJvFyQ3)

Superseded-premise check (owner request 2026-11-21): none used; pure complexity / growth-order mathematics.

The body's only progress entry points at closed batch PR #8312. Here is what is actually on main:
- The squeeze `not_polyBounded_of_superPoly` (`QOU/Information/SurrealBudgetGrade.lean`, commit d339df7c39).
- `+` and `·` closure on the constant-safe class `PolyGrowth` (`QOU/Information/PolyGrowthAlgebra.lean`: `add`, `mul`, `PolyGrowth.mono`).

Branch `claude/pnp-surreal-grade-comp-2026-11-21` (commit `819da5b7f`, additive only) adds three results:
- `PolyGrowth.comp`: the budget grade is closed under composition.
- `superPolynomial_not_stable_under_precomp`: the super-poly grade is **not** closed under precomposition (2ⁿ after the constant 0). So the title's "stable under ∘" is true for the budget side only, and false as stated for the super-poly side.
- `polyGrowth_iff_not_superPolynomial`: the exact De Morgan dual. `PolyBounded` is not the dual, despite its docstring: `n ↦ n+1` is neither.

All three: lean exit 0, axioms [propext, Classical.choice, Quot.sound]. Complete this bean when that PR merges.

2026-11-21: PR #8844 merged. PolyGrowth.comp (poly stable under composition), superPolynomial_not_stable_under_precomp (the "∘" half of the title is false for super-poly in general, proved), polyGrowth_iff_not_superPolynomial. Sorry-free, standard axioms.
