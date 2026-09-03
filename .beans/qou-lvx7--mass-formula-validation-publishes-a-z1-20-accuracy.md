---
# qou-lvx7
title: mass-formula-validation publishes a Z=1-20 accuracy table at status:verified with NO producer that can make it
status: in-progress
type: bug
priority: normal
created_at: 2026-08-30T08:08:02Z
updated_at: 2026-09-03T20:34:57Z
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


## Addressed in PR #6532 (branch claude/mass-formula-validation-scope-2026-09-03)

Both halves done as the bean specified, and the one thing it forbade was
not done.

**1. False producer attribution removed.** `computation` is OPTIONAL on
`remark` and other observation blocks omit it, so the honest form was to
delete the block rather than downgrade the status of a producer that was
never the producer. Provenance moved to `authorNotes` per §4d, including
the bean's own UNDETERMINED list verbatim: whether 0.04 % is wrong, whether
it is convention-C, and where it came from are all open, and absence of a
producer is not evidence about a convention. The figure is LEFT STANDING.

**No producer written**, per the bean's explicit prohibition.

**2. A second defect, not in the original bean.** `Delta/M` in Table 5
divides by the ATOMIC MASS, which the 2026-08-11 owner ruling (`qou-exam`)
excised as a prediction target — absolute mass is `m_e` x ratio and `m_e`
fixes the MeV scale by fiat. So the table divides a binding-scale residual
by a nucleon-scale mass and the percentage is small for that reason.

Computed from Table 5's own Delta against AME2020 binding:

    4He  +0.079  0.002 %   B 28.296  ->  0.28 %
    6Li  +2.191  0.039 %   B 31.995  ->  6.85 %
    7Li  +1.740  0.027 %   B 39.245  ->  4.43 %
    9Be  +1.234  0.015 %   B 58.165  ->  2.12 %
    10B  +0.648  0.007 %   B 64.751  ->  1.00 %
    12C  +0.618  0.006 %   B 92.162  ->  0.67 %

**6Li — the row the 0.04 % bound is tightest against — is 6.85 % of the
binding it is meant to reproduce. A factor of 176.** This does NOT show the
0.04 % figure is wrong (still undetermined); it shows the bound is a claim
about the denominator as much as about the formula.

**1H is not an accuracy result at all**: free nucleon, no binding energy
(Table 1 says so), so its 1e-6 % is the `m_e` scale returning what was put
in — the same round-trip the per-observable dashboard excludes `m_p` for.

## Verification

Render-QA battery clean; manifest imported under bun (builds, `computation`
absent, 2 authorNotes); `check-sidecars.sh` clean.
**`run-validate.ts` could not run** — `Cannot find module
'.../references-registry-di'`, identical with the changes stashed, so a
pre-existing qou/platform version skew, not this change. Reported as
un-run rather than as green.
