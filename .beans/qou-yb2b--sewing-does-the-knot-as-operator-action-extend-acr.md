---
# qou-yb2b
title: 'Sewing: does the knot-as-operator action extend across the complement, or degenerate there?'
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:23:16Z
updated_at: 2026-09-04T09:24:02Z
---

THE OWNER'S ASK, verbatim (2026-09-04): "remember the knots themselves are operators and sewing should be able to extend the not actions to the knot compliment, or show that they degenerate there."

MEASURED, and it is beaned NOWHERE. content/ 0, docs/ 0, .beans/ 0 for 'sewing' and 'sewn'; 0/1/0 for 'extend.*action.*complement'; 0 everywhere for 'gluing axiom'. Checked under other vocabulary in case the concept is present differently: TQFT 28/46/6, Turaev 76/58/15, cobordism 8/3/1 - so the ambient literature IS represented and the specific move is not.

THE OPERATOR SIDE EXISTS. braids-and-knots/fundamental-knots-operator-basis.md plus six siblings state knots as operators. What is missing is the EXTENSION: no artifact anywhere asks whether that action extends across S^3 minus K, or degenerates on the exceptional divisor.

WHY TWO SWEEPS MISSED IT. The citation inventory looks for a claim whose source does not carry it; the Mathlib inventory looks for an API that does not exist. This is neither - a mathematical question nobody has asked in a durable artifact has no citation to be wrong and no API to be absent. A gap with no artifact is invisible to an artifact-scanning sweep.

WHAT WOULD SETTLE IT, in the order that costs least:
1. State the question. Which operator, acting on what, and what 'extends' means - a functor out of a cobordism/tangle category, or a module structure on something attached to the complement. There is no statement yet, so there is nothing to prove or refute.
2. Check the degenerate branch FIRST. HyperbolicVolumeFormType already proves S^3_Reeb is simply connected and carries no complete hyperbolic metric, and the round geometry on the exceptional divisor is proved. If the action degenerates there, that is the cheaper and possibly the true answer, and it is close to results already in hand.
3. Only then the extension. Turaev/TQFT machinery is the natural home and the library holds it (76 Turaev hits) - but note qou-52fu: the complement's hyperbolic holonomy is PSL(2,C), rank 1, so an extension route that lands back in SL(2) does not reach the eightfold.

DO NOT start by building infrastructure for it. The gap is a missing STATEMENT, not a missing API.

Roast: docs/audits/2026-09-04-roast-of-the-two-inventories.md R1.
