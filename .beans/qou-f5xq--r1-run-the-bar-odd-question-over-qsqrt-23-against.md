---
# qou-f5xq
title: 'R1: run the bar-odd question over Q(sqrt-23) against the A6 sigma-pair tower (SHAPE only — value is q0-gated)'
status: todo
type: task
created_at: 2026-08-19T13:37:31Z
updated_at: 2026-08-19T13:37:31Z
---


## Answered: NEGATIVE (scope-(a))

Ran the bar-odd question over Q(sqrt-23) against the A6 tower, scoped to SHAPE
(no value; q0 gate respected).

**Question.** The corpus shows the odd projection lands ON the sqrt(-23) line.
Does it also land LOWER -- i.e. is the odd channel 23-adically shallower than
the element it came from? A shallower odd part would be a real lever: a bar-odd
closed form with smaller denominators is easier to identify.

**Measured, exact rational arithmetic, 24 orders.** Depth of the odd part
min(v23(u),v23(v)) vs depth of the full element min(v23(a),v23(b),v23(c)):
EQUAL at 24 of 24. Never shallower. Max deviation 0.

**Verdict.** The sqrt(-23) line is special in DIRECTION, not in SIZE. Rules out
the "restricting to the line simplifies the arithmetic" hope. Does NOT claim no
bar-odd closed form exists (that would need a proved invariant, scope-(b)), and
computes no value.

## Method note -- I got this wrong on the first pass

My exploratory read called k=14 and k=24 exceptions. Wrong: it compared
valuations COMPONENTWISE, where a_k and c_k do sit one power of 23 apart at
those orders. Depth is the MINIMUM over components, and under the minimum they
agree everywhere. Caught by writing the probe properly rather than trusting the
eyeball pass; the docstring and audit both record the correction.

Generalises: a quantity defined as an extremum over components is not tested by
comparing the components. Reading it the other way turned a clean 24/24 into a
spurious pair of exceptions and would have invited a hunt for a pattern that is
not there.
