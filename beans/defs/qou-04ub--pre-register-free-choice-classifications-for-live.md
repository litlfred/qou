---
# qou-04ub
title: Pre-register free-choice classifications for live open binding candidates, before outcomes
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-27T06:16:28Z
updated_at: 2026-10-04T15:22:09Z
parent: qou-v2om
---

AMENDMENT 1 (same day, before any outcome): the SU(4) call OVER-CLAIMED and is corrected in a NEW dated file, not by editing the registry.

I classified su4-supermultiplet as 'the sharpest entry ... refutable in one measurement' from a one-line summary in an audit doc. The primary source, SU4SupermultipletGate.lean, proves Nat.choose 4 A = 0 <-> 4 < A via Nat.choose_eq_zero_iff -- binomial arithmetic, no nucleon, no braid, no q0. The vanishing is ANALYTIC; confirming it confirms arithmetic. The gate's own docstring already said it 'predicts the A=4 locality ALREADY MEASURED' (2.09x at 4He, ~0.94 by 6Li) -- postdiction, labelled at source, and my entry lost the label.

Effect on the rule: both halves hold (no free choice; definite prediction). What fails is a step I silently added -- that definite implies INFORMATIVE. The prediction holds for ANY C(4,A)-dimensional object, so it discriminates nothing. This is a THIRD failure mode I did not register: a choice-free candidate whose definite prediction is ANALYTIC rather than synthetic. The rule needs a second question after 'is a choice left unfixed?': 'could the prediction have come out otherwise, given the specification?'

Process error named: classified from a secondary summary with the primary source one grep away. Surfaced in under an hour -- the pre-registration working. Retrospective scoring would have logged 'testable, confirmed' and learned nothing.

Registry untouched, outcome still null, guard still green. PR #5877.

### Progress (Round 72 — PR litlfred/qou#8311)
- Formalized in PR `litlfred/qou#8311` (`feat/round72-su4gate-markovzd-interface-vassiliev-lever1-43c1`, Commit 1 `120f8595e20646e98de0e5ba129245b973aa1574`, Head `be2282b84c903a928b1e78fc59abcd496c8ceea5`, `scriptHash: 3cfc48bf2b24`).
