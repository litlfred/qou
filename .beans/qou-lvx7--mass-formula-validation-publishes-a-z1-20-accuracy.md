---
# qou-lvx7
title: mass-formula-validation publishes a Z=1-20 accuracy table at status:verified with NO producer that can make it
status: todo
type: bug
priority: normal
created_at: 2026-08-30T08:08:02Z
updated_at: 2026-08-30T08:08:50Z
---

Surfaced by the qou-zzwm survey (owner question: "investigate 2.4 accuracy
loss -- some other related issues?"). Filed separately because it is a
MISSING-PRODUCER defect, not a convention one.

THE CLAIM: content/quantum-observable-universe/observations/mass-formula-validation.md:41
publishes "all beta-stable nuclei satisfy |Delta/M| < 0.04 %", with a Table 5
spanning 1e-6 .. 0.04 %.

THE PROBLEM: its .ts declares
    script: computations/q_pinning_50_digit.py
    status: "verified"
That script solves for q0 to 50 digits. It cannot produce a mass table, and no
other producer for this block resolves.

WHY IT MATTERS BEYOND BOOKKEEPING: 0.04 % is roughly 5x TIGHTER than the table
this repo just adopted (convention D, mean 0.1827 %, max 0.3214 % over Z=1..20,
PR #6043). Two published accuracy claims about overlapping nuclei differ by 5x
and only one of them has a producer. A reader comparing them has no way to tell
which is current.

NOT ESTABLISHED, do not write it down as if it were: whether the 0.04 % figure
is wrong, whether it is convention-C, or where it came from. It is UNDETERMINED
-- absence of a producer is not evidence about a convention. What IS established
is that status:"verified" is unsupported: nothing in the corpus regenerates it.

HONEST NEXT STEP: either find/write the producer and re-derive the table (then
the status is earned), or downgrade the status and mark the figure as carried
from an unrecoverable prior computation. Do NOT fit a producer to reproduce
0.04 % -- that would be manufacturing provenance for a number whose origin is
unknown, which is worse than the missing producer.
