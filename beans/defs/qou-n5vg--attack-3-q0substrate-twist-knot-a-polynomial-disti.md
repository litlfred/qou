---
# qou-n5vg
title: 'ATTACK #3: q0/substrate <- twist-knot A-polynomial distinguished point (Subgoal-2 geometric); Takata+Garoufalidis'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T00:19:26Z
updated_at: 2026-11-22T21:33:11Z
parent: c7vs
---

## Round 73 Progress (`litlfred/qou#8257`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/HabiroCyclotomicRecurrenceAndHopfCSBrick.lean` (`twist_knot_distinguished_trace_field_quadratic_lock`)
- **Summary**: Proved distinguished `4_1` twist-knot trace specialization at `s^2 = 3`: root pair `(2 + s, 2 - s)` has trace `4`, reciprocal norm `1`, and quadratic discriminant `12`.
- **80-dps Probe & Witness**: `computations/probes/habiro_cyclotomic_recurrence_and_hopf_cs_brick_probe.py` -> `computations/probes/habiro-cyclotomic-recurrence-and-hopf-cs-brick.witness.json` (`scriptCommitSha: aee44290d86add18624df3d3bce0a730246dc422`, PR head `eb8e68feba9367aa951532accb9ea1ab3a723c3a`)
- **PR**: https://github.com/litlfred/qou/pulls (`status: in-progress` pending merge)

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

No change. The latest note above points at batch PR #8257, which is still open and unmerged; its theorems are short algebraic identities with the bean's quantities as free variables, and they do not bear on this bean's question. Treat this bean's state as what the earlier text says.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: SUPERSEDED-BY.** SUPERSEDED-BY the forever-gate on substrate-q₀ derivation (owner ruling 2026-08-02, AGENTS.md §Precision goals Subgoal-2, bean qou-eic1). This bean (created 2026-07-19) is an attack on deriving q₀ from the 4₁/twist-knot A-polynomial distinguished point, which is now a forbidden route in any form. The pure-algebra fact in the Round 73 note (trace 4, norm 1, discriminant 12 at s² = 3) needs no bean and is on unmerged batch PR #8257 only. Scrapped; reopen only if the owner lifts the gate.
