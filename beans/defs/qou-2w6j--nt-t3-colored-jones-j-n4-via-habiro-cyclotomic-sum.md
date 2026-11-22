---
# qou-2w6j
title: 'NT-T3: colored Jones J_N(4₁) via Habiro cyclotomic sum in Lean + prove its order-2 inhomogeneous recurrence (q-WZ certificate identity, pure algebra)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T03:21:57Z
updated_at: 2026-11-22T21:33:11Z
parent: c7vs
---

## Round 73 Progress (`litlfred/qou#8257`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/HabiroCyclotomicRecurrenceAndHopfCSBrick.lean` (`habiro_cyclotomic_one_step_inhomogeneous_recurrence`)
- **Summary**: Proved order-2 inhomogeneous recurrence certificate `J^{(1)}(u_{N+1}, c1) - t * J^{(1)}(u_N, c1) + J^{(1)}(u_{N-1}, c1) = (2 - t) * (1 + 2 * c1)` under the Chebyshev step `u_{N+1} + u_{N-1} = t * u_N`.
- **80-dps Probe & Witness**: `computations/probes/habiro_cyclotomic_recurrence_and_hopf_cs_brick_probe.py` -> `computations/probes/habiro-cyclotomic-recurrence-and-hopf-cs-brick.witness.json` (`scriptCommitSha: aee44290d86add18624df3d3bce0a730246dc422`, PR head `eb8e68feba9367aa951532accb9ea1ab3a723c3a`)
- **PR**: https://github.com/litlfred/qou/pulls (`status: in-progress` pending merge)

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

Check against `main`: `BraidKnot/AJFigureEightAnnihilation.lean` `figureEightOperator_annihilates` proves the order-2 inhomogeneous recurrence for the whole colored Jones tower `coloredJones41` ("`N = 0` direct; `N ≥ 1` the division-free certificate telescope"). If its `#print axioms` is clean and `coloredJones41` is the Habiro cyclotomic sum, this bean is done; verification pending (Lean toolchain setup in this session). The latest note above points at batch PR #8257, which is still open and unmerged; its theorems are short algebraic identities with the bean's quantities as free variables, and they do not bear on this bean's question. Treat this bean's state as what the earlier text says.

## 2026-11-22 — verified, closed

**Closed with evidence.** `BraidKnot/HabiroNewtonLadder.lean` defines `coloredJones41 q N = Σ_{k<N} habiroTerm q N k` (the Habiro cyclotomic sum), and `BraidKnot/AJFigureEightAnnihilation.lean` `figureEightOperator_annihilates` proves the order-2 inhomogeneous recurrence for every `N`. `#print axioms` → [propext, Classical.choice, Quot.sound], checked 2026-11-22 with lean-direct against the restored cache. The Round 73 batch-PR note above (#8257) is unrelated to this result.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: ALREADY-DONE.** Confirmed on review: the result is on main (see the note above) and none of its premises is on the retired list in owner-rulings.md.
