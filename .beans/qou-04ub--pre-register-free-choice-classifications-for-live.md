---
# qou-04ub
title: Pre-register free-choice classifications for live open binding candidates, before outcomes
status: todo
type: task
priority: normal
created_at: 2026-08-27T06:16:28Z
updated_at: 2026-08-27T13:04:32Z
---

AMENDMENT 1 (same day, before any outcome): the SU(4) call OVER-CLAIMED and is corrected in a NEW dated file, not by editing the registry.

I classified su4-supermultiplet as 'the sharpest entry ... refutable in one measurement' from a one-line summary in an audit doc. The primary source, SU4SupermultipletGate.lean, proves Nat.choose 4 A = 0 <-> 4 < A via Nat.choose_eq_zero_iff -- binomial arithmetic, no nucleon, no braid, no q0. The vanishing is ANALYTIC; confirming it confirms arithmetic. The gate's own docstring already said it 'predicts the A=4 locality ALREADY MEASURED' (2.09x at 4He, ~0.94 by 6Li) -- postdiction, labelled at source, and my entry lost the label.

Effect on the rule: both halves hold (no free choice; definite prediction). What fails is a step I silently added -- that definite implies INFORMATIVE. The prediction holds for ANY C(4,A)-dimensional object, so it discriminates nothing. This is a THIRD failure mode I did not register: a choice-free candidate whose definite prediction is ANALYTIC rather than synthetic. The rule needs a second question after 'is a choice left unfixed?': 'could the prediction have come out otherwise, given the specification?'

Process error named: classified from a secondary summary with the primary source one grep away. Surfaced in under an hour -- the pre-registration working. Retrospective scoring would have logged 'testable, confirmed' and learned nothing.

Registry untouched, outcome still null, guard still green. PR #5877.
