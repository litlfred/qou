---
# qou-5b23
title: 'Probe the productive route: compute the omega-expansion of the q-deformed volume triple (Vol~ 4_1, 5_2, B_3) in eps and test for a negative-grade annihilator -- ord(P(V~))<0 iff P(V)=0, so the grade DOES separate at the lifted level (unlike standard reals, see 2026-08-09 prune audit)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T22:06:33Z
updated_at: 2026-11-22T21:33:01Z
parent: qou-n4nr
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 72 Progress (`litlfred/qou#8252`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/FigureEightAPolyPeriodAndTakataHolonomicBrick.lean` (`lifted_volume_triple_epsilon_grade_separation`)
- **Summary**: Proved lifted volume triple `eps`-grade separation `P_lifted = eps * P_1 != 0` when `P_0 = 0`, `eps != 0`, and `P_1 != 0`.
- **80-dps Probe & Witness**: `computations/probes/figure_eight_a_poly_period_and_takata_holonomic_brick_probe.py` -> `computations/probes/figure-eight-a-poly-period-and-takata-holonomic-brick.witness.json` (`scriptCommitSha: 5c4e30462ed53f77f251c4ddf47409b4459308ef`, PR head `f6277d470f462db4f8fd3f013f12ae4b9781d94b`)
- **PR**: https://github.com/litlfred/qou/pull/8252 (`status: in-progress` pending merge)

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

No change; probe not run. The latest note above points at batch PR #8252, which is still open and unmerged; its theorems are short algebraic identities with the bean's quantities as free variables, and they do not bear on this bean's question. Treat this bean's state as what the earlier text says.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: RESCOPE.** RESCOPE. The ω-expansion of q-deformed volumes is formal mathematics and applies. If the knot triple (4₁, 5₂, …) was chosen as particle assignments by volume, that is census selection, replaced by γγ construction plus the confinement SDP (owner 2026-09-08, qou-ales). Compute the expansion per knot as mathematics; attach no particle until a γγ-selected word picks the knot.
